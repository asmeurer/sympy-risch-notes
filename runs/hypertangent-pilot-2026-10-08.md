# `risch-hypertangent` pilot (2026-10-08)

The first corpus measurement of the Phase 5 branch (tan/atan towers,
5a-5e done).  Purpose: decide whether a full real-trig run is worth
doing now.  Two slices, both through `--engine risch`
(`risch_integrate(f, x)` directly, not `integrate()`), serial, on the
plain checkout.

- sympy: `risch-hypertangent` tip `66bc72d6b8` (2026-08-22)
- corpus: `sympy/integration-test-suites` `871364f` (2026-09-13)
- baselines: the 2026-08-21 MIT Bee runs on master `8454607030` and
  `risch-rde-cancellation` `d7dafa43c1` (corpus `4d1aacc`; all 263
  integrand strings identical at both corpus commits)

```
python -m integration_test_suites.run --engine risch --sympy-path <checkout> \
  --suite mit_bee_official --filter risch-attemptable --indefinite-only \
  --timeout 5 --check --check-timeout 20 --isolate --results mitbee-hypertangent.jsonl

python -m integration_test_suites.run --engine risch --sympy-path <checkout> \
  --suite rubi --source-prefix 4 --filter trig-rational --indefinite-only --limit 200 \
  --timeout 5 --check --check-timeout 20 --isolate --results rubi4-hypertangent.jsonl

python -m integration_test_suites.run --engine risch --sympy-path <checkout> \
  --suite rubi --source-prefix 4 --filter trig-rational --indefinite-only --limit 60 \
  --timeout 10 --isolate --results rubi4-nocheck.jsonl
```

## MIT Bee official, 263 indefinite cases (4 min)

| | master | rde-cancellation | **hypertangent** |
|---|---|---|---|
| SOLVED | 84 | 84 | **157** |
| NIE | 169 | 169 | 90 |
| timeout (5 s) | 6 | 6 | 13 |
| crash | 0 | 0 | 2 |
| CLAIMS-NE | 0 | 0 | **1 (wrong)** |
| WRONG (oracle) | 1 | 0 | **0** |

Per case against both baselines: 84 SOLVED stay SOLVED, 73 NIE become
SOLVED, 0 lost, 90 NIE stay NIE, 7 NIE become timeouts, 1 NIE becomes
a crash each of two kinds, 1 NIE becomes a wrong nonelementary claim.
All 157 answers verified (153 `DERIV-OK-PROVEN`, 2 `DERIV-OK-SPLIT`,
2 `DERIV-OK`).

- **The 73 new solves** are exactly the real-trig cases the old code
  rejected with "Trigonometric and hyperbolic extensions are not
  supported": `sec x`, `1/(1+sin x)`, `cos^6 x`, `tan^4 x`,
  `sin(2x) cos(3x)`, `sin(sin x) cos(sin x) cos x`,
  `cos(x) cos(sin x) cos(sin(sin x))`,
  `(cos x + cos(x+2π/3) + cos(x−2π/3))²`, `exp(2x) cos(3x)`,
  `x atan x`, `sin(4 atan x)`, `cos(2026x)² cos(1013x)`, ... (full list:
  `cls` NIE in `mitbee-risch-master.jsonl`, SOLVED in
  `mitbee-hypertangent.jsonl`).  Four of them took 20-22 s
  (`1/(9cos²x + 4sin²x)`, `sin(2x)cos(3x)`, `1/(1+cos²x)`,
  `(cos x − sin x)/(2 + sin 2x)`): the integration itself is fast, the
  oracle is slow on the tangent-form answer.
- **The 90 remaining NIEs** are all outside Phase 5's scope: 15
  hyperbolic / asin / acos (the documented "needs
  `rewrite_complex=True`" gap), 2 `root counting not supported over
  QQ_I`, and 73 algebraic integrands (radicals; the transcendental
  Risch has no algebraic case).
- **Wrong nonelementary claim:** `sin(x + sin x) − sin(x − sin x)`
  comes back as `NonElementaryIntegral`.  It equals `2 cos x sin(sin x)`,
  whose integral is `−2 cos(sin x)`, and that form *does* integrate on
  the branch.  The tower for the sum is `[tan(x/2), tan((sin x − x)/2)]`
  (the second argument is picked from the second term and the first
  term is rewritten through it with the addition formula): a valid
  tower in which the answer is `−2[(1 − t₀t₁)² − (t₀ + t₁)²] /
  [(1 + t₀²)(1 + t₁²)]`, so the integration algorithm, not the tower
  builder, decides wrongly.  Nested tangent, denominator purely the
  special polynomial `1 + t₁²`, `η = −t₀²/(1 + t₀²)` nonconstant.  This
  is the one correctness failure of the pilot and is distinct from the
  documented nested-tan `NotImplementedError`.  **Fixed 2026-10-09
  (`1ad2ea09da`)**: the coupled system over `Q(x)(t₀)` is solved as a
  Risch differential equation over a field containing `√−1`, where the
  special polynomials of `t₀` are `t₀ ± √−1`, not `t₀² + 1`;
  `special_denom()` missed the `(t₀ + √−1)²` denominator of the
  solution (Bronstein Exercise 6.1, used in his Example 8.4.1).  The
  same root cause made `coupled_DE_system()` take the "real part" of
  a solution by `I → −I`, which is not a solution once `I` is in the
  field; that was the `ExactQuotientFailed` crash below (and the
  book's own Example 8.4.1 system (8.11) crashed the same way).  Both
  pilot crashes now integrate correctly (verified by differentiation);
  the `zoo`/`EX` one stopped crashing with the same fix without being
  traced separately, so its mechanism is not confirmed.
- **Crashes** (master NIE'd both, so new classes, not regressions):
  `exp(cos x) cos(2x + sin x)` → `PolynomialDivisionFailed` dividing
  `[EX(zoo)]` by `[EX(1)]` (a `zoo` reaches an `EX` domain);
  `sin x sin(sin x) sin(cos x) + cos x cos(sin x) cos(cos x)` →
  `ExactQuotientFailed`, `_t1**2 + 1` does not divide a polynomial with
  `I` in its coefficients (an imaginary unit leaks into a real tangent
  tower).
- **7 new timeouts** are all huge-degree or many-generator trig:
  `sin(101x) sin^99 x`, `csc²x tan^2024 x`,
  `3 sin(20x) cos(23x) + 20 sin(43x)` (hard kill at 30 s),
  `(tan(1012x) + tan(1013x)) cos(1012x) cos(1013x)/cos(2025x)`,
  `(sec²(1 + log x) − tan(1 + log x))/x²`,
  `1/(cos x cos(x+2π/3) cos(x−2π/3))²`,
  `2020 sin^2019 x cos^2019 x − 8084 sin^2021 x cos^2021 x`.  Master
  rejected them in 0.1 s; the branch tries and does not finish in 5 s.

## Rubi chapter 4 `trig-rational`, first 200 of 6,931 (60 min)

Checked run: **4 SOLVED (all proven), 6 `HeuristicGCDFailed`, 190
"timeout"**.  The timeout figure is not an integrator measurement:

| | count | what happened |
|---|---|---|
| soft timeout, 5 s | 87 | the integration itself exceeded 5 s |
| hard kill, 30 s | 103 | the integration finished and the oracle check blew the 5 + 20 + 5 s child budget |

`sin(a + bx)` alone is logged at 21.6 s; `risch_integrate` takes 0.3 s
on it, the rest is the oracle.  So the slice was rerun without the
oracle and with 10 s per case (first 60 cases): **37 SOLVED, 23
timeout**.  Those 37 are *unverified* by the runner; a numeric spot
check of 10 of them (random, seed 1; `a, b, c, d` and two `x` values
substituted, derivative minus integrand at 30 digits) found all 10
correct to 1e-163.

**One cause for everything on this slice.**  Rubi's trig chapters are
almost entirely `f(a + b x)` with symbolic `a`, `b` (360 of the 6,931
cases are parameter-free).  `_tan_part()` splits every tangent
argument into a constant part and a tower part
(`as_independent(*T, as_Add=True)`), so `(a + bx)/2` becomes the
generator `tan(bx/2)` plus the constant `tan(a/2)`, and `sin(a + bx)`
is expanded with the addition formula.  Consequences, all seen in the
pilot:

- the coefficients live in `Q(a, b, tan(a/2))` and their degree grows
  with the integrand's: `sin(a+bx)^6` 6.9 s, `^7` 14.7 s, `^8` 33 s,
  `sin²(a+bx) cos^7(a+bx)` > 50 s (vs 0.1 s for `sin²(bx)`);
- the multivariate `heugcd` gives up ("no luck") in `splitfactor()`
  during the Hermite reduction on `sec^n(a+bx)/sin^m(a+bx)` (the 6
  crashes);
- the answers come out as rational functions of `tan(a/2)` and
  `tan(bx/2)`: `restore_sincos()` does not fire (its recorded angle is
  `a + bx`, the generator's double angle is `bx`), the expressions are
  large, and the oracle needs minutes to verify them;
- the output form is the documented "shifted angles give `tan(1/2)`
  coefficients" limit of Phase 5e, at corpus scale.

**Substituting values for the constants does not help** (checked the
same day, in answer to the idea of a random-substitution runner mode).
The 60 no-oracle cases rerun with `a = 3/7, b = 5/3` (10 s each) give
the same classification on every case but 6 (4 solves become timeouts,
2 timeouts become `HeuristicGCDFailed`), with per-case times within
0.8-1.5x of the symbolic ones: the cost is the transcendental constant
`tan(a/2)`, which survives substitution as `tan(3/14)`, not the
symbols `a`, `b`.  `sin(5x/3 + 3/7)^6` even takes over 60 s against
6.9 s symbolic.  The converse experiment pins the cause: with a shift
whose half-angle tangent is rational, `a = 2 atan(1/3)` so that
`tan(a/2) = 1/3`, `sin(a + 5x/3)^6` and `^8` take 0.2-0.3 s and come
back in sin/cos form, and the `sec^6(a + bx)/sin(a + bx)` gcd crash
solves in 0.3 s.

The alternative is to keep a single constant shift inside the
generator, `t = tan((a + bx)/2)` with `Dt = (b/2)(1 + t²)`, and only
fall back to the split when the same base angle occurs with several
different shifts (then `tan(c − c')` constants are unavoidable; the
solved MIT Bee case `(cos x + cos(x+2π/3) + cos(x−2π/3))²` is that
situation).  That is a tower-building decision for Aaron, not a bug
fix; until it is made, the Rubi trig chapters measure this one choice
and little else.

## What this says about a full run

- **MIT Bee is done** (above); the branch nearly doubles the solve
  count with no regressions and no wrong answers.
- **Hebisch (2,000 exp-log cases, baseline 1,851 solved / 0 wrong on
  `risch-rde-cancellation`)** has not been run on this branch.  It
  does not exercise the tangent code, but the pilot shows the new
  tower code reaching shared machinery (`EX` domains, `splitfactor`),
  so it is the right regression check and is cheap.
- **Rubi chapter 4 in full (6,931 cases)** would cost roughly 36 hours
  at the pilot's rate with the oracle, and would mostly re-measure the
  shift split.  The 360 parameter-free cases (`--concrete-only`) are
  runnable now.
- Before any full trig run: the wrong nonelementary claim, the two
  crashes, and the shift decision.
