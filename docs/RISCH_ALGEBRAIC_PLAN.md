# Plan: branch-correct algebraic integration, and correctness testing
against the Rubi corpus

Companion to `RISCH_PLAN.md` (the transcendental Risch plan) and
`BRONSTEIN_ERRATA.md`.  This file covers the experimental algebraic
track on branch `risch-algebraic` and is written to be picked up by a
fresh session.

Status: **both items implemented and corpus-verified** (2026-08-15/16
session); see §6.  Final measurement: the pre-fix branch had 1,705
wrong answers among 4,239 corpus solves (40%); the fixed branch
(`518d57ad37`) has **zero** among 4,287 (net +48 solves, median
per-case time unchanged).  Runs 11-13 in `runs/algebraic-run-log.md`.

**2026-08-21: restacked onto the rde branch-cut fixes.**  The 29
commits since the common base were replayed onto
`risch-rde-cancellation` head `d7dafa43c1` (which carries the
log/exp branch-constant fixes, the restart backsubs fold, and the
#26502 `residue_reduce` gcd_z fix); new head `33e90e420a`,
force-pushed.  Two hand-resolved conflicts: the `__slots__` unions,
and the extension-restart site, which now composes both branches'
fixes -- backsubs are folded into `newf` before `reset()` *except*
the `sign_consts` ratio Dummies, whose mapping is carried across the
reset and re-recorded (their Dummys intentionally stay in `newf`).
`residue_reduce` is the gcd_z version plus the `NotInvertible ->
(H, False)` net, now an invariant check rather than a live fallback.
test_risch/prde/rde/integrals green, mypy/ruff clean.  The branch
stays rebased-as-we-go while experimental (Aaron's call).

**2026-08-20: the type hints moved to `risch-typing` only.**  The
branch stack is `master (d01ca185c7)` -> `risch-typing` ->
`risch-rde-cancellation` -> `risch-algebraic`, and the typing sat at
the *base* of the lower two, so their PR diffs carried it.  Aaron's
call: keep the structural changes where they are, move the type hints
out.  Note `risch-typing` was never purely type hints -- three of its
eleven commits are behavioral and stayed: `77d52c183e` (drops the
`None` sentinel from `exts`/`extargs`, i.e. the indexing convention
every later commit including `_nontrans_power_relations` relies on),
`57ed7463cb` (`as_poly()` -> `Poly()`), and the prde.py edge-case
fixes (`sum(..., S.Zero)`), which were split out of "Typing and
edge-case fixes" and reworded.  A fourth wrinkle: a typing commit had
smuggled `derivation(DE.t, DE)` -> `derivation(Poly(DE.t, DE.t), DE)`
into prde.py; both forms return the identical Poly, so dropping it is
behavior-neutral.  Result: `risch-rde-cancellation` 38 -> 30 commits
(`3c5b649612`), `risch-algebraic` 64 -> 56 (`86883305b3`), both
force-pushed, `_Extension` count zero on both.  Verified the content
diff against the old tips is typing-only, integrals/polytools/
polymatrix tests pass, ruff clean, and the Rubi trinomial pilot is
identical (45 solved, 0 wrong).  Backups:
`backup/risch-rde-cancellation-20260820b`,
`backup/risch-algebraic-20260820`.  The docs fix for the private
alias lives on `risch-typing` (`18c53717fd`), rendering
`handle_first: Literal['exp', 'log']`.

**2026-08-19: CI triage of the flip.**  Four jobs were red on
`27d455752e`; all four are green on upstream master, so each needed
separating.  Two were ours, from the flip, both form-only and fixed
by updating the expectations in `757fa4fa7e`: `test_heurisch_issue_26930`
(`integrate(x**(4/3)*log(x))` keeps the radical outside the Add;
`heurisch()` itself unchanged) and the ODE example
`1st_homogeneous_coeff_best_04` (`checkodesol` verifies both the old
and new solution as `(True, 0)`; the new expectation must be written
with the 2 divided into the radical first, since dsolve builds the
product without distributing it and a natural-order literal
auto-distributes and will not compare equal).  **Build Docs** is not
from the flip: it fails from `346f1bdd87` ("Use Literal types ...")
on `risch-rde-cancellation`/`risch-typing`, where the private
`_Extension` TypeAlias appears in autodoc'd signatures and sphinx
(nitpicky, warnings-as-errors) cannot resolve it -- it has been red
on this branch since well before the flip, and the fix belongs on
that lower branch (`nitpick_ignore` or `autodoc_type_aliases` in
`doc/src/conf.py`).  **mpmath-master Tests** and **Bleeding edge
dependencies** are branch staleness: master fixed the first in
`cdb8ace228` ("don't pass invalid parameter to mpmath.nsum") and our
base predates it; both failures are in stats/matrix code untouched by
integration, and both vanish on a rebase onto current master.

**Output-form data point (deferred item, not applied).**  While
triaging, `expand_mul(powsimp(factor_terms(r), combine='exp'))`
applied to risch results was found to recover the *historical* form
in every case the flip changed -- the two above plus the `sqrt(1+x)`
doctest and issue 4403 -- and to improve others sharply
(`x/sqrt(x**2 - 1)` collapses to `sqrt(x**2 - 1)`).  Spot checks kept
the branch corrections intact (derivative error 0 at the
previously-wrong points; `sign` factors and `sqrt((x + 2/3)**2)` not
collapsed, i.e. powsimp does not perform the unsound
`x/sqrt(x**2) -> 1`).  Aaron's decision (2026-08-19): **do not** add
simplification inside `integrate()`/`risch_integrate()` for now,
beyond what the tower back-substitution already does; change the
tests instead.  Recorded here as the starting point if the
output-form item is picked up later.

**2026-08-20 (later): failing-integrals audit and the degenerate-retry
dead end.**  First-ever run of `test_failing_integrals.py` on the
branch (never checked before; the plan had no record).  Two deltas vs
the branch's own base: `test_issue_11813`
(`integrate(x/sqrt(a - x), (x, 0, a))`) newly passes and its XFAIL is
removed; `test_issue_7147` (`x/sqrt(a*x**2 + b*x + c)**3`) newly
*fails* -- risch runs first, solves the generic branch, and the
`Eq(4*a*c - b**2, 0)` degenerate branch stays an honest unevaluated
Integral, where the pre-flip pipeline's non-risch methods solved every
degenerate case.  The loss is masked in CI (the test was a non-strict
XPASS, still marked XFAIL).  An easy fix was tried and **rejected**:
retrying the embedded degenerate Integrals in `integrals.py` with
`doit(risch=False)` (plus `together()` on the integrand, which the
sub-integrators need) fixes 7147, but the sub-integrators answer
generically, so the degenerate slot gets values wrong at exactly the
parameter values that select it -- `test_issue_2975` gets `nan` at
`C = 0` (the very expectation this branch deliberately changed to an
honest Integral), `test_old_issues` a wrong-sign `-oo`, `test_issue_10211`
`nan` at `y = 0`.  7147 worked only because manualintegrate happened
to do per-case analysis.  A sound retry must validate the candidate on
the degenerate variety -- the deferred special-values problem (§3.2);
do not re-attempt the mechanical version.  `test_issue_16396a` xpasses
on master but not here: fixed on master after our base; a rebase picks
it up.  Slow failing-integrals tests: identical on base and branch;
the three `@tooslow` ones were not run (exp/tan/log, not radical).

**2026-08-21: the guards now decide or degrade over transcendental
towers too** (`15e76e361e`, "Decide or degrade the non-rational
structure-constant guards").  The four remaining `NotImplementedError`
raises (`is_deriv_k`/`is_log_deriv_k_t_radical` non-rational solution,
`parametric_log_deriv_structure` non-rational system,
`parametric_log_deriv` inconclusive) still aborted transcendental
towers, e.g. `risch_integrate(2**log(x)/x**2, x)` (any power base
that isn't `E`).  Two-tier replacement: (1) a *unique* structure
solution with a provably irrational entry (`is_rational is False`,
e.g. `log(2)`) is a proven "no relation" -- `_structure_system_solve`
now returns a uniqueness flag -- so `2**log(x)` towers stay proven
transcendental at full power; (2) genuinely undecided cases
(`log(3)/log(2)` for `2**x + 3**x`, symbolic constants, zeroed free
parameters, `parametric_log_deriv` inconclusive) answer "no relation"
and set `DE.transcendental = False`, reusing the degradation/vetting
machinery (which handles towers with no algebraic generators fine:
`_nontrans_power_relations` is empty, the kernel test reduces to
`cancel == 0`).  `DE.transcendental` semantics are now "proven purely
transcendental".  Validation: Hebisch 400-case spot check 365 -> 368
solved (the 3 new = former aborts with `exp(5)`, `exp(4)*log(2)`,
`log(log(12))` constants), all proven, rest unchanged modulo one
equivalent constant factoring and borderline 5 s timeouts; Blake
1,500-case sweep unchanged (303 solved both sides, identical
results).  `test_integrate_returns_piecewise` (issue 23707,
`exp(t)*exp(-t*sqrt(x - y))`) updated: risch now answers instead of
the fallback integrators, so the degenerate `x == y + 1` slot is an
honest Integral (the deferred special-values problem, same as the
7147 class).  Known remaining gap, deliberately out of scope: a
constant irrational *exponent* on a variable base (`x**log(2)`,
`x**pi`) is never swept into `pows` (risch.py `_rewrite_exps_pows`
filter requires the exponent to involve the tower), so those still
fail tower construction as before -- the fix would be to rewrite
`x**c -> exp(c*log(x))` for constant non-rational `c`.

**2026-08-21 follow-up** (`3b072169b7`, "Gate _exp_part's radical
restart on actual algebraic generators", from the roborev finding on
the previous commit): `_exp_part`'s restart-versus-adjoin choice for
a proven radical relation used `self.transcendental`, so a tower
downgraded by an undecided question adjoined the radical as a
generator with an *unrecorded* relation (invisible to the kernel
checks) instead of restarting to regroup.  New
`DifferentialExtension.algebraic_gens` attribute ("the build is
deliberately erecting algebraic generators", set at the four
construction sites) now gates that choice; `transcendental` keeps
gating proof degradation.  Fixing that exposed a *pre-existing*
restart deadlock: `rad` was written as `exp(arg)**(p/n)` and the
backsubs fold on restart turned the base into `2**x`, leaving
`sqrt(2**x)` that `_rewrite_exps_pows`'s `exp(u)**q` fold never
recognizes -- `2**x + exp(x*log(2)/2 + 1)` failed construction on
all earlier commits.  Exponential radical factors are now folded to
`exp((p/n)*arg)` directly (exact for construction-chosen roots).
Fresh Hebisch 400 spot check vs the previous commit: no behavioral
change (3 borderline-timeout flips on an unloaded run, one
equivalent constant refactoring); Blake unaffected by construction
(algebraic builds never take the restart branch).

**2026-08-21: test coverage for the guard-relaxation commit.**  Two
commits, both pushed: `50e022674e` ("Add tests for the
non-transcendental structure-guard relaxations") and `a3e179745f`
("Remove the XFAIL from test_issue_11813"): unit tests
in `test_prde.py` for three of the four relaxed guards (a tower with
`Dt1 == sqrt(2)/x` makes the structure system solve with the
non-rational constant `1/sqrt(2)`; raise when transcendental, None
when not), an end-to-end `test_risch.py` regression for
`parametric_log_deriv`'s inconclusive case
(`1/(x**2*(x**4 - 1)**(3/4))` from the Blake corpus, derivative
checked numerically), and a Float-skip test.  The `residue_reduce()`
`NotInvertible` fallback is corpus-verified only: a fresh full
3,154-case Blake sweep on the pre-relaxation commit at the
`risch_integrate(f, x)` entry point (`runs/data/pretip-blake-abort-census.jsonl`) found 485
`parametric_log_deriv` aborts, 286 solved, 197 timeouts (8 s) and
**zero** `NotInvertible` -- the 5 crashes recorded in the branch
comparison came through a different entry point (its `i` indices
match neither corpus nor attempted order), and no direct reproducer
is known.  The residual-side leak guard (`2d780558cf`) likewise has
no known reproducer, per its own commit message.  Note the Blake
corpus is all-algebraic: the `risch-algebraic` filter accepts all
3,154 cases, so the earlier "1,500-case" figure must reflect
additional dedupe/filtering in that session's runner.

**Removable singularities: out of scope (decided 2026-08-20).**  The
uncombined forms are `nan` at the roots of the split factors, since
the ratio `original/split` is literally `0/0` there (e.g.
`risch_integrate(sqrt(x**2+2*x+1)/x)` at `x = -1`, limit
`-1 + I*pi`).  Aaron: an expression that is correct in the limit
rather than under direct substitution is not considered a problem,
the general case is much broader than unsimplified
`expr**a/expr**b`, and removing them would need the declined
simplification pass.  Not a defect of this work; do not chase it.

**Historical expectations became XFAILs (`8d4f4a0307`).**  Where the
value a test used to expect turned out to be a *wrong* answer that
meijerint still returns -- issue 5462
(`x/(y**3*sqrt(x**2/y**2 + 1))`, derivative wrong for `y < 0`) and
issue 10211 (`2*sqrt(1 + w**2/h**2)/h - 2/h`, odd in `h` for an
integrand even in `h`) -- risch is only shadowing the bug by running
first.  Those are now `test_meijerg_issue_5462_sign` and
`test_meijerg_issue_10211_sign`, XFAILs against `meijerg=True`, and
the comments about what the tests used to expect are gone (per
Aaron: never comment a test about a previous state of the code).

**2026-08-18 (later): the conds='piecewise' degenerate branches.**
The flip's review chain (jobs 786-791, five commits `80f6c02950` ..
`27d455752e`) converged on the semantics of parameter-degenerate
Piecewise branches for algebraic towers, where the transcendental
`t == 1` fallback is meaningless: for a fully integrated level, the
degenerate branch is `Integral(a/d - i) - ret` (assembles to exactly
the unevaluated rest of the level; the continuing constant stays
outside); for a *partially* integrated level with an undecidable
parametric denominator, the whole level returns unevaluated (no
branch value survives the degenerate substitution -- an intermediate
"formal telescoping" design left two Integrals each divided by the
vanishing parameter); when the denominator provably cannot vanish
there is no branch at all.  En route: a latent Poly-unification
crash in the residual arithmetic (residue dummy in one ground domain
but not the other) fixed by Expr-level arithmetic, and a first
whole-level-fold design rejected for breaking the (ans, i) contract
that lets integrate() retry residuals (20 test regressions, caught
before commit).  The corpus runner now classifies on the generic
branch (`degenerate_unevaluated` flag in the JSONL), since honest
unevaluated degenerate branches otherwise counted verified generic
solves as partial.

**2026-08-18: `algebraic=True` is now the default** in
`risch_integrate()` (Aaron's decision), so plain `integrate()` uses
the towers automatically.  Fallout fixed in the same commit: the
`integrals.py` NonElementaryIntegral stamp now requires a provably
nonelementary leftover (it was overriding the algebraic degradation;
caught via `series()` in test_issue_23942), and split factors are
sign-normalized by their leading coefficient in x (factor() is not
canonical about signs, which made structurally equal radicands under
different symbol names split differently; caught by test_issue_22527).
Test-suite audit of the flip: the integrals package runs in unchanged
time; two historical expected answers turned out to be wrong for
negative parameter values (issues 5462 and 10211 -- sign errors of
the y**3-vs-y**2*Abs(y) kind) and are now correct; the remaining
expectation changes are form-level (uncancelled same-base radical
products, conds Piecewise guards).  The stats test_sample_scipy
failure investigated along the way is an unrelated scipy-version
issue (scipy passes integer arrays to rv_discrete._pmf in some
versions; sympy #26862, scipy #21272) -- decided to ignore.

1. **Correctness testing against the Rubi corpus' expected
   antiderivatives** (Aaron: "Correctness is the most important thing,
   so let's be thorough") -- DONE: numerical oracle in
   `risch_expected_check.py` in the corpus clone, calibrated against
   the known-wrong answers, pilots run; full-corpus audit of the
   pre-fix branch and the post-fix re-sweep in progress.
2. **Branch-correct radicand normalization** -- DONE, with a design
   that supersedes the signum sketch in §4: the split is multiplied by
   an *exact branch-ratio constant* `s = original/split` (locally
   constant, `s**q == 1`), substituted back after integration.  Jump
   corrections (Jeffrey's maximum-extent continuity) are in too, first
   pass: real finite jumps only.

---

## 1. Where things stand

### Branches (SHAs shift under rebases -- match on commit subjects)

- `risch-gaps` -- Phase 0, PR #30180.  Tip at time of writing
  `d01ca185c7`.
- `risch-rde-cancellation` -- Phases 1-4 plus fixes; stacked on
  `risch-gaps`.  Tip `bf88623d8e` ("Rewrite all computable residue
  terms via log_to_real() in the Risch code").  The last three commits
  are Aaron's Rioboo `LogToReal` work (real arc-tangents for
  complex-conjugate residue pairs) -- relevant here, since output form
  and branch behavior interact.
- `risch-algebraic` -- the experimental exp-log-tower representation of
  radicals; stacked on `risch-rde-cancellation`.  Tip `a1c2226052`.
  Nine commits: Aaron's two proof-of-concept commits, repairs, the
  `algebraic=False` gate, the acceptance filter, the radicand
  normalization, and regression tests.

No PRs opened for the latter two branches.  Aaron's rule: keep the
branches sharing identical commits so merged work disappears from the
others; rebase only when necessary.

### What the algebraic mode is

`risch_integrate(f, x, algebraic=True)` represents radicals as exp-log
towers (`sqrt(x)` as `exp(log(x)/2)`), runs the transcendental
machinery over the (non-transcendental) tower, and degrades every
nonelementary conclusion to a plain `Integral`, since those proofs
assume transcendence.  Off by default: ungated tower building sent the
integrals test suite from 90 s to a 10-minute timeout, because
`integrate()` attempts Risch automatically.

Results over the Rubi corpus (~16,800 attemptable radical cases):
about 1,357 integrals solved that non-Risch `integrate()` cannot do,
2,771 solved by both, zero false nonelementary claims.  Timing: solved
cases have a 0.09-0.26 s median; roughly 2% of cases exceed 300 s, all
in bounded-arithmetic sites (no loops).  Full details, per-case tables
and the run log-book: `runs/` in
https://github.com/asmeurer/sympy-risch-notes

### The acceptance filter (already implemented)

`_nontrans_accept()` in `sympy/integrals/risch.py`, called from
`integrate_primitive()` and `integrate_hyperexponential()` when
`not DE.transcendental`.  It accepts a candidate only if

1. `f == D(elem) + D(residue part) + i` holds as a formal
   rational-function identity in the tower generators (decided by
   `cancel()`, on the polynomial representation -- never on the final
   Expr, per Aaron: sympy's Expr-level simplification cannot be
   trusted or afforded for algebraic expressions), and
2. no denominator (of `elem`, `i`, or the residue terms' root
   polynomials and logarithm arguments) lies in the kernel of the
   evaluation map, decided by reduction modulo the tower's power
   relations `t**q == u**p`.

Check 2 was added after a backward-constructed test exposed a real
hole; the corpus never triggers either check (400-case instrumented
sample), so both are covered by constructed tests only.

**Known limitation, and the reason for item 2 below:** the filter
certifies the candidate against the tower image of the integrand *as
the tower builder rewrote it*.  Any rewriting applied before the tower
is built is outside its guarantee.

---

## 2. The open correctness problem

`5779866b43` ("Factor radicands before erecting algebraic tower
generators") factors each radicand and distributes the fractional
power over the factors, so that content like a perfect square does not
become a spurious generator.  Measured benefit: +387 `SOLVED-NEW`
cases corpus-wide (23.2% -> 25.6% overall solve rate).

**This is an algebraic equivalence only where the factors are
positive.**  `sqrt((x+1)**2*(x+2)) -> (x+1)*sqrt(x+2)` drops an
absolute value and has the wrong sign for `x < -1`.  Confirmed
numerically on the current branch:

    risch_integrate(sqrt(x**2 + 2*x + 1)/x, x, algebraic=True)
        -> sqrt(x**2 + 2*x + 1) + log(x) - 1
    at x = -3:  D(answer) = -1.3333  but  f(-3) = -0.6667

and Timofeev's `(x**3 - 5*x**2 + 3*x + 9)**(-2/3)` (radicand
`(x-3)**2*(x+1)`, one of the nine chapter-0 headline solves) is wrong
on all of `x < 3`, returning complex values where the integrand is
real.

Scope of the damage:

- The **core machinery is not affected**.  `exp(log(u)/2)` is
  identically the principal `sqrt(u)` on the cut plane, so the tower
  representation substitutes nothing; core-path answers spot-checked at
  negative and complex points are faithful.  Only the pre-tower
  rewriting is at fault.
- The regression test that pins the normalization uses
  `Symbol('y', positive=True)`, where the collapse *is* sound.  The
  corpus failures are all on assumption-less symbols.
- Continuity is a separate, milder matter: the core path inherits
  sympy's principal-branch conventions (`log` jumps), the same as
  stock `integrate()`.  Aaron's new Rioboo work improves output form
  here.

Interim options considered and rejected: gating the split on provable
nonnegativity is sound but loses essentially all corpus gains (Rubi's
symbols carry no assumptions); keeping generic-only validity
contradicts sympy's assumption discipline.  The signum algorithm below
is strictly better than both.

---

## 3. Item 1: correctness testing against the corpus' expected answers

The corpus is `Upabjojr/rubi-integration-test-suite`, cloned at
`~/Documents/Python/sympy/rubi-integration-test-suite` (a sibling of
the sympy checkout; **not** to be checked into sympy).  Each
`RubiTestSuiteCase` carries `integrand`, `variable`, `num_steps` and
**`integral` -- the expected antiderivative, which we have never
used.**  The runner is `risch_test_suite_runner.py` in that clone,
also proposed upstream as PR #1 there (opened as Claude, per Aaron).

Goal: use `integral` as an oracle to find answers that are *potentially*
wrong, then investigate each.  Our answers legitimately differ in form,
so a mismatch is a signal to investigate, not a verdict.

### 3.1 Comparison ladder

Apply in order; stop at the first conclusive outcome.

1. **Difference is constant.**  `ours - expected` should be constant.
   Test by differentiating and simplifying to zero, on the polynomial
   representation where possible.
2. **Derivative check.**  `D(ours) - f == 0`.  Note this is what the
   internal filter already does at tower level; at Expr level it is
   unreliable for radicals (during this session a correct answer was
   flagged "WRONG" purely because Expr-level zero-testing of a radical
   identity failed -- exactly the reason Aaron insisted the internal
   check stay on the polynomial representation).
3. **Numerical evaluation at many points** -- the decisive test for
   this class of bug, and the one that catches branch errors that
   every symbolic check misses.  Requirements:
   - sample **both signs** of every factor that appears under a
     radical, and points on either side of each real root of those
     factors (the branch bug is invisible if you only sample where
     everything is positive);
   - sample complex points as well as real ones;
   - compare `D(ours)` against `f` pointwise, and separately check
     `ours - expected` is constant across points within a connected
     region;
   - freeze `sign()` factors locally before differentiating (they are
     locally constant; naive differentiation produces `DiracDelta`).

### 3.2 The symbolic-constants caution (Aaron's point)

Rubi's `a, b, c, ...` are pattern variables with **no assumptions**,
whereas real sympy usage substitutes actual numbers.  Both directions
matter and both must be tested:

- **Instantiation testing.**  Replace the symbolic constants with
  random concrete values -- rational and irrational, positive *and
  negative*, and some complex -- then re-run the comparison ladder.
  This is the strongest available oracle: it turns a generically-valid
  formula into a checkable one, and it is precisely how a
  domain-dependent error (a dropped absolute value, a division by a
  constant that vanishes) becomes visible.  Skip instantiations that
  make the integrand degenerate (a denominator identically zero).
- **Assumption sensitivity.**  Run each case with the constants
  assumption-free and again with `positive=True`, and diff the
  outcomes.  Divergence is informative in both directions: it flags
  results that silently depend on assumptions (our normalization is
  sound under `positive=True` and wrong without), and it flags cases
  where sympy refuses to proceed without assumptions.
- **Special values.**  Related to the `Piecewise`/`conds` work already
  documented in `RISCH_PLAN.md` item 6: a result obtained by dividing
  by a symbolic constant is valid only generically.  Instantiating at
  the vanishing values of those divisors is the test for it.

### 3.3 Mismatch taxonomy

Every mismatch should be classified, not just counted:

- our answer genuinely wrong (branch, sign, dropped condition);
- our answer correct, different form (constant of integration,
  algebraically equal, or `log` vs `atan` forms -- especially now that
  Rioboo rewriting is in);
- both correct on different domains (Rubi's conventions are real-
  oriented; sympy's are principal-branch);
- the corpus' own answer questionable (Rubi answers are not immune to
  branch issues, and Rubi's `sqrt` conventions differ from sympy's);
- integrand degenerate under the chosen instantiation.

### 3.4 Deliverables for item 1

- Extend the runner with an `expected`-comparison mode (keep it
  environment-variable driven, as with `RISCH_RESULTS`, `RISCH_MODE`,
  `RISCH_HANDLE_FIRST`, so the CLI stays compatible with the upstream
  runner) and push it to the same PR branch.
- Run it over every case the algebraic mode currently solves
  (~4,100 `SOLVED-NEW` + `SOLVED-both`), and over the transcendental
  chapters as a control -- this re-audits everything already landed,
  including the pre-normalization solves.
- Publish the mismatch table (SymPy expression, our answer, expected
  answer, classification) as a new page under `runs/`.
- File a regression test in sympy for every confirmed wrong answer.

---

## 4. Item 2: branch-correct normalization via the signum algorithm

### 4.1 Sources (both in `~/Dropbox/papers/symbolic-computation/`)

- **Jeffrey 1993**, *Integration to obtain expressions valid on domains
  of maximum extent*, ISSAC 93.  §2 has the log-combining theory,
  including the rule for fractional coefficients
  `a*ln f1 + b*ln f2 -> (m/n)*ln(f1**p * f2**q)` (needed because
  combining under a fractional power reintroduces discontinuities).
  §5 works `∫sqrt(x**(2/3) + x**(4/3))`, whose correct antiderivative
  carries `sgn**(5/3)` factors -- our failure shape.
- **Jeffrey, Labahn, von Mohrenschildt & Rich**, *Integration of the
  signum, piecewise and related functions*.  §5 gives the complete
  algorithm; Theorem 5 gives the jump-correction formula; Example 1 is
  the case reproduced by the prototype below.
- Background: `numerical-analysis/Kahan 1986 - Branch Cuts for Complex
  Elementary Functions`; `theses/von Mohrenschildt 1994 - Symbolic
  Solutions of Discontinuous Differential Equations`.

### 4.2 The algorithm, as it applies here

Rewrite `sqrt(w**2 * v)` as `s*w*sqrt(v)` where `s = sgn(w)` is
introduced as a **symbolic constant**, integrate as usual, then

- substitute `s -> sgn(w)` in the result, and
- add a jump correction `-J_k * sgn(x - x_k)` at each breakpoint
  `x_k` (each real **root or pole** of `w`), where
  `J_k = (G(x_k, s=+1) - G(x_k, s=-1))/2`.

The corrections restore continuity across the breakpoints, giving
answers on Jeffrey's "domain of maximum extent" -- better than merely
correct.  The approach fits this machinery unusually well because the
signs ride through as ordinary symbolic constants, which the corpus
runs already showed the towers handle at rates comparable to concrete
coefficients.

### 4.3 Prototype evidence (verified this session)

`signum_proto2.py`, in the frozen run gist.  Results:

- Jeffrey's Example 1 reproduced exactly: `3*x**2*sqrt(1 + 1/x**2)`
  -> `sgn(x)*((1 + x**2)**(3/2) - 1)`, with `J = 1`.
- `sqrt((x+1)**2*(x+2))`: `J = -4/15`; derivative correct at
  `x = -1.9, -1.5, -0.5, 3` (the first two are where the current code
  is wrong), and the correction takes the discontinuity at `x = -1`
  from 0.533 to 0.
- `sqrt(x**2 + 2*x + 1)/x`: correct at `x = -3` and `-1.5`, the exact
  failing points.

### 4.4 Implementation sketch

1. Replace the current unconditional split in `_rewrite_exps_pows()`
   with the sign-carrying rewrite; record `(s, w)` pairs on the
   `DifferentialExtension` (a new slot, like `backsubs`).
2. After integration, in `risch_integrate()`, substitute the signs
   back and apply the jump corrections.  Keep this outside the tower
   machinery -- it is a post-processing pass on the final result.
3. Breakpoints: real roots of numerator and denominator of each `w`.
4. Where the sign of `w` is provable (`w.is_nonnegative`), skip the
   whole apparatus and split unconditionally, as now.

### 4.5 Open problems to solve during implementation

- **Complex jumps.**  When a breakpoint coincides with a singularity of
  the integrand, `J` comes out complex (our `sqrt(x**2+2*x+1)/x` case
  gives `J = -1 + I*pi`).  Theorem 7 of the signum paper covers the
  integrable-singularity case; decide what to return when the jump is
  genuinely infinite.
- **Odd-order radicals.**  Cube roots need the `sgn**(2/3)` treatment
  of Jeffrey 1993 §5 -- this is the Timofeev case, and sympy's
  principal-branch cube root of a negative real is complex while
  Rubi's is real.  Decide the convention explicitly.
- **Non-polynomial sign arguments.**  Breakpoint detection needs the
  real roots of arbitrary `w`; restrict to what `roots`/`real_roots`
  can do and fall back to leaving the case unsplit.
- **Interaction with the acceptance filter.**  With signs as symbolic
  constants, the filter's kernel test must not treat `s` as an
  ordinary constant that could vanish -- `s**2 == 1` should be part of
  the relation set.
- **Output size.**  `sgn` factors multiply through; consider collecting
  them (`sgn(w)*G` rather than distributing) for readable answers.

---

## 5. Working notes for a new session

### Infrastructure

- Corpus clone: `~/Documents/Python/sympy/rubi-integration-test-suite`
  (MIT; Rubi-derived content under Albert Rich's MIT license).  Runner:
  `risch_test_suite_runner.py` there; upstream PR
  https://github.com/Upabjojr/rubi-integration-test-suite/pull/1
  (opened as Claude at Aaron's direction; Aaron meets Francesco
  Bonazzi regularly if questions come up).
- This file, `RISCH_PLAN.md`, `RISCH_DECISIONS.md` and
  `BRONSTEIN_ERRATA.md` live in `docs/` of
  https://github.com/asmeurer/sympy-risch-notes (the sympy checkout's
  root copies are symlinks into a clone of it); the run log-book is
  `runs/algebraic-run-log.md` there, with the current state in
  `runs/README.md` and per-case data under `runs/data/`.  Commit and
  push in the same turn as any edit: the session scratchpad was wiped
  once mid-session and only the published copies survived, so the
  repository is the durable location, not the working tree.

### Conventions learned the hard way

- **Never point long-running jobs at the live checkout.**  Aaron works
  in it and switches branches; a mid-run checkout silently invalidated
  a whole timing study (every call raised `TypeError` in 0.00 s, which
  looked like instant success).  Use
  `git worktree add <scratchpad>/wt-<name> <branch>` and run against
  that.  Remove worktrees when done so Aaron can check the branch out.
- Timing claims come from **serial** runs only; parallel sweeps inflate
  timeouts through contention.
- Sanity-check measurements: 0.00 s medians mean the code did not run.
- Tests: `python -m pytest -p no:pudb <files> -q` (the pytest-pudb
  plugin is broken).  Lint: `ruff check sympy/integrals/`.
- Commit style: no comments about past code state or session context
  (that belongs in the commit message); known sympy idioms need no
  comment; keep fixes minimal; fix bugs at their source rather than
  working around them in a caller.  No `Claude-Session` trailers;
  keep `Co-Authored-By`.
- Commits are SSH-signed through Secretive and need Aaron's approval
  touch; a persistent monitor that retries commit-and-push is the
  smoothest way to handle it.

## 6. 2026-08-15 session: what was done, what remains

### The bug class is broader than §2 says

§2 describes the square-content case only.  The numerical oracle
showed the same branch error in **every** split shape: distinct
factors (`x/sqrt(x**2 - 1)` wrong for `x < -1`, where both factors are
negative) and symbolic constant factors (`1/sqrt(c*(a + b*x))` wrong
where `c` and `a + b*x` are both negative).  In the trinomial-products
pilot (first 150 attemptable cases), 41 of 45 solved cases were wrong,
including **all 21** `SOLVED-NEW` -- most of the +387 normalization
gain was bogus.  Instantiation sign-dependence is real: for
`1/(x*sqrt(b*x + c*x**2))` the split is correct for `b > 0, c < 0`
(at most one factor negative anywhere) and wrong for the other sign
combinations.

### Item 1 as implemented

`risch_expected_check.py` (corpus clone, `risch-runner` branch),
driven by `RISCH_CHECK=expected`.  Primary verdict: differentiate our
answer and compare with the integrand *numerically* at dyadic points
on both sides of every real root of every radicand factor, plus
complex points; mismatches confirmed at doubled precision.  Expected
antiderivative used only for taxonomy: `DERIV-OK` (one constant
difference), `DERIV-OK-SPLIT` (per-region constants -- the deferred
jump-correction cases), `DERIV-OK-EXP-BAD` (corpus answer's own
derivative fails pointwise), `DERIV-OK-EXP-NC` (expected not
evaluatable/closed).  Parametric cases instantiate in five rounds
(pos/mixed/neg/irrational/complex); worst round wins; TIMEOUT ranks
above the OK verdicts in the aggregate.  Calibration gate: flags both
§2 known-wrong answers, passes known-good ones -- rerun it before
trusting any modified oracle.

Not yet run (deliberately deferred, still §3.2 obligations): the
`positive=True` assumption-sensitivity diff, and special-value
instantiation at vanishing divisors.

### Item 2 as implemented (supersedes §4's sgn design)

In `_rewrite_exps_pows()`: the split `base**(p/q) ->
prod(b**(e*p/q))` is multiplied by a fresh Dummy `s` recorded in
`DE.sign_consts` as `(s, base**(p/q)/split, q)` and back-substituted
via `backsubs`, unless every factor is provably nonnegative (then the
old unconditional split, so `positive=True` outputs are unchanged).
Why the exact ratio instead of `sgn`: its logarithmic derivative
vanishes identically, so it is locally constant off the branch cuts
**including at complex points** (a `sgn(w)` answer is real-line only);
its logarithm is `2*pi*I*(p/q)` times an integer winding, so
`s**q == 1` holds identically, and that relation joins
`_nontrans_power_relations()` (the §4.5 filter-interaction issue).
Any split whatsoever becomes sound -- the ratio absorbs every branch
discrepancy -- so no case analysis of factor signs is needed.

Result: trinomial pilot went 41-wrong-of-45 to 0-wrong with the same
45 solved (no solve-rate loss; one extra 5 s timeout).  All previously
known-wrong cases now verify numerically; regression tests in
`test_risch_integrate_algebraic_branches()`.

### Jump corrections (landed in `7e1b26b875`)

`_nontrans_branch_corrections()` subtracts `J*sign(x - r)` with
`J = (G(r+) - G(r-))/2` at each real root/pole of the split factors
(Jeffrey/Labahn/von Mohrenschildt/Rich Theorem 5).  Reproduces the
paper's Example 1 (`-sign(x)` term, continuous at 0) and the
prototype's `J = -4/15` for `sqrt((x+1)**2*(x+2))`.  Corrections are
locally constant so they cannot affect the derivative; every step may
give up, leaving the (already correct-per-region) plain substitution.
Deliberately skipped: complex `J` (would make real regions complex --
the `sqrt(x**2+2*x+1)/x` case keeps its jump), infinite/undecidable
`J`, symbolic `J` (parametric cases), non-`roots()`-able breakpoints.
The split now also triggers on structure (not `factor()` changing the
expression), so pre-factored radicands and nested rational powers like
`(c*(a+b*x)**(3/2))**(2/3)` work -- the latter integrates instead of
raising.  Pilot effect: 3 of the 5 `DERIV-OK-SPLIT` upgrade to
`DERIV-OK`, no other change.

### Review fixes (landed in `c0167ba61a` and `91db1c31ee`)

The roborev/codex reviews of the two commits above found four real
problems, all fixed and regression-tested:

1. **Restart leak**: the `_exp_part()` restart kept `newf` but wiped
   `sign_consts`/`backsubs`, leaking `_s0` Dummys into results
   (demonstrated with `sqrt(x**2+2*x+1)*(exp(x) + exp(x/2+1))`).
   State now survives the restart.
2. **Genericity of s**: results are only generic in the ratio
   constants, so introducing one now marks the tower
   non-transcendental even when every radical collapses -- candidates
   get the filter, and nonelementary claims are degraded (an
   integrand proportional to `s + 1` vanishes identically where the
   ratio is -1).  Advisor follow-up: the *base case* never reaches
   the per-level filter and `ratint()` over QQ(s) can divide by
   s-polynomials vanishing at attained values (a constructed
   candidate was nan on all of x > -1); the total result is now
   vetted under every ratio assignment before substitution.
3. **Kernel test insufficiency**: `s**q - 1` is reducible, so
   `s - 1` is formally nonzero while the ratio equals 1 on whole
   regions; `_nontrans_accept()` now checks denominators under every
   root-of-unity assignment (conservative: unattained assignments not
   excluded; exotic q that lack exact algebraic values reject).
4. **Complex validity of corrections**: `sign(x - r)` is not analytic,
   so corrected answers stopped being antiderivatives off the real
   axis (confirmed numerically at 1+I).  The correction factor is now
   `(x - r)/sqrt((x - r)**2)` -- equal on the real line, locally
   constant on the complex plane off `Re(x) == r`.  Side-sampling
   offsets are now certified exactly against neighboring breakpoints
   (no fixed 2**-20 minimum, no float collapse).

Corpus pilots unchanged through all four fixes (same solves, same
verdicts, same timing).

Second-round review of the fixes themselves (landed in `5f019bb64c`):
the per-assignment checks over-rejected when a ratio constant lacked
exact algebraic roots of unity (order >= 7) even where it could not
affect the check -- now only constants occurring in the checked
expressions (denominators; plus function arguments and exponents for
the final vetting) are enumerated, so `(x**2+2*x+1)**(1/7)`
integrates instead of degrading; and jump-correction breakpoints now
come from `real_roots()` (complete exact isolation) instead of
`roots()` (which omits roots inexpressible in radicals -- an omitted
root could let a side sample certify a nonlocal ratio value), with
corrections abandoned wholesale when any factor's complete real-root
set is unavailable.  `sqrt((x**5-x-1)**2)` gets its jump corrected at
the exact `CRootOf` breakpoint.  The corpus-clone runner/oracle repo
is not under roborev (sympy only).

Third round (landed in `098641086e`, the vetting factored into a
unit-testable `_nontrans_vet()`): entire functions (`exp`) contribute
only the singular positions inside their arguments, not the arguments
wholesale (but their arguments' *internal denominators* stay risky --
`as_numer_denom()` cannot see into function arguments, so
`exp(x/(x+s))` still rejects); fractional-power bases contribute
their internal denominators for the same reason; and `RootSum`
defining polynomials (an `Expr`, invisible to the `Function` scan)
join the scan with their leading coefficients checked under every
assignment, since an LC vanishing under specialization silently
changes the root set and no value check can see it.

### The full pre-fix audit and the second bug class (2026-08-15 late)

The item-1 audit completed (Run 12 in `runs/algebraic-run-log.md`, per-case table
`rubi-audit-wrong.md` there): of 4,239 solved cases on the pre-fix
branch, **1,705 (40%) had wrong derivatives** -- 1,684 the radicand
split, 13 split-at-complex-points, and **8 of a novel class the audit
was built to find**: proportional radicands
(`sqrt(a+b*x)/sqrt(-a-b*x)` came back as `-I*x`).  Those route
through `is_deriv_k()`, whose rewrite takes the principal
`log(const)` (`log(-1) == I*pi`) unconditionally -- the same
unsoundness as the split, through a different door.  Fixed by the
same exact-branch-ratio mechanism (`97ef0340ca`); its review found
the ratio needed the standard sequential tower substitutions
(`efae6e79e7`, with regression `sqrt(log(x))/sqrt(-log(x))`).  The
transcendental control (285 solved) had zero genuine wrongs.

The audit also surfaced a **leaked-Dummy answer**:
`1/sqrt(I*a*sinh(c+d*x)+a)` returned `_t0*RootSum(...)` pre-fix (a
tower symbol escaped through a residue term).  `risch_integrate()`
now refuses to return a non-transcendental result containing
internal symbols, and the oracle reports such answers statically as
`LEAKED-SYMBOLS` (`72b0a72`).  The oracle also collapses
`Ne(<exact complex arithmetic>, 0)` Piecewise conditions when
instantiating (`7c4b97c`) -- 143 of the audit's 144
`UNDECIDED-COVERAGE` were that artifact (real rounds all verified) --
and the runner survives corpus modules that crash at import
(`f55a8b6`), which had silently cost t_5/t_7/t_8.

### Still open

- **Jump corrections, second pass**: the skipped classes above
  (complex jumps at integrand singularities; symbolic jumps under
  assumptions; breakpoints needing `real_roots` on non-rational
  factors).  The remaining `DERIV-OK-SPLIT` sweep bucket is the
  acceptance set.
- The `1/sqrt(I*a*sinh(c+d*x)+a)` case now dies with a
  PolynomialError inside `as_poly_1t()` (fail-safe, but of the
  pre-existing PolynomialError-crash family, cf. issue #26502).
- When analyzing sweep results, treat "ours unevaluatable on a whole
  region" inside `UNDECIDED-COVERAGE` as a red-flag pattern (the
  base-path hole above surfaced as nan regions, which the oracle
  skips as unevaluatable points rather than flagging WRONG).
- **Output form**: branch-ratio factors ride through unsimplified
  (e.g. `sqrt(x**2 + 2*x + 1)/(x + 1)` appearing verbatim).  Any
  cleanup must be structural (cancel-level), never Expr simplify.
- Full-corpus post-fix sweep (queued behind the pre-fix audit sweep,
  against `91db1c31ee`) and the mismatch table for the run log;
  regression tests for any *new* wrong answers the sweep finds.

### Bugs this corpus has already surfaced (all fixed, with tests)

Five in sympy master: the `spde()` infinite loop for SymPy Integer
degree bounds; malformed Polys from
`is_log_deriv_k_t_radical_in_field()`; `ratint_logpart()`'s
`PolynomialError` for radical coefficients (issue #26502, partially
fixed -- octic cases still crash); `PolyMatrix` scalar multiplication
with a ground-domain fallback; plus the `bound_degree` Poly-vs-int
family from Phase 0.  Two in the algebraic branch itself, and one hole
in the acceptance filter.  Expect item 1 to find more.
