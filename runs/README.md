# Corpus runs: current state

Where each Risch branch stands on each corpus, as last measured.  The
numbers are copied from the write-ups linked in each row; the reasoning
behind them, run by run, is in [algebraic-run-log.md](algebraic-run-log.md).

Since 2026-08-19 every run uses the
[sympy/integration-test-suites](https://github.com/sympy/integration-test-suites)
runner (`python -m integration_test_suites.run`), with every solved
answer checked by its oracle: a symbolic proof of `d/dx F = f`, falling
back to numerical sampling at points straddling every real root of
every radicand factor plus complex points.  `WRONG` means that check
failed and was reconfirmed at higher precision; `CLAIMS-NE` means a
`NonElementaryIntegral` was returned for an integral that is elementary
by construction.

## Status by corpus

### Hebisch (2,000 cases; exp-log, elementary by construction)

| branch | sympy commit | date | SOLVED | WRONG | CLAIMS-NE | source |
|---|---|---|---|---|---|---|
| master | `bd4ee7fc6d` | 2026-08-19 | 1,825 | 30 | 2 | [branch comparison](branch-comparison-2026-08-19.md) |
| risch-rde-cancellation | `bf88623d8e` (pre-fix) | 2026-08-19 | 1,845 | 31 | 0 | [branch comparison](branch-comparison-2026-08-19.md) |
| risch-rde-cancellation | post-fix rerun (`562d069b5e` .. `d7dafa43c1`) | 2026-08-20 | **1,851** | **0** | 0 | [run log, follow-up](algebraic-run-log.md#follow-up--the-wrong-answers-are-fixed-2026-08-20) |
| risch-algebraic | `757fa4fa7e` (pre-fix) | 2026-08-19 | 1,848 | 31 | 0 | [branch comparison](branch-comparison-2026-08-19.md) |

- Every wrong answer on every branch was one defect, the principal-branch
  constant in the log/exp tower rewrite
  ([root cause](wrong-answers-root-cause.md)); fixed on
  `risch-rde-cancellation` by `562d069b5e` + `3c5b649612` (+ `0b77ab246b`,
  `d7dafa43c1`).
- Crashes: master 39, both branches 13 (all `PolynomialError`); 12 of
  those 13 closed since by `025e390835`, the 13th (Hebisch 274) fails on
  `E` and `exp(1/2)` as independent constant generators.
- Still open vs master: 8 named regressions (`SOLVED -> NIE/timeout`,
  6 of them `parametric_log_deriv` NIEs), listed in the branch comparison.
- `risch-algebraic` has not been rerun on the full 2,000 since the fix;
  a 400-case spot check at `3b072169b7` (structure-constant guards,
  2026-08-21) went 365 -> 368 solved, all proven.

### Blake (algebraic: pseudo-elliptic, hyperelliptic, nested radicals)

| branch | sympy commit | date | slice | SOLVED | WRONG | source |
|---|---|---|---|---|---|---|
| master, risch-rde-cancellation | `bd4ee7fc6d`, `bf88623d8e` | 2026-08-19 | 200 sample | 0 (all NIE) | — | [branch comparison](branch-comparison-2026-08-19.md) |
| risch-algebraic, `algebraic=True` | `757fa4fa7e` | 2026-08-19 | 1,500 | 291 | **0** | [branch comparison](branch-comparison-2026-08-19.md) |
| risch-algebraic, `algebraic=True` | `3b072169b7` | 2026-08-21 | 1,500 | **303** | **0** | [run log, structure-constant guards](algebraic-run-log.md#structure-constant-guards-decide-or-degrade--2026-08-21) |
| risch-algebraic, plain `risch_integrate(f, x)` | pre-relaxation tip | 2026-08-21 | all 3,154 | 286 | — | `data/pretip-blake-abort-census.jsonl`: 485 `parametric_log_deriv` aborts, 197 timeouts (8 s) |

Stock `risch_integrate` has no algebraic case, so the whole Blake
capability is the experimental branch's.

### Rubi radical chapters (~16,800 attemptable cases, `algebraic=True`)

| branch | sympy commit | date | oracle-checked SOLVED | WRONG | source |
|---|---|---|---|---|---|
| risch-algebraic, pre-fix | `a1c2226052` | 2026-08-15..18 (Runs 11-13) | 4,239 | 1,705 (40%) | [run log, Run 12](algebraic-run-log.md#run-12-full-corpus-pre-fix-audit-worktree-a1c2226052); [per-case table](rubi-prefix-audit-wrong.md) |
| risch-algebraic, post-fix | `97ef0340ca` / `518d57ad37` | 2026-08-15..18 (Runs 11-13) | **4,286** | **0** | [run log, Run 13](algebraic-run-log.md#run-13-post-fix-re-sweep-t_1-worktree-97ef0340ca) |

- The 1,705 wrong answers were the unconditional radicand split and the
  `is_deriv_k` principal-constant rewrite; the exact-branch-ratio fixes
  (`e3caaaeb2a` .. `b40b70ce0a`, `97ef0340ca`) removed every one with a
  net gain of 48 solves, median per-case time 0.167 -> 0.173 s.
- 425 `DERIV-OK-SPLIT` results (correct, per-region constants) are the
  acceptance set for the jump-correction second pass.
- Since Run 14 (2026-08-18) `algebraic=True` is the default on
  `risch-algebraic`: plain `integrate()` builds algebraic towers.

### MIT Integration Bee official suite (263 indefinite cases)

| branch | sympy commit | date | SOLVED | partial | WRONG | source |
|---|---|---|---|---|---|---|
| master | `8454607030` | 2026-08-21 | 84 | 0 | 1 | [mit-bee-2026-08-21.md](mit-bee-2026-08-21.md) |
| risch-rde-cancellation | `d7dafa43c1` | 2026-08-21 | 84 | 0 | 0 | |
| risch-algebraic | `3b072169b7` | 2026-08-21 | **98** | 36 | 0 | |
| risch-hypertangent | `66bc72d6b8` | 2026-10-08 | **157** | 0 | 0 (+1 wrong CLAIMS-NE) | [hypertangent pilot](hypertangent-pilot-2026-10-08.md) |

Master's one wrong answer is the same principal-branch defect, fixed on
both branches.  The suite has almost no exp-log tower content, so the
cancellation work is not exercised here; the 14 algebraic-branch solves
are the algebraic-function subset, and the 73 hypertangent solves are
the real-trig subset (0 lost, all 157 verified).  The hypertangent
branch also claimed `sin(x + sin x) − sin(x − sin x)` nonelementary (it
is `−2 cos(sin x)`), and crashed on two nested-trig cases; both fixed
2026-10-09 (`1ad2ea09da`, special polynomials `t ± √−1` and the
conjugate equation in the coupled-system solver, see the pilot log).

### Rubi chapter 4 `trig-rational` (6,931 indefinite cases; 360 parameter-free)

| branch | sympy commit | date | slice | SOLVED | WRONG | source |
|---|---|---|---|---|---|---|
| risch-hypertangent | `66bc72d6b8` | 2026-10-08 | first 200, oracle, 5 s | 4 (proven); 190 "timeout", 103 of them the oracle's; 6 `HeuristicGCDFailed` | 0 | [hypertangent pilot](hypertangent-pilot-2026-10-08.md) |
| risch-hypertangent | `66bc72d6b8` | 2026-10-08 | first 60, no oracle, 10 s | 37 (unverified; 10 spot-checked numerically); 23 timeout | — | same |

Pilot only.  Nearly every case is `f(a + bx)` with symbolic `a`, `b`,
and the tower builder splits the shift off as a `tan(a/2)` constant;
the resulting coefficient growth is behind the timeouts, the gcd
failures and the slow oracle.  A full run waits on that tower decision.

### Not measured: `risch-hypertangent` on Hebisch

The Phase 5 branch has had no exp-log regression run.  Hebisch does not
exercise the tangent code, but the pilot shows the new tower code
reaching shared machinery (`EX` domains, `splitfactor`), so the 2,000
cases against the 1,851 / 0-wrong baseline are the next thing to run.

## Open items (as of 2026-08-21)

- The exp-side `sympows` rewrite `exp(b*(log(const) + u))` for symbolic
  powers still takes the principal constant (not exercised by any corpus).
- The 8 Hebisch regressions vs master named in the branch comparison.
- Hebisch 274: `E` and `exp(1/2)` as independent constant generators.
- Constant irrational exponents on a variable base (`x**log(2)`) never
  reach the tower.
- The jump-correction second pass (`DERIV-OK-SPLIT` acceptance set).
- Output-form cleanup of algebraic answers (uncancelled same-base radical
  products).

## Files

| file | what |
|---|---|
| [algebraic-run-log.md](algebraic-run-log.md) | chronological log, Run 0 (2026-08-09) through the structure-constant guards (2026-08-21) |
| [branch-comparison-2026-08-19.md](branch-comparison-2026-08-19.md) | three-way master / rde-cancellation / algebraic comparison on Hebisch and Blake |
| [wrong-answers-root-cause.md](wrong-answers-root-cause.md) | all 32 Hebisch wrong answers traced to the principal-branch rewrite |
| [mit-bee-2026-08-21.md](mit-bee-2026-08-21.md) | the three branches on the MIT Integration Bee official suite |
| [hypertangent-pilot-2026-10-08.md](hypertangent-pilot-2026-10-08.md) | `risch-hypertangent` on MIT Bee and a Rubi trig slice: the first Phase 5 measurement, and why the Rubi trig chapters wait on the shift-handling decision |
| [rubi-prefix-audit-wrong.md](rubi-prefix-audit-wrong.md) | Run 12's per-case table of the 1,705 pre-fix wrong answers (all fixed) |
| [data/](data/README.md) | per-case JSONL results for the runs above |

## Adding a run

Append a dated section to [algebraic-run-log.md](algebraic-run-log.md)
(or a new write-up for a run with its own story), put the per-case
JSONL under `data/` with a row in [data/README.md](data/README.md), and
update the status tables above.  Record the sympy commit, the corpus
commit, the exact `integration_test_suites.run` invocation, and the
per-case time limit; only compare timings from serial runs.
