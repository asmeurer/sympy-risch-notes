# Errata for Bronstein, *Symbolic Integration I: Transcendental Functions*

Errata found while completing SymPy's implementation of the transcendental
Risch algorithm (see `RISCH_PLAN.md`).  Each was verified by deriving the
correct statement from the surrounding theory and empirically checking the
algorithm's own stated contract on examples.  As far as we can tell these
are unreported: no official errata list survives (the archived INRIA pages
for the book do not link one), and the second edition's preface does not
mention them.

Editions: 1st = Springer 1997 (ISBN 3-662-03388-8); 2nd = Springer 2005
(ISBN 3-540-21493-3).  Section numbering is identical in both.

---

## 1. §7.2, `LimitedIntegrateReduce` — wrong first return component (both editions)

Location: 1st ed. pp. 244–245; 2nd ed. p. 248 (the pseudocode's return
statement).

The pseudocode ends with

    return(a, b, a, N, a*hn*f, -a*hn*w1, ..., -a*hn*wm)

where `a = hn*hs` was assigned in the `S1irr == Sirr` branch.  The stated
contract is that for any solution `v` of `f == Dv + Sum(ci*wi)`, the
polynomial `p == v*h` (with `h` the third component) satisfies
`a'*Dp + b*p == g + Sum(ci*vi)`, where `a'` is the **first** component.
With `a' = a` this is false whenever `hs != 1`.

Correct statement: the first component must be `hn`:

    return(hn, b, a, N, a*hn*f, -a*hn*w1, ..., -a*hn*wm)

Derivation: from `v = p/a`, multiplying `f = Dv + Sum(ci*wi)` by `a**2`
gives

    a*Dp - Da*p = a**2*f - Sum(ci*a**2*wi).

Since `hs` is special, `hs | Da` exactly, so dividing through by `hs`
yields

    hn*Dp + b*p = a*hn*f - Sum(ci*a*hn*wi),

which matches the returned `b = -Dhn - hn*Dhs/hs`, `g = a*hn*f`, and
`vi = -a*hn*wi` — with the coefficient of `Dp` equal to `hn`, not `a`.
(The two agree exactly when `hs == 1`, e.g. for purely primitive towers,
which is why simple tests do not detect the error.)

Empirical check: for `t = exp(x)`, `f = Dv + 3*w1` with `v = 1/(t*x)`,
`w1 = 1`, the returned tuple fails the contract as printed and satisfies
it with `hn` in the first slot (similarly for other exp towers with
`hs != 1`).

SymPy inherited the printed version verbatim (harmlessly, as the function
was unused); fixed in commit `2172cd9844` on the `risch-rde-cancellation`
branch, with a contract-based regression test.

---

## 2. §7.3, `ParametricLogarithmicDerivative` — N and M swapped in the first branch (both editions)

Location: 1st ed. p. 249; 2nd ed. p. 253 (the `deg(q) > B` branch of the
pseudocode).

The first branch reads

    s <- solve(coefficient(p, t^i) = c*coefficient(q, t^i), B+1 <= i <= C)
    if s = {} or s not in QQ then return "no solution"
    N <- numerator(s), M <- denominator(s)
    if Q*(N*f - M*w) = Dv/v for some Q in ZZ ... then return(Q*N, Q*M, v)

while the second branch of the *same* pseudocode (the residue-equations
branch) correctly reads

    M <- numerator(s), N <- denominator(s)

In both branches `s` is the candidate for `c = m/n` (from
`n*coefficient(p) = m*coefficient(q)`), the return value is
`(n, m, v) = (Q*N, Q*M, v)`, and the verification needs `N*f - M*w`
proper — all of which require `N = denominator(s)` and
`M = numerator(s)`.  With the printed assignments of the first branch,
`N*f - M*w` has the nonvanishing polynomial part
`coefficient(q, t^i)*(m^2 - n^2)/n` at high degrees, so the subsequent
in-field check fails and valid solutions are reported as "no solution".

Correct statement: the first branch should assign
`M <- numerator(s), N <- denominator(s)`, as the second branch does.

SymPy's implementation (`parametric_log_deriv_heu()`) has always used the
corrected form (`M, N = s[c1].as_numer_denom()`) in both branches.

---

## 3. §7.1, Liouvillian cancellation — wrong sign in the residual equations (1st edition only; corrected in the 2nd)

Location: 1st ed. pp. 237–238 (the cancellation-case discussion for
`delta(t) <= 1`, `b` in `k`).  The 2nd edition (pp. 239–240) prints the
corrected signs.

Substituting `q = h + Sum(dj*fj*t^n)` into `Dq + b*q = Sum(ci*qi)`
leaves the residual equation with `-Sum(dj*(D(fj*t^n) + b*fj*t^n))` on
the right hand side, since the operator being applied is
`L[h] = Dh + b*h`.  The 1st edition prints the inner sign as a minus, in
two displayed equations:

    Sum(ci*qi) - Sum(djn*(D(fjn*t^n) - b*fjn*t^n))         [p. 237/238]

    Sum(ci*qi) - Sum(Sum(dji*(D(hji) - b*hji))) = 0        [after (7.24)]

both of which should have `+ b*(...)` inside.  The 2nd edition's
corresponding displays (e.g. the equation following (7.17), and
`Sum(ci*(qi - Dhi - b*hi)) - Sum(dj*(D(fj) + b*fj)) = 0` in the
`deg(b) = delta(t) - 1` discussion) have the correct signs.

Historical note: SymPy's implementation of this discussion
(`prde_cancel_liouvillian()`, from Gaurav Dhingra's 2017 GSoC work on
the parametric Liouvillian cases, commit `60ddd7a0d9`) contained
exactly this sign error — `Fi = -(derivation(hji, DE) - b*hji)` with a
comment citing "eq. on top of p.238", a 1st-edition page reference
(notable in 2017, when the corrected 2nd edition had been out for a
decade) — so it was a faithful implementation of the 1st edition's
typo rather than a transcription slip.  The printed sign was corrected
in commit `b6f6a5d9b7`, adjudicated against the 2nd edition.

Amusingly, the misprint turns out to be behaviorally inert in SymPy's
implementation structure (verified by mutation testing: both signs
produce identical results): the algorithm's descending degree loop
only ever consumes the `t^(i-1)`-coefficient of the appended residual
`Fi`, while the `b*h` term contributes only to the
`t^i`-coefficient.  So the 1st edition's typo, faithfully implemented,
never affected any output — and no test can distinguish the signs.

---

## 4. §8.4, `CoupledDECancelTan` — wrong sign in the system's bottom-right matrix entry (both editions)

Location: 1st ed. p. 261; 2nd ed. p. 265 (the system displayed in the
pseudocode's specification comment).

The specification states that the algorithm decides solvability of

    (Dq1)   (b0 - n*eta*t      -b2     ) (q1)   (c1)
    (Dq2) + (b2            b0 + n*eta*t) (q2) = (c2)

The bottom-right entry should be `b0 - n*eta*t`: the system is the
real/imaginary split of the Risch differential equation
`Dq + (b0 - n*eta*t + b2*sqrt(-1))*q = c1 + c2*sqrt(-1)` (the §6.6
hypertangent cancellation case with `b1 = b0 - n*eta*t`), and splitting
any equation `Dq + (B1 + B2*sqrt(-1))*q = c1 + c2*sqrt(-1)` with real
`B1` produces the matrix `((B1, -B2), (B2, B1))` with *equal* diagonal
entries, as in the chapter's own equation (8.4).  Three independent
confirmations: (a) with unequal diagonal entries the system does not
correspond to any single complex Risch differential equation, so the
§8.4 derivation preceding the pseudocode would not apply to it; (b) the
book's own worked Example 8.4.1 solves the system (8.15), whose
diagonal entries are both `-2*t` (`b0 = 0`, `n = 2`, `eta = 1`); (c)
the recursion's argument updates (`b2 + eta`, degree bound `n - 1`)
match the displayed equation for `h`, which carries
`b0 - (n-1)*eta*t` on the diagonal.

Empirical check: SymPy's `coupled_DE_cancel_tan()` (on the
`risch-hypertangent` branch), implemented with the equal-diagonal
system, reproduces Example 8.4.1 exactly (`(q1, q2) = (t - 1, 2*x)`),
and the result satisfies the equal-diagonal system by substitution.

---

## 5. §8.2, `CoupledDECancelExp` — degree condition tests `p2` instead of `q2` (both editions)

Location: 1st ed. p. 258; 2nd ed. p. 262 (the change-of-variable
branch of the pseudocode).

The branch ends with

    if q1 in k[t] and q2 in k[t] and deg(q1) <= n and deg(p2) <= n
        then return(q1, q2) else return "no solution"

The last condition should be `deg(q2) <= n`: the contract bounds the
degrees of the returned solution `(q1, q2)`, and `p2` is the
intermediate antiderivative with `q2 = (z1*p2 - z2*p1)*t^(-m)/(z1^2 -
a*z2^2)`, whose degree differs from `deg(p2)` whenever `m != 0` or the
`z`-transformation mixes the components.  (`deg(p1)` and `deg(p2)` are
the correct conditions in `CoupledDECancelPrim` (§8.1), where the
change of variable is `t`-free, so the degrees agree; the §8.2
pseudocode looks like an incomplete adaptation of that one.)

SymPy's `coupled_DE_cancel_exp()` (on the `risch-hypertangent` branch)
checks `deg(q1) <= n` and `deg(q2) <= n`.

---

## 6. §6.6, `PolyRischDECancelTan` — the `n == 1` early return is unverified and can return a wrong answer (both editions)

Location: 1st ed. p. 211; 2nd ed. p. 215 (the `if n = 1 then
return(u + vt)` line of the pseudocode; the 1st edition additionally
misprints the returned expression as `ut + v`, contradicting its own
`r = u + vt` on the following line).

For `deg(q) <= 1`, the `t**2` coefficient of
`Dq + (b0 - eta*t)*q` vanishes identically (with `q = u + v*t`, the
`t**2` contribution `v*eta` from `Dq` cancels against `-eta*v*t**2`
from the `b` term).  So if `c` has a nonzero `t**2` coefficient,
the equation has no solution of degree at most 1 — but the coupled
differential system for `(u, v)`, which only sees the remainder of
`c` mod `t**2 + 1`, can still be solvable, and the algorithm then
returns `u + v*t` without checking the residual.  Example: `b0 == 1`,
`c == t**2 + 1` (with `eta == 1`).  The remainder of `c` is `0`, the
coupled system `Du + u + v == 0`, `Dv - u + v == 0` has only the
solution `(0, 0)` (over `k(sqrt(-1))` it is `Dy + (1 - sqrt(-1))y ==
0`, whose nonzero solutions are not rational), so the algorithm
returns `q == 0`, which does not solve the equation; the correct
answer is "no solution".

For `n >= 2` there is no such gap: the recursion divides the
residual `c - Dr - (b0 - n*eta*t)*r` exactly by `t**2 + 1` and the
`n == 0` base case checks `c` is in `k`, so mismatched high-degree
parts of `c` surface there.  The fix is to route `n == 1` through
the same reduction as `n >= 2` and verify at the bottom of the
recursion (degree bound `-1`) that the residual is exactly zero,
which is what SymPy's `cancel_tan()` (on the `risch-hypertangent`
branch) does; the spurious case above is a regression test.  The
same consideration applies to `CoupledDECancelTan` (§8.4), whose
recursion descends by 1 and therefore already verifies through its
`n == 0` base case (its `q` has both a `t` and a constant
coefficient at every level, so no coefficient of the right hand side
escapes checking).
