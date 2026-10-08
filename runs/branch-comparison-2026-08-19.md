# Risch branch comparison: master vs risch-rde-cancellation vs risch-algebraic

2026-08-19.  A three-way A/B/C of the Risch work, run from the new
[integration-test-suites](https://github.com/sympy/integration-test-suites)
corpus rather than ad-hoc scripts.  Companion to
[algebraic-run-log.md](algebraic-run-log.md) and to
[RISCH_PLAN.md](../docs/RISCH_PLAN.md) /
[RISCH_ALGEBRAIC_PLAN.md](../docs/RISCH_ALGEBRAIC_PLAN.md).

**Status, 2026-08-21.**  The wrong-answer counts below are the pre-fix
measurement: the 30-31 verified-wrong answers per branch were one
principal-branch defect (root-caused in
[wrong-answers-root-cause.md](wrong-answers-root-cause.md)) and are
fixed on `risch-rde-cancellation` (`562d069b5e`, `3c5b649612` and
follow-ups); the 2,000-case rerun has zero wrong answers and 1,851
solved (see the follow-up section of
[algebraic-run-log.md](algebraic-run-log.md)).
The 13 `PolynomialError` crashes are down to 1 (`025e390835`).  Still
open from this run: the 8 named regressions vs master (6 of them
`parametric_log_deriv` NIEs).  Per-case data in
`data/branch-cmp-*.jsonl` is unchanged (pre-fix).

## Headline

- **Transcendental axis** (2,000 Hebisch cases, all three branches):
  `risch-rde-cancellation` nets **+20 solved** over master — 29 newly
  solved against 9 lost — and eliminates both of master's false
  nonelementary claims and 26 of its 39 crashes.
- **8 of those 9 losses are genuine regressions**, all `SOLVED -> NIE`
  or `SOLVED -> timeout`, and each one is named below.  The ninth is an
  improvement: master returned a *wrong* answer there and the branch now
  honestly declines.
- **The branch introduces 2 new wrong answers** (cases 221 and 1704,
  both `error -> SOLVED` on master, i.e. a crash became a wrong result).
  This is the finding that most wants attention.
  *[Update 2026-08-20: root-cause analysis in
  [wrong-answers-root-cause.md](wrong-answers-root-cause.md)
  shows these are the pre-existing principal-branch log rewrite defect,
  reached once the crash was fixed — the branch adds no new failure
  mechanism.]*
- **29 wrong answers are pre-existing on master** and survive on every
  branch: `risch_integrate` returns a non-antiderivative on ~1.6% of the
  Hebisch cases it claims to solve.  Not caused by this work, but now
  measured.
- **Algebraic axis** (1,500 Blake cases): `risch-algebraic` solves
  **291**, all of them verified correct, **zero wrong**.  Master and
  `risch-rde-cancellation` solve **zero** of these — they raise
  `NotImplementedError` immediately.  The entire algebraic capability is
  new.

## Configuration

| | |
|---|---|
| `master` | `bd4ee7fc6d` |
| `risch-rde-cancellation` | `bf88623d8e` (55 commits ahead of master) |
| `risch-algebraic` | `757fa4fa7e` (82 ahead; contains rde-cancellation) |
| corpus | `sympy/integration-test-suites` at `b0a1083` |
| engine | `risch_integrate`; on the Blake run, `algebraic=True` |
| per-case limit | 5 s, enforced by killing a forked child (`--isolate`) |
| verification | numerical oracle, 20 s per instantiation |

`risch-rde-cancellation` branched from an older master, so a small part
of the master-to-branch difference is unrelated churn; none of the
touched files outside `sympy/integrals/` bear on these results.

Both axes ran the same slice on every branch, so every number below is a
per-case join on `(suite, index)`, not a comparison of totals.

Commands:

```console
$ python -m integration_test_suites.run --engine risch --sympy-path <worktree> \
    --suite hebisch --limit 2000 --timeout 5 --check --check-timeout 20 \
    --isolate --results heb-<branch>.jsonl

$ python -m integration_test_suites.run --engine risch_algebraic \
    --sympy-path <worktree> --suite blake --filter risch-algebraic \
    --limit 1500 --timeout 5 --check --check-timeout 20 --isolate
```

## Transcendental axis: 2,000 Hebisch cases

The Hebisch suite is randomly generated so that every integrand is the
expanded derivative of a known exp-log expression.  Every case is
therefore elementary and in scope for transcendental Risch, which makes
it the sharpest available measure of this work.  No filters were needed.

| branch | SOLVED | timeout | NIE | error | CLAIMS-NE | total s |
|---|---|---|---|---|---|---|
| master | 1825 | 86 | 48 | 39 | **2** | 1655 |
| risch-rde-cancellation | 1845 | 86 | 56 | 13 | 0 | 1691 |
| risch-algebraic | **1848** | 88 | 51 | 13 | 0 | 1705 |

`CLAIMS-NE` is a `NonElementaryIntegral` returned for an integral that
is elementary by construction — a wrong answer of the worst kind.
Master returns two; both branches return none.

Verification of the solved answers:

| branch | DERIV-OK | DERIV-OK-SPLIT | WRONG | undecided |
|---|---|---|---|---|
| master | 1585 | 207 | 30 | 3 |
| risch-rde-cancellation | 1605 | 206 | 31 | 3 |
| risch-algebraic | 1608 | 206 | 31 | 3 |

### master -> risch-rde-cancellation

1,959 of 2,000 cases are unchanged.

| master | rde-cancellation | count |
|---|---|---|
| error | SOLVED | 24 |
| SOLVED | NIE | 7 |
| timeout | SOLVED | 4 |
| error | timeout | 2 |
| SOLVED | timeout | 2 |
| CLAIMS-NE | NIE | 1 |
| CLAIMS-NE | SOLVED | 1 |

Net **+29 solved, −9 solved**.  The 24 `error -> SOLVED` transitions are
the crash fixes; both `CLAIMS-NE` cases are resolved, one into a correct
answer and one into an honest `NIE`.

**The 8 genuine regressions** (master's answer was verified correct):

| case | master | rde-cancellation | master's verdict |
|---|---|---|---|
| `hebisch[0]` | SOLVED | timeout | DERIV-OK |
| `hebisch[433]` | SOLVED | NIE | DERIV-OK |
| `hebisch[528]` | SOLVED | timeout | DERIV-OK-SPLIT |
| `hebisch[647]` | SOLVED | NIE | DERIV-OK-SPLIT |
| `hebisch[821]` | SOLVED | NIE | DERIV-OK |
| `hebisch[920]` | SOLVED | NIE | DERIV-OK |
| `hebisch[1613]` | SOLVED | NIE | DERIV-OK |
| `hebisch[1783]` | SOLVED | NIE | DERIV-OK |

The ninth, `hebisch[1940]`, is **not** a regression: master's answer is
verified WRONG and the branch declines with `NIE` instead.

### The two new wrong answers

Comparing the WRONG sets case by case:

- 29 cases are WRONG on **all three** branches — pre-existing.
- `hebisch[1940]` is WRONG on master only — **fixed** (now `NIE`).
- `hebisch[221]` and `hebisch[1704]` are WRONG on
  `risch-rde-cancellation` and `risch-algebraic` but **not** on master.

Both new ones were `error` on master, so the branch converted a crash
into a confidently wrong result.  `hebisch[1704]` appears in the
"newly solved" column above, which is exactly why counting solves without
verifying them is not enough.

### risch-rde-cancellation -> risch-algebraic

1,994 of 2,000 unchanged — the algebraic work leaves the transcendental
path almost exactly as it found it, which is what it should do.

| rde-cancellation | algebraic | count |
|---|---|---|
| NIE | SOLVED | 4 |
| NIE | timeout | 1 |
| SOLVED | timeout | 1 |

One case, previously solved, now times out within the 5 s budget.

## Algebraic axis: 1,500 Blake cases

Sam Blake's suite is algebraic by construction — pseudo-elliptic,
hyperelliptic and nested-radical integrands.  Filtered with
`--filter risch-algebraic` (concrete rational exponents, elementary, at
least one true radical); the filter removed nothing, as expected.

| branch | attempted | SOLVED | partial | NIE | timeout | error |
|---|---|---|---|---|---|---|
| master | 200 (sample) | 0 | 0 | **200** | 0 | 0 |
| risch-rde-cancellation | 200 (sample) | 0 | 0 | **200** | 0 | 0 |
| risch-algebraic (`algebraic=True`) | 1500 | **291** (19.4%) | 818 | 313 | 73 | 5 |

Master and `risch-rde-cancellation` reject all 200 sampled cases in
under a second between them: stock `risch_integrate` has no algebraic
case at all, so a 200-case sample is enough to establish the baseline
of zero.

Verification of the 291 solved:

| verdict | count |
|---|---|
| DERIV-OK | 290 |
| DERIV-OK-SPLIT | 1 |
| **WRONG** | **0** |

**Zero wrong answers on the algebraic axis.**  The degrade-to-`Integral`
policy and the tower-level acceptance filter continue to hold at this
scale, on a corpus the experiment has not been tuned against.

The 818 `partial` results are honest unevaluated integrals, and the 5
`error:NotInvertible` cases are worth triaging.

## What this says about the work

The rde-cancellation branch is a clear net gain on the transcendental
axis — more solved, no false nonelementary claims, two thirds fewer
crashes — but it is not a pure improvement: 8 cases that master solved
correctly are now declined or too slow, and 2 crashes turned into wrong
answers.  Those 10 cases are the actionable output of this run.

The algebraic branch adds capability that simply does not exist
elsewhere in sympy, and does it without a single verified-wrong answer.

The 29 pre-existing wrong answers on master are the largest single
finding by count and are independent of this work.  ~1.6% of the
Hebisch integrals that `risch_integrate` claims to solve come back with
something that is not an antiderivative.
