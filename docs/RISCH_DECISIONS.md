# Risch Phase 5e — decisions needed from Aaron

Written 2026-08-25 (session ending 5e).  Context: RISCH_PLAN.md “Phase 5e
— DONE”; branch `risch-hypertangent`, tip `66bc72d6b8`, pushed.  Each
item stands alone; none block further work, but 1–4 gate the eventual
Phase 5 PR.

## 1. Continuity convention for `risch_integrate()` (5e-ii)

**Aaron, 2026-09-18: keep as is for now.**  Possible future direction:
move the atan rewriting inside the integrators, which requires adjusting
how the other integrators work too.

**Decision made (veto-able):** `risch_integrate()` returns the raw
antiderivative with **no floor terms** — e.g. `∫1/(2+cos x)` →
`2√3·atan(tan(x/2)/√3)/3`, discontinuous at odd multiples of π, same as
Mathematica/Maple.  This matches the sympy convention that the low-level
routines (trigintegrate, manualintegrate, heurisch) return the raw form
and `Integral.doit()`’s final round adds the Jeffrey–Rich corrections;
that pass was generalized (`4215515f97`) from `atan(c·tan a + d)` to
`atan(P(tan a))`, P of odd degree, jump `sign(lc)·π`.  So `integrate()`
results are continuous on ℝ; direct `risch_integrate()` results are not.

Alternatives if vetoed:
- floor terms inside `risch_integrate()` itself — then `integrate()`
  must be kept from double-correcting (its doit pass matches
  `atan(…tan…)` syntactically);
- the continuous *elementary* form via the θ/2-shift identity,
  `∫1/(2+cos x) = x/√3 − (2/√3)·atan(sin x/(cos x + 2 + √3))` — no floor
  at all, but only valid when the new denominator is provably nonzero
  (for `atan(c·t + d)`: `4c > d²`); not implemented, possible refinement.

## 2. How far to enable Risch in `integrate()` (5e-iii)

**Aaron, 2026-09-18: keep Risch last for now.**  Returning cleaner
answers more often is one of the next steps for this branch (see the
output-form logic in item 3); revisit the ordering after that.

**Decision made (veto-able):** the `_real_trig` gate still skips the
*early* automatic Risch attempts for real trigonometric integrands; Risch
runs as the **last resort**, after trigintegrate, heurisch, meijerg,
manual, and the `sincos_to_sum` expansion retry (`9ad87ed6a9`).  Result:
zero changes to existing `integrate()` answers; new answers and
nonelementary proofs where everything else fails
(`integrate(exp(x)/(1+tan(x)))` → `NonElementaryIntegral`).

Open question: should Risch be tried *earlier* for trig?  That would
replace many conventional answers (`∫tan x` → `log(tan²x+1)/2` instead
of `−log(cos x)`, atan forms differing from manual’s, …) and churn many
test expectations.  A cheap experiment is available on request: lift the
gate, run `test_integrals.py`, and look at the concrete expectation diff
before deciding.

## 3. Output-form liberties in the answers (5e-i)

**Aaron, 2026-09-18: accepted.**

Accept (or veto) these taste calls in `restore_sincos()` /
`_half_angle_to_sincos()` (`916d99404e`):

- **Additive constants dropped** from the antiderivative
  (`−cos x − 1` → `−cos x`).
- **Commensurable log terms combined** into a single log, with constant
  factors/numerators stripped from its argument, when shorter:
  `∫sin x/(cos x+2) = −log(cos x + 2)`,
  `∫sec x = log((1+sin x)/cos x)`,
  `∫(sin x + tan x) = −log(cos x) − cos x`.
  These change the result by a locally constant function only (derivative
  preserved everywhere; equal on the real intervals where the arguments
  are positive).
- `∫1/(1+sin x)` = `(sin x − 1)/cos x` (i.e. tan x − sec x) rather than
  the old `−2/(tan(x/2)+1)`.
- **atan arguments stay in `tan(x/2)` form** (conventional, and the form
  the doit floor pass recognizes); rational parts and log arguments go to
  sin/cos.  Fewest-ops candidate wins; the tangent form is kept when
  strictly shorter (`∫1/sin x = log(tan(x/2))`,
  `∫1/(1+cos x)² = tan³(x/2)/6 + tan(x/2)/2`).
- Known cosmetic limits: a generator whose double angle is not an angle
  the user wrote stays a tangent (`sin x + sin(2x/3)`); `sin(x+1)` gives
  `tan(1/2)` coefficients; `log(2−cos²x)/2` vs `log(1+sin²x)/2` ties are
  decided by fixed candidate order.

## 4. Changed issue-test expectations — sign off

**Aaron, 2026-09-18: accepted.**

- `test_issue_12645`: the double integral now returns an inner
  `NonElementaryIntegral` nested inside the outer `Integral` (the inner
  x-integral is proven nonelementary).  This is the pre-existing
  convention for such integrands — master nests `∫∫exp(x)/(1+x)²` the
  same way, and `test_issue_2708` pins definite `NonElementaryIntegral`s.
  Flattening multiple integrals of proven-nonelementary integrands would
  be a separate cleanup if wanted.
- `test_issue_23704`: a wholly nonelementary result now shows the
  integrand as the user wrote it (`aee789ea9b`), not the canceled
  internal form.

## 5. Floor-pass caveats from roborev 849 — fix or leave

**2026-09-18:** both flaws reproduce on master through `integrate()`,
plus a third: the `cot` correction has the wrong sign (doubles the jump;
also still present on this branch).  Issue text drafted in
[ISSUE_atan_floor.md](ISSUE_atan_floor.md) for Aaron to post.

Two flaws in `Integral.doit()`’s atan floor pass are **pre-existing
linear-case semantics** that the odd-degree extension deliberately
mirrors:
- x-dependent leading coefficient: `atan(x·tan x)` gets
  `sign(x)·π·floor(…)`, which introduces a spurious jump at `x = 0`;
- two tan atoms sharing a pole (`atan(tan x + tan 3x)`) are corrected
  twice at the shared pole.

Fixing these properly (require a constant, known-sign leading
coefficient; combine atoms sharing a pole) changes long-standing
`integrate()` behavior.  Decide whether to pursue, separately from the
Phase 5 PR.

**2026-10-08:** the fix landed on branch `fix-atan-floor-terms` /
PR #30558 (see RISCH_PLAN.md Phase 5e for the rebase notes and the
Woodman04 test integrand, which Risch solves and heurisch takes 7.5 s
on).  Open question raised by it: the odd-degree per-atan rule double
corrects when several atans share poles, as that integrand shows
(result already continuous, rule would add 2π); switch to the
whole-antiderivative jump of Jeffrey–Rich eq. (9) when rebasing.

## 6. What to work on next

Options, any order:
- (a) real hyperbolic functions through `exp` in the non-complex branch
  (exact, no branch constants; removes the `rewrite_complex=True`
  requirement for sinh/cosh/tanh/coth) — small;
- (b) nested tan-under-tan cancellation (the `k(√−1)` in-field/structure
  calls at a tan level currently raise NotImplementedError honestly;
  the special-denominator and coupled-system parts over `k(√−1)` are
  done, `1ad2ea09da`);
- (c) Phase 6: wire up `integrate_nonlinear_no_specials`, decide the
  `other_linear` policy;
- (d) prep the Phase 5 PR branch/body (Aaron opens PRs himself).

## 7. Older items awaiting a go-ahead (not 5e)

- roborev review **805** (`0b77ab2`, risch-rde-cancellation, “Survive
  extension restarts with recorded backsubs intact”) — still open from an
  earlier session; assess/close?
- the **signum implementation** for branch-correct algebraic integration
  (Jeffrey 1993 domain-of-maximum-extent; prototype verified 2026-08-13,
  see RISCH_ALGEBRAIC_PLAN.md and `runs/algebraic-run-log.md`) — awaiting go-ahead
  since 2026-08-13.
