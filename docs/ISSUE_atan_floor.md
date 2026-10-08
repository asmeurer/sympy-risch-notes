Title: integrate(): the floor terms added to atan(tan)/atan(cot) antiderivatives are wrong in several cases

`Integral.doit()` has a final pass (added in #13808 for #13749) that makes
antiderivatives containing `atan(c*tan(a) + d)` or `atan(c*cot(a) + d)`
continuous by adding a `floor` term that cancels the jump of `atan` at the
poles of `tan(a)`/`cot(a)`:

https://github.com/sympy/sympy/blob/6e5b7af0f8/sympy/integrals/integrals.py#L634-L658

This works for the case it was written for (`c` a constant, a single `tan`),
but in several other cases that the code accepts, the floor term it adds is
wrong. In each case it *introduces* a discontinuity into the antiderivative,
and definite integrals across that point come out wrong. All of the below is
on master (6e5b7af0f8).

## 1. The `cot` correction has the wrong sign

At a pole of `cot(a)`, `atan(c*cot(a))` jumps by `+sign(c)*pi` (for `c > 0` it
goes from `-pi/2` to `pi/2`), which is the opposite direction from the `tan`
case. The code adds `+sign(c)*pi*floor(a/pi)`, which has a jump of the same
sign, so instead of canceling the jump it doubles it to `2*pi`.

```py
>>> x = symbols('x', real=True)
>>> f = diff(atan(2*cot(x)), x)
>>> f
(-2*cot(x)**2 - 2)/(4*cot(x)**2 + 1)
>>> F = integrate(f, x)
>>> F
atan(2*cot(x)) + pi*floor(x/pi)
>>> e = Rational(1, 10**6)
>>> (F.subs(x, e) - F.subs(x, -e)).evalf(5)  # atan(2*cot(x)) alone jumps by pi here
6.2832
>>> integrate(f, (x, -1, 1)).evalf()
4.95994544347923
```

The integrand is equal to `-2/(4*cos(x)**2 + sin(x)**2)`, which is negative
everywhere, and the correct value is `2*atan(2*cot(1)) - pi = -1.32323986...`.
The term should be `-sign(c)*pi*floor(a/pi)`.

## 2. The coefficient may depend on the integration variable

The check is only that the coefficient of `tan(a)` does not contain that
`tan(a)`, not that it is constant, so the pass also fires for something like
`atan(x*tan(x))` and adds `sign(x)*pi*floor(...)`:

```py
>>> f = diff(atan(x*tan(x)), x)
>>> F = integrate(f, x)
>>> F
atan(x*tan(x)) + pi*floor((x - pi/2)/pi)*sign(x)
>>> (F.subs(x, e) - F.subs(x, -e)).evalf(5)
-6.2832
>>> integrate(f, (x, -1, 1))
-2*pi
```

`atan(x*tan(x))` is continuous (and even) on `(-pi/2, pi/2)`, so the correct
value of the definite integral is 0. The `sign(x)` factor does give the right
jump direction at each pole, but `floor((x - pi/2)/pi)` is `-1` on
`(-pi/2, pi/2)`, so the added term is `-pi*sign(x)` there, which jumps by
`2*pi` at `x = 0`. More generally a spurious jump appears wherever the
coefficient changes sign.

## 3. Several `tan` atoms with a common pole are each corrected

The loop adds one floor term per `tan` atom. When two of them have a pole at
the same point, the argument of the `atan` passes through infinity once there
and the `atan` jumps by `pi` once, but it is corrected twice:

```py
>>> f = diff(atan(tan(x) + tan(3*x)), x)
>>> F = integrate(f, x)
>>> F
atan(tan(x) + tan(3*x)) + pi*floor((x - pi/2)/pi) + pi*floor((3*x - pi/2)/pi)
>>> (F.subs(x, pi/6 + e) - F.subs(x, pi/6 - e)).evalf(5)  # only tan(3*x) has a pole: fine
6.0000e-6
>>> (F.subs(x, pi/2 + e) - F.subs(x, pi/2 - e)).evalf(5)  # both have a pole
3.1416
>>> integrate(f, (x, 1, 2)).evalf()
4.14069443054328
>>> Integral(f, (x, 1, 2)).evalf()
0.999101776953486
```

(The two values differ by `pi`.)

## 4. `tan`/`cot` that do not contain the integration variable are corrected

```py
>>> integrate(atan(tan(y)), x)
x*(atan(tan(y)) + pi*floor((y - pi/2)/pi))
>>> integrate(1/(1 + (x + 2*tan(1))**2), x)
atan(x + 2*tan(1)) - 2*pi
```

The first is not an antiderivative of `atan(tan(y))` (the second is only off by
a constant).

## Possible fixes

- For 1., flip the sign of the `cot` term.
- For 2., only add the term when the sign of the coefficient is the same for
  all real values of the integration variable (e.g. `exp(x)` or `x**2 + 1`,
  which work correctly now). When it is not, leave the `atan` uncorrected:
  that form is discontinuous only at the poles, where the user can see the
  `tan`, whereas the corrected form is discontinuous at a point where the
  integrand is perfectly regular.
- For 3., require the argument to be jointly linear in the `tan`/`cot` atoms
  and add a single term for atoms that have the same poles. For arguments
  `m*x + b`, which poles two atoms have in common is a comparison of two
  lattices. If there are none (`tan(x) + tan(2*x)`, `tan(x) - cot(x)`) the
  separate terms are right. If there are some (`tan(x) + tan(3*x)`), an
  additional floor term for the common poles fixes the jump there, which is
  given by the sign of the sum of the two poles; here the result is just
  `atan(tan(x) + tan(3*x)) + pi*floor((3*x - pi/2)/pi)`. When this cannot be
  determined, leave the `atan` uncorrected.
- For 4., ignore `tan`/`cot` atoms that are free of the integration variable.
- More generally, only add the terms when evaluating a definite integral
  (they are only needed there), only for a real integration variable, and
  only when the antiderivative is linear in the `atan` (see #20898).

This pass is also the source of #20898, where the floor term is substituted
into an `atan(tan(x))` that comes from the integrand rather than from the
integration.
