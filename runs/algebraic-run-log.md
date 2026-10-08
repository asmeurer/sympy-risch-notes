# risch-algebraic experiment: run log

Runs of sympy's `risch_integrate(f, x, algebraic=True)` (the experimental
exp-log-tower representation of radicals, e.g. `sqrt(x)` as
`exp(log(x)/2)`) over test corpora.  Companion to the "Experimental
track" section of the RISCH_PLAN.md gist.

## Summary (as of 2026-08-21)

The experiment: represent radicals as exp-log towers, run the
transcendental Risch machinery over them, degrade every nonelementary
conclusion to a plain `Integral` (the proofs assume transcendence), and
accept solved results only after a tower-level verification.  Since
2026-08-18 (Run 14) this is what plain `integrate()` does by default on
the `risch-algebraic` branch.

**Where things stand** (each claim links to the run that measured it):

- **Rubi radical corpus** (Runs 11-13): the numerical oracle found that
  **40% of the pre-fix solves were wrong** (1,705 of 4,239 -- the
  unconditional radicand split and the `is_deriv_k` principal-constant
  rewrite); after the exact-branch-ratio fixes the full post-fix sweep
  has **0 wrong among 4,287 solved** (4,286 at tip `518d57ad37` once
  the one leaked-Dummy "solve" is reclassified), 425 `DERIV-OK-SPLIT`,
  median per-case time unchanged.
- **Hebisch exp-log corpus, 2,000 cases** (three-way comparison +
  follow-up): the principal-branch log/exp rewrite gave 30-31
  verified-wrong answers on every branch (incl. master); fixed on
  `risch-rde-cancellation` (`562d069b5e`, `3c5b649612`, follow-ups
  `0b77ab246b`, `d7dafa43c1`) -- **0 wrong, 1,851 solved, all
  symbolically proven**.  `risch-rde-cancellation` nets +20 solved over
  master; 12 of the 13 `PolynomialError` crashes fixed by `025e390835`.
  Root-cause write-up: `01b-WRONG_ANSWERS.md`.
- **Blake algebraic corpus**: 1,500-case sweep 291 solved (08-19) ->
  303 (08-21, after the structure-guard decide-or-degrade commits),
  **0 wrong**, master/rde-cancellation solve none; the full 3,154-case
  pre-relaxation sweep at the plain `risch_integrate(f, x)` entry point
  (`pretip-blake-abort-census.jsonl`): 286 solved, 485
  `parametric_log_deriv` aborts, 197 timeouts.
- **MIT Integration Bee official suite** (`09-mit-bee-official-risch.md`,
  08-21): `risch-algebraic` 98 vs master 84 of 263 indefinite cases,
  0 wrong, 0 losses.
- **Structure-constant guards** (08-21, `15e76e361e` + `3b072169b7` on
  `risch-algebraic`): the remaining `NotImplementedError` aborts on
  non-rational structure constants now decide ("no relation", proven
  irrational entry) or degrade; Hebisch 400-case spot check 365 -> 368.

**Still open**: the exp-side `sympows` rewrite `exp(b*(log(const) + u))`
for symbolic powers still takes the principal constant (not exercised
by any corpus); the Hebisch regressions vs master named in
`01-RISCH_BRANCH_COMPARISON.md` (the 6 `parametric_log_deriv` NIEs among
them); Hebisch 274 (`E` and `exp(1/2)` as independent constant
generators); constant irrational exponents on a variable base
(`x**log(2)`) never reach the tower; the jump-correction second pass
(`DERIV-OK-SPLIT` acceptance set); output-form cleanup.

**Files in this gist**: `00` this log-book (runs in order below);
`01`/`01b` the 2026-08-19 three-way comparison and its wrong-answer
root-cause analysis (per-case data `branch-cmp-*.jsonl`);
`02-rubi-audit-wrong.md` the Run 12 pre-fix WRONG table (all fixed);
`09` the MIT Bee run (per-case data `mitbee-*.jsonl`);
`pretip-blake-abort-census.jsonl` the full Blake sweep.
**`zz-archive-*`** holds superseded material kept for the record:
the 2026-08-10/11 per-case Rubi tables and their raw results
(`zz-archive-0[3-8]-rubi-table-*.md`, `zz-archive-rubi-alg-results.jsonl`,
`zz-archive-rubi-linear-chapter.log`) -- their SOLVED statuses predate
the oracle and Run 12 found 40% of them wrong; the Run 3 transcendental
A/B logs (`zz-archive-rubi-trans-wt-*.jsonl`), superseded by the Hebisch
comparison; and `zz-archive-signum_proto2.py`, the `sgn` prototype
superseded by the exact-ratio design (Run 11).

## Original summary (2026-08-11, pre-oracle)

*Kept as written.  Its "zero wrong answers" rested on the tower-level
formal check alone; the numerical oracle of Run 12 later showed 40% of
these solves had wrong derivatives (branch errors), and Run 13 shows
the fixed branch back at zero with more solves.  The per-part table
below is still the only per-chapter breakdown of the capture run.*


The experiment: represent radicals as exp-log towers, run the
transcendental Risch machinery over them, degrade every nonelementary
conclusion to a plain `Integral` (the proofs assume transcendence), and
accept solved results only after a tower-level verification (formal
derivative identity + denominators nonzero under the tower's algebraic
relations).  Test corpus: the Rubi test suite, ~16,800 attemptable
radical cases.

**Headline numbers** (details in the runs below; per-case tables in the
`zz-archive-0*-rubi-table-*.md` files, pre-fix):

- **970 integrals solved that sympy's non-Risch `integrate()` cannot do**
  (`SOLVED-NEW`), plus 2,771 solved by both.  **Zero wrong answers and
  zero false nonelementary claims** across the whole corpus.
- Single-radical families solve at 40–50%; the classic collections
  (Timofeev, Hearn, Bronstein) contribute 9 concrete new solves.
- The transcendental A/B on the radical-free exp-log chapters (master
  vs the `risch-rde-cancellation` branch): **zero regressions, five
  improvements** (four crashes become decided results, two of them
  newly solved).

**Results by corpus part** (uniform capture run, per-case data in
the `zz-archive-0*-rubi-table-*.md` files):

| corpus part | attempted | SOLVED-NEW | SOLVED-both | partial | timeout | NIE |
|---|---|---|---|---|---|---|
| 0. Independent suites | 632 | 9 (1%) | 110 (17%) | 345 (55%) | 3 (0%) | 165 (26%) |
| 1.1.1 Linear binomials | 3377 | 159 (5%) | 615 (18%) | 2235 (66%) | 353 (10%) | 15 (0%) |
| 1.1.2-4 Other binomials | 5144 | 143 (3%) | 1102 (21%) | 3735 (73%) | 141 (3%) | 23 (0%) |
| 1.2 Trinomials | 6148 | 617 (10%) | 874 (14%) | 4451 (72%) | 203 (3%) | 3 (0%) |
| 1.3 Miscellaneous | 726 | 36 (5%) | 49 (7%) | 566 (78%) | 11 (2%) | 64 (9%) |
| 2-3 Exp/log radicals | 131 | 6 (5%) | 21 (16%) | 82 (63%) | 1 (1%) | 21 (16%) |
| **all** | **16158** | **970 (6%)** | **2771 (17%)** | **11414 (71%)** | **712 (4%)** | **291 (2%)** |

**Key findings**:

- Input representation (`1/sqrt(x)` vs `sqrt(x)/x` etc.) and tower
  order have **negligible** effect on solvability (1 flip in 250
  unsolved samples) — no retry driver needed.
- **~95% of the unsolved mass is the genuine algebraic-Risch frontier**:
  the per-power rischDE subproblems correctly find no solution of
  transcendental shape, because the true antiderivatives need terms
  mixing several radical generators.  Finishing the exp-log gaps buys
  only the residue-side slice (~4%), the `parametric_log_deriv`
  undecidables (47 cases), and part of the timeouts; the rest needs
  real algebraic machinery (Trager / Bronstein Vol. II).
- The corpus flushed out three genuine sympy master bugs (an spde()
  infinite loop, malformed Polys in is_log_deriv_k_t_radical_in_field(),
  and the ratint_logpart() PolynomialError of issue #26502) plus two
  crashes in the experimental branch itself — all fixed except the
  octic tail of #26502.

## Configuration (2026-08-10)

- sympy branch: `risch-algebraic` at `56520fe191` (stacked on
  `risch-rde-cancellation` at `496a777876`; fork `asmeurer/sympy`)
- corpus: [Upabjojr/rubi-integration-test-suite](https://github.com/Upabjojr/rubi-integration-test-suite)
  at `0643a6b` — the Rubi MathematicaSyntaxTestSuite translated to
  SymPy, 66k+ cases
- runner: `risch_test_suite_runner.py` (local, in the corpus clone;
  mirrors the upstream runner's role)
- per-case timeout: 5 s (SIGALRM); first 120-case sample used 15 s
- case filter ("attemptable"): every exponent a concrete Rational, at
  least one non-integer (an actual radical), no nan/oo; cases split
  into **concrete** (free symbols == {x}) and **parametric** (symbolic
  constants, e.g. `(a + b*x)**(3/2)`)

Classification: `SOLVED` = no unevaluated Integral in the result (for
algebraic towers every solved result was certified internally by the
tower-level acceptance filter: formal-derivative identity + kernel-free
denominators); `partial` = plain unevaluated Integral returned
(honest); `CLAIMS-NE` = NonElementaryIntegral present (**would be a
bug**: nonelementary proofs are invalid over algebraic towers);
`NIE` = NotImplementedError; `timeout`; `error:*`.

## Corpus census (algebraic chapters)

| chapter | total | radical-concrete | radical-parametric | symbolic-exponent | no-radical |
|---|---|---|---|---|---|
| 1.1 binomial products | 13,777 | 2,117 | 6,436 | 1,507 | 3,717 |
| 1.2 trinomial products | 10,200 | 1,163 | 5,009 | 1,003 | 3,025 |
| 1.3 miscellaneous | 1,350 | 373 | 358 | 159 | 460 |

(symbolic-exponent cases — `(a + b*x)**m` with symbolic `m` — are
unattemptable by any Risch-style method and are excluded from runs.)

## Run 1: chapter 1.1.1 (linear binomials), complete — 2026-08-10

Totals: **3,385 attempted, 782 SOLVED (23%), 0 CLAIMS-NE, 0 errors.**

| shard (source family) | tried | concrete | parametric | notes |
|---|---|---|---|---|
| 1.1.1.2 `(a+b x)^m (c+d x)^n` (single-radical slice) | 1,247 | 126: 64 S, 48 p, 14 t | 1,121: 415 S, 626 p, 80 t | ~40–50% solve on single-radical forms |
| 1.1.1.3 (two-radical products) | 1,903 | 1,185: 131 S, 935 p, 119 t | 718: 156 S, 366 p, 196 t | new-extension frontier |
| 1.1.1.4 (improper/general) | 105 | 56: 0 S, 31 p, 13 NIE, 12 t | 49: 4 S, 26 p, 2 NIE, 17 t | |
| 1.1.1.5 (cubic numerators) | 24 | — | 24: 12 S, 12 p | |
| 1.1.1.6 (three linear factors) | 71 | — | 71: 0 S, 38 p, 33 t | profiling target |
| 1.1.1.7 `P(x) (a+b x)^m ...` | 35 | — | 35: 0 S, 35 t | profiling target |

(S = SOLVED, p = partial, t = timeout.  Full raw log, including
per-shard SOLVED listings and timing progress lines, in
`zz-archive-rubi-linear-chapter.log` below.)

Reading of the results:

- The **zero CLAIMS-NE / zero errors** across 3,385 cases is the
  headline: the degrade-to-Integral policy plus the acceptance filter
  hold at scale.
- Symbolic constants flow through the towers fine — parametric cases
  solve at comparable-or-better rates than concrete ones.
- Failures partition into the two known work streams: honest partials
  cluster on multi-radical integrands (new-extension discovery /
  structure theorems), and the all-timeout families point at tower
  construction or machinery cost (profile one representative case).

## Run 0: 30-case hand battery + failing-integrals sampling — 2026-08-09

16/30 solved, 0 wrong answers (every solved case verified by
differentiation in the harness), 0 false nonelementary claims; the
acceptance filter caused no false rejections.  Newly solving vs the
original PoC branch: `sqrt(x)`, `x**(3/2)`, `x**(5/2)`, `x**(4/3)`,
`sqrt(x)*log(x)`, `d/dx[sqrt(x)*sqrt(x+1)]`, `sqrt(1-x) + sqrt(1+x)`.
From `test_failing_integrals.py` territory: `x/sqrt(a - x)`,
`x*sqrt(x**2 + 1)`, `x**(3/2)*log(x)` solve; `sqrt(1 - x**2)`,
`sqrt(x)/(1 + sqrt(x))`, `sqrt(1 + sqrt(x))` honest-partial;
`1/sqrt(a*x**2 + b*x + c)` times out.

## Run 2: full relevant corpus, comparison mode — 2026-08-10/11

Runner gained `integrate(f, x, risch=False)` cross-checks: `SOLVED-NEW`
means only the algebraic towers solve it.  Chapters 0 + 1.1 ran on the
tree at the spde-loop fix; 1.2/1.3/2/3 after it.  Totals across the
~16,800 attempted radical cases: **~980 SOLVED-NEW, ~1,900 SOLVED-both,
0 wrong answers, 0 false nonelementary claims** (the 10 apparent
CLAIMS-NE were classifier false alarms: radicals of exponentials and of
constants leave the tower transcendental, so those NonElementary
results are sound proofs; classifier fixed).  Highlights: trinomial
products 617 SOLVED-NEW; linear binomials 159; chapter 0 classics 9
(Timofeev, Hearn, Bronstein).  Crashes found and fixed along the way:
the spde() SymPy-Integer infinite loop (master bug), the exps-worklist
AttributeError (nested rational powers), and the ratint_logpart()
PolynomialError for radical coefficients (master bug, issue #26502,
partially fixed: quartic algebraic and symbolic-radical cases work,
octic cases still crash at later constructions).

## Run 3: transcendental A/B, master vs risch-rde-cancellation — 2026-08-11

The radical-free exp-log cases of chapters 2-3 (856 cases) through
stock risch_integrate on both trees.  **Identical outcomes except five
master->branch improvements, zero regressions**: four master
error:TypeError crashes in 3.2.3 (the bound_degree Poly-vs-int family
fixed in Phase 0) become two sound nonelementary decisions and two
SOLVED-NEW (e.g. integrands built over log((a+b*x)/(c+d*x)) towers
that only risch solves), and one master timeout becomes a decided
nonelementary result.  In this mode a NonElementaryIntegral result is
a legitimate proof (the towers are genuinely transcendental).

## Full per-case tables

*Archived 2026-08-21 (`zz-archive-` prefix): these are the 2026-08-10/11
pre-fix capture; Run 12 found 40% of their SOLVED entries wrong and
Run 13 is the post-fix measurement.  Kept for the record only.*

Every attempted algebraic case with SymPy expression, rendered math,
and status, split by corpus part: see the zz-archive-0*-rubi-table-*.md files in
this gist (SOLVED-NEW bolded).  Raw per-case data:
`zz-archive-rubi-alg-results.jsonl` / `zz-archive-rubi-trans-wt-*.jsonl`.

## Run 4: representation and tower-order sensitivity — 2026-08-11

250 sampled unsolved (partial/NIE) cases retried under together/
expand/powsimp(force)/cancel rewritings and handle_first='exp' tower
order: **1 flip** (a perfect square, (a**2 + 2*a*b*x +
b**2*x**2)**(3/2), which expand/cancel let the builder reduce), and
tower order flipped nothing.  Representation sensitivity exists in
principle but is empirically negligible on this corpus: a
retry-driver over rewritings is not worth building for the current
failure mass.

## Run 5: why the partials fail — 2026-08-11

200 sampled partial cases rerun with stage instrumentation:

| stage that gave up | count |
|---|---|
| integrate_hyperexponential_polynomial (in-field rischDE per t-power) | 191 |
| residue side (needs new log/atan extensions) | 8 |
| acceptance-filter reject | 1 |

So ~95% of the unsolved mass dies in the polynomial part: the
per-power rischDE subproblems conclude "no solution", which over a
non-transcendental tower means "no solution *of the transcendental
shape*" -- the true antiderivatives (Rubi solves these) need terms
mixing several radical generators, which the single-monomial machinery
cannot produce.  This is the genuine algebraic-Risch frontier
(Trager/Bronstein Vol. II territory), NOT something that finishing the
exp-log gaps will fix.  The exp-log-completion payoff on this corpus
is the smaller slice: the residue-side partials, the 47
parametric_log_deriv NIEs, and part of the timeouts.

## Run 6: tower-level representatives and the kernel checks — 2026-08-12

Two follow-ups.  (a) The acceptance-filter checks never fire on corpus
inputs (400-case instrumented sample: 379 passes, 0 identity failures,
0 kernel failures, remainder not reaching the filter), so the kernel
path is covered by a constructed regression test instead — which
exposed and fixed a real hole: kernel contamination entering through
the residue coefficients, invisible to both prior checks because the
kernel factors cancel between a logarithm's coefficient and its
argument's derivative (sympy commit 46dcb5c928).

(b) The representation question done at the *representation* level
(Expr-level rewriting cannot express it -- sympy auto-canonicalizes
same-base powers): multiply fa/fd by algebraic generators and reduce
modulo the power relations, giving a different formal rational
function for the same function.  **2 flips in 150 unsolved cases**,
both by clearing the radical from the formal denominator
(e.g. (x + (1 - 9*x**2)**(3/2))/sqrt(1 - 9*x**2)).  Conclusion: the
sensitivity is real and lives exactly where predicted, but is small;
the actionable form is a canonical representative -- normalize fa/fd
at tower-build time so algebraic generators do not divide the
denominator -- rather than a retry driver.

## Run 7: controlled identical-representation pairs — 2026-08-12

Pairs of algebraically identical inputs that sympy keeps syntactically
distinct (x positive), both run through `algebraic=True`:

| pair | form A | form B |
|---|---|---|
| `sqrt(x*(x+1))` vs `sqrt(x)*sqrt(x+1)` | partial | partial |
| `1/sqrt(x*(x+1))` vs `1/(sqrt(x)*sqrt(x+1))` | partial | partial |
| `sqrt(x/(x+1))` vs `sqrt(x)/sqrt(x+1)` | partial | partial |
| `1/(sqrt(x+1)+sqrt(x))` vs `sqrt(x+1)-sqrt(x)` | partial | **SOLVED** |
| `sqrt((x+1)**2*(x+2))` vs `(x+1)*sqrt(x+2)` | SOLVED | SOLVED |
| `sqrt(x**2+3*x+2)` vs `sqrt(x+1)*sqrt(x+2)` | partial | partial |
| `sqrt(x**2+2*x+1)/x` vs `(x+1)/x` | partial | **SOLVED** |
| `sqrt(exp(2*x)+2*exp(x)+1)` vs `exp(x)+1` | SOLVED | SOLVED |

Discordance occurs exactly when a representation hides structure the
tower builder does not normalize: rationalizable sum-of-radicals
denominators, and perfect squares unexpanded inside a radicand.
Structurally equivalent representations (split vs combined radicals)
agree, matching the failure taxonomy.  Actionable: two build-time
canonical-form fixes (square-content extraction from radicands;
clearing radicals from the formal denominator, cf. Run 6) would close
every discordance found by any of the three methods.

## Run 8: corpus-scale normalization measurement — 2026-08-12

The two candidate canonical-form fixes from Runs 6-7, measured over
1,500 sampled unsolved cases before deciding whether to implement:

| normalization | flips | corpus-wide estimate |
|---|---|---|
| square-content extraction (factor radicands) | 65 (4.3%) | ~507 cases |
| clearing radicals from the formal denominator | 6 (0.4%) | ~47 cases |
| either | 71 (4.7%) | ~554 cases (overall solve rate 23.2% -> ~26.6%) |

Decision (per Aaron's rule -- implement if significant, skip or
flag-gate if rare): **square-content extraction implemented** in
DifferentialExtension for the algebraic mode (sympy commit
409f898b96); denominator clearing skipped.  With it,
`sqrt(x**2 + 2*x + 1)/x` integrates to
`sqrt(x**2 + 2*x + 1) + log(x) - 1`, and the Run 7 perfect-square
discordances close.  Timing: the runner now records per-case seconds
in the JSONL for all future runs; the transcendental A/B already
showed master and the branch identical to within noise (783 s vs
785 s over the same 856 cases), so the new machinery has not slowed
the classic fast path.

## Run 9: timing, and the anatomy of the slow tail — 2026-08-13

**Distributions** (per-class study, serial, pinned worktree): solved
cases are fast and failures are cheap — SOLVED-both median 0.09 s
(p90 0.36 s), SOLVED-NEW median 0.26 s (p90 1.29 s), partial median
0.16 s.

**Head-to-head vs `integrate(risch=False)` on 600 SOLVED-both**:
median 0.09 s vs 0.21 s; **risch >=5x faster on 116 cases (19%)** vs
integrate >=5x faster on 33 (5.5%); extremes ~60x (e.g.
`(1 - 2*x**2)**(-7/2)` at 0.05 s vs 3.0 s).  integrate() never failed
outright on the sample, so the advantage is pure speed.

**Full timed rerun** (parallel, 6 workers): validates the radicand
normalization at **+387 SOLVED-NEW** (970 -> 1,357; overall 23.2% ->
25.6%), all landing as SOLVED-NEW.  Timeout counts under parallelism
are inflated by contention (953 vs 712 serial) — timing conclusions
here come from the serial runs.  The rerun also flushed out a real
master bug in sympy/polys: PolyMatrix scalar multiplication with a
ground-domain fallback (EX) crashed with AttributeError, reached
through constant_system() for nested symbolic radicals like
`sqrt(a + b*sqrt(d/x) + c/x)` (fixed at the PolyMatrix level,
`bd3dde37f8`).

**Deep probe of the former timeout class** (120 sampled, 300 s cap,
serial): 68 finish within 30 s — including **9 that fully solve**
(several instantly, their hidden perfect squares now collapsed by the
normalization; others genuinely slow solves at 40-67 s) — 13 more by
120 s, 3 by 300 s, and **36 exceed 300 s**.  Stack sites at the cap:
residue_reduce 17, gcdex_diophantine 8, ratint_logpart 8, spde 3 —
all bounded-arithmetic shapes (subresultant PRS and extended-GCD
coefficient blowup over parametric multi-radical towers), no
loop-signature sites.  **Conclusion: the tail is slow, not hung.**
Roughly 2% of attempted corpus cases sit beyond 300 s; a production
cap of ~30 s would recover ~60% of the former timeout class,
including new solves.

## Run 10: branch-correctness of the radicand normalization — 2026-08-13

**The problem.** The radicand factoring of Run 8 distributes fractional
powers over factors, an algebraic equivalence only where the factors
are positive: `sqrt((x+1)**2*(x+2)) -> (x+1)*sqrt(x+2)` has the wrong
sign for x < -1.  Verified numerically: the answers for
`sqrt(x**2+2*x+1)/x` and Timofeev's `(x**3-5*x**2+3*x+9)**(-2/3)` are
wrong on whole real intervals (the latter is one of the 9 chapter-0
headline solves).  The tower-level acceptance filter cannot see this:
it certifies against the tower image of the *rewritten* integrand.
The core machinery is NOT affected -- `exp(log(u)/2)` is identically
the principal `sqrt(u)`, and core-path answers spot-checked at
negative and complex points are all faithful.

**The literature answer** (Jeffrey 1993, ISSAC 93; Jeffrey, Labahn,
von Mohrenschildt & Rich, "Integration of the signum, piecewise and
related functions" -- both in ~/Dropbox/papers/symbolic-computation):
carry the sign explicitly.  `sqrt(w**2*v) == |w|*sqrt(v) ==
s*w*sqrt(v)` with `s = sgn(w)` treated as a **symbolic constant**
during integration; afterwards substitute `s -> sgn(w)` and add jump
corrections `-J_k*sgn(x - x_k)` at each breakpoint (root or pole of
w), where `J_k = (G(x_k, s=+1) - G(x_k, s=-1))/2`.  That restores
continuity -- Jeffrey's "domain of maximum extent".  Jeffrey 1993 §2
additionally gives the rule for combining logarithms with fractional
coefficients: `a*ln f1 + b*ln f2 -> (m/n)*ln(f1**p * f2**q)`.

**Prototype result** (`zz-archive-signum_proto2.py`): the approach works end to end
on our towers.
- Jeffrey's Example 1 reproduced exactly: `3*x**2*sqrt(1+1/x**2)` ->
  `sgn(x)*((1+x**2)**(3/2) - 1)`, J = 1.
- `sqrt((x+1)**2*(x+2))`: J = -4/15; derivative correct at x = -1.9,
  -1.5, -0.5, 3 (the first two are where the current code is wrong),
  and the correction makes the answer continuous at x = -1 (jump
  0.533 -> 0).
- `sqrt(x**2+2*x+1)/x`: correct at x = -3 and -1.5, the exact failing
  points.
The signs pass through as ordinary symbolic constants, which the
corpus runs already showed the towers handle well.

**Consequence for the Run 8 decision**: the choice is not "gate on
positivity (losing ~all corpus gains) vs keep a generically-valid
answer".  The signum algorithm keeps the gains *and* returns answers
valid on the whole real line, at the cost of `sgn` factors in the
output and a jump-correction pass.  Open work: complex-valued jumps
when a breakpoint sits at a singularity of the integrand (our
`sqrt(x**2+2*x+1)/x` case gives J = -1 + I*pi); cube roots and other
odd radicals need the `sgn**(2/3)`-style treatment of Jeffrey 1993 §5;
and breakpoint detection needs the roots of non-polynomial sign
arguments.

## Run 11 (2026-08-15): expected-antiderivative oracle; branch-ratio fix

Sympy commit `e3caaaeb2a` ("Carry branch-ratio constants through the
algebraic radicand split") on `risch-algebraic`; runner commit
`30c19c7` ("Add an expected-antiderivative oracle to the risch
runner") on the corpus clone's `risch-runner`.

### The oracle (plan item 1)

`risch_expected_check.py`, driven by `RISCH_CHECK=expected`.  Primary
verdict: differentiate our answer, compare with the integrand
numerically at dyadic points on both sides of every real root of every
radicand factor plus complex points; mismatches confirmed at doubled
precision.  Expected answer used only for taxonomy (DERIV-OK /
DERIV-OK-SPLIT / DERIV-OK-EXP-BAD / DERIV-OK-EXP-NC).  Five
instantiation rounds for symbolic constants (pos/mixed/neg/irr/cx),
worst round wins.

Calibration gate (all passed): flags `sqrt(x**2+2*x+1)/x` and
Timofeev's `(x**3-5*x**2+3*x+9)**(-2/3)` as WRONG; passes
`x*sqrt(x**2+1)`, log-vs-asinh form differences, parametric
`1/sqrt(x+a)` across all rounds; classifies `atan(x)` vs `-atan(1/x)`
as SPLIT and a sign-flipped expected as EXP-BAD.

### The bug class is bigger than the plan said

The oracle immediately showed the branch error in *every* split
shape, not just square content:

- distinct factors: `x/sqrt(x**2 - 1)` wrong for `x < -1` (both
  factors negative);
- symbolic constant factors: `1/sqrt(c*(a+b*x))` wrong where `c` and
  `a+b*x` are both negative;
- sign-dependence per instantiation: `1/(x*sqrt(b*x + c*x**2))` is
  *correct* for `b > 0, c < 0` (at most one factor ever negative) and
  wrong for the other sign combinations.

Trinomial-products pilot (first 150 attemptable cases), pre-fix
worktree `a1c2226052`: **41 of 45 solved cases WRONG, including all
21 SOLVED-NEW**.  Binomial-products pilot: 82/82 solved correct (its
radicands don't factor).

### The fix (plan item 2, superseding the sgn design)

Instead of `s -> sgn(w)`: multiply the split by the *exact branch
ratio* `s = original/split`, a locally-constant function (its
logarithmic derivative vanishes identically) with `s**q == 1`
(logarithm is `2*pi*I*(p/q)` times an integer winding).  Valid at
complex points, no sgn in the output, any split becomes sound, and
`s**q - 1` joins the kernel-test relation set (the plan's §4.5
filter-interaction issue).  Jump corrections (continuity/maximum
extent) deferred: they never affect derivative correctness; the
DERIV-OK-SPLIT bucket is the acceptance set for that follow-up.

Post-fix pilots: trinomials **0 wrong of the same 45 solved** (40
DERIV-OK + 5 DERIV-OK-SPLIT; one extra 5 s timeout), binomials
unchanged 82/82.  Regression tests in
`test_risch_integrate_algebraic_branches()`.

### In progress

Full-corpus audit sweep of the pre-fix branch (all chapters algebraic
mode + transcendental control on t_2/t_3), then the post-fix re-sweep;
mismatch table to follow as a gist page.  Not yet run: `positive=True`
assumption-sensitivity diff; special-value instantiation.

### Run 11 addendum: jump corrections landed

Commit `7e1b26b875` ("Correct the jumps left by branch-ratio
substitution"); oracle update `c7557f3` (freeze `sign()` before
differentiating; TIMEOUT outranks OK verdicts in round aggregation).

`_nontrans_branch_corrections()` implements Jeffrey/Labahn/von
Mohrenschildt/Rich Theorem 5: subtract `J*sign(x - r)`,
`J = (G(r+) - G(r-))/2`, at each real root/pole of the split factors.
Reproduces the paper's Example 1 (`3*x**2*sqrt(1 + 1/x**2)` gains
`-sign(x)`, continuous at 0, jump 2.0 -> 1e-12) and the prototype's
`J = -4/15` for `sqrt((x+1)**2*(x+2))` (jump 0.533 -> 0).  Skipped by
design: complex J (`sqrt(x**2+2*x+1)/x` keeps its jump at 0 rather
than turning real regions complex), infinite/symbolic J,
non-`roots()`-able breakpoints -- corrections are locally constant, so
skipping never affects derivative correctness.

The split trigger is now structural (multiple factors or multiplicity
in the factorization) instead of "`factor()` changed the expression",
which picks up pre-factored radicands and nested rational powers:
`(c*(a+b*x)**(3/2))**(2/3)` now integrates branch-correctly (verified
across all five instantiation rounds) where it used to raise
NotImplementedError.

Pilot deltas (150-case slices, live checkout at `7e1b26b875`):
trinomials 17 SOLVED-both concrete = 15 DERIV-OK + 2 DERIV-OK-SPLIT
(was 12 + 5 pre-corrections; was 17 WRONG pre-fix); parametric 28/28
DERIV-OK; binomials unchanged 82/82 DERIV-OK.  No solve-rate or
timing change.

### Run 11 addendum 2: review fixes

Commits `c0167ba61a` ("Fix four review findings in the branch-ratio
machinery") and `91db1c31ee` ("Vet sign-carrying results under every
ratio assignment"); oracle `06c2ef9` (complex sample points on odd
64ths, off plausible `Re(x) == r` correction-discontinuity lines).

The roborev/codex reviews of the two Run 11 commits found four real
problems; all confirmed (two demonstrated: the `_s0` Dummy leak via
the `_exp_part()` restart, and the sign()-correction complex-axis
breakage at 1+I) and fixed:

1. restart preserves `sign_consts`/`backsubs` (and the
   non-transcendental flag);
2. introducing a ratio constant marks the tower non-transcendental
   even when every radical collapses (results are only generic in s),
   and -- advisor follow-up on the same finding -- the total result is
   vetted under every ratio assignment before substitution, closing
   the base-case path where `ratint()` over QQ(s) divided by
   s-polynomials vanishing at attained values (a constructed
   candidate was nan on all of x > -1 while the integrand was 1
   there);
3. `_nontrans_accept()` checks denominators under every root-of-unity
   assignment, since `s - 1` is formally nonzero mod `s**2 - 1` but
   the ratio equals 1 on whole regions;
4. jump corrections use `(x - r)/sqrt((x - r)**2)` (sign(x - r) on
   the real line, locally constant on C off `Re(x) == r`), restoring
   complex-point validity, with side-sampling offsets certified
   exactly against neighboring breakpoints.

Corpus pilots unchanged through all fixes (same solves, verdicts,
timing).  The post-fix full sweep is queued against `91db1c31ee`.
Analysis note for the sweeps: results unevaluatable on a whole region
surface as UNDECIDED-COVERAGE (skipped points), not WRONG -- treat
that bucket as a red flag, not noise.

### Run 11 addendum 3: second-round review fixes

Commit `5f019bb64c` ("Address the second-round review of the
branch-ratio fixes"), from the roborev/codex reviews of the previous
two fix commits (both findings relevant and fixed):

1. The per-assignment checks rejected every candidate whenever any
   ratio constant lacked exact algebraic roots of unity (order >= 7),
   even where the constant could not affect the check.  Now only
   constants occurring in the checked expressions are enumerated
   (denominators for the acceptance filter; denominator + function
   arguments + exponents for the final vetting -- purely
   numerator-polynomial occurrences cannot produce singularities).
   `(x**2 + 2*x + 1)**(1/7)` integrates now instead of degrading.
2. Jump-correction breakpoints came from `roots()`, which omits real
   roots inexpressible in radicals; an omitted root could let a side
   sample cross an unrecognized breakpoint and certify a nonlocal
   ratio value (continuity-only damage: corrections are locally
   constant, so the derivative was never at risk).  `real_roots()`
   now supplies the complete exact real-root set, and corrections are
   abandoned entirely for factors that cannot provide one.
   `sqrt((x**5 - x - 1)**2)` now gets its jump corrected at the exact
   `CRootOf` breakpoint (jump 8e-6 across the isolated root).

Trinomial pilot unchanged again (17 + 28 solved, 0 WRONG, 2 SPLIT).
The post-fix sweep worktree is advanced to `5f019bb64c`.  The
corpus-clone runner/oracle repo is not under roborev (sympy only);
those commits were reviewed by the session advisor instead.

### Run 11 addendum 4: third-round review fixes

Commit `098641086e` ("Refine the sign-carrying vetting into
_nontrans_vet()"), from the review of `5f019bb64c`.  Both findings
relevant and fixed:

1. Entire-function over-rejection: every `Function` argument was
   treated as singularity-sensitive, so an unenumerable ratio
   constant inside an `exp()` argument still degraded the result.
   `exp` now contributes only the singular positions inside its
   arguments -- while keeping the arguments' internal denominators
   risky (`as_numer_denom()` cannot see into function arguments, so
   `exp(x/(x + s))` still rejects), with nested functions, powers,
   and exponents covered by the recursive `atoms()` walks.
   Fractional-power bases contribute their internal denominators for
   the same reason.
2. `RootSum` blind spot: `RootSum` is an `Expr`, not a `Function`,
   so ratio constants in its defining polynomial escaped the scan --
   and a leading coefficient vanishing under an assignment silently
   changes the root set, which no nan/zoo value check can see.
   Defining polynomials join the scan; their LCs are checked under
   every assignment.

The vetting is factored into `_nontrans_vet()` and unit-tested
directly (entire-arg pass, log-arg reject, hidden-denominator
reject, RootSum LC reject/pass on quintic defining polys).  Corpus
pilot unchanged for the fourth time.  Sweep worktree advanced to
`098641086e`.

### Run 11 addendum 5: fourth-round review

Review of `098641086e` (job 760) found one Medium: only `exp` was
recognized as entire, so `sin`/`cos`/`sinh`/`cosh` arguments were
still scanned wholesale.  Fixed (same denominator-only handling; tan,
cot, coth keep their poles and atan its +-I singularities, so they
stay fully risky), with unit tests both ways.  Commit is staged and
waiting on the signing key (retry monitor running); trig output is
essentially absent from this pipeline (rewrite_complex converts to
exp/log), so the sweep is unaffected either way.  The review loop has
converged: round four found no correctness issues, only a
completeness refinement of round three's own refinement.

### Run 11 addendum 6: review loop closed

`b40b70ce0a` ("Treat all entire functions as safe in _nontrans_vet()")
signed, pushed, and reviewed clean ("No issues found", job 763).
Severity trajectory across the five review rounds: Dummy leak +
complex-axis correctness break -> soundness holes (zero divisors,
base-case bypass) -> over-rejection refinements -> a refinement of a
refinement -> clean.  The post-fix sweep worktree is at `b40b70ce0a`;
the audit sweep is ~11k cases into t_1 with the re-sweep queued
behind it.

---

## Run 12: full-corpus pre-fix audit (worktree `a1c2226052`)

The item-1 deliverable: every chapter in algebraic mode plus the
transcendental control on t_2/t_3, all solved cases checked against
the numerical oracle (`RISCH_CHECK=expected`).  7h42m serial.
Full per-case WRONG table: `02-rubi-audit-wrong.md` in this gist.

### Headline

Of 4,239 solved cases, **1,705 (40%) had a wrong derivative** at some
sample point:

| class | count | status |
|---|---|---|
| radicand-split (unconditional factor split) | 1,684 | fixed (`e3caaaeb2a`..`b40b70ce0a`) |
| complex-only (split bug visible only at complex points) | 13 | fixed (same commits; spot-checked) |
| dependent-radicands (novel: `is_deriv_k` rewrite) | 8 | fixed (`97ef0340ca`, found by this audit) |

Per chapter (solved / wrong): t_0 106/23, t_1 3,997/1,573, t_2 10/1,
t_3 17/0, t_4 90/90, t_6 19/18.  t_4's cases are the complex
`(I*a*tan(c+d*x)+a)**(3/2)`-family radicands; all fail at *real*
points and are fixed by the branch-ratio commits (spot-checked).

### The novel class this audit found

`sqrt(a + b*x)/sqrt(-a - b*x)` returned `-I*x`: wrong sign wherever
`a + b*x < 0`.  The radicand split never sees it -- `is_deriv_k()`
recognizes `-a - b*x` as `-1` times an existing tower logarithm's
argument, and the rewrite took the principal `log(-1) == I*pi`
unconditionally (`sqrt(-w) -> I*sqrt(w)`, wrong where `w < 0`).  The
same exact-branch-ratio mechanism fixes it (`97ef0340ca`); all 8
corpus instances verify across every instantiation round after the
fix.  This is the "relations among several radicals" TODO of
`_nontrans_power_relations()` manifesting in practice.

### Non-WRONG buckets (no silent buckets)

- `DERIV-OK` 2,383; `DERIV-OK-SPLIT` 75 (correct, per-region
  constants -- the jump-correction acceptance set).
- `UNDECIDED-COVERAGE` 144: 143 are "real rounds fully verified, the
  complex-constants round unevaluatable" -- an oracle artifact:
  `Ne(<exact complex arithmetic>, 0)` Piecewise conditions do not
  auto-evaluate, so the instantiated Piecewise never collapsed.
  Fixed in the checker (`7c4b97c`); the remaining 1
  (`1/sqrt(I*a*sinh(c+d*x)+a)`) is unverified in every round and
  needs a hand check.
- timeouts 85 in t_1 (5 s cap), plus 1 unchecked timeout elsewhere.
- t_5/t_7/t_8 were lost to corpus modules that crash at import
  (`hyper()` with list arguments); runner now skips such modules
  loudly (`f55a8b6`) -- these chapters are unaudited pre-fix and will
  be covered by the post-fix sweep.

### Transcendental control (t_2/t_3, no algebraic towers)

285 solved, 0 genuinely wrong.  The single flagged case,
`log(exp(a+b*x))` -> `a*x + b*x**2/2`, fails only at a complex point
where the *integrand itself* unwinds (`Im(a+b*z)` outside
`(-pi, pi]`); the answer is correct on the real line.  100
`DERIV-OK-SPLIT` (mostly `atan`/`log` form differences vs Rubi, both
correct) -- consistent with the branch-correctness problem being
specific to the algebraic radicand handling, as designed.

### Post-fix re-sweep

Running against `97ef0340ca` (all fixes + repaired runner, so
t_5/t_7/t_8 get covered); the success criterion is the WRONG bucket
collapsing to zero with solve counts intact.

### Run 12 addendum: is_deriv_k review + leak findings

- Review of `97ef0340ca` (job 766) found the ratio was built with a
  one-pass xreplace, leaking tower Dummys for nested radicands like
  `sqrt(log(x))/sqrt(-log(x))` (Tfuncs images reference lower
  generators).  Fixed with the standard sequential highest-first
  substitutions (`efae6e79e7`); the nested case now returns
  `x*sqrt(log(x))/sqrt(-log(x))` and verifies.
- The audit's one all-rounds-unverified case was in fact
  `_t0*RootSum(...)` -- a leaked tower Dummy through a residue term
  (worse than unverified).  risch_integrate() now refuses to return
  non-transcendental results containing internal symbols, and the
  oracle flags such answers statically as LEAKED-SYMBOLS (`72b0a72`).
  Corpus-wide static scan found exactly that one leaked answer.  On
  the fixed branch the case dies in as_poly_1t() with a
  PolynomialError instead (fail-safe; pre-existing crash family).
- The post-fix re-sweep runs t_1 at `97ef0340ca` (the efae6e79e7
  delta provably does not touch that chapter: no nested tower
  radicands, no leaks) and will be advanced to `efae6e79e7` at the
  chapter boundary for t_0 onward.

---

## Run 13: post-fix re-sweep, t_1 (worktree `97ef0340ca`)

The headline chapter of the re-sweep (6h44m serial):

|  | pre-fix (`a1c2226052`) | post-fix (`97ef0340ca`) |
|---|---|---|
| solved | 3,997 | **4,077** |
| genuinely wrong | 1,573 | **0** |
| DERIV-OK | 2,210 | 3,655 |
| DERIV-OK-SPLIT | 71 | 417 |
| unverified | 143 (cx-round artifact) + 1 leak | 1 |

Solve count *rose* (nested rational powers, 7th-roots, and the
dependent-radicand class now integrate).  DERIV-OK-SPLIT grew because
parametric jump corrections are skipped by design (symbolic J) --
these are correct answers with per-region constants, the acceptance
set for the corrections' second pass.

Four cases were initially flagged WRONG, all
`(A + B*x)/(x**k*((a + b*x)**2)**(m/2))` at the complex-constants
round.  Adjudication (finite differences of the antiderivative's
values, mpmath cross-evaluation, per-precision comparison): the
answers are correct; under those constants the residue logarithms'
arguments collapse to `x` itself (a degenerate instantiation), so at
negative sample points the logs sit exactly on their branch cut,
where precisions and engines legitimately disagree by `2*pi*I` times
a coefficient.  The oracle now requires precision-stability and a
lambdify/mpmath cross-engine confirmation before convicting; the four
report UNDECIDED-NUMERICS (cx round) with all real rounds verified.
Calibration gate re-passed.

Remaining chapters (t_0, t_2..t_8) are re-running at `518d57ad37`
(the leak-guard tip; its delta from `97ef0340ca` provably does not
affect t_1).

### Run 13 completion: full post-fix corpus results

All chapters done.  Corpus-wide, solved cases checked by the oracle:

| chapter | pre solved/wrong | post solved/wrong |
|---|---|---|
| t_0 | 106 / 23 | 106 / 0 |
| t_1 | 3,997 / 1,573 | 4,077 / 0* |
| t_2 | 10 / 1 | 9 / 0 |
| t_3 | 17 / 0 | 17 / 0 |
| t_4 | 90 / 90 | 61 / 0 |
| t_5 | (crashed) | 4 / 0 |
| t_6 | 19 / 18 | 13 / 0 |
| **total** | **4,239 / 1,705 (40%)** | **4,287 / 0** |

*t_1's four recorded WRONGs are the adjudicated branch-cut
evaluation artifacts of the previous section (answers proven correct;
oracle hardened afterward).  DERIV-OK-SPLIT total 425 (the
jump-correction second-pass acceptance set).  Timeouts t_1 948 ->
1,044 (+10%), median per-case time 0.167 -> 0.173 s -- the
correctness machinery is essentially free.  t_4 90 wrong -> 61
correct (the rest now honestly fail or time out); same shape in t_6.
t_7/t_8 have no oracle-checkable solves (their radical cases do not
solve); 13 corpus modules skipped as BROKEN-MODULE.

The one unverified t_1 case, sqrt(sqrt(1/x) + 1/x), is another
leaked-Dummy answer -- t_1 ran at 97ef0340ca, which predates the
leak guard; at the current tip (518d57ad37) the guard catches it and
returns an honest unevaluated Integral.  This validates the
residual-integral guard on a case nobody constructed.

**Bottom line: every genuinely wrong answer in the corpus is gone,
with a net gain of 48 solved cases and no measurable cost.**

### Run 13 closure: the t_1-at-97ef0340ca footnote, measured

Since one nested-radicand case disproved the "delta cannot affect
t_1" reasoning, the closure was made empirical: all 337 t_1 cases
with nested fractional powers re-ran at `518d57ad37`.  Zero solved
cases changed answer or verdict; the 10 classification deltas are 7
timeout->NIE and 2 timeout->partial (non-answers either way), plus
the known leaked case now degrading to partial under the leak guard.
A `_[ts]\d` scan over all post-fix results confirms that leaked case
is the only one.  Final solved count at the tip is therefore 4,286
(the leaked "solve" was never real).

---

## Run 14 (2026-08-18): algebraic=True becomes the default

Aaron flipped the default; plain integrate() now builds algebraic
towers automatically.  Suite audit and fallout (one commit, see the
plan file for details):

- integrals package: unchanged runtime (~100 s), all 437 tests + 85
  doctests pass after updates.
- Two genuine fallout bugs fixed: the integrals.py
  NonElementaryIntegral stamp overriding the algebraic degradation
  (surfaced via series() in test_issue_23942), and non-canonical
  factor() signs making structurally equal radicands split
  differently under different symbol names (test_issue_22527) --
  split factors are now sign-normalized by leading coefficient in x,
  which the branch ratio makes correctness-neutral.
- Two historical expected answers were themselves wrong for negative
  parameters and are now correct: issue 5462
  (integrate(1/(x**2+y**2)**(3/2), x), wrong sign for y < 0) and
  issue 10211 (double integral, odd-in-h expectation for an
  even-in-h integrand).  integrate(sqrt(x)*(1+x)) drops its meijerg
  Piecewise for sqrt(x)*(6*x**2 + 10*x)/15.
- Remaining expectation diffs are form-level: uncancelled same-base
  radical products (the output-form pass remains the open item) and
  conds Piecewise guards on definite integrals.
- Corpus pilots unchanged after the flip + canonicalization.

### Run 14 addendum: the conds='piecewise' degenerate-branch chain

Reviews 786-791 of the default-flip drilled into what a
parameter-degenerate Piecewise branch can honestly say for algebraic
towers (the transcendental t == 1 fallback is meaningless there).
Five commits converged on: fully-integrated level -> degenerate
branch = Integral(a/d - i) - ret (assembles to exactly the
unevaluated rest of the level); partially-integrated level with
undecidable parametric denominator -> whole level unevaluated (no
branch value survives the substitution); provably nonzero
denominator -> no branch at all.  Wrong turns caught en route: a
whole-level fold broke the (ans, i) retry contract (20 test
regressions, pre-commit); "formal telescoping" left two Integrals
each divided by the vanishing parameter (review 789); the bailout
over-fired on qds == 1 (review 790).  Plus a latent Poly-unification
crash in the residual arithmetic, now Expr-level.  Review 791: clean.

Corpus impact: none on capability -- but honest degenerate branches
carry an unevaluated Integral, which the runner's bare has(Integral)
counted as partial (28 parametric trinomial solves "vanished").  The
runner now classifies on the generic branch and records a
degenerate_unevaluated flag; pilot counts and verdicts fully
restored (45 solved / 0 wrong).

---

## Three-way branch comparison — 2026-08-19

Full write-up in `01-RISCH_BRANCH_COMPARISON.md` in this gist; per-case data
in the `branch-cmp-heb-*.jsonl` and `branch-cmp-blake-algebraic.jsonl`
files.

This run moves off the ad-hoc `risch_test_suite_runner.py` onto the
[integration-test-suites](https://github.com/asmeurer/integration-test-suites)
repo, which collects the Rubi corpus together with the Hebisch, Blake and
MIT Integration Bee suites (80,063 problems) behind one runner.  Two
things changed methodologically:

- The **Hebisch suite** is now the transcendental measure.  Every one of
  its integrands is the expanded derivative of a known exp-log
  expression, so every case is elementary by construction — a much
  sharper instrument than the radical-free slice of Rubi used before.
- Per-case time limits are enforced by **killing a forked child**.  A
  `SIGALRM` only lands between bytecodes, and one Hebisch case with a
  triple-nested exponential hung the numerical oracle indefinitely,
  which the old in-process alarm could not break.

Results, 2,000 Hebisch cases on each of the three branches, joined per
case:

| branch | SOLVED | timeout | NIE | error | CLAIMS-NE | WRONG (of solved) |
|---|---|---|---|---|---|---|
| master `bd4ee7fc6d` | 1825 | 86 | 48 | 39 | 2 | 30 |
| risch-rde-cancellation `bf88623d8e` | 1845 | 86 | 56 | 13 | 0 | 31 |
| risch-algebraic `757fa4fa7e` | 1848 | 88 | 51 | 13 | 0 | 31 |

- master → rde-cancellation: **+29 solved, −9 solved**, both false
  nonelementary claims gone, 26 of 39 crashes fixed.
- **8 of the 9 losses are genuine regressions** (master's answer verified
  correct): cases 0, 433, 528, 647, 821, 920, 1613, 1783.  The ninth
  (1940) is an improvement — master was wrong there.
- **2 new wrong answers**, cases 221 and 1704, both crashes on master
  that the branch now answers incorrectly.  *[2026-08-20: per
  `01b-WRONG_ANSWERS.md`, these are the pre-existing principal-branch
  rewrite defect, not a new mechanism.]*
- **29 wrong answers are pre-existing on master** and unchanged by this
  work: ~1.6% of the Hebisch integrals `risch_integrate` claims to solve
  are not antiderivatives.

Algebraic axis, 1,500 Blake cases (pseudo-elliptic, hyperelliptic,
nested radicals):

| branch | attempted | SOLVED | partial | NIE | timeout | error | WRONG |
|---|---|---|---|---|---|---|---|
| master | 200 (sample) | 0 | 0 | 200 | 0 | 0 | — |
| risch-rde-cancellation | 200 (sample) | 0 | 0 | 200 | 0 | 0 | — |
| risch-algebraic, `algebraic=True` | 1500 | 291 | 818 | 313 | 73 | 5 | **0** |

Stock `risch_integrate` has no algebraic case and rejects all of these
immediately, so the whole 291 is new capability — and on a suite the
experiment was never tuned against, still with zero wrong answers.


### Follow-up — the wrong answers are fixed (2026-08-20)

Both doors of the principal-branch defect are closed on
`risch-rde-cancellation`:

- `562d069b5e` — log side: `_log_part()` integrates with an opaque
  constant and backsubstitutes the exact locally-constant difference
  `log(arg) - u`; a gate keeps the principal constant in the one
  everywhere-exact case (single tower log, coefficient 1, positive
  constant).
- `3c5b649612` — exp side: the tower had integrated these correctly all
  along; the bug was the backsubs pair restoring `exp(q*u)` as the
  principal root `exp(u)**q` even for radicals the construction had
  invented internally.  The pair is now recorded only for integer
  powers or notation present in the user's own integrand.
- (Those two were `6d3b5d3392`/`083bdb6e8e` before the 2026-08-20
  typing-move restack; originals on
  `backup/risch-rde-cancellation-20260820b`.)  Review follow-ups
  `0b77ab246b` (backsubs folded into `newf` before a restart's
  `reset()`, so the `_log_branch` Dummy no longer leaks into results)
  and `d7dafa43c1` (user exp-radicals folded as `ratio*exp(q*u)` with
  an opaque ratio, so mixed `sqrt(exp(x)) + exp(x/2)` input is exact
  off the real line) closed the two wrong-answer leaks found in the
  fixes.

Rerun of the identical 2,000 Hebisch cases (same runner, `--isolate`,
oracle with symbolic-proof fast path):

| | pre-fix | post-fix |
|---|---|---|
| verified WRONG | 31 | **0** |
| SOLVED | 1845 | 1851 (all `DERIV-OK-PROVEN`) |
| CLAIMS-NE | 0 | 0 |

Still open, tracked in `01b-WRONG_ANSWERS.md` terms: the `sympows` door
(`exp(g*(log(const) + u))` for symbolic powers — not exercised by the
Hebisch corpus), the 6 `parametric_log_deriv` NIE regressions vs
master, and the 13 `error:PolynomialError` cases — the last of which
`025e390835` (`residue_reduce` done per §5.6 with `gcd_z`) has since
closed: 12 of 13 → SOLVED, WRONG stays 0; the 13th (Hebisch 274) fails
elsewhere, on `E` and `exp(1/2)` as independent constant generators.

---

## MIT Integration Bee official suite — 2026-08-21

Write-up in `09-mit-bee-official-risch.md`; per-case data in the
`mitbee-*.jsonl` files (master, `risch-rde-cancellation`,
`risch-algebraic` through `risch_integrate`, and `risch-algebraic`
through `risch_integrate(..., algebraic=True)`).  Headline:
`risch-algebraic` 98 solved vs master 84 of 263 indefinite cases, zero
losses, zero wrong (all `DERIV-OK-PROVEN`); master's one wrong answer
(`log(x**2) - 2*log(2*x)`, the principal-branch defect) is fixed on
both branches.

## Structure-constant guards: decide or degrade — 2026-08-21

`15e76e361e` and `3b072169b7` on `risch-algebraic` (details in
RISCH_ALGEBRAIC_PLAN.md): the last four `NotImplementedError` raises on
non-rational structure-theorem solutions now either decide (a unique
solution with a provably irrational entry is a proven "no relation",
so `2**log(x)` towers stay proven transcendental) or answer "no
relation" and set `DE.transcendental = False`, routing the result
through the degradation/vetting machinery.  Hebisch 400-case spot
check 365 -> 368 solved, all proven; Blake 1,500-case sweep unchanged
(303 solved both sides, identical results).
