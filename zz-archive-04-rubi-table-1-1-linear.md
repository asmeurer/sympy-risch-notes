# 1.1.1 Linear binomial products

All attempted radical cases from this part of the Rubi corpus, run through `risch_integrate(f, x, algebraic=True)` (sympy branch `risch-algebraic`).  **SOLVED-NEW** means solved here but not by sympy's non-risch `integrate()`; SOLVED-both means both solve it.  3377 cases: partial 2235 (66%), SOLVED-both 615 (18%), timeout 353 (10%), SOLVED-NEW 159 (5%), NIE 15 (0%).

| Status | Kind | SymPy expression | Math |
|---|---|---|---|
| SOLVED-both | concrete | `x**(5/2)` | $x^{\frac{5}{2}}$ |
| SOLVED-both | concrete | `x**(3/2)` | $x^{\frac{3}{2}}$ |
| SOLVED-both | concrete | `sqrt(x)` | $\sqrt{x}$ |
| SOLVED-both | concrete | `1/sqrt(x)` | $\frac{1}{\sqrt{x}}$ |
| SOLVED-both | concrete | `x**(-3/2)` | $\frac{1}{x^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x**(-5/2)` | $\frac{1}{x^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `x**(5/3)` | $x^{\frac{5}{3}}$ |
| SOLVED-both | concrete | `x**(4/3)` | $x^{\frac{4}{3}}$ |
| SOLVED-both | concrete | `x**(2/3)` | $x^{\frac{2}{3}}$ |
| SOLVED-both | concrete | `x**(1/3)` | $\sqrt[3]{x}$ |
| SOLVED-both | concrete | `x**(-1/3)` | $\frac{1}{\sqrt[3]{x}}$ |
| SOLVED-both | concrete | `x**(-2/3)` | $\frac{1}{x^{\frac{2}{3}}}$ |
| SOLVED-both | concrete | `x**(-4/3)` | $\frac{1}{x^{\frac{4}{3}}}$ |
| SOLVED-both | concrete | `x**(-5/3)` | $\frac{1}{x^{\frac{5}{3}}}$ |
| SOLVED-both | parametric | `(c + d*(a + b*x))**(5/2)` | $\left(c + d \left(a + b x\right)\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(c + d*(a + b*x))**(3/2)` | $\left(c + d \left(a + b x\right)\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `sqrt(c + d*(a + b*x))` | $\sqrt{c + d \left(a + b x\right)}$ |
| SOLVED-both | parametric | `1/sqrt(c + d*(a + b*x))` | $\frac{1}{\sqrt{c + d \left(a + b x\right)}}$ |
| SOLVED-both | parametric | `(c + d*(a + b*x))**(-3/2)` | $\frac{1}{\left(c + d \left(a + b x\right)\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(c + d*(a + b*x))**(-5/2)` | $\frac{1}{\left(c + d \left(a + b x\right)\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**3*sqrt(a + b*x)` | $x^{3} \sqrt{a + b x}$ |
| SOLVED-both | parametric | `x**2*sqrt(a + b*x)` | $x^{2} \sqrt{a + b x}$ |
| SOLVED-both | parametric | `x*sqrt(a + b*x)` | $x \sqrt{a + b x}$ |
| SOLVED-both | parametric | `sqrt(a + b*x)` | $\sqrt{a + b x}$ |
| partial | parametric | `sqrt(a + b*x)/x` | $\frac{\sqrt{a + b x}}{x}$ |
| partial | parametric | `sqrt(a + b*x)/x**2` | $\frac{\sqrt{a + b x}}{x^{2}}$ |
| partial | parametric | `sqrt(a + b*x)/x**3` | $\frac{\sqrt{a + b x}}{x^{3}}$ |
| partial | parametric | `sqrt(a + b*x)/x**4` | $\frac{\sqrt{a + b x}}{x^{4}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x)**(3/2)` | $x^{3} \left(a + b x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x)**(3/2)` | $x^{2} \left(a + b x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x*(a + b*x)**(3/2)` | $x \left(a + b x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)**(3/2)` | $\left(a + b x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)**(3/2)/x` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a + b*x)**(3/2)/x**2` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x)**(3/2)/x**3` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x)**(3/2)/x**4` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{4}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x)**(5/2)` | $x^{3} \left(a + b x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x)**(5/2)` | $x^{2} \left(a + b x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x*(a + b*x)**(5/2)` | $x \left(a + b x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)**(5/2)` | $\left(a + b x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x)**(5/2)/x` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(a + b*x)**(5/2)/x**2` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x)**(5/2)/x**3` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x)**(5/2)/x**4` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x)**(5/2)/x**5` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{5}}$ |
| SOLVED-both | parametric | `x**7*(a + b*x)**(9/2)` | $x^{7} \left(a + b x\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x**6*(a + b*x)**(9/2)` | $x^{6} \left(a + b x\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x**5*(a + b*x)**(9/2)` | $x^{5} \left(a + b x\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x**4*(a + b*x)**(9/2)` | $x^{4} \left(a + b x\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x)**(9/2)` | $x^{3} \left(a + b x\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x)**(9/2)` | $x^{2} \left(a + b x\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x*(a + b*x)**(9/2)` | $x \left(a + b x\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)**(9/2)` | $\left(a + b x\right)^{\frac{9}{2}}$ |
| partial | parametric | `(a + b*x)**(9/2)/x` | $\frac{\left(a + b x\right)^{\frac{9}{2}}}{x}$ |
| partial | parametric | `(a + b*x)**(9/2)/x**2` | $\frac{\left(a + b x\right)^{\frac{9}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x)**(9/2)/x**3` | $\frac{\left(a + b x\right)^{\frac{9}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x)**(9/2)/x**4` | $\frac{\left(a + b x\right)^{\frac{9}{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x)**(9/2)/x**5` | $\frac{\left(a + b x\right)^{\frac{9}{2}}}{x^{5}}$ |
| partial | parametric | `(a + b*x)**(9/2)/x**6` | $\frac{\left(a + b x\right)^{\frac{9}{2}}}{x^{6}}$ |
| partial | parametric | `(a + b*x)**(9/2)/x**7` | $\frac{\left(a + b x\right)^{\frac{9}{2}}}{x^{7}}$ |
| partial | parametric | `(a + b*x)**(9/2)/x**8` | $\frac{\left(a + b x\right)^{\frac{9}{2}}}{x^{8}}$ |
| partial | parametric | `sqrt(-a + b*x)/x` | $\frac{\sqrt{- a + b x}}{x}$ |
| partial | parametric | `sqrt(-a + b*x)/x**2` | $\frac{\sqrt{- a + b x}}{x^{2}}$ |
| partial | parametric | `sqrt(-a + b*x)/x**3` | $\frac{\sqrt{- a + b x}}{x^{3}}$ |
| partial | parametric | `(-a + b*x)**(3/2)/x` | $\frac{\left(- a + b x\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(-a + b*x)**(3/2)/x**2` | $\frac{\left(- a + b x\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(-a + b*x)**(3/2)/x**3` | $\frac{\left(- a + b x\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(-a + b*x)**(5/2)/x` | $\frac{\left(- a + b x\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(-a + b*x)**(5/2)/x**2` | $\frac{\left(- a + b x\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(-a + b*x)**(5/2)/x**3` | $\frac{\left(- a + b x\right)^{\frac{5}{2}}}{x^{3}}$ |
| SOLVED-both | parametric | `x**4/sqrt(a + b*x)` | $\frac{x^{4}}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `x**3/sqrt(a + b*x)` | $\frac{x^{3}}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `x**2/sqrt(a + b*x)` | $\frac{x^{2}}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `x/sqrt(a + b*x)` | $\frac{x}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `1/sqrt(a + b*x)` | $\frac{1}{\sqrt{a + b x}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x))` | $\frac{1}{x \sqrt{a + b x}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b*x))` | $\frac{1}{x^{2} \sqrt{a + b x}}$ |
| partial | parametric | `1/(x**3*sqrt(a + b*x))` | $\frac{1}{x^{3} \sqrt{a + b x}}$ |
| partial | parametric | `1/(x**4*sqrt(a + b*x))` | $\frac{1}{x^{4} \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `x**4/(a + b*x)**(3/2)` | $\frac{x^{4}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x)**(3/2)` | $\frac{x^{3}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**2/(a + b*x)**(3/2)` | $\frac{x^{2}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x/(a + b*x)**(3/2)` | $\frac{x}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**(-3/2)` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x)**(3/2))` | $\frac{1}{x \left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x)**(3/2))` | $\frac{1}{x^{2} \left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x)**(3/2))` | $\frac{1}{x^{3} \left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**4/(a + b*x)**(5/2)` | $\frac{x^{4}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x)**(5/2)` | $\frac{x^{3}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2/(a + b*x)**(5/2)` | $\frac{x^{2}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x/(a + b*x)**(5/2)` | $\frac{x}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**(-5/2)` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x)**(5/2))` | $\frac{1}{x \left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x)**(5/2))` | $\frac{1}{x^{2} \left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x)**(5/2))` | $\frac{1}{x^{3} \left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*sqrt(-a + b*x))` | $\frac{1}{x \sqrt{- a + b x}}$ |
| partial | parametric | `1/(x**2*sqrt(-a + b*x))` | $\frac{1}{x^{2} \sqrt{- a + b x}}$ |
| partial | parametric | `1/(x**3*sqrt(-a + b*x))` | $\frac{1}{x^{3} \sqrt{- a + b x}}$ |
| partial | parametric | `1/(x*(-a + b*x)**(3/2))` | $\frac{1}{x \left(- a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(-a + b*x)**(3/2))` | $\frac{1}{x^{2} \left(- a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(-a + b*x)**(3/2))` | $\frac{1}{x^{3} \left(- a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(-a + b*x)**(5/2))` | $\frac{1}{x \left(- a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**2*(-a + b*x)**(5/2))` | $\frac{1}{x^{2} \left(- a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**3*(-a + b*x)**(5/2))` | $\frac{1}{x^{3} \left(- a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x))` | $\frac{1}{x \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x)**(1/3)` | $x^{3} \sqrt[3]{a + b x}$ |
| SOLVED-both | parametric | `x**2*(a + b*x)**(1/3)` | $x^{2} \sqrt[3]{a + b x}$ |
| SOLVED-both | parametric | `x*(a + b*x)**(1/3)` | $x \sqrt[3]{a + b x}$ |
| SOLVED-both | parametric | `(a + b*x)**(1/3)` | $\sqrt[3]{a + b x}$ |
| partial | parametric | `(a + b*x)**(1/3)/x` | $\frac{\sqrt[3]{a + b x}}{x}$ |
| partial | parametric | `(a + b*x)**(1/3)/x**2` | $\frac{\sqrt[3]{a + b x}}{x^{2}}$ |
| partial | parametric | `(a + b*x)**(1/3)/x**3` | $\frac{\sqrt[3]{a + b x}}{x^{3}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x)**(2/3)` | $x^{3} \left(a + b x\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x)**(2/3)` | $x^{2} \left(a + b x\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `x*(a + b*x)**(2/3)` | $x \left(a + b x\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `(a + b*x)**(2/3)` | $\left(a + b x\right)^{\frac{2}{3}}$ |
| partial | parametric | `(a + b*x)**(2/3)/x` | $\frac{\left(a + b x\right)^{\frac{2}{3}}}{x}$ |
| partial | parametric | `(a + b*x)**(2/3)/x**2` | $\frac{\left(a + b x\right)^{\frac{2}{3}}}{x^{2}}$ |
| partial | parametric | `(a + b*x)**(2/3)/x**3` | $\frac{\left(a + b x\right)^{\frac{2}{3}}}{x^{3}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x)**(4/3)` | $x^{3} \left(a + b x\right)^{\frac{4}{3}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x)**(4/3)` | $x^{2} \left(a + b x\right)^{\frac{4}{3}}$ |
| SOLVED-both | parametric | `x*(a + b*x)**(4/3)` | $x \left(a + b x\right)^{\frac{4}{3}}$ |
| SOLVED-both | parametric | `(a + b*x)**(4/3)` | $\left(a + b x\right)^{\frac{4}{3}}$ |
| partial | parametric | `(a + b*x)**(4/3)/x` | $\frac{\left(a + b x\right)^{\frac{4}{3}}}{x}$ |
| partial | parametric | `(a + b*x)**(4/3)/x**2` | $\frac{\left(a + b x\right)^{\frac{4}{3}}}{x^{2}}$ |
| partial | parametric | `(a + b*x)**(4/3)/x**3` | $\frac{\left(a + b x\right)^{\frac{4}{3}}}{x^{3}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x)**(1/3)` | $\frac{x^{3}}{\sqrt[3]{a + b x}}$ |
| SOLVED-both | parametric | `x**2/(a + b*x)**(1/3)` | $\frac{x^{2}}{\sqrt[3]{a + b x}}$ |
| SOLVED-both | parametric | `x/(a + b*x)**(1/3)` | $\frac{x}{\sqrt[3]{a + b x}}$ |
| SOLVED-both | parametric | `(a + b*x)**(-1/3)` | $\frac{1}{\sqrt[3]{a + b x}}$ |
| partial | parametric | `1/(x*(a + b*x)**(1/3))` | $\frac{1}{x \sqrt[3]{a + b x}}$ |
| partial | parametric | `1/(x**2*(a + b*x)**(1/3))` | $\frac{1}{x^{2} \sqrt[3]{a + b x}}$ |
| partial | parametric | `1/(x**3*(a + b*x)**(1/3))` | $\frac{1}{x^{3} \sqrt[3]{a + b x}}$ |
| SOLVED-both | parametric | `x**3/(-a + b*x)**(1/3)` | $\frac{x^{3}}{\sqrt[3]{- a + b x}}$ |
| SOLVED-both | parametric | `x**2/(-a + b*x)**(1/3)` | $\frac{x^{2}}{\sqrt[3]{- a + b x}}$ |
| SOLVED-both | parametric | `x/(-a + b*x)**(1/3)` | $\frac{x}{\sqrt[3]{- a + b x}}$ |
| SOLVED-both | parametric | `(-a + b*x)**(-1/3)` | $\frac{1}{\sqrt[3]{- a + b x}}$ |
| partial | parametric | `1/(x*(-a + b*x)**(1/3))` | $\frac{1}{x \sqrt[3]{- a + b x}}$ |
| partial | parametric | `1/(x**2*(-a + b*x)**(1/3))` | $\frac{1}{x^{2} \sqrt[3]{- a + b x}}$ |
| partial | parametric | `1/(x**3*(-a + b*x)**(1/3))` | $\frac{1}{x^{3} \sqrt[3]{- a + b x}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x)**(2/3)` | $\frac{x^{3}}{\left(a + b x\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `x**2/(a + b*x)**(2/3)` | $\frac{x^{2}}{\left(a + b x\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `x/(a + b*x)**(2/3)` | $\frac{x}{\left(a + b x\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `(a + b*x)**(-2/3)` | $\frac{1}{\left(a + b x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x*(a + b*x)**(2/3))` | $\frac{1}{x \left(a + b x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x**2*(a + b*x)**(2/3))` | $\frac{1}{x^{2} \left(a + b x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x**3*(a + b*x)**(2/3))` | $\frac{1}{x^{3} \left(a + b x\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x)**(4/3)` | $\frac{x^{3}}{\left(a + b x\right)^{\frac{4}{3}}}$ |
| SOLVED-both | parametric | `x**2/(a + b*x)**(4/3)` | $\frac{x^{2}}{\left(a + b x\right)^{\frac{4}{3}}}$ |
| SOLVED-both | parametric | `x/(a + b*x)**(4/3)` | $\frac{x}{\left(a + b x\right)^{\frac{4}{3}}}$ |
| SOLVED-both | parametric | `(a + b*x)**(-4/3)` | $\frac{1}{\left(a + b x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/(x*(a + b*x)**(4/3))` | $\frac{1}{x \left(a + b x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/(x**2*(a + b*x)**(4/3))` | $\frac{1}{x^{2} \left(a + b x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/(x**3*(a + b*x)**(4/3))` | $\frac{1}{x^{3} \left(a + b x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/(x*(a**3 + b**3*x)**(1/3))` | $\frac{1}{x \sqrt[3]{a^{3} + b^{3} x}}$ |
| partial | parametric | `1/(x*(a**3 - b**3*x)**(1/3))` | $\frac{1}{x \sqrt[3]{a^{3} - b^{3} x}}$ |
| partial | parametric | `1/(x*(-a**3 + b**3*x)**(1/3))` | $\frac{1}{x \sqrt[3]{- a^{3} + b^{3} x}}$ |
| partial | parametric | `1/(x*(-a**3 - b**3*x)**(1/3))` | $\frac{1}{x \sqrt[3]{- a^{3} - b^{3} x}}$ |
| partial | parametric | `1/(x*(a**3 + b**3*x)**(2/3))` | $\frac{1}{x \left(a^{3} + b^{3} x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x*(a**3 - b**3*x)**(2/3))` | $\frac{1}{x \left(a^{3} - b^{3} x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x*(-a**3 + b**3*x)**(2/3))` | $\frac{1}{x \left(- a^{3} + b^{3} x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x*(-a**3 - b**3*x)**(2/3))` | $\frac{1}{x \left(- a^{3} - b^{3} x\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b*x)` | $x^{\frac{5}{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b*x)` | $x^{\frac{3}{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b*x)` | $\sqrt{x} \left(a + b x\right)$ |
| SOLVED-both | parametric | `(a + b*x)/sqrt(x)` | $\frac{a + b x}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b*x)/x**(3/2)` | $\frac{a + b x}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/x**(5/2)` | $\frac{a + b x}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b*x)**2` | $x^{\frac{5}{2}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b*x)**2` | $x^{\frac{3}{2}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b*x)**2` | $\sqrt{x} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x)**2/sqrt(x)` | $\frac{\left(a + b x\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/x**(3/2)` | $\frac{\left(a + b x\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/x**(5/2)` | $\frac{\left(a + b x\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b*x)**3` | $x^{\frac{5}{2}} \left(a + b x\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b*x)**3` | $x^{\frac{3}{2}} \left(a + b x\right)^{3}$ |
| **SOLVED-NEW** | parametric | `sqrt(x)*(a + b*x)**3` | $\sqrt{x} \left(a + b x\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x)**3/sqrt(x)` | $\frac{\left(a + b x\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b*x)**3/x**(3/2)` | $\frac{\left(a + b x\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**3/x**(5/2)` | $\frac{\left(a + b x\right)^{3}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)/(a + b*x)` | $\frac{x^{\frac{5}{2}}}{a + b x}$ |
| partial | parametric | `x**(3/2)/(a + b*x)` | $\frac{x^{\frac{3}{2}}}{a + b x}$ |
| partial | parametric | `sqrt(x)/(a + b*x)` | $\frac{\sqrt{x}}{a + b x}$ |
| partial | parametric | `1/(sqrt(x)*(a + b*x))` | $\frac{1}{\sqrt{x} \left(a + b x\right)}$ |
| partial | parametric | `1/(x**(3/2)*(a + b*x))` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x\right)}$ |
| partial | parametric | `1/(x**(5/2)*(a + b*x))` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x\right)}$ |
| partial | parametric | `1/(x**(7/2)*(a + b*x))` | $\frac{1}{x^{\frac{7}{2}} \left(a + b x\right)}$ |
| partial | parametric | `x**(5/2)/(a + b*x)**2` | $\frac{x^{\frac{5}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `x**(3/2)/(a + b*x)**2` | $\frac{x^{\frac{3}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `sqrt(x)/(a + b*x)**2` | $\frac{\sqrt{x}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `1/(sqrt(x)*(a + b*x)**2)` | $\frac{1}{\sqrt{x} \left(a + b x\right)^{2}}$ |
| partial | parametric | `1/(x**(3/2)*(a + b*x)**2)` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `1/(x**(5/2)*(a + b*x)**2)` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x**(7/2)/(a + b*x)**3` | $\frac{x^{\frac{7}{2}}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `x**(5/2)/(a + b*x)**3` | $\frac{x^{\frac{5}{2}}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `x**(3/2)/(a + b*x)**3` | $\frac{x^{\frac{3}{2}}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `sqrt(x)/(a + b*x)**3` | $\frac{\sqrt{x}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `1/(sqrt(x)*(a + b*x)**3)` | $\frac{1}{\sqrt{x} \left(a + b x\right)^{3}}$ |
| partial | parametric | `1/(x**(3/2)*(a + b*x)**3)` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x\right)^{3}}$ |
| partial | parametric | `1/(x**(5/2)*(a + b*x)**3)` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x\right)^{3}}$ |
| partial | parametric | `x**(5/2)/(-a + b*x)` | $\frac{x^{\frac{5}{2}}}{- a + b x}$ |
| partial | parametric | `x**(3/2)/(-a + b*x)` | $\frac{x^{\frac{3}{2}}}{- a + b x}$ |
| partial | parametric | `sqrt(x)/(-a + b*x)` | $\frac{\sqrt{x}}{- a + b x}$ |
| partial | parametric | `1/(sqrt(x)*(-a + b*x))` | $\frac{1}{\sqrt{x} \left(- a + b x\right)}$ |
| partial | parametric | `1/(x**(3/2)*(-a + b*x))` | $\frac{1}{x^{\frac{3}{2}} \left(- a + b x\right)}$ |
| partial | parametric | `1/(x**(5/2)*(-a + b*x))` | $\frac{1}{x^{\frac{5}{2}} \left(- a + b x\right)}$ |
| partial | parametric | `1/(x**(7/2)*(-a + b*x))` | $\frac{1}{x^{\frac{7}{2}} \left(- a + b x\right)}$ |
| partial | parametric | `x**(5/2)/(-a + b*x)**2` | $\frac{x^{\frac{5}{2}}}{\left(- a + b x\right)^{2}}$ |
| partial | parametric | `x**(3/2)/(-a + b*x)**2` | $\frac{x^{\frac{3}{2}}}{\left(- a + b x\right)^{2}}$ |
| partial | parametric | `sqrt(x)/(-a + b*x)**2` | $\frac{\sqrt{x}}{\left(- a + b x\right)^{2}}$ |
| partial | parametric | `1/(sqrt(x)*(-a + b*x)**2)` | $\frac{1}{\sqrt{x} \left(- a + b x\right)^{2}}$ |
| partial | parametric | `1/(x**(3/2)*(-a + b*x)**2)` | $\frac{1}{x^{\frac{3}{2}} \left(- a + b x\right)^{2}}$ |
| partial | parametric | `1/(x**(5/2)*(-a + b*x)**2)` | $\frac{1}{x^{\frac{5}{2}} \left(- a + b x\right)^{2}}$ |
| partial | parametric | `x**(7/2)/(-a + b*x)**3` | $\frac{x^{\frac{7}{2}}}{\left(- a + b x\right)^{3}}$ |
| partial | parametric | `x**(5/2)/(-a + b*x)**3` | $\frac{x^{\frac{5}{2}}}{\left(- a + b x\right)^{3}}$ |
| partial | parametric | `x**(3/2)/(-a + b*x)**3` | $\frac{x^{\frac{3}{2}}}{\left(- a + b x\right)^{3}}$ |
| partial | parametric | `sqrt(x)/(-a + b*x)**3` | $\frac{\sqrt{x}}{\left(- a + b x\right)^{3}}$ |
| partial | parametric | `1/(sqrt(x)*(-a + b*x)**3)` | $\frac{1}{\sqrt{x} \left(- a + b x\right)^{3}}$ |
| partial | parametric | `1/(x**(3/2)*(-a + b*x)**3)` | $\frac{1}{x^{\frac{3}{2}} \left(- a + b x\right)^{3}}$ |
| partial | parametric | `1/(x**(5/2)*(-a + b*x)**3)` | $\frac{1}{x^{\frac{5}{2}} \left(- a + b x\right)^{3}}$ |
| partial | parametric | `x**(5/2)*sqrt(a + b*x)` | $x^{\frac{5}{2}} \sqrt{a + b x}$ |
| partial | parametric | `x**(3/2)*sqrt(a + b*x)` | $x^{\frac{3}{2}} \sqrt{a + b x}$ |
| partial | parametric | `sqrt(x)*sqrt(a + b*x)` | $\sqrt{x} \sqrt{a + b x}$ |
| partial | parametric | `sqrt(a + b*x)/sqrt(x)` | $\frac{\sqrt{a + b x}}{\sqrt{x}}$ |
| partial | parametric | `sqrt(a + b*x)/x**(3/2)` | $\frac{\sqrt{a + b x}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `sqrt(a + b*x)/x**(5/2)` | $\frac{\sqrt{a + b x}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `sqrt(a + b*x)/x**(7/2)` | $\frac{\sqrt{a + b x}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `sqrt(a + b*x)/x**(9/2)` | $\frac{\sqrt{a + b x}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `x**(5/2)*sqrt(a - b*x)` | $x^{\frac{5}{2}} \sqrt{a - b x}$ |
| partial | parametric | `x**(3/2)*sqrt(a - b*x)` | $x^{\frac{3}{2}} \sqrt{a - b x}$ |
| partial | parametric | `sqrt(x)*sqrt(a - b*x)` | $\sqrt{x} \sqrt{a - b x}$ |
| partial | parametric | `sqrt(a - b*x)/sqrt(x)` | $\frac{\sqrt{a - b x}}{\sqrt{x}}$ |
| partial | parametric | `sqrt(a - b*x)/x**(3/2)` | $\frac{\sqrt{a - b x}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `sqrt(a - b*x)/x**(5/2)` | $\frac{\sqrt{a - b x}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `sqrt(a - b*x)/x**(7/2)` | $\frac{\sqrt{a - b x}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `sqrt(a - b*x)/x**(9/2)` | $\frac{\sqrt{a - b x}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `x**(5/2)*sqrt(b*x + 2)` | $x^{\frac{5}{2}} \sqrt{b x + 2}$ |
| partial | parametric | `x**(3/2)*sqrt(b*x + 2)` | $x^{\frac{3}{2}} \sqrt{b x + 2}$ |
| partial | parametric | `sqrt(x)*sqrt(b*x + 2)` | $\sqrt{x} \sqrt{b x + 2}$ |
| partial | parametric | `sqrt(b*x + 2)/sqrt(x)` | $\frac{\sqrt{b x + 2}}{\sqrt{x}}$ |
| partial | parametric | `sqrt(b*x + 2)/x**(3/2)` | $\frac{\sqrt{b x + 2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `sqrt(b*x + 2)/x**(5/2)` | $\frac{\sqrt{b x + 2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `sqrt(b*x + 2)/x**(7/2)` | $\frac{\sqrt{b x + 2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `sqrt(b*x + 2)/x**(9/2)` | $\frac{\sqrt{b x + 2}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `x**(5/2)*sqrt(-b*x + 2)` | $x^{\frac{5}{2}} \sqrt{- b x + 2}$ |
| partial | parametric | `x**(3/2)*sqrt(-b*x + 2)` | $x^{\frac{3}{2}} \sqrt{- b x + 2}$ |
| partial | parametric | `sqrt(x)*sqrt(-b*x + 2)` | $\sqrt{x} \sqrt{- b x + 2}$ |
| partial | parametric | `sqrt(-b*x + 2)/sqrt(x)` | $\frac{\sqrt{- b x + 2}}{\sqrt{x}}$ |
| partial | parametric | `sqrt(-b*x + 2)/x**(3/2)` | $\frac{\sqrt{- b x + 2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `sqrt(-b*x + 2)/x**(5/2)` | $\frac{\sqrt{- b x + 2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `sqrt(-b*x + 2)/x**(7/2)` | $\frac{\sqrt{- b x + 2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `sqrt(-b*x + 2)/x**(9/2)` | $\frac{\sqrt{- b x + 2}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `x**(5/2)*(a + b*x)**(3/2)` | $x^{\frac{5}{2}} \left(a + b x\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(3/2)*(a + b*x)**(3/2)` | $x^{\frac{3}{2}} \left(a + b x\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(x)*(a + b*x)**(3/2)` | $\sqrt{x} \left(a + b x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)**(3/2)/sqrt(x)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(a + b*x)**(3/2)/x**(3/2)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)**(3/2)/x**(5/2)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)*(a - b*x)**(3/2)` | $x^{\frac{5}{2}} \left(a - b x\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(3/2)*(a - b*x)**(3/2)` | $x^{\frac{3}{2}} \left(a - b x\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(x)*(a - b*x)**(3/2)` | $\sqrt{x} \left(a - b x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a - b*x)**(3/2)/sqrt(x)` | $\frac{\left(a - b x\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(a - b*x)**(3/2)/x**(3/2)` | $\frac{\left(a - b x\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(a - b*x)**(3/2)/x**(5/2)` | $\frac{\left(a - b x\right)^{\frac{3}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)*(b*x + 2)**(3/2)` | $x^{\frac{5}{2}} \left(b x + 2\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(3/2)*(b*x + 2)**(3/2)` | $x^{\frac{3}{2}} \left(b x + 2\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(x)*(b*x + 2)**(3/2)` | $\sqrt{x} \left(b x + 2\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*x + 2)**(3/2)/sqrt(x)` | $\frac{\left(b x + 2\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(b*x + 2)**(3/2)/x**(3/2)` | $\frac{\left(b x + 2\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(b*x + 2)**(3/2)/x**(5/2)` | $\frac{\left(b x + 2\right)^{\frac{3}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)*(-b*x + 2)**(3/2)` | $x^{\frac{5}{2}} \left(- b x + 2\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(3/2)*(-b*x + 2)**(3/2)` | $x^{\frac{3}{2}} \left(- b x + 2\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(x)*(-b*x + 2)**(3/2)` | $\sqrt{x} \left(- b x + 2\right)^{\frac{3}{2}}$ |
| partial | parametric | `(-b*x + 2)**(3/2)/sqrt(x)` | $\frac{\left(- b x + 2\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(-b*x + 2)**(3/2)/x**(3/2)` | $\frac{\left(- b x + 2\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(-b*x + 2)**(3/2)/x**(5/2)` | $\frac{\left(- b x + 2\right)^{\frac{3}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)*(a + b*x)**(5/2)` | $x^{\frac{5}{2}} \left(a + b x\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**(3/2)*(a + b*x)**(5/2)` | $x^{\frac{3}{2}} \left(a + b x\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(x)*(a + b*x)**(5/2)` | $\sqrt{x} \left(a + b x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x)**(5/2)/sqrt(x)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(a + b*x)**(5/2)/x**(3/2)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)**(5/2)/x**(5/2)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)*(a - b*x)**(5/2)` | $x^{\frac{5}{2}} \left(a - b x\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**(3/2)*(a - b*x)**(5/2)` | $x^{\frac{3}{2}} \left(a - b x\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(x)*(a - b*x)**(5/2)` | $\sqrt{x} \left(a - b x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a - b*x)**(5/2)/sqrt(x)` | $\frac{\left(a - b x\right)^{\frac{5}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(a - b*x)**(5/2)/x**(3/2)` | $\frac{\left(a - b x\right)^{\frac{5}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(a - b*x)**(5/2)/x**(5/2)` | $\frac{\left(a - b x\right)^{\frac{5}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)*(b*x + 2)**(5/2)` | $x^{\frac{5}{2}} \left(b x + 2\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**(3/2)*(b*x + 2)**(5/2)` | $x^{\frac{3}{2}} \left(b x + 2\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(x)*(b*x + 2)**(5/2)` | $\sqrt{x} \left(b x + 2\right)^{\frac{5}{2}}$ |
| partial | parametric | `(b*x + 2)**(5/2)/sqrt(x)` | $\frac{\left(b x + 2\right)^{\frac{5}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(b*x + 2)**(5/2)/x**(3/2)` | $\frac{\left(b x + 2\right)^{\frac{5}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(b*x + 2)**(5/2)/x**(5/2)` | $\frac{\left(b x + 2\right)^{\frac{5}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)*(-b*x + 2)**(5/2)` | $x^{\frac{5}{2}} \left(- b x + 2\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**(3/2)*(-b*x + 2)**(5/2)` | $x^{\frac{3}{2}} \left(- b x + 2\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(x)*(-b*x + 2)**(5/2)` | $\sqrt{x} \left(- b x + 2\right)^{\frac{5}{2}}$ |
| partial | parametric | `(-b*x + 2)**(5/2)/sqrt(x)` | $\frac{\left(- b x + 2\right)^{\frac{5}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(-b*x + 2)**(5/2)/x**(3/2)` | $\frac{\left(- b x + 2\right)^{\frac{5}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(-b*x + 2)**(5/2)/x**(5/2)` | $\frac{\left(- b x + 2\right)^{\frac{5}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)/sqrt(a + b*x)` | $\frac{x^{\frac{5}{2}}}{\sqrt{a + b x}}$ |
| partial | parametric | `x**(3/2)/sqrt(a + b*x)` | $\frac{x^{\frac{3}{2}}}{\sqrt{a + b x}}$ |
| partial | parametric | `sqrt(x)/sqrt(a + b*x)` | $\frac{\sqrt{x}}{\sqrt{a + b x}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(a + b*x))` | $\frac{1}{\sqrt{x} \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*sqrt(a + b*x))` | $\frac{1}{x^{\frac{3}{2}} \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*sqrt(a + b*x))` | $\frac{1}{x^{\frac{5}{2}} \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `1/(x**(7/2)*sqrt(a + b*x))` | $\frac{1}{x^{\frac{7}{2}} \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `1/(x**(9/2)*sqrt(a + b*x))` | $\frac{1}{x^{\frac{9}{2}} \sqrt{a + b x}}$ |
| partial | parametric | `x**(5/2)/(a + b*x)**(3/2)` | $\frac{x^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(3/2)/(a + b*x)**(3/2)` | $\frac{x^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)/(a + b*x)**(3/2)` | $\frac{\sqrt{x}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(sqrt(x)*(a + b*x)**(3/2))` | $\frac{1}{\sqrt{x} \left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*(a + b*x)**(3/2))` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*(a + b*x)**(3/2))` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(7/2)*(a + b*x)**(3/2))` | $\frac{1}{x^{\frac{7}{2}} \left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(5/2)/(a + b*x)**(5/2)` | $\frac{x^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(3/2)/(a + b*x)**(5/2)` | $\frac{x^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `sqrt(x)/(a + b*x)**(5/2)` | $\frac{\sqrt{x}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(sqrt(x)*(a + b*x)**(5/2))` | $\frac{1}{\sqrt{x} \left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*(a + b*x)**(5/2))` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*(a + b*x)**(5/2))` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)/sqrt(a - b*x)` | $\frac{x^{\frac{5}{2}}}{\sqrt{a - b x}}$ |
| partial | parametric | `x**(3/2)/sqrt(a - b*x)` | $\frac{x^{\frac{3}{2}}}{\sqrt{a - b x}}$ |
| partial | parametric | `sqrt(x)/sqrt(a - b*x)` | $\frac{\sqrt{x}}{\sqrt{a - b x}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(a - b*x))` | $\frac{1}{\sqrt{x} \sqrt{a - b x}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*sqrt(a - b*x))` | $\frac{1}{x^{\frac{3}{2}} \sqrt{a - b x}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*sqrt(a - b*x))` | $\frac{1}{x^{\frac{5}{2}} \sqrt{a - b x}}$ |
| partial | parametric | `x**(5/2)/(a - b*x)**(3/2)` | $\frac{x^{\frac{5}{2}}}{\left(a - b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(3/2)/(a - b*x)**(3/2)` | $\frac{x^{\frac{3}{2}}}{\left(a - b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)/(a - b*x)**(3/2)` | $\frac{\sqrt{x}}{\left(a - b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(sqrt(x)*(a - b*x)**(3/2))` | $\frac{1}{\sqrt{x} \left(a - b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*(a - b*x)**(3/2))` | $\frac{1}{x^{\frac{3}{2}} \left(a - b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*(a - b*x)**(3/2))` | $\frac{1}{x^{\frac{5}{2}} \left(a - b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(5/2)/(a - b*x)**(5/2)` | $\frac{x^{\frac{5}{2}}}{\left(a - b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(3/2)/(a - b*x)**(5/2)` | $\frac{x^{\frac{3}{2}}}{\left(a - b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `sqrt(x)/(a - b*x)**(5/2)` | $\frac{\sqrt{x}}{\left(a - b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(sqrt(x)*(a - b*x)**(5/2))` | $\frac{1}{\sqrt{x} \left(a - b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*(a - b*x)**(5/2))` | $\frac{1}{x^{\frac{3}{2}} \left(a - b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*(a - b*x)**(5/2))` | $\frac{1}{x^{\frac{5}{2}} \left(a - b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)/sqrt(b*x + 2)` | $\frac{x^{\frac{5}{2}}}{\sqrt{b x + 2}}$ |
| partial | parametric | `x**(3/2)/sqrt(b*x + 2)` | $\frac{x^{\frac{3}{2}}}{\sqrt{b x + 2}}$ |
| partial | parametric | `sqrt(x)/sqrt(b*x + 2)` | $\frac{\sqrt{x}}{\sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{x} \sqrt{b x + 2}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*sqrt(b*x + 2))` | $\frac{1}{x^{\frac{3}{2}} \sqrt{b x + 2}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*sqrt(b*x + 2))` | $\frac{1}{x^{\frac{5}{2}} \sqrt{b x + 2}}$ |
| SOLVED-both | parametric | `1/(x**(7/2)*sqrt(b*x + 2))` | $\frac{1}{x^{\frac{7}{2}} \sqrt{b x + 2}}$ |
| SOLVED-both | parametric | `1/(x**(9/2)*sqrt(b*x + 2))` | $\frac{1}{x^{\frac{9}{2}} \sqrt{b x + 2}}$ |
| partial | parametric | `x**(5/2)/(b*x + 2)**(3/2)` | $\frac{x^{\frac{5}{2}}}{\left(b x + 2\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(3/2)/(b*x + 2)**(3/2)` | $\frac{x^{\frac{3}{2}}}{\left(b x + 2\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)/(b*x + 2)**(3/2)` | $\frac{\sqrt{x}}{\left(b x + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(sqrt(x)*(b*x + 2)**(3/2))` | $\frac{1}{\sqrt{x} \left(b x + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*(b*x + 2)**(3/2))` | $\frac{1}{x^{\frac{3}{2}} \left(b x + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*(b*x + 2)**(3/2))` | $\frac{1}{x^{\frac{5}{2}} \left(b x + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(7/2)*(b*x + 2)**(3/2))` | $\frac{1}{x^{\frac{7}{2}} \left(b x + 2\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(5/2)/(b*x + 2)**(5/2)` | $\frac{x^{\frac{5}{2}}}{\left(b x + 2\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(3/2)/(b*x + 2)**(5/2)` | $\frac{x^{\frac{3}{2}}}{\left(b x + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `sqrt(x)/(b*x + 2)**(5/2)` | $\frac{\sqrt{x}}{\left(b x + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(sqrt(x)*(b*x + 2)**(5/2))` | $\frac{1}{\sqrt{x} \left(b x + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*(b*x + 2)**(5/2))` | $\frac{1}{x^{\frac{3}{2}} \left(b x + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*(b*x + 2)**(5/2))` | $\frac{1}{x^{\frac{5}{2}} \left(b x + 2\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)/sqrt(-b*x + 2)` | $\frac{x^{\frac{5}{2}}}{\sqrt{- b x + 2}}$ |
| partial | parametric | `x**(3/2)/sqrt(-b*x + 2)` | $\frac{x^{\frac{3}{2}}}{\sqrt{- b x + 2}}$ |
| partial | parametric | `sqrt(x)/sqrt(-b*x + 2)` | $\frac{\sqrt{x}}{\sqrt{- b x + 2}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(-b*x + 2))` | $\frac{1}{\sqrt{x} \sqrt{- b x + 2}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*sqrt(-b*x + 2))` | $\frac{1}{x^{\frac{3}{2}} \sqrt{- b x + 2}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*sqrt(-b*x + 2))` | $\frac{1}{x^{\frac{5}{2}} \sqrt{- b x + 2}}$ |
| partial | parametric | `x**(5/2)/(-b*x + 2)**(3/2)` | $\frac{x^{\frac{5}{2}}}{\left(- b x + 2\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(3/2)/(-b*x + 2)**(3/2)` | $\frac{x^{\frac{3}{2}}}{\left(- b x + 2\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)/(-b*x + 2)**(3/2)` | $\frac{\sqrt{x}}{\left(- b x + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(sqrt(x)*(-b*x + 2)**(3/2))` | $\frac{1}{\sqrt{x} \left(- b x + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*(-b*x + 2)**(3/2))` | $\frac{1}{x^{\frac{3}{2}} \left(- b x + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*(-b*x + 2)**(3/2))` | $\frac{1}{x^{\frac{5}{2}} \left(- b x + 2\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(5/2)/(-b*x + 2)**(5/2)` | $\frac{x^{\frac{5}{2}}}{\left(- b x + 2\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(3/2)/(-b*x + 2)**(5/2)` | $\frac{x^{\frac{3}{2}}}{\left(- b x + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `sqrt(x)/(-b*x + 2)**(5/2)` | $\frac{\sqrt{x}}{\left(- b x + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(sqrt(x)*(-b*x + 2)**(5/2))` | $\frac{1}{\sqrt{x} \left(- b x + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*(-b*x + 2)**(5/2))` | $\frac{1}{x^{\frac{3}{2}} \left(- b x + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*(-b*x + 2)**(5/2))` | $\frac{1}{x^{\frac{5}{2}} \left(- b x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(x)/sqrt(1 - x)` | $\frac{\sqrt{x}}{\sqrt{1 - x}}$ |
| partial | concrete | `1/(sqrt(x)*sqrt(1 - x))` | $\frac{1}{\sqrt{x} \sqrt{1 - x}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(-b*x + 1))` | $\frac{1}{\sqrt{x} \sqrt{- b x + 1}}$ |
| SOLVED-both | parametric | `x**(5/3)*(a + b*x)` | $x^{\frac{5}{3}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `x**(4/3)*(a + b*x)` | $x^{\frac{4}{3}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `x**(2/3)*(a + b*x)` | $x^{\frac{2}{3}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `x**(1/3)*(a + b*x)` | $\sqrt[3]{x} \left(a + b x\right)$ |
| SOLVED-both | parametric | `(a + b*x)/x**(1/3)` | $\frac{a + b x}{\sqrt[3]{x}}$ |
| SOLVED-both | parametric | `(a + b*x)/x**(2/3)` | $\frac{a + b x}{x^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `(a + b*x)/x**(4/3)` | $\frac{a + b x}{x^{\frac{4}{3}}}$ |
| SOLVED-both | parametric | `(a + b*x)/x**(5/3)` | $\frac{a + b x}{x^{\frac{5}{3}}}$ |
| SOLVED-both | parametric | `x**(5/3)*(a + b*x)**2` | $x^{\frac{5}{3}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `x**(4/3)*(a + b*x)**2` | $x^{\frac{4}{3}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `x**(2/3)*(a + b*x)**2` | $x^{\frac{2}{3}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `x**(1/3)*(a + b*x)**2` | $\sqrt[3]{x} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x)**2/x**(1/3)` | $\frac{\left(a + b x\right)^{2}}{\sqrt[3]{x}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/x**(2/3)` | $\frac{\left(a + b x\right)^{2}}{x^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/x**(4/3)` | $\frac{\left(a + b x\right)^{2}}{x^{\frac{4}{3}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/x**(5/3)` | $\frac{\left(a + b x\right)^{2}}{x^{\frac{5}{3}}}$ |
| SOLVED-both | parametric | `x**(5/3)*(a + b*x)**3` | $x^{\frac{5}{3}} \left(a + b x\right)^{3}$ |
| SOLVED-both | parametric | `x**(4/3)*(a + b*x)**3` | $x^{\frac{4}{3}} \left(a + b x\right)^{3}$ |
| SOLVED-both | parametric | `x**(2/3)*(a + b*x)**3` | $x^{\frac{2}{3}} \left(a + b x\right)^{3}$ |
| SOLVED-both | parametric | `x**(1/3)*(a + b*x)**3` | $\sqrt[3]{x} \left(a + b x\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x)**3/x**(1/3)` | $\frac{\left(a + b x\right)^{3}}{\sqrt[3]{x}}$ |
| SOLVED-both | parametric | `(a + b*x)**3/x**(2/3)` | $\frac{\left(a + b x\right)^{3}}{x^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `(a + b*x)**3/x**(4/3)` | $\frac{\left(a + b x\right)^{3}}{x^{\frac{4}{3}}}$ |
| SOLVED-both | parametric | `(a + b*x)**3/x**(5/3)` | $\frac{\left(a + b x\right)^{3}}{x^{\frac{5}{3}}}$ |
| partial | parametric | `x**(5/3)/(a + b*x)` | $\frac{x^{\frac{5}{3}}}{a + b x}$ |
| partial | parametric | `x**(4/3)/(a + b*x)` | $\frac{x^{\frac{4}{3}}}{a + b x}$ |
| partial | parametric | `x**(2/3)/(a + b*x)` | $\frac{x^{\frac{2}{3}}}{a + b x}$ |
| partial | parametric | `x**(1/3)/(a + b*x)` | $\frac{\sqrt[3]{x}}{a + b x}$ |
| partial | parametric | `1/(x**(1/3)*(a + b*x))` | $\frac{1}{\sqrt[3]{x} \left(a + b x\right)}$ |
| partial | parametric | `1/(x**(2/3)*(a + b*x))` | $\frac{1}{x^{\frac{2}{3}} \left(a + b x\right)}$ |
| partial | parametric | `1/(x**(4/3)*(a + b*x))` | $\frac{1}{x^{\frac{4}{3}} \left(a + b x\right)}$ |
| partial | parametric | `1/(x**(5/3)*(a + b*x))` | $\frac{1}{x^{\frac{5}{3}} \left(a + b x\right)}$ |
| partial | parametric | `x**(5/3)/(a + b*x)**2` | $\frac{x^{\frac{5}{3}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `x**(4/3)/(a + b*x)**2` | $\frac{x^{\frac{4}{3}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `x**(2/3)/(a + b*x)**2` | $\frac{x^{\frac{2}{3}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `x**(1/3)/(a + b*x)**2` | $\frac{\sqrt[3]{x}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `1/(x**(1/3)*(a + b*x)**2)` | $\frac{1}{\sqrt[3]{x} \left(a + b x\right)^{2}}$ |
| partial | parametric | `1/(x**(2/3)*(a + b*x)**2)` | $\frac{1}{x^{\frac{2}{3}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `1/(x**(4/3)*(a + b*x)**2)` | $\frac{1}{x^{\frac{4}{3}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `1/(x**(5/3)*(a + b*x)**2)` | $\frac{1}{x^{\frac{5}{3}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x**(5/3)/(a + b*x)**3` | $\frac{x^{\frac{5}{3}}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `x**(4/3)/(a + b*x)**3` | $\frac{x^{\frac{4}{3}}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `x**(2/3)/(a + b*x)**3` | $\frac{x^{\frac{2}{3}}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `x**(1/3)/(a + b*x)**3` | $\frac{\sqrt[3]{x}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `1/(x**(1/3)*(a + b*x)**3)` | $\frac{1}{\sqrt[3]{x} \left(a + b x\right)^{3}}$ |
| partial | parametric | `1/(x**(2/3)*(a + b*x)**3)` | $\frac{1}{x^{\frac{2}{3}} \left(a + b x\right)^{3}}$ |
| partial | parametric | `1/(x**(4/3)*(a + b*x)**3)` | $\frac{1}{x^{\frac{4}{3}} \left(a + b x\right)^{3}}$ |
| partial | parametric | `1/(x**(5/3)*(a + b*x)**3)` | $\frac{1}{x^{\frac{5}{3}} \left(a + b x\right)^{3}}$ |
| partial | concrete | `(1 - x)**(1/4)/(x + 1)` | $\frac{\sqrt[4]{1 - x}}{x + 1}$ |
| SOLVED-both | parametric | `x**3*sqrt(c*x**2)*(a + b*x)` | $x^{3} \sqrt{c x^{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `x**2*sqrt(c*x**2)*(a + b*x)` | $x^{2} \sqrt{c x^{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `x*sqrt(c*x**2)*(a + b*x)` | $x \sqrt{c x^{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `sqrt(c*x**2)*(a + b*x)` | $\sqrt{c x^{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `sqrt(c*x**2)*(a + b*x)/x` | $\frac{\sqrt{c x^{2}} \left(a + b x\right)}{x}$ |
| SOLVED-both | parametric | `sqrt(c*x**2)*(a + b*x)/x**2` | $\frac{\sqrt{c x^{2}} \left(a + b x\right)}{x^{2}}$ |
| SOLVED-both | parametric | `sqrt(c*x**2)*(a + b*x)/x**3` | $\frac{\sqrt{c x^{2}} \left(a + b x\right)}{x^{3}}$ |
| SOLVED-both | parametric | `sqrt(c*x**2)*(a + b*x)/x**4` | $\frac{\sqrt{c x^{2}} \left(a + b x\right)}{x^{4}}$ |
| SOLVED-both | parametric | `x**3*(c*x**2)**(3/2)*(a + b*x)` | $x^{3} \left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `x**2*(c*x**2)**(3/2)*(a + b*x)` | $x^{2} \left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `x*(c*x**2)**(3/2)*(a + b*x)` | $x \left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `(c*x**2)**(3/2)*(a + b*x)` | $\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `(c*x**2)**(3/2)*(a + b*x)/x` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)}{x}$ |
| SOLVED-both | parametric | `(c*x**2)**(3/2)*(a + b*x)/x**2` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)}{x^{2}}$ |
| SOLVED-both | parametric | `(c*x**2)**(3/2)*(a + b*x)/x**3` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)}{x^{3}}$ |
| SOLVED-both | parametric | `(c*x**2)**(3/2)*(a + b*x)/x**4` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)}{x^{4}}$ |
| SOLVED-both | parametric | `x**3*(c*x**2)**(5/2)*(a + b*x)` | $x^{3} \left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `x**2*(c*x**2)**(5/2)*(a + b*x)` | $x^{2} \left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `x*(c*x**2)**(5/2)*(a + b*x)` | $x \left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `(c*x**2)**(5/2)*(a + b*x)` | $\left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)$ |
| SOLVED-both | parametric | `(c*x**2)**(5/2)*(a + b*x)/x` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)}{x}$ |
| SOLVED-both | parametric | `(c*x**2)**(5/2)*(a + b*x)/x**2` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)}{x^{2}}$ |
| SOLVED-both | parametric | `(c*x**2)**(5/2)*(a + b*x)/x**3` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)}{x^{3}}$ |
| SOLVED-both | parametric | `(c*x**2)**(5/2)*(a + b*x)/x**4` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)}{x^{4}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x)/sqrt(c*x**2)` | $\frac{x^{3} \left(a + b x\right)}{\sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x)/sqrt(c*x**2)` | $\frac{x^{2} \left(a + b x\right)}{\sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `x*(a + b*x)/sqrt(c*x**2)` | $\frac{x \left(a + b x\right)}{\sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/sqrt(c*x**2)` | $\frac{a + b x}{\sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(x*sqrt(c*x**2))` | $\frac{a + b x}{x \sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(x**2*sqrt(c*x**2))` | $\frac{a + b x}{x^{2} \sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(x**3*sqrt(c*x**2))` | $\frac{a + b x}{x^{3} \sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(x**4*sqrt(c*x**2))` | $\frac{a + b x}{x^{4} \sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x)/(c*x**2)**(3/2)` | $\frac{x^{3} \left(a + b x\right)}{\left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x)/(c*x**2)**(3/2)` | $\frac{x^{2} \left(a + b x\right)}{\left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x*(a + b*x)/(c*x**2)**(3/2)` | $\frac{x \left(a + b x\right)}{\left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(c*x**2)**(3/2)` | $\frac{a + b x}{\left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(x*(c*x**2)**(3/2))` | $\frac{a + b x}{x \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(x**2*(c*x**2)**(3/2))` | $\frac{a + b x}{x^{2} \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(x**3*(c*x**2)**(3/2))` | $\frac{a + b x}{x^{3} \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(x**4*(c*x**2)**(3/2))` | $\frac{a + b x}{x^{4} \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x)/(c*x**2)**(5/2)` | $\frac{x^{3} \left(a + b x\right)}{\left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x)/(c*x**2)**(5/2)` | $\frac{x^{2} \left(a + b x\right)}{\left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x*(a + b*x)/(c*x**2)**(5/2)` | $\frac{x \left(a + b x\right)}{\left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(c*x**2)**(5/2)` | $\frac{a + b x}{\left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(x*(c*x**2)**(5/2))` | $\frac{a + b x}{x \left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(x**2*(c*x**2)**(5/2))` | $\frac{a + b x}{x^{2} \left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(x**3*(c*x**2)**(5/2))` | $\frac{a + b x}{x^{3} \left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(x**4*(c*x**2)**(5/2))` | $\frac{a + b x}{x^{4} \left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**3*sqrt(c*x**2)*(a + b*x)**2` | $x^{3} \sqrt{c x^{2}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `x**2*sqrt(c*x**2)*(a + b*x)**2` | $x^{2} \sqrt{c x^{2}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `x*sqrt(c*x**2)*(a + b*x)**2` | $x \sqrt{c x^{2}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(c*x**2)*(a + b*x)**2` | $\sqrt{c x^{2}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(c*x**2)*(a + b*x)**2/x` | $\frac{\sqrt{c x^{2}} \left(a + b x\right)^{2}}{x}$ |
| SOLVED-both | parametric | `sqrt(c*x**2)*(a + b*x)**2/x**2` | $\frac{\sqrt{c x^{2}} \left(a + b x\right)^{2}}{x^{2}}$ |
| SOLVED-both | parametric | `sqrt(c*x**2)*(a + b*x)**2/x**3` | $\frac{\sqrt{c x^{2}} \left(a + b x\right)^{2}}{x^{3}}$ |
| SOLVED-both | parametric | `sqrt(c*x**2)*(a + b*x)**2/x**4` | $\frac{\sqrt{c x^{2}} \left(a + b x\right)^{2}}{x^{4}}$ |
| SOLVED-both | parametric | `x**3*(c*x**2)**(3/2)*(a + b*x)**2` | $x^{3} \left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `x**2*(c*x**2)**(3/2)*(a + b*x)**2` | $x^{2} \left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `x*(c*x**2)**(3/2)*(a + b*x)**2` | $x \left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `(c*x**2)**(3/2)*(a + b*x)**2` | $\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `(c*x**2)**(3/2)*(a + b*x)**2/x` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}}{x}$ |
| SOLVED-both | parametric | `(c*x**2)**(3/2)*(a + b*x)**2/x**2` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}}{x^{2}}$ |
| SOLVED-both | parametric | `(c*x**2)**(3/2)*(a + b*x)**2/x**3` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}}{x^{3}}$ |
| SOLVED-both | parametric | `(c*x**2)**(3/2)*(a + b*x)**2/x**4` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}}{x^{4}}$ |
| SOLVED-both | parametric | `x*(c*x**2)**(5/2)*(a + b*x)**2` | $x \left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `(c*x**2)**(5/2)*(a + b*x)**2` | $\left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `(c*x**2)**(5/2)*(a + b*x)**2/x` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)^{2}}{x}$ |
| SOLVED-both | parametric | `(c*x**2)**(5/2)*(a + b*x)**2/x**2` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)^{2}}{x^{2}}$ |
| SOLVED-both | parametric | `(c*x**2)**(5/2)*(a + b*x)**2/x**3` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)^{2}}{x^{3}}$ |
| SOLVED-both | parametric | `(c*x**2)**(5/2)*(a + b*x)**2/x**4` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)^{2}}{x^{4}}$ |
| SOLVED-both | parametric | `(c*x**2)**(5/2)*(a + b*x)**2/x**5` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)^{2}}{x^{5}}$ |
| SOLVED-both | parametric | `(c*x**2)**(5/2)*(a + b*x)**2/x**6` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}} \left(a + b x\right)^{2}}{x^{6}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x)**2/sqrt(c*x**2)` | $\frac{x^{3} \left(a + b x\right)^{2}}{\sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x)**2/sqrt(c*x**2)` | $\frac{x^{2} \left(a + b x\right)^{2}}{\sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `x*(a + b*x)**2/sqrt(c*x**2)` | $\frac{x \left(a + b x\right)^{2}}{\sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/sqrt(c*x**2)` | $\frac{\left(a + b x\right)^{2}}{\sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(x*sqrt(c*x**2))` | $\frac{\left(a + b x\right)^{2}}{x \sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(x**2*sqrt(c*x**2))` | $\frac{\left(a + b x\right)^{2}}{x^{2} \sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(x**3*sqrt(c*x**2))` | $\frac{\left(a + b x\right)^{2}}{x^{3} \sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(x**4*sqrt(c*x**2))` | $\frac{\left(a + b x\right)^{2}}{x^{4} \sqrt{c x^{2}}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x)**2/(c*x**2)**(3/2)` | $\frac{x^{3} \left(a + b x\right)^{2}}{\left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x)**2/(c*x**2)**(3/2)` | $\frac{x^{2} \left(a + b x\right)^{2}}{\left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x*(a + b*x)**2/(c*x**2)**(3/2)` | $\frac{x \left(a + b x\right)^{2}}{\left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(c*x**2)**(3/2)` | $\frac{\left(a + b x\right)^{2}}{\left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(x*(c*x**2)**(3/2))` | $\frac{\left(a + b x\right)^{2}}{x \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(x**2*(c*x**2)**(3/2))` | $\frac{\left(a + b x\right)^{2}}{x^{2} \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(x**3*(c*x**2)**(3/2))` | $\frac{\left(a + b x\right)^{2}}{x^{3} \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(x**4*(c*x**2)**(3/2))` | $\frac{\left(a + b x\right)^{2}}{x^{4} \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x)**2/(c*x**2)**(5/2)` | $\frac{x^{3} \left(a + b x\right)^{2}}{\left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x)**2/(c*x**2)**(5/2)` | $\frac{x^{2} \left(a + b x\right)^{2}}{\left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x*(a + b*x)**2/(c*x**2)**(5/2)` | $\frac{x \left(a + b x\right)^{2}}{\left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(c*x**2)**(5/2)` | $\frac{\left(a + b x\right)^{2}}{\left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(x*(c*x**2)**(5/2))` | $\frac{\left(a + b x\right)^{2}}{x \left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(x**2*(c*x**2)**(5/2))` | $\frac{\left(a + b x\right)^{2}}{x^{2} \left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(x**3*(c*x**2)**(5/2))` | $\frac{\left(a + b x\right)^{2}}{x^{3} \left(c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(x**4*(c*x**2)**(5/2))` | $\frac{\left(a + b x\right)^{2}}{x^{4} \left(c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3*sqrt(c*x**2)/(a + b*x)` | $\frac{x^{3} \sqrt{c x^{2}}}{a + b x}$ |
| partial | parametric | `x**2*sqrt(c*x**2)/(a + b*x)` | $\frac{x^{2} \sqrt{c x^{2}}}{a + b x}$ |
| partial | parametric | `x*sqrt(c*x**2)/(a + b*x)` | $\frac{x \sqrt{c x^{2}}}{a + b x}$ |
| partial | parametric | `sqrt(c*x**2)/(a + b*x)` | $\frac{\sqrt{c x^{2}}}{a + b x}$ |
| partial | parametric | `sqrt(c*x**2)/(x*(a + b*x))` | $\frac{\sqrt{c x^{2}}}{x \left(a + b x\right)}$ |
| partial | parametric | `sqrt(c*x**2)/(x**2*(a + b*x))` | $\frac{\sqrt{c x^{2}}}{x^{2} \left(a + b x\right)}$ |
| partial | parametric | `sqrt(c*x**2)/(x**3*(a + b*x))` | $\frac{\sqrt{c x^{2}}}{x^{3} \left(a + b x\right)}$ |
| partial | parametric | `sqrt(c*x**2)/(x**4*(a + b*x))` | $\frac{\sqrt{c x^{2}}}{x^{4} \left(a + b x\right)}$ |
| partial | parametric | `x*(c*x**2)**(3/2)/(a + b*x)` | $\frac{x \left(c x^{2}\right)^{\frac{3}{2}}}{a + b x}$ |
| partial | parametric | `(c*x**2)**(3/2)/(a + b*x)` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{a + b x}$ |
| partial | parametric | `(c*x**2)**(3/2)/(x*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(3/2)/(x**2*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x^{2} \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(3/2)/(x**3*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x^{3} \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(3/2)/(x**4*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x^{4} \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(3/2)/(x**5*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x^{5} \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(3/2)/(x**6*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x^{6} \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(3/2)/(x**7*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x^{7} \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(5/2)/(a + b*x)` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}}}{a + b x}$ |
| partial | parametric | `(c*x**2)**(5/2)/(x*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}}}{x \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(5/2)/(x**2*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}}}{x^{2} \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(5/2)/(x**3*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}}}{x^{3} \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(5/2)/(x**4*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}}}{x^{4} \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(5/2)/(x**5*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}}}{x^{5} \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(5/2)/(x**6*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}}}{x^{6} \left(a + b x\right)}$ |
| partial | parametric | `(c*x**2)**(5/2)/(x**7*(a + b*x))` | $\frac{\left(c x^{2}\right)^{\frac{5}{2}}}{x^{7} \left(a + b x\right)}$ |
| partial | parametric | `x**4/(sqrt(c*x**2)*(a + b*x))` | $\frac{x^{4}}{\sqrt{c x^{2}} \left(a + b x\right)}$ |
| partial | parametric | `x**3/(sqrt(c*x**2)*(a + b*x))` | $\frac{x^{3}}{\sqrt{c x^{2}} \left(a + b x\right)}$ |
| partial | parametric | `x**2/(sqrt(c*x**2)*(a + b*x))` | $\frac{x^{2}}{\sqrt{c x^{2}} \left(a + b x\right)}$ |
| partial | parametric | `x/(sqrt(c*x**2)*(a + b*x))` | $\frac{x}{\sqrt{c x^{2}} \left(a + b x\right)}$ |
| partial | parametric | `1/(sqrt(c*x**2)*(a + b*x))` | $\frac{1}{\sqrt{c x^{2}} \left(a + b x\right)}$ |
| partial | parametric | `1/(x*sqrt(c*x**2)*(a + b*x))` | $\frac{1}{x \sqrt{c x^{2}} \left(a + b x\right)}$ |
| partial | parametric | `1/(x**2*sqrt(c*x**2)*(a + b*x))` | $\frac{1}{x^{2} \sqrt{c x^{2}} \left(a + b x\right)}$ |
| partial | parametric | `1/(x**3*sqrt(c*x**2)*(a + b*x))` | $\frac{1}{x^{3} \sqrt{c x^{2}} \left(a + b x\right)}$ |
| partial | parametric | `x**6/((c*x**2)**(3/2)*(a + b*x))` | $\frac{x^{6}}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)}$ |
| partial | parametric | `x**5/((c*x**2)**(3/2)*(a + b*x))` | $\frac{x^{5}}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)}$ |
| partial | parametric | `x**4/((c*x**2)**(3/2)*(a + b*x))` | $\frac{x^{4}}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)}$ |
| partial | parametric | `x**3/((c*x**2)**(3/2)*(a + b*x))` | $\frac{x^{3}}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)}$ |
| partial | parametric | `x**2/((c*x**2)**(3/2)*(a + b*x))` | $\frac{x^{2}}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)}$ |
| partial | parametric | `x/((c*x**2)**(3/2)*(a + b*x))` | $\frac{x}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)}$ |
| partial | parametric | `1/((c*x**2)**(3/2)*(a + b*x))` | $\frac{1}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)}$ |
| partial | parametric | `1/(x*(c*x**2)**(3/2)*(a + b*x))` | $\frac{1}{x \left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)}$ |
| partial | parametric | `x**3*sqrt(c*x**2)/(a + b*x)**2` | $\frac{x^{3} \sqrt{c x^{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `x**2*sqrt(c*x**2)/(a + b*x)**2` | $\frac{x^{2} \sqrt{c x^{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `x*sqrt(c*x**2)/(a + b*x)**2` | $\frac{x \sqrt{c x^{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `sqrt(c*x**2)/(a + b*x)**2` | $\frac{\sqrt{c x^{2}}}{\left(a + b x\right)^{2}}$ |
| SOLVED-both | parametric | `sqrt(c*x**2)/(x*(a + b*x)**2)` | $\frac{\sqrt{c x^{2}}}{x \left(a + b x\right)^{2}}$ |
| partial | parametric | `sqrt(c*x**2)/(x**2*(a + b*x)**2)` | $\frac{\sqrt{c x^{2}}}{x^{2} \left(a + b x\right)^{2}}$ |
| partial | parametric | `sqrt(c*x**2)/(x**3*(a + b*x)**2)` | $\frac{\sqrt{c x^{2}}}{x^{3} \left(a + b x\right)^{2}}$ |
| partial | parametric | `sqrt(c*x**2)/(x**4*(a + b*x)**2)` | $\frac{\sqrt{c x^{2}}}{x^{4} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x*(c*x**2)**(3/2)/(a + b*x)**2` | $\frac{x \left(c x^{2}\right)^{\frac{3}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `(c*x**2)**(3/2)/(a + b*x)**2` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `(c*x**2)**(3/2)/(x*(a + b*x)**2)` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x \left(a + b x\right)^{2}}$ |
| partial | parametric | `(c*x**2)**(3/2)/(x**2*(a + b*x)**2)` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x^{2} \left(a + b x\right)^{2}}$ |
| SOLVED-both | parametric | `(c*x**2)**(3/2)/(x**3*(a + b*x)**2)` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x^{3} \left(a + b x\right)^{2}}$ |
| partial | parametric | `(c*x**2)**(3/2)/(x**4*(a + b*x)**2)` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x^{4} \left(a + b x\right)^{2}}$ |
| partial | parametric | `(c*x**2)**(3/2)/(x**5*(a + b*x)**2)` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x^{5} \left(a + b x\right)^{2}}$ |
| partial | parametric | `(c*x**2)**(3/2)/(x**6*(a + b*x)**2)` | $\frac{\left(c x^{2}\right)^{\frac{3}{2}}}{x^{6} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x**5/(sqrt(c*x**2)*(a + b*x)**2)` | $\frac{x^{5}}{\sqrt{c x^{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x**4/(sqrt(c*x**2)*(a + b*x)**2)` | $\frac{x^{4}}{\sqrt{c x^{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x**3/(sqrt(c*x**2)*(a + b*x)**2)` | $\frac{x^{3}}{\sqrt{c x^{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x**2/(sqrt(c*x**2)*(a + b*x)**2)` | $\frac{x^{2}}{\sqrt{c x^{2}} \left(a + b x\right)^{2}}$ |
| SOLVED-both | parametric | `x/(sqrt(c*x**2)*(a + b*x)**2)` | $\frac{x}{\sqrt{c x^{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `1/(sqrt(c*x**2)*(a + b*x)**2)` | $\frac{1}{\sqrt{c x^{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `1/(x*sqrt(c*x**2)*(a + b*x)**2)` | $\frac{1}{x \sqrt{c x^{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `1/(x**2*sqrt(c*x**2)*(a + b*x)**2)` | $\frac{1}{x^{2} \sqrt{c x^{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x**5/((c*x**2)**(3/2)*(a + b*x)**2)` | $\frac{x^{5}}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x**4/((c*x**2)**(3/2)*(a + b*x)**2)` | $\frac{x^{4}}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}}$ |
| SOLVED-both | parametric | `x**3/((c*x**2)**(3/2)*(a + b*x)**2)` | $\frac{x^{3}}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x**2/((c*x**2)**(3/2)*(a + b*x)**2)` | $\frac{x^{2}}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x/((c*x**2)**(3/2)*(a + b*x)**2)` | $\frac{x}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `1/((c*x**2)**(3/2)*(a + b*x)**2)` | $\frac{1}{\left(c x^{2}\right)^{\frac{3}{2}} \left(a + b x\right)^{2}}$ |
| SOLVED-both | concrete | `1/(sqrt(-3*x - 2)*sqrt(3*x + 2))` | $\frac{1}{\sqrt{- 3 x - 2} \sqrt{3 x + 2}}$ |
| partial | concrete | `(1 - x)**(9/2)*sqrt(x + 1)` | $\left(1 - x\right)^{\frac{9}{2}} \sqrt{x + 1}$ |
| partial | concrete | `(1 - x)**(7/2)*sqrt(x + 1)` | $\left(1 - x\right)^{\frac{7}{2}} \sqrt{x + 1}$ |
| partial | concrete | `(1 - x)**(5/2)*sqrt(x + 1)` | $\left(1 - x\right)^{\frac{5}{2}} \sqrt{x + 1}$ |
| partial | concrete | `(1 - x)**(3/2)*sqrt(x + 1)` | $\left(1 - x\right)^{\frac{3}{2}} \sqrt{x + 1}$ |
| partial | concrete | `sqrt(1 - x)*sqrt(x + 1)` | $\sqrt{1 - x} \sqrt{x + 1}$ |
| partial | concrete | `sqrt(x + 1)/sqrt(1 - x)` | $\frac{\sqrt{x + 1}}{\sqrt{1 - x}}$ |
| partial | concrete | `sqrt(x + 1)/(1 - x)**(3/2)` | $\frac{\sqrt{x + 1}}{\left(1 - x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `sqrt(x + 1)/(1 - x)**(5/2)` | $\frac{\sqrt{x + 1}}{\left(1 - x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `sqrt(x + 1)/(1 - x)**(7/2)` | $\frac{\sqrt{x + 1}}{\left(1 - x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | concrete | `sqrt(x + 1)/(1 - x)**(9/2)` | $\frac{\sqrt{x + 1}}{\left(1 - x\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | concrete | `sqrt(x + 1)/(1 - x)**(11/2)` | $\frac{\sqrt{x + 1}}{\left(1 - x\right)^{\frac{11}{2}}}$ |
| **SOLVED-NEW** | concrete | `sqrt(x + 1)/(1 - x)**(13/2)` | $\frac{\sqrt{x + 1}}{\left(1 - x\right)^{\frac{13}{2}}}$ |
| partial | concrete | `(1 - x)**(9/2)*(x + 1)**(3/2)` | $\left(1 - x\right)^{\frac{9}{2}} \left(x + 1\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - x)**(7/2)*(x + 1)**(3/2)` | $\left(1 - x\right)^{\frac{7}{2}} \left(x + 1\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - x)**(5/2)*(x + 1)**(3/2)` | $\left(1 - x\right)^{\frac{5}{2}} \left(x + 1\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - x)**(3/2)*(x + 1)**(3/2)` | $\left(1 - x\right)^{\frac{3}{2}} \left(x + 1\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(1 - x)*(x + 1)**(3/2)` | $\sqrt{1 - x} \left(x + 1\right)^{\frac{3}{2}}$ |
| partial | concrete | `(x + 1)**(3/2)/sqrt(1 - x)` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{\sqrt{1 - x}}$ |
| partial | concrete | `(x + 1)**(3/2)/(1 - x)**(3/2)` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{\left(1 - x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x + 1)**(3/2)/(1 - x)**(5/2)` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{\left(1 - x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(x + 1)**(3/2)/(1 - x)**(7/2)` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{\left(1 - x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | concrete | `(x + 1)**(3/2)/(1 - x)**(9/2)` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{\left(1 - x\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | concrete | `(x + 1)**(3/2)/(1 - x)**(11/2)` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{\left(1 - x\right)^{\frac{11}{2}}}$ |
| **SOLVED-NEW** | concrete | `(x + 1)**(3/2)/(1 - x)**(13/2)` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{\left(1 - x\right)^{\frac{13}{2}}}$ |
| **SOLVED-NEW** | concrete | `(x + 1)**(3/2)/(1 - x)**(15/2)` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{\left(1 - x\right)^{\frac{15}{2}}}$ |
| partial | concrete | `(1 - x)**(11/2)*(x + 1)**(5/2)` | $\left(1 - x\right)^{\frac{11}{2}} \left(x + 1\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - x)**(9/2)*(x + 1)**(5/2)` | $\left(1 - x\right)^{\frac{9}{2}} \left(x + 1\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - x)**(7/2)*(x + 1)**(5/2)` | $\left(1 - x\right)^{\frac{7}{2}} \left(x + 1\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - x)**(5/2)*(x + 1)**(5/2)` | $\left(1 - x\right)^{\frac{5}{2}} \left(x + 1\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - x)**(3/2)*(x + 1)**(5/2)` | $\left(1 - x\right)^{\frac{3}{2}} \left(x + 1\right)^{\frac{5}{2}}$ |
| partial | concrete | `sqrt(1 - x)*(x + 1)**(5/2)` | $\sqrt{1 - x} \left(x + 1\right)^{\frac{5}{2}}$ |
| partial | concrete | `(x + 1)**(5/2)/sqrt(1 - x)` | $\frac{\left(x + 1\right)^{\frac{5}{2}}}{\sqrt{1 - x}}$ |
| partial | concrete | `(x + 1)**(5/2)/(1 - x)**(3/2)` | $\frac{\left(x + 1\right)^{\frac{5}{2}}}{\left(1 - x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x + 1)**(5/2)/(1 - x)**(5/2)` | $\frac{\left(x + 1\right)^{\frac{5}{2}}}{\left(1 - x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(x + 1)**(5/2)/(1 - x)**(7/2)` | $\frac{\left(x + 1\right)^{\frac{5}{2}}}{\left(1 - x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | concrete | `(x + 1)**(5/2)/(1 - x)**(9/2)` | $\frac{\left(x + 1\right)^{\frac{5}{2}}}{\left(1 - x\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | concrete | `(x + 1)**(5/2)/(1 - x)**(11/2)` | $\frac{\left(x + 1\right)^{\frac{5}{2}}}{\left(1 - x\right)^{\frac{11}{2}}}$ |
| **SOLVED-NEW** | concrete | `(x + 1)**(5/2)/(1 - x)**(13/2)` | $\frac{\left(x + 1\right)^{\frac{5}{2}}}{\left(1 - x\right)^{\frac{13}{2}}}$ |
| **SOLVED-NEW** | concrete | `(x + 1)**(5/2)/(1 - x)**(15/2)` | $\frac{\left(x + 1\right)^{\frac{5}{2}}}{\left(1 - x\right)^{\frac{15}{2}}}$ |
| **SOLVED-NEW** | concrete | `(x + 1)**(5/2)/(1 - x)**(17/2)` | $\frac{\left(x + 1\right)^{\frac{5}{2}}}{\left(1 - x\right)^{\frac{17}{2}}}$ |
| **SOLVED-NEW** | concrete | `(x + 1)**(5/2)/(1 - x)**(19/2)` | $\frac{\left(x + 1\right)^{\frac{5}{2}}}{\left(1 - x\right)^{\frac{19}{2}}}$ |
| partial | parametric | `(a*x + 1)**(3/2)/sqrt(-a*x + 1)` | $\frac{\left(a x + 1\right)^{\frac{3}{2}}}{\sqrt{- a x + 1}}$ |
| partial | parametric | `(a*x + 1)*sqrt(-a**2*x**2 + 1)/(-a*x + 1)` | $\frac{\left(a x + 1\right) \sqrt{- a^{2} x^{2} + 1}}{- a x + 1}$ |
| partial | concrete | `(1 - x)**(7/2)/sqrt(x + 1)` | $\frac{\left(1 - x\right)^{\frac{7}{2}}}{\sqrt{x + 1}}$ |
| partial | concrete | `(1 - x)**(5/2)/sqrt(x + 1)` | $\frac{\left(1 - x\right)^{\frac{5}{2}}}{\sqrt{x + 1}}$ |
| partial | concrete | `(1 - x)**(3/2)/sqrt(x + 1)` | $\frac{\left(1 - x\right)^{\frac{3}{2}}}{\sqrt{x + 1}}$ |
| partial | concrete | `sqrt(1 - x)/sqrt(x + 1)` | $\frac{\sqrt{1 - x}}{\sqrt{x + 1}}$ |
| partial | concrete | `1/(sqrt(1 - x)*sqrt(x + 1))` | $\frac{1}{\sqrt{1 - x} \sqrt{x + 1}}$ |
| SOLVED-both | concrete | `1/((1 - x)**(3/2)*sqrt(x + 1))` | $\frac{1}{\left(1 - x\right)^{\frac{3}{2}} \sqrt{x + 1}}$ |
| SOLVED-both | concrete | `1/((1 - x)**(5/2)*sqrt(x + 1))` | $\frac{1}{\left(1 - x\right)^{\frac{5}{2}} \sqrt{x + 1}}$ |
| SOLVED-both | concrete | `1/((1 - x)**(7/2)*sqrt(x + 1))` | $\frac{1}{\left(1 - x\right)^{\frac{7}{2}} \sqrt{x + 1}}$ |
| SOLVED-both | concrete | `1/((1 - x)**(9/2)*sqrt(x + 1))` | $\frac{1}{\left(1 - x\right)^{\frac{9}{2}} \sqrt{x + 1}}$ |
| **SOLVED-NEW** | concrete | `1/((1 - x)**(11/2)*sqrt(x + 1))` | $\frac{1}{\left(1 - x\right)^{\frac{11}{2}} \sqrt{x + 1}}$ |
| partial | concrete | `(1 - x)**(7/2)/(x + 1)**(3/2)` | $\frac{\left(1 - x\right)^{\frac{7}{2}}}{\left(x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - x)**(5/2)/(x + 1)**(3/2)` | $\frac{\left(1 - x\right)^{\frac{5}{2}}}{\left(x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - x)**(3/2)/(x + 1)**(3/2)` | $\frac{\left(1 - x\right)^{\frac{3}{2}}}{\left(x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - x)/(x + 1)**(3/2)` | $\frac{\sqrt{1 - x}}{\left(x + 1\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/(sqrt(1 - x)*(x + 1)**(3/2))` | $\frac{1}{\sqrt{1 - x} \left(x + 1\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/((1 - x)**(3/2)*(x + 1)**(3/2))` | $\frac{1}{\left(1 - x\right)^{\frac{3}{2}} \left(x + 1\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/((1 - x)**(5/2)*(x + 1)**(3/2))` | $\frac{1}{\left(1 - x\right)^{\frac{5}{2}} \left(x + 1\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/((1 - x)**(7/2)*(x + 1)**(3/2))` | $\frac{1}{\left(1 - x\right)^{\frac{7}{2}} \left(x + 1\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | concrete | `1/((1 - x)**(9/2)*(x + 1)**(3/2))` | $\frac{1}{\left(1 - x\right)^{\frac{9}{2}} \left(x + 1\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | concrete | `1/((1 - x)**(11/2)*(x + 1)**(3/2))` | $\frac{1}{\left(1 - x\right)^{\frac{11}{2}} \left(x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - x)**(9/2)/(x + 1)**(5/2)` | $\frac{\left(1 - x\right)^{\frac{9}{2}}}{\left(x + 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - x)**(7/2)/(x + 1)**(5/2)` | $\frac{\left(1 - x\right)^{\frac{7}{2}}}{\left(x + 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - x)**(5/2)/(x + 1)**(5/2)` | $\frac{\left(1 - x\right)^{\frac{5}{2}}}{\left(x + 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - x)**(3/2)/(x + 1)**(5/2)` | $\frac{\left(1 - x\right)^{\frac{3}{2}}}{\left(x + 1\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `sqrt(1 - x)/(x + 1)**(5/2)` | $\frac{\sqrt{1 - x}}{\left(x + 1\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `1/(sqrt(1 - x)*(x + 1)**(5/2))` | $\frac{1}{\sqrt{1 - x} \left(x + 1\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `1/((1 - x)**(3/2)*(x + 1)**(5/2))` | $\frac{1}{\left(1 - x\right)^{\frac{3}{2}} \left(x + 1\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `1/((1 - x)**(5/2)*(x + 1)**(5/2))` | $\frac{1}{\left(1 - x\right)^{\frac{5}{2}} \left(x + 1\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `1/((1 - x)**(7/2)*(x + 1)**(5/2))` | $\frac{1}{\left(1 - x\right)^{\frac{7}{2}} \left(x + 1\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | concrete | `1/((1 - x)**(9/2)*(x + 1)**(5/2))` | $\frac{1}{\left(1 - x\right)^{\frac{9}{2}} \left(x + 1\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | concrete | `1/((1 - x)**(11/2)*(x + 1)**(5/2))` | $\frac{1}{\left(1 - x\right)^{\frac{11}{2}} \left(x + 1\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a*x + a)**(5/2)*(-c*x + c)**(5/2)` | $\left(a x + a\right)^{\frac{5}{2}} \left(- c x + c\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a*x + a)**(3/2)*(-c*x + c)**(3/2)` | $\left(a x + a\right)^{\frac{3}{2}} \left(- c x + c\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(a*x + a)*sqrt(-c*x + c)` | $\sqrt{a x + a} \sqrt{- c x + c}$ |
| partial | parametric | `1/(sqrt(a*x + a)*sqrt(-c*x + c))` | $\frac{1}{\sqrt{a x + a} \sqrt{- c x + c}}$ |
| SOLVED-both | parametric | `1/((a*x + a)**(3/2)*(-c*x + c)**(3/2))` | $\frac{1}{\left(a x + a\right)^{\frac{3}{2}} \left(- c x + c\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/((a*x + a)**(5/2)*(-c*x + c)**(5/2))` | $\frac{1}{\left(a x + a\right)^{\frac{5}{2}} \left(- c x + c\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a*x + a)**(7/2)*(-c*x + c)**(7/2))` | $\frac{1}{\left(a x + a\right)^{\frac{7}{2}} \left(- c x + c\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a*x + a)**(9/2)*(-c*x + c)**(9/2))` | $\frac{1}{\left(a x + a\right)^{\frac{9}{2}} \left(- c x + c\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x)**(5/2)*(a*c - b*c*x)**(5/2)` | $\left(a + b x\right)^{\frac{5}{2}} \left(a c - b c x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(a*c - b*c*x)**(3/2)` | $\left(a + b x\right)^{\frac{3}{2}} \left(a c - b c x\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(a + b*x)*sqrt(a*c - b*c*x)` | $\sqrt{a + b x} \sqrt{a c - b c x}$ |
| partial | parametric | `1/(sqrt(a + b*x)*sqrt(a*c - b*c*x))` | $\frac{1}{\sqrt{a + b x} \sqrt{a c - b c x}}$ |
| SOLVED-both | parametric | `1/((a + b*x)**(3/2)*(a*c - b*c*x)**(3/2))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(a c - b c x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/((a + b*x)**(5/2)*(a*c - b*c*x)**(5/2))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \left(a c - b c x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(7/2)*(a*c - b*c*x)**(7/2))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{2}} \left(a c - b c x\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(9/2)*(a*c - b*c*x)**(9/2))` | $\frac{1}{\left(a + b x\right)^{\frac{9}{2}} \left(a c - b c x\right)^{\frac{9}{2}}}$ |
| partial | concrete | `(3 - 6*x)**(5/2)*(4*x + 2)**(5/2)` | $\left(3 - 6 x\right)^{\frac{5}{2}} \left(4 x + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(3 - 6*x)**(3/2)*(4*x + 2)**(3/2)` | $\left(3 - 6 x\right)^{\frac{3}{2}} \left(4 x + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(3 - 6*x)*sqrt(4*x + 2)` | $\sqrt{3 - 6 x} \sqrt{4 x + 2}$ |
| partial | concrete | `1/(sqrt(3 - 6*x)*sqrt(4*x + 2))` | $\frac{1}{\sqrt{3 - 6 x} \sqrt{4 x + 2}}$ |
| SOLVED-both | concrete | `1/((3 - 6*x)**(3/2)*(4*x + 2)**(3/2))` | $\frac{1}{\left(3 - 6 x\right)^{\frac{3}{2}} \left(4 x + 2\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | concrete | `1/((3 - 6*x)**(5/2)*(4*x + 2)**(5/2))` | $\frac{1}{\left(3 - 6 x\right)^{\frac{5}{2}} \left(4 x + 2\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | concrete | `1/((3 - 6*x)**(7/2)*(4*x + 2)**(7/2))` | $\frac{1}{\left(3 - 6 x\right)^{\frac{7}{2}} \left(4 x + 2\right)^{\frac{7}{2}}}$ |
| partial | concrete | `(3 - x)**(3/2)*(x - 2)**(3/2)` | $\left(3 - x\right)^{\frac{3}{2}} \left(x - 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(3 - x)*sqrt(x - 2)` | $\sqrt{3 - x} \sqrt{x - 2}$ |
| partial | concrete | `1/(sqrt(3 - x)*sqrt(x - 2))` | $\frac{1}{\sqrt{3 - x} \sqrt{x - 2}}$ |
| SOLVED-both | concrete | `1/((3 - x)**(3/2)*(x - 2)**(3/2))` | $\frac{1}{\left(3 - x\right)^{\frac{3}{2}} \left(x - 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/((3 - x)**(5/2)*(x - 2)**(5/2))` | $\frac{1}{\left(3 - x\right)^{\frac{5}{2}} \left(x - 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `1/((3 - x)**(3/2)*(x + 3)**(3/2))` | $\frac{1}{\left(3 - x\right)^{\frac{3}{2}} \left(x + 3\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/((-b*x + 3)**(3/2)*(b*x + 3)**(3/2))` | $\frac{1}{\left(- b x + 3\right)^{\frac{3}{2}} \left(b x + 3\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/((6 - 2*x)**(3/2)*(x + 3)**(3/2))` | $\frac{1}{\left(6 - 2 x\right)^{\frac{3}{2}} \left(x + 3\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/((-2*b*x + 6)**(3/2)*(b*x + 3)**(3/2))` | $\frac{1}{\left(- 2 b x + 6\right)^{\frac{3}{2}} \left(b x + 3\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*sqrt(-a*d + b*d*x))` | $\frac{1}{\sqrt{a + b x} \sqrt{- a d + b d x}}$ |
| partial | parametric | `1/((-3*e*x + 6)**(1/4)*(e*x + 2)**(3/4))` | $\frac{1}{\sqrt[4]{- 3 e x + 6} \left(e x + 2\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(7/4)/(I*a*x + a)**(1/4)` | $\frac{\left(- i a x + a\right)^{\frac{7}{4}}}{\sqrt[4]{i a x + a}}$ |
| partial | parametric | `(-I*a*x + a)**(3/4)/(I*a*x + a)**(1/4)` | $\frac{\left(- i a x + a\right)^{\frac{3}{4}}}{\sqrt[4]{i a x + a}}$ |
| partial | parametric | `1/((-I*a*x + a)**(1/4)*(I*a*x + a)**(1/4))` | $\frac{1}{\sqrt[4]{- i a x + a} \sqrt[4]{i a x + a}}$ |
| partial | parametric | `1/((-I*a*x + a)**(5/4)*(I*a*x + a)**(1/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{5}{4}} \sqrt[4]{i a x + a}}$ |
| partial | parametric | `1/((-I*a*x + a)**(9/4)*(I*a*x + a)**(1/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{9}{4}} \sqrt[4]{i a x + a}}$ |
| partial | parametric | `1/((-I*a*x + a)**(13/4)*(I*a*x + a)**(1/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{13}{4}} \sqrt[4]{i a x + a}}$ |
| partial | parametric | `1/((-I*a*x + a)**(17/4)*(I*a*x + a)**(1/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{17}{4}} \sqrt[4]{i a x + a}}$ |
| partial | parametric | `(-I*a*x + a)**(1/4)/(I*a*x + a)**(1/4)` | $\frac{\sqrt[4]{- i a x + a}}{\sqrt[4]{i a x + a}}$ |
| partial | parametric | `1/((-I*a*x + a)**(3/4)*(I*a*x + a)**(1/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{3}{4}} \sqrt[4]{i a x + a}}$ |
| partial | parametric | `1/((-I*a*x + a)**(7/4)*(I*a*x + a)**(1/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{7}{4}} \sqrt[4]{i a x + a}}$ |
| partial | parametric | `1/((-I*a*x + a)**(11/4)*(I*a*x + a)**(1/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{11}{4}} \sqrt[4]{i a x + a}}$ |
| partial | parametric | `1/((-I*a*x + a)**(15/4)*(I*a*x + a)**(1/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{15}{4}} \sqrt[4]{i a x + a}}$ |
| partial | parametric | `1/((-I*a*x + a)**(19/4)*(I*a*x + a)**(1/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{19}{4}} \sqrt[4]{i a x + a}}$ |
| partial | parametric | `(-I*a*x + a)**(3/4)/(I*a*x + a)**(3/4)` | $\frac{\left(- i a x + a\right)^{\frac{3}{4}}}{\left(i a x + a\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(1/4)*(I*a*x + a)**(3/4))` | $\frac{1}{\sqrt[4]{- i a x + a} \left(i a x + a\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(5/4)*(I*a*x + a)**(3/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{5}{4}} \left(i a x + a\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(9/4)*(I*a*x + a)**(3/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{9}{4}} \left(i a x + a\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(13/4)*(I*a*x + a)**(3/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{13}{4}} \left(i a x + a\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(5/4)/(I*a*x + a)**(3/4)` | $\frac{\left(- i a x + a\right)^{\frac{5}{4}}}{\left(i a x + a\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(1/4)/(I*a*x + a)**(3/4)` | $\frac{\sqrt[4]{- i a x + a}}{\left(i a x + a\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(3/4)*(I*a*x + a)**(3/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{3}{4}} \left(i a x + a\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(7/4)*(I*a*x + a)**(3/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{7}{4}} \left(i a x + a\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(11/4)*(I*a*x + a)**(3/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{11}{4}} \left(i a x + a\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(7/4)/(I*a*x + a)**(7/4)` | $\frac{\left(- i a x + a\right)^{\frac{7}{4}}}{\left(i a x + a\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(3/4)/(I*a*x + a)**(7/4)` | $\frac{\left(- i a x + a\right)^{\frac{3}{4}}}{\left(i a x + a\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(1/4)*(I*a*x + a)**(7/4))` | $\frac{1}{\sqrt[4]{- i a x + a} \left(i a x + a\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(5/4)*(I*a*x + a)**(7/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{5}{4}} \left(i a x + a\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(9/4)*(I*a*x + a)**(7/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{9}{4}} \left(i a x + a\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(9/4)/(I*a*x + a)**(7/4)` | $\frac{\left(- i a x + a\right)^{\frac{9}{4}}}{\left(i a x + a\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(5/4)/(I*a*x + a)**(7/4)` | $\frac{\left(- i a x + a\right)^{\frac{5}{4}}}{\left(i a x + a\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(1/4)/(I*a*x + a)**(7/4)` | $\frac{\sqrt[4]{- i a x + a}}{\left(i a x + a\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(3/4)*(I*a*x + a)**(7/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{3}{4}} \left(i a x + a\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(7/4)*(I*a*x + a)**(7/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{7}{4}} \left(i a x + a\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(11/4)*(I*a*x + a)**(7/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{11}{4}} \left(i a x + a\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(15/4)*(I*a*x + a)**(7/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{15}{4}} \left(i a x + a\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(7/4)/(I*a*x + a)**(5/4)` | $\frac{\left(- i a x + a\right)^{\frac{7}{4}}}{\left(i a x + a\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(3/4)/(I*a*x + a)**(5/4)` | $\frac{\left(- i a x + a\right)^{\frac{3}{4}}}{\left(i a x + a\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(1/4)*(I*a*x + a)**(5/4))` | $\frac{1}{\sqrt[4]{- i a x + a} \left(i a x + a\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(5/4)*(I*a*x + a)**(5/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{5}{4}} \left(i a x + a\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(9/4)*(I*a*x + a)**(5/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{9}{4}} \left(i a x + a\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(13/4)*(I*a*x + a)**(5/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{13}{4}} \left(i a x + a\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(5/4)/(I*a*x + a)**(5/4)` | $\frac{\left(- i a x + a\right)^{\frac{5}{4}}}{\left(i a x + a\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(1/4)/(I*a*x + a)**(5/4)` | $\frac{\sqrt[4]{- i a x + a}}{\left(i a x + a\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(3/4)*(I*a*x + a)**(5/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{3}{4}} \left(i a x + a\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(7/4)*(I*a*x + a)**(5/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{7}{4}} \left(i a x + a\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(11/4)*(I*a*x + a)**(5/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{11}{4}} \left(i a x + a\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(7/4)/(I*a*x + a)**(9/4)` | $\frac{\left(- i a x + a\right)^{\frac{7}{4}}}{\left(i a x + a\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(3/4)/(I*a*x + a)**(9/4)` | $\frac{\left(- i a x + a\right)^{\frac{3}{4}}}{\left(i a x + a\right)^{\frac{9}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(1/4)*(I*a*x + a)**(9/4))` | $\frac{1}{\sqrt[4]{- i a x + a} \left(i a x + a\right)^{\frac{9}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(5/4)*(I*a*x + a)**(9/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{5}{4}} \left(i a x + a\right)^{\frac{9}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(9/4)*(I*a*x + a)**(9/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{9}{4}} \left(i a x + a\right)^{\frac{9}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(13/4)*(I*a*x + a)**(9/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{13}{4}} \left(i a x + a\right)^{\frac{9}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(17/4)*(I*a*x + a)**(9/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{17}{4}} \left(i a x + a\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(-I*a*x + a)**(5/4)/(I*a*x + a)**(9/4)` | $\frac{\left(- i a x + a\right)^{\frac{5}{4}}}{\left(i a x + a\right)^{\frac{9}{4}}}$ |
| **SOLVED-NEW** | parametric | `(-I*a*x + a)**(1/4)/(I*a*x + a)**(9/4)` | $\frac{\sqrt[4]{- i a x + a}}{\left(i a x + a\right)^{\frac{9}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(3/4)*(I*a*x + a)**(9/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{3}{4}} \left(i a x + a\right)^{\frac{9}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(7/4)*(I*a*x + a)**(9/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{7}{4}} \left(i a x + a\right)^{\frac{9}{4}}}$ |
| partial | parametric | `1/((-I*a*x + a)**(11/4)*(I*a*x + a)**(9/4))` | $\frac{1}{\left(- i a x + a\right)^{\frac{11}{4}} \left(i a x + a\right)^{\frac{9}{4}}}$ |
| SOLVED-both | parametric | `(a + b*x)**5*sqrt(c + d*x)` | $\left(a + b x\right)^{5} \sqrt{c + d x}$ |
| SOLVED-both | parametric | `(a + b*x)**4*sqrt(c + d*x)` | $\left(a + b x\right)^{4} \sqrt{c + d x}$ |
| SOLVED-both | parametric | `(a + b*x)**3*sqrt(c + d*x)` | $\left(a + b x\right)^{3} \sqrt{c + d x}$ |
| SOLVED-both | parametric | `(a + b*x)**2*sqrt(c + d*x)` | $\left(a + b x\right)^{2} \sqrt{c + d x}$ |
| SOLVED-both | parametric | `(a + b*x)*sqrt(c + d*x)` | $\left(a + b x\right) \sqrt{c + d x}$ |
| SOLVED-both | parametric | `sqrt(c + d*x)` | $\sqrt{c + d x}$ |
| partial | parametric | `sqrt(c + d*x)/(a + b*x)` | $\frac{\sqrt{c + d x}}{a + b x}$ |
| partial | parametric | `sqrt(c + d*x)/(a + b*x)**2` | $\frac{\sqrt{c + d x}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x)/(a + b*x)**3` | $\frac{\sqrt{c + d x}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `sqrt(c + d*x)/(a + b*x)**4` | $\frac{\sqrt{c + d x}}{\left(a + b x\right)^{4}}$ |
| partial | parametric | `sqrt(c + d*x)/(a + b*x)**5` | $\frac{\sqrt{c + d x}}{\left(a + b x\right)^{5}}$ |
| partial | parametric | `sqrt(c + d*x)/(a + b*x)**6` | $\frac{\sqrt{c + d x}}{\left(a + b x\right)^{6}}$ |
| SOLVED-both | parametric | `(a + b*x)**5*(c + d*x)**(3/2)` | $\left(a + b x\right)^{5} \left(c + d x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)**4*(c + d*x)**(3/2)` | $\left(a + b x\right)^{4} \left(c + d x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)**3*(c + d*x)**(3/2)` | $\left(a + b x\right)^{3} \left(c + d x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)**2*(c + d*x)**(3/2)` | $\left(a + b x\right)^{2} \left(c + d x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(c + d*x)**(3/2)` | $\left(a + b x\right) \left(c + d x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(c + d*x)**(3/2)` | $\left(c + d x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(c + d*x)**(3/2)/(a + b*x)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{a + b x}$ |
| partial | parametric | `(c + d*x)**(3/2)/(a + b*x)**2` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `(c + d*x)**(3/2)/(a + b*x)**3` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `(c + d*x)**(3/2)/(a + b*x)**4` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{4}}$ |
| partial | parametric | `(c + d*x)**(3/2)/(a + b*x)**5` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{5}}$ |
| partial | parametric | `(c + d*x)**(3/2)/(a + b*x)**6` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{6}}$ |
| SOLVED-both | parametric | `(a + b*x)**5*(c + d*x)**(5/2)` | $\left(a + b x\right)^{5} \left(c + d x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)**4*(c + d*x)**(5/2)` | $\left(a + b x\right)^{4} \left(c + d x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)**3*(c + d*x)**(5/2)` | $\left(a + b x\right)^{3} \left(c + d x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)**2*(c + d*x)**(5/2)` | $\left(a + b x\right)^{2} \left(c + d x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(c + d*x)**(5/2)` | $\left(a + b x\right) \left(c + d x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(c + d*x)**(5/2)` | $\left(c + d x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{a + b x}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)**2` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)**3` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)**4` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{4}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)**5` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{5}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)**6` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{6}}$ |
| partial | concrete | `sqrt(x - 1)/(x + 1)**2` | $\frac{\sqrt{x - 1}}{\left(x + 1\right)^{2}}$ |
| partial | concrete | `sqrt(x - 1)/(x + 1)**3` | $\frac{\sqrt{x - 1}}{\left(x + 1\right)^{3}}$ |
| SOLVED-both | parametric | `(a + b*x)**5/sqrt(c + d*x)` | $\frac{\left(a + b x\right)^{5}}{\sqrt{c + d x}}$ |
| SOLVED-both | parametric | `(a + b*x)**4/sqrt(c + d*x)` | $\frac{\left(a + b x\right)^{4}}{\sqrt{c + d x}}$ |
| SOLVED-both | parametric | `(a + b*x)**3/sqrt(c + d*x)` | $\frac{\left(a + b x\right)^{3}}{\sqrt{c + d x}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/sqrt(c + d*x)` | $\frac{\left(a + b x\right)^{2}}{\sqrt{c + d x}}$ |
| SOLVED-both | parametric | `(a + b*x)/sqrt(c + d*x)` | $\frac{a + b x}{\sqrt{c + d x}}$ |
| SOLVED-both | parametric | `1/sqrt(c + d*x)` | $\frac{1}{\sqrt{c + d x}}$ |
| partial | parametric | `1/((a + b*x)*sqrt(c + d*x))` | $\frac{1}{\left(a + b x\right) \sqrt{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**2*sqrt(c + d*x))` | $\frac{1}{\left(a + b x\right)^{2} \sqrt{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**3*sqrt(c + d*x))` | $\frac{1}{\left(a + b x\right)^{3} \sqrt{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**4*sqrt(c + d*x))` | $\frac{1}{\left(a + b x\right)^{4} \sqrt{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**5*sqrt(c + d*x))` | $\frac{1}{\left(a + b x\right)^{5} \sqrt{c + d x}}$ |
| SOLVED-both | parametric | `(a + b*x)**5/(c + d*x)**(3/2)` | $\frac{\left(a + b x\right)^{5}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**4/(c + d*x)**(3/2)` | $\frac{\left(a + b x\right)^{4}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**3/(c + d*x)**(3/2)` | $\frac{\left(a + b x\right)^{3}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(c + d*x)**(3/2)` | $\frac{\left(a + b x\right)^{2}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(c + d*x)**(3/2)` | $\frac{a + b x}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(c + d*x)**(-3/2)` | $\frac{1}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x)*(c + d*x)**(3/2))` | $\frac{1}{\left(a + b x\right) \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x)**2*(c + d*x)**(3/2))` | $\frac{1}{\left(a + b x\right)^{2} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x)**3*(c + d*x)**(3/2))` | $\frac{1}{\left(a + b x\right)^{3} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x)**4*(c + d*x)**(3/2))` | $\frac{1}{\left(a + b x\right)^{4} \left(c + d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**5/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right)^{5}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**4/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right)^{4}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**3/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right)^{3}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right)^{2}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(c + d*x)**(5/2)` | $\frac{a + b x}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(c + d*x)**(-5/2)` | $\frac{1}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((a + b*x)*(c + d*x)**(5/2))` | $\frac{1}{\left(a + b x\right) \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((a + b*x)**2*(c + d*x)**(5/2))` | $\frac{1}{\left(a + b x\right)^{2} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((a + b*x)**3*(c + d*x)**(5/2))` | $\frac{1}{\left(a + b x\right)^{3} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((a + b*x)**4*(c + d*x)**(5/2))` | $\frac{1}{\left(a + b x\right)^{4} \left(c + d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**5*(a*c + b*c*x)**(3/2)` | $\left(a + b x\right)^{5} \left(a c + b c x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)**5*sqrt(a*c + b*c*x)` | $\left(a + b x\right)^{5} \sqrt{a c + b c x}$ |
| SOLVED-both | parametric | `(a + b*x)**5/sqrt(a*c + b*c*x)` | $\frac{\left(a + b x\right)^{5}}{\sqrt{a c + b c x}}$ |
| SOLVED-both | parametric | `(a + b*x)**5/(a*c + b*c*x)**(3/2)` | $\frac{\left(a + b x\right)^{5}}{\left(a c + b c x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**5/(a*c + b*c*x)**(5/2)` | $\frac{\left(a + b x\right)^{5}}{\left(a c + b c x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**5/(a*c + b*c*x)**(7/2)` | $\frac{\left(a + b x\right)^{5}}{\left(a c + b c x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**5/(a*c + b*c*x)**(9/2)` | $\frac{\left(a + b x\right)^{5}}{\left(a c + b c x\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**5/(a*c + b*c*x)**(11/2)` | $\frac{\left(a + b x\right)^{5}}{\left(a c + b c x\right)^{\frac{11}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**5/(a*c + b*c*x)**(13/2)` | $\frac{\left(a + b x\right)^{5}}{\left(a c + b c x\right)^{\frac{13}{2}}}$ |
| partial | concrete | `1/((x - 2)*sqrt(x + 2))` | $\frac{1}{\left(x - 2\right) \sqrt{x + 2}}$ |
| partial | concrete | `1/((3*x + 2)*sqrt(5*x + 1))` | $\frac{1}{\left(3 x + 2\right) \sqrt{5 x + 1}}$ |
| partial | concrete | `(1 - x)**(1/3)/(x + 1)` | $\frac{\sqrt[3]{1 - x}}{x + 1}$ |
| SOLVED-both | concrete | `(3 - 2*x)**(1/3)*(x + 7)` | $\sqrt[3]{3 - 2 x} \left(x + 7\right)$ |
| SOLVED-both | concrete | `(1 - x)**(1/3)*(x + 1)**2` | $\sqrt[3]{1 - x} \left(x + 1\right)^{2}$ |
| partial | parametric | `1/((a + b*x)*(c + d*x)**(1/3))` | $\frac{1}{\left(a + b x\right) \sqrt[3]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)*(c + d*x)**(2/3))` | $\frac{1}{\left(a + b x\right) \left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a + b*x)**(7/2)*sqrt(c + d*x)` | $\left(a + b x\right)^{\frac{7}{2}} \sqrt{c + d x}$ |
| partial | parametric | `(a + b*x)**(5/2)*sqrt(c + d*x)` | $\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x}$ |
| partial | parametric | `(a + b*x)**(3/2)*sqrt(c + d*x)` | $\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x}$ |
| partial | parametric | `sqrt(a + b*x)*sqrt(c + d*x)` | $\sqrt{a + b x} \sqrt{c + d x}$ |
| partial | parametric | `sqrt(c + d*x)/sqrt(a + b*x)` | $\frac{\sqrt{c + d x}}{\sqrt{a + b x}}$ |
| partial | parametric | `sqrt(c + d*x)/(a + b*x)**(3/2)` | $\frac{\sqrt{c + d x}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(c + d*x)/(a + b*x)**(5/2)` | $\frac{\sqrt{c + d x}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(c + d*x)/(a + b*x)**(7/2)` | $\frac{\sqrt{c + d x}}{\left(a + b x\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(c + d*x)/(a + b*x)**(9/2)` | $\frac{\sqrt{c + d x}}{\left(a + b x\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(c + d*x)/(a + b*x)**(11/2)` | $\frac{\sqrt{c + d x}}{\left(a + b x\right)^{\frac{11}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(c + d*x)/(a + b*x)**(13/2)` | $\frac{\sqrt{c + d x}}{\left(a + b x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(a + b*x)**(5/2)*(c + d*x)**(3/2)` | $\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(3/2)` | $\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)**(3/2)` | $\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(c + d*x)**(3/2)/sqrt(a + b*x)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\sqrt{a + b x}}$ |
| partial | parametric | `(c + d*x)**(3/2)/(a + b*x)**(3/2)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x)**(3/2)/(a + b*x)**(5/2)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(3/2)/(a + b*x)**(7/2)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(3/2)/(a + b*x)**(9/2)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(3/2)/(a + b*x)**(11/2)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{11}{2}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(3/2)/(a + b*x)**(13/2)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(a + b*x)**(5/2)*(c + d*x)**(5/2)` | $\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(5/2)` | $\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)**(5/2)` | $\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(c + d*x)**(5/2)/sqrt(a + b*x)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\sqrt{a + b x}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)**(3/2)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)**(5/2)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)**(7/2)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(5/2)/(a + b*x)**(9/2)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(5/2)/(a + b*x)**(11/2)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{11}{2}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(5/2)/(a + b*x)**(13/2)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{13}{2}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(5/2)/(a + b*x)**(15/2)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{15}{2}}}$ |
| partial | parametric | `(a + b*x)**(7/2)/sqrt(c + d*x)` | $\frac{\left(a + b x\right)^{\frac{7}{2}}}{\sqrt{c + d x}}$ |
| partial | parametric | `(a + b*x)**(5/2)/sqrt(c + d*x)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\sqrt{c + d x}}$ |
| partial | parametric | `(a + b*x)**(3/2)/sqrt(c + d*x)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\sqrt{c + d x}}$ |
| partial | parametric | `sqrt(a + b*x)/sqrt(c + d*x)` | $\frac{\sqrt{a + b x}}{\sqrt{c + d x}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*sqrt(c + d*x))` | $\frac{1}{\sqrt{a + b x} \sqrt{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(3/2)*sqrt(c + d*x))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(5/2)*sqrt(c + d*x))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(7/2)*sqrt(c + d*x))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{2}} \sqrt{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(9/2)*sqrt(c + d*x))` | $\frac{1}{\left(a + b x\right)^{\frac{9}{2}} \sqrt{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(11/2)*sqrt(c + d*x))` | $\frac{1}{\left(a + b x\right)^{\frac{11}{2}} \sqrt{c + d x}}$ |
| partial | parametric | `(a + b*x)**(7/2)/(c + d*x)**(3/2)` | $\frac{\left(a + b x\right)^{\frac{7}{2}}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)**(5/2)/(c + d*x)**(3/2)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(3/2)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(3/2)` | $\frac{\sqrt{a + b x}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(3/2))` | $\frac{1}{\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(3/2))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(7/2)*(c + d*x)**(3/2))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(9/2)*(c + d*x)**(3/2))` | $\frac{1}{\left(a + b x\right)^{\frac{9}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(11/2)*(c + d*x)**(3/2))` | $\frac{1}{\left(a + b x\right)^{\frac{11}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)**(9/2)/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right)^{\frac{9}{2}}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)**(7/2)/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right)^{\frac{7}{2}}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)**(5/2)/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a + b*x)/(c + d*x)**(5/2)` | $\frac{\sqrt{a + b x}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(5/2))` | $\frac{1}{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(5/2))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(5/2))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(7/2)*(c + d*x)**(5/2))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(9/2)*(c + d*x)**(5/2))` | $\frac{1}{\left(a + b x\right)^{\frac{9}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*sqrt(a + b*x + 4))` | $\frac{1}{\sqrt{a + b x} \sqrt{a + b x + 4}}$ |
| partial | parametric | `1/(sqrt(b*x + 2)*sqrt(b*x + 6))` | $\frac{1}{\sqrt{b x + 2} \sqrt{b x + 6}}$ |
| partial | parametric | `1/(sqrt(b*x + 1)*sqrt(b*x + 5))` | $\frac{1}{\sqrt{b x + 1} \sqrt{b x + 5}}$ |
| partial | parametric | `1/(sqrt(b*x)*sqrt(b*x + 4))` | $\frac{1}{\sqrt{b x} \sqrt{b x + 4}}$ |
| partial | parametric | `1/(sqrt(b*x - 1)*sqrt(b*x + 3))` | $\frac{1}{\sqrt{b x - 1} \sqrt{b x + 3}}$ |
| partial | parametric | `1/(sqrt(b*x - 2)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{b x - 2} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(b*x - 3)*sqrt(b*x + 1))` | $\frac{1}{\sqrt{b x - 3} \sqrt{b x + 1}}$ |
| partial | parametric | `1/(sqrt(b*x + 2)*sqrt(b*x + 3))` | $\frac{1}{\sqrt{b x + 2} \sqrt{b x + 3}}$ |
| partial | parametric | `1/(sqrt(b*x + 1)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{b x + 1} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(b*x)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{b x} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(b*x - 1)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{b x - 1} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(b*x - 2)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{b x - 2} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(b*x - 3)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{b x - 3} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(-b*x + 3)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{- b x + 3} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(-b*x + 2)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{- b x + 2} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(-b*x + 1)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{- b x + 1} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(-b*x)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{- b x} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(-b*x - 1)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{- b x - 1} \sqrt{b x + 2}}$ |
| SOLVED-both | parametric | `1/(sqrt(-b*x - 2)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{- b x - 2} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(-b*x - 3)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{- b x - 3} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(-b*x + 2)*sqrt(-b*x + 3))` | $\frac{1}{\sqrt{- b x + 2} \sqrt{- b x + 3}}$ |
| partial | parametric | `1/(sqrt(-b*x + 1)*sqrt(-b*x + 2))` | $\frac{1}{\sqrt{- b x + 1} \sqrt{- b x + 2}}$ |
| partial | parametric | `1/(sqrt(-b*x)*sqrt(-b*x + 2))` | $\frac{1}{\sqrt{- b x} \sqrt{- b x + 2}}$ |
| partial | parametric | `1/(sqrt(-b*x - 1)*sqrt(-b*x + 2))` | $\frac{1}{\sqrt{- b x - 1} \sqrt{- b x + 2}}$ |
| partial | parametric | `1/(sqrt(-b*x - 2)*sqrt(-b*x + 2))` | $\frac{1}{\sqrt{- b x - 2} \sqrt{- b x + 2}}$ |
| partial | parametric | `1/(sqrt(-b*x - 3)*sqrt(-b*x + 2))` | $\frac{1}{\sqrt{- b x - 3} \sqrt{- b x + 2}}$ |
| partial | parametric | `1/(sqrt(b*x - 4)*sqrt(b*x + 4))` | $\frac{1}{\sqrt{b x - 4} \sqrt{b x + 4}}$ |
| partial | parametric | `1/(sqrt(c + d*x)*sqrt(b*x + (b*c - b)/d))` | $\frac{1}{\sqrt{c + d x} \sqrt{b x + \frac{b c - b}{d}}}$ |
| partial | concrete | `1/(sqrt(x)*sqrt(2*x - 3))` | $\frac{1}{\sqrt{x} \sqrt{2 x - 3}}$ |
| partial | concrete | `1/(sqrt(2*x - 3)*sqrt(3*x + 2))` | $\frac{1}{\sqrt{2 x - 3} \sqrt{3 x + 2}}$ |
| partial | parametric | `1/(sqrt(c - d*x)*sqrt(b*x + (-b*c + b)/d))` | $\frac{1}{\sqrt{c - d x} \sqrt{b x + \frac{- b c + b}{d}}}$ |
| partial | concrete | `1/(sqrt(x)*sqrt(4 - x))` | $\frac{1}{\sqrt{x} \sqrt{4 - x}}$ |
| partial | concrete | `1/(sqrt(x)*sqrt(3 - 2*x))` | $\frac{1}{\sqrt{x} \sqrt{3 - 2 x}}$ |
| partial | concrete | `1/(sqrt(3 - 2*x)*sqrt(5*x + 3))` | $\frac{1}{\sqrt{3 - 2 x} \sqrt{5 x + 3}}$ |
| partial | parametric | `1/(sqrt(a - b*x)*sqrt(c + d*x))` | $\frac{1}{\sqrt{a - b x} \sqrt{c + d x}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(1/3)` | $\left(a + b x\right)^{\frac{3}{2}} \sqrt[3]{c + d x}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)**(1/3)` | $\sqrt{a + b x} \sqrt[3]{c + d x}$ |
| partial | parametric | `(c + d*x)**(1/3)/sqrt(a + b*x)` | $\frac{\sqrt[3]{c + d x}}{\sqrt{a + b x}}$ |
| partial | parametric | `(c + d*x)**(1/3)/(a + b*x)**(3/2)` | $\frac{\sqrt[3]{c + d x}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x)**(1/3)/(a + b*x)**(5/2)` | $\frac{\sqrt[3]{c + d x}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d*x)**(1/3)/(a + b*x)**(7/2)` | $\frac{\sqrt[3]{c + d x}}{\left(a + b x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(1/3)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\sqrt[3]{c + d x}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(1/3)` | $\frac{\sqrt{a + b x}}{\sqrt[3]{c + d x}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(1/3))` | $\frac{1}{\sqrt{a + b x} \sqrt[3]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(1/3))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \sqrt[3]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(1/3))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \sqrt[3]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(2/3)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(2/3)` | $\frac{\sqrt{a + b x}}{\left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(2/3))` | $\frac{1}{\sqrt{a + b x} \left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(2/3))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(2/3))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a + b*x)**(2/3)*(c + d*x)**(1/3)` | $\left(a + b x\right)^{\frac{2}{3}} \sqrt[3]{c + d x}$ |
| partial | parametric | `(c + d*x)**(1/3)/(a + b*x)**(1/3)` | $\frac{\sqrt[3]{c + d x}}{\sqrt[3]{a + b x}}$ |
| partial | parametric | `(c + d*x)**(1/3)/(a + b*x)**(4/3)` | $\frac{\sqrt[3]{c + d x}}{\left(a + b x\right)^{\frac{4}{3}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(1/3)/(a + b*x)**(7/3)` | $\frac{\sqrt[3]{c + d x}}{\left(a + b x\right)^{\frac{7}{3}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(1/3)/(a + b*x)**(10/3)` | $\frac{\sqrt[3]{c + d x}}{\left(a + b x\right)^{\frac{10}{3}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(1/3)/(a + b*x)**(13/3)` | $\frac{\sqrt[3]{c + d x}}{\left(a + b x\right)^{\frac{13}{3}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(1/3)/(a + b*x)**(16/3)` | $\frac{\sqrt[3]{c + d x}}{\left(a + b x\right)^{\frac{16}{3}}}$ |
| partial | parametric | `(a + b*x)**(4/3)*(c + d*x)**(1/3)` | $\left(a + b x\right)^{\frac{4}{3}} \sqrt[3]{c + d x}$ |
| partial | parametric | `(a + b*x)**(1/3)*(c + d*x)**(1/3)` | $\sqrt[3]{a + b x} \sqrt[3]{c + d x}$ |
| partial | parametric | `(c + d*x)**(1/3)/(a + b*x)**(2/3)` | $\frac{\sqrt[3]{c + d x}}{\left(a + b x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(c + d*x)**(1/3)/(a + b*x)**(5/3)` | $\frac{\sqrt[3]{c + d x}}{\left(a + b x\right)^{\frac{5}{3}}}$ |
| partial | parametric | `(c + d*x)**(1/3)/(a + b*x)**(8/3)` | $\frac{\sqrt[3]{c + d x}}{\left(a + b x\right)^{\frac{8}{3}}}$ |
| partial | parametric | `(a + b*x)**(4/3)/(c + d*x)**(1/3)` | $\frac{\left(a + b x\right)^{\frac{4}{3}}}{\sqrt[3]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(1/3)/(c + d*x)**(1/3)` | $\frac{\sqrt[3]{a + b x}}{\sqrt[3]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(2/3)*(c + d*x)**(1/3))` | $\frac{1}{\left(a + b x\right)^{\frac{2}{3}} \sqrt[3]{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(5/3)*(c + d*x)**(1/3))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{3}} \sqrt[3]{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(8/3)*(c + d*x)**(1/3))` | $\frac{1}{\left(a + b x\right)^{\frac{8}{3}} \sqrt[3]{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(11/3)*(c + d*x)**(1/3))` | $\frac{1}{\left(a + b x\right)^{\frac{11}{3}} \sqrt[3]{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(14/3)*(c + d*x)**(1/3))` | $\frac{1}{\left(a + b x\right)^{\frac{14}{3}} \sqrt[3]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(8/3)/(c + d*x)**(1/3)` | $\frac{\left(a + b x\right)^{\frac{8}{3}}}{\sqrt[3]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(5/3)/(c + d*x)**(1/3)` | $\frac{\left(a + b x\right)^{\frac{5}{3}}}{\sqrt[3]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(2/3)/(c + d*x)**(1/3)` | $\frac{\left(a + b x\right)^{\frac{2}{3}}}{\sqrt[3]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(1/3)*(c + d*x)**(1/3))` | $\frac{1}{\sqrt[3]{a + b x} \sqrt[3]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(4/3)*(c + d*x)**(1/3))` | $\frac{1}{\left(a + b x\right)^{\frac{4}{3}} \sqrt[3]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(7/3)*(c + d*x)**(1/3))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{3}} \sqrt[3]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(10/3)*(c + d*x)**(1/3))` | $\frac{1}{\left(a + b x\right)^{\frac{10}{3}} \sqrt[3]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(5/3)/(c + d*x)**(2/3)` | $\frac{\left(a + b x\right)^{\frac{5}{3}}}{\left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a + b*x)**(2/3)/(c + d*x)**(2/3)` | $\frac{\left(a + b x\right)^{\frac{2}{3}}}{\left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((a + b*x)**(1/3)*(c + d*x)**(2/3))` | $\frac{1}{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(4/3)*(c + d*x)**(2/3))` | $\frac{1}{\left(a + b x\right)^{\frac{4}{3}} \left(c + d x\right)^{\frac{2}{3}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(7/3)*(c + d*x)**(2/3))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{3}} \left(c + d x\right)^{\frac{2}{3}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(10/3)*(c + d*x)**(2/3))` | $\frac{1}{\left(a + b x\right)^{\frac{10}{3}} \left(c + d x\right)^{\frac{2}{3}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(13/3)*(c + d*x)**(2/3))` | $\frac{1}{\left(a + b x\right)^{\frac{13}{3}} \left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a + b*x)**(7/3)/(c + d*x)**(2/3)` | $\frac{\left(a + b x\right)^{\frac{7}{3}}}{\left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a + b*x)**(4/3)/(c + d*x)**(2/3)` | $\frac{\left(a + b x\right)^{\frac{4}{3}}}{\left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a + b*x)**(1/3)/(c + d*x)**(2/3)` | $\frac{\sqrt[3]{a + b x}}{\left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((a + b*x)**(2/3)*(c + d*x)**(2/3))` | $\frac{1}{\left(a + b x\right)^{\frac{2}{3}} \left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((a + b*x)**(5/3)*(c + d*x)**(2/3))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{3}} \left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((a + b*x)**(8/3)*(c + d*x)**(2/3))` | $\frac{1}{\left(a + b x\right)^{\frac{8}{3}} \left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((a + b*x)**(11/3)*(c + d*x)**(2/3))` | $\frac{1}{\left(a + b x\right)^{\frac{11}{3}} \left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a + b*x)**(7/3)/(c + d*x)**(4/3)` | $\frac{\left(a + b x\right)^{\frac{7}{3}}}{\left(c + d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(a + b*x)**(4/3)/(c + d*x)**(4/3)` | $\frac{\left(a + b x\right)^{\frac{4}{3}}}{\left(c + d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(a + b*x)**(1/3)/(c + d*x)**(4/3)` | $\frac{\sqrt[3]{a + b x}}{\left(c + d x\right)^{\frac{4}{3}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(2/3)*(c + d*x)**(4/3))` | $\frac{1}{\left(a + b x\right)^{\frac{2}{3}} \left(c + d x\right)^{\frac{4}{3}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(5/3)*(c + d*x)**(4/3))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{3}} \left(c + d x\right)^{\frac{4}{3}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(8/3)*(c + d*x)**(4/3))` | $\frac{1}{\left(a + b x\right)^{\frac{8}{3}} \left(c + d x\right)^{\frac{4}{3}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(11/3)*(c + d*x)**(4/3))` | $\frac{1}{\left(a + b x\right)^{\frac{11}{3}} \left(c + d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(a + b*x)**(8/3)/(c + d*x)**(4/3)` | $\frac{\left(a + b x\right)^{\frac{8}{3}}}{\left(c + d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(a + b*x)**(5/3)/(c + d*x)**(4/3)` | $\frac{\left(a + b x\right)^{\frac{5}{3}}}{\left(c + d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(a + b*x)**(2/3)/(c + d*x)**(4/3)` | $\frac{\left(a + b x\right)^{\frac{2}{3}}}{\left(c + d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/((a + b*x)**(1/3)*(c + d*x)**(4/3))` | $\frac{1}{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/((a + b*x)**(4/3)*(c + d*x)**(4/3))` | $\frac{1}{\left(a + b x\right)^{\frac{4}{3}} \left(c + d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/((a + b*x)**(7/3)*(c + d*x)**(4/3))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{3}} \left(c + d x\right)^{\frac{4}{3}}}$ |
| partial | concrete | `(x - 1)**(1/3)/(x + 1)**(1/3)` | $\frac{\sqrt[3]{x - 1}}{\sqrt[3]{x + 1}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(1/4)` | $\left(a + b x\right)^{\frac{3}{2}} \sqrt[4]{c + d x}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)**(1/4)` | $\sqrt{a + b x} \sqrt[4]{c + d x}$ |
| partial | parametric | `(c + d*x)**(1/4)/sqrt(a + b*x)` | $\frac{\sqrt[4]{c + d x}}{\sqrt{a + b x}}$ |
| partial | parametric | `(c + d*x)**(1/4)/(a + b*x)**(3/2)` | $\frac{\sqrt[4]{c + d x}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x)**(1/4)/(a + b*x)**(5/2)` | $\frac{\sqrt[4]{c + d x}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d*x)**(1/4)/(a + b*x)**(7/2)` | $\frac{\sqrt[4]{c + d x}}{\left(a + b x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(3/4)` | $\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{4}}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)**(3/4)` | $\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{4}}$ |
| partial | parametric | `(c + d*x)**(3/4)/sqrt(a + b*x)` | $\frac{\left(c + d x\right)^{\frac{3}{4}}}{\sqrt{a + b x}}$ |
| partial | parametric | `(c + d*x)**(3/4)/(a + b*x)**(3/2)` | $\frac{\left(c + d x\right)^{\frac{3}{4}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x)**(3/4)/(a + b*x)**(5/2)` | $\frac{\left(c + d x\right)^{\frac{3}{4}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d*x)**(3/4)/(a + b*x)**(7/2)` | $\frac{\left(c + d x\right)^{\frac{3}{4}}}{\left(a + b x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(5/4)` | $\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{4}}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)**(5/4)` | $\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{4}}$ |
| partial | parametric | `(c + d*x)**(5/4)/sqrt(a + b*x)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\sqrt{a + b x}}$ |
| partial | parametric | `(c + d*x)**(5/4)/(a + b*x)**(3/2)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x)**(5/4)/(a + b*x)**(5/2)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d*x)**(5/4)/(a + b*x)**(7/2)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(c + d*x)**(5/4)/(a + b*x)**(9/2)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x)**(5/2)/(c + d*x)**(1/4)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\sqrt[4]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(1/4)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\sqrt[4]{c + d x}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(1/4)` | $\frac{\sqrt{a + b x}}{\sqrt[4]{c + d x}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(1/4))` | $\frac{1}{\sqrt{a + b x} \sqrt[4]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(1/4))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \sqrt[4]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(1/4))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \sqrt[4]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(3/4)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(3/4)` | $\frac{\sqrt{a + b x}}{\left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(3/4))` | $\frac{1}{\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(3/4))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(3/4))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(a + b*x)**(5/2)/(c + d*x)**(5/4)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(5/4)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(5/4)` | $\frac{\sqrt{a + b x}}{\left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(5/4))` | $\frac{1}{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(5/4))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(5/4))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(a + b*x)**(7/2)/(c + d*x)**(7/4)` | $\frac{\left(a + b x\right)^{\frac{7}{2}}}{\left(c + d x\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(7/4)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{7}{4}}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(7/4)` | $\frac{\sqrt{a + b x}}{\left(c + d x\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(7/4))` | $\frac{1}{\sqrt{a + b x} \left(c + d x\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(7/4))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(7/4))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(a + b*x)**(7/2)/(c + d*x)**(9/4)` | $\frac{\left(a + b x\right)^{\frac{7}{2}}}{\left(c + d x\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(a + b*x)**(5/2)/(c + d*x)**(9/4)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(9/4)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{9}{4}}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(9/4)` | $\frac{\sqrt{a + b x}}{\left(c + d x\right)^{\frac{9}{4}}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(9/4))` | $\frac{1}{\sqrt{a + b x} \left(c + d x\right)^{\frac{9}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(9/4))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{9}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(9/4))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(a + b*x)**(3/4)*(c + d*x)**(5/4)` | $\left(a + b x\right)^{\frac{3}{4}} \left(c + d x\right)^{\frac{5}{4}}$ |
| partial | parametric | `(c + d*x)**(5/4)/(a + b*x)**(1/4)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\sqrt[4]{a + b x}}$ |
| partial | parametric | `(c + d*x)**(5/4)/(a + b*x)**(5/4)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(c + d*x)**(5/4)/(a + b*x)**(9/4)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{9}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(5/4)/(a + b*x)**(13/4)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{13}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(5/4)/(a + b*x)**(17/4)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{17}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(5/4)/(a + b*x)**(21/4)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{21}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x)**(5/4)/(a + b*x)**(25/4)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{25}{4}}}$ |
| partial | parametric | `(a + b*x)**(5/4)*(c + d*x)**(5/4)` | $\left(a + b x\right)^{\frac{5}{4}} \left(c + d x\right)^{\frac{5}{4}}$ |
| partial | parametric | `(a + b*x)**(1/4)*(c + d*x)**(5/4)` | $\sqrt[4]{a + b x} \left(c + d x\right)^{\frac{5}{4}}$ |
| partial | parametric | `(c + d*x)**(5/4)/(a + b*x)**(3/4)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(c + d*x)**(5/4)/(a + b*x)**(7/4)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(c + d*x)**(5/4)/(a + b*x)**(11/4)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{11}{4}}}$ |
| partial | parametric | `(c + d*x)**(5/4)/(a + b*x)**(15/4)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{15}{4}}}$ |
| partial | parametric | `(c + d*x)**(5/4)/(a + b*x)**(19/4)` | $\frac{\left(c + d x\right)^{\frac{5}{4}}}{\left(a + b x\right)^{\frac{19}{4}}}$ |
| partial | parametric | `(a + b*x)**(5/4)/(c + d*x)**(1/4)` | $\frac{\left(a + b x\right)^{\frac{5}{4}}}{\sqrt[4]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(1/4)/(c + d*x)**(1/4)` | $\frac{\sqrt[4]{a + b x}}{\sqrt[4]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(3/4)*(c + d*x)**(1/4))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{4}} \sqrt[4]{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(7/4)*(c + d*x)**(1/4))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{4}} \sqrt[4]{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(11/4)*(c + d*x)**(1/4))` | $\frac{1}{\left(a + b x\right)^{\frac{11}{4}} \sqrt[4]{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(15/4)*(c + d*x)**(1/4))` | $\frac{1}{\left(a + b x\right)^{\frac{15}{4}} \sqrt[4]{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(19/4)*(c + d*x)**(1/4))` | $\frac{1}{\left(a + b x\right)^{\frac{19}{4}} \sqrt[4]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(7/4)/(c + d*x)**(1/4)` | $\frac{\left(a + b x\right)^{\frac{7}{4}}}{\sqrt[4]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(3/4)/(c + d*x)**(1/4)` | $\frac{\left(a + b x\right)^{\frac{3}{4}}}{\sqrt[4]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(1/4)*(c + d*x)**(1/4))` | $\frac{1}{\sqrt[4]{a + b x} \sqrt[4]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(5/4)*(c + d*x)**(1/4))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{4}} \sqrt[4]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(9/4)*(c + d*x)**(1/4))` | $\frac{1}{\left(a + b x\right)^{\frac{9}{4}} \sqrt[4]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(7/4)/(c + d*x)**(3/4)` | $\frac{\left(a + b x\right)^{\frac{7}{4}}}{\left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(a + b*x)**(3/4)/(c + d*x)**(3/4)` | $\frac{\left(a + b x\right)^{\frac{3}{4}}}{\left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(1/4)*(c + d*x)**(3/4))` | $\frac{1}{\sqrt[4]{a + b x} \left(c + d x\right)^{\frac{3}{4}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(5/4)*(c + d*x)**(3/4))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{4}} \left(c + d x\right)^{\frac{3}{4}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(9/4)*(c + d*x)**(3/4))` | $\frac{1}{\left(a + b x\right)^{\frac{9}{4}} \left(c + d x\right)^{\frac{3}{4}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(13/4)*(c + d*x)**(3/4))` | $\frac{1}{\left(a + b x\right)^{\frac{13}{4}} \left(c + d x\right)^{\frac{3}{4}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(17/4)*(c + d*x)**(3/4))` | $\frac{1}{\left(a + b x\right)^{\frac{17}{4}} \left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(a + b*x)**(5/4)/(c + d*x)**(3/4)` | $\frac{\left(a + b x\right)^{\frac{5}{4}}}{\left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(a + b*x)**(1/4)/(c + d*x)**(3/4)` | $\frac{\sqrt[4]{a + b x}}{\left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(3/4)*(c + d*x)**(3/4))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{4}} \left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(7/4)*(c + d*x)**(3/4))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{4}} \left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(11/4)*(c + d*x)**(3/4))` | $\frac{1}{\left(a + b x\right)^{\frac{11}{4}} \left(c + d x\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(a + b*x)**(5/4)/(c + d*x)**(5/4)` | $\frac{\left(a + b x\right)^{\frac{5}{4}}}{\left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(a + b*x)**(1/4)/(c + d*x)**(5/4)` | $\frac{\sqrt[4]{a + b x}}{\left(c + d x\right)^{\frac{5}{4}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(3/4)*(c + d*x)**(5/4))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{4}} \left(c + d x\right)^{\frac{5}{4}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(7/4)*(c + d*x)**(5/4))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{4}} \left(c + d x\right)^{\frac{5}{4}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(11/4)*(c + d*x)**(5/4))` | $\frac{1}{\left(a + b x\right)^{\frac{11}{4}} \left(c + d x\right)^{\frac{5}{4}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(15/4)*(c + d*x)**(5/4))` | $\frac{1}{\left(a + b x\right)^{\frac{15}{4}} \left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(a + b*x)**(11/4)/(c + d*x)**(5/4)` | $\frac{\left(a + b x\right)^{\frac{11}{4}}}{\left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(a + b*x)**(7/4)/(c + d*x)**(5/4)` | $\frac{\left(a + b x\right)^{\frac{7}{4}}}{\left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(a + b*x)**(3/4)/(c + d*x)**(5/4)` | $\frac{\left(a + b x\right)^{\frac{3}{4}}}{\left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(1/4)*(c + d*x)**(5/4))` | $\frac{1}{\sqrt[4]{a + b x} \left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(5/4)*(c + d*x)**(5/4))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{4}} \left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((a + b*x)**(9/4)*(c + d*x)**(5/4))` | $\frac{1}{\left(a + b x\right)^{\frac{9}{4}} \left(c + d x\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((-a*x + 1)**(1/4)*(b*x + 1)**(3/4))` | $\frac{1}{\sqrt[4]{- a x + 1} \left(b x + 1\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((-a*x + 1)**(1/4)*(a*x + 1)**(3/4))` | $\frac{1}{\sqrt[4]{- a x + 1} \left(a x + 1\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(1/5)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\sqrt[5]{c + d x}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(1/5)` | $\frac{\sqrt{a + b x}}{\sqrt[5]{c + d x}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(1/5))` | $\frac{1}{\sqrt{a + b x} \sqrt[5]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(1/5))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \sqrt[5]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(1/5))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \sqrt[5]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(5/2)*(c + d*x)**(1/6)` | $\left(a + b x\right)^{\frac{5}{2}} \sqrt[6]{c + d x}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(1/6)` | $\left(a + b x\right)^{\frac{3}{2}} \sqrt[6]{c + d x}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)**(1/6)` | $\sqrt{a + b x} \sqrt[6]{c + d x}$ |
| partial | parametric | `(c + d*x)**(1/6)/sqrt(a + b*x)` | $\frac{\sqrt[6]{c + d x}}{\sqrt{a + b x}}$ |
| partial | parametric | `(c + d*x)**(1/6)/(a + b*x)**(3/2)` | $\frac{\sqrt[6]{c + d x}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x)**(1/6)/(a + b*x)**(5/2)` | $\frac{\sqrt[6]{c + d x}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(5/6)` | $\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{6}}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)**(5/6)` | $\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{6}}$ |
| partial | parametric | `(c + d*x)**(5/6)/sqrt(a + b*x)` | $\frac{\left(c + d x\right)^{\frac{5}{6}}}{\sqrt{a + b x}}$ |
| partial | parametric | `(c + d*x)**(5/6)/(a + b*x)**(3/2)` | $\frac{\left(c + d x\right)^{\frac{5}{6}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x)**(5/6)/(a + b*x)**(5/2)` | $\frac{\left(c + d x\right)^{\frac{5}{6}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d*x)**(5/6)/(a + b*x)**(7/2)` | $\frac{\left(c + d x\right)^{\frac{5}{6}}}{\left(a + b x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x)**(5/2)/(c + d*x)**(1/6)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\sqrt[6]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(1/6)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\sqrt[6]{c + d x}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(1/6)` | $\frac{\sqrt{a + b x}}{\sqrt[6]{c + d x}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(1/6))` | $\frac{1}{\sqrt{a + b x} \sqrt[6]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(1/6))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \sqrt[6]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(1/6))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \sqrt[6]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(5/2)/(c + d*x)**(5/6)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(5/6)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(5/6)` | $\frac{\sqrt{a + b x}}{\left(c + d x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(5/6))` | $\frac{1}{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(5/6))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(5/6))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `(a + b*x)**(5/2)/(c + d*x)**(7/6)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(7/6)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(7/6)` | $\frac{\sqrt{a + b x}}{\left(c + d x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(7/6))` | $\frac{1}{\sqrt{a + b x} \left(c + d x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(7/6))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(7/6))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `(a + b*x)**(1/6)*(c + d*x)**(13/6)` | $\sqrt[6]{a + b x} \left(c + d x\right)^{\frac{13}{6}}$ |
| partial | parametric | `(a + b*x)**(1/6)*(c + d*x)**(7/6)` | $\sqrt[6]{a + b x} \left(c + d x\right)^{\frac{7}{6}}$ |
| partial | parametric | `(a + b*x)**(1/6)*(c + d*x)**(1/6)` | $\sqrt[6]{a + b x} \sqrt[6]{c + d x}$ |
| partial | parametric | `(a + b*x)**(1/6)/(c + d*x)**(5/6)` | $\frac{\sqrt[6]{a + b x}}{\left(c + d x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `(a + b*x)**(1/6)/(c + d*x)**(11/6)` | $\frac{\sqrt[6]{a + b x}}{\left(c + d x\right)^{\frac{11}{6}}}$ |
| partial | parametric | `(a + b*x)**(1/6)/(c + d*x)**(17/6)` | $\frac{\sqrt[6]{a + b x}}{\left(c + d x\right)^{\frac{17}{6}}}$ |
| partial | parametric | `(a + b*x)**(1/6)*(c + d*x)**(5/6)` | $\sqrt[6]{a + b x} \left(c + d x\right)^{\frac{5}{6}}$ |
| partial | parametric | `(a + b*x)**(1/6)/(c + d*x)**(1/6)` | $\frac{\sqrt[6]{a + b x}}{\sqrt[6]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(1/6)/(c + d*x)**(7/6)` | $\frac{\sqrt[6]{a + b x}}{\left(c + d x\right)^{\frac{7}{6}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)**(1/6)/(c + d*x)**(13/6)` | $\frac{\sqrt[6]{a + b x}}{\left(c + d x\right)^{\frac{13}{6}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)**(1/6)/(c + d*x)**(19/6)` | $\frac{\sqrt[6]{a + b x}}{\left(c + d x\right)^{\frac{19}{6}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)**(1/6)/(c + d*x)**(25/6)` | $\frac{\sqrt[6]{a + b x}}{\left(c + d x\right)^{\frac{25}{6}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)**(1/6)/(c + d*x)**(31/6)` | $\frac{\sqrt[6]{a + b x}}{\left(c + d x\right)^{\frac{31}{6}}}$ |
| partial | parametric | `(a + b*x)**(5/6)*(c + d*x)**(1/6)` | $\left(a + b x\right)^{\frac{5}{6}} \sqrt[6]{c + d x}$ |
| partial | parametric | `(a + b*x)**(5/6)/(c + d*x)**(5/6)` | $\frac{\left(a + b x\right)^{\frac{5}{6}}}{\left(c + d x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `(a + b*x)**(5/6)/(c + d*x)**(11/6)` | $\frac{\left(a + b x\right)^{\frac{5}{6}}}{\left(c + d x\right)^{\frac{11}{6}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)**(5/6)/(c + d*x)**(17/6)` | $\frac{\left(a + b x\right)^{\frac{5}{6}}}{\left(c + d x\right)^{\frac{17}{6}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)**(5/6)/(c + d*x)**(23/6)` | $\frac{\left(a + b x\right)^{\frac{5}{6}}}{\left(c + d x\right)^{\frac{23}{6}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)**(5/6)/(c + d*x)**(29/6)` | $\frac{\left(a + b x\right)^{\frac{5}{6}}}{\left(c + d x\right)^{\frac{29}{6}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)**(5/6)/(c + d*x)**(35/6)` | $\frac{\left(a + b x\right)^{\frac{5}{6}}}{\left(c + d x\right)^{\frac{35}{6}}}$ |
| partial | parametric | `(a + b*x)**(5/6)*(c + d*x)**(11/6)` | $\left(a + b x\right)^{\frac{5}{6}} \left(c + d x\right)^{\frac{11}{6}}$ |
| partial | parametric | `(a + b*x)**(5/6)*(c + d*x)**(5/6)` | $\left(a + b x\right)^{\frac{5}{6}} \left(c + d x\right)^{\frac{5}{6}}$ |
| partial | parametric | `(a + b*x)**(5/6)/(c + d*x)**(1/6)` | $\frac{\left(a + b x\right)^{\frac{5}{6}}}{\sqrt[6]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(5/6)/(c + d*x)**(7/6)` | $\frac{\left(a + b x\right)^{\frac{5}{6}}}{\left(c + d x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `(a + b*x)**(5/6)/(c + d*x)**(13/6)` | $\frac{\left(a + b x\right)^{\frac{5}{6}}}{\left(c + d x\right)^{\frac{13}{6}}}$ |
| partial | parametric | `(a + b*x)**(5/6)/(c + d*x)**(19/6)` | $\frac{\left(a + b x\right)^{\frac{5}{6}}}{\left(c + d x\right)^{\frac{19}{6}}}$ |
| partial | parametric | `(a + b*x)**(7/6)*(c + d*x)**(13/6)` | $\left(a + b x\right)^{\frac{7}{6}} \left(c + d x\right)^{\frac{13}{6}}$ |
| partial | parametric | `(a + b*x)**(7/6)*(c + d*x)**(7/6)` | $\left(a + b x\right)^{\frac{7}{6}} \left(c + d x\right)^{\frac{7}{6}}$ |
| partial | parametric | `(a + b*x)**(7/6)*(c + d*x)**(1/6)` | $\left(a + b x\right)^{\frac{7}{6}} \sqrt[6]{c + d x}$ |
| partial | parametric | `(a + b*x)**(7/6)/(c + d*x)**(5/6)` | $\frac{\left(a + b x\right)^{\frac{7}{6}}}{\left(c + d x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `(a + b*x)**(7/6)/(c + d*x)**(11/6)` | $\frac{\left(a + b x\right)^{\frac{7}{6}}}{\left(c + d x\right)^{\frac{11}{6}}}$ |
| partial | parametric | `(a + b*x)**(7/6)/(c + d*x)**(17/6)` | $\frac{\left(a + b x\right)^{\frac{7}{6}}}{\left(c + d x\right)^{\frac{17}{6}}}$ |
| partial | parametric | `(a + b*x)**(7/6)/(c + d*x)**(1/6)` | $\frac{\left(a + b x\right)^{\frac{7}{6}}}{\sqrt[6]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(7/6)/(c + d*x)**(7/6)` | $\frac{\left(a + b x\right)^{\frac{7}{6}}}{\left(c + d x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `(a + b*x)**(7/6)/(c + d*x)**(13/6)` | $\frac{\left(a + b x\right)^{\frac{7}{6}}}{\left(c + d x\right)^{\frac{13}{6}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)**(7/6)/(c + d*x)**(19/6)` | $\frac{\left(a + b x\right)^{\frac{7}{6}}}{\left(c + d x\right)^{\frac{19}{6}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)**(7/6)/(c + d*x)**(25/6)` | $\frac{\left(a + b x\right)^{\frac{7}{6}}}{\left(c + d x\right)^{\frac{25}{6}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)**(7/6)/(c + d*x)**(31/6)` | $\frac{\left(a + b x\right)^{\frac{7}{6}}}{\left(c + d x\right)^{\frac{31}{6}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)**(7/6)/(c + d*x)**(37/6)` | $\frac{\left(a + b x\right)^{\frac{7}{6}}}{\left(c + d x\right)^{\frac{37}{6}}}$ |
| partial | parametric | `(c + d*x)**(7/6)/(a + b*x)**(1/6)` | $\frac{\left(c + d x\right)^{\frac{7}{6}}}{\sqrt[6]{a + b x}}$ |
| partial | parametric | `(c + d*x)**(1/6)/(a + b*x)**(1/6)` | $\frac{\sqrt[6]{c + d x}}{\sqrt[6]{a + b x}}$ |
| partial | parametric | `1/((a + b*x)**(1/6)*(c + d*x)**(5/6))` | $\frac{1}{\sqrt[6]{a + b x} \left(c + d x\right)^{\frac{5}{6}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(1/6)*(c + d*x)**(11/6))` | $\frac{1}{\sqrt[6]{a + b x} \left(c + d x\right)^{\frac{11}{6}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(1/6)*(c + d*x)**(17/6))` | $\frac{1}{\sqrt[6]{a + b x} \left(c + d x\right)^{\frac{17}{6}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(1/6)*(c + d*x)**(23/6))` | $\frac{1}{\sqrt[6]{a + b x} \left(c + d x\right)^{\frac{23}{6}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(1/6)*(c + d*x)**(29/6))` | $\frac{1}{\sqrt[6]{a + b x} \left(c + d x\right)^{\frac{29}{6}}}$ |
| partial | parametric | `(c + d*x)**(11/6)/(a + b*x)**(1/6)` | $\frac{\left(c + d x\right)^{\frac{11}{6}}}{\sqrt[6]{a + b x}}$ |
| partial | parametric | `(c + d*x)**(5/6)/(a + b*x)**(1/6)` | $\frac{\left(c + d x\right)^{\frac{5}{6}}}{\sqrt[6]{a + b x}}$ |
| partial | parametric | `1/((a + b*x)**(1/6)*(c + d*x)**(1/6))` | $\frac{1}{\sqrt[6]{a + b x} \sqrt[6]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(1/6)*(c + d*x)**(7/6))` | $\frac{1}{\sqrt[6]{a + b x} \left(c + d x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(1/6)*(c + d*x)**(13/6))` | $\frac{1}{\sqrt[6]{a + b x} \left(c + d x\right)^{\frac{13}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(1/6)*(c + d*x)**(19/6))` | $\frac{1}{\sqrt[6]{a + b x} \left(c + d x\right)^{\frac{19}{6}}}$ |
| partial | parametric | `(c + d*x)**(13/6)/(a + b*x)**(5/6)` | $\frac{\left(c + d x\right)^{\frac{13}{6}}}{\left(a + b x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `(c + d*x)**(7/6)/(a + b*x)**(5/6)` | $\frac{\left(c + d x\right)^{\frac{7}{6}}}{\left(a + b x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `(c + d*x)**(1/6)/(a + b*x)**(5/6)` | $\frac{\sqrt[6]{c + d x}}{\left(a + b x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(5/6)*(c + d*x)**(5/6))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{6}} \left(c + d x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(5/6)*(c + d*x)**(11/6))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{6}} \left(c + d x\right)^{\frac{11}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(5/6)*(c + d*x)**(17/6))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{6}} \left(c + d x\right)^{\frac{17}{6}}}$ |
| partial | parametric | `(c + d*x)**(11/6)/(a + b*x)**(5/6)` | $\frac{\left(c + d x\right)^{\frac{11}{6}}}{\left(a + b x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `(c + d*x)**(5/6)/(a + b*x)**(5/6)` | $\frac{\left(c + d x\right)^{\frac{5}{6}}}{\left(a + b x\right)^{\frac{5}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(5/6)*(c + d*x)**(1/6))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{6}} \sqrt[6]{c + d x}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(5/6)*(c + d*x)**(7/6))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{6}} \left(c + d x\right)^{\frac{7}{6}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(5/6)*(c + d*x)**(13/6))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{6}} \left(c + d x\right)^{\frac{13}{6}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(5/6)*(c + d*x)**(19/6))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{6}} \left(c + d x\right)^{\frac{19}{6}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(5/6)*(c + d*x)**(25/6))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{6}} \left(c + d x\right)^{\frac{25}{6}}}$ |
| partial | parametric | `(c + d*x)**(13/6)/(a + b*x)**(7/6)` | $\frac{\left(c + d x\right)^{\frac{13}{6}}}{\left(a + b x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `(c + d*x)**(7/6)/(a + b*x)**(7/6)` | $\frac{\left(c + d x\right)^{\frac{7}{6}}}{\left(a + b x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `(c + d*x)**(1/6)/(a + b*x)**(7/6)` | $\frac{\sqrt[6]{c + d x}}{\left(a + b x\right)^{\frac{7}{6}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(7/6)*(c + d*x)**(5/6))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{6}} \left(c + d x\right)^{\frac{5}{6}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(7/6)*(c + d*x)**(11/6))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{6}} \left(c + d x\right)^{\frac{11}{6}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(7/6)*(c + d*x)**(17/6))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{6}} \left(c + d x\right)^{\frac{17}{6}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(7/6)*(c + d*x)**(23/6))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{6}} \left(c + d x\right)^{\frac{23}{6}}}$ |
| partial | parametric | `(c + d*x)**(11/6)/(a + b*x)**(7/6)` | $\frac{\left(c + d x\right)^{\frac{11}{6}}}{\left(a + b x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `(c + d*x)**(5/6)/(a + b*x)**(7/6)` | $\frac{\left(c + d x\right)^{\frac{5}{6}}}{\left(a + b x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(7/6)*(c + d*x)**(1/6))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{6}} \sqrt[6]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(7/6)*(c + d*x)**(7/6))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{6}} \left(c + d x\right)^{\frac{7}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(7/6)*(c + d*x)**(13/6))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{6}} \left(c + d x\right)^{\frac{13}{6}}}$ |
| partial | parametric | `1/((a + b*x)**(7/6)*(c + d*x)**(19/6))` | $\frac{1}{\left(a + b x\right)^{\frac{7}{6}} \left(c + d x\right)^{\frac{19}{6}}}$ |
| SOLVED-both | concrete | `x**(5/6) - x**3` | $x^{\frac{5}{6}} - x^{3}$ |
| SOLVED-both | concrete | `x**(1/33) + 33` | $\sqrt[33]{x} + 33$ |
| partial | concrete | `2*sqrt(x) + 1/(2*sqrt(x))` | $2 \sqrt{x} + \frac{1}{2 \sqrt{x}}$ |
| SOLVED-both | concrete | `6*sqrt(x) + 10/x - 1/x**2` | $6 \sqrt{x} + \frac{10}{x} - \frac{1}{x^{2}}$ |
| partial | concrete | `x**(3/2) + x**(-3/2)` | $x^{\frac{3}{2}} + \frac{1}{x^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `7*x**(5/2) - 5*x**(3/2)` | $7 x^{\frac{5}{2}} - 5 x^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(x) - x/2 + 2/sqrt(x)` | $\sqrt{x} - \frac{x}{2} + \frac{2}{\sqrt{x}}$ |
| SOLVED-both | concrete | `x**(3/2) + sqrt(x)/5 - 2/x` | $x^{\frac{3}{2}} + \frac{\sqrt{x}}{5} - \frac{2}{x}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(a + b*x)` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a + b x\right)$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(a + b*x)` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a + b x\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(a + b*x)` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a + b x\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(a + b*x)` | $\sqrt{x} \left(A + B x\right) \left(a + b x\right)$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)/sqrt(x)` | $\frac{\left(A + B x\right) \left(a + b x\right)}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)/x**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)/x**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)/x**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(a + b*x)**2` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(a + b*x)**2` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(a + b*x)**2` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(a + b*x)**2` | $\sqrt{x} \left(A + B x\right) \left(a + b x\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**2/sqrt(x)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**2/x**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**2/x**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**2/x**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(a + b*x)**3` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a + b x\right)^{3}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(a + b*x)**3` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a + b x\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(a + b*x)**3` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a + b x\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(a + b*x)**3` | $\sqrt{x} \left(A + B x\right) \left(a + b x\right)^{3}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**3/sqrt(x)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**3/x**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**3/x**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**3/x**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{3}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(a + b*x)` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{a + b x}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a + b*x)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{a + b x}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a + b*x)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{a + b x}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a + b*x)` | $\frac{\sqrt{x} \left(A + B x\right)}{a + b x}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a + b*x))` | $\frac{A + B x}{\sqrt{x} \left(a + b x\right)}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a + b*x))` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a + b x\right)}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(a + b*x))` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a + b x\right)}$ |
| partial | parametric | `(A + B*x)/(x**(7/2)*(a + b*x))` | $\frac{A + B x}{x^{\frac{7}{2}} \left(a + b x\right)}$ |
| partial | parametric | `(A + B*x)/(x**(9/2)*(a + b*x))` | $\frac{A + B x}{x^{\frac{9}{2}} \left(a + b x\right)}$ |
| partial | parametric | `(A + B*x)/(x**(11/2)*(a + b*x))` | $\frac{A + B x}{x^{\frac{11}{2}} \left(a + b x\right)}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(a + b*x)**2` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a + b*x)**2` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a + b*x)**2` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a + b*x)**2` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a + b*x)**2)` | $\frac{A + B x}{\sqrt{x} \left(a + b x\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a + b*x)**2)` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(a + b*x)**2)` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(x**(7/2)*(a + b*x)**2)` | $\frac{A + B x}{x^{\frac{7}{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(x**(9/2)*(a + b*x)**2)` | $\frac{A + B x}{x^{\frac{9}{2}} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(a + b*x)**3` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a + b*x)**3` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a + b*x)**3` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a + b*x)**3` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a + b*x)**3)` | $\frac{A + B x}{\sqrt{x} \left(a + b x\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a + b*x)**3)` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a + b x\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(a + b*x)**3)` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a + b x\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(x**(7/2)*(a + b*x)**3)` | $\frac{A + B x}{x^{\frac{7}{2}} \left(a + b x\right)^{3}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x)*sqrt(a + b*x)` | $x^{4} \left(A + B x\right) \sqrt{a + b x}$ |
| SOLVED-both | parametric | `x**3*(A + B*x)*sqrt(a + b*x)` | $x^{3} \left(A + B x\right) \sqrt{a + b x}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)*sqrt(a + b*x)` | $x^{2} \left(A + B x\right) \sqrt{a + b x}$ |
| SOLVED-both | parametric | `x*(A + B*x)*sqrt(a + b*x)` | $x \left(A + B x\right) \sqrt{a + b x}$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(a + b*x)` | $\left(A + B x\right) \sqrt{a + b x}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)/x` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)/x**2` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)/x**3` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)/x**4` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)/x**5` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x^{5}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)/x**6` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x^{6}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x)*(a + b*x)**(3/2)` | $x^{4} \left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x)*(a + b*x)**(3/2)` | $x^{3} \left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)*(a + b*x)**(3/2)` | $x^{2} \left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x*(A + B*x)*(a + b*x)**(3/2)` | $x \left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**(3/2)` | $\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/x` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**2` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**3` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**4` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**5` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**6` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**7` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{7}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x)*(a + b*x)**(5/2)` | $x^{4} \left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x)*(a + b*x)**(5/2)` | $x^{3} \left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)*(a + b*x)**(5/2)` | $x^{2} \left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x*(A + B*x)*(a + b*x)**(5/2)` | $x \left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**(5/2)` | $\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/x` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**2` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**3` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**4` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**5` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**6` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**7` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{7}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**8` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{8}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x)/sqrt(a + b*x)` | $\frac{x^{4} \left(A + B x\right)}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x)/sqrt(a + b*x)` | $\frac{x^{3} \left(A + B x\right)}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)/sqrt(a + b*x)` | $\frac{x^{2} \left(A + B x\right)}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `x*(A + B*x)/sqrt(a + b*x)` | $\frac{x \left(A + B x\right)}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `(A + B*x)/sqrt(a + b*x)` | $\frac{A + B x}{\sqrt{a + b x}}$ |
| partial | parametric | `(A + B*x)/(x*sqrt(a + b*x))` | $\frac{A + B x}{x \sqrt{a + b x}}$ |
| partial | parametric | `(A + B*x)/(x**2*sqrt(a + b*x))` | $\frac{A + B x}{x^{2} \sqrt{a + b x}}$ |
| partial | parametric | `(A + B*x)/(x**3*sqrt(a + b*x))` | $\frac{A + B x}{x^{3} \sqrt{a + b x}}$ |
| partial | parametric | `(A + B*x)/(x**4*sqrt(a + b*x))` | $\frac{A + B x}{x^{4} \sqrt{a + b x}}$ |
| partial | parametric | `(A + B*x)/(x**5*sqrt(a + b*x))` | $\frac{A + B x}{x^{5} \sqrt{a + b x}}$ |
| partial | parametric | `(A + B*x)/(x**6*sqrt(a + b*x))` | $\frac{A + B x}{x^{6} \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x)/(a + b*x)**(3/2)` | $\frac{x^{4} \left(A + B x\right)}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x)/(a + b*x)**(3/2)` | $\frac{x^{3} \left(A + B x\right)}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)/(a + b*x)**(3/2)` | $\frac{x^{2} \left(A + B x\right)}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x)/(a + b*x)**(3/2)` | $\frac{x \left(A + B x\right)}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a + b*x)**(3/2)` | $\frac{A + B x}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x*(a + b*x)**(3/2))` | $\frac{A + B x}{x \left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*(a + b*x)**(3/2))` | $\frac{A + B x}{x^{2} \left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*(a + b*x)**(3/2))` | $\frac{A + B x}{x^{3} \left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**4*(a + b*x)**(3/2))` | $\frac{A + B x}{x^{4} \left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**5*(a + b*x)**(3/2))` | $\frac{A + B x}{x^{5} \left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x)/(a + b*x)**(5/2)` | $\frac{x^{4} \left(A + B x\right)}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x)/(a + b*x)**(5/2)` | $\frac{x^{3} \left(A + B x\right)}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)/(a + b*x)**(5/2)` | $\frac{x^{2} \left(A + B x\right)}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x)/(a + b*x)**(5/2)` | $\frac{x \left(A + B x\right)}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a + b*x)**(5/2)` | $\frac{A + B x}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x*(a + b*x)**(5/2))` | $\frac{A + B x}{x \left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*(a + b*x)**(5/2))` | $\frac{A + B x}{x^{2} \left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*(a + b*x)**(5/2))` | $\frac{A + B x}{x^{3} \left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**4*(a + b*x)**(5/2))` | $\frac{A + B x}{x^{4} \left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**5*(a + b*x)**(5/2))` | $\frac{A + B x}{x^{5} \left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)**2/(x**2*sqrt(c + d*x))` | $\frac{\left(a + b x\right)^{2}}{x^{2} \sqrt{c + d x}}$ |
| partial | parametric | `x**3*(c + d*x)**(5/2)/(a + b*x)` | $\frac{x^{3} \left(c + d x\right)^{\frac{5}{2}}}{a + b x}$ |
| partial | parametric | `x**2*(c + d*x)**(5/2)/(a + b*x)` | $\frac{x^{2} \left(c + d x\right)^{\frac{5}{2}}}{a + b x}$ |
| partial | parametric | `x*(c + d*x)**(5/2)/(a + b*x)` | $\frac{x \left(c + d x\right)^{\frac{5}{2}}}{a + b x}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{a + b x}$ |
| partial | parametric | `(c + d*x)**(5/2)/(x*(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x \left(a + b x\right)}$ |
| partial | parametric | `(c + d*x)**(5/2)/(x**2*(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{2} \left(a + b x\right)}$ |
| partial | parametric | `(c + d*x)**(5/2)/(x**3*(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{3} \left(a + b x\right)}$ |
| partial | parametric | `(c + d*x)**(5/2)/(x**4*(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{4} \left(a + b x\right)}$ |
| partial | parametric | `1/(x**(1/3)*sqrt(c + d*x)*(4*c + d*x))` | $\frac{1}{\sqrt[3]{x} \sqrt{c + d x} \left(4 c + d x\right)}$ |
| partial | parametric | `1/(x**(1/3)*sqrt(c + d*x)*(8*c - d*x))` | $\frac{1}{\sqrt[3]{x} \sqrt{c + d x} \left(8 c - d x\right)}$ |
| partial | parametric | `sqrt(c + d*x)/(x**2*(a + b*x)**2)` | $\frac{\sqrt{c + d x}}{x^{2} \left(a + b x\right)^{2}}$ |
| partial | parametric | `(c + d*x)**(3/2)/(x*(a + b*x)**2)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{x \left(a + b x\right)^{2}}$ |
| partial | parametric | `(c + d*x)**(3/2)/(x**2*(a + b*x)**2)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{x^{2} \left(a + b x\right)^{2}}$ |
| partial | parametric | `x**3*(c + d*x)**(5/2)/(a + b*x)**2` | $\frac{x^{3} \left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `x**2*(c + d*x)**(5/2)/(a + b*x)**2` | $\frac{x^{2} \left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `x*(c + d*x)**(5/2)/(a + b*x)**2` | $\frac{x \left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)**2` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(x*(a + b*x)**2)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x \left(a + b x\right)^{2}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(x**3*(a + b*x)**2)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{3} \left(a + b x\right)^{2}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(x**4*(a + b*x)**2)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{4} \left(a + b x\right)^{2}}$ |
| partial | parametric | `1/(x**2*(a + b*x)**2*sqrt(c + d*x))` | $\frac{1}{x^{2} \left(a + b x\right)^{2} \sqrt{c + d x}}$ |
| partial | parametric | `1/(x**2*(a + b*x)**2*(c + d*x)**(3/2))` | $\frac{1}{x^{2} \left(a + b x\right)^{2} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x)**2*(c + d*x)**(5/2))` | $\frac{1}{x^{2} \left(a + b x\right)^{2} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)*sqrt(a + b*x)` | $x^{\frac{5}{2}} \left(A + B x\right) \sqrt{a + b x}$ |
| partial | parametric | `x**(3/2)*(A + B*x)*sqrt(a + b*x)` | $x^{\frac{3}{2}} \left(A + B x\right) \sqrt{a + b x}$ |
| partial | parametric | `sqrt(x)*(A + B*x)*sqrt(a + b*x)` | $\sqrt{x} \left(A + B x\right) \sqrt{a + b x}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)/sqrt(x)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{\sqrt{x}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)/x**(3/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)/x**(5/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(a + b*x)/x**(7/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(a + b*x)/x**(9/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(a + b*x)/x**(11/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x^{\frac{11}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(a + b*x)/x**(13/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x^{\frac{13}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(a + b*x)/x**(15/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{x^{\frac{15}{2}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)*(a + b*x)**(3/2)` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)*(a + b*x)**(3/2)` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)*(a + b*x)**(3/2)` | $\sqrt{x} \left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/sqrt(x)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**(9/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**(11/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{\frac{11}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**(13/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{\frac{13}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**(15/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{\frac{15}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**(3/2)/x**(17/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{x^{\frac{17}{2}}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)*(a + b*x)**(5/2)` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)*(a + b*x)**(5/2)` | $\sqrt{x} \left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/sqrt(x)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**(9/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**(11/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{\frac{11}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**(13/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{\frac{13}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**(15/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{\frac{15}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**(17/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{\frac{17}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**(5/2)/x**(19/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{x^{\frac{19}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/sqrt(a + b*x)` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\sqrt{a + b x}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/sqrt(a + b*x)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\sqrt{a + b x}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/sqrt(a + b*x)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\sqrt{a + b x}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/sqrt(a + b*x)` | $\frac{\sqrt{x} \left(A + B x\right)}{\sqrt{a + b x}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*sqrt(a + b*x))` | $\frac{A + B x}{\sqrt{x} \sqrt{a + b x}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*sqrt(a + b*x))` | $\frac{A + B x}{x^{\frac{3}{2}} \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(5/2)*sqrt(a + b*x))` | $\frac{A + B x}{x^{\frac{5}{2}} \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(7/2)*sqrt(a + b*x))` | $\frac{A + B x}{x^{\frac{7}{2}} \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(9/2)*sqrt(a + b*x))` | $\frac{A + B x}{x^{\frac{9}{2}} \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(11/2)*sqrt(a + b*x))` | $\frac{A + B x}{x^{\frac{11}{2}} \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(13/2)*sqrt(a + b*x))` | $\frac{A + B x}{x^{\frac{13}{2}} \sqrt{a + b x}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(15/2)*sqrt(a + b*x))` | $\frac{A + B x}{x^{\frac{15}{2}} \sqrt{a + b x}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(a + b*x)**(3/2)` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a + b*x)**(3/2)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a + b*x)**(3/2)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a + b*x)**(3/2)` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a + b*x)**(3/2))` | $\frac{A + B x}{\sqrt{x} \left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(3/2)*(a + b*x)**(3/2))` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(5/2)*(a + b*x)**(3/2))` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(7/2)*(a + b*x)**(3/2))` | $\frac{A + B x}{x^{\frac{7}{2}} \left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(9/2)*(a + b*x)**(3/2))` | $\frac{A + B x}{x^{\frac{9}{2}} \left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(11/2)*(a + b*x)**(3/2))` | $\frac{A + B x}{x^{\frac{11}{2}} \left(a + b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(13/2)*(a + b*x)**(3/2))` | $\frac{A + B x}{x^{\frac{13}{2}} \left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(a + b*x)**(5/2)` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a + b*x)**(5/2)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a + b*x)**(5/2)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a + b*x)**(5/2)` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(sqrt(x)*(a + b*x)**(5/2))` | $\frac{A + B x}{\sqrt{x} \left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(3/2)*(a + b*x)**(5/2))` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(5/2)*(a + b*x)**(5/2))` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(7/2)*(a + b*x)**(5/2))` | $\frac{A + B x}{x^{\frac{7}{2}} \left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(9/2)*(a + b*x)**(5/2))` | $\frac{A + B x}{x^{\frac{9}{2}} \left(a + b x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(x**(11/2)*(a + b*x)**(5/2))` | $\frac{A + B x}{x^{\frac{11}{2}} \left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3*sqrt(a + b*x)*sqrt(c + d*x)` | $x^{3} \sqrt{a + b x} \sqrt{c + d x}$ |
| partial | parametric | `x**2*sqrt(a + b*x)*sqrt(c + d*x)` | $x^{2} \sqrt{a + b x} \sqrt{c + d x}$ |
| partial | parametric | `x*sqrt(a + b*x)*sqrt(c + d*x)` | $x \sqrt{a + b x} \sqrt{c + d x}$ |
| partial | parametric | `sqrt(a + b*x)*sqrt(c + d*x)` | $\sqrt{a + b x} \sqrt{c + d x}$ |
| partial | parametric | `sqrt(a + b*x)*sqrt(c + d*x)/x` | $\frac{\sqrt{a + b x} \sqrt{c + d x}}{x}$ |
| partial | parametric | `sqrt(a + b*x)*sqrt(c + d*x)/x**2` | $\frac{\sqrt{a + b x} \sqrt{c + d x}}{x^{2}}$ |
| partial | parametric | `sqrt(a + b*x)*sqrt(c + d*x)/x**3` | $\frac{\sqrt{a + b x} \sqrt{c + d x}}{x^{3}}$ |
| partial | parametric | `sqrt(a + b*x)*sqrt(c + d*x)/x**4` | $\frac{\sqrt{a + b x} \sqrt{c + d x}}{x^{4}}$ |
| partial | parametric | `sqrt(a + b*x)*sqrt(c + d*x)/x**5` | $\frac{\sqrt{a + b x} \sqrt{c + d x}}{x^{5}}$ |
| timeout | parametric | `sqrt(a + b*x)*sqrt(c + d*x)/x**6` | $\frac{\sqrt{a + b x} \sqrt{c + d x}}{x^{6}}$ |
| partial | parametric | `x**2*sqrt(a + b*x)*(c + d*x)**(3/2)` | $x^{2} \sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*sqrt(a + b*x)*(c + d*x)**(3/2)` | $x \sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)**(3/2)` | $\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(3/2)/x` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}{x}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(3/2)/x**2` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}{x^{2}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(3/2)/x**3` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}{x^{3}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(3/2)/x**4` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}{x^{4}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(3/2)/x**5` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}{x^{5}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(3/2)/x**6` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `x**2*sqrt(a + b*x)*(c + d*x)**(5/2)` | $x^{2} \sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}$ |
| partial | parametric | `x*sqrt(a + b*x)*(c + d*x)**(5/2)` | $x \sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)**(5/2)` | $\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(5/2)/x` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}{x}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(5/2)/x**2` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}{x^{2}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(5/2)/x**3` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}{x^{3}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(5/2)/x**4` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}{x^{4}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(5/2)/x**5` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}{x^{5}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(5/2)/x**6` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}{x^{6}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(5/2)/x**7` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}{x^{7}}$ |
| partial | parametric | `x**3*sqrt(a + b*x)/sqrt(c + d*x)` | $\frac{x^{3} \sqrt{a + b x}}{\sqrt{c + d x}}$ |
| partial | parametric | `x**2*sqrt(a + b*x)/sqrt(c + d*x)` | $\frac{x^{2} \sqrt{a + b x}}{\sqrt{c + d x}}$ |
| partial | parametric | `x*sqrt(a + b*x)/sqrt(c + d*x)` | $\frac{x \sqrt{a + b x}}{\sqrt{c + d x}}$ |
| partial | parametric | `sqrt(a + b*x)/sqrt(c + d*x)` | $\frac{\sqrt{a + b x}}{\sqrt{c + d x}}$ |
| timeout | parametric | `sqrt(a + b*x)/(x*sqrt(c + d*x))` | $\frac{\sqrt{a + b x}}{x \sqrt{c + d x}}$ |
| timeout | parametric | `sqrt(a + b*x)/(x**2*sqrt(c + d*x))` | $\frac{\sqrt{a + b x}}{x^{2} \sqrt{c + d x}}$ |
| timeout | parametric | `sqrt(a + b*x)/(x**3*sqrt(c + d*x))` | $\frac{\sqrt{a + b x}}{x^{3} \sqrt{c + d x}}$ |
| timeout | parametric | `sqrt(a + b*x)/(x**4*sqrt(c + d*x))` | $\frac{\sqrt{a + b x}}{x^{4} \sqrt{c + d x}}$ |
| timeout | parametric | `sqrt(a + b*x)/(x**5*sqrt(c + d*x))` | $\frac{\sqrt{a + b x}}{x^{5} \sqrt{c + d x}}$ |
| partial | parametric | `x**2*sqrt(a + b*x)/(c + d*x)**(3/2)` | $\frac{x^{2} \sqrt{a + b x}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*sqrt(a + b*x)/(c + d*x)**(3/2)` | $\frac{x \sqrt{a + b x}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*x)/(c + d*x)**(3/2)` | $\frac{\sqrt{a + b x}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(a + b*x)/(x*(c + d*x)**(3/2))` | $\frac{\sqrt{a + b x}}{x \left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(a + b*x)/(x**2*(c + d*x)**(3/2))` | $\frac{\sqrt{a + b x}}{x^{2} \left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(a + b*x)/(x**3*(c + d*x)**(3/2))` | $\frac{\sqrt{a + b x}}{x^{3} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*sqrt(a + b*x)/(c + d*x)**(5/2)` | $\frac{x^{3} \sqrt{a + b x}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2*sqrt(a + b*x)/(c + d*x)**(5/2)` | $\frac{x^{2} \sqrt{a + b x}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x*sqrt(a + b*x)/(c + d*x)**(5/2)` | $\frac{x \sqrt{a + b x}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a + b*x)/(c + d*x)**(5/2)` | $\frac{\sqrt{a + b x}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `sqrt(a + b*x)/(x*(c + d*x)**(5/2))` | $\frac{\sqrt{a + b x}}{x \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `sqrt(a + b*x)/(x**2*(c + d*x)**(5/2))` | $\frac{\sqrt{a + b x}}{x^{2} \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `sqrt(a + b*x)/(x**3*(c + d*x)**(5/2))` | $\frac{\sqrt{a + b x}}{x^{3} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2*(a + b*x)**(3/2)*sqrt(c + d*x)` | $x^{2} \left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x}$ |
| partial | parametric | `x*(a + b*x)**(3/2)*sqrt(c + d*x)` | $x \left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x}$ |
| partial | parametric | `(a + b*x)**(3/2)*sqrt(c + d*x)` | $\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x}$ |
| timeout | parametric | `(a + b*x)**(3/2)*sqrt(c + d*x)/x` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x}}{x}$ |
| timeout | parametric | `(a + b*x)**(3/2)*sqrt(c + d*x)/x**2` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x}}{x^{2}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*sqrt(c + d*x)/x**3` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x}}{x^{3}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*sqrt(c + d*x)/x**4` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x}}{x^{4}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*sqrt(c + d*x)/x**5` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x}}{x^{5}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*sqrt(c + d*x)/x**6` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x}}{x^{6}}$ |
| partial | parametric | `x**2*(a + b*x)**(3/2)*(c + d*x)**(3/2)` | $x^{2} \left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a + b*x)**(3/2)*(c + d*x)**(3/2)` | $x \left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(3/2)` | $\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(3/2)/x` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(3/2)/x**2` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(3/2)/x**3` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(3/2)/x**4` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(3/2)/x**5` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}{x^{5}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*(c + d*x)**(3/2)/x**6` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `x**2*(a + b*x)**(3/2)*(c + d*x)**(5/2)` | $x^{2} \left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}$ |
| partial | parametric | `x*(a + b*x)**(3/2)*(c + d*x)**(5/2)` | $x \left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x)**(3/2)*(c + d*x)**(5/2)` | $\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*(c + d*x)**(5/2)/x` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x}$ |
| timeout | parametric | `(a + b*x)**(3/2)*(c + d*x)**(5/2)/x**2` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x^{2}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*(c + d*x)**(5/2)/x**3` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x^{3}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*(c + d*x)**(5/2)/x**4` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x^{4}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*(c + d*x)**(5/2)/x**5` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x^{5}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*(c + d*x)**(5/2)/x**6` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x^{6}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*(c + d*x)**(5/2)/x**7` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x^{7}}$ |
| partial | parametric | `x**2*(a + b*x)**(3/2)/sqrt(c + d*x)` | $\frac{x^{2} \left(a + b x\right)^{\frac{3}{2}}}{\sqrt{c + d x}}$ |
| partial | parametric | `x*(a + b*x)**(3/2)/sqrt(c + d*x)` | $\frac{x \left(a + b x\right)^{\frac{3}{2}}}{\sqrt{c + d x}}$ |
| partial | parametric | `(a + b*x)**(3/2)/sqrt(c + d*x)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\sqrt{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(x*sqrt(c + d*x))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x \sqrt{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(x**2*sqrt(c + d*x))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{2} \sqrt{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(x**3*sqrt(c + d*x))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{3} \sqrt{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(x**4*sqrt(c + d*x))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{4} \sqrt{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(x**5*sqrt(c + d*x))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{5} \sqrt{c + d x}}$ |
| partial | parametric | `x**2*(a + b*x)**(3/2)/(c + d*x)**(3/2)` | $\frac{x^{2} \left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(a + b*x)**(3/2)/(c + d*x)**(3/2)` | $\frac{x \left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(3/2)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(x*(c + d*x)**(3/2))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x \left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(x**2*(c + d*x)**(3/2))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{2} \left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(x**3*(c + d*x)**(3/2))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{3} \left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(x**4*(c + d*x)**(3/2))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{4} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(a + b*x)**(3/2)/(c + d*x)**(5/2)` | $\frac{x^{2} \left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x*(a + b*x)**(3/2)/(c + d*x)**(5/2)` | $\frac{x \left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)**(3/2)/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(x*(c + d*x)**(5/2))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(x**2*(c + d*x)**(5/2))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{2} \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(x**3*(c + d*x)**(5/2))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{x^{3} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2*(a + b*x)**(5/2)*sqrt(c + d*x)` | $x^{2} \left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x}$ |
| partial | parametric | `x*(a + b*x)**(5/2)*sqrt(c + d*x)` | $x \left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x}$ |
| partial | parametric | `(a + b*x)**(5/2)*sqrt(c + d*x)` | $\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x}$ |
| timeout | parametric | `(a + b*x)**(5/2)*sqrt(c + d*x)/x` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x}}{x}$ |
| timeout | parametric | `(a + b*x)**(5/2)*sqrt(c + d*x)/x**2` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x}}{x^{2}}$ |
| timeout | parametric | `(a + b*x)**(5/2)*sqrt(c + d*x)/x**3` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x}}{x^{3}}$ |
| timeout | parametric | `(a + b*x)**(5/2)*sqrt(c + d*x)/x**4` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x}}{x^{4}}$ |
| timeout | parametric | `(a + b*x)**(5/2)*sqrt(c + d*x)/x**5` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x}}{x^{5}}$ |
| timeout | parametric | `(a + b*x)**(5/2)*sqrt(c + d*x)/x**6` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x}}{x^{6}}$ |
| partial | parametric | `x**2*(a + b*x)**(5/2)*(c + d*x)**(3/2)` | $x^{2} \left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a + b*x)**(5/2)*(c + d*x)**(3/2)` | $x \left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)**(5/2)*(c + d*x)**(3/2)` | $\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{3}{2}}$ |
| timeout | parametric | `(a + b*x)**(5/2)*(c + d*x)**(3/2)/x` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{3}{2}}}{x}$ |
| timeout | parametric | `(a + b*x)**(5/2)*(c + d*x)**(3/2)/x**2` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{3}{2}}}{x^{2}}$ |
| timeout | parametric | `(a + b*x)**(5/2)*(c + d*x)**(3/2)/x**3` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{3}{2}}}{x^{3}}$ |
| timeout | parametric | `(a + b*x)**(5/2)*(c + d*x)**(3/2)/x**4` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{3}{2}}}{x^{4}}$ |
| timeout | parametric | `(a + b*x)**(5/2)*(c + d*x)**(3/2)/x**5` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{3}{2}}}{x^{5}}$ |
| timeout | parametric | `(a + b*x)**(5/2)*(c + d*x)**(3/2)/x**6` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `x*(a + b*x)**(5/2)*(c + d*x)**(5/2)` | $x \left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x)**(5/2)*(c + d*x)**(5/2)` | $\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x)**(5/2)*(c + d*x)**(5/2)/x` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(a + b*x)**(5/2)*(c + d*x)**(5/2)/x**2` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x)**(5/2)*(c + d*x)**(5/2)/x**3` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x)**(5/2)*(c + d*x)**(5/2)/x**4` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x)**(5/2)*(c + d*x)**(5/2)/x**5` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x^{5}}$ |
| timeout | parametric | `(a + b*x)**(5/2)*(c + d*x)**(5/2)/x**6` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x^{6}}$ |
| timeout | parametric | `(a + b*x)**(5/2)*(c + d*x)**(5/2)/x**7` | $\frac{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}{x^{7}}$ |
| partial | parametric | `x**2*(a + b*x)**(5/2)/sqrt(c + d*x)` | $\frac{x^{2} \left(a + b x\right)^{\frac{5}{2}}}{\sqrt{c + d x}}$ |
| partial | parametric | `x*(a + b*x)**(5/2)/sqrt(c + d*x)` | $\frac{x \left(a + b x\right)^{\frac{5}{2}}}{\sqrt{c + d x}}$ |
| partial | parametric | `(a + b*x)**(5/2)/sqrt(c + d*x)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\sqrt{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x*sqrt(c + d*x))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x \sqrt{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x**2*sqrt(c + d*x))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{2} \sqrt{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x**3*sqrt(c + d*x))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{3} \sqrt{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x**4*sqrt(c + d*x))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{4} \sqrt{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x**5*sqrt(c + d*x))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{5} \sqrt{c + d x}}$ |
| partial | parametric | `x**2*(a + b*x)**(5/2)/(c + d*x)**(3/2)` | $\frac{x^{2} \left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(a + b*x)**(5/2)/(c + d*x)**(3/2)` | $\frac{x \left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)**(5/2)/(c + d*x)**(3/2)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x*(c + d*x)**(3/2))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x \left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x**2*(c + d*x)**(3/2))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{2} \left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x**3*(c + d*x)**(3/2))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{3} \left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x**4*(c + d*x)**(3/2))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{4} \left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x**5*(c + d*x)**(3/2))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{5} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*(a + b*x)**(5/2)/(c + d*x)**(5/2)` | $\frac{x^{3} \left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2*(a + b*x)**(5/2)/(c + d*x)**(5/2)` | $\frac{x^{2} \left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x*(a + b*x)**(5/2)/(c + d*x)**(5/2)` | $\frac{x \left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)**(5/2)/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x*(c + d*x)**(5/2))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x**2*(c + d*x)**(5/2))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{2} \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x**3*(c + d*x)**(5/2))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{3} \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x**4*(c + d*x)**(5/2))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{4} \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a + b*x)**(5/2)/(x**5*(c + d*x)**(5/2))` | $\frac{\left(a + b x\right)^{\frac{5}{2}}}{x^{5} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2*sqrt(c + d*x)/sqrt(a + b*x)` | $\frac{x^{2} \sqrt{c + d x}}{\sqrt{a + b x}}$ |
| partial | parametric | `x*sqrt(c + d*x)/sqrt(a + b*x)` | $\frac{x \sqrt{c + d x}}{\sqrt{a + b x}}$ |
| partial | parametric | `sqrt(c + d*x)/sqrt(a + b*x)` | $\frac{\sqrt{c + d x}}{\sqrt{a + b x}}$ |
| timeout | parametric | `sqrt(c + d*x)/(x*sqrt(a + b*x))` | $\frac{\sqrt{c + d x}}{x \sqrt{a + b x}}$ |
| timeout | parametric | `sqrt(c + d*x)/(x**2*sqrt(a + b*x))` | $\frac{\sqrt{c + d x}}{x^{2} \sqrt{a + b x}}$ |
| timeout | parametric | `sqrt(c + d*x)/(x**3*sqrt(a + b*x))` | $\frac{\sqrt{c + d x}}{x^{3} \sqrt{a + b x}}$ |
| timeout | parametric | `sqrt(c + d*x)/(x**4*sqrt(a + b*x))` | $\frac{\sqrt{c + d x}}{x^{4} \sqrt{a + b x}}$ |
| partial | parametric | `x**2*(c + d*x)**(3/2)/sqrt(a + b*x)` | $\frac{x^{2} \left(c + d x\right)^{\frac{3}{2}}}{\sqrt{a + b x}}$ |
| partial | parametric | `x*(c + d*x)**(3/2)/sqrt(a + b*x)` | $\frac{x \left(c + d x\right)^{\frac{3}{2}}}{\sqrt{a + b x}}$ |
| partial | parametric | `(c + d*x)**(3/2)/sqrt(a + b*x)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\sqrt{a + b x}}$ |
| timeout | parametric | `(c + d*x)**(3/2)/(x*sqrt(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{x \sqrt{a + b x}}$ |
| timeout | parametric | `(c + d*x)**(3/2)/(x**2*sqrt(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{x^{2} \sqrt{a + b x}}$ |
| timeout | parametric | `(c + d*x)**(3/2)/(x**3*sqrt(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{x^{3} \sqrt{a + b x}}$ |
| timeout | parametric | `(c + d*x)**(3/2)/(x**4*sqrt(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{x^{4} \sqrt{a + b x}}$ |
| timeout | parametric | `(c + d*x)**(3/2)/(x**5*sqrt(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{x^{5} \sqrt{a + b x}}$ |
| partial | parametric | `x**2*(c + d*x)**(5/2)/sqrt(a + b*x)` | $\frac{x^{2} \left(c + d x\right)^{\frac{5}{2}}}{\sqrt{a + b x}}$ |
| partial | parametric | `x*(c + d*x)**(5/2)/sqrt(a + b*x)` | $\frac{x \left(c + d x\right)^{\frac{5}{2}}}{\sqrt{a + b x}}$ |
| partial | parametric | `(c + d*x)**(5/2)/sqrt(a + b*x)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\sqrt{a + b x}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x*sqrt(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x \sqrt{a + b x}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**2*sqrt(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{2} \sqrt{a + b x}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**3*sqrt(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{3} \sqrt{a + b x}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**4*sqrt(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{4} \sqrt{a + b x}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**5*sqrt(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{5} \sqrt{a + b x}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**6*sqrt(a + b*x))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{6} \sqrt{a + b x}}$ |
| partial | concrete | `x**4*(x + 1)**(3/2)/sqrt(1 - x)` | $\frac{x^{4} \left(x + 1\right)^{\frac{3}{2}}}{\sqrt{1 - x}}$ |
| partial | concrete | `x**3*(x + 1)**(3/2)/sqrt(1 - x)` | $\frac{x^{3} \left(x + 1\right)^{\frac{3}{2}}}{\sqrt{1 - x}}$ |
| partial | concrete | `x**2*(x + 1)**(3/2)/sqrt(1 - x)` | $\frac{x^{2} \left(x + 1\right)^{\frac{3}{2}}}{\sqrt{1 - x}}$ |
| partial | concrete | `x*(x + 1)**(3/2)/sqrt(1 - x)` | $\frac{x \left(x + 1\right)^{\frac{3}{2}}}{\sqrt{1 - x}}$ |
| partial | concrete | `(x + 1)**(3/2)/sqrt(1 - x)` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{\sqrt{1 - x}}$ |
| partial | concrete | `(x + 1)**(3/2)/(x*sqrt(1 - x))` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{x \sqrt{1 - x}}$ |
| partial | concrete | `(x + 1)**(3/2)/(x**2*sqrt(1 - x))` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{x^{2} \sqrt{1 - x}}$ |
| partial | concrete | `(x + 1)**(3/2)/(x**3*sqrt(1 - x))` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{x^{3} \sqrt{1 - x}}$ |
| partial | concrete | `(x + 1)**(3/2)/(x**4*sqrt(1 - x))` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{x^{4} \sqrt{1 - x}}$ |
| partial | concrete | `(x + 1)**(3/2)/(x**5*sqrt(1 - x))` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{x^{5} \sqrt{1 - x}}$ |
| partial | parametric | `x**3/(sqrt(a + b*x)*sqrt(c + d*x))` | $\frac{x^{3}}{\sqrt{a + b x} \sqrt{c + d x}}$ |
| partial | parametric | `x**2/(sqrt(a + b*x)*sqrt(c + d*x))` | $\frac{x^{2}}{\sqrt{a + b x} \sqrt{c + d x}}$ |
| partial | parametric | `x/(sqrt(a + b*x)*sqrt(c + d*x))` | $\frac{x}{\sqrt{a + b x} \sqrt{c + d x}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*sqrt(c + d*x))` | $\frac{1}{\sqrt{a + b x} \sqrt{c + d x}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x)*sqrt(c + d*x))` | $\frac{1}{x \sqrt{a + b x} \sqrt{c + d x}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b*x)*sqrt(c + d*x))` | $\frac{1}{x^{2} \sqrt{a + b x} \sqrt{c + d x}}$ |
| partial | parametric | `1/(x**3*sqrt(a + b*x)*sqrt(c + d*x))` | $\frac{1}{x^{3} \sqrt{a + b x} \sqrt{c + d x}}$ |
| partial | parametric | `1/(x**4*sqrt(a + b*x)*sqrt(c + d*x))` | $\frac{1}{x^{4} \sqrt{a + b x} \sqrt{c + d x}}$ |
| partial | parametric | `x**3/(sqrt(a + b*x)*(c + d*x)**(3/2))` | $\frac{x^{3}}{\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(sqrt(a + b*x)*(c + d*x)**(3/2))` | $\frac{x^{2}}{\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(sqrt(a + b*x)*(c + d*x)**(3/2))` | $\frac{x}{\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(3/2))` | $\frac{1}{\sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/(x*sqrt(a + b*x)*(c + d*x)**(3/2))` | $\frac{1}{x \sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/(x**2*sqrt(a + b*x)*(c + d*x)**(3/2))` | $\frac{1}{x^{2} \sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/(x**3*sqrt(a + b*x)*(c + d*x)**(3/2))` | $\frac{1}{x^{3} \sqrt{a + b x} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/(sqrt(a + b*x)*(c + d*x)**(5/2))` | $\frac{x^{4}}{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3/(sqrt(a + b*x)*(c + d*x)**(5/2))` | $\frac{x^{3}}{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2/(sqrt(a + b*x)*(c + d*x)**(5/2))` | $\frac{x^{2}}{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/(sqrt(a + b*x)*(c + d*x)**(5/2))` | $\frac{x}{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(sqrt(a + b*x)*(c + d*x)**(5/2))` | $\frac{1}{\sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `1/(x*sqrt(a + b*x)*(c + d*x)**(5/2))` | $\frac{1}{x \sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `1/(x**2*sqrt(a + b*x)*(c + d*x)**(5/2))` | $\frac{1}{x^{2} \sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `1/(x**3*sqrt(a + b*x)*(c + d*x)**(5/2))` | $\frac{1}{x^{3} \sqrt{a + b x} \left(c + d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x*sqrt(c*x)*sqrt(a + b*x))` | $\frac{1}{x \sqrt{c x} \sqrt{a + b x}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x)*sqrt(a*c - b*c*x))` | $\frac{1}{x \sqrt{a + b x} \sqrt{a c - b c x}}$ |
| partial | parametric | `1/(x*sqrt(-a - b*x + 1)*sqrt(a + b*x + 1))` | $\frac{1}{x \sqrt{- a - b x + 1} \sqrt{a + b x + 1}}$ |
| partial | parametric | `x**3*(c + d*x)**(3/2)/(a + b*x)**(3/2)` | $\frac{x^{3} \left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(c + d*x)**(3/2)/(a + b*x)**(3/2)` | $\frac{x^{2} \left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(c + d*x)**(3/2)/(a + b*x)**(3/2)` | $\frac{x \left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x)**(3/2)/(a + b*x)**(3/2)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(c + d*x)**(3/2)/(x*(a + b*x)**(3/2))` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{x \left(a + b x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(c + d*x)**(3/2)/(x**2*(a + b*x)**(3/2))` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{x^{2} \left(a + b x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(c + d*x)**(3/2)/(x**3*(a + b*x)**(3/2))` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{x^{3} \left(a + b x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(c + d*x)**(3/2)/(x**4*(a + b*x)**(3/2))` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{x^{4} \left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*(c + d*x)**(5/2)/(a + b*x)**(3/2)` | $\frac{x^{3} \left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(c + d*x)**(5/2)/(a + b*x)**(3/2)` | $\frac{x^{2} \left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(c + d*x)**(5/2)/(a + b*x)**(3/2)` | $\frac{x \left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)**(3/2)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x*(a + b*x)**(3/2))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x \left(a + b x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**2*(a + b*x)**(3/2))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{2} \left(a + b x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**3*(a + b*x)**(3/2))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{3} \left(a + b x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**4*(a + b*x)**(3/2))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{4} \left(a + b x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**5*(a + b*x)**(3/2))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{5} \left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/((a + b*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{x^{4}}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/((a + b*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{x^{3}}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/((a + b*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{x^{2}}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/((a + b*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{x}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{1}{x \left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{1}{x^{2} \left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{1}{x^{3} \left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5/((a + b*x)**(3/2)*(c + d*x)**(5/2))` | $\frac{x^{5}}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4/((a + b*x)**(3/2)*(c + d*x)**(5/2))` | $\frac{x^{4}}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3/((a + b*x)**(3/2)*(c + d*x)**(5/2))` | $\frac{x^{3}}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2/((a + b*x)**(3/2)*(c + d*x)**(5/2))` | $\frac{x^{2}}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/((a + b*x)**(3/2)*(c + d*x)**(5/2))` | $\frac{x}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(5/2))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `1/(x*(a + b*x)**(3/2)*(c + d*x)**(5/2))` | $\frac{1}{x \left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `1/(x**2*(a + b*x)**(3/2)*(c + d*x)**(5/2))` | $\frac{1}{x^{2} \left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `1/(x**3*(a + b*x)**(3/2)*(c + d*x)**(5/2))` | $\frac{1}{x^{3} \left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4*(c + d*x)**(5/2)/(a + b*x)**(5/2)` | $\frac{x^{4} \left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3*(c + d*x)**(5/2)/(a + b*x)**(5/2)` | $\frac{x^{3} \left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2*(c + d*x)**(5/2)/(a + b*x)**(5/2)` | $\frac{x^{2} \left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x*(c + d*x)**(5/2)/(a + b*x)**(5/2)` | $\frac{x \left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d*x)**(5/2)/(a + b*x)**(5/2)` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x*(a + b*x)**(5/2))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x \left(a + b x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**2*(a + b*x)**(5/2))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{2} \left(a + b x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**3*(a + b*x)**(5/2))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{3} \left(a + b x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**4*(a + b*x)**(5/2))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{4} \left(a + b x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(c + d*x)**(5/2)/(x**5*(a + b*x)**(5/2))` | $\frac{\left(c + d x\right)^{\frac{5}{2}}}{x^{5} \left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2/((a + b*x)**(5/2)*sqrt(c + d*x))` | $\frac{x^{2}}{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x}}$ |
| partial | parametric | `x**6/((a + b*x)**(5/2)*(c + d*x)**(5/2))` | $\frac{x^{6}}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**5/((a + b*x)**(5/2)*(c + d*x)**(5/2))` | $\frac{x^{5}}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4/((a + b*x)**(5/2)*(c + d*x)**(5/2))` | $\frac{x^{4}}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**3/((a + b*x)**(5/2)*(c + d*x)**(5/2))` | $\frac{x^{3}}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2/((a + b*x)**(5/2)*(c + d*x)**(5/2))` | $\frac{x^{2}}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/((a + b*x)**(5/2)*(c + d*x)**(5/2))` | $\frac{x}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*x)**(5/2)*(c + d*x)**(5/2))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x)**(5/2)*(c + d*x)**(5/2))` | $\frac{1}{x \left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x)**(5/2)*(c + d*x)**(5/2))` | $\frac{1}{x^{2} \left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x)**(5/2)*(c + d*x)**(5/2))` | $\frac{1}{x^{3} \left(a + b x\right)^{\frac{5}{2}} \left(c + d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2*sqrt(a + b*x)/sqrt(-a - b*x)` | $\frac{x^{2} \sqrt{a + b x}}{\sqrt{- a - b x}}$ |
| SOLVED-both | parametric | `x*sqrt(a + b*x)/sqrt(-a - b*x)` | $\frac{x \sqrt{a + b x}}{\sqrt{- a - b x}}$ |
| SOLVED-both | parametric | `sqrt(a + b*x)/sqrt(-a - b*x)` | $\frac{\sqrt{a + b x}}{\sqrt{- a - b x}}$ |
| SOLVED-both | parametric | `sqrt(a + b*x)/(x*sqrt(-a - b*x))` | $\frac{\sqrt{a + b x}}{x \sqrt{- a - b x}}$ |
| SOLVED-both | parametric | `sqrt(a + b*x)/(x**2*sqrt(-a - b*x))` | $\frac{\sqrt{a + b x}}{x^{2} \sqrt{- a - b x}}$ |
| SOLVED-both | parametric | `sqrt(a + b*x)/(x**3*sqrt(-a - b*x))` | $\frac{\sqrt{a + b x}}{x^{3} \sqrt{- a - b x}}$ |
| partial | concrete | `x**3*sqrt(x + 1)/(1 - x)**(5/2)` | $\frac{x^{3} \sqrt{x + 1}}{\left(1 - x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x*sqrt(x + 1)/(1 - x)**(5/2)` | $\frac{x \sqrt{x + 1}}{\left(1 - x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `sqrt(x + 1)/(1 - x)**(5/2)` | $\frac{\sqrt{x + 1}}{\left(1 - x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `sqrt(x + 1)/(x - 1)**(5/2)` | $\frac{\sqrt{x + 1}}{\left(x - 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(x + 1)/(x*(1 - x)**(5/2))` | $\frac{\sqrt{x + 1}}{x \left(1 - x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(x + 1)/(x**2*(1 - x)**(5/2))` | $\frac{\sqrt{x + 1}}{x^{2} \left(1 - x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(x + 1)/(x**3*(1 - x)**(5/2))` | $\frac{\sqrt{x + 1}}{x^{3} \left(1 - x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x**2/(sqrt(x - 1)*sqrt(x + 1))` | $\frac{x^{2}}{\sqrt{x - 1} \sqrt{x + 1}}$ |
| SOLVED-both | concrete | `x/(sqrt(x - 1)*sqrt(x + 1))` | $\frac{x}{\sqrt{x - 1} \sqrt{x + 1}}$ |
| partial | concrete | `1/(sqrt(x - 1)*sqrt(x + 1))` | $\frac{1}{\sqrt{x - 1} \sqrt{x + 1}}$ |
| partial | concrete | `1/(x*sqrt(x - 1)*sqrt(x + 1))` | $\frac{1}{x \sqrt{x - 1} \sqrt{x + 1}}$ |
| SOLVED-both | concrete | `1/(x**2*sqrt(x - 1)*sqrt(x + 1))` | $\frac{1}{x^{2} \sqrt{x - 1} \sqrt{x + 1}}$ |
| partial | concrete | `x**2*sqrt(x - 1)*sqrt(x + 1)` | $x^{2} \sqrt{x - 1} \sqrt{x + 1}$ |
| **SOLVED-NEW** | concrete | `x*sqrt(x - 1)*sqrt(x + 1)` | $x \sqrt{x - 1} \sqrt{x + 1}$ |
| partial | concrete | `sqrt(x - 1)*sqrt(x + 1)` | $\sqrt{x - 1} \sqrt{x + 1}$ |
| partial | concrete | `sqrt(x - 1)*sqrt(x + 1)/x` | $\frac{\sqrt{x - 1} \sqrt{x + 1}}{x}$ |
| partial | concrete | `sqrt(x - 1)*sqrt(x + 1)/x**2` | $\frac{\sqrt{x - 1} \sqrt{x + 1}}{x^{2}}$ |
| partial | concrete | `1/(sqrt(2*x + 1)*sqrt(2*x + 3))` | $\frac{1}{\sqrt{2 x + 1} \sqrt{2 x + 3}}$ |
| partial | concrete | `1/(x*sqrt(3*x - 2)*sqrt(5*x + 3))` | $\frac{1}{x \sqrt{3 x - 2} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/(x*(x - 1)**(3/2)*(x + 1)**(3/2))` | $\frac{1}{x \left(x - 1\right)^{\frac{3}{2}} \left(x + 1\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | concrete | `x*sqrt(1 - x)*sqrt(x + 1)` | $x \sqrt{1 - x} \sqrt{x + 1}$ |
| partial | concrete | `x**3*(3*x + 2)**(3/2)*sqrt(4*x + 1)` | $x^{3} \left(3 x + 2\right)^{\frac{3}{2}} \sqrt{4 x + 1}$ |
| partial | parametric | `1/(sqrt(a + b*x - 1)*sqrt(a + b*x + 1))` | $\frac{1}{\sqrt{a + b x - 1} \sqrt{a + b x + 1}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(a - b*x)*sqrt(a + b*x))` | $\frac{1}{\sqrt{x} \sqrt{a - b x} \sqrt{a + b x}}$ |
| partial | parametric | `1/(sqrt(-x)*sqrt(a - b*x)*sqrt(a + b*x))` | $\frac{1}{\sqrt{- x} \sqrt{a - b x} \sqrt{a + b x}}$ |
| partial | parametric | `1/(sqrt(e*x)*sqrt(a - b*x)*sqrt(a + b*x))` | $\frac{1}{\sqrt{e x} \sqrt{a - b x} \sqrt{a + b x}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(-b*x + 2)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{x} \sqrt{- b x + 2} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(-x)*sqrt(-b*x + 2)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{- x} \sqrt{- b x + 2} \sqrt{b x + 2}}$ |
| partial | parametric | `1/(sqrt(e*x)*sqrt(-b*x + 2)*sqrt(b*x + 2))` | $\frac{1}{\sqrt{e x} \sqrt{- b x + 2} \sqrt{b x + 2}}$ |
| partial | concrete | `1/(sqrt(x)*sqrt(2 - 3*x)*sqrt(3*x + 2))` | $\frac{1}{\sqrt{x} \sqrt{2 - 3 x} \sqrt{3 x + 2}}$ |
| partial | concrete | `1/(sqrt(-x)*sqrt(2 - 3*x)*sqrt(3*x + 2))` | $\frac{1}{\sqrt{- x} \sqrt{2 - 3 x} \sqrt{3 x + 2}}$ |
| partial | parametric | `1/(sqrt(e*x)*sqrt(2 - 3*x)*sqrt(3*x + 2))` | $\frac{1}{\sqrt{e x} \sqrt{2 - 3 x} \sqrt{3 x + 2}}$ |
| partial | concrete | `1/(sqrt(x)*sqrt(1 - x)*sqrt(x + 1))` | $\frac{1}{\sqrt{x} \sqrt{1 - x} \sqrt{x + 1}}$ |
| partial | concrete | `1/(sqrt(x + 1)*sqrt(-x**2 + x))` | $\frac{1}{\sqrt{x + 1} \sqrt{- x^{2} + x}}$ |
| partial | parametric | `1/(sqrt(b*x)*sqrt(-c*x + 1)*sqrt(c*x + 1))` | $\frac{1}{\sqrt{b x} \sqrt{- c x + 1} \sqrt{c x + 1}}$ |
| partial | parametric | `1/(sqrt(b*x)*sqrt(-c*x + 1)*sqrt(d*x + 1))` | $\frac{1}{\sqrt{b x} \sqrt{- c x + 1} \sqrt{d x + 1}}$ |
| partial | concrete | `sqrt(x + 1)/(sqrt(x)*sqrt(1 - x))` | $\frac{\sqrt{x + 1}}{\sqrt{x} \sqrt{1 - x}}$ |
| partial | concrete | `sqrt(x + 1)/sqrt(-x**2 + x)` | $\frac{\sqrt{x + 1}}{\sqrt{- x^{2} + x}}$ |
| partial | parametric | `sqrt(c*x + 1)/(sqrt(b*x)*sqrt(-c*x + 1))` | $\frac{\sqrt{c x + 1}}{\sqrt{b x} \sqrt{- c x + 1}}$ |
| partial | parametric | `sqrt(c*x + 1)/(sqrt(b*x)*sqrt(-d*x + 1))` | $\frac{\sqrt{c x + 1}}{\sqrt{b x} \sqrt{- d x + 1}}$ |
| partial | concrete | `sqrt(1 - x)/(sqrt(x)*sqrt(x + 1))` | $\frac{\sqrt{1 - x}}{\sqrt{x} \sqrt{x + 1}}$ |
| partial | parametric | `sqrt(-c*x + 1)/(sqrt(b*x)*sqrt(c*x + 1))` | $\frac{\sqrt{- c x + 1}}{\sqrt{b x} \sqrt{c x + 1}}$ |
| partial | parametric | `sqrt(-c*x + 1)/(sqrt(b*x)*sqrt(d*x + 1))` | $\frac{\sqrt{- c x + 1}}{\sqrt{b x} \sqrt{d x + 1}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(2 - 3*x)*sqrt(d + e*x))` | $\frac{1}{\sqrt{x} \sqrt{2 - 3 x} \sqrt{d + e x}}$ |
| partial | parametric | `sqrt(d + e*x)/(sqrt(x)*sqrt(2 - 3*x))` | $\frac{\sqrt{d + e x}}{\sqrt{x} \sqrt{2 - 3 x}}$ |
| partial | concrete | `x**4/((1 - x)**(1/3)*(2 - x)**(1/3))` | $\frac{x^{4}}{\sqrt[3]{1 - x} \sqrt[3]{2 - x}}$ |
| partial | concrete | `x**3/((1 - x)**(1/3)*(2 - x)**(1/3))` | $\frac{x^{3}}{\sqrt[3]{1 - x} \sqrt[3]{2 - x}}$ |
| partial | concrete | `x**2/((1 - x)**(1/3)*(2 - x)**(1/3))` | $\frac{x^{2}}{\sqrt[3]{1 - x} \sqrt[3]{2 - x}}$ |
| partial | concrete | `x/((1 - x)**(1/3)*(2 - x)**(1/3))` | $\frac{x}{\sqrt[3]{1 - x} \sqrt[3]{2 - x}}$ |
| partial | concrete | `1/((1 - x)**(1/3)*(2 - x)**(1/3))` | $\frac{1}{\sqrt[3]{1 - x} \sqrt[3]{2 - x}}$ |
| partial | concrete | `1/(x*(1 - x)**(1/3)*(2 - x)**(1/3))` | $\frac{1}{x \sqrt[3]{1 - x} \sqrt[3]{2 - x}}$ |
| partial | concrete | `1/(x**2*(1 - x)**(1/3)*(2 - x)**(1/3))` | $\frac{1}{x^{2} \sqrt[3]{1 - x} \sqrt[3]{2 - x}}$ |
| partial | concrete | `1/(x**3*(1 - x)**(1/3)*(2 - x)**(1/3))` | $\frac{1}{x^{3} \sqrt[3]{1 - x} \sqrt[3]{2 - x}}$ |
| partial | parametric | `x**3*(a + b*x)**(1/4)/(c + d*x)**(1/4)` | $\frac{x^{3} \sqrt[4]{a + b x}}{\sqrt[4]{c + d x}}$ |
| partial | parametric | `x**2*(a + b*x)**(1/4)/(c + d*x)**(1/4)` | $\frac{x^{2} \sqrt[4]{a + b x}}{\sqrt[4]{c + d x}}$ |
| partial | parametric | `x*(a + b*x)**(1/4)/(c + d*x)**(1/4)` | $\frac{x \sqrt[4]{a + b x}}{\sqrt[4]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(1/4)/(c + d*x)**(1/4)` | $\frac{\sqrt[4]{a + b x}}{\sqrt[4]{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(1/4)/(x*(c + d*x)**(1/4))` | $\frac{\sqrt[4]{a + b x}}{x \sqrt[4]{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(1/4)/(x**2*(c + d*x)**(1/4))` | $\frac{\sqrt[4]{a + b x}}{x^{2} \sqrt[4]{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(1/4)/(x**3*(c + d*x)**(1/4))` | $\frac{\sqrt[4]{a + b x}}{x^{3} \sqrt[4]{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(1/4)/(x**4*(c + d*x)**(1/4))` | $\frac{\sqrt[4]{a + b x}}{x^{4} \sqrt[4]{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(1/4)/(x**5*(c + d*x)**(1/4))` | $\frac{\sqrt[4]{a + b x}}{x^{5} \sqrt[4]{c + d x}}$ |
| partial | concrete | `x**2*(x + 1)**(1/4)/(1 - x)**(1/4)` | $\frac{x^{2} \sqrt[4]{x + 1}}{\sqrt[4]{1 - x}}$ |
| partial | concrete | `x*(x + 1)**(1/4)/(1 - x)**(1/4)` | $\frac{x \sqrt[4]{x + 1}}{\sqrt[4]{1 - x}}$ |
| partial | concrete | `(x + 1)**(1/4)/(1 - x)**(1/4)` | $\frac{\sqrt[4]{x + 1}}{\sqrt[4]{1 - x}}$ |
| partial | concrete | `(x + 1)**(1/4)/(x*(1 - x)**(1/4))` | $\frac{\sqrt[4]{x + 1}}{x \sqrt[4]{1 - x}}$ |
| partial | concrete | `(x + 1)**(1/4)/(x**2*(1 - x)**(1/4))` | $\frac{\sqrt[4]{x + 1}}{x^{2} \sqrt[4]{1 - x}}$ |
| partial | concrete | `(x + 1)**(1/4)/(x**3*(1 - x)**(1/4))` | $\frac{\sqrt[4]{x + 1}}{x^{3} \sqrt[4]{1 - x}}$ |
| partial | concrete | `(x + 1)**(1/4)/(x**4*(1 - x)**(1/4))` | $\frac{\sqrt[4]{x + 1}}{x^{4} \sqrt[4]{1 - x}}$ |
| partial | concrete | `(x + 1)**(1/4)/(x**5*(1 - x)**(1/4))` | $\frac{\sqrt[4]{x + 1}}{x^{5} \sqrt[4]{1 - x}}$ |
| partial | parametric | `x**3/((a + b*x)**(3/4)*(c + d*x)**(1/4))` | $\frac{x^{3}}{\left(a + b x\right)^{\frac{3}{4}} \sqrt[4]{c + d x}}$ |
| partial | parametric | `x**2/((a + b*x)**(3/4)*(c + d*x)**(1/4))` | $\frac{x^{2}}{\left(a + b x\right)^{\frac{3}{4}} \sqrt[4]{c + d x}}$ |
| partial | parametric | `x/((a + b*x)**(3/4)*(c + d*x)**(1/4))` | $\frac{x}{\left(a + b x\right)^{\frac{3}{4}} \sqrt[4]{c + d x}}$ |
| partial | parametric | `1/((a + b*x)**(3/4)*(c + d*x)**(1/4))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{4}} \sqrt[4]{c + d x}}$ |
| timeout | parametric | `1/(x*(a + b*x)**(3/4)*(c + d*x)**(1/4))` | $\frac{1}{x \left(a + b x\right)^{\frac{3}{4}} \sqrt[4]{c + d x}}$ |
| timeout | parametric | `1/(x**2*(a + b*x)**(3/4)*(c + d*x)**(1/4))` | $\frac{1}{x^{2} \left(a + b x\right)^{\frac{3}{4}} \sqrt[4]{c + d x}}$ |
| timeout | parametric | `1/(x**3*(a + b*x)**(3/4)*(c + d*x)**(1/4))` | $\frac{1}{x^{3} \left(a + b x\right)^{\frac{3}{4}} \sqrt[4]{c + d x}}$ |
| timeout | parametric | `1/(x**4*(a + b*x)**(3/4)*(c + d*x)**(1/4))` | $\frac{1}{x^{4} \left(a + b x\right)^{\frac{3}{4}} \sqrt[4]{c + d x}}$ |
| partial | parametric | `(e*x)**(3/2)/((1 - x)**(1/4)*(x + 1)**(1/4))` | $\frac{\left(e x\right)^{\frac{3}{2}}}{\sqrt[4]{1 - x} \sqrt[4]{x + 1}}$ |
| partial | parametric | `1/(sqrt(e*x)*(1 - x)**(1/4)*(x + 1)**(1/4))` | $\frac{1}{\sqrt{e x} \sqrt[4]{1 - x} \sqrt[4]{x + 1}}$ |
| **SOLVED-NEW** | parametric | `1/((e*x)**(5/2)*(1 - x)**(1/4)*(x + 1)**(1/4))` | $\frac{1}{\left(e x\right)^{\frac{5}{2}} \sqrt[4]{1 - x} \sqrt[4]{x + 1}}$ |
| timeout | parametric | `1/((e*x)**(9/2)*(1 - x)**(1/4)*(x + 1)**(1/4))` | $\frac{1}{\left(e x\right)^{\frac{9}{2}} \sqrt[4]{1 - x} \sqrt[4]{x + 1}}$ |
| timeout | parametric | `1/((e*x)**(13/2)*(1 - x)**(1/4)*(x + 1)**(1/4))` | $\frac{1}{\left(e x\right)^{\frac{13}{2}} \sqrt[4]{1 - x} \sqrt[4]{x + 1}}$ |
| partial | parametric | `(e*x)**(5/2)/((1 - x)**(1/4)*(x + 1)**(1/4))` | $\frac{\left(e x\right)^{\frac{5}{2}}}{\sqrt[4]{1 - x} \sqrt[4]{x + 1}}$ |
| partial | parametric | `sqrt(e*x)/((1 - x)**(1/4)*(x + 1)**(1/4))` | $\frac{\sqrt{e x}}{\sqrt[4]{1 - x} \sqrt[4]{x + 1}}$ |
| partial | parametric | `1/((e*x)**(3/2)*(1 - x)**(1/4)*(x + 1)**(1/4))` | $\frac{1}{\left(e x\right)^{\frac{3}{2}} \sqrt[4]{1 - x} \sqrt[4]{x + 1}}$ |
| partial | parametric | `1/((e*x)**(7/2)*(1 - x)**(1/4)*(x + 1)**(1/4))` | $\frac{1}{\left(e x\right)^{\frac{7}{2}} \sqrt[4]{1 - x} \sqrt[4]{x + 1}}$ |
| timeout | parametric | `1/((e*x)**(11/2)*(1 - x)**(1/4)*(x + 1)**(1/4))` | $\frac{1}{\left(e x\right)^{\frac{11}{2}} \sqrt[4]{1 - x} \sqrt[4]{x + 1}}$ |
| partial | parametric | `(c + d*x)**(3/2)/((a + b*x)**2*(e + f*x))` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{2} \left(e + f x\right)}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)*(d + e*x)**(7/2)` | $\left(A + B x\right) \left(a + b x\right) \left(d + e x\right)^{\frac{7}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)*(d + e*x)**(5/2)` | $\left(A + B x\right) \left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)*(d + e*x)**(3/2)` | $\left(A + B x\right) \left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)*sqrt(d + e*x)` | $\left(A + B x\right) \left(a + b x\right) \sqrt{d + e x}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a + b x\right)}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**2*(d + e*x)**(7/2)` | $\left(A + B x\right) \left(a + b x\right)^{2} \left(d + e x\right)^{\frac{7}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**2*(d + e*x)**(5/2)` | $\left(A + B x\right) \left(a + b x\right)^{2} \left(d + e x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**2*(d + e*x)**(3/2)` | $\left(A + B x\right) \left(a + b x\right)^{2} \left(d + e x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**2*sqrt(d + e*x)` | $\left(A + B x\right) \left(a + b x\right)^{2} \sqrt{d + e x}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**2/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**2/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**2/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**2/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**3*(d + e*x)**(7/2)` | $\left(A + B x\right) \left(a + b x\right)^{3} \left(d + e x\right)^{\frac{7}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**3*(d + e*x)**(5/2)` | $\left(A + B x\right) \left(a + b x\right)^{3} \left(d + e x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**3*(d + e*x)**(3/2)` | $\left(A + B x\right) \left(a + b x\right)^{3} \left(d + e x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**3*sqrt(d + e*x)` | $\left(A + B x\right) \left(a + b x\right)^{3} \sqrt{d + e x}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**3/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{3}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**3/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{3}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**3/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{3}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x)**3/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{3}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(a + b*x)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{a + b x}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a + b*x)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{a + b x}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a + b*x)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{a + b x}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a + b*x)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{a + b x}$ |
| partial | parametric | `(A + B*x)/((a + b*x)*sqrt(d + e*x))` | $\frac{A + B x}{\left(a + b x\right) \sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)/((a + b*x)*(d + e*x)**(3/2))` | $\frac{A + B x}{\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((a + b*x)*(d + e*x)**(5/2))` | $\frac{A + B x}{\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((a + b*x)*(d + e*x)**(7/2))` | $\frac{A + B x}{\left(a + b x\right) \left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(a + b*x)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a + b*x)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a + b*x)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a + b*x)**2` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `(A + B*x)/((a + b*x)**2*sqrt(d + e*x))` | $\frac{A + B x}{\left(a + b x\right)^{2} \sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)/((a + b*x)**2*(d + e*x)**(3/2))` | $\frac{A + B x}{\left(a + b x\right)^{2} \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((a + b*x)**2*(d + e*x)**(5/2))` | $\frac{A + B x}{\left(a + b x\right)^{2} \left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((a + b*x)**2*(d + e*x)**(7/2))` | $\frac{A + B x}{\left(a + b x\right)^{2} \left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(a + b*x)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a + b*x)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a + b*x)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a + b*x)**3` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `(A + B*x)/((a + b*x)**3*sqrt(d + e*x))` | $\frac{A + B x}{\left(a + b x\right)^{3} \sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)/((a + b*x)**3*(d + e*x)**(3/2))` | $\frac{A + B x}{\left(a + b x\right)^{3} \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((a + b*x)**3*(d + e*x)**(5/2))` | $\frac{A + B x}{\left(a + b x\right)^{3} \left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((a + b*x)**3*(d + e*x)**(7/2))` | $\frac{A + B x}{\left(a + b x\right)^{3} \left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x)*(e + f*x)**(5/2)/(c + d*x)` | $\frac{\left(a + b x\right) \left(e + f x\right)^{\frac{5}{2}}}{c + d x}$ |
| partial | parametric | `(a + b*x)*(e + f*x)**(3/2)/(c + d*x)` | $\frac{\left(a + b x\right) \left(e + f x\right)^{\frac{3}{2}}}{c + d x}$ |
| partial | parametric | `(a + b*x)*sqrt(e + f*x)/(c + d*x)` | $\frac{\left(a + b x\right) \sqrt{e + f x}}{c + d x}$ |
| partial | parametric | `(a + b*x)/((c + d*x)*sqrt(e + f*x))` | $\frac{a + b x}{\left(c + d x\right) \sqrt{e + f x}}$ |
| partial | parametric | `(a + b*x)/((c + d*x)*(e + f*x)**(3/2))` | $\frac{a + b x}{\left(c + d x\right) \left(e + f x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)/((c + d*x)*(e + f*x)**(5/2))` | $\frac{a + b x}{\left(c + d x\right) \left(e + f x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)/((c + d*x)*(e + f*x)**(7/2))` | $\frac{a + b x}{\left(c + d x\right) \left(e + f x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x)/((c + d*x)*(e + f*x)**(9/2))` | $\frac{a + b x}{\left(c + d x\right) \left(e + f x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x)**2*(e + f*x)**(5/2)/(c + d*x)` | $\frac{\left(a + b x\right)^{2} \left(e + f x\right)^{\frac{5}{2}}}{c + d x}$ |
| partial | parametric | `(a + b*x)**2*(e + f*x)**(3/2)/(c + d*x)` | $\frac{\left(a + b x\right)^{2} \left(e + f x\right)^{\frac{3}{2}}}{c + d x}$ |
| partial | parametric | `(a + b*x)**2*sqrt(e + f*x)/(c + d*x)` | $\frac{\left(a + b x\right)^{2} \sqrt{e + f x}}{c + d x}$ |
| partial | parametric | `(a + b*x)**2/((c + d*x)*sqrt(e + f*x))` | $\frac{\left(a + b x\right)^{2}}{\left(c + d x\right) \sqrt{e + f x}}$ |
| partial | parametric | `(a + b*x)**2/((c + d*x)*(e + f*x)**(3/2))` | $\frac{\left(a + b x\right)^{2}}{\left(c + d x\right) \left(e + f x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)**2/((c + d*x)*(e + f*x)**(5/2))` | $\frac{\left(a + b x\right)^{2}}{\left(c + d x\right) \left(e + f x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)**2/((c + d*x)*(e + f*x)**(7/2))` | $\frac{\left(a + b x\right)^{2}}{\left(c + d x\right) \left(e + f x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x)**2/((c + d*x)*(e + f*x)**(9/2))` | $\frac{\left(a + b x\right)^{2}}{\left(c + d x\right) \left(e + f x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x)**3*(e + f*x)**(5/2)/(c + d*x)` | $\frac{\left(a + b x\right)^{3} \left(e + f x\right)^{\frac{5}{2}}}{c + d x}$ |
| partial | parametric | `(a + b*x)**3*(e + f*x)**(3/2)/(c + d*x)` | $\frac{\left(a + b x\right)^{3} \left(e + f x\right)^{\frac{3}{2}}}{c + d x}$ |
| partial | parametric | `(a + b*x)**3*sqrt(e + f*x)/(c + d*x)` | $\frac{\left(a + b x\right)^{3} \sqrt{e + f x}}{c + d x}$ |
| partial | parametric | `(a + b*x)**3/((c + d*x)*sqrt(e + f*x))` | $\frac{\left(a + b x\right)^{3}}{\left(c + d x\right) \sqrt{e + f x}}$ |
| partial | parametric | `(a + b*x)**3/((c + d*x)*(e + f*x)**(5/2))` | $\frac{\left(a + b x\right)^{3}}{\left(c + d x\right) \left(e + f x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)**3/((c + d*x)*(e + f*x)**(7/2))` | $\frac{\left(a + b x\right)^{3}}{\left(c + d x\right) \left(e + f x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x)**3/((c + d*x)*(e + f*x)**(9/2))` | $\frac{\left(a + b x\right)^{3}}{\left(c + d x\right) \left(e + f x\right)^{\frac{9}{2}}}$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)**6*(5*x + 3)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{6} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)**5*(5*x + 3)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{5} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)**4*(5*x + 3)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{4} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)**3*(5*x + 3)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{3} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)**2*(5*x + 3)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{2} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)*(5*x + 3)` | $\sqrt{1 - 2 x} \left(3 x + 2\right) \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(5*x + 3)` | $\sqrt{1 - 2 x} \left(5 x + 3\right)$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)/(3*x + 2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)}{3 x + 2}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)/(3*x + 2)**2` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)/(3*x + 2)**3` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)/(3*x + 2)**4` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)/(3*x + 2)**5` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)/(3*x + 2)**6` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)}{\left(3 x + 2\right)^{6}}$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)**4*(5*x + 3)**2` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{2}$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)**3*(5*x + 3)**2` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{2}$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)**2*(5*x + 3)**2` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{2}$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)*(5*x + 3)**2` | $\sqrt{1 - 2 x} \left(3 x + 2\right) \left(5 x + 3\right)^{2}$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(5*x + 3)**2` | $\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**2/(3*x + 2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}{3 x + 2}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**2/(3*x + 2)**2` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**2/(3*x + 2)**3` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**2/(3*x + 2)**4` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**2/(3*x + 2)**5` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**2/(3*x + 2)**6` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**2/(3*x + 2)**7` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{7}}$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)**4*(5*x + 3)**3` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{3}$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)**3*(5*x + 3)**3` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{3}$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)**2*(5*x + 3)**3` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{3}$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(3*x + 2)*(5*x + 3)**3` | $\sqrt{1 - 2 x} \left(3 x + 2\right) \left(5 x + 3\right)^{3}$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)*(5*x + 3)**3` | $\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**3/(3*x + 2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}{3 x + 2}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**3/(3*x + 2)**2` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**3/(3*x + 2)**3` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**3/(3*x + 2)**4` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**3/(3*x + 2)**5` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**3/(3*x + 2)**6` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**3/(3*x + 2)**7` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{7}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**3/(3*x + 2)**8` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{8}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**4/(5*x + 3)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4}}{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**3/(5*x + 3)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3}}{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**2/(5*x + 3)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2}}{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)/(5*x + 3)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)}{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)/(5*x + 3)` | $\frac{\sqrt{1 - 2 x}}{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)*(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right) \left(5 x + 3\right)}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**2*(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**3*(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**4*(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**5*(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{5} \left(5 x + 3\right)}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**5/(5*x + 3)**2` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{5}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**4/(5*x + 3)**2` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**3/(5*x + 3)**2` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**2/(5*x + 3)**2` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)/(5*x + 3)**2` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)/(5*x + 3)**2` | $\frac{\sqrt{1 - 2 x}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)*(5*x + 3)**2)` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right) \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**2*(5*x + 3)**2)` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**3*(5*x + 3)**2)` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**4*(5*x + 3)**2)` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**4/(5*x + 3)**3` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4}}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**3/(5*x + 3)**3` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3}}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**2/(5*x + 3)**3` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2}}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)/(5*x + 3)**3` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/(5*x + 3)**3` | $\frac{\sqrt{1 - 2 x}}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)*(5*x + 3)**3)` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right) \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**2*(5*x + 3)**3)` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**3*(5*x + 3)**3)` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**4*(5*x + 3)**3)` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{3}}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**6*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{6} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**5*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{5} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**4*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**3*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**2*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right) \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)/(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}{3 x + 2}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)/(3*x + 2)**2` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)/(3*x + 2)**3` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)/(3*x + 2)**4` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)/(3*x + 2)**5` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)/(3*x + 2)**6` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}{\left(3 x + 2\right)^{6}}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**4*(5*x + 3)**2` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{2}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**3*(5*x + 3)**2` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{2}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**2*(5*x + 3)**2` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{2}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)*(5*x + 3)**2` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{2}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**2` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**2/(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}{3 x + 2}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**2/(3*x + 2)**2` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**2/(3*x + 2)**3` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**2/(3*x + 2)**4` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**2/(3*x + 2)**5` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**2/(3*x + 2)**6` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**2/(3*x + 2)**7` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{7}}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**4*(5*x + 3)**3` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{3}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**3*(5*x + 3)**3` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{3}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**2*(5*x + 3)**3` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{3}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)*(5*x + 3)**3` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{3}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**3` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**3/(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}{3 x + 2}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**3/(3*x + 2)**2` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**3/(3*x + 2)**3` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**3/(3*x + 2)**4` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**3/(3*x + 2)**5` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**3/(3*x + 2)**6` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**3/(3*x + 2)**7` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{7}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**3/(3*x + 2)**8` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{8}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**6/(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{6}}{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**5/(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{5}}{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**4/(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4}}{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**3/(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3}}{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**2/(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2}}{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)/(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)}{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right) \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**2*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**3*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**4*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**5*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{5} \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**6*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{6} \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**5/(5*x + 3)**2` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{5}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**4/(5*x + 3)**2` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**3/(5*x + 3)**2` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**2/(5*x + 3)**2` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)/(5*x + 3)**2` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/(5*x + 3)**2` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)*(5*x + 3)**2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right) \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**2*(5*x + 3)**2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**3*(5*x + 3)**2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**4*(5*x + 3)**2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**5*(5*x + 3)**2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{5} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**4/(5*x + 3)**3` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4}}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**3/(5*x + 3)**3` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3}}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**2/(5*x + 3)**3` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2}}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)/(5*x + 3)**3` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/(5*x + 3)**3` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)*(5*x + 3)**3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right) \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**2*(5*x + 3)**3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**3*(5*x + 3)**3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**4*(5*x + 3)**3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{3}}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**6*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{6} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**5*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{5} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**4*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**3*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**2*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right) \left(5 x + 3\right)$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)/(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}{3 x + 2}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)/(3*x + 2)**2` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)/(3*x + 2)**3` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)/(3*x + 2)**4` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)/(3*x + 2)**5` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)/(3*x + 2)**6` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)/(3*x + 2)**7` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}{\left(3 x + 2\right)^{7}}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**4*(5*x + 3)**2` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{2}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**3*(5*x + 3)**2` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{2}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**2*(5*x + 3)**2` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{2}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)*(5*x + 3)**2` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{2}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**2` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**2/(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}{3 x + 2}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**2/(3*x + 2)**2` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**2/(3*x + 2)**3` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**2/(3*x + 2)**4` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**2/(3*x + 2)**5` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**2/(3*x + 2)**6` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**2/(3*x + 2)**7` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{7}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**2/(3*x + 2)**8` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}{\left(3 x + 2\right)^{8}}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**4*(5*x + 3)**3` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{3}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**3*(5*x + 3)**3` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{3}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**2*(5*x + 3)**3` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{3}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)*(5*x + 3)**3` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{3}$ |
| SOLVED-both | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**3` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**3/(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}{3 x + 2}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**3/(3*x + 2)**2` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**3/(3*x + 2)**3` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**3/(3*x + 2)**4` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**3/(3*x + 2)**5` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**3/(3*x + 2)**6` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**3/(3*x + 2)**7` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{7}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**3/(3*x + 2)**8` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}{\left(3 x + 2\right)^{8}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**4/(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4}}{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**3/(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3}}{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**2/(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2}}{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)/(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)}{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right) \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**2*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**3*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**4*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**5*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{5} \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**6*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{6} \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**7*(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{7} \left(5 x + 3\right)}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**4/(5*x + 3)**2` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**3/(5*x + 3)**2` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**2/(5*x + 3)**2` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)/(5*x + 3)**2` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/(5*x + 3)**2` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)*(5*x + 3)**2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right) \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**2*(5*x + 3)**2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**3*(5*x + 3)**2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**4*(5*x + 3)**2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**5*(5*x + 3)**2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{5} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**6*(5*x + 3)**2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{6} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**4/(5*x + 3)**3` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4}}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**3/(5*x + 3)**3` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3}}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**2/(5*x + 3)**3` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2}}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)/(5*x + 3)**3` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/(5*x + 3)**3` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)*(5*x + 3)**3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right) \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**2*(5*x + 3)**3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**3*(5*x + 3)**3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**4*(5*x + 3)**3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**5*(5*x + 3)**3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{5} \left(5 x + 3\right)^{3}}$ |
| SOLVED-both | concrete | `(3*x + 2)**5*(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{5} \left(5 x + 3\right)}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(3*x + 2)**4*(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(3*x + 2)**3*(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(3*x + 2)**2*(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(3*x + 2)*(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(5*x + 3)/sqrt(1 - 2*x)` | $\frac{5 x + 3}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2))` | $\frac{5 x + 3}{\sqrt{1 - 2 x} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2)**2)` | $\frac{5 x + 3}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2)**3)` | $\frac{5 x + 3}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2)**4)` | $\frac{5 x + 3}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2)**5)` | $\frac{5 x + 3}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{5}}$ |
| SOLVED-both | concrete | `(3*x + 2)**5*(5*x + 3)**2/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{5} \left(5 x + 3\right)^{2}}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(3*x + 2)**4*(5*x + 3)**2/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{2}}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(3*x + 2)**3*(5*x + 3)**2/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{2}}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(3*x + 2)**2*(5*x + 3)**2/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{2}}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(3*x + 2)*(5*x + 3)**2/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)^{2}}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(5*x + 3)**2/sqrt(1 - 2*x)` | $\frac{\left(5 x + 3\right)^{2}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(5*x + 3)**2/(sqrt(1 - 2*x)*(3*x + 2))` | $\frac{\left(5 x + 3\right)^{2}}{\sqrt{1 - 2 x} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)**2/(sqrt(1 - 2*x)*(3*x + 2)**2)` | $\frac{\left(5 x + 3\right)^{2}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)**2/(sqrt(1 - 2*x)*(3*x + 2)**3)` | $\frac{\left(5 x + 3\right)^{2}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)**2/(sqrt(1 - 2*x)*(3*x + 2)**4)` | $\frac{\left(5 x + 3\right)^{2}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)**2/(sqrt(1 - 2*x)*(3*x + 2)**5)` | $\frac{\left(5 x + 3\right)^{2}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(5*x + 3)**2/(sqrt(1 - 2*x)*(3*x + 2)**6)` | $\frac{\left(5 x + 3\right)^{2}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{6}}$ |
| SOLVED-both | concrete | `(3*x + 2)**4*(5*x + 3)**3/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{3}}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(3*x + 2)**3*(5*x + 3)**3/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{3}}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(3*x + 2)**2*(5*x + 3)**3/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{3}}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(3*x + 2)*(5*x + 3)**3/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)^{3}}{\sqrt{1 - 2 x}}$ |
| SOLVED-both | concrete | `(5*x + 3)**3/sqrt(1 - 2*x)` | $\frac{\left(5 x + 3\right)^{3}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(5*x + 3)**3/(sqrt(1 - 2*x)*(3*x + 2))` | $\frac{\left(5 x + 3\right)^{3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)**3/(sqrt(1 - 2*x)*(3*x + 2)**2)` | $\frac{\left(5 x + 3\right)^{3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)**3/(sqrt(1 - 2*x)*(3*x + 2)**3)` | $\frac{\left(5 x + 3\right)^{3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)**3/(sqrt(1 - 2*x)*(3*x + 2)**4)` | $\frac{\left(5 x + 3\right)^{3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)**3/(sqrt(1 - 2*x)*(3*x + 2)**5)` | $\frac{\left(5 x + 3\right)^{3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(5*x + 3)**3/(sqrt(1 - 2*x)*(3*x + 2)**6)` | $\frac{\left(5 x + 3\right)^{3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{6}}$ |
| partial | parametric | `(a + b*x)**2/((c + d*x)**2*sqrt(e + f*x))` | $\frac{\left(a + b x\right)^{2}}{\left(c + d x\right)^{2} \sqrt{e + f x}}$ |
| partial | concrete | `(3*x + 2)**5/(sqrt(1 - 2*x)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{5}}{\sqrt{1 - 2 x} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**4/(sqrt(1 - 2*x)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{4}}{\sqrt{1 - 2 x} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**3/(sqrt(1 - 2*x)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{3}}{\sqrt{1 - 2 x} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**2/(sqrt(1 - 2*x)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{2}}{\sqrt{1 - 2 x} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)/(sqrt(1 - 2*x)*(5*x + 3))` | $\frac{3 x + 2}{\sqrt{1 - 2 x} \left(5 x + 3\right)}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(5 x + 3\right)}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)*(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right) \left(5 x + 3\right)}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**2*(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2} \left(5 x + 3\right)}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**3*(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3} \left(5 x + 3\right)}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**4*(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4} \left(5 x + 3\right)}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**5*(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{5} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**6/(sqrt(1 - 2*x)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{6}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**5/(sqrt(1 - 2*x)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{5}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**4/(sqrt(1 - 2*x)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{4}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**3/(sqrt(1 - 2*x)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{3}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**2/(sqrt(1 - 2*x)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{2}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)/(sqrt(1 - 2*x)*(5*x + 3)**2)` | $\frac{3 x + 2}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(5*x + 3)**2)` | $\frac{1}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)*(5*x + 3)**2)` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right) \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**2*(5*x + 3)**2)` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**3*(5*x + 3)**2)` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**4*(5*x + 3)**2)` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**6/(sqrt(1 - 2*x)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{6}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)**5/(sqrt(1 - 2*x)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{5}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)**4/(sqrt(1 - 2*x)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{4}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)**3/(sqrt(1 - 2*x)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{3}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)**2/(sqrt(1 - 2*x)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{2}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)/(sqrt(1 - 2*x)*(5*x + 3)**3)` | $\frac{3 x + 2}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(5*x + 3)**3)` | $\frac{1}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)*(5*x + 3)**3)` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right) \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**2*(5*x + 3)**3)` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**3*(5*x + 3)**3)` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**4*(5*x + 3)**3)` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{3}}$ |
| SOLVED-both | concrete | `(3*x + 2)**7*(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{7} \left(5 x + 3\right)}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**6*(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{6} \left(5 x + 3\right)}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**5*(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{5} \left(5 x + 3\right)}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**4*(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**3*(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**2*(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)*(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2))` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2)**2)` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2)**3)` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2)**4)` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2)**5)` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2)**6)` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{6}}$ |
| SOLVED-both | concrete | `(3*x + 2)**5*(5*x + 3)**2/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{5} \left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**4*(5*x + 3)**2/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**3*(5*x + 3)**2/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**2*(5*x + 3)**2/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)*(5*x + 3)**2/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(5*x + 3)**2/(1 - 2*x)**(3/2)` | $\frac{\left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**2/((1 - 2*x)**(3/2)*(3*x + 2))` | $\frac{\left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)**2/((1 - 2*x)**(3/2)*(3*x + 2)**2)` | $\frac{\left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)**2/((1 - 2*x)**(3/2)*(3*x + 2)**3)` | $\frac{\left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)**2/((1 - 2*x)**(3/2)*(3*x + 2)**4)` | $\frac{\left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)**2/((1 - 2*x)**(3/2)*(3*x + 2)**5)` | $\frac{\left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{5}}$ |
| SOLVED-both | concrete | `(3*x + 2)**4*(5*x + 3)**3/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**3*(5*x + 3)**3/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**2*(5*x + 3)**3/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)*(5*x + 3)**3/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(5*x + 3)**3/(1 - 2*x)**(3/2)` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**3/((1 - 2*x)**(3/2)*(3*x + 2))` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)**3/((1 - 2*x)**(3/2)*(3*x + 2)**2)` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)**3/((1 - 2*x)**(3/2)*(3*x + 2)**3)` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)**3/((1 - 2*x)**(3/2)*(3*x + 2)**4)` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)**3/((1 - 2*x)**(3/2)*(3*x + 2)**5)` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(3*x + 2)**6/((1 - 2*x)**(3/2)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{6}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**5/((1 - 2*x)**(3/2)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{5}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**4/((1 - 2*x)**(3/2)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{4}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**3/((1 - 2*x)**(3/2)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**2/((1 - 2*x)**(3/2)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)/((1 - 2*x)**(3/2)*(5*x + 3))` | $\frac{3 x + 2}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)*(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right) \left(5 x + 3\right)}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**2*(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**3*(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**4*(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**6/((1 - 2*x)**(3/2)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{6}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**5/((1 - 2*x)**(3/2)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{5}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**4/((1 - 2*x)**(3/2)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{4}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**3/((1 - 2*x)**(3/2)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**2/((1 - 2*x)**(3/2)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)/((1 - 2*x)**(3/2)*(5*x + 3)**2)` | $\frac{3 x + 2}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(5*x + 3)**2)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)*(5*x + 3)**2)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**2*(5*x + 3)**2)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**3*(5*x + 3)**2)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**6/((1 - 2*x)**(3/2)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{6}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)**5/((1 - 2*x)**(3/2)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{5}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)**4/((1 - 2*x)**(3/2)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{4}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)**3/((1 - 2*x)**(3/2)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)**2/((1 - 2*x)**(3/2)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)/((1 - 2*x)**(3/2)*(5*x + 3)**3)` | $\frac{3 x + 2}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(5*x + 3)**3)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)*(5*x + 3)**3)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**2*(5*x + 3)**3)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**3*(5*x + 3)**3)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{3}}$ |
| SOLVED-both | concrete | `(3*x + 2)**5*(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{5} \left(5 x + 3\right)}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**4*(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**3*(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**2*(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)*(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)/((1 - 2*x)**(5/2)*(3*x + 2))` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)/((1 - 2*x)**(5/2)*(3*x + 2)**2)` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)/((1 - 2*x)**(5/2)*(3*x + 2)**3)` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)/((1 - 2*x)**(5/2)*(3*x + 2)**4)` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)/((1 - 2*x)**(5/2)*(3*x + 2)**5)` | $\frac{5 x + 3}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{5}}$ |
| SOLVED-both | concrete | `(3*x + 2)**5*(5*x + 3)**2/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{5} \left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**4*(5*x + 3)**2/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**3*(5*x + 3)**2/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**2*(5*x + 3)**2/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)*(5*x + 3)**2/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5*x + 3)**2/(1 - 2*x)**(5/2)` | $\frac{\left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)**2/((1 - 2*x)**(5/2)*(3*x + 2))` | $\frac{\left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)**2/((1 - 2*x)**(5/2)*(3*x + 2)**2)` | $\frac{\left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)**2/((1 - 2*x)**(5/2)*(3*x + 2)**3)` | $\frac{\left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)**2/((1 - 2*x)**(5/2)*(3*x + 2)**4)` | $\frac{\left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)**2/((1 - 2*x)**(5/2)*(3*x + 2)**5)` | $\frac{\left(5 x + 3\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{5}}$ |
| SOLVED-both | concrete | `(3*x + 2)**5*(5*x + 3)**3/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{5} \left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**4*(5*x + 3)**3/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**3*(5*x + 3)**3/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)**2*(5*x + 3)**3/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 2)*(5*x + 3)**3/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5*x + 3)**3/(1 - 2*x)**(5/2)` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)**3/((1 - 2*x)**(5/2)*(3*x + 2))` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)**3/((1 - 2*x)**(5/2)*(3*x + 2)**2)` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)**3/((1 - 2*x)**(5/2)*(3*x + 2)**3)` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)**3/((1 - 2*x)**(5/2)*(3*x + 2)**4)` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)**3/((1 - 2*x)**(5/2)*(3*x + 2)**5)` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(5*x + 3)**3/((1 - 2*x)**(5/2)*(3*x + 2)**6)` | $\frac{\left(5 x + 3\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(3*x + 2)**6/((1 - 2*x)**(5/2)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{6}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**5/((1 - 2*x)**(5/2)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{5}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**4/((1 - 2*x)**(5/2)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{4}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**3/((1 - 2*x)**(5/2)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**2/((1 - 2*x)**(5/2)*(5*x + 3))` | $\frac{\left(3 x + 2\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)/((1 - 2*x)**(5/2)*(5*x + 3))` | $\frac{3 x + 2}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)*(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right) \left(5 x + 3\right)}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**2*(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**3*(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**4*(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4} \left(5 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**6/((1 - 2*x)**(5/2)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{6}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**5/((1 - 2*x)**(5/2)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{5}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**4/((1 - 2*x)**(5/2)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{4}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**3/((1 - 2*x)**(5/2)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**2/((1 - 2*x)**(5/2)*(5*x + 3)**2)` | $\frac{\left(3 x + 2\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)/((1 - 2*x)**(5/2)*(5*x + 3)**2)` | $\frac{3 x + 2}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(5*x + 3)**2)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)*(5*x + 3)**2)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**2*(5*x + 3)**2)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**3*(5*x + 3)**2)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{2}}$ |
| partial | concrete | `(3*x + 2)**6/((1 - 2*x)**(5/2)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{6}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)**5/((1 - 2*x)**(5/2)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{5}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)**4/((1 - 2*x)**(5/2)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{4}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)**3/((1 - 2*x)**(5/2)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)**2/((1 - 2*x)**(5/2)*(5*x + 3)**3)` | $\frac{\left(3 x + 2\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `(3*x + 2)/((1 - 2*x)**(5/2)*(5*x + 3)**3)` | $\frac{3 x + 2}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(5*x + 3)**3)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)*(5*x + 3)**3)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**2*(5*x + 3)**3)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{3}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**3*(5*x + 3)**3)` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{3}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)*(d + e*x)**(5/2)` | $\left(A + B x\right) \sqrt{a + b x} \left(d + e x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)*(d + e*x)**(3/2)` | $\left(A + B x\right) \sqrt{a + b x} \left(d + e x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)*sqrt(d + e*x)` | $\left(A + B x\right) \sqrt{a + b x} \sqrt{d + e x}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{\sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a + b*x)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a + b*x)/(d + e*x)**(9/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a + b*x)/(d + e*x)**(11/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a + b*x)/(d + e*x)**(13/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| timeout | parametric | `(A + B*x)*sqrt(a + b*x)/(d + e*x)**(15/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{\left(d + e x\right)^{\frac{15}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)*(d + e*x)**(5/2)` | $\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}} \left(d + e x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)*(d + e*x)**(3/2)` | $\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}} \left(d + e x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)*sqrt(d + e*x)` | $\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}} \sqrt{d + e x}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a + b*x)**(3/2)/(d + e*x)**(9/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a + b*x)**(3/2)/(d + e*x)**(11/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a + b*x)**(3/2)/(d + e*x)**(13/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a + b*x)**(3/2)/(d + e*x)**(15/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{15}{2}}}$ |
| timeout | parametric | `(A + B*x)*(a + b*x)**(3/2)/(d + e*x)**(17/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{17}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)*(d + e*x)**(5/2)` | $\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}} \left(d + e x\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)*(d + e*x)**(3/2)` | $\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}} \left(d + e x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)*sqrt(d + e*x)` | $\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}} \sqrt{d + e x}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + b*x)**(5/2)/(d + e*x)**(9/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a + b*x)**(5/2)/(d + e*x)**(11/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a + b*x)**(5/2)/(d + e*x)**(13/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a + b*x)**(5/2)/(d + e*x)**(15/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{15}{2}}}$ |
| timeout | parametric | `(A + B*x)*(a + b*x)**(5/2)/(d + e*x)**(17/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{17}{2}}}$ |
| timeout | parametric | `(A + B*x)*(a + b*x)**(5/2)/(d + e*x)**(19/2)` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{19}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/sqrt(a + b*x)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\sqrt{a + b x}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/sqrt(a + b*x)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\sqrt{a + b x}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/sqrt(a + b*x)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\sqrt{a + b x}}$ |
| partial | parametric | `(A + B*x)/(sqrt(a + b*x)*sqrt(d + e*x))` | $\frac{A + B x}{\sqrt{a + b x} \sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)/(sqrt(a + b*x)*(d + e*x)**(3/2))` | $\frac{A + B x}{\sqrt{a + b x} \left(d + e x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(sqrt(a + b*x)*(d + e*x)**(5/2))` | $\frac{A + B x}{\sqrt{a + b x} \left(d + e x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(sqrt(a + b*x)*(d + e*x)**(7/2))` | $\frac{A + B x}{\sqrt{a + b x} \left(d + e x\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(sqrt(a + b*x)*(d + e*x)**(9/2))` | $\frac{A + B x}{\sqrt{a + b x} \left(d + e x\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(sqrt(a + b*x)*(d + e*x)**(11/2))` | $\frac{A + B x}{\sqrt{a + b x} \left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a + b*x)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a + b*x)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a + b*x)**(3/2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((a + b*x)**(3/2)*sqrt(d + e*x))` | $\frac{A + B x}{\left(a + b x\right)^{\frac{3}{2}} \sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/((a + b*x)**(3/2)*(d + e*x)**(3/2))` | $\frac{A + B x}{\left(a + b x\right)^{\frac{3}{2}} \left(d + e x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/((a + b*x)**(3/2)*(d + e*x)**(5/2))` | $\frac{A + B x}{\left(a + b x\right)^{\frac{3}{2}} \left(d + e x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/((a + b*x)**(3/2)*(d + e*x)**(7/2))` | $\frac{A + B x}{\left(a + b x\right)^{\frac{3}{2}} \left(d + e x\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/((a + b*x)**(3/2)*(d + e*x)**(9/2))` | $\frac{A + B x}{\left(a + b x\right)^{\frac{3}{2}} \left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(a + b*x)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a + b*x)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a + b*x)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a + b*x)**(5/2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/((a + b*x)**(5/2)*sqrt(d + e*x))` | $\frac{A + B x}{\left(a + b x\right)^{\frac{5}{2}} \sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/((a + b*x)**(5/2)*(d + e*x)**(3/2))` | $\frac{A + B x}{\left(a + b x\right)^{\frac{5}{2}} \left(d + e x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/((a + b*x)**(5/2)*(d + e*x)**(5/2))` | $\frac{A + B x}{\left(a + b x\right)^{\frac{5}{2}} \left(d + e x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/((a + b*x)**(5/2)*(d + e*x)**(7/2))` | $\frac{A + B x}{\left(a + b x\right)^{\frac{5}{2}} \left(d + e x\right)^{\frac{7}{2}}}$ |
| timeout | parametric | `(A + B*x)/((a + b*x)**(5/2)*(d + e*x)**(9/2))` | $\frac{A + B x}{\left(a + b x\right)^{\frac{5}{2}} \left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**4*sqrt(5*x + 3)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{4} \sqrt{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**3*sqrt(5*x + 3)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{3} \sqrt{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**2*sqrt(5*x + 3)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{2} \sqrt{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)*sqrt(5*x + 3)` | $\sqrt{1 - 2 x} \left(3 x + 2\right) \sqrt{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)` | $\sqrt{1 - 2 x} \sqrt{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)/(3*x + 2)` | $\frac{\sqrt{1 - 2 x} \sqrt{5 x + 3}}{3 x + 2}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)/(3*x + 2)**2` | $\frac{\sqrt{1 - 2 x} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)/(3*x + 2)**3` | $\frac{\sqrt{1 - 2 x} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)/(3*x + 2)**4` | $\frac{\sqrt{1 - 2 x} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)/(3*x + 2)**5` | $\frac{\sqrt{1 - 2 x} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)/(3*x + 2)**6` | $\frac{\sqrt{1 - 2 x} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)/(3*x + 2)**7` | $\frac{\sqrt{1 - 2 x} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{7}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**4*(5*x + 3)**(3/2)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**3*(5*x + 3)**(3/2)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**2*(5*x + 3)**(3/2)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)*(5*x + 3)**(3/2)` | $\sqrt{1 - 2 x} \left(3 x + 2\right) \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)` | $\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/(3*x + 2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{3 x + 2}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/(3*x + 2)**2` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/(3*x + 2)**3` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/(3*x + 2)**4` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/(3*x + 2)**5` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/(3*x + 2)**6` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/(3*x + 2)**7` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{7}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**4*(5*x + 3)**(5/2)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**3*(5*x + 3)**(5/2)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**2*(5*x + 3)**(5/2)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)*(5*x + 3)**(5/2)` | $\sqrt{1 - 2 x} \left(3 x + 2\right) \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)` | $\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{3 x + 2}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**2` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**3` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**4` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**5` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**6` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**7` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{7}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**8` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{8}}$ |
| timeout | parametric | `sqrt(a + b*x)/(sqrt(c + d*x)*(e + f*x))` | $\frac{\sqrt{a + b x}}{\sqrt{c + d x} \left(e + f x\right)}$ |
| timeout | parametric | `sqrt(c + d*x)/(sqrt(a + b*x)*(e + f*x))` | $\frac{\sqrt{c + d x}}{\sqrt{a + b x} \left(e + f x\right)}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**3/sqrt(5*x + 3)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**2/sqrt(5*x + 3)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)/sqrt(5*x + 3)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)}{\sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/sqrt(5*x + 3)` | $\frac{\sqrt{1 - 2 x}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)*sqrt(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right) \sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**2*sqrt(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{2} \sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**3*sqrt(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{3} \sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**4*sqrt(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{4} \sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**5*sqrt(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{5} \sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**3/(5*x + 3)**(3/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**2/(5*x + 3)**(3/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)/(5*x + 3)**(3/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/(5*x + 3)**(3/2)` | $\frac{\sqrt{1 - 2 x}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)*(5*x + 3)**(3/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right) \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**2*(5*x + 3)**(3/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**3*(5*x + 3)**(3/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**4*(5*x + 3)**(3/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**4/(5*x + 3)**(5/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**3/(5*x + 3)**(5/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**2/(5*x + 3)**(5/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)/(5*x + 3)**(5/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `sqrt(1 - 2*x)/(5*x + 3)**(5/2)` | $\frac{\sqrt{1 - 2 x}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)*(5*x + 3)**(5/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right) \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**2*(5*x + 3)**(5/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**3*(5*x + 3)**(5/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**4*(5*x + 3)**(5/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**3*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3} \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**2*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2} \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right) \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)/(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{3 x + 2}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)/(3*x + 2)**2` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)/(3*x + 2)**3` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)/(3*x + 2)**4` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)/(3*x + 2)**5` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)/(3*x + 2)**6` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**3*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**2*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{3 x + 2}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**2` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**3` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**4` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**5` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**6` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**7` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{7}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**8` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{8}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**3*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**2*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{3 x + 2}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**2` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**3` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**4` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**5` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**6` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**7` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{7}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**8` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{8}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**3/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**2/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right) \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**2*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{2} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**3*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{3} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**4*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{4} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**5*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{5} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**6*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{6} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**3/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**2/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right) \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**2*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**3*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**4*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**5*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{5} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**3/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**2/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right) \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**2*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**3*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**4*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**3*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3} \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**2*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2} \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right) \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{3 x + 2}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)**2` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)**3` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)**4` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)**5` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)**6` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)**7` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{7}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**3*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**2*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{3 x + 2}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**2` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**3` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**4` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**5` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**6` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**7` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{7}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**8` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{8}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**3*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**2*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{3 x + 2}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**2` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**3` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**4` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**5` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**6` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**7` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{7}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**8` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{8}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**9` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{9}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**4/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**3/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**2/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right) \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**2*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{2} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**3*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{3} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**4*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{4} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**5*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{5} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**6*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{6} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**7*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{7} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**4/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**3/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**2/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right) \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**2*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**3*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**4*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**5*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{5} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**6*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{6} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**4/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**3/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**2/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right) \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**2*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**3*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**4*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**5*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{5} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**6*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{6} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**4*sqrt(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{4} \sqrt{5 x + 3}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(3*x + 2)**3*sqrt(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{3} \sqrt{5 x + 3}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(3*x + 2)**2*sqrt(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{2} \sqrt{5 x + 3}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(3*x + 2)*sqrt(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right) \sqrt{5 x + 3}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `sqrt(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\sqrt{5 x + 3}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `sqrt(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2))` | $\frac{\sqrt{5 x + 3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)}$ |
| partial | concrete | `sqrt(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2)**2)` | $\frac{\sqrt{5 x + 3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `sqrt(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2)**3)` | $\frac{\sqrt{5 x + 3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `sqrt(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2)**4)` | $\frac{\sqrt{5 x + 3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `sqrt(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2)**5)` | $\frac{\sqrt{5 x + 3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(3*x + 2)**3*(5*x + 3)**(3/2)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(3*x + 2)**2*(5*x + 3)**(3/2)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(3*x + 2)*(5*x + 3)**(3/2)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/sqrt(1 - 2*x)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/(sqrt(1 - 2*x)*(3*x + 2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)**(3/2)/(sqrt(1 - 2*x)*(3*x + 2)**2)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/(sqrt(1 - 2*x)*(3*x + 2)**3)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/(sqrt(1 - 2*x)*(3*x + 2)**4)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/(sqrt(1 - 2*x)*(3*x + 2)**5)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/(sqrt(1 - 2*x)*(3*x + 2)**6)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(3*x + 2)**3*(5*x + 3)**(5/2)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(3*x + 2)**2*(5*x + 3)**(5/2)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(3*x + 2)*(5*x + 3)**(5/2)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/sqrt(1 - 2*x)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2)**2)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2)**3)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2)**4)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2)**5)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2)**6)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2)**7)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{7}}$ |
| partial | concrete | `(3*x + 2)**4/(sqrt(1 - 2*x)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{4}}{\sqrt{1 - 2 x} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**3/(sqrt(1 - 2*x)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{3}}{\sqrt{1 - 2 x} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**2/(sqrt(1 - 2*x)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{2}}{\sqrt{1 - 2 x} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)/(sqrt(1 - 2*x)*sqrt(5*x + 3))` | $\frac{3 x + 2}{\sqrt{1 - 2 x} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*sqrt(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)*sqrt(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right) \sqrt{5 x + 3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**2*sqrt(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**3*sqrt(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**4*sqrt(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**4/(sqrt(1 - 2*x)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{4}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**3/(sqrt(1 - 2*x)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{3}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**2/(sqrt(1 - 2*x)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{2}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)/(sqrt(1 - 2*x)*(5*x + 3)**(3/2))` | $\frac{3 x + 2}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/(sqrt(1 - 2*x)*(5*x + 3)**(3/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)*(5*x + 3)**(3/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right) \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**2*(5*x + 3)**(3/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**3*(5*x + 3)**(3/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**4*(5*x + 3)**(3/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**5/(sqrt(1 - 2*x)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{5}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**4/(sqrt(1 - 2*x)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{4}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**3/(sqrt(1 - 2*x)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{3}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**2/(sqrt(1 - 2*x)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{2}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | concrete | `(3*x + 2)/(sqrt(1 - 2*x)*(5*x + 3)**(5/2))` | $\frac{3 x + 2}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `1/(sqrt(1 - 2*x)*(5*x + 3)**(5/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)*(5*x + 3)**(5/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right) \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**2*(5*x + 3)**(5/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**3*(5*x + 3)**(5/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**4*(5*x + 3)**(5/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*(e + f*x)*sqrt(-a*f + 2*b*e + b*f*x))` | $\frac{1}{\sqrt{a + b x} \left(e + f x\right) \sqrt{- a f + 2 b e + b f x}}$ |
| partial | concrete | `(3*x + 2)**5*sqrt(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{5} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**4*sqrt(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{4} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**3*sqrt(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{3} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**2*sqrt(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{2} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)*sqrt(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right) \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2))` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2)**2)` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2)**3)` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2)**4)` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2)**5)` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(3*x + 2)**4*(5*x + 3)**(3/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**3*(5*x + 3)**(3/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**2*(5*x + 3)**(3/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)*(5*x + 3)**(3/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/(1 - 2*x)**(3/2)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(3/2)*(3*x + 2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(3/2)*(3*x + 2)**2)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(3/2)*(3*x + 2)**3)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(3/2)*(3*x + 2)**4)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(3/2)*(3*x + 2)**5)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(3*x + 2)**4*(5*x + 3)**(5/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**3*(5*x + 3)**(5/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**2*(5*x + 3)**(5/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)*(5*x + 3)**(5/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(1 - 2*x)**(3/2)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(3/2)*(3*x + 2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(3/2)*(3*x + 2)**2)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(3/2)*(3*x + 2)**3)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(3/2)*(3*x + 2)**4)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(3/2)*(3*x + 2)**5)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(3/2)*(3*x + 2)**6)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{6}}$ |
| partial | concrete | `(3*x + 2)**5/((1 - 2*x)**(3/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{5}}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**4/((1 - 2*x)**(3/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{4}}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**3/((1 - 2*x)**(3/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**2/((1 - 2*x)**(3/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)/((1 - 2*x)**(3/2)*sqrt(5*x + 3))` | $\frac{3 x + 2}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| SOLVED-both | concrete | `1/((1 - 2*x)**(3/2)*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right) \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**2*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**3*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**4*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**5*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{5} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**5/((1 - 2*x)**(3/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{5}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**4/((1 - 2*x)**(3/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{4}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**3/((1 - 2*x)**(3/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**2/((1 - 2*x)**(3/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | concrete | `(3*x + 2)/((1 - 2*x)**(3/2)*(5*x + 3)**(3/2))` | $\frac{3 x + 2}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/((1 - 2*x)**(3/2)*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**2*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**3*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**4*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**5/((1 - 2*x)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{5}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**4/((1 - 2*x)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{4}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**3/((1 - 2*x)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | concrete | `(3*x + 2)**2/((1 - 2*x)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | concrete | `(3*x + 2)/((1 - 2*x)**(3/2)*(5*x + 3)**(5/2))` | $\frac{3 x + 2}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `1/((1 - 2*x)**(3/2)*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**2*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**3*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**4*sqrt(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{4} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**3*sqrt(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{3} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**2*sqrt(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{2} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)*sqrt(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right) \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `sqrt(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(5/2)*(3*x + 2))` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(5/2)*(3*x + 2)**2)` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(5/2)*(3*x + 2)**3)` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(5/2)*(3*x + 2)**4)` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(3*x + 2)**4*(5*x + 3)**(3/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**3*(5*x + 3)**(3/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**2*(5*x + 3)**(3/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)*(5*x + 3)**(3/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/(1 - 2*x)**(5/2)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(5/2)*(3*x + 2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(5/2)*(3*x + 2)**2)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(5/2)*(3*x + 2)**3)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(5/2)*(3*x + 2)**4)` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(3*x + 2)**4*(5*x + 3)**(5/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{4} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**3*(5*x + 3)**(5/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**2*(5*x + 3)**(5/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)*(5*x + 3)**(5/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right) \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(1 - 2*x)**(5/2)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(5/2)*(3*x + 2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(5/2)*(3*x + 2)**2)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(5/2)*(3*x + 2)**3)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(5/2)*(3*x + 2)**4)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(5/2)*(3*x + 2)**5)` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{5}}$ |
| partial | concrete | `(3*x + 2)**5/((1 - 2*x)**(5/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{5}}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**4/((1 - 2*x)**(5/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{4}}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**3/((1 - 2*x)**(5/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**2/((1 - 2*x)**(5/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| **SOLVED-NEW** | concrete | `(3*x + 2)/((1 - 2*x)**(5/2)*sqrt(5*x + 3))` | $\frac{3 x + 2}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| SOLVED-both | concrete | `1/((1 - 2*x)**(5/2)*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right) \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**2*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**3*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**4*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{4} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**5/((1 - 2*x)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{5}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**4/((1 - 2*x)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{4}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**3/((1 - 2*x)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | concrete | `(3*x + 2)**2/((1 - 2*x)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | concrete | `(3*x + 2)/((1 - 2*x)**(5/2)*(5*x + 3)**(3/2))` | $\frac{3 x + 2}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/((1 - 2*x)**(5/2)*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**2*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**3*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(3*x + 2)**6/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{6}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**5/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{5}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**4/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{4}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | concrete | `(3*x + 2)**3/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | concrete | `(3*x + 2)**2/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | concrete | `(3*x + 2)/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{3 x + 2}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `1/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right) \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**2*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{2} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**3*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{3} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(a + b*x)*sqrt(c + b*x*(c - 1)/a)*sqrt(e + b*x*(e - 1)/a))` | $\frac{1}{\sqrt{a + b x} \sqrt{c + \frac{b x \left(c - 1\right)}{a}} \sqrt{e + \frac{b x \left(e - 1\right)}{a}}}$ |
| timeout | parametric | `1/(sqrt(a + b*x)*sqrt(c + d*x)*sqrt(e + b*x*(e - 1)/a))` | $\frac{1}{\sqrt{a + b x} \sqrt{c + d x} \sqrt{e + \frac{b x \left(e - 1\right)}{a}}}$ |
| timeout | parametric | `1/(sqrt(a + b*x)*sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{1}{\sqrt{a + b x} \sqrt{c + d x} \sqrt{e + f x}}$ |
| partial | parametric | `sqrt(e + b*x*(e - 1)/a)/(sqrt(a + b*x)*sqrt(c + b*x*(c - 1)/a))` | $\frac{\sqrt{e + \frac{b x \left(e - 1\right)}{a}}}{\sqrt{a + b x} \sqrt{c + \frac{b x \left(c - 1\right)}{a}}}$ |
| timeout | parametric | `sqrt(c + d*x)/(sqrt(a + b*x)*sqrt(e + b*x*(e - 1)/a))` | $\frac{\sqrt{c + d x}}{\sqrt{a + b x} \sqrt{e + \frac{b x \left(e - 1\right)}{a}}}$ |
| partial | parametric | `sqrt(a + b*x)/(sqrt(c + b*x*(c - 1)/a)*sqrt(e + b*x*(e - 1)/a))` | $\frac{\sqrt{a + b x}}{\sqrt{c + \frac{b x \left(c - 1\right)}{a}} \sqrt{e + \frac{b x \left(e - 1\right)}{a}}}$ |
| timeout | parametric | `sqrt(e + f*x)/(sqrt(a + b*x)*sqrt(c + d*x))` | $\frac{\sqrt{e + f x}}{\sqrt{a + b x} \sqrt{c + d x}}$ |
| partial | parametric | `1/(sqrt(-c + d*x)*sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{1}{\sqrt{- c + d x} \sqrt{c + d x} \sqrt{e + f x}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(5/2)*sqrt(5*x + 3)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{5}{2}} \sqrt{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(3/2)*sqrt(5*x + 3)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{3}{2}} \sqrt{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(3*x + 2)*sqrt(5*x + 3)` | $\sqrt{1 - 2 x} \sqrt{3 x + 2} \sqrt{5 x + 3}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)/sqrt(3*x + 2)` | $\frac{\sqrt{1 - 2 x} \sqrt{5 x + 3}}{\sqrt{3 x + 2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)/(3*x + 2)**(3/2)` | $\frac{\sqrt{1 - 2 x} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)/(3*x + 2)**(5/2)` | $\frac{\sqrt{1 - 2 x} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)/(3*x + 2)**(7/2)` | $\frac{\sqrt{1 - 2 x} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `sqrt(1 - 2*x)*sqrt(5*x + 3)/(3*x + 2)**(9/2)` | $\frac{\sqrt{1 - 2 x} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{9}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(5/2)*(5*x + 3)**(3/2)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(3/2)*(5*x + 3)**(3/2)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(3*x + 2)*(5*x + 3)**(3/2)` | $\sqrt{1 - 2 x} \sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/sqrt(3*x + 2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{3 x + 2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/(3*x + 2)**(3/2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/(3*x + 2)**(5/2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/(3*x + 2)**(7/2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/(3*x + 2)**(9/2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(3/2)/(3*x + 2)**(11/2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{11}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(5/2)*(5*x + 3)**(5/2)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(3/2)*(5*x + 3)**(5/2)` | $\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(3*x + 2)*(5*x + 3)**(5/2)` | $\sqrt{1 - 2 x} \sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/sqrt(3*x + 2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{3 x + 2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**(3/2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**(5/2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**(7/2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**(9/2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**(11/2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{11}{2}}}$ |
| timeout | concrete | `sqrt(1 - 2*x)*(5*x + 3)**(5/2)/(3*x + 2)**(13/2)` | $\frac{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{13}{2}}}$ |
| timeout | parametric | `sqrt(e + f*x)/(sqrt(a + b*x)*sqrt(c + d*x))` | $\frac{\sqrt{e + f x}}{\sqrt{a + b x} \sqrt{c + d x}}$ |
| timeout | parametric | `sqrt(e + f*x)/((a + b*x)**(3/2)*sqrt(c + d*x))` | $\frac{\sqrt{e + f x}}{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x}}$ |
| partial | concrete | `sqrt(1 - 2*x)/(sqrt(-5*x - 3)*sqrt(3*x + 2))` | $\frac{\sqrt{1 - 2 x}}{\sqrt{- 5 x - 3} \sqrt{3 x + 2}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(5/2)/sqrt(5*x + 3)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{5}{2}}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(3/2)/sqrt(5*x + 3)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{3}{2}}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(3*x + 2)/sqrt(5*x + 3)` | $\frac{\sqrt{1 - 2 x} \sqrt{3 x + 2}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/(sqrt(3*x + 2)*sqrt(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\sqrt{3 x + 2} \sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**(3/2)*sqrt(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**(5/2)*sqrt(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**(7/2)*sqrt(5*x + 3))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{\frac{7}{2}} \sqrt{5 x + 3}}$ |
| timeout | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(7/2)/(5*x + 3)**(3/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{7}{2}}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(5/2)/(5*x + 3)**(3/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{5}{2}}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(3/2)/(5*x + 3)**(3/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{3}{2}}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(3*x + 2)/(5*x + 3)**(3/2)` | $\frac{\sqrt{1 - 2 x} \sqrt{3 x + 2}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/(sqrt(3*x + 2)*(5*x + 3)**(3/2))` | $\frac{\sqrt{1 - 2 x}}{\sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**(3/2)*(5*x + 3)**(3/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**(7/2)*(5*x + 3)**(3/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(9/2)/(5*x + 3)**(5/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{9}{2}}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(7/2)/(5*x + 3)**(5/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{7}{2}}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(5/2)/(5*x + 3)**(5/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{5}{2}}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*(3*x + 2)**(3/2)/(5*x + 3)**(5/2)` | $\frac{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{3}{2}}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)*sqrt(3*x + 2)/(5*x + 3)**(5/2)` | $\frac{\sqrt{1 - 2 x} \sqrt{3 x + 2}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/(sqrt(3*x + 2)*(5*x + 3)**(5/2))` | $\frac{\sqrt{1 - 2 x}}{\sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(1 - 2*x)/((3*x + 2)**(7/2)*(5*x + 3)**(5/2))` | $\frac{\sqrt{1 - 2 x}}{\left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(5/2)*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{5}{2}} \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(3/2)*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{3}{2}} \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(3*x + 2)*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{3 x + 2} \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)/sqrt(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\sqrt{3 x + 2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)/(3*x + 2)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)/(3*x + 2)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)/(3*x + 2)**(7/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)/(3*x + 2)**(9/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*sqrt(5*x + 3)/(3*x + 2)**(11/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{11}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(5/2)*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(3/2)*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(3*x + 2)*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/sqrt(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{3 x + 2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**(7/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**(9/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**(11/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{11}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(3/2)/(3*x + 2)**(13/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{13}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(5/2)*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(3/2)*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(3*x + 2)*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/sqrt(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{3 x + 2}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**(7/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**(9/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**(11/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{11}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**(13/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{13}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(5*x + 3)**(5/2)/(3*x + 2)**(15/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{15}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(5/2)/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{5}{2}}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(3/2)/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{3}{2}}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(3*x + 2)/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{3 x + 2}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/(sqrt(3*x + 2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\sqrt{3 x + 2} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**(3/2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**(5/2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**(7/2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{7}{2}} \sqrt{5 x + 3}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**(9/2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{9}{2}} \sqrt{5 x + 3}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(7/2)/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{7}{2}}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(5/2)/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{5}{2}}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(3/2)/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{3}{2}}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(3*x + 2)/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{3 x + 2}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/(sqrt(3*x + 2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**(3/2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**(7/2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**(9/2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{9}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(7/2)/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{7}{2}}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(5/2)/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{5}{2}}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*(3*x + 2)**(3/2)/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{3}{2}}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)*sqrt(3*x + 2)/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{3 x + 2}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/(sqrt(3*x + 2)*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(3/2)/((3*x + 2)**(7/2)*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(5/2)*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{5}{2}} \sqrt{5 x + 3}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(3/2)*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{3}{2}} \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(3*x + 2)*sqrt(5*x + 3)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{3 x + 2} \sqrt{5 x + 3}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/sqrt(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\sqrt{3 x + 2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)**(7/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)**(9/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)**(11/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{11}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*sqrt(5*x + 3)/(3*x + 2)**(13/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(3 x + 2\right)^{\frac{13}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(5/2)*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(3/2)*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(3*x + 2)*(5*x + 3)**(3/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/sqrt(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{3 x + 2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**(7/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**(9/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**(11/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{11}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**(13/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{13}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(3/2)/(3*x + 2)**(15/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(3 x + 2\right)^{\frac{15}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(3/2)*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(3*x + 2)*(5*x + 3)**(5/2)` | $\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{5}{2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/sqrt(3*x + 2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{3 x + 2}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**(7/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**(9/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**(11/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{11}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**(13/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{13}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**(15/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{15}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(5*x + 3)**(5/2)/(3*x + 2)**(17/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{17}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(5/2)/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{5}{2}}}{\sqrt{5 x + 3}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(3/2)/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{3}{2}}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(3*x + 2)/sqrt(5*x + 3)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{3 x + 2}}{\sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/(sqrt(3*x + 2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\sqrt{3 x + 2} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(3/2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(5/2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(7/2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{7}{2}} \sqrt{5 x + 3}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(9/2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{9}{2}} \sqrt{5 x + 3}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(11/2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{11}{2}} \sqrt{5 x + 3}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(13/2)*sqrt(5*x + 3))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{13}{2}} \sqrt{5 x + 3}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(7/2)/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{7}{2}}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(5/2)/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{5}{2}}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(3/2)/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{3}{2}}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(3*x + 2)/(5*x + 3)**(3/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{3 x + 2}}{\left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/(sqrt(3*x + 2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(3/2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(7/2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(9/2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{9}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(11/2)*(5*x + 3)**(3/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{11}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(7/2)/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{7}{2}}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(5/2)/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{5}{2}}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)*(3*x + 2)**(3/2)/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{3}{2}}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)*sqrt(3*x + 2)/(5*x + 3)**(5/2)` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{3 x + 2}}{\left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/(sqrt(3*x + 2)*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(7/2)*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(1 - 2*x)**(5/2)/((3*x + 2)**(9/2)*(5*x + 3)**(5/2))` | $\frac{\left(1 - 2 x\right)^{\frac{5}{2}}}{\left(3 x + 2\right)^{\frac{9}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)*sqrt(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(3*x + 2)**(3/2)*sqrt(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `sqrt(3*x + 2)*sqrt(5*x + 3)/sqrt(1 - 2*x)` | $\frac{\sqrt{3 x + 2} \sqrt{5 x + 3}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `sqrt(5*x + 3)/(sqrt(1 - 2*x)*sqrt(3*x + 2))` | $\frac{\sqrt{5 x + 3}}{\sqrt{1 - 2 x} \sqrt{3 x + 2}}$ |
| partial | concrete | `sqrt(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2)**(3/2))` | $\frac{\sqrt{5 x + 3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2)**(5/2))` | $\frac{\sqrt{5 x + 3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(5*x + 3)/(sqrt(1 - 2*x)*(3*x + 2)**(7/2))` | $\frac{\sqrt{5 x + 3}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{7}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)*(5*x + 3)**(3/2)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(3*x + 2)**(3/2)*(5*x + 3)**(3/2)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `sqrt(3*x + 2)*(5*x + 3)**(3/2)/sqrt(1 - 2*x)` | $\frac{\sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/(sqrt(1 - 2*x)*sqrt(3*x + 2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \sqrt{3 x + 2}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/(sqrt(1 - 2*x)*(3*x + 2)**(3/2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/(sqrt(1 - 2*x)*(3*x + 2)**(5/2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/(sqrt(1 - 2*x)*(3*x + 2)**(7/2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(5*x + 3)**(3/2)/(sqrt(1 - 2*x)*(3*x + 2)**(9/2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)*(5*x + 3)**(5/2)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(3*x + 2)**(5/2)*(5*x + 3)**(5/2)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(3*x + 2)**(3/2)*(5*x + 3)**(5/2)/sqrt(1 - 2*x)` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `sqrt(3*x + 2)*(5*x + 3)**(5/2)/sqrt(1 - 2*x)` | $\frac{\sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*sqrt(3*x + 2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \sqrt{3 x + 2}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2)**(3/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2)**(5/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2)**(7/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2)**(9/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2)**(11/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{11}{2}}}$ |
| timeout | concrete | `(5*x + 3)**(5/2)/(sqrt(1 - 2*x)*(3*x + 2)**(13/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{13}{2}}}$ |
| partial | concrete | `1/(sqrt(x + 1)*sqrt(x + 2)*sqrt(x + 3))` | $\frac{1}{\sqrt{x + 1} \sqrt{x + 2} \sqrt{x + 3}}$ |
| partial | concrete | `1/(sqrt(3 - x)*sqrt(x + 1)*sqrt(x + 2))` | $\frac{1}{\sqrt{3 - x} \sqrt{x + 1} \sqrt{x + 2}}$ |
| partial | concrete | `1/(sqrt(2 - x)*sqrt(x + 1)*sqrt(x + 3))` | $\frac{1}{\sqrt{2 - x} \sqrt{x + 1} \sqrt{x + 3}}$ |
| partial | concrete | `1/(sqrt(2 - x)*sqrt(3 - x)*sqrt(x + 1))` | $\frac{1}{\sqrt{2 - x} \sqrt{3 - x} \sqrt{x + 1}}$ |
| partial | concrete | `1/(sqrt(1 - x)*sqrt(x + 2)*sqrt(x + 3))` | $\frac{1}{\sqrt{1 - x} \sqrt{x + 2} \sqrt{x + 3}}$ |
| partial | concrete | `1/(sqrt(1 - x)*sqrt(3 - x)*sqrt(x + 2))` | $\frac{1}{\sqrt{1 - x} \sqrt{3 - x} \sqrt{x + 2}}$ |
| partial | concrete | `1/(sqrt(1 - x)*sqrt(2 - x)*sqrt(x + 3))` | $\frac{1}{\sqrt{1 - x} \sqrt{2 - x} \sqrt{x + 3}}$ |
| partial | concrete | `1/(sqrt(1 - x)*sqrt(2 - x)*sqrt(3 - x))` | $\frac{1}{\sqrt{1 - x} \sqrt{2 - x} \sqrt{3 - x}}$ |
| partial | concrete | `1/(sqrt(x - 3)*sqrt(x - 2)*sqrt(x - 1))` | $\frac{1}{\sqrt{x - 3} \sqrt{x - 2} \sqrt{x - 1}}$ |
| partial | concrete | `1/(sqrt(-x - 2)*sqrt(x - 3)*sqrt(x - 1))` | $\frac{1}{\sqrt{- x - 2} \sqrt{x - 3} \sqrt{x - 1}}$ |
| partial | concrete | `1/(sqrt(-x - 1)*sqrt(x - 3)*sqrt(x - 2))` | $\frac{1}{\sqrt{- x - 1} \sqrt{x - 3} \sqrt{x - 2}}$ |
| partial | concrete | `1/(sqrt(-x - 3)*sqrt(-x - 1)*sqrt(x - 2))` | $\frac{1}{\sqrt{- x - 3} \sqrt{- x - 1} \sqrt{x - 2}}$ |
| partial | concrete | `1/(sqrt(-x - 2)*sqrt(-x - 1)*sqrt(x - 3))` | $\frac{1}{\sqrt{- x - 2} \sqrt{- x - 1} \sqrt{x - 3}}$ |
| partial | concrete | `1/(sqrt(-x - 3)*sqrt(-x - 2)*sqrt(-x - 1))` | $\frac{1}{\sqrt{- x - 3} \sqrt{- x - 2} \sqrt{- x - 1}}$ |
| timeout | parametric | `1/((a + b*x)**(3/2)*sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | parametric | `1/((a + b*x)**(5/2)*sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{1}{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)/(sqrt(1 - 2*x)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}}}{\sqrt{1 - 2 x} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**(5/2)/(sqrt(1 - 2*x)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**(3/2)/(sqrt(1 - 2*x)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(3*x + 2)/(sqrt(1 - 2*x)*sqrt(5*x + 3))` | $\frac{\sqrt{3 x + 2}}{\sqrt{1 - 2 x} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*sqrt(3*x + 2)*sqrt(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \sqrt{3 x + 2} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**(3/2)*sqrt(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**(5/2)*sqrt(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**(7/2)*sqrt(5*x + 3))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{7}{2}} \sqrt{5 x + 3}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)/(sqrt(1 - 2*x)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)/(sqrt(1 - 2*x)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**(3/2)/(sqrt(1 - 2*x)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(3*x + 2)/(sqrt(1 - 2*x)*(5*x + 3)**(3/2))` | $\frac{\sqrt{3 x + 2}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*sqrt(3*x + 2)*(5*x + 3)**(3/2))` | $\frac{1}{\sqrt{1 - 2 x} \sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**(3/2)*(5*x + 3)**(3/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**(5/2)*(5*x + 3)**(3/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**(7/2)*(5*x + 3)**(3/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(9/2)/(sqrt(1 - 2*x)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{9}{2}}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)/(sqrt(1 - 2*x)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)/(sqrt(1 - 2*x)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(3/2)/(sqrt(1 - 2*x)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(3*x + 2)/(sqrt(1 - 2*x)*(5*x + 3)**(5/2))` | $\frac{\sqrt{3 x + 2}}{\sqrt{1 - 2 x} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*sqrt(3*x + 2)*(5*x + 3)**(5/2))` | $\frac{1}{\sqrt{1 - 2 x} \sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**(3/2)*(5*x + 3)**(5/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**(5/2)*(5*x + 3)**(5/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - 2*x)*(3*x + 2)**(7/2)*(5*x + 3)**(5/2))` | $\frac{1}{\sqrt{1 - 2 x} \left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(x)/(sqrt(a + 2*x)*sqrt(c + 2*x))` | $\frac{\sqrt{x}}{\sqrt{a + 2 x} \sqrt{c + 2 x}}$ |
| partial | concrete | `1/(sqrt(4 - x)*sqrt(5 - x)*sqrt(x - 3))` | $\frac{1}{\sqrt{4 - x} \sqrt{5 - x} \sqrt{x - 3}}$ |
| partial | concrete | `1/(sqrt((5 - x)*(x - 3))*sqrt(4 - x))` | $\frac{1}{\sqrt{\left(5 - x\right) \left(x - 3\right)} \sqrt{4 - x}}$ |
| partial | concrete | `1/(sqrt(4 - x)*sqrt(-x**2 + 8*x - 15))` | $\frac{1}{\sqrt{4 - x} \sqrt{- x^{2} + 8 x - 15}}$ |
| partial | concrete | `1/(sqrt(6 - x)*sqrt(x - 2)*sqrt(x - 1))` | $\frac{1}{\sqrt{6 - x} \sqrt{x - 2} \sqrt{x - 1}}$ |
| partial | concrete | `1/(sqrt((6 - x)*(x - 2))*sqrt(x - 1))` | $\frac{1}{\sqrt{\left(6 - x\right) \left(x - 2\right)} \sqrt{x - 1}}$ |
| partial | concrete | `1/(sqrt(x - 1)*sqrt(-x**2 + 8*x - 12))` | $\frac{1}{\sqrt{x - 1} \sqrt{- x^{2} + 8 x - 12}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)*sqrt(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)*sqrt(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**(3/2)*sqrt(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(3*x + 2)*sqrt(5*x + 3)/(1 - 2*x)**(3/2)` | $\frac{\sqrt{3 x + 2} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(3/2)*sqrt(3*x + 2))` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{3 x + 2}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2)**(3/2))` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2)**(5/2))` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(3/2)*(3*x + 2)**(7/2))` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)*(5*x + 3)**(3/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)*(5*x + 3)**(3/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**(3/2)*(5*x + 3)**(3/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(3*x + 2)*(5*x + 3)**(3/2)/(1 - 2*x)**(3/2)` | $\frac{\sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(3/2)*sqrt(3*x + 2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{3 x + 2}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(3/2)*(3*x + 2)**(3/2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(3/2)*(3*x + 2)**(5/2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(3/2)*(3*x + 2)**(7/2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(3/2)*(3*x + 2)**(9/2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)*(5*x + 3)**(5/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)*(5*x + 3)**(5/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**(3/2)*(5*x + 3)**(5/2)/(1 - 2*x)**(3/2)` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(3*x + 2)*(5*x + 3)**(5/2)/(1 - 2*x)**(3/2)` | $\frac{\sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(3/2)*sqrt(3*x + 2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{3 x + 2}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(3/2)*(3*x + 2)**(3/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(3/2)*(3*x + 2)**(5/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(3/2)*(3*x + 2)**(7/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(3/2)*(3*x + 2)**(9/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(3/2)*(3*x + 2)**(11/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{11}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)/((1 - 2*x)**(3/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**(5/2)/((1 - 2*x)**(3/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**(3/2)/((1 - 2*x)**(3/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(3*x + 2)/((1 - 2*x)**(3/2)*sqrt(5*x + 3))` | $\frac{\sqrt{3 x + 2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*sqrt(3*x + 2)*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{3 x + 2} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**(3/2)*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**(5/2)*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**(7/2)*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{7}{2}} \sqrt{5 x + 3}}$ |
| timeout | concrete | `(3*x + 2)**(9/2)/((1 - 2*x)**(3/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{\frac{9}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)/((1 - 2*x)**(3/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)/((1 - 2*x)**(3/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**(3/2)/((1 - 2*x)**(3/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(3*x + 2)/((1 - 2*x)**(3/2)*(5*x + 3)**(3/2))` | $\frac{\sqrt{3 x + 2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*sqrt(3*x + 2)*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**(3/2)*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**(5/2)*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**(7/2)*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(11/2)/((1 - 2*x)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{11}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(9/2)/((1 - 2*x)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{9}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)/((1 - 2*x)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)/((1 - 2*x)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(3/2)/((1 - 2*x)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(3*x + 2)/((1 - 2*x)**(3/2)*(5*x + 3)**(5/2))` | $\frac{\sqrt{3 x + 2}}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*sqrt(3*x + 2)*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**(3/2)*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**(5/2)*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(3/2)*(3*x + 2)**(7/2)*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{3}{2}} \left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(9/2)*sqrt(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{\frac{9}{2}} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)*sqrt(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)*sqrt(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(3/2)*sqrt(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(3*x + 2)*sqrt(5*x + 3)/(1 - 2*x)**(5/2)` | $\frac{\sqrt{3 x + 2} \sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(5/2)*sqrt(3*x + 2))` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{3 x + 2}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(5/2)*(3*x + 2)**(3/2))` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(5/2)*(3*x + 2)**(5/2))` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `sqrt(5*x + 3)/((1 - 2*x)**(5/2)*(3*x + 2)**(7/2))` | $\frac{\sqrt{5 x + 3}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)*(5*x + 3)**(3/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)*(5*x + 3)**(3/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(3/2)*(5*x + 3)**(3/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(3*x + 2)*(5*x + 3)**(3/2)/(1 - 2*x)**(5/2)` | $\frac{\sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(5/2)*sqrt(3*x + 2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{3 x + 2}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(5/2)*(3*x + 2)**(3/2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(5/2)*(3*x + 2)**(5/2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(5*x + 3)**(3/2)/((1 - 2*x)**(5/2)*(3*x + 2)**(7/2))` | $\frac{\left(5 x + 3\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)*(5*x + 3)**(5/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)*(5*x + 3)**(5/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(3/2)*(5*x + 3)**(5/2)/(1 - 2*x)**(5/2)` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(3*x + 2)*(5*x + 3)**(5/2)/(1 - 2*x)**(5/2)` | $\frac{\sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(5/2)*sqrt(3*x + 2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{3 x + 2}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(5/2)*(3*x + 2)**(3/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(5/2)*(3*x + 2)**(5/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(5/2)*(3*x + 2)**(7/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{7}{2}}}$ |
| timeout | concrete | `(5*x + 3)**(5/2)/((1 - 2*x)**(5/2)*(3*x + 2)**(9/2))` | $\frac{\left(5 x + 3\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{9}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(9/2)/((1 - 2*x)**(5/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{\frac{9}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)/((1 - 2*x)**(5/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**(5/2)/((1 - 2*x)**(5/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `(3*x + 2)**(3/2)/((1 - 2*x)**(5/2)*sqrt(5*x + 3))` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `sqrt(3*x + 2)/((1 - 2*x)**(5/2)*sqrt(5*x + 3))` | $\frac{\sqrt{3 x + 2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*sqrt(3*x + 2)*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{3 x + 2} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**(3/2)*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{3}{2}} \sqrt{5 x + 3}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**(5/2)*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{5}{2}} \sqrt{5 x + 3}}$ |
| timeout | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**(7/2)*sqrt(5*x + 3))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{7}{2}} \sqrt{5 x + 3}}$ |
| timeout | concrete | `(3*x + 2)**(11/2)/((1 - 2*x)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{\frac{11}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(9/2)/((1 - 2*x)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{\frac{9}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)/((1 - 2*x)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)/((1 - 2*x)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x + 2)**(3/2)/((1 - 2*x)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(3*x + 2)/((1 - 2*x)**(5/2)*(5*x + 3)**(3/2))` | $\frac{\sqrt{3 x + 2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*sqrt(3*x + 2)*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**(3/2)*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**(5/2)*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**(7/2)*(5*x + 3)**(3/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(13/2)/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{13}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(11/2)/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{11}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(9/2)/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{9}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `(3*x + 2)**(7/2)/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{7}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(5/2)/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{5}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(3*x + 2)**(3/2)/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\left(3 x + 2\right)^{\frac{3}{2}}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(3*x + 2)/((1 - 2*x)**(5/2)*(5*x + 3)**(5/2))` | $\frac{\sqrt{3 x + 2}}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*sqrt(3*x + 2)*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \sqrt{3 x + 2} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**(3/2)*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{3}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**(5/2)*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{5}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| timeout | concrete | `1/((1 - 2*x)**(5/2)*(3*x + 2)**(7/2)*(5*x + 3)**(5/2))` | $\frac{1}{\left(1 - 2 x\right)^{\frac{5}{2}} \left(3 x + 2\right)^{\frac{7}{2}} \left(5 x + 3\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)**(1/3)*(c + d*x)**(2/3)*(e + f*x)**2` | $\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}} \left(e + f x\right)^{2}$ |
| partial | parametric | `(a + b*x)**(1/3)*(c + d*x)**(2/3)*(e + f*x)` | $\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}} \left(e + f x\right)$ |
| partial | parametric | `(a + b*x)**(1/3)*(c + d*x)**(2/3)` | $\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}}$ |
| timeout | parametric | `(a + b*x)**(1/3)*(c + d*x)**(2/3)/(e + f*x)` | $\frac{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}}}{e + f x}$ |
| timeout | parametric | `(a + b*x)**(1/3)*(c + d*x)**(2/3)/(e + f*x)**2` | $\frac{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}}}{\left(e + f x\right)^{2}}$ |
| timeout | parametric | `(a + b*x)**(1/3)*(c + d*x)**(2/3)/(e + f*x)**3` | $\frac{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}}}{\left(e + f x\right)^{3}}$ |
| timeout | parametric | `(a + b*x)**(1/3)*(c + d*x)**(2/3)/(e + f*x)**4` | $\frac{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}}}{\left(e + f x\right)^{4}}$ |
| partial | parametric | `(a + b*x)**(1/3)*(e + f*x)**2/(c + d*x)**(1/3)` | $\frac{\sqrt[3]{a + b x} \left(e + f x\right)^{2}}{\sqrt[3]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(1/3)*(e + f*x)/(c + d*x)**(1/3)` | $\frac{\sqrt[3]{a + b x} \left(e + f x\right)}{\sqrt[3]{c + d x}}$ |
| partial | parametric | `(a + b*x)**(1/3)/(c + d*x)**(1/3)` | $\frac{\sqrt[3]{a + b x}}{\sqrt[3]{c + d x}}$ |
| timeout | parametric | `(a + b*x)**(1/3)/((c + d*x)**(1/3)*(e + f*x))` | $\frac{\sqrt[3]{a + b x}}{\sqrt[3]{c + d x} \left(e + f x\right)}$ |
| timeout | parametric | `(a + b*x)**(1/3)/((c + d*x)**(1/3)*(e + f*x)**2)` | $\frac{\sqrt[3]{a + b x}}{\sqrt[3]{c + d x} \left(e + f x\right)^{2}}$ |
| timeout | parametric | `(a + b*x)**(1/3)/((c + d*x)**(1/3)*(e + f*x)**3)` | $\frac{\sqrt[3]{a + b x}}{\sqrt[3]{c + d x} \left(e + f x\right)^{3}}$ |
| timeout | parametric | `(a + b*x)**(1/3)/((c + d*x)**(1/3)*(e + f*x)**4)` | $\frac{\sqrt[3]{a + b x}}{\sqrt[3]{c + d x} \left(e + f x\right)^{4}}$ |
| partial | parametric | `(e + f*x)**3/((a + b*x)**(1/3)*(c + d*x)**(2/3))` | $\frac{\left(e + f x\right)^{3}}{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(e + f*x)**2/((a + b*x)**(1/3)*(c + d*x)**(2/3))` | $\frac{\left(e + f x\right)^{2}}{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(e + f*x)/((a + b*x)**(1/3)*(c + d*x)**(2/3))` | $\frac{e + f x}{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((a + b*x)**(1/3)*(c + d*x)**(2/3))` | $\frac{1}{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}}}$ |
| timeout | parametric | `1/((a + b*x)**(1/3)*(c + d*x)**(2/3)*(e + f*x))` | $\frac{1}{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}} \left(e + f x\right)}$ |
| timeout | parametric | `1/((a + b*x)**(1/3)*(c + d*x)**(2/3)*(e + f*x)**2)` | $\frac{1}{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}} \left(e + f x\right)^{2}}$ |
| timeout | parametric | `1/((a + b*x)**(1/3)*(c + d*x)**(2/3)*(e + f*x)**3)` | $\frac{1}{\sqrt[3]{a + b x} \left(c + d x\right)^{\frac{2}{3}} \left(e + f x\right)^{3}}$ |
| partial | parametric | `(a + b*x)**3/((c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(1/3))` | $\frac{\left(a + b x\right)^{3}}{\sqrt[3]{c + d x} \sqrt[3]{a d + b c + 2 b d x}}$ |
| partial | parametric | `(a + b*x)**2/((c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(1/3))` | $\frac{\left(a + b x\right)^{2}}{\sqrt[3]{c + d x} \sqrt[3]{a d + b c + 2 b d x}}$ |
| partial | parametric | `(a + b*x)/((c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(1/3))` | $\frac{a + b x}{\sqrt[3]{c + d x} \sqrt[3]{a d + b c + 2 b d x}}$ |
| partial | parametric | `1/((c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(1/3))` | $\frac{1}{\sqrt[3]{c + d x} \sqrt[3]{a d + b c + 2 b d x}}$ |
| partial | parametric | `1/((a + b*x)*(c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(1/3))` | $\frac{1}{\left(a + b x\right) \sqrt[3]{c + d x} \sqrt[3]{a d + b c + 2 b d x}}$ |
| partial | parametric | `1/((a + b*x)**2*(c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(1/3))` | $\frac{1}{\left(a + b x\right)^{2} \sqrt[3]{c + d x} \sqrt[3]{a d + b c + 2 b d x}}$ |
| partial | parametric | `1/((a + b*x)**3*(c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(1/3))` | $\frac{1}{\left(a + b x\right)^{3} \sqrt[3]{c + d x} \sqrt[3]{a d + b c + 2 b d x}}$ |
| partial | parametric | `(a + b*x)**3/((c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(4/3))` | $\frac{\left(a + b x\right)^{3}}{\sqrt[3]{c + d x} \left(a d + b c + 2 b d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(a + b*x)**2/((c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(4/3))` | $\frac{\left(a + b x\right)^{2}}{\sqrt[3]{c + d x} \left(a d + b c + 2 b d x\right)^{\frac{4}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)/((c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(4/3))` | $\frac{a + b x}{\sqrt[3]{c + d x} \left(a d + b c + 2 b d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/((c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(4/3))` | $\frac{1}{\sqrt[3]{c + d x} \left(a d + b c + 2 b d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/((a + b*x)*(c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(4/3))` | $\frac{1}{\left(a + b x\right) \sqrt[3]{c + d x} \left(a d + b c + 2 b d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/((a + b*x)**2*(c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(4/3))` | $\frac{1}{\left(a + b x\right)^{2} \sqrt[3]{c + d x} \left(a d + b c + 2 b d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/((a + b*x)**3*(c + d*x)**(1/3)*(a*d + b*c + 2*b*d*x)**(4/3))` | $\frac{1}{\left(a + b x\right)^{3} \sqrt[3]{c + d x} \left(a d + b c + 2 b d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/((d - 3*e*x)**(1/3)*(d + e*x)*(d + 3*e*x)**(1/3))` | $\frac{1}{\sqrt[3]{d - 3 e x} \left(d + e x\right) \sqrt[3]{d + 3 e x}}$ |
| partial | parametric | `(a + b*x)**(4/3)*(e + f*x)**2/(c + d*x)**(4/3)` | $\frac{\left(a + b x\right)^{\frac{4}{3}} \left(e + f x\right)^{2}}{\left(c + d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(a + b*x)**(4/3)*(e + f*x)/(c + d*x)**(4/3)` | $\frac{\left(a + b x\right)^{\frac{4}{3}} \left(e + f x\right)}{\left(c + d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(a + b*x)**(4/3)/(c + d*x)**(4/3)` | $\frac{\left(a + b x\right)^{\frac{4}{3}}}{\left(c + d x\right)^{\frac{4}{3}}}$ |
| timeout | parametric | `(a + b*x)**(4/3)/((c + d*x)**(4/3)*(e + f*x))` | $\frac{\left(a + b x\right)^{\frac{4}{3}}}{\left(c + d x\right)^{\frac{4}{3}} \left(e + f x\right)}$ |
| timeout | parametric | `(a + b*x)**(4/3)/((c + d*x)**(4/3)*(e + f*x)**2)` | $\frac{\left(a + b x\right)^{\frac{4}{3}}}{\left(c + d x\right)^{\frac{4}{3}} \left(e + f x\right)^{2}}$ |
| timeout | parametric | `(a + b*x)**(4/3)/((c + d*x)**(4/3)*(e + f*x)**3)` | $\frac{\left(a + b x\right)^{\frac{4}{3}}}{\left(c + d x\right)^{\frac{4}{3}} \left(e + f x\right)^{3}}$ |
| timeout | parametric | `(a + b*x)**(4/3)/((c + d*x)**(4/3)*(e + f*x)**4)` | $\frac{\left(a + b x\right)^{\frac{4}{3}}}{\left(c + d x\right)^{\frac{4}{3}} \left(e + f x\right)^{4}}$ |
| timeout | parametric | `1/((a + b*x)*sqrt(c + d*x)*(e + f*x)**(1/4))` | $\frac{1}{\left(a + b x\right) \sqrt{c + d x} \sqrt[4]{e + f x}}$ |
| timeout | parametric | `1/((a + b*x)*sqrt(c + d*x)*(e + f*x)**(3/4))` | $\frac{1}{\left(a + b x\right) \sqrt{c + d x} \left(e + f x\right)^{\frac{3}{4}}}$ |
| timeout | parametric | `(a + b*x)**(4/3)/(sqrt(c + d*x)*(e + f*x))` | $\frac{\left(a + b x\right)^{\frac{4}{3}}}{\sqrt{c + d x} \left(e + f x\right)}$ |
| timeout | parametric | `(c + d*x)**(2/5)*(e + f*x)**(3/5)/sqrt(a + b*x)` | $\frac{\left(c + d x\right)^{\frac{2}{5}} \left(e + f x\right)^{\frac{3}{5}}}{\sqrt{a + b x}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(1/3)/(e + f*x)` | $\frac{\sqrt{a + b x} \sqrt[3]{c + d x}}{e + f x}$ |
| timeout | parametric | `(a + b*x)**(1/3)*sqrt(c + d*x)/(e + f*x)` | $\frac{\sqrt[3]{a + b x} \sqrt{c + d x}}{e + f x}$ |
| timeout | parametric | `sqrt(a + b*x)*(c + d*x)**(1/3)*(e + f*x)**(1/4)` | $\sqrt{a + b x} \sqrt[3]{c + d x} \sqrt[4]{e + f x}$ |
| timeout | parametric | `(a + b*x)**(1/3)*sqrt(c + d*x)*(e + f*x)**(1/4)` | $\sqrt[3]{a + b x} \sqrt{c + d x} \sqrt[4]{e + f x}$ |
| partial | parametric | `(a + b*x)**3*sqrt(c + d*x)*(e + f*x)/x` | $\frac{\left(a + b x\right)^{3} \sqrt{c + d x} \left(e + f x\right)}{x}$ |
| partial | parametric | `(a + b*x)**2*sqrt(c + d*x)*(e + f*x)/x` | $\frac{\left(a + b x\right)^{2} \sqrt{c + d x} \left(e + f x\right)}{x}$ |
| partial | parametric | `(a + b*x)*sqrt(c + d*x)*(e + f*x)/x` | $\frac{\left(a + b x\right) \sqrt{c + d x} \left(e + f x\right)}{x}$ |
| partial | parametric | `sqrt(c + d*x)*(e + f*x)/x` | $\frac{\sqrt{c + d x} \left(e + f x\right)}{x}$ |
| partial | parametric | `sqrt(c + d*x)*(e + f*x)/(x*(a + b*x))` | $\frac{\sqrt{c + d x} \left(e + f x\right)}{x \left(a + b x\right)}$ |
| partial | parametric | `sqrt(c + d*x)*(e + f*x)/(x*(a + b*x)**2)` | $\frac{\sqrt{c + d x} \left(e + f x\right)}{x \left(a + b x\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x)*(e + f*x)/(x*(a + b*x)**3)` | $\frac{\sqrt{c + d x} \left(e + f x\right)}{x \left(a + b x\right)^{3}}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)**3*(e + f*x)/x` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{3} \left(e + f x\right)}{x}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)**2*(e + f*x)/x` | $\frac{\sqrt{a + b x} \left(c + d x\right)^{2} \left(e + f x\right)}{x}$ |
| partial | parametric | `sqrt(a + b*x)*(c + d*x)*(e + f*x)/x` | $\frac{\sqrt{a + b x} \left(c + d x\right) \left(e + f x\right)}{x}$ |
| partial | parametric | `sqrt(a + b*x)*(e + f*x)/x` | $\frac{\sqrt{a + b x} \left(e + f x\right)}{x}$ |
| partial | parametric | `sqrt(a + b*x)*(e + f*x)/(x*(c + d*x))` | $\frac{\sqrt{a + b x} \left(e + f x\right)}{x \left(c + d x\right)}$ |
| partial | parametric | `sqrt(a + b*x)*(e + f*x)/(x*(c + d*x)**2)` | $\frac{\sqrt{a + b x} \left(e + f x\right)}{x \left(c + d x\right)^{2}}$ |
| partial | parametric | `sqrt(a + b*x)*(e + f*x)/(x*(c + d*x)**3)` | $\frac{\sqrt{a + b x} \left(e + f x\right)}{x \left(c + d x\right)^{3}}$ |
| partial | parametric | `x**3*(a*x + 1)/(sqrt(a*x)*sqrt(-a*x + 1))` | $\frac{x^{3} \left(a x + 1\right)}{\sqrt{a x} \sqrt{- a x + 1}}$ |
| partial | parametric | `x**2*(a*x + 1)/(sqrt(a*x)*sqrt(-a*x + 1))` | $\frac{x^{2} \left(a x + 1\right)}{\sqrt{a x} \sqrt{- a x + 1}}$ |
| partial | parametric | `x*(a*x + 1)/(sqrt(a*x)*sqrt(-a*x + 1))` | $\frac{x \left(a x + 1\right)}{\sqrt{a x} \sqrt{- a x + 1}}$ |
| partial | parametric | `(a*x + 1)/(sqrt(a*x)*sqrt(-a*x + 1))` | $\frac{a x + 1}{\sqrt{a x} \sqrt{- a x + 1}}$ |
| partial | parametric | `(a*x + 1)/(x*sqrt(a*x)*sqrt(-a*x + 1))` | $\frac{a x + 1}{x \sqrt{a x} \sqrt{- a x + 1}}$ |
| SOLVED-both | parametric | `(a*x + 1)/(x**2*sqrt(a*x)*sqrt(-a*x + 1))` | $\frac{a x + 1}{x^{2} \sqrt{a x} \sqrt{- a x + 1}}$ |
| SOLVED-both | parametric | `(a*x + 1)/(x**3*sqrt(a*x)*sqrt(-a*x + 1))` | $\frac{a x + 1}{x^{3} \sqrt{a x} \sqrt{- a x + 1}}$ |
| SOLVED-both | parametric | `(a*x + 1)/(x**4*sqrt(a*x)*sqrt(-a*x + 1))` | $\frac{a x + 1}{x^{4} \sqrt{a x} \sqrt{- a x + 1}}$ |
| SOLVED-both | parametric | `(a*x + 1)/(x**5*sqrt(a*x)*sqrt(-a*x + 1))` | $\frac{a x + 1}{x^{5} \sqrt{a x} \sqrt{- a x + 1}}$ |
| partial | parametric | `(2*a*x - 1)/(x**2*sqrt(x - 1)*sqrt(x + 1))` | $\frac{2 a x - 1}{x^{2} \sqrt{x - 1} \sqrt{x + 1}}$ |
| partial | parametric | `(a**2*x**2 - (-a*x + 1)**2)/(x**2*sqrt(x - 1)*sqrt(x + 1))` | $\frac{a^{2} x^{2} - \left(- a x + 1\right)^{2}}{x^{2} \sqrt{x - 1} \sqrt{x + 1}}$ |
| partial | parametric | `(A + B*x)/(sqrt(a + b*x)*sqrt(c + b*x*(c - 1)/a)*sqrt(e + b*x*(e - 1)/a))` | $\frac{A + B x}{\sqrt{a + b x} \sqrt{c + \frac{b x \left(c - 1\right)}{a}} \sqrt{e + \frac{b x \left(e - 1\right)}{a}}}$ |
| timeout | parametric | `(A + B*x)/(sqrt(a + b*x)*sqrt(c + d*x)*sqrt(e + b*x*(e - 1)/a))` | $\frac{A + B x}{\sqrt{a + b x} \sqrt{c + d x} \sqrt{e + \frac{b x \left(e - 1\right)}{a}}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7)**3` | $\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)^{3}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7)**2` | $\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)^{2}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7)` | $\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)` | $\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}$ |
| NIE | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)/(5*x + 7)` | $\frac{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}{5 x + 7}$ |
| NIE | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)/(5*x + 7)**2` | $\frac{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}{\left(5 x + 7\right)^{2}}$ |
| NIE | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)/(5*x + 7)**3` | $\frac{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}{\left(5 x + 7\right)^{3}}$ |
| NIE | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)/(5*x + 7)**4` | $\frac{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}{\left(5 x + 7\right)^{4}}$ |
| timeout | parametric | `sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x)/(a + b*x)` | $\frac{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}{a + b x}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)*(5*x + 7)**3/sqrt(2*x - 5)` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1} \left(5 x + 7\right)^{3}}{\sqrt{2 x - 5}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)*(5*x + 7)**2/sqrt(2*x - 5)` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1} \left(5 x + 7\right)^{2}}{\sqrt{2 x - 5}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)*(5*x + 7)/sqrt(2*x - 5)` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1} \left(5 x + 7\right)}{\sqrt{2 x - 5}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)/sqrt(2*x - 5)` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1}}{\sqrt{2 x - 5}}$ |
| NIE | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)/(sqrt(2*x - 5)*(5*x + 7))` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1}}{\sqrt{2 x - 5} \left(5 x + 7\right)}$ |
| NIE | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)/(sqrt(2*x - 5)*(5*x + 7)**2)` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1}}{\sqrt{2 x - 5} \left(5 x + 7\right)^{2}}$ |
| NIE | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)/(sqrt(2*x - 5)*(5*x + 7)**3)` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1}}{\sqrt{2 x - 5} \left(5 x + 7\right)^{3}}$ |
| partial | concrete | `sqrt(2 - 3*x)*(5*x + 7)**3/(sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\sqrt{2 - 3 x} \left(5 x + 7\right)^{3}}{\sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `sqrt(2 - 3*x)*(5*x + 7)**2/(sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\sqrt{2 - 3 x} \left(5 x + 7\right)^{2}}{\sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `sqrt(2 - 3*x)*(5*x + 7)/(sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\sqrt{2 - 3 x} \left(5 x + 7\right)}{\sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `sqrt(2 - 3*x)/(sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\sqrt{2 - 3 x}}{\sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| NIE | concrete | `sqrt(2 - 3*x)/(sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7))` | $\frac{\sqrt{2 - 3 x}}{\sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)}$ |
| NIE | concrete | `sqrt(2 - 3*x)/(sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7)**2)` | $\frac{\sqrt{2 - 3 x}}{\sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)^{2}}$ |
| NIE | concrete | `sqrt(2 - 3*x)/(sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7)**3)` | $\frac{\sqrt{2 - 3 x}}{\sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)^{3}}$ |
| timeout | parametric | `sqrt(c + d*x)/((a + b*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\sqrt{c + d x}}{\left(a + b x\right) \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(c + d*x)**(3/2)/((a + b*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\left(a + b x\right) \sqrt{e + f x} \sqrt{g + h x}}$ |
| partial | concrete | `(5*x + 7)**4/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\left(5 x + 7\right)^{4}}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `(5*x + 7)**3/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\left(5 x + 7\right)^{3}}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `(5*x + 7)**2/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\left(5 x + 7\right)^{2}}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `(5*x + 7)/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{5 x + 7}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `1/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{1}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| NIE | concrete | `1/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7))` | $\frac{1}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)}$ |
| NIE | concrete | `1/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7)**2)` | $\frac{1}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)^{2}}$ |
| NIE | concrete | `1/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7)**3)` | $\frac{1}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)^{3}}$ |
| timeout | parametric | `(c*i + d*i*x)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{c i + d i x}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(a + b*x)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{a + b x}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `1/((a + b*x)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{1}{\left(a + b x\right) \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `1/((a + b*x)*(c + d*x)**(3/2)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{1}{\left(a + b x\right) \left(c + d x\right)^{\frac{3}{2}} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `1/((a + b*x)*(c + d*x)**(5/2)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{1}{\left(a + b x\right) \left(c + d x\right)^{\frac{5}{2}} \sqrt{e + f x} \sqrt{g + h x}}$ |
| NIE | parametric | `1/((a + b*x)*sqrt(c + d*x)*sqrt(-f*x + 1)*sqrt(f*x + 1))` | $\frac{1}{\left(a + b x\right) \sqrt{c + d x} \sqrt{- f x + 1} \sqrt{f x + 1}}$ |
| timeout | parametric | `1/((a + b*x)*sqrt(c + d*x)*sqrt(-f**2*x**2 + 1))` | $\frac{1}{\left(a + b x\right) \sqrt{c + d x} \sqrt{- f^{2} x^{2} + 1}}$ |
| NIE | parametric | `1/((a + b*x)*sqrt(c + d*x)*sqrt(-f**2*x + 1)*sqrt(f**2*x + 1))` | $\frac{1}{\left(a + b x\right) \sqrt{c + d x} \sqrt{- f^{2} x + 1} \sqrt{f^{2} x + 1}}$ |
| timeout | parametric | `1/((a + b*x)*sqrt(c + d*x)*sqrt(-f**4*x**2 + 1))` | $\frac{1}{\left(a + b x\right) \sqrt{c + d x} \sqrt{- f^{4} x^{2} + 1}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7)**(5/2)` | $\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)^{\frac{5}{2}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7)**(3/2)` | $\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)*sqrt(5*x + 7)` | $\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1} \sqrt{5 x + 7}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)/sqrt(5*x + 7)` | $\frac{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}{\sqrt{5 x + 7}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)/(5*x + 7)**(3/2)` | $\frac{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}{\left(5 x + 7\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)/(5*x + 7)**(5/2)` | $\frac{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}{\left(5 x + 7\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)/(5*x + 7)**(7/2)` | $\frac{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}{\left(5 x + 7\right)^{\frac{7}{2}}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)/(5*x + 7)**(9/2)` | $\frac{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}{\left(5 x + 7\right)^{\frac{9}{2}}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)*(5*x + 7)**(5/2)/sqrt(2*x - 5)` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1} \left(5 x + 7\right)^{\frac{5}{2}}}{\sqrt{2 x - 5}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)*(5*x + 7)**(3/2)/sqrt(2*x - 5)` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1} \left(5 x + 7\right)^{\frac{3}{2}}}{\sqrt{2 x - 5}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)*sqrt(5*x + 7)/sqrt(2*x - 5)` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1} \sqrt{5 x + 7}}{\sqrt{2 x - 5}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)/(sqrt(2*x - 5)*sqrt(5*x + 7))` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1}}{\sqrt{2 x - 5} \sqrt{5 x + 7}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)/(sqrt(2*x - 5)*(5*x + 7)**(3/2))` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1}}{\sqrt{2 x - 5} \left(5 x + 7\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)/(sqrt(2*x - 5)*(5*x + 7)**(5/2))` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1}}{\sqrt{2 x - 5} \left(5 x + 7\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)/(sqrt(2*x - 5)*(5*x + 7)**(7/2))` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1}}{\sqrt{2 x - 5} \left(5 x + 7\right)^{\frac{7}{2}}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(4*x + 1)/(sqrt(2*x - 5)*(5*x + 7)**(9/2))` | $\frac{\sqrt{2 - 3 x} \sqrt{4 x + 1}}{\sqrt{2 x - 5} \left(5 x + 7\right)^{\frac{9}{2}}}$ |
| partial | concrete | `sqrt(2 - 3*x)*(5*x + 7)**(5/2)/(sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\sqrt{2 - 3 x} \left(5 x + 7\right)^{\frac{5}{2}}}{\sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `sqrt(2 - 3*x)*(5*x + 7)**(3/2)/(sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\sqrt{2 - 3 x} \left(5 x + 7\right)^{\frac{3}{2}}}{\sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `sqrt(2 - 3*x)*sqrt(5*x + 7)/(sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\sqrt{2 - 3 x} \sqrt{5 x + 7}}{\sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `sqrt(2 - 3*x)/(sqrt(2*x - 5)*sqrt(4*x + 1)*sqrt(5*x + 7))` | $\frac{\sqrt{2 - 3 x}}{\sqrt{2 x - 5} \sqrt{4 x + 1} \sqrt{5 x + 7}}$ |
| partial | concrete | `sqrt(2 - 3*x)/(sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7)**(5/2))` | $\frac{\sqrt{2 - 3 x}}{\sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `sqrt(a + b*x)*sqrt(c + d*x)/(sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\sqrt{a + b x} \sqrt{c + d x}}{\sqrt{e + f x} \sqrt{g + h x}}$ |
| partial | concrete | `(5*x + 7)**(5/2)/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\left(5 x + 7\right)^{\frac{5}{2}}}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `(5*x + 7)**(3/2)/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\left(5 x + 7\right)^{\frac{3}{2}}}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `sqrt(5*x + 7)/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1))` | $\frac{\sqrt{5 x + 7}}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1}}$ |
| partial | concrete | `1/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)*sqrt(5*x + 7))` | $\frac{1}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1} \sqrt{5 x + 7}}$ |
| partial | concrete | `1/(sqrt(2 - 3*x)*sqrt(2*x - 5)*sqrt(4*x + 1)*(5*x + 7)**(5/2))` | $\frac{1}{\sqrt{2 - 3 x} \sqrt{2 x - 5} \sqrt{4 x + 1} \left(5 x + 7\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a + b*x)**(3/2)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\left(a + b x\right)^{\frac{3}{2}}}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `sqrt(a + b*x)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\sqrt{a + b x}}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `1/((a + b*x)**(3/2)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `1/((a + b*x)**(3/2)*(c + d*x)**(3/2)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{1}{\left(a + b x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}} \sqrt{e + f x} \sqrt{g + h x}}$ |
| partial | parametric | `x*(a + b*x + c*x**2)/(sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{x \left(a + b x + c x^{2}\right)}{\sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(a + b*x + c*x**2)/(sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{a + b x + c x^{2}}{\sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(a + b*x + c*x**2)/(x*sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{a + b x + c x^{2}}{x \sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(a + b*x + c*x**2)/(x**2*sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{a + b x + c x^{2}}{x^{2} \sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(a + b*x + c*x**2)/(x**3*sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{a + b x + c x^{2}}{x^{3} \sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| SOLVED-both | parametric | `(a + b*x)**3*(A + B*x + C*x**2 + D*x**3)/sqrt(c + d*x)` | $\frac{\left(a + b x\right)^{3} \left(A + B x + C x^{2} + D x^{3}\right)}{\sqrt{c + d x}}$ |
| SOLVED-both | parametric | `(a + b*x)**2*(A + B*x + C*x**2 + D*x**3)/sqrt(c + d*x)` | $\frac{\left(a + b x\right)^{2} \left(A + B x + C x^{2} + D x^{3}\right)}{\sqrt{c + d x}}$ |
| SOLVED-both | parametric | `(a + b*x)*(A + B*x + C*x**2 + D*x**3)/sqrt(c + d*x)` | $\frac{\left(a + b x\right) \left(A + B x + C x^{2} + D x^{3}\right)}{\sqrt{c + d x}}$ |
| SOLVED-both | parametric | `(A + B*x + C*x**2 + D*x**3)/sqrt(c + d*x)` | $\frac{A + B x + C x^{2} + D x^{3}}{\sqrt{c + d x}}$ |
| partial | parametric | `(A + B*x + C*x**2 + D*x**3)/((a + b*x)*sqrt(c + d*x))` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(a + b x\right) \sqrt{c + d x}}$ |
| partial | parametric | `(A + B*x + C*x**2 + D*x**3)/((a + b*x)**2*sqrt(c + d*x))` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(a + b x\right)^{2} \sqrt{c + d x}}$ |
| partial | parametric | `(A + B*x + C*x**2 + D*x**3)/((a + b*x)**3*sqrt(c + d*x))` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(a + b x\right)^{3} \sqrt{c + d x}}$ |
| partial | parametric | `(A + B*x + C*x**2 + D*x**3)/((a + b*x)**4*sqrt(c + d*x))` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(a + b x\right)^{4} \sqrt{c + d x}}$ |
| partial | parametric | `(A + B*x + C*x**2 + D*x**3)/((a + b*x)**5*sqrt(c + d*x))` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(a + b x\right)^{5} \sqrt{c + d x}}$ |
| SOLVED-both | parametric | `(a + b*x)**3*(A + B*x + C*x**2 + D*x**3)/(c + d*x)**(3/2)` | $\frac{\left(a + b x\right)^{3} \left(A + B x + C x^{2} + D x^{3}\right)}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2*(A + B*x + C*x**2 + D*x**3)/(c + d*x)**(3/2)` | $\frac{\left(a + b x\right)^{2} \left(A + B x + C x^{2} + D x^{3}\right)}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(A + B*x + C*x**2 + D*x**3)/(c + d*x)**(3/2)` | $\frac{\left(a + b x\right) \left(A + B x + C x^{2} + D x^{3}\right)}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x + C*x**2 + D*x**3)/(c + d*x)**(3/2)` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2 + D*x**3)/((a + b*x)*(c + d*x)**(3/2))` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(a + b x\right) \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2 + D*x**3)/((a + b*x)**2*(c + d*x)**(3/2))` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(a + b x\right)^{2} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2 + D*x**3)/((a + b*x)**3*(c + d*x)**(3/2))` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(a + b x\right)^{3} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2 + D*x**3)/((a + b*x)**4*(c + d*x)**(3/2))` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(a + b x\right)^{4} \left(c + d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**3*(A + B*x + C*x**2 + D*x**3)/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right)^{3} \left(A + B x + C x^{2} + D x^{3}\right)}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)**2*(A + B*x + C*x**2 + D*x**3)/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right)^{2} \left(A + B x + C x^{2} + D x^{3}\right)}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(A + B*x + C*x**2 + D*x**3)/(c + d*x)**(5/2)` | $\frac{\left(a + b x\right) \left(A + B x + C x^{2} + D x^{3}\right)}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x + C*x**2 + D*x**3)/(c + d*x)**(5/2)` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2 + D*x**3)/((a + b*x)*(c + d*x)**(5/2))` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(a + b x\right) \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2 + D*x**3)/((a + b*x)**2*(c + d*x)**(5/2))` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(a + b x\right)^{2} \left(c + d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2 + D*x**3)/((a + b*x)**3*(c + d*x)**(5/2))` | $\frac{A + B x + C x^{2} + D x^{3}}{\left(a + b x\right)^{3} \left(c + d x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(e + f*x)**3*sqrt(-d*x + 1)*sqrt(d*x + 1)*(A + B*x + C*x**2)` | $\left(e + f x\right)^{3} \sqrt{- d x + 1} \sqrt{d x + 1} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `(e + f*x)**2*sqrt(-d*x + 1)*sqrt(d*x + 1)*(A + B*x + C*x**2)` | $\left(e + f x\right)^{2} \sqrt{- d x + 1} \sqrt{d x + 1} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `(e + f*x)*sqrt(-d*x + 1)*sqrt(d*x + 1)*(A + B*x + C*x**2)` | $\left(e + f x\right) \sqrt{- d x + 1} \sqrt{d x + 1} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `sqrt(-d*x + 1)*sqrt(d*x + 1)*(A + B*x + C*x**2)` | $\sqrt{- d x + 1} \sqrt{d x + 1} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `(A + B*x + C*x**2)/((e + f*x)*sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{A + B x + C x^{2}}{\left(e + f x\right) \sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(A + B*x + C*x**2)/((e + f*x)**2*sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{A + B x + C x^{2}}{\left(e + f x\right)^{2} \sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(A + B*x + C*x**2)/((e + f*x)**3*sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{A + B x + C x^{2}}{\left(e + f x\right)^{3} \sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| timeout | parametric | `(e + f*x)**3*(A + B*x + C*x**2)/(sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{\left(e + f x\right)^{3} \left(A + B x + C x^{2}\right)}{\sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(e + f*x)**2*(A + B*x + C*x**2)/(sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{\left(e + f x\right)^{2} \left(A + B x + C x^{2}\right)}{\sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(e + f*x)*(A + B*x + C*x**2)/(sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{\left(e + f x\right) \left(A + B x + C x^{2}\right)}{\sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(A + B*x + C*x**2)/(sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{A + B x + C x^{2}}{\sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(A + B*x + C*x**2)/((e + f*x)*sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{A + B x + C x^{2}}{\left(e + f x\right) \sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(A + B*x + C*x**2)/((e + f*x)**2*sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{A + B x + C x^{2}}{\left(e + f x\right)^{2} \sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(A + B*x + C*x**2)/((e + f*x)**3*sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{A + B x + C x^{2}}{\left(e + f x\right)^{3} \sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `x*(a + b*x + c*x**2)/(sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{x \left(a + b x + c x^{2}\right)}{\sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(a + b*x + c*x**2)/(sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{a + b x + c x^{2}}{\sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(a + b*x + c*x**2)/(x*sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{a + b x + c x^{2}}{x \sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(a + b*x + c*x**2)/(x**2*sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{a + b x + c x^{2}}{x^{2} \sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(a + b*x + c*x**2)/(x**3*sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{a + b x + c x^{2}}{x^{3} \sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| timeout | parametric | `sqrt(a + b*x)*(e + f*x)**3*sqrt(a*c - b*c*x)*(A + B*x + C*x**2)` | $\sqrt{a + b x} \left(e + f x\right)^{3} \sqrt{a c - b c x} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `sqrt(a + b*x)*(e + f*x)**2*sqrt(a*c - b*c*x)*(A + B*x + C*x**2)` | $\sqrt{a + b x} \left(e + f x\right)^{2} \sqrt{a c - b c x} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `sqrt(a + b*x)*(e + f*x)*sqrt(a*c - b*c*x)*(A + B*x + C*x**2)` | $\sqrt{a + b x} \left(e + f x\right) \sqrt{a c - b c x} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `sqrt(a + b*x)*sqrt(a*c - b*c*x)*(A + B*x + C*x**2)` | $\sqrt{a + b x} \sqrt{a c - b c x} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `(A + B*x + C*x**2)/(sqrt(a + b*x)*(e + f*x)*sqrt(a*c - b*c*x))` | $\frac{A + B x + C x^{2}}{\sqrt{a + b x} \left(e + f x\right) \sqrt{a c - b c x}}$ |
| partial | parametric | `(A + B*x + C*x**2)/(sqrt(a + b*x)*(e + f*x)**2*sqrt(a*c - b*c*x))` | $\frac{A + B x + C x^{2}}{\sqrt{a + b x} \left(e + f x\right)^{2} \sqrt{a c - b c x}}$ |
| partial | parametric | `(A + B*x + C*x**2)/(sqrt(a + b*x)*(e + f*x)**3*sqrt(a*c - b*c*x))` | $\frac{A + B x + C x^{2}}{\sqrt{a + b x} \left(e + f x\right)^{3} \sqrt{a c - b c x}}$ |
| timeout | parametric | `(e + f*x)**3*(A + B*x + C*x**2)/(sqrt(a + b*x)*sqrt(a*c - b*c*x))` | $\frac{\left(e + f x\right)^{3} \left(A + B x + C x^{2}\right)}{\sqrt{a + b x} \sqrt{a c - b c x}}$ |
| partial | parametric | `(e + f*x)**2*(A + B*x + C*x**2)/(sqrt(a + b*x)*sqrt(a*c - b*c*x))` | $\frac{\left(e + f x\right)^{2} \left(A + B x + C x^{2}\right)}{\sqrt{a + b x} \sqrt{a c - b c x}}$ |
| partial | parametric | `(e + f*x)*(A + B*x + C*x**2)/(sqrt(a + b*x)*sqrt(a*c - b*c*x))` | $\frac{\left(e + f x\right) \left(A + B x + C x^{2}\right)}{\sqrt{a + b x} \sqrt{a c - b c x}}$ |
| partial | parametric | `(A + B*x + C*x**2)/(sqrt(a + b*x)*sqrt(a*c - b*c*x))` | $\frac{A + B x + C x^{2}}{\sqrt{a + b x} \sqrt{a c - b c x}}$ |
| partial | parametric | `(A + B*x + C*x**2)/(sqrt(a + b*x)*(e + f*x)*sqrt(a*c - b*c*x))` | $\frac{A + B x + C x^{2}}{\sqrt{a + b x} \left(e + f x\right) \sqrt{a c - b c x}}$ |
| partial | parametric | `(A + B*x + C*x**2)/(sqrt(a + b*x)*(e + f*x)**2*sqrt(a*c - b*c*x))` | $\frac{A + B x + C x^{2}}{\sqrt{a + b x} \left(e + f x\right)^{2} \sqrt{a c - b c x}}$ |
| partial | parametric | `(A + B*x + C*x**2)/(sqrt(a + b*x)*(e + f*x)**3*sqrt(a*c - b*c*x))` | $\frac{A + B x + C x^{2}}{\sqrt{a + b x} \left(e + f x\right)^{3} \sqrt{a c - b c x}}$ |
| partial | parametric | `(a + b*x)**2*sqrt(c + d*x)*sqrt(e + f*x)*(A + B*x + C*x**2)` | $\left(a + b x\right)^{2} \sqrt{c + d x} \sqrt{e + f x} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `(a + b*x)*sqrt(c + d*x)*sqrt(e + f*x)*(A + B*x + C*x**2)` | $\left(a + b x\right) \sqrt{c + d x} \sqrt{e + f x} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `sqrt(c + d*x)*sqrt(e + f*x)*(A + B*x + C*x**2)` | $\sqrt{c + d x} \sqrt{e + f x} \left(A + B x + C x^{2}\right)$ |
| timeout | parametric | `sqrt(c + d*x)*sqrt(e + f*x)*(A + B*x + C*x**2)/(a + b*x)` | $\frac{\sqrt{c + d x} \sqrt{e + f x} \left(A + B x + C x^{2}\right)}{a + b x}$ |
| timeout | parametric | `sqrt(c + d*x)*sqrt(e + f*x)*(A + B*x + C*x**2)/(a + b*x)**2` | $\frac{\sqrt{c + d x} \sqrt{e + f x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right)^{2}}$ |
| timeout | parametric | `sqrt(c + d*x)*sqrt(e + f*x)*(A + B*x + C*x**2)/(a + b*x)**3` | $\frac{\sqrt{c + d x} \sqrt{e + f x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `(a + b*x)**2*sqrt(c + d*x)*(A + B*x + C*x**2)/sqrt(e + f*x)` | $\frac{\left(a + b x\right)^{2} \sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\sqrt{e + f x}}$ |
| partial | parametric | `(a + b*x)*sqrt(c + d*x)*(A + B*x + C*x**2)/sqrt(e + f*x)` | $\frac{\left(a + b x\right) \sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\sqrt{e + f x}}$ |
| partial | parametric | `sqrt(c + d*x)*(A + B*x + C*x**2)/sqrt(e + f*x)` | $\frac{\sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\sqrt{e + f x}}$ |
| timeout | parametric | `sqrt(c + d*x)*(A + B*x + C*x**2)/((a + b*x)*sqrt(e + f*x))` | $\frac{\sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right) \sqrt{e + f x}}$ |
| timeout | parametric | `sqrt(c + d*x)*(A + B*x + C*x**2)/((a + b*x)**2*sqrt(e + f*x))` | $\frac{\sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right)^{2} \sqrt{e + f x}}$ |
| timeout | parametric | `sqrt(c + d*x)*(A + B*x + C*x**2)/((a + b*x)**3*sqrt(e + f*x))` | $\frac{\sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right)^{3} \sqrt{e + f x}}$ |
| timeout | parametric | `sqrt(c + d*x)*(A + B*x + C*x**2)/((a + b*x)**4*sqrt(e + f*x))` | $\frac{\sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right)^{4} \sqrt{e + f x}}$ |
| partial | parametric | `(a + b*x)**2*(A + B*x + C*x**2)/(sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{\left(a + b x\right)^{2} \left(A + B x + C x^{2}\right)}{\sqrt{c + d x} \sqrt{e + f x}}$ |
| partial | parametric | `(a + b*x)*(A + B*x + C*x**2)/(sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{\left(a + b x\right) \left(A + B x + C x^{2}\right)}{\sqrt{c + d x} \sqrt{e + f x}}$ |
| partial | parametric | `(A + B*x + C*x**2)/(sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{A + B x + C x^{2}}{\sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | parametric | `(A + B*x + C*x**2)/((a + b*x)*sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{A + B x + C x^{2}}{\left(a + b x\right) \sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | parametric | `(A + B*x + C*x**2)/((a + b*x)**2*sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{A + B x + C x^{2}}{\left(a + b x\right)^{2} \sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | parametric | `(A + B*x + C*x**2)/((a + b*x)**3*sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{A + B x + C x^{2}}{\left(a + b x\right)^{3} \sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | parametric | `(A + B*x + C*x**2)/((a + b*x)**4*sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{A + B x + C x^{2}}{\left(a + b x\right)^{4} \sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | parametric | `sqrt(a + b*x)*sqrt(c + d*x)*sqrt(e + f*x)*(A + B*x + C*x**2)` | $\sqrt{a + b x} \sqrt{c + d x} \sqrt{e + f x} \left(A + B x + C x^{2}\right)$ |
| timeout | parametric | `sqrt(c + d*x)*sqrt(e + f*x)*(A + B*x + C*x**2)/sqrt(a + b*x)` | $\frac{\sqrt{c + d x} \sqrt{e + f x} \left(A + B x + C x^{2}\right)}{\sqrt{a + b x}}$ |
| timeout | parametric | `sqrt(c + d*x)*sqrt(e + f*x)*(A + B*x + C*x**2)/(a + b*x)**(3/2)` | $\frac{\sqrt{c + d x} \sqrt{e + f x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(c + d*x)*sqrt(e + f*x)*(A + B*x + C*x**2)/(a + b*x)**(5/2)` | $\frac{\sqrt{c + d x} \sqrt{e + f x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `sqrt(c + d*x)*sqrt(e + f*x)*(A + B*x + C*x**2)/(a + b*x)**(7/2)` | $\frac{\sqrt{c + d x} \sqrt{e + f x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right)^{\frac{7}{2}}}$ |
| timeout | parametric | `sqrt(c + d*x)*sqrt(e + f*x)*(A + B*x + C*x**2)/(a + b*x)**(9/2)` | $\frac{\sqrt{c + d x} \sqrt{e + f x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right)^{\frac{9}{2}}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*sqrt(c + d*x)*(A + B*x + C*x**2)/sqrt(e + f*x)` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\sqrt{e + f x}}$ |
| timeout | parametric | `sqrt(a + b*x)*sqrt(c + d*x)*(A + B*x + C*x**2)/sqrt(e + f*x)` | $\frac{\sqrt{a + b x} \sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\sqrt{e + f x}}$ |
| timeout | parametric | `sqrt(c + d*x)*(A + B*x + C*x**2)/(sqrt(a + b*x)*sqrt(e + f*x))` | $\frac{\sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\sqrt{a + b x} \sqrt{e + f x}}$ |
| timeout | parametric | `sqrt(c + d*x)*(A + B*x + C*x**2)/((a + b*x)**(3/2)*sqrt(e + f*x))` | $\frac{\sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right)^{\frac{3}{2}} \sqrt{e + f x}}$ |
| timeout | parametric | `sqrt(c + d*x)*(A + B*x + C*x**2)/((a + b*x)**(5/2)*sqrt(e + f*x))` | $\frac{\sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right)^{\frac{5}{2}} \sqrt{e + f x}}$ |
| timeout | parametric | `sqrt(c + d*x)*(A + B*x + C*x**2)/((a + b*x)**(7/2)*sqrt(e + f*x))` | $\frac{\sqrt{c + d x} \left(A + B x + C x^{2}\right)}{\left(a + b x\right)^{\frac{7}{2}} \sqrt{e + f x}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*(A + B*x + C*x**2)/(sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(A + B x + C x^{2}\right)}{\sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | parametric | `sqrt(a + b*x)*(A + B*x + C*x**2)/(sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{\sqrt{a + b x} \left(A + B x + C x^{2}\right)}{\sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | parametric | `(A + B*x + C*x**2)/(sqrt(a + b*x)*sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{A + B x + C x^{2}}{\sqrt{a + b x} \sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | parametric | `(A + B*x + C*x**2)/((a + b*x)**(3/2)*sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{A + B x + C x^{2}}{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | parametric | `(A + B*x + C*x**2)/((a + b*x)**(5/2)*sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{A + B x + C x^{2}}{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | parametric | `(A + B*x + C*x**2)/((a + b*x)**(7/2)*sqrt(c + d*x)*sqrt(e + f*x))` | $\frac{A + B x + C x^{2}}{\left(a + b x\right)^{\frac{7}{2}} \sqrt{c + d x} \sqrt{e + f x}}$ |
| timeout | parametric | `(A + B*x)*(a + b*x)**2/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\left(A + B x\right) \left(a + b x\right)^{2}}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + B*x)*(a + b*x)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\left(A + B x\right) \left(a + b x\right)}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + B*x)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{A + B x}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + B*x)/((a + b*x)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{A + B x}{\left(a + b x\right) \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + B*x)/((a + b*x)**2*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{A + B x}{\left(a + b x\right)^{2} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + B*x)*(a + b*x)**(3/2)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\left(A + B x\right) \left(a + b x\right)^{\frac{3}{2}}}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + B*x)*sqrt(a + b*x)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\left(A + B x\right) \sqrt{a + b x}}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + B*x)/(sqrt(a + b*x)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{A + B x}{\sqrt{a + b x} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + B*x)/((a + b*x)**(3/2)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{A + B x}{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + B*x)/((a + b*x)**(5/2)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{A + B x}{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(a + b*x)**(3/2)*(c*f + d*e + 2*d*f*x)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\left(a + b x\right)^{\frac{3}{2}} \left(c f + d e + 2 d f x\right)}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `sqrt(a + b*x)*(c*f + d*e + 2*d*f*x)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\sqrt{a + b x} \left(c f + d e + 2 d f x\right)}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(c*f + d*e + 2*d*f*x)/(sqrt(a + b*x)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{c f + d e + 2 d f x}{\sqrt{a + b x} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(c*f + d*e + 2*d*f*x)/((a + b*x)**(3/2)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{c f + d e + 2 d f x}{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(c*f + d*e + 2*d*f*x)/((a + b*x)**(5/2)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{c f + d e + 2 d f x}{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(a + b*x)*(B*a*b + B*b**2*x - C*a**2 + C*b**2*x**2)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\left(a + b x\right) \left(B a b + B b^{2} x - C a^{2} + C b^{2} x^{2}\right)}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(B*a*b + B*b**2*x - C*a**2 + C*b**2*x**2)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{B a b + B b^{2} x - C a^{2} + C b^{2} x^{2}}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(B*a*b + B*b**2*x - C*a**2 + C*b**2*x**2)/((a + b*x)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{B a b + B b^{2} x - C a^{2} + C b^{2} x^{2}}{\left(a + b x\right) \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(B*a*b + B*b**2*x - C*a**2 + C*b**2*x**2)/((a + b*x)**2*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{B a b + B b^{2} x - C a^{2} + C b^{2} x^{2}}{\left(a + b x\right)^{2} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(B*a*b + B*b**2*x - C*a**2 + C*b**2*x**2)/((a + b*x)**3*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{B a b + B b^{2} x - C a^{2} + C b^{2} x^{2}}{\left(a + b x\right)^{3} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `sqrt(a + b*x)*(B*a*b + B*b**2*x - C*a**2 + C*b**2*x**2)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\sqrt{a + b x} \left(B a b + B b^{2} x - C a^{2} + C b^{2} x^{2}\right)}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(B*a*b + B*b**2*x - C*a**2 + C*b**2*x**2)/(sqrt(a + b*x)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{B a b + B b^{2} x - C a^{2} + C b^{2} x^{2}}{\sqrt{a + b x} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(B*a*b + B*b**2*x - C*a**2 + C*b**2*x**2)/((a + b*x)**(3/2)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{B a b + B b^{2} x - C a^{2} + C b^{2} x^{2}}{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(B*a*b + B*b**2*x - C*a**2 + C*b**2*x**2)/((a + b*x)**(5/2)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{B a b + B b^{2} x - C a^{2} + C b^{2} x^{2}}{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(B*a*b + B*b**2*x - C*a**2 + C*b**2*x**2)/((a + b*x)**(7/2)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{B a b + B b^{2} x - C a^{2} + C b^{2} x^{2}}{\left(a + b x\right)^{\frac{7}{2}} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + C*x**2)*(a + b*x)**2/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\left(A + C x^{2}\right) \left(a + b x\right)^{2}}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + C*x**2)*(a + b*x)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\left(A + C x^{2}\right) \left(a + b x\right)}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + C*x**2)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{A + C x^{2}}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + C*x**2)/((a + b*x)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{A + C x^{2}}{\left(a + b x\right) \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + C*x**2)/((a + b*x)**2*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{A + C x^{2}}{\left(a + b x\right)^{2} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + C*x**2)*(a + b*x)**(3/2)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\left(A + C x^{2}\right) \left(a + b x\right)^{\frac{3}{2}}}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + C*x**2)*sqrt(a + b*x)/(sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{\left(A + C x^{2}\right) \sqrt{a + b x}}{\sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + C*x**2)/(sqrt(a + b*x)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{A + C x^{2}}{\sqrt{a + b x} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + C*x**2)/((a + b*x)**(3/2)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{A + C x^{2}}{\left(a + b x\right)^{\frac{3}{2}} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
| timeout | parametric | `(A + C*x**2)/((a + b*x)**(5/2)*sqrt(c + d*x)*sqrt(e + f*x)*sqrt(g + h*x))` | $\frac{A + C x^{2}}{\left(a + b x\right)^{\frac{5}{2}} \sqrt{c + d x} \sqrt{e + f x} \sqrt{g + h x}}$ |
