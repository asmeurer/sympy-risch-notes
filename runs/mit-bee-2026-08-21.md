# Risch branches on the mit_bee_official suite

2026-08-21. The corpus gained the `mit_bee_official` suite (every posted
MIT Integration Bee problem with its official answer, 544 cases of which
262 are definite integrals) and definite-integral support. This run
measures the Risch branches on the suite's indefinite section, with the
same invocation and per-case join methodology as the three-way
comparison in `01-RISCH_BRANCH_COMPARISON.md`.

## Headline

- **`risch-algebraic` solves 14 integrals on this suite that master's
  Risch cannot** (98 vs 84 of 263 attempted), with **zero losses and
  zero wrong answers** — all 98 solved cases verified
  `DERIV-OK-PROVEN`. Another 36 cases move `NIE -> partial` (honest
  partial results on radical towers).
- **Master's one wrong answer here is already fixed on both branches.**
  On `log(x**2) - 2*log(2*x)` master returns `-2*x*log(2)` (wrong for
  `x < 0`; the same principal-branch log-rewrite defect root-caused in
  `01b-WRONG_ANSWERS.md`). Both branches return
  `x*(-2*log(2*x) + log(x**2))`, correct everywhere.
- `master` and `risch-rde-cancellation` produce **identical
  classifications on all 263 cases** — this suite has almost no exp-log
  tower content, so the cancellation work is not exercised; the fixed
  wrong answer is the only per-case difference in verification.
- Competition problems are heuristics territory (trig substitutions,
  clever pairings), so the 66% NIE on master is expected: the wins of
  the algebraic branch are exactly the algebraic-function subset.

## Configuration

| | |
|---|---|
| `master` | `8454607030` |
| `risch-rde-cancellation` | `d7dafa43c1` |
| `risch-algebraic` | `3b072169b7` |
| corpus | `asmeurer/integration-test-suites` at `4d1aacc` |
| suite slice | `mit_bee_official`, `--filter risch-attemptable` (19 filtered out; the 262 definite cases are skipped — Risch engines are antiderivative-only) |
| per-case limit | 5 s, `--isolate`; verification 20 s per instantiation |

```console
$ python -m integration_test_suites.run --engine risch --sympy-path <worktree> \
    --suite mit_bee_official --filter risch-attemptable --timeout 5 \
    --check --check-timeout 20 --isolate --results mitbee-risch-<branch>.jsonl
```

## Results (263 attempted indefinite cases)

| branch | SOLVED | partial | NIE | timeout | wrong |
|---|---|---|---|---|---|
| master | 84 | 0 | 173 | 6 | **1** |
| risch-rde-cancellation | 84 | 0 | 173 | 6 | 0 |
| risch-algebraic | **98** | 36 | 123 | 6 | 0 |

On the `risch-algebraic` branch, plain `risch_integrate(f, x)` and
`risch_integrate(f, x, algebraic=True)` give identical results on this
suite (`mitbee-risch-algbranch.jsonl` vs
`mitbee-rischalg-algbranch.jsonl`): the branch recently made the
algebraic machinery the default. To measure `integrate()` without it on
an algebraic integrand, pass `risch=False`.

## The 14 newly solved cases (`risch-algebraic` vs master, all `NIE -> SOLVED`)

| case | source | integrand |
|---|---|---|
| 2 | 2010 qualifier, 3 | `(x + 1)**2*(x - 1)**(1/3)` |
| 37 | 2011 qualifier, 14 | `1/(x**2*(x**4 + 1)**(3/4))` |
| 50 | 2012 qualifier, 2 | `x**(1/4)*log(x)` |
| 119 | 2015 qualifier, 2 | `x/sqrt(2 + 4*x)` |
| 152 | 2016 qualifier, 15 | `x**3*sqrt(x**2 + 1)` |
| 158 | 2017 qualifier, 1 | `x**2/sqrt(x**3 + 2)` |
| 193 | 2018 qualifier, 17 | `1/(1 + x**2)**(3/2)` |
| 212 | 2019 qualifier, 17 | `1/(x + x**(1/3))` |
| 259 | 2022 regular season, 6 | `(3*x**3 + 2*x**2 + 1)/(x**3 + 1)**(1/3)` |
| 315 | 2023 regular season, 7 | `1/sqrt((x + 1)**3*(x - 1))` |
| 331 | 2023 quarterfinal, 104 | `(1 - 2*x)/((1 + x)**2*x**(2/3))` |
| 439 | 2025 regular season, 2 | `x**2*cos(acsc(x))` |
| 468 | 2025 quarterfinal, 113 | `x/(x**3 - 3*x - 2)**(1/3)` |
| 509 | 2026 regular season, 6 | `1/(27*x - x**(-1/3))` |

Two of these (`x**(1/4)*log(x)`, `x**2*cos(acsc(x))`) are cases where
default `integrate()` on master returns a *wrong* Piecewise
(sympy/sympy#30319); the branch's answers are single expressions correct
on the whole domain.

## Not covered here

The definite half of the suite (262 cases) is out of scope for the
Risch engines by design. Its baseline on master is in the corpus repo's
first measurement runs: `integrate` solves 137+2 of the definite cases
it attempts with verified values, `meijerint` 65, with the wrong-value
findings filed as sympy/sympy#30319.

Per-case records: `mitbee-risch-master.jsonl`,
`mitbee-risch-rdecancel.jsonl`, `mitbee-risch-algbranch.jsonl`,
`mitbee-rischalg-algbranch.jsonl`.
