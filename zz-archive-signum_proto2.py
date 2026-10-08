import sys
sys.path.insert(0, '/Users/aaronmeurer/Documents/Python/sympy/sympy')
from sympy import (symbols, sqrt, Pow, S, sign, factor, roots, Symbol,
    cancel, N, Integral, together, expand, re as sym_re)
from sympy.integrals.risch import risch_integrate

x = symbols('x')

def split_with_sign(f):
    reps, signs = {}, {}
    for k, p in enumerate(sorted(f.atoms(Pow), key=str)):
        if not (p.exp.is_Rational and p.exp.q == 2 and not p.exp.is_Integer):
            continue
        outside, inside = S.One, S.One
        for b, e in factor(p.base).as_powers_dict().items():
            if e.is_Integer and e % 2 == 0:
                outside *= b**(e//2)
            else:
                inside *= b**e
        if outside == 1:
            continue
        s = Symbol('s_%d' % k)
        signs[s] = outside
        reps[p] = (s*outside*sqrt(inside))**(2*p.exp)
    return f.xreplace(reps), signs

def integrate_with_signs(f, x, verbose=True):
    g, signs = split_with_sign(f)
    if not signs:
        return risch_integrate(f, x, algebraic=True)
    if verbose:
        print('   rewritten: %s' % g)
    G = risch_integrate(g, x, algebraic=True)
    if G.has(Integral):
        return None
    if verbose:
        print('   G(x,s)   : %s' % G)
    ans = G
    corrections = []
    for s, w in signs.items():
        wn, wd = cancel(w).as_numer_denom()
        rs = []
        for part in (wn, wd):          # sign flips at roots AND poles
            try:
                rs += [r for r in roots(part, x) if r.is_real is not False]
            except Exception:
                pass
        for r in rs:
            Jp, Jm = G.subs(s, 1).subs(x, r), G.subs(s, -1).subs(x, r)
            J = cancel(together((Jp - Jm)/2))
            if J != 0:
                corrections.append((J, r))
                if verbose:
                    print('   jump at x=%s: J=%s' % (r, J))
        ans = ans.subs(s, sign(w))
    for J, r in corrections:
        ans = ans - J*sign(x - r)
    return ans

def check(name, f, pts):
    print(name)
    ans = integrate_with_signs(f, x)
    print('   ANSWER   : %s' % ans)
    if ans is None:
        print('   (not solved)\n'); return
    out = []
    for p in pts:
        try:
            # sign() is locally constant: freeze it at the test point,
            # then differentiate
            frozen = ans
            for sg in ans.atoms(sign):
                frozen = frozen.subs(sg, N(sg.args[0].subs(x, S(p))) > 0 and 1 or -1)
            lhs = complex(N(frozen.diff(x).subs(x, S(p))))
            rhs = complex(N(f.subs(x, S(p))))
            ok = abs(lhs - rhs) < 1e-7*(1 + abs(rhs))
            out.append('x=%s:%s' % (p, 'ok' if ok else 'WRONG(%.4g vs %.4g)' % (lhs.real, rhs.real)))
        except Exception as e:
            out.append('x=%s:err(%s)' % (p, type(e).__name__))
    print('   deriv    : %s' % '  '.join(out))
    # continuity across breakpoints
    for J, r in []:
        pass
    print()

check('Jeffrey Ex.1  3*x**2*sqrt(1+1/x**2)', 3*x**2*sqrt(1 + 1/x**2), [-2, '-1/2', '1/2', 2])
check('perfect square  sqrt((x+1)**2*(x+2))', sqrt((x + 1)**2*(x + 2)), ['-19/10', '-3/2', '-1/2', 3])
check('our bug  sqrt(x**2+2*x+1)/x', sqrt(x**2 + 2*x + 1)/x, [-3, '-3/2', '1/2', 2])
