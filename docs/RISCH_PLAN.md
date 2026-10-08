# Plan: completing the transcendental Risch algorithm in SymPy

Scope: the transcendental algorithm from Bronstein, *Symbolic Integration I*
(2nd ed. section numbers used throughout; the OCR'd 2nd-edition PDF is at
`~/Dropbox/papers/symbolic-computation/_books/`, PDF page = book page + 16).
Algebraic extensions (Volume II territory) are explicitly out of scope.
Line numbers originally referred to master at 89796fa512.

## Status (updated 2026-08-21)

- **Phase 0 — DONE.** PR #30180 (branch `risch-gaps`, 16 commits),
  awaiting upstream review.  Every fix has an integral-level or
  direct-call reproducer as a regression test.
- **Phases 1–4 — DONE.** Branch `risch-rde-cancellation`, stacked on
  `risch-gaps` (open its PR with a stacking note against master; the
  diff collapses when #30180 merges).  Eight commits:
  `b6f6a5d9b7` (prde_cancel_liouvillian eta-level + residual-sign
  bugs), `96610bfc54` (is_deriv_in_field + the three RDE cancellation
  cases), `5a4e8585b2` (prde_no_cancel_b_equal), `6c1e432340` +
  `2ab1c1cfd7` (structure-theorem parametric_log_deriv, plus the
  constant_system-misuse fix), `2172cd9844` + `5635f4788d`
  (limited_integrate_reduce erratum fix and wiring), and a
  direct-coverage test commit.
- **Value-coverage audit — DONE** (section below).
- **Symbolic-constant Piecewise audit — DONE** (`81b9d588fc`; item 6
  below).
- **Soundness/termination cleanup — DONE** (`7b4e227ad6`,
  `53ab4e4601`, `950f7ce629`; items 2–3 below): dead parametric
  dispatch removed from `solve_poly_rde()`, the unsound `n = 5` guess
  removed from `param_rischDE()`, `spde()` guarded against the
  `n = oo` hang.
- **Per-commit roborev (codex) review — DONE** (2026-08-08, jobs
  581–609, all 29 commits since master): 12 clean, 17 with findings.
  Ten findings were per-commit-isolation artifacts (flagging things
  fixed in later commits of the series) or moot; the real ones are
  fixed in `d3b3da71ec` (cancel_exp unconditional t**(-m) stripping —
  an actual wrong-answer bug in the Phase 1 code), `e8ce2fa9d4`
  (spde() n == oo guard was rejecting solvable one-pass reductions;
  now a generous pass cap), and `34959151d9` (recognize_derivative
  special-factors-first ordering, case-enumeration messages,
  documentation of the mutation-verified inertness of the
  prde_cancel_liouvillian sign, specialization-TODO extensions, and
  five test-coverage additions).  Notable review discovery: the
  1st-edition sign misprint was behaviorally inert all along (see
  `BRONSTEIN_ERRATA.md` erratum 3).  The findings against Phase 0
  commits are fixed on `risch-gaps` itself (`ec8fbc016b`, part of PR
  #30180): the recognize_derivative ordering, the case enumerations,
  and four test-coverage additions.
- **PR scope decision (Aaron, 2026-08-07):** the
  `risch-rde-cancellation` PR ends here (plus whatever review turns
  up).  The hypertangent work (Phase 5) and the structure-theorem
  work (real versions, and the `parametric_log_deriv` no-solution
  side, item 1) go in future PRs.
- **Rioboo real-arctangent output (§2.8) — DONE** (2026-08-13/14,
  `3d200fa696`, `ad8f111eca`, `460ffaa8d3`):
  `residue_reduce_to_basic()` now rewrites residue terms via
  `log_to_real()` from `rationaltools.py` (resolving the long-standing
  TODO in `residue_reduce()`), so e.g.
  `risch_integrate(atan(exp(x) + 1).diff(x), x)` returns
  `atan(exp(x) + 1)` instead of a complex-log `RootSum`.  The
  rewriting applies whenever all the residues can be computed
  explicitly — all-real residues become explicit logarithms too, for
  consistency with `ratint()` (Aaron will confirm this policy with the
  other maintainers; `log_to_real()` grew a `complex_only` keyword to
  make it easy to flip back to rewriting only when it removes complex
  logarithms).  Terms with uncomputable residues fall back to
  `RootSum`, and the rewriting is skipped when `I` appears in a term
  or the extension tower (checked by the caller, since realness is a
  decision about whether to call, not part of the algorithm).
  `log_to_real()` also gained a guard skipping the arc-tangent term
  when `A` or `B` is the zero polynomial (previously a division error
  when `h` does not involve the resultant variable).
- **Principal-branch constants in the log/exp tower rewrite — DONE**
  (2026-08-20, on `risch-rde-cancellation`): `562d069b5e` (log side:
  when `is_deriv_k` rewrites a new log through existing generators,
  `_log_part()` integrates with an opaque constant and backsubstitutes
  the exact locally-constant difference `log(arg) - u` instead of the
  principal `log(const)`), `3c5b649612` (exp side: the notation-restoring
  backsubs pair `(exp(q*u), exp(u)**q)` is recorded only for integer
  `q` or notation present in the user's integrand, never for radicals
  `_exp_part()` invents), plus review follow-ups `0b77ab246b` (fold
  backsubs into `newf` before a restart's `reset()`, closing a
  `_log_branch` Dummy leak) and `d7dafa43c1` (user exp-radicals folded
  as `ratio*exp(q*u)` with an opaque ratio, so mixed `sqrt(exp(x)) +
  exp(x/2)` input is exact off the real line).  Hebisch corpus (2000,
  5 s): 31 verified-wrong → 0, 1,851 solved, all with symbolically
  proven derivatives.  Full analysis in `01b-WRONG_ANSWERS.md` of the
  run-log gist.
- **`residue_reduce()` PolynomialError (issue #26502) — DONE**
  (2026-08-20, `025e390835` on `risch-rde-cancellation`): the
  Lazard-Rioboo-Trager step factored `lc_t(S_i)` as a Poly in `t`
  (trivially) and took the gcd with `s_i` over the generators
  `[1/x, 1/t0, ..., x, t0, ...]`, which raised whenever a coefficient
  denominator was a non-monomial polynomial in `x` (e.g. `1/(x**3 +
  2*x**2 + x)`, as for `D(log(log(x) + 1/(x + 1)))`).  Now follows §5.6
  literally: square-free factorization in `z` over `k`, divide by
  `gcd_z(A_j, s_i)**j` (full multiplicity, so `lc` is also guaranteed
  invertible mod `s_i` — the `NotInvertible` symptom seen on the
  algebraic branch).  Hebisch corpus (2000, 5 s): 12 of the 13 crashes
  → SOLVED, WRONG stays 0, timings unchanged.  The 13th (index 274)
  fails elsewhere: its tower has `E` and `exp(1/2)` as independent
  generators, so `hermite_reduce` cannot see that `t0**2*exp(5/2) +
  8*t0*exp(3) + 16*exp(7/2)` is a perfect square (see the
  constant-field bullet under Phase 7).  The `ratint_logpart()`
  manifestation of #26502 was fixed earlier in `e32f22cd72`.
- **Phase 5 STARTED** (2026-08-15, branch `risch-hypertangent`,
  stacked on `risch-rde-cancellation`):
  - Adversarial review of the 2013-era recognizers — DONE (commit
    `9100aa2753`): `laurent_series()`/`recognize_derivative()`
    crashed with ExactQuotientFailed on any denominator with a
    special factor (D(F) is never invertible mod F at special
    primes, which the construction requires); they now raise
    NotImplementedError, with conclusive False still returned from
    the decidable part of mixed factors.
    `recognize_log_derivative()` wrongly returned True on non-simple
    inputs (e.g. `1/x**2`; constant Rothstein-Trager resultant makes
    the integer-root check vacuous) — the normal-denominator
    necessary condition is now checked, and its docstring states the
    actual filter contract (False conclusive, True not).  Plus
    docstring/reference fixes and removal of the stale TODOs on
    `special_denom()`/`bound_degree()` (their tan branches have been
    done since Phase 0).
  - **5b core — DONE** (commit `1474d1268e`): new module
    `sympy/integrals/cde.py` with `coupled_DE_system()` (via the
    equivalent RDE over k(sqrt(-1)), which the existing `rischDE()`
    machinery handles — verified on the book's no-solution
    tan(x**2) system, Example 6.6.2 and the inner system of Example
    8.4.1) and `coupled_DE_cancel_prim/exp/tan()` (§8.1/§8.2/§8.4,
    specialized to a == -1; Example 8.4.1 reproduces exactly and the
    prde helpers `is_log_deriv_k_t_radical_in_field()` and
    `parametric_log_deriv()` work over k(sqrt(-1))).  **Two new
    errata found** (BRONSTEIN_ERRATA.md 4 and 5, both editions): the
    `CoupledDECancelTan` spec's matrix prints `b0 + n*eta*t` in the
    bottom-right entry (should be `b0 - n*eta*t`, equal diagonals),
    and `CoupledDECancelExp`'s final degree condition tests
    `deg(p2)` where the bounded quantity is `deg(q2)`.  Not yet
    done from the 5b description: the "two independent RDEs when
    sqrt(-1) IS in k" variant of `coupled_DE_system()` (no caller
    needs it until the rewrite_complex paths do).
  - Path correction: the Risch papers cited under Phase 5 live in
    `~/Dropbox/papers/symbolic-computation/` (not
    `~/Dropbox/papers/Risch/`), e.g. "Davenport - On the Parallel
    Risch Algorithm (III) - Use of Tangents.pdf", "Bronstein -
    Simplification of Real Elementary Functions.pdf", "Jeffrey &
    Rich 1994 - The Evaluation of Trigonometric Integrals Avoiding
    Spurious Discontinuities.pdf".
- **Phase 5c — DONE** (2026-08-15, branch `risch-hypertangent`):
  - `cancel_tan()` in rde.py (PolyRischDECancelTan, §6.6) wired into
    `solve_poly_rde()`'s cancellation dispatch (commit `72ba3cfcdf`).
    `rischDE()` now solves hypertangent cancellation problems
    end-to-end for the first time: equation (6.21) reproduces
    Examples 6.5.3 + 6.6.1 through the full pipeline.  **New erratum
    found** (BRONSTEIN_ERRATA.md 6, both editions): the book's
    `n == 1` early return is unverified and returns wrong answers
    when the projected coupled system is solvable but the equation is
    not (e.g. `b0 == 1`, `c == t**2 + 1` returns 0); `cancel_tan()`
    routes `n == 1` through the `n >= 2` reduction and verifies the
    residual at the bottom of the recursion.  (The 1st edition
    additionally misprints the return as `ut + v`.)
  - `param_coupled_DE_system()` in cde.py and `prde_cancel_tan()` in
    prde.py (commit `378879df4f`): the parametric analogue (the book
    gives no parametric tan pseudocode; follows the §7.1 cancellation
    pattern applied to the tangent projection, with the p-quotient
    trick keeping the recursion's generators polynomial).  Wired into
    `param_poly_rischDE()`, completing `prde_no_cancel_b_equal()`'s
    delta >= 2 hand-off (which used to raise NotImplementedError).
    Also fixed: `prde_no_cancel_b_equal()` mutated its caller's Q
    list.
  - Roborev findings fixed (commits `6ae23fef88`, `bc3492c50f`,
    `00a0d558af`, `6903974f4a` — an iterative review chain on the
    nonlinear-case dispatch, each review of a fix finding the next
    layer): the pre-TODO'd `lc(b).is_number` guard blocked valid
    nonconstant-eta hypertangent problems (e.g. `Dt == x*(t**2+1)`);
    the dispatch compared n against the *uncancelled* ratio (TypeError
    for e.g. `(2x+2)/(x+1)`); numeric noninteger, negative,
    non-real, and above-bound integer ratios were misrouted to the
    cancellation branch (NotImplementedError for solvable inputs —
    and `no_cancel_equal()` called directly with an unattainable
    cancellation degree produced a *false no-solution proof* via its
    m > n check).  Now both `solve_poly_rde()` and
    `param_poly_rischDE()` decide via `_no_cancel_equal_applies()`:
    the cancellation algorithms take over exactly when the cancelled
    ratio is a positive integer equal to n; nonconstant-element-of-k
    ratios (incl. safely parameter-mixed ones like `x + y`, whose
    tower part survives every specialization) route to
    `no_cancel_equal()`, which now ignores cancellation degrees above
    the bound; parameter-only ratios are still refused.
- **Branch housekeeping (2026-08-21):** `risch-hypertangent` had been
  branched from a pre-rebase `risch-rde-cancellation` (it carried stale
  copies of the Phase 1–4 commits and the old `risch-typing` stack);
  its 10 Phase-5 commits were rebased onto the current
  `risch-rde-cancellation` (`d7dafa43c1`) with no conflicts and all
  Risch tests green.  `github/risch-hypertangent` still has the old
  history — a `--force-with-lease` push is Aaron's call.  Typing
  (`risch-typing`, Literal aliases etc.) is no longer in this stack.
- **Phase 5a — DONE** (2026-08-21, `e9c6f7e105` + roborev follow-up
  `624213a55a` (the tan/atan adjunction tests always use the real
  theorem, so they refuse explicit `I` even over pure exp/log towers —
  e.g. `atan(x) == -I*t/2` over `QQ(I)(x, log((1+Ix)/(1-Ix)))`) on
  `risch-hypertangent`; real structure theorems, §9.3 + the 1989
  Bronstein paper — `~/Dropbox/papers/symbolic-computation/Bronstein
  - Simplification of Real Elementary Functions.pdf`):
  - `DE.exts` labels `'tan'` (`T[i] == tan(extargs[i-1])`, `Dt ==
    Db*(t**2+1)`) and `'atan'` (`T[i] == atan(extargs[i-1])`, `Dt ==
    Db/(b**2+1)`); `DifferentialExtension` does not yet *build* them
    (that is 5d), so they are only reachable through manual extensions.
  - `is_deriv_k`/`is_log_deriv_k_t_radical`/
    `parametric_log_deriv_structure` accept real towers: by Corollary
    9.3.2 (i)/(ii) the tan/atan monomials never contribute to the sums
    over E and L.  The three copied tower guards are now
    `_structure_tower()` (every monomial labeled, and — only when
    tan/atan monomials are present at or below the current level —
    explicit `I` in the tower or the input raises NotImplementedError,
    the theorem's √−1 ∉ K precondition; the level filter is what keeps
    cde.py's `k(√−1)` calls below a tan level working), and the three
    copied system solves are `_structure_solve()` (zero right hand
    side is the trivial combination, so constants decide correctly).
  - New `is_deriv_k_atan()` — equation (9.14), Corollary 9.3.2 (iii),
    paper eq. (4): is `Df/(f²+1)` a derivative in K, i.e. `atan(f) ==
    u + c`; returns `(ans, u)` and deliberately no `const` (it is
    piecewise constant, e.g. `atan(2x/(1-x²)) - 2atan(x)` jumps at
    |x|=1; 5d should use an opaque constant exactly like
    `_log_branch`).  New `is_log_deriv_k_t_radical_tan()` — (9.15),
    Corollary 9.3.2 (iv), paper eq. (3): is `√−1·Df` the log derivative
    of a K(√−1)-radical, i.e. `n*f == u + n*c`, so `tan(f)` is
    algebraic of degree ≤ n over `K(tan(c))` (rational when n == 1 via
    the addition formula — 5d needs a tan analog of `integer_powers`
    to avoid n > 1, cf. the paper's Flory claim); returns
    `(ans, u, n, const)` mirroring `is_log_deriv_k_t_radical`.  Both
    reproduce the paper's Examples 1 (`c1 = -1/3`) and 2
    (`(3/4, -1)`, `c = 2`).
  - Hypertangent case of `is_log_deriv_k_t_radical_in_field()`
    (§5.12): `p == a + b*t`, `u == v*(t²+1)**e`, `n*a == Dv/v`
    recursively in k, `e == n*b/(2η)`; non-rational ratio → None
    (same generic-soundness convention as the residue check), √−1
    present → NotImplementedError; nested tan-under-tan recursion
    tested.
  - Reconstructed equations (the 1st-edition OCR drops them): (9.12)
    and (9.13) have the same right hand sides as (9.8)/(9.9) over E ∪
    L; (9.14) `Db/(b²+1)` and (9.15) `Db` both equal `Σ_A r_i Dt_i +
    Σ_T r_i Dt_i/(t_i²+1)`.
- **Phase 5d — DONE (core)** (2026-08-21, `b248038889` + roborev
  follow-up `b0982ae9dc` (nested trig functions rewritten inside out;
  the exp-restart path reapplies `_rewrite_trig()`) on
  `risch-hypertangent`, pushed): `risch_integrate` now integrates real
  trigonometric integrands through tangent/arc-tangent towers:
  - `DifferentialExtension._tan_part()`: `t = tan(g)`, `Dt =
    Dg(t²+1)`; tan arguments are split into constant + tower-dependent
    parts, the dependent parts grouped with `integer_powers()` (the
    analog of the exp treatment), and every `tan(n·g + c)` rewritten
    through `tan(g)` by `expand_trig` (exact identities, no branch
    constants); transcendence by `is_log_deriv_k_t_radical_tan`
    (n == 1 ⇒ rewrite through existing tan/atan generators, n > 1 ⇒
    NotImplementedError "algebraic", e.g. `tan(atan(x)/2)`).
    `_atan_part()`: primitive `Dt = Darg/(arg²+1)`; `is_deriv_k_atan`
    solutions become `u + opaque Dummy` with the exact difference in
    `backsubs` (mirrors `_log_branch`; e.g. `atan(x) + atan(1/x)`
    integrates to `x·(atan(x) + atan(1/x))`).  `_rewrite_trig()`:
    sin/cos/sec/csc → tan of the half angle (`.rewrite(tan)`), cot →
    1/tan, acot(u) → atan(1/u) + opaque constant; functions of
    constants untouched; hyperbolics/asin/acos still need
    `rewrite_complex=True`.  `I` present ⇒ complex rewriting as before.
  - `integrate_hypertangent()` / `integrate_hypertangent_reduced()`
    (IntegrateHypertangent / IntegrateHypertangentReduced, §5.10; the
    reduced step solves (5.20) with `coupled_DE_system(0, 2mη, a, b)`
    one level down) + the `case == 'tan'` dispatch.  Examples
    5.10.1–5.10.3 and Exercise 5.6 f) (`atan(x + tan(x))`) reproduce;
    `rischDE` over a tan level runs end-to-end (`x·exp(tan(x))`);
    atan towers go through the primitive case (`∫atan(x)`,
    `log(atan(x))`, `atan(x)²/2`).  A 24-integrand sweep: all answers
    verified (symbolically or numerically), nonelementary proofs for
    `sin(x)/x`, `exp(x)/(1+tan(x))`, `atan(x)/x`, `exp(x)·tan(x)`,
    `log(x)·tan(x)`, `∫x·atan(x)/(1+x²)`.
  - Output form: the answers first came back as rational functions of
    `tan(x/2)` etc.; Phase 5e below rewrites them.  To keep
    `integrate()`'s behavior unchanged, `Integral._eval_integral` skips
    the automatic Risch attempts for integrands containing real
    trigonometric functions of `x` (`_real_trig()`); `risch=True` uses
    the new code.
- **Phase 5e — DONE** (2026-08-22, `916d99404e` (output form),
  `4215515f97` (floor terms for odd-degree atan arguments),
  `9ad87ed6a9` (integrate() last-resort fallback) + five roborev
  follow-ups (below) on `risch-hypertangent`, pushed (tip `66bc72d6b8`);
  full `sympy/integrals` suite green, mypy clean):
  - (i) **Real output form.** `_rewrite_trig()` records the arguments
    of the sines/cosines/secants/cosecants it rewrites in the new
    `sincos_args` slot; `DifferentialExtension.restore_sincos()` (called
    at the end of `risch_integrate()` on the result and on the
    nonelementary integrand) rewrites, for every hypertangent generator
    tan(g) not written by the user as tan(g)/cot(g) and whose double
    angle 2g is (up to a constant shift) a recorded angle, all rational
    functions of tan(g) through sin(2g), cos(2g) via
    `_half_angle_to_sincos()`: exact (same meromorphic function;
    numerator and denominator reduced mod s²+c²−1 to be linear in s or
    in c, optionally rationalized with the conjugate; of the four forms
    the fewest-ops one wins, unless the tangent form is shorter —
    `∫1/sin x = log(tan(x/2))`, `∫1/(1+cos x)² = tan³(x/2)/6 +
    tan(x/2)/2` stay).  Applies inside function arguments (`exp(sin x)`,
    `log(sin x)` restored) and to nested generators (processed bottom
    up: `sin(sin x)`).  Arc-tangents of *polynomials* in tan(g) keep
    that form (conventional, and the one `Integral.doit()`'s floor pass
    matches).  Two antiderivative-only liberties (the result changes by
    a locally constant function): additive constants are dropped
    (`−cos x − 1 → −cos x`), and top-level logs with commensurable
    constant coefficients are combined into one log whose argument
    loses constant factors/numerators when shorter (`∫sin x/(cos x+2) =
    −log(cos x + 2)`, `∫sec x = log((1+sin x)/cos x)`, `∫(sin x+tan x) =
    −log cos x − cos x`).  A ~70-integrand sweep verified exactly
    (tan(u/2) decision procedure) or numerically.  Known limits: a
    generator whose double angle is not a recorded angle stays a
    tangent (`sin x + sin(2x/3)`); shifted angles (`sin(x+1)`) give
    tan(1/2) coefficients; `log(2 − cos²x)/2` vs `log(1+sin²x)/2` is a
    tie decided by candidate order.
  - (ii) **Continuity — decision (Aaron may veto):** `risch_integrate()`
    itself adds *no* floor terms, following sympy's convention that the
    low-level routines (trigintegrate, manualintegrate, heurisch, ...)
    return the raw antiderivative and `Integral.doit()` adds the
    Jeffrey–Rich corrections in its final round; that pass was
    generalized from `atan(c·tan(a) + d)` to `atan(P(tan a))` with P of
    odd degree (jump `sign(lc)·π`, even degree ⇒ no jump), which covers
    Risch's cubic outputs (`∫1/(1+sin²x)`).  Rejected: floor terms inside
    `risch_integrate()` (double correction in `integrate()` unless
    doit's pass is suppressed), and the elementary continuous form
    `x/√3 − (2/√3)·atan(sin x/(cos x + 2 + √3))` from the θ/2-shift
    identity (needs a positivity proof of the new denominator, `4c >
    d²`; a possible later refinement).
  - (iii) **integrate():** the `_real_trig` gate stays for the early
    Risch attempts (the other methods are faster and give the
    conventional forms; every existing answer unchanged), and Risch is
    now the **last resort** for real trig integrands — after heurisch,
    meijerg, manual and the `sincos_to_sum` expansion retry (placing it
    before the retry lost the Fresnel answer of `test_issue_5547`):
    `integrate(exp(x)/(1+tan(x)))` is a `NonElementaryIntegral`,
    `Si(x)` etc. unaffected; the nonelementary residual is integrated
    with `final=False` so its floor terms are not added twice.
    `test_issue_12645` now returns an inner `NonElementaryIntegral`
    inside the outer `Integral` — the pre-existing convention for
    proven-nonelementary integrands (`test_issue_2708` pins definite
    `NonElementaryIntegral`s; master nests `∫∫exp(x)/(1+x)²` the same
    way); flattening that is a possible separate cleanup.
  - **Tests to add when rebasing on PR #30558 (2026-10-08).**  That
    PR (branch `fix-atan-floor-terms`, off master) replaces doit's
    inline floor pass with `_add_atan_floor_terms(antideriv, x)` /
    `_atan_floor_correction(atan_arg, x)`: definite integrals only,
    real `x`, the antiderivative must be a polynomial in the atan with
    x-free coefficients (jump `(P(π/2) − P(−π/2))/π` times the atan's),
    the atan argument must be *linear* in the tan/cot atoms with real
    x-free coefficients (or one atom with a constant-sign coefficient),
    the rest of the argument finite at the poles, pole lattices of
    several atoms compared, cot sign fixed, anchor `(a + π/2)/π`.  The
    5e-ii odd-degree extension `atan(P(tan a))` (jump `sign(lc)·π`)
    must be re-applied on top of `_atan_floor_correction` (its
    `total_degree() > 1 → None` line) when this branch is rebased.
    Test to add then — Woodman04's integrand from the PR review,
    `f = (cos x + tan²x + 2 tan x sec²x + 1)/((sin x + tan x + sec²x)² + 1)`
    (= `d/dx atan(sin x + tan x + sec²x)`): `risch_integrate(f, x)`
    solves it in 0.2 s (heurisch: 7.5 s) as a sum of four atans of
    polynomials in tan(x/2) of degrees 2, 5, 7, 10 — verified
    numerically (derivative, and `F(4) − F(1)` = quadrature across the
    pole x = π).  Note the result is *already continuous*: the jumps of
    the degree-5 and degree-7 atans cancel at the poles of tan(x/2), so
    the per-atan odd-degree correction (+π each ⇒ +2π spurious) would
    be wrong here.  The per-atan rule is only right when the atans do
    not share poles; the proper fix is the Jeffrey–Rich one — compute
    the jump of the *whole* antiderivative at a representative pole
    (limits from both sides) and add one floor term per pole lattice —
    which is also what the PR's polynomial-in-the-atan rule does for a
    single atan.  Until then, pin `integrate(f, (x, 1, 4))` (crosses
    x = π) against the quadrature value −0.17972457 and `(x, 1, 2)` =
    −0.048698414, plus `integrate(f, x)` having no floor term.
  - Roborev follow-ups (2026-08-22): `b8c3011500` (sincos_args survives
    the exponential restart — it was reset with the tower),
    `0ee412a433` (integrate_hyperexponential's zero-exponent Piecewise
    fallback called `integrate()` eagerly even when `Ne(qds, 0)` was
    trivially true — 147 s of manualintegrate on
    `exp(x)·atan(tan x + 2)/x`; now only built when qds may be zero),
    `aee789ea9b` (a wholly nonelementary `risch_integrate` result shows
    the user's f, not the rewritten internal form), `8856e15da9`
    (**pre-existing crash** in `solve_poly_rde`'s "k might be a field"
    branch: `no_cancel_b_small`'s reduced `Dy + b0 y = c0` is now solved
    by `rischDE` one level down (or `c0/b0` over the constants) instead of
    `as_poly`-ing b0/c0 into the lower generator, which was None for
    rational b0/c0 — reached from the tan level), `eee09faf1b`
    (`Integral.doit`'s floor round masks unevaluated Integrals so their
    integrands are not rewritten).  Reviews 848–850 assessed/closed; the
    x-dependent-leading-coefficient and shared-pole caveats of the floor
    pass are pre-existing linear-case semantics, deliberately mirrored.
    Second round (reviews 851–855, all closed): `366b9141f6` (`qds.is_zero
    is not False`), `e7e2085a62` (masking Dummies keep commutativity),
    `66bc72d6b8` (`test_issue_23704` expects the user's form).
  - Still open from 5d: real hyperbolic functions through `exp` in the
    non-complex branch (exact, no branch issue), and nested tan-under-tan
    cancellation (the `k(√−1)` in-field/structure calls at a tan level
    raise NotImplementedError honestly).

Key discoveries along the way, so nobody re-derives them:

- **Three errata in the book itself** — see `BRONSTEIN_ERRATA.md` for
  full statements and derivations: (1) `LimitedIntegrateReduce`'s first
  return component must be `hn`, not `a == hn*hs` (both editions);
  (2) the first branch of `ParametricLogarithmicDerivative` swaps N and
  M (both editions; sympy always had the corrected form); (3) the §7.1
  Liouvillian-cancellation residual equations have a wrong sign in the
  1st edition only — which is precisely the sign error that
  `prde_cancel_liouvillian()` (Gaurav Dhingra's 2017 GSoC work, not the
  2013 hypertangent effort as previously stated here) faithfully
  implemented.
- **`constant_system()` returns a reduced system, not a solution.**
  Treating its `u` as a solution vector only works when the reduction
  happens to be identity-like.  Fixed in
  `parametric_log_deriv_structure()` and then, during the audit, in
  `is_log_deriv_k_t_radical()`/`is_deriv_k()` via
  `_structure_system_solve()`.
- **Tower canonicalization shields the cancellation branches**: for
  top-level `risch_integrate` inputs, `DifferentialExtension`
  normalizes away exactly the `b == Dz/z (+ m*Dt/t)` structure the
  §6.6 cancellation branches detect (such exponentials would be
  algebraic or rewritable), so those branches are only reachable today
  through the rde/prde API and the recursions of later phases.  This
  is why several correct-by-construction features have no top-level
  reproducer.
- **End-to-end wins now pinned in tests**:
  `exp(x)*log(exp(x) + 1)` (used to hang; fixed by the
  prde_cancel_liouvillian eta fix), the whole
  `log(<exp and log mixed>)` family, e.g. `log(exp(x) + log(x))`
  (used to raise NotImplementedError; fixed by the structure-theorem
  parametric_log_deriv), including purely elementary cases such as
  the derivatives of `(x - 1)*log(exp(x) + log(x))` and
  `exp(x)*log(exp(x) + log(x))`.

## Remaining gaps for the pure exponential-logarithmic case

After Phases 0–4, the remaining exp/log-tower incompleteness is:

1. **`parametric_log_deriv` no-solution side** (§7.3): the structure
   method proves existence constructively but cannot prove
   nonexistence when `Integral(f)`'s elementary extension needs
   monomials outside the current tower (pinned counterexample:
   `f == 1/(x + 1)`, `w == 1`), so it raises.  Completing it means
   building that extension by recursive in-field integration first.
2. **Parametric `b == 0` cancellation** — RESOLVED 2026-08-07
   (`7b4e227ad6`): investigation showed nothing calls
   `solve_poly_rde()` with `parametric=True`; the parametric problem
   is dispatched entirely by Kalevi's `param_poly_rischDE()`, whose
   Liouvillian cancellation (including `b == 0`) has been handled by
   `prde_cancel_liouvillian()` since 2017 (and fixed/reviewed in
   Phase 1).  The unreachable duplicate parametric dispatch in
   `solve_poly_rde()` was removed rather than completed.
3. **Residual degree-bound fallbacks** — RESOLVED 2026-08-07
   (`53ab4e4601`, `950f7ce629`): `param_rischDE()` now propagates
   `bound_degree()`'s honest `NotImplementedError` instead of the
   unsound `n = 5` guess (which silently truncated the parametric
   solution basis — false-nonelementary-proof capable); `rischDE()`
   keeps the sound `n = oo` fallback, and `spde()` now stops with an
   honest `NotImplementedError` (after a generous pass cap, added in
   `e8ce2fa9d4` after review) instead of looping forever on
   unsolvable `n == oo` reductions with `deg(a) > 0` (demonstrated
   hang: `spde(t, 1, x, oo)` over `t = exp(x)`).  Provenance: Aaron's 2010 `rischDE` and Kalevi's
   2016 `param_rischDE` (`03787514f0`) both used the honest `n = oo`;
   Gaurav Dhingra's 2017 GSoC changed the parametric one to `n = 2`,
   then `n = 5` (`315d933f06`).  Empirically the fallbacks are
   near-unreachable post-Phases 1–4: the exp-case undecidable alpha is
   intercepted first by the identical query in `special_denom()`, the
   primitive-case structure tests now decide, and constructed
   near-misses hit `weak_normalizer()`'s root-machinery
   `NotImplementedError` first.  The guards matter for deeper towers
   and the hypertangent case.  Note the residual undecidable core is
   item 1 (needs `Integral(f)`'s extension), so bound-related honest
   errors will shrink further if item 1 is ever completed.
4. **Constant-field robustness**: the structure theorems raise on
   non-rational combination coefficients (`log(2)/log(3)`-type);
   pragmatic handling is a Phase 7 item.
5. **Quality items** (the `Piecewise`/`conds` heuristic in
   `integrate_hyperexponential()` escapes to non-Risch `integrate()`;
   output-form cosmetics in `as_poly_1t`/backsubs).  One quality item
   is done: complex-conjugate residue pairs are now rewritten as real
   arc-tangents (Rioboo's `LogToReal`, §2.8) as of 2026-08-13
   (`3d200fa696`); see the status section.
6. **Symbolic-constant division sites** (audited 2026-08-07, commit
   `81b9d588fc`): three sites in the new code divide by quantities
   that can vanish for special values of symbolic constants and can
   produce generically-valid answers with unstated conditions; the
   complete answer would be a Piecewise as in
   `risch_integrate(exp(x*y), x)`.  Each is marked with a TODO:
   `prde_no_cancel_b_equal` (u = N*lam + lc(b); demonstrated
   `H == [-t**3/(y-3) - 3*t/(y**2-4*y+3)]` for `b == -y*t`),
   `limited_integrate` (`w = W[0]/W[0][0]`), and `constant_system`
   (`D(A[i,j])` pivots).  Scope rules (per Aaron): a condition is only
   *needed* when the integrand is regular at the special value but
   the answer is not (if the vanishing degenerates the integrand
   itself, the condition is implicit in its domain), and sites whose
   only possible failure is a false nonelementary proof or an honest
   error need no Piecewise at all — the gauss_jordan_solve
   inconsistency branches in `_structure_system_solve`/
   `parametric_log_deriv_structure` (returned solutions are rational
   and verified as symbolic identities, hence valid at all parameter
   values) and `parametric_log_deriv_heu`'s `cc.is_Rational` check
   are in that class and carry explanatory comments instead.
   All three TODO sites are Poly-level; Piecewise assembly is only
   possible at the top level (the `conds` mechanism), and the
   conditions would need `solve()` and/or multiple branches — hence
   TODOs, not fixes.

None of items 1-5 silently corrupts a currently reachable input: each
either raises honestly or is unreachable from `risch_integrate()`.
For item 6, `prde_no_cancel_b_equal` is top-level unreachable
(nonlinear monomials), but whether a top-level integrand can drive a
symbolic constant into `limited_integrate`'s `W[0][0]` or
`constant_system`'s pivots without degenerating the integrand itself
has not been settled; probes so far (e.g. `2*y*x + 1` against `1/x`)
came out rational.

Dependency graph of the major gaps:

```
Phase 1: is_deriv_in_field  ──────────► cancel_primitive / cancel_exp / b==0 case
                                        (Ch. 6 complete for exp/log towers)
Phase 2: prde_no_cancel_b_equal ──────► param_poly_rischDE complete
                                        └► sharper bound_degree (primitive)
Phase 3: parametric_log_deriv (full) ─► sharper bound_degree (exp), sound
                                        special_denom decisions
Phase 5a: real structure theorems ────► tan support in is_deriv_k etc.
Phase 5b: CoupledDESystem (Ch. 8) ────► cancel_tan (Ch. 6.6)
Phase 5a + 5b + DE builders ──────────► integrate_hypertangent (Ch. 5.10)
```

---

## Phase 0 — Correctness bugs and hygiene (lowest-hanging fruit)

**DONE** (PR #30180).  As implemented, item 7 turned out to be a stale
TODO rather than a bug (the residual was always correct; verified against
the book and locked with tests), the N-formula divergence in item 5 turned
out to be intentional (the book differs between §6.2 and §7.1), and the
review process found more than was in the original list: the
`laurent_series` quotient-rule sign error (with test expectations recorded
from the buggy code), the wrong-generator `real_imag` call, and the
recognizers ignoring the normal part of the splitting factorization
(nonconstant poles/roots; found by a Codex review).

Each item is a small, independently mergeable PR with a regression test.
These fix silent wrong results or crashes, and several are prerequisites for
later phases.

1. **`rischDE` discards the weak normalizer** (`rde.py:777`). It computes
   `weak_normalizer(fa, fd, DE)` but throws away the quotient `q`: per
   Theorem 6.1.2, if `q` is the weak normalizer of `f`, one must solve
   `Dz + (f − Dq/q)z = qg` and return `y = z/q`. `param_rischDE`
   (`prde.py:662–676`) does this correctly; `rischDE` never multiplies `g` by
   `q` or divides the answer, so it is correct only when `q = 1`.

2. **Complex roots ignored in Laurent/recognition code.**
   `recognize_log_derivative` (`risch.py:1253`) and `laurent_series`
   (`risch.py:1196`) use `real_roots` on the Rothstein–Trager resultant,
   dropping complex roots — `recognize_log_derivative` can return `True`
   incorrectly (the TODO at 1251 admits this). This feeds
   `special_denom`/`prde_special_denom`, i.e. real integrals.

3. **`recognize_derivative` is broken twice** (`risch.py:1219–1225`):
   `g is not d` is an object-identity test (always true for a fresh
   `gcd(...)`), and the multiplicity from `splitfactor_sqf` is discarded in
   favor of a loop counter, which makes `laurent_series` crash with
   `ExactQuotientFailed` on e.g. `d = t²`. Currently dead code (no callers
   outside tests) — fix or remove.

4. **`bound_degree` unpacks `None`** (`rde.py:324, 348`): `limited_integrate`
   returns `None` on failure, but the call sites unpack
   `(za, zd), m = limited_integrate(...)` guarded only by
   `except NonElementaryIntegralException` — an exception it no longer
   raises. Failure here is an uncaught `TypeError` instead of falling back to
   the weak bound.

5. **`special_denom` (rde.py) has diverged from `prde_special_denom`
   (prde.py)** — the standing TODO at `prde.py:115` says to merge them, and
   they now disagree three ways: the final bound (`N = max(0, -nb, n - nc)`
   at `rde.py:256` vs `N = max(0, -nb)` at `prde.py:163`); the tan branch
   (direct `.eval(sqrt(-1))` at `rde.py:246` vs the `real_imag()` helper
   written to avoid that, `prde.py:151`); and `n = min(n, m)` vs
   `n = min(n, s/2)`. Adjudicate against Section 6.2/7.1 and keep one
   implementation.

6. **`parametric_log_deriv_heu` conflates "no solution" with "can't tell"**
   (`prde.py:861–974`). The docstring promises `NotImplementedError` when the
   heuristic fails, but every failure path returns `None` ("proven no
   solution"). Callers — `special_denom`, `bound_degree` (exp),
   `cancel_exp`, `is_log_deriv_k_t_radical_in_field` — treat `None` as a
   proof. Fix the contract now (raise on the genuinely-inconclusive paths,
   e.g. `z.degree < 1` at `prde.py:947`) so soundness holds even before the
   Phase 3 fallback exists.

7. **`integrate_primitive` mishandles the nonelementary branch**
   (`risch.py:1459`, marked TODO): when `integrate_primitive_polynomial`
   returns `b=False` it wraps the *unreduced* remainder in
   `NonElementaryIntegral` instead of subtracting the part already
   integrated.

8. **Graceful-failure hygiene** (bundle into one PR):
   - `other_linear` derivations hit `ValueError` (`rde.py:219, 381`;
     `prde.py:126`), which `rischDE`'s `except NotImplementedError` does not
     catch → uncaught crash instead of fallback. Use `NotImplementedError`.
   - The trig guard at `risch.py:246` checks `sin, cos, tan, atan, asin,
     acos` but the rewrite table covers `cot, acot, tanh, cosh, coth, sinh`
     too, so those fall through to a confusing generic error.
   - Bare `raise NonElementaryIntegralException` everywhere in rde.py
     (module TODO at `rde.py:39`) — add messages.
   - `no_cancel_equal` returns an `Expr` instead of a `Poly` in the `m == 0`
     branch (`rde.py:544–552`).
   - `n` shadowing in `cancel_primitive` (`rde.py:578`) — harmless today,
     wrong once Phase 1 lands.

---

## Phase 1 — `is_deriv_in_field()` and the RDE cancellation cases (§5.12, §6.6)

**DONE** (`96610bfc54`, plus prerequisite bugfix `b6f6a5d9b7`).  Route 1
(the `limited_integrate` wrapper) was used as planned.  Implementing it
exposed two more inherited issues in `prde_cancel_liouvillian()` (from
Gaurav Dhingra's 2017 GSoC work on the parametric Liouvillian cases,
commit `60ddd7a0d9` — not 2013 as previously stated here): the exp-case
coefficient shift computed at the wrong level (the fix for which alone
repaired the previously-hanging
`risch_integrate(exp(x)*log(exp(x) + 1), x)`), and the 1st-edition sign
misprint in the residual update — which the 2026-08-08 roborev pass
revealed to be *behaviorally inert* (mutation-verified: only the
`t^(i-1)`-coefficient of `Fi` is ever consumed, and the `b*h` term
contributes only at degree `i`), so that fix was cosmetic alignment
with the 2nd edition; see `BRONSTEIN_ERRATA.md`.  The completed cancellation
branches themselves are canonicalization-shielded from top-level inputs
(see Status), so their tests are direct, with solvable and
provably-unsolvable cases.

**The single highest-value feature item.** One missing function blocks three
already-sketched code paths (the fix-up code is literally sitting in comments
under each `raise`):

- `cancel_primitive` (`rde.py:580`) — CancelPrim, p. 209
- `cancel_exp` (`rde.py:632`) — CancelExp, p. 210
- the `b == 0` cancellation branch of `solve_poly_rde` (`rde.py:736`)

`is_deriv_in_field(f)` decides whether `f = Dv` for some `v` *in the same
field* — Section 5.12's in-field integration. Two implementation routes:

1. Thin wrapper over the existing `limited_integrate(fa, fd, [], DE)` —
   limited integration with an empty `w`-list is exactly `f = Dv` in `k(t)`.
   This is the cheap route and reuses tested machinery.
2. The §5.12 `InFieldIntegrate` approach (run the integrator, check the
   result lies in the field). More work, but also directly useful as a
   public "is this function a derivative" API.

Recommend route 1 first. Completing this closes out Chapter 6 entirely for
exp/log towers — every non-parametric RDE for the currently supported tower
types then either solves or proves nonelementary. Test with the §6.6 book
examples plus integrands currently dying with
"is_deriv_in_field() is required".

Difficulty: **low–medium** (the surrounding code exists; the book pseudocode
is complete).

---

## Phase 2 — `prde_no_cancel_b_equal` (§7.1)

**DONE** (`5a4e8585b2`).  Implemented from the §7.1 prose as planned; the
possible-cancellation-degree branch delegates through
`param_poly_rischDE()` so it will start working automatically when the
δ ≥ 2 cancellation lands in Phase 5 (until then it raises).  Not reachable
from `risch_integrate()` (needs nonlinear-monomial towers).

The parametric analogue of `no_cancel_equal` (`deg(b) = δ(t) − 1`,
`n = −lc(b)/λ(t)`), needed at `rde.py:720` and `prde.py:550`. The book covers
it in the §7.1 cancellation discussion (pp. 236–241): the algorithm produces
`f₁, …, fᵣ ∈ k[t]` and a constant matrix `B` constraining
`q = Σ dⱼfⱼ` — no named pseudocode, but the nonparametric version
(`rde.py:512`) plus the existing parametric patterns
(`prde_no_cancel_b_large/small`) give the template.

Payoff: `param_poly_rischDE` stops raising in this case →
`limited_integrate` more complete → `bound_degree`'s primitive-case sharp
bound (`rde.py:320–355`) actually fires → fewer `n = oo` degree-bound
fallbacks (which risk non-termination in `spde`, see the warning at
`rde.py:781–786`) and deep log towers integrate more often.

Difficulty: **medium** (derivation from prose, but well-scoped and testable
in isolation).

---

## Phase 3 — Full `parametric_log_deriv` via the structure theorems (§7.3)

**DONE** (`6c1e432340`, `2ab1c1cfd7`).  Solution side complete and
constructive (generators level-filtered; underdetermined systems solved
properly after fixing the `constant_system` misuse); no-solution side
still raises by design (see Remaining gaps item 1).  This unlocked the
whole `log(<exp and log mixed>)` integrand family end to end.

Replace the heuristic-only `parametric_log_deriv` (`prde.py:977–986`, with
its commented-out fallback scaffold) with the complete §7.3 algorithm. The
key ingredient — `is_log_deriv_k_t_radical` — is already implemented
(complex/exp-log towers), so this is mostly assembling the reduction and
wiring the fallback the Phase 0 contract fix prepared for.

Payoff: sound and sharp `bound_degree` in the exp case (`rde.py:361–371`),
sound `special_denom` decisions, and `cancel_exp` gets a complete
`parametric_log_deriv` to call. Until Phase 5a, this remains limited to
exp/log towers, which is fine — that is where all its callers live today.

Difficulty: **medium**.

---

## Phase 4 — Parametric cleanup: cancellation review + limited integration (§7.1, §7.2)

**DONE** (`2172cd9844`, `5635f4788d`).  `limited_integrate_reduce()` was
wired in (not deleted), after fixing a book erratum in its first return
component; its proven degree bound N replaces the unsound `n = 5`
fallback on the main pipeline.  The solving tail is shared with
`param_rischDE()` via `_prde_normalized_solve()`.  The
`prde_cancel_liouvillian` review had already happened in Phase 1; the
`constant_system` docstring now describes the actual contract.

- `prde_cancel_liouvillian` (`prde.py:459`, docstring is literally
  "Pg, 237.") — review against the book, document, add direct tests, fix the
  `UnboundLocalError` hazard when the case is neither primitive nor exp.
- `limited_integrate_reduce` (`prde.py:780–827`) is **dead code**: the §7.2
  reduction is written and tested but `limited_integrate` bypasses it
  entirely, reducing to `param_rischDE` instead. Either wire it in (it gives
  tighter reductions and is where the promised `bound_degree()` call for
  `other_linear` belongs, per the comment at `prde.py:818–820`) or delete it
  and its `NotImplementedError` at `prde.py:824`.
- `constant_system` (`prde.py:228`): docstring promises `(B, v, s)` with a
  solvability flag; implementation returns 2-tuples and every caller
  re-derives solvability by hand. Align one way or the other.

Difficulty: **low–medium**, mostly consolidation. Can proceed in parallel
with Phases 1–3.

---

## Post-Phase-4: value-coverage audit — DONE

Completed 2026-08-06 (audit commit on `risch-rde-cancellation`).
Method: instrumented the full suite + end-to-end batteries and measured
the value distributions of key parameters, then probed the untested
ranges directly, with special attention to symbolic constants in the
matrix machinery (per Aaron).

Measured distributions (pre-audit): every `constant_system()` input had
at most ONE row; only 1 of 357 calls had any symbolic constant;
`splitfactor_sqf` multiplicities never exceeded 2; `hs == 1` outside
the newest tests; `no_cancel_equal` had one hit per branch; 64/148
nonempty `constant_system` outputs were non-identity (exposing the
u-as-solution idiom).

Findings and fixes:

- **`is_deriv_k`/`is_log_deriv_k_t_radical` misread the reduced system
  as a solution** and zip-truncated it against the generator list —
  correct only by pivot-placement luck; wrong-answer capable on
  dependent-generator towers (log(x), log(x**2)).  Fixed via the shared
  `_structure_system_solve()` (explicit gauss_jordan_solve + verified
  against the original equation).  These feed tower construction, so
  the latent risk was real.
- **`constant_system`'s elimination loop deviated from the book**:
  snapshot iteration instead of 'while A is not constant', so appended
  nonconstant rows could escape (no failing input was constructed, but
  the book's loop is now implemented, with a safety cap that turns
  uncomputable-constant nontermination into an explicit error).
- **Symbolic constants otherwise pass**: rref/gauss pivoting on
  symbolic constant entries is sound (nonzero elements of QQ(y));
  end-to-end battery with parameter y all verified, including the
  Piecewise((exp(x*y)/y, Ne(y, 0)), (x, True)) case split; structure
  theorems find rational coefficients over QQ(y) towers.  The known
  limitation stands: genuinely non-rational structure coefficients
  raise NotImplementedError.
- New tests pin all previously-untested value ranges (multi-row and
  symbolic matrices, multi-pass elimination, dependent generators in
  both orderings, multiplicity 3, immediate-reduction branch of
  no_cancel_equal, symbolic limited_integrate, the Piecewise result).

Still open from the audit: multi-row `constant_system` inputs never
arise from the current callers (all build 1-row systems), so the rref
path with real pivoting is only covered by direct tests; and the
constant-field computability caveat (cancel()-recognizable zeros)
remains the documented boundary of correctness.

Prefer semantic-contract assertions (verify the defining equation) over
exact output tuples where multiple valid answers exist.

## Phase 5 — The hypertangent case (§5.10, §6.6, Ch. 8, §9.3)

**Review warning (from Aaron):** the existing hypertangent-adjacent code
(the tan branches of `special_denom`/`prde_special_denom`, `real_imag`,
`laurent_series`, `recognize_derivative`, `recognize_log_derivative`,
`integrate_hypertangent_polynomial`) comes from a 2013 GSoC effort that
was never fully integrated or exercised end-to-end.  Phase 0 already
found and fixed several bugs in it (wrong quotient-rule sign, wrong
generator in the `real_imag` call, sign of `-b/a`, missing factor 2,
recorded-from-implementation test expectations, ignored normal factors
in both recognizers).  When Phase 5 starts, review **all** remaining
pieces of that code extra carefully — not just for correctness against
the book, but for whether the architecture is what we actually want,
especially any parts that do not closely follow the book's pseudocode
(e.g. the differential-indeterminate generalization of Theorem 2.7.1 in
`laurent_series`, which is only justified for constant roots, and the
`parametric_log_deriv` approximation of the book's
`z in k(sqrt(-1))*` condition).  Do not assume anything unexercised
from that era is correct merely because its tests pass.

The largest block, and the one users notice most (`tan`, `atan`, and real
trig generally). Split into four sub-phases, each a PR or several. Relevant
papers beyond the book, already in ~/Dropbox/papers/Risch: Bronstein,
*Simplification of Real Elementary Functions* (p207-bronstein.pdf — the real
structure theorem); Davenport, *On the Parallel Risch Algorithm (III): Use of
tangents* (p3-davenport.pdf); Jeffrey, *The Evaluation of Trigonometric
Integrals Avoiding Spurious Discontinuities* (p124-jeffrey.pdf — for choosing
continuous antiderivative forms in backsubs).

**5a. Real structure theorems (§9.3 + the 1989 Bronstein paper).**
Extend `is_deriv_k` / `is_log_deriv_k_t_radical` to towers containing tan and
non-log primitives (atan) — currently `prde.py:1054–1063` and `1179–1188`
(one gap, two copy-pasted sites; factor the check out). Then implement the
tan case of `is_log_deriv_k_t_radical_in_field` (`prde.py:1340`). This also
requires deciding what `DE.exts`/`DE.extargs` look like for `'tan'`/`'atan'`
entries.

**5b. The coupled differential system (Ch. 8).**
New solver for `Dy₁ + by₁ + cy₂ = d₁, Dy₂ − cy₁ + by₂ = d₂`:
`CoupledDESystem` (reduce to a single RDE over k(√−1) when √−1 ∉ k, or two
independent RDEs when it is) plus the cancellation recursions
`CoupledDECancelPrim` (§8.1), `CoupledDECancelExp` (§8.2),
`CoupledDECancelTan` (§8.4); §8.3 (nonlinear) has no general algorithm, same
as the RDE. Probably a new module (`cde.py`) or an rde.py section.
Independent of 5a; can be developed and tested standalone against the
Chapter 8 worked examples.

**5c. Tan branches of the RDE machinery (§6.6, §7.1).**
`PolyRischDECancelTan` (p. 211) on top of 5b → fills `solve_poly_rde`'s
`rde.py:752` gap; the parametric tan cancellation for `param_poly_rischDE`
(`prde.py:558`); finish/test the tan branches of
`special_denom`/`bound_degree` (both marked "TODO: finish writing this and
write tests", `rde.py:206, 287`) using the merged implementation from
Phase 0.

**5d. Tower construction and top-level dispatch (§5.10).**
`_tan_part`/`_atan_part` builders in `DifferentialExtension` (tan: monomial
with `Dt = η(1 + t²)`, transcendence decided via 5a; atan: a primitive), a
`case == 'tan'` branch in `risch_integrate` calling a new
`integrate_hypertangent()` (Hermite + residue reduction already handle
special polynomials; the polynomial part's helper
`integrate_hypertangent_polynomial` exists at `risch.py:1590` with zero
callers), enforcement of the "√−1 ∉ k" precondition, and backsubs that
produce real, preferably continuous results (Jeffrey's paper).

**Interim quick win (can land before any of 5a–5d):** the complex-exponential
path already works — `rewrite_complex` handles all trig/hyperbolic functions
but is auto-enabled only when `I` appears in the integrand
(`risch.py:233–244`). Expose/permit `rewrite_complex=True` for real trig
integrands in `risch_integrate` with a post-pass converting the result back
to real form. Ugly intermediates, but it turns "NotImplementedError" into
answers for a large class of trig integrals with modest effort.

Difficulty: **hard** overall; 5b and 5a are the genuinely new algorithmic
work, 5c–5d are large but mechanical given 5a+5b.

---

## Phase 6 — Nonlinear-no-specials and remaining case wiring (§5.11)

`integrate_nonlinear_no_specials` (`risch.py:1609`) is implemented but
unreachable (no `other_nonlinear` dispatch in `risch_integrate`) and has a
divergent return contract (2-tuple, no residual-integral splitting — TODOs at
1628–1629) and an unchecked "Sirr is empty" precondition. Fix the contract,
verify the precondition, and dispatch it for manually specified extensions
(e.g. Lambert W-style monomials). Decide `other_linear` policy: graceful
`NotImplementedError` at minimum (Phase 0.8), real support only if a use case
appears.

Difficulty: **low–medium**; niche payoff until `DifferentialExtension` can
build such monomials automatically.

---

## Experimental track — algebraic integrands via exp-log towers

**Branch `risch-algebraic` (started 2026-08-09, stacked on
`risch-rde-cancellation`; no PR yet).**  Contains: Aaron's two PoC
commits cherry-picked (authorship preserved; the `basic=True` fix was
already in the base), repairs (the manual-extension path left
`transcendental` unset/None → every extension-dict DE silently
degraded `NonElementaryIntegral` to `Integral`; identity backsubs
pairs; a `transcendental` key is now accepted in the extension dict),
the **acceptance filter** (below), and the **`algebraic=False` gate**:
plain `integrate()` attempts risch automatically, and ungated tower
building sent the integrals suite from ~90 s to a 10-minute timeout —
so the experimental path is opt-in via
`risch_integrate(f, x, algebraic=True)`.

**Is a final verification really needed? (Aaron's question, resolved):
yes, but the reason is specific.**  The machinery computes in the
formal field Q(x, t0, ..., tn) where the generators genuinely are
transcendental, and results maintained as formal identities push
forward through the evaluation map — so "solutions are solutions" is
*almost* right, and negative conclusions are the *known* casualty.
The gap: the formal tower has **genuinely new constants** —
`D(t1**2/x) == 0` for `t1` representing `sqrt(x)` (one-line check) —
so `Const != QQ`, and the evaluation map is only defined on elements
whose denominators avoid the kernel of the relations (`t1**2 - x`).
Internal divisions by formally-nonzero constants (`t1**2/x - 1`,
which evaluates to 0) can smuggle actually-zero denominators into a
result *while keeping the formal identity intact* — the exact
0/0-answer mechanism demonstrated earlier with
`z == sin(1)**2 + cos(1)**2 - 1`.  Exposure is essentially nested
towers (`exp(sqrt(x))`, multiple radicals); a single radical on top
has kernel-free coefficient arithmetic below it.

**Acceptance filter** (`_nontrans_accept()` in risch.py, hooked into
`integrate_primitive()`/`integrate_hyperexponential()` when
`not DE.transcendental`, per Aaron: on the polynomial extension
representation, never the final Expr):
1. formal identity `f == D(elem) + D(residue part) + i`, decided by
   `cancel()` in the tower generators — pure rational arithmetic, no
   radical simplification, and it re-verifies everything rischDE
   produced under hypotheses it is not entitled to here;
2. denominators evaluate to nonzero: reduction modulo the recognized
   power relations `t**q == u**p` (triangular, monic up to a unit —
   iterated `rem()`), which are recorded from `exts`/`extargs` for
   generators `exp(Rational*log(u))`.
A formal identity between evaluable elements pushes forward
(evaluation commutes with D by construction), so 1+2 certify every
accepted answer regardless of the invalid transcendence assumptions
used to find it.  Rejects degrade to a plain `Integral`.  Known
limitations (TODOs in code): relations *among* radicals (branch
choices like `t1*t2 == 1` for `exp(±t0/2)`) are not captured, and
RootSum residue coefficients are unchecked.

**Results** (battery of 30 + failing-integrals sampling, all through
`algebraic=True`): 16/30 solved, 0 wrong answers, 0 false
nonelementary claims, no false rejections by the filter.

**RUBI-scale results (2026-08-10)** (full run logs:
https://gist.github.com/asmeurer/b4b8ceb7c364566f5e7a3d07ce133300): Francesco Bonazzi's
`Upabjojr/rubi-integration-test-suite` (66k+ cases, MIT, cloned as a
sibling of the sympy checkout — NOT checked in) is the test-case mine;
`risch_test_suite_runner.py` (in the clone, candidate upstream
contribution) drives `risch_integrate(algebraic=True)` over it.
Census of the algebraic chapters: 3,653 concrete radical cases +
~11,800 parametric (symbolic constants, concrete Rational exponents);
~2,700 symbolic-exponent cases are filtered as unattemptable by any
Risch-style method.  Full linear-binomial chapter (3,385 attempted,
5 s/case cap): **782 solved (23%), 0 false nonelementary claims, 0
errors** — the degrade+filter honesty holds at scale, and parametric
constants flow through the towers fine (single-radical families solve
at 40-50%; two-radical products 15% with honest partials; three-factor
products and P(x)*radical families all partial/timeout — both the
new-extension frontier and the profiling target).  Ask Francesco:
would he take the runner upstream (aligned with his runner CLI)?  From
`test_failing_integrals.py` territory: `x/sqrt(a - x)` (issue 4486
core), `x*sqrt(x**2 + 1)`, and `x**(3/2)*log(x)` now solve;
`sqrt(1 - x**2)`, `sqrt(x)/(1 + sqrt(x))`, `sqrt(1 + sqrt(x))`,
`sqrt(x**2 + 1/x**2)` come back partial (need new-extension
discovery); `1/sqrt(a*x**2 + b*x + c)` times out.

**Design notes for the next passes (Aaron, 2026-08-09):**
- *Representation multiplicity*: `1/sqrt(x) == sqrt(x)/x` are
  different inputs taking different code paths, and tower order
  matters; the whole approach is heuristic.  The natural architecture
  is a retry driver — try several input rewritings and tower orders,
  accept the first candidate the filter certifies (the filter is what
  makes trying-many safe).
- Keep changes to the transcendental machinery small; the real
  algebraic Risch algorithm (Vol. II/Trager) is the eventual proper
  answer.
- *Singularities*: rewriting through exp-log towers can introduce
  spurious singularities (cf. the Rich/Jeffrey continuity work); not a
  first-pass concern — this pass is a proof of concept.
- Aaron has additional example sources in mind once the PoC works;
  the failing-integrals file and the issue tracker are the first
  mines.

### Original idea and viability experiment (2026-08-07)


The idea (Aaron, branches `algebraic-risch` and `algebraic-risch-claude`,
Oct 2025): represent radicals as exp-log combinations — `sqrt(x)` as
`exp(log(x)/2)` — and let `DifferentialExtension` build the tower anyway,
bypassing the transcendence checks.  The tower is *not* transcendental, so
two classes of conclusions become invalid and must be degraded from
`NonElementaryIntegral` to plain `Integral`: nonelementary *returns* (the
branch patches five sites conditioned on `DE.transcendental`) and
nonelementary *exceptions* (`NonElementaryIntegralException` proofs also
assume transcendence).  Solutions that are found remain solutions — but
since other parts of the theory (degree bounds, splitfactor, canonical
representations) also assume transcendence, every answer in this mode
should be verified by differentiation before being returned.

**Viability experiment (2026-08-07)**: merging `algebraic-risch-claude`
onto `risch-rde-cancellation` (two trivial conflicts in `risch.py`: keep
the Phase 0 trig guard; combine the `DE.transcendental` conditional with
the Phase 4 comment in `integrate_primitive`) and running a 30-case
algebraic battery:

- Old branch as-is: 9/30 solved, 2 crashes (`UnificationFailed`), many
  silent partials.
- Merged with Phases 1–4: **16/30 solved, zero wrong answers, zero false
  nonelementary claims**, crashes gone.  Newly solved: `sqrt(x)`,
  `x**(3/2)`, `x**(5/2)`, `x**(4/3)`, `sqrt(x)*log(x)`,
  `d/dx[sqrt(x)*sqrt(x+1)]`, `sqrt(1-x) + sqrt(1+x)`.
- **The "unreachable" code paths go live, as predicted**: `∫sqrt(x)`
  runs straight through `cancel_primitive()` (the §6.6 cancellation is
  exactly the `b == Dz/z` shape that tower canonicalization shields from
  transcendental inputs); `sqrt(1-x) + sqrt(1+x)` additionally exercises
  `cancel_exp()` and `parametric_log_deriv_structure()`;
  `sqrt(x)*log(x)` uses `limited_integrate()`.  The `spde`/`bound_degree`
  guards and the `n = 5` removal likely also become load-bearing here.
- What still fails, and why: `sqrt(x)*exp(x)` hits the honest
  `parametric_log_deriv()` undecidable side — gap item 1 (needs
  `Integral(f)`'s extension) gains practical relevance in this mode.
  `sqrt(x)/(x + 1)` (needs `atan(sqrt(x))`-type logs), `exp(sqrt(x))`
  (elementary; returns partial), and the `asinh`-type integrals
  `1/sqrt(x**2 + 1)`, `1/(sqrt(x)*sqrt(x+1))` (timeouts) all need
  **new-extension discovery** — logs/atans whose arguments involve the
  radical — which is the structure-theorem frontier again.

Assessment: genuinely promising as "algebraic integration for free" for
the radical-monomial × exp-log class; the frontier is exactly the
structure-theorem work (item 1 and Phase 5's real structure theorems), so
scheduling depends on how far the approach goes without them (Aaron's
call).  Nonelementary conclusions can never be trusted in this mode —
they must always degrade to unevaluated `Integral`.

## Phase 7 — Beyond the book (long-term)

- **Integration in terms of special functions** (Ei, li, erf, dilog, …):
  Raab, *Generalization of Risch's Algorithm to Special Functions*
  (1305.1481.pdf) and Raab's thesis. The limited-integration and parametric
  machinery from Phases 1–4 is exactly what this builds on.
- **Special functions in the integrand** (nonelementary extensions in the
  structure theorems — the second `NotImplementedError` at
  `prde.py:1061/1186`, "What should really be done in this case?").
- **Constant-field robustness**: the structure theorems bail on non-rational
  combination coefficients like `log(2)/log(3)` (`prde.py:1086, 1214`);
  needs a real `Const(K)` story (related to SymPy's longstanding
  constant-recognition problem — undecidable in general, so pragmatic
  bounds/assumptions).  Concrete instance (Hebisch index 274,
  2026-08-20): `E` and `exp(1/2)` (and `exp(n/2)` in general) end up
  as independent Poly generators of the coefficient domain, so
  `hermite_reduce` misses a repeated factor and `integrate_hyperexponential`
  dies in `as_poly_1t()`; the constants of the tower need to be
  canonicalized to powers of one `exp(1/2)` (or rational powers of `E`).
- **Algebraic extensions, done properly**: out of scope (Bronstein
  Vol. II, Trager, et al.).  The cheap exp-log-tower trick is the
  experimental track above.
- **Not planned**: Chapter 10 of the second edition (Parallel Integration,
  i.e. the Risch–Norman method) — SymPy already implements a form of this
  as `heurisch()`, and improving it is not a priority for this effort.

---

## Testing strategy (all phases)

- Every Bronstein example/exercise in the touched section becomes a test
  (test_risch.py:251 already asks for the `integrate_hyperexponential` book
  examples).
- Differentiate-and-compare (`diff(result) − integrand == 0` via `cancel`)
  for every new integral computed.
- Nonelementary verdicts are proofs — test them explicitly (e.g. the
  classical `exp(x²)`, `1/log(x)`, `sin(x)/x` family stays correct through
  every phase).
- Grep-driven regression corpus: collect integrands that currently raise
  `NotImplementedError` with each distinct message; each phase should move a
  batch from "raises" to "solves or proves nonelementary".
- Cross-check against `heurisch()` on a shared corpus for wrong-answer
  detection.

## Suggested PR sequence

| # | Content | Phase |
|---|---------|-------|
| 1 | `rischDE` weak-normalizer bug + `bound_degree` None-unpack + exception hygiene | 0.1, 0.4, 0.8 |
| 2 | Complex-roots fixes (`recognize_log_derivative`, `laurent_series`, `recognize_derivative`) | 0.2, 0.3 |
| 3 | Merge `special_denom`/`prde_special_denom`; `parametric_log_deriv_heu` contract | 0.5, 0.6 |
| 4 | `is_deriv_in_field` + cancel_primitive/cancel_exp/b==0 | 1 |
| 5 | `prde_no_cancel_b_equal` | 2 |
| 6 | Structure-theorem `parametric_log_deriv` | 3 |
| 7 | Parametric cleanup (`prde_cancel_liouvillian`, `limited_integrate_reduce`) | 4 |
| 8 | `rewrite_complex` quick win for real trig | 5-interim |
| 9+ | Real structure theorems → CoupledDESystem → cancel_tan → tan towers | 5a–5d |
| … | Nonlinear wiring; special functions | 6, 7 |
