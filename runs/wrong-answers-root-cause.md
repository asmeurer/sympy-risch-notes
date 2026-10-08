# The wrong answers: all 32 cases, one root cause

**Status update, 2026-08-20 (later):** both doors are now fixed on
`risch-rde-cancellation`.  Commit `562d069b5e` fixes the log side
(Class A + most of Class B); commit `3c5b649612` fixes the exp side —
whose defect turned out to be not in the integration at all but in the
notation-restoring backsubs pair `(exp(q*u), exp(u)**q)` recorded for
internally created radicals.  (Those two were `6d3b5d3392` and
`083bdb6e8e` before the 2026-08-20 typing-move restack; the original
hashes survive on `backup/risch-rde-cancellation-20260820b`.)  Two
review follow-ups closed leaks in the fixes themselves: `0b77ab246b`
(fold backsubs into `newf` before an extension restart's `reset()`,
so the `_log_branch` Dummy no longer escapes into results such as
`log(x) + log(x**2) + exp(x) + exp(x/2 + 1)`) and `d7dafa43c1` (fold a
user's fractional exp-power as `ratio*exp(q*u)` with an opaque
locally-constant ratio, so mixed input like `sqrt(exp(x)) + exp(x/2)`
is right off the real line too).  A rerun of the same 2,000 Hebisch
cases: **zero verified-wrong answers; 1,851 solved, every one with a
symbolically proven derivative.**  The analysis below describes the
pre-fix state.

2026-08-20.  Companion to `01-RISCH_BRANCH_COMPARISON.md`, which counted
30–31 verified-wrong answers per branch on the 2,000-case Hebisch run.
This document identifies every one of them.  Per-case data is in the
`branch-cmp-heb-*.jsonl` files; the raw runs carry the full
integrand/answer/expected strings.

## TL;DR

- **None of the wrong answers are algebraic integrals.**  All 32 distinct
  wrong cases are pure exp-log integrands (the Hebisch suite contains no
  radicals by construction; verified per case).  They live entirely in
  the *transcendental* code, on master, and `risch-algebraic` inherits
  them unchanged.  On the actual algebraic axis (Blake), master emits no
  wrong answers because it emits no answers at all (100% `NIE` on a
  200-case sample), and all 291 of `risch-algebraic`'s solved cases
  verified correct.
- **One root cause explains every case**: when the tower construction
  meets a log (or exp) whose argument is multiplicatively related to
  existing generators, it rewrites it in terms of them **plus a
  principal-branch constant** — `ln(5/x) -> ln 5 - ln x`,
  `ln(-x**2) -> 2 ln x + I*pi`, `ln(exp(x)*x**2) -> x + 2 ln x` — an
  identity valid on x > 0 but off by a branch constant on x < 0 (or off
  the real line).  When that mis-branched term then enters the
  integration *nonlinearly* — multiplied by another log, nested inside
  another log, in a denominator, or inside an exp — the branch constant
  stops being a constant of integration and becomes a genuine derivative
  error.
- 25 cases are **wrong on the real axis** (every conviction at a
  negative real point).  7 cases are **wrong only off the real line**
  and are correct for every real x — defensible answers for real
  integration, flagged because the oracle also samples complex points.
- **The branches introduce no new failure mechanism.**  The two "new"
  wrong answers on `risch-rde-cancellation` (cases 221, 1704) are this
  same pre-existing bug, previously hidden behind a `TypeError` crash
  that the branch fixed.  The one wrong answer the branch *removes*
  (case 1940) becomes an honest `NIE`.

## Where the rewrite happens

`sympy/integrals/risch.py`, in `DifferentialExtension`:

- log side (`_log_new_extension`, ~L576–588): if `is_deriv_k` (in
  `prde.py`) finds that a new log's derivative is a k-linear combination
  of existing tower generators, the log is not added as a new generator —
  the structure theorem forbids it — but rewritten as
  `newterm = log(const) + u`.
- exp side (~L363–379 and ~L479–496): the analogous rewrite through
  `is_log_deriv_k_t_radical`, producing `exp(i.exp*(log(const) + u))`
  and `exp(const*p)*rad` terms, where `rad` can be a fractional power of
  an existing exp generator.

The unification itself is mathematically forced (two logs with dependent
derivatives cannot both be transcendental generators).  The defect is the
constant: `log(const)` is the *principal-branch* constant, correct only
on the connected component where every argument involved is positive.
On the other components the true constant differs (typically by
`2*I*pi`), and no single constant is right everywhere.

### Worked example (case 1462, the smallest)

    f = (6 ln x + 6 ln(-x**2)) / x

The tower rewrites `ln(-x**2) -> 2 ln x + I*pi`.  Correct for x > 0.
For x < 0, `ln(-x**2) = 2 ln(-x) + I*pi = 2 ln x - I*pi`: the rewrite is
off by `2*I*pi`.  Master returns

    F = 9 ln(x)**2 + 6*I*pi*ln x

and because the mis-branched log was *multiplied by another log*, the
`2*I*pi` shows up in `F'` with a factor of `1/x`:

    x = -333/64:  f  = -5.7055 - 7.2455 I
                  F' = -5.7055 - 14.4910 I     (diff = 6*(2*pi*I)/|x|)

Independently confirmed with mpmath at 40 digits, outside the oracle.
At any x > 0 the two agree exactly.  In case 1942 the mis-branched
`ln(3/2/x)` multiplies `ln(x)`, and the error picks up a **real** part
of exactly `4*pi**2 = 39.478...` — differentiating a squared branch
offset.  These are not borderline numerics.

### Why only these 32, when the rewrite fires constantly

The same rewrite fires on hundreds of the 2,000 cases.  When the
mis-branched term enters the answer only *linearly*, the branch error is
a piecewise constant — the derivative is still right everywhere, and the
oracle reports `DERIV-OK-SPLIT` (correct antiderivative, different
integration constant per region).  Many of the ~206 SPLIT cases are
consistent with this mechanism, though SPLIT also arises from the
*expected* answer's own branch conventions and they have not been
individually attributed.  The 32 below are the cases
where the term participates **nonlinearly**, so the offset differentiates
into a real error.  `DERIV-OK-SPLIT` and `WRONG` here are the benign and
malignant faces of the same defect.

## Class A: wrong on the real axis (25 cases)

Every conviction is at a negative real point.  All 25 answers were
explicitly re-verified correct at three positive points (x = 0.51, 2.31,
7.77; relative error at or below 1e-32 — pure roundoff at 35 digits):
the conviction points being negative is not an artifact of sampling
order, and the answers really are right on the positive half-line.
"Guilty rewrite" is the log whose argument is negative (or
sign-flipping) for x < 0, present in the integrand and unified into the
tower with a principal-branch constant.

| case | guilty rewrite(s) | master | rde-cancel | algebraic |
|---|---|---|---|---|
| 141 | `ln(5/x**2)` | WRONG | WRONG | WRONG |
| 221 | `ln(2*x**2)`, nested in `ln(x/ln(2*x**2))` | crash (TypeError) | WRONG | WRONG |
| 384 | `ln(1/x)`, deeply nested | WRONG | WRONG | WRONG |
| 484 | `ln(5/x)` | WRONG | WRONG | WRONG |
| 603 | `ln(5/x)`, `ln(x**2)`, nested | WRONG | WRONG | WRONG |
| 796 | `ln(1/x)` | WRONG | WRONG | WRONG |
| 953 | `ln(x**2)` | WRONG | WRONG | WRONG |
| 1225 | `ln(exp(x)*x**2)` (in denominator) | WRONG | WRONG | WRONG |
| 1236 | `ln(2*x)`, `ln(x**2)` | WRONG | WRONG | WRONG |
| 1252 | `ln(-x/(ln 5 - 1))` | WRONG | WRONG | WRONG |
| 1271 | `ln(2*x)`, `ln(x**2)` | WRONG | WRONG | WRONG |
| 1443 | `ln(3/x)` | WRONG | WRONG | WRONG |
| 1462 | `ln(-x**2)` | WRONG | WRONG | WRONG |
| 1464 | `ln(x**3)` | WRONG | WRONG | WRONG |
| 1529 | `ln(9/x**2)`, nested in `ln(ln(9/x**2))` | WRONG | WRONG | WRONG |
| 1645 | `ln(x**2)`, nested in `ln(ln(x**2))` | WRONG | WRONG | WRONG |
| 1704 | `ln(4/x)`, nested five deep | crash (TypeError) | WRONG | WRONG |
| 1740 | `ln(x**2/ln(5)**2)` | WRONG | WRONG | WRONG |
| 1793 | `ln(1/x)`, nested | WRONG | WRONG | WRONG |
| 1823 | `ln(x**2)` | WRONG | WRONG | WRONG |
| 1898 | `ln(2/x)`, nested in `ln(3/ln(2/x))` | WRONG | WRONG | WRONG |
| 1940 | `ln(x**2)` (inside an exp argument) | WRONG | **NIE** | **NIE** |
| 1942 | `ln(3/2/x)` (times `ln x`) | WRONG | WRONG | WRONG |
| 1966 | `ln(-5*x)` | WRONG | WRONG | WRONG |
| 1996 | `ln(x**2)` | WRONG | WRONG | WRONG |

## Class B: correct on all of R, wrong off the real line (7 cases)

These use identities that hold for every real x but not on the complex
plane.  All 7 were explicitly re-verified correct at negative real
points (x = -1.37, -5.203) in addition to the oracle's own real grid.
As real-variable antiderivatives they are arguably *correct*;
they are listed separately so the headline "wrong" count can be read
either way (strict: 32; real-axis only: 25).

| case | mechanism | valid on R because |
|---|---|---|
| 292 | `ln(x*exp(x-1)) -> ln x + x - 1` | both sides gain the same `I*pi` for x < 0 |
| 458 | `ln(3/5/x)`, `ln(x**2)` unified; offsets stay linear on R | error is constant per real interval |
| 535 | exp-radical: answer contains `exp(27*x**2)**(2/27)` | `exp(27x**2) > 0` on R, principal root exact |
| 856 | `ln(-exp(u)) -> u + I*pi` | `-exp(u) < 0` for real u, identity exact |
| 882 | `ln(x**2)`, `ln(ln(x**2))` | offsets stay effectively linear on R |
| 1549 | `ln(exp(x**2)**2 / 16) -> 2x**2 - 4 ln 2` | argument positive on R |
| 1878 | `ln(-exp(x)) -> x + I*pi` | exact for real x |

## The three cases that change across branches

- **221, 1704** (`error -> WRONG` on `risch-rde-cancellation`): on
  master both die with `TypeError: '>' not supported between instances
  of 'Poly' and 'int'` — the malformed-Poly bug the branch fixes.  With
  the crash gone, they proceed into the same principal-branch rewrite as
  everyone else (`ln(2*x**2) -> 2 ln x + ln 2`, `ln(4/x) -> ln 4 - ln x`
  — both visible verbatim in the returned answers) and join Class A.
  **The branch did not create a new bug; it uncovered the reach of an
  old one.**
- **1940** (`WRONG -> NIE`): master emits an answer that mishandles
  `ln(x**2)` inside an exponential's argument; the branch's stricter
  `parametric_log_deriv` declines instead.  One fewer wrong answer.

## What a fix would look like

The unification cannot simply be skipped — `is_deriv_k` firing is
exactly the structure theorem saying the new log *must* be expressed in
terms of the tower.  The options are about the constant:

1. **Region-aware constant in backsubstitution**: keep `log(const) + u`
   internally (any constant is valid for the formal integration), but on
   backsubstitution restore the original expression — the tower knows it
   replaced `ln(-x**2)` by `2 t0 + I*pi`; substituting `t0 -> ln x`
   could instead substitute `2 t0 + I*pi -> ln(-x**2)` where the
   combination appears.  This is the principled fix and also what the
   `DERIV-OK-SPLIT` cases want.
2. **Assume-positive gating**: only apply the principal-branch constant
   when the argument is provably positive for the declared domain
   (e.g. `x > 0`), otherwise emit a `Piecewise` constant or decline.
3. At minimum, **document the domain of validity**: every answer
   involving such a rewrite is correct on the component of R+ — the
   current behavior silently extends it to all of C.

The 7 Class B cases would be resolved by (3) alone; the 25 Class A cases
need (1) or (2).

*(2026-08-20: option 1 is what landed — `562d069b5e` integrates with an
opaque `_log_branch` Dummy and backsubstitutes the exact
`log(arg) - u`; `3c5b649612`/`d7dafa43c1` do the same for the exp-radical
notation.  The exp-side `sympows` rewrite `exp(b*(log(const) + u))` for
a symbolic power `a**b` still uses the principal constant; the Hebisch
corpus doesn't exercise it.)*

## Provenance of the verdicts

WRONG here means: the numerical oracle found `D(ours) != f` at a sample
point at working precision, reconfirmed at double precision, and
cross-checked with an independent mpmath evaluation via `lambdify`.
For this document, cases 1462 and 1942 were additionally re-derived by
hand at 40 digits outside the harness, every Class A case was re-checked
at three positive real points, and every Class B case at two negative
real points — all outside the oracle.  The expected corpus answers
play no role in the verdict (a mistranslated expected answer cannot
produce a false WRONG); they were used only to see what the correct form
looks like.
