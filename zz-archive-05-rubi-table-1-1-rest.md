# 1.1.2-1.1.4 Quadratic/general/improper binomials

All attempted radical cases from this part of the Rubi corpus, run through `risch_integrate(f, x, algebraic=True)` (sympy branch `risch-algebraic`).  **SOLVED-NEW** means solved here but not by sympy's non-risch `integrate()`; SOLVED-both means both solve it.  5144 cases: partial 3735 (73%), SOLVED-both 1102 (21%), SOLVED-NEW 143 (3%), timeout 141 (3%), NIE 23 (0%).

| Status | Kind | SymPy expression | Math |
|---|---|---|---|
| SOLVED-both | parametric | `x**(7/2)*(a + b*x**2)` | $x^{\frac{7}{2}} \left(a + b x^{2}\right)$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b*x**2)` | $x^{\frac{5}{2}} \left(a + b x^{2}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b*x**2)` | $x^{\frac{3}{2}} \left(a + b x^{2}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b*x**2)` | $\sqrt{x} \left(a + b x^{2}\right)$ |
| SOLVED-both | parametric | `(a + b*x**2)/sqrt(x)` | $\frac{a + b x^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b*x**2)/x**(3/2)` | $\frac{a + b x^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)/x**(5/2)` | $\frac{a + b x^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)/x**(7/2)` | $\frac{a + b x^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(a + b*x**2)**2` | $x^{\frac{7}{2}} \left(a + b x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b*x**2)**2` | $x^{\frac{5}{2}} \left(a + b x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b*x**2)**2` | $x^{\frac{3}{2}} \left(a + b x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b*x**2)**2` | $\sqrt{x} \left(a + b x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2/sqrt(x)` | $\frac{\left(a + b x^{2}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2/x**(3/2)` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2/x**(5/2)` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2/x**(7/2)` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(a + b*x**2)**3` | $x^{\frac{7}{2}} \left(a + b x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b*x**2)**3` | $x^{\frac{5}{2}} \left(a + b x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b*x**2)**3` | $x^{\frac{3}{2}} \left(a + b x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b*x**2)**3` | $\sqrt{x} \left(a + b x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x**2)**3/sqrt(x)` | $\frac{\left(a + b x^{2}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**3/x**(3/2)` | $\frac{\left(a + b x^{2}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**3/x**(5/2)` | $\frac{\left(a + b x^{2}\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**3/x**(7/2)` | $\frac{\left(a + b x^{2}\right)^{3}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `x**(7/2)/(a + b*x**2)` | $\frac{x^{\frac{7}{2}}}{a + b x^{2}}$ |
| partial | parametric | `x**(5/2)/(a + b*x**2)` | $\frac{x^{\frac{5}{2}}}{a + b x^{2}}$ |
| partial | parametric | `x**(3/2)/(a + b*x**2)` | $\frac{x^{\frac{3}{2}}}{a + b x^{2}}$ |
| partial | parametric | `sqrt(x)/(a + b*x**2)` | $\frac{\sqrt{x}}{a + b x^{2}}$ |
| partial | parametric | `1/(sqrt(x)*(a + b*x**2))` | $\frac{1}{\sqrt{x} \left(a + b x^{2}\right)}$ |
| partial | parametric | `1/(x**(3/2)*(a + b*x**2))` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `1/(x**(5/2)*(a + b*x**2))` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `1/(x**(7/2)*(a + b*x**2))` | $\frac{1}{x^{\frac{7}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `x**(7/2)/(a + b*x**2)**2` | $\frac{x^{\frac{7}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**(5/2)/(a + b*x**2)**2` | $\frac{x^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**(3/2)/(a + b*x**2)**2` | $\frac{x^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(x)/(a + b*x**2)**2` | $\frac{\sqrt{x}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(x)*(a + b*x**2)**2)` | $\frac{1}{\sqrt{x} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `1/(x**(3/2)*(a + b*x**2)**2)` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `1/(x**(5/2)*(a + b*x**2)**2)` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `1/(x**(7/2)*(a + b*x**2)**2)` | $\frac{1}{x^{\frac{7}{2}} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**(7/2)/(a + b*x**2)**3` | $\frac{x^{\frac{7}{2}}}{\left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `x**(5/2)/(a + b*x**2)**3` | $\frac{x^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `x**(3/2)/(a + b*x**2)**3` | $\frac{x^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(x)/(a + b*x**2)**3` | $\frac{\sqrt{x}}{\left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `1/(sqrt(x)*(a + b*x**2)**3)` | $\frac{1}{\sqrt{x} \left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `1/(x**(3/2)*(a + b*x**2)**3)` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `1/(x**(5/2)*(a + b*x**2)**3)` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `1/(x**(7/2)*(a + b*x**2)**3)` | $\frac{1}{x^{\frac{7}{2}} \left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(x)/(a - b*x**2)` | $\frac{\sqrt{x}}{a - b x^{2}}$ |
| partial | concrete | `x**(7/2)/(x**2 + 1)` | $\frac{x^{\frac{7}{2}}}{x^{2} + 1}$ |
| partial | concrete | `x**(5/2)/(x**2 + 1)` | $\frac{x^{\frac{5}{2}}}{x^{2} + 1}$ |
| partial | concrete | `x**(3/2)/(x**2 + 1)` | $\frac{x^{\frac{3}{2}}}{x^{2} + 1}$ |
| partial | concrete | `sqrt(x)/(x**2 + 1)` | $\frac{\sqrt{x}}{x^{2} + 1}$ |
| partial | concrete | `1/(sqrt(x)*(x**2 + 1))` | $\frac{1}{\sqrt{x} \left(x^{2} + 1\right)}$ |
| partial | concrete | `1/(x**(3/2)*(x**2 + 1))` | $\frac{1}{x^{\frac{3}{2}} \left(x^{2} + 1\right)}$ |
| partial | concrete | `1/(x**(5/2)*(x**2 + 1))` | $\frac{1}{x^{\frac{5}{2}} \left(x^{2} + 1\right)}$ |
| partial | concrete | `1/(x**(7/2)*(x**2 + 1))` | $\frac{1}{x^{\frac{7}{2}} \left(x^{2} + 1\right)}$ |
| partial | concrete | `x**(7/2)/(x**2 + 1)**2` | $\frac{x^{\frac{7}{2}}}{\left(x^{2} + 1\right)^{2}}$ |
| partial | concrete | `x**(5/2)/(x**2 + 1)**2` | $\frac{x^{\frac{5}{2}}}{\left(x^{2} + 1\right)^{2}}$ |
| partial | concrete | `x**(3/2)/(x**2 + 1)**2` | $\frac{x^{\frac{3}{2}}}{\left(x^{2} + 1\right)^{2}}$ |
| partial | concrete | `sqrt(x)/(x**2 + 1)**2` | $\frac{\sqrt{x}}{\left(x^{2} + 1\right)^{2}}$ |
| partial | concrete | `1/(sqrt(x)*(x**2 + 1)**2)` | $\frac{1}{\sqrt{x} \left(x^{2} + 1\right)^{2}}$ |
| partial | concrete | `1/(x**(3/2)*(x**2 + 1)**2)` | $\frac{1}{x^{\frac{3}{2}} \left(x^{2} + 1\right)^{2}}$ |
| partial | concrete | `1/(x**(5/2)*(x**2 + 1)**2)` | $\frac{1}{x^{\frac{5}{2}} \left(x^{2} + 1\right)^{2}}$ |
| partial | concrete | `1/(x**(7/2)*(x**2 + 1)**2)` | $\frac{1}{x^{\frac{7}{2}} \left(x^{2} + 1\right)^{2}}$ |
| partial | concrete | `x**(7/2)/(x**2 + 1)**3` | $\frac{x^{\frac{7}{2}}}{\left(x^{2} + 1\right)^{3}}$ |
| partial | concrete | `x**(5/2)/(x**2 + 1)**3` | $\frac{x^{\frac{5}{2}}}{\left(x^{2} + 1\right)^{3}}$ |
| partial | concrete | `x**(3/2)/(x**2 + 1)**3` | $\frac{x^{\frac{3}{2}}}{\left(x^{2} + 1\right)^{3}}$ |
| partial | concrete | `sqrt(x)/(x**2 + 1)**3` | $\frac{\sqrt{x}}{\left(x^{2} + 1\right)^{3}}$ |
| partial | concrete | `1/(sqrt(x)*(x**2 + 1)**3)` | $\frac{1}{\sqrt{x} \left(x^{2} + 1\right)^{3}}$ |
| partial | concrete | `1/(x**(3/2)*(x**2 + 1)**3)` | $\frac{1}{x^{\frac{3}{2}} \left(x^{2} + 1\right)^{3}}$ |
| partial | concrete | `1/(x**(5/2)*(x**2 + 1)**3)` | $\frac{1}{x^{\frac{5}{2}} \left(x^{2} + 1\right)^{3}}$ |
| partial | concrete | `1/(x**(7/2)*(x**2 + 1)**3)` | $\frac{1}{x^{\frac{7}{2}} \left(x^{2} + 1\right)^{3}}$ |
| partial | concrete | `sqrt(x)/(1 - x**2)` | $\frac{\sqrt{x}}{1 - x^{2}}$ |
| SOLVED-both | parametric | `x**7*sqrt(a + b*x**2)` | $x^{7} \sqrt{a + b x^{2}}$ |
| SOLVED-both | parametric | `x**5*sqrt(a + b*x**2)` | $x^{5} \sqrt{a + b x^{2}}$ |
| SOLVED-both | parametric | `x**3*sqrt(a + b*x**2)` | $x^{3} \sqrt{a + b x^{2}}$ |
| SOLVED-both | parametric | `x*sqrt(a + b*x**2)` | $x \sqrt{a + b x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**2)/x` | $\frac{\sqrt{a + b x^{2}}}{x}$ |
| partial | parametric | `sqrt(a + b*x**2)/x**3` | $\frac{\sqrt{a + b x^{2}}}{x^{3}}$ |
| partial | parametric | `sqrt(a + b*x**2)/x**5` | $\frac{\sqrt{a + b x^{2}}}{x^{5}}$ |
| partial | parametric | `sqrt(a + b*x**2)/x**7` | $\frac{\sqrt{a + b x^{2}}}{x^{7}}$ |
| partial | parametric | `x**4*sqrt(a + b*x**2)` | $x^{4} \sqrt{a + b x^{2}}$ |
| partial | parametric | `x**2*sqrt(a + b*x**2)` | $x^{2} \sqrt{a + b x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**2)` | $\sqrt{a + b x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**2)/x**2` | $\frac{\sqrt{a + b x^{2}}}{x^{2}}$ |
| SOLVED-both | parametric | `sqrt(a + b*x**2)/x**4` | $\frac{\sqrt{a + b x^{2}}}{x^{4}}$ |
| SOLVED-both | parametric | `sqrt(a + b*x**2)/x**6` | $\frac{\sqrt{a + b x^{2}}}{x^{6}}$ |
| SOLVED-both | parametric | `sqrt(a + b*x**2)/x**8` | $\frac{\sqrt{a + b x^{2}}}{x^{8}}$ |
| SOLVED-both | parametric | `sqrt(a + b*x**2)/x**10` | $\frac{\sqrt{a + b x^{2}}}{x^{10}}$ |
| SOLVED-both | parametric | `x**7*(a + b*x**2)**(3/2)` | $x^{7} \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**5*(a + b*x**2)**(3/2)` | $x^{5} \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)**(3/2)` | $x^{3} \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)**(3/2)` | $x \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/x` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/x**3` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/x**5` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/x**7` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/x**9` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{9}}$ |
| partial | parametric | `x**4*(a + b*x**2)**(3/2)` | $x^{4} \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(a + b*x**2)**(3/2)` | $x^{2} \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)` | $\left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/x**2` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/x**4` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(3/2)/x**6` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(3/2)/x**8` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{8}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(3/2)/x**10` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{10}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(3/2)/x**12` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{12}}$ |
| SOLVED-both | parametric | `x**7*(a + b*x**2)**(5/2)` | $x^{7} \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**5*(a + b*x**2)**(5/2)` | $x^{5} \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)**(5/2)` | $x^{3} \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)**(5/2)` | $x \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/x` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/x**3` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/x**5` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{5}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/x**7` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{7}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/x**9` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{9}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/x**11` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{11}}$ |
| partial | parametric | `x**4*(a + b*x**2)**(5/2)` | $x^{4} \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**2*(a + b*x**2)**(5/2)` | $x^{2} \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)` | $\left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/x**2` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/x**4` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/x**6` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(5/2)/x**8` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{8}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(5/2)/x**10` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{10}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(5/2)/x**12` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{12}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(5/2)/x**14` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{14}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(5/2)/x**16` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{16}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(5/2)/x**18` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{18}}$ |
| SOLVED-both | parametric | `x**15*(a + b*x**2)**(9/2)` | $x^{15} \left(a + b x^{2}\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x**13*(a + b*x**2)**(9/2)` | $x^{13} \left(a + b x^{2}\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x**11*(a + b*x**2)**(9/2)` | $x^{11} \left(a + b x^{2}\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x**9*(a + b*x**2)**(9/2)` | $x^{9} \left(a + b x^{2}\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x**7*(a + b*x**2)**(9/2)` | $x^{7} \left(a + b x^{2}\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x**5*(a + b*x**2)**(9/2)` | $x^{5} \left(a + b x^{2}\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)**(9/2)` | $x^{3} \left(a + b x^{2}\right)^{\frac{9}{2}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)**(9/2)` | $x \left(a + b x^{2}\right)^{\frac{9}{2}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x**3` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x**5` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{5}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x**7` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{7}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x**9` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{9}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x**11` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{11}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x**13` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{13}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x**15` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{15}}$ |
| partial | parametric | `x**6*(a + b*x**2)**(9/2)` | $x^{6} \left(a + b x^{2}\right)^{\frac{9}{2}}$ |
| partial | parametric | `x**4*(a + b*x**2)**(9/2)` | $x^{4} \left(a + b x^{2}\right)^{\frac{9}{2}}$ |
| partial | parametric | `x**2*(a + b*x**2)**(9/2)` | $x^{2} \left(a + b x^{2}\right)^{\frac{9}{2}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)` | $\left(a + b x^{2}\right)^{\frac{9}{2}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x**2` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x**4` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x**6` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{6}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x**8` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{8}}$ |
| partial | parametric | `(a + b*x**2)**(9/2)/x**10` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{10}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(9/2)/x**12` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{12}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(9/2)/x**14` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{14}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(9/2)/x**16` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{16}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(9/2)/x**18` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{18}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(9/2)/x**20` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{20}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(9/2)/x**22` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{22}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(9/2)/x**24` | $\frac{\left(a + b x^{2}\right)^{\frac{9}{2}}}{x^{24}}$ |
| SOLVED-both | concrete | `x**5*sqrt(4*x**2 + 9)` | $x^{5} \sqrt{4 x^{2} + 9}$ |
| partial | concrete | `x**4*sqrt(4*x**2 + 9)` | $x^{4} \sqrt{4 x^{2} + 9}$ |
| SOLVED-both | concrete | `x**3*sqrt(4*x**2 + 9)` | $x^{3} \sqrt{4 x^{2} + 9}$ |
| partial | concrete | `x**2*sqrt(4*x**2 + 9)` | $x^{2} \sqrt{4 x^{2} + 9}$ |
| SOLVED-both | concrete | `x*sqrt(4*x**2 + 9)` | $x \sqrt{4 x^{2} + 9}$ |
| partial | concrete | `sqrt(4*x**2 + 9)` | $\sqrt{4 x^{2} + 9}$ |
| partial | concrete | `sqrt(4*x**2 + 9)/x` | $\frac{\sqrt{4 x^{2} + 9}}{x}$ |
| partial | concrete | `sqrt(4*x**2 + 9)/x**2` | $\frac{\sqrt{4 x^{2} + 9}}{x^{2}}$ |
| partial | concrete | `sqrt(4*x**2 + 9)/x**3` | $\frac{\sqrt{4 x^{2} + 9}}{x^{3}}$ |
| SOLVED-both | concrete | `sqrt(4*x**2 + 9)/x**4` | $\frac{\sqrt{4 x^{2} + 9}}{x^{4}}$ |
| partial | concrete | `sqrt(4*x**2 + 9)/x**5` | $\frac{\sqrt{4 x^{2} + 9}}{x^{5}}$ |
| SOLVED-both | concrete | `x**5*sqrt(9 - 4*x**2)` | $x^{5} \sqrt{9 - 4 x^{2}}$ |
| partial | concrete | `x**4*sqrt(9 - 4*x**2)` | $x^{4} \sqrt{9 - 4 x^{2}}$ |
| SOLVED-both | concrete | `x**3*sqrt(9 - 4*x**2)` | $x^{3} \sqrt{9 - 4 x^{2}}$ |
| partial | concrete | `x**2*sqrt(9 - 4*x**2)` | $x^{2} \sqrt{9 - 4 x^{2}}$ |
| SOLVED-both | concrete | `x*sqrt(9 - 4*x**2)` | $x \sqrt{9 - 4 x^{2}}$ |
| partial | concrete | `sqrt(9 - 4*x**2)` | $\sqrt{9 - 4 x^{2}}$ |
| partial | concrete | `sqrt(9 - 4*x**2)/x` | $\frac{\sqrt{9 - 4 x^{2}}}{x}$ |
| partial | concrete | `sqrt(9 - 4*x**2)/x**2` | $\frac{\sqrt{9 - 4 x^{2}}}{x^{2}}$ |
| partial | concrete | `sqrt(9 - 4*x**2)/x**3` | $\frac{\sqrt{9 - 4 x^{2}}}{x^{3}}$ |
| SOLVED-both | concrete | `sqrt(9 - 4*x**2)/x**4` | $\frac{\sqrt{9 - 4 x^{2}}}{x^{4}}$ |
| partial | concrete | `sqrt(9 - 4*x**2)/x**5` | $\frac{\sqrt{9 - 4 x^{2}}}{x^{5}}$ |
| SOLVED-both | concrete | `x**5*sqrt(4*x**2 - 9)` | $x^{5} \sqrt{4 x^{2} - 9}$ |
| partial | concrete | `x**4*sqrt(4*x**2 - 9)` | $x^{4} \sqrt{4 x^{2} - 9}$ |
| SOLVED-both | concrete | `x**3*sqrt(4*x**2 - 9)` | $x^{3} \sqrt{4 x^{2} - 9}$ |
| partial | concrete | `x**2*sqrt(4*x**2 - 9)` | $x^{2} \sqrt{4 x^{2} - 9}$ |
| SOLVED-both | concrete | `x*sqrt(4*x**2 - 9)` | $x \sqrt{4 x^{2} - 9}$ |
| partial | concrete | `sqrt(4*x**2 - 9)` | $\sqrt{4 x^{2} - 9}$ |
| partial | concrete | `sqrt(4*x**2 - 9)/x` | $\frac{\sqrt{4 x^{2} - 9}}{x}$ |
| partial | concrete | `sqrt(4*x**2 - 9)/x**2` | $\frac{\sqrt{4 x^{2} - 9}}{x^{2}}$ |
| partial | concrete | `sqrt(4*x**2 - 9)/x**3` | $\frac{\sqrt{4 x^{2} - 9}}{x^{3}}$ |
| SOLVED-both | concrete | `sqrt(4*x**2 - 9)/x**4` | $\frac{\sqrt{4 x^{2} - 9}}{x^{4}}$ |
| partial | concrete | `sqrt(4*x**2 - 9)/x**5` | $\frac{\sqrt{4 x^{2} - 9}}{x^{5}}$ |
| SOLVED-both | concrete | `x**5*sqrt(-4*x**2 - 9)` | $x^{5} \sqrt{- 4 x^{2} - 9}$ |
| partial | concrete | `x**4*sqrt(-4*x**2 - 9)` | $x^{4} \sqrt{- 4 x^{2} - 9}$ |
| SOLVED-both | concrete | `x**3*sqrt(-4*x**2 - 9)` | $x^{3} \sqrt{- 4 x^{2} - 9}$ |
| partial | concrete | `x**2*sqrt(-4*x**2 - 9)` | $x^{2} \sqrt{- 4 x^{2} - 9}$ |
| SOLVED-both | concrete | `x*sqrt(-4*x**2 - 9)` | $x \sqrt{- 4 x^{2} - 9}$ |
| partial | concrete | `sqrt(-4*x**2 - 9)` | $\sqrt{- 4 x^{2} - 9}$ |
| partial | concrete | `sqrt(-4*x**2 - 9)/x` | $\frac{\sqrt{- 4 x^{2} - 9}}{x}$ |
| partial | concrete | `sqrt(-4*x**2 - 9)/x**2` | $\frac{\sqrt{- 4 x^{2} - 9}}{x^{2}}$ |
| partial | concrete | `sqrt(-4*x**2 - 9)/x**3` | $\frac{\sqrt{- 4 x^{2} - 9}}{x^{3}}$ |
| SOLVED-both | concrete | `sqrt(-4*x**2 - 9)/x**4` | $\frac{\sqrt{- 4 x^{2} - 9}}{x^{4}}$ |
| partial | concrete | `sqrt(-4*x**2 - 9)/x**5` | $\frac{\sqrt{- 4 x^{2} - 9}}{x^{5}}$ |
| SOLVED-both | parametric | `x**5/sqrt(a + b*x**2)` | $\frac{x^{5}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**4/sqrt(a + b*x**2)` | $\frac{x^{4}}{\sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x**3/sqrt(a + b*x**2)` | $\frac{x^{3}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**2/sqrt(a + b*x**2)` | $\frac{x^{2}}{\sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x/sqrt(a + b*x**2)` | $\frac{x}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/sqrt(a + b*x**2)` | $\frac{1}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x**2))` | $\frac{1}{x \sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `1/(x**2*sqrt(a + b*x**2))` | $\frac{1}{x^{2} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/(x**3*sqrt(a + b*x**2))` | $\frac{1}{x^{3} \sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `1/(x**4*sqrt(a + b*x**2))` | $\frac{1}{x^{4} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/(x**5*sqrt(a + b*x**2))` | $\frac{1}{x^{5} \sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x**5/(a + b*x**2)**(3/2)` | $\frac{x^{5}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/(a + b*x**2)**(3/2)` | $\frac{x^{4}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x**2)**(3/2)` | $\frac{x^{3}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a + b*x**2)**(3/2)` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x/(a + b*x**2)**(3/2)` | $\frac{x}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(-3/2)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**2)**(3/2))` | $\frac{1}{x \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**2*(a + b*x**2)**(3/2))` | $\frac{1}{x^{2} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2)**(3/2))` | $\frac{1}{x^{3} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**4*(a + b*x**2)**(3/2))` | $\frac{1}{x^{4} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**6/(a + b*x**2)**(5/2)` | $\frac{x^{6}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**5/(a + b*x**2)**(5/2)` | $\frac{x^{5}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4/(a + b*x**2)**(5/2)` | $\frac{x^{4}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x**2)**(5/2)` | $\frac{x^{3}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2/(a + b*x**2)**(5/2)` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x/(a + b*x**2)**(5/2)` | $\frac{x}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(-5/2)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**2)**(5/2))` | $\frac{1}{x \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**2*(a + b*x**2)**(5/2))` | $\frac{1}{x^{2} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2)**(5/2))` | $\frac{1}{x^{3} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**4*(a + b*x**2)**(5/2))` | $\frac{1}{x^{4} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**10/(a + b*x**2)**(9/2)` | $\frac{x^{10}}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**9/(a + b*x**2)**(9/2)` | $\frac{x^{9}}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `x**8/(a + b*x**2)**(9/2)` | $\frac{x^{8}}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**7/(a + b*x**2)**(9/2)` | $\frac{x^{7}}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**6/(a + b*x**2)**(9/2)` | $\frac{x^{6}}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**5/(a + b*x**2)**(9/2)` | $\frac{x^{5}}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**4/(a + b*x**2)**(9/2)` | $\frac{x^{4}}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x**2)**(9/2)` | $\frac{x^{3}}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**2/(a + b*x**2)**(9/2)` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x/(a + b*x**2)**(9/2)` | $\frac{x}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(-9/2)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**2)**(9/2))` | $\frac{1}{x \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `1/(x**2*(a + b*x**2)**(9/2))` | $\frac{1}{x^{2} \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2)**(9/2))` | $\frac{1}{x^{3} \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `1/(x**4*(a + b*x**2)**(9/2))` | $\frac{1}{x^{4} \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | concrete | `x**5/sqrt(4*x**2 + 9)` | $\frac{x^{5}}{\sqrt{4 x^{2} + 9}}$ |
| partial | concrete | `x**4/sqrt(4*x**2 + 9)` | $\frac{x^{4}}{\sqrt{4 x^{2} + 9}}$ |
| SOLVED-both | concrete | `x**3/sqrt(4*x**2 + 9)` | $\frac{x^{3}}{\sqrt{4 x^{2} + 9}}$ |
| partial | concrete | `x**2/sqrt(4*x**2 + 9)` | $\frac{x^{2}}{\sqrt{4 x^{2} + 9}}$ |
| SOLVED-both | concrete | `x/sqrt(4*x**2 + 9)` | $\frac{x}{\sqrt{4 x^{2} + 9}}$ |
| partial | concrete | `1/sqrt(4*x**2 + 9)` | $\frac{1}{\sqrt{4 x^{2} + 9}}$ |
| partial | concrete | `1/(x*sqrt(4*x**2 + 9))` | $\frac{1}{x \sqrt{4 x^{2} + 9}}$ |
| SOLVED-both | concrete | `1/(x**2*sqrt(4*x**2 + 9))` | $\frac{1}{x^{2} \sqrt{4 x^{2} + 9}}$ |
| partial | concrete | `1/(x**3*sqrt(4*x**2 + 9))` | $\frac{1}{x^{3} \sqrt{4 x^{2} + 9}}$ |
| SOLVED-both | concrete | `1/(x**4*sqrt(4*x**2 + 9))` | $\frac{1}{x^{4} \sqrt{4 x^{2} + 9}}$ |
| partial | concrete | `1/(x**5*sqrt(4*x**2 + 9))` | $\frac{1}{x^{5} \sqrt{4 x^{2} + 9}}$ |
| SOLVED-both | concrete | `x**5/sqrt(9 - 4*x**2)` | $\frac{x^{5}}{\sqrt{9 - 4 x^{2}}}$ |
| partial | concrete | `x**4/sqrt(9 - 4*x**2)` | $\frac{x^{4}}{\sqrt{9 - 4 x^{2}}}$ |
| SOLVED-both | concrete | `x**3/sqrt(9 - 4*x**2)` | $\frac{x^{3}}{\sqrt{9 - 4 x^{2}}}$ |
| partial | concrete | `x**2/sqrt(9 - 4*x**2)` | $\frac{x^{2}}{\sqrt{9 - 4 x^{2}}}$ |
| SOLVED-both | concrete | `x/sqrt(9 - 4*x**2)` | $\frac{x}{\sqrt{9 - 4 x^{2}}}$ |
| partial | concrete | `1/sqrt(9 - 4*x**2)` | $\frac{1}{\sqrt{9 - 4 x^{2}}}$ |
| partial | concrete | `1/(x*sqrt(9 - 4*x**2))` | $\frac{1}{x \sqrt{9 - 4 x^{2}}}$ |
| SOLVED-both | concrete | `1/(x**2*sqrt(9 - 4*x**2))` | $\frac{1}{x^{2} \sqrt{9 - 4 x^{2}}}$ |
| partial | concrete | `1/(x**3*sqrt(9 - 4*x**2))` | $\frac{1}{x^{3} \sqrt{9 - 4 x^{2}}}$ |
| SOLVED-both | concrete | `1/(x**4*sqrt(9 - 4*x**2))` | $\frac{1}{x^{4} \sqrt{9 - 4 x^{2}}}$ |
| partial | concrete | `1/(x**5*sqrt(9 - 4*x**2))` | $\frac{1}{x^{5} \sqrt{9 - 4 x^{2}}}$ |
| SOLVED-both | concrete | `x**5/sqrt(4*x**2 - 9)` | $\frac{x^{5}}{\sqrt{4 x^{2} - 9}}$ |
| partial | concrete | `x**4/sqrt(4*x**2 - 9)` | $\frac{x^{4}}{\sqrt{4 x^{2} - 9}}$ |
| SOLVED-both | concrete | `x**3/sqrt(4*x**2 - 9)` | $\frac{x^{3}}{\sqrt{4 x^{2} - 9}}$ |
| partial | concrete | `x**2/sqrt(4*x**2 - 9)` | $\frac{x^{2}}{\sqrt{4 x^{2} - 9}}$ |
| SOLVED-both | concrete | `x/sqrt(4*x**2 - 9)` | $\frac{x}{\sqrt{4 x^{2} - 9}}$ |
| partial | concrete | `1/sqrt(4*x**2 - 9)` | $\frac{1}{\sqrt{4 x^{2} - 9}}$ |
| partial | concrete | `1/(x*sqrt(4*x**2 - 9))` | $\frac{1}{x \sqrt{4 x^{2} - 9}}$ |
| SOLVED-both | concrete | `1/(x**2*sqrt(4*x**2 - 9))` | $\frac{1}{x^{2} \sqrt{4 x^{2} - 9}}$ |
| partial | concrete | `1/(x**3*sqrt(4*x**2 - 9))` | $\frac{1}{x^{3} \sqrt{4 x^{2} - 9}}$ |
| SOLVED-both | concrete | `1/(x**4*sqrt(4*x**2 - 9))` | $\frac{1}{x^{4} \sqrt{4 x^{2} - 9}}$ |
| partial | concrete | `1/(x**5*sqrt(4*x**2 - 9))` | $\frac{1}{x^{5} \sqrt{4 x^{2} - 9}}$ |
| SOLVED-both | concrete | `x**5/sqrt(-4*x**2 - 9)` | $\frac{x^{5}}{\sqrt{- 4 x^{2} - 9}}$ |
| partial | concrete | `x**4/sqrt(-4*x**2 - 9)` | $\frac{x^{4}}{\sqrt{- 4 x^{2} - 9}}$ |
| SOLVED-both | concrete | `x**3/sqrt(-4*x**2 - 9)` | $\frac{x^{3}}{\sqrt{- 4 x^{2} - 9}}$ |
| partial | concrete | `x**2/sqrt(-4*x**2 - 9)` | $\frac{x^{2}}{\sqrt{- 4 x^{2} - 9}}$ |
| SOLVED-both | concrete | `x/sqrt(-4*x**2 - 9)` | $\frac{x}{\sqrt{- 4 x^{2} - 9}}$ |
| partial | concrete | `1/sqrt(-4*x**2 - 9)` | $\frac{1}{\sqrt{- 4 x^{2} - 9}}$ |
| partial | concrete | `1/(x*sqrt(-4*x**2 - 9))` | $\frac{1}{x \sqrt{- 4 x^{2} - 9}}$ |
| SOLVED-both | concrete | `1/(x**2*sqrt(-4*x**2 - 9))` | $\frac{1}{x^{2} \sqrt{- 4 x^{2} - 9}}$ |
| partial | concrete | `1/(x**3*sqrt(-4*x**2 - 9))` | $\frac{1}{x^{3} \sqrt{- 4 x^{2} - 9}}$ |
| SOLVED-both | concrete | `1/(x**4*sqrt(-4*x**2 - 9))` | $\frac{1}{x^{4} \sqrt{- 4 x^{2} - 9}}$ |
| partial | concrete | `1/(x**5*sqrt(-4*x**2 - 9))` | $\frac{1}{x^{5} \sqrt{- 4 x^{2} - 9}}$ |
| partial | parametric | `1/sqrt(b*x**2 + 9)` | $\frac{1}{\sqrt{b x^{2} + 9}}$ |
| partial | parametric | `1/sqrt(-b*x**2 + 9)` | $\frac{1}{\sqrt{- b x^{2} + 9}}$ |
| partial | parametric | `1/sqrt(b*x**2 - 9)` | $\frac{1}{\sqrt{b x^{2} - 9}}$ |
| partial | parametric | `1/sqrt(-b*x**2 - 9)` | $\frac{1}{\sqrt{- b x^{2} - 9}}$ |
| partial | parametric | `1/sqrt(b*x**2 + pi)` | $\frac{1}{\sqrt{b x^{2} + \pi}}$ |
| partial | parametric | `1/sqrt(-b*x**2 + pi)` | $\frac{1}{\sqrt{- b x^{2} + \pi}}$ |
| partial | parametric | `1/sqrt(b*x**2 - pi)` | $\frac{1}{\sqrt{b x^{2} - \pi}}$ |
| partial | parametric | `1/sqrt(-b*x**2 - pi)` | $\frac{1}{\sqrt{- b x^{2} - \pi}}$ |
| partial | parametric | `1/sqrt(a + b*x**2)` | $\frac{1}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/sqrt(a - b*x**2)` | $\frac{1}{\sqrt{a - b x^{2}}}$ |
| partial | parametric | `1/sqrt(-a + b*x**2)` | $\frac{1}{\sqrt{- a + b x^{2}}}$ |
| partial | parametric | `1/sqrt(-a - b*x**2)` | $\frac{1}{\sqrt{- a - b x^{2}}}$ |
| partial | parametric | `1/sqrt(a**2 - x**2)` | $\frac{1}{\sqrt{a^{2} - x^{2}}}$ |
| partial | parametric | `(c*x)**(7/2)*sqrt(a + b*x**2)` | $\left(c x\right)^{\frac{7}{2}} \sqrt{a + b x^{2}}$ |
| partial | parametric | `(c*x)**(5/2)*sqrt(a + b*x**2)` | $\left(c x\right)^{\frac{5}{2}} \sqrt{a + b x^{2}}$ |
| partial | parametric | `(c*x)**(3/2)*sqrt(a + b*x**2)` | $\left(c x\right)^{\frac{3}{2}} \sqrt{a + b x^{2}}$ |
| partial | parametric | `sqrt(c*x)*sqrt(a + b*x**2)` | $\sqrt{c x} \sqrt{a + b x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**2)/sqrt(c*x)` | $\frac{\sqrt{a + b x^{2}}}{\sqrt{c x}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(c*x)**(3/2)` | $\frac{\sqrt{a + b x^{2}}}{\left(c x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(c*x)**(5/2)` | $\frac{\sqrt{a + b x^{2}}}{\left(c x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(c*x)**(7/2)` | $\frac{\sqrt{a + b x^{2}}}{\left(c x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(c*x)**(7/2)*(a + b*x**2)**(3/2)` | $\left(c x\right)^{\frac{7}{2}} \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(c*x)**(5/2)*(a + b*x**2)**(3/2)` | $\left(c x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(c*x)**(3/2)*(a + b*x**2)**(3/2)` | $\left(c x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(c*x)*(a + b*x**2)**(3/2)` | $\sqrt{c x} \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/sqrt(c*x)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\sqrt{c x}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(c*x)**(3/2)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(c x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(c*x)**(5/2)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(c x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(c*x)**(7/2)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(c x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(c*x)**(9/2)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(c x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(c*x)**(11/2)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(c x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(c*x)**(5/2)*sqrt(-2*a*x**2 + 3*a)` | $\left(c x\right)^{\frac{5}{2}} \sqrt{- 2 a x^{2} + 3 a}$ |
| partial | parametric | `(c*x)**(3/2)*sqrt(-2*a*x**2 + 3*a)` | $\left(c x\right)^{\frac{3}{2}} \sqrt{- 2 a x^{2} + 3 a}$ |
| partial | parametric | `sqrt(c*x)*sqrt(-2*a*x**2 + 3*a)` | $\sqrt{c x} \sqrt{- 2 a x^{2} + 3 a}$ |
| partial | parametric | `sqrt(-2*a*x**2 + 3*a)/sqrt(c*x)` | $\frac{\sqrt{- 2 a x^{2} + 3 a}}{\sqrt{c x}}$ |
| partial | parametric | `sqrt(-2*a*x**2 + 3*a)/(c*x)**(3/2)` | $\frac{\sqrt{- 2 a x^{2} + 3 a}}{\left(c x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(-2*a*x**2 + 3*a)/(c*x)**(5/2)` | $\frac{\sqrt{- 2 a x^{2} + 3 a}}{\left(c x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c*x)**(7/2)/sqrt(a + b*x**2)` | $\frac{\left(c x\right)^{\frac{7}{2}}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c*x)**(5/2)/sqrt(a + b*x**2)` | $\frac{\left(c x\right)^{\frac{5}{2}}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c*x)**(3/2)/sqrt(a + b*x**2)` | $\frac{\left(c x\right)^{\frac{3}{2}}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `sqrt(c*x)/sqrt(a + b*x**2)` | $\frac{\sqrt{c x}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/(sqrt(c*x)*sqrt(a + b*x**2))` | $\frac{1}{\sqrt{c x} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/((c*x)**(3/2)*sqrt(a + b*x**2))` | $\frac{1}{\left(c x\right)^{\frac{3}{2}} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/((c*x)**(5/2)*sqrt(a + b*x**2))` | $\frac{1}{\left(c x\right)^{\frac{5}{2}} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/((c*x)**(7/2)*sqrt(a + b*x**2))` | $\frac{1}{\left(c x\right)^{\frac{7}{2}} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c*x)**(7/2)/(a + b*x**2)**(3/2)` | $\frac{\left(c x\right)^{\frac{7}{2}}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c*x)**(5/2)/(a + b*x**2)**(3/2)` | $\frac{\left(c x\right)^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c*x)**(3/2)/(a + b*x**2)**(3/2)` | $\frac{\left(c x\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(c*x)/(a + b*x**2)**(3/2)` | $\frac{\sqrt{c x}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(c*x)*(a + b*x**2)**(3/2))` | $\frac{1}{\sqrt{c x} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((c*x)**(3/2)*(a + b*x**2)**(3/2))` | $\frac{1}{\left(c x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((c*x)**(5/2)*(a + b*x**2)**(3/2))` | $\frac{1}{\left(c x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((c*x)**(7/2)*(a + b*x**2)**(3/2))` | $\frac{1}{\left(c x\right)^{\frac{7}{2}} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c*x)**(7/2)/(a + b*x**2)**(5/2)` | $\frac{\left(c x\right)^{\frac{7}{2}}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c*x)**(5/2)/(a + b*x**2)**(5/2)` | $\frac{\left(c x\right)^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c*x)**(3/2)/(a + b*x**2)**(5/2)` | $\frac{\left(c x\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(c*x)/(a + b*x**2)**(5/2)` | $\frac{\sqrt{c x}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(c*x)*(a + b*x**2)**(5/2))` | $\frac{1}{\sqrt{c x} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((c*x)**(3/2)*(a + b*x**2)**(5/2))` | $\frac{1}{\left(c x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((c*x)**(5/2)*(a + b*x**2)**(5/2))` | $\frac{1}{\left(c x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((c*x)**(7/2)*(a + b*x**2)**(5/2))` | $\frac{1}{\left(c x\right)^{\frac{7}{2}} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c*x)**(5/2)/sqrt(-2*a*x**2 + 3*a)` | $\frac{\left(c x\right)^{\frac{5}{2}}}{\sqrt{- 2 a x^{2} + 3 a}}$ |
| partial | parametric | `(c*x)**(3/2)/sqrt(-2*a*x**2 + 3*a)` | $\frac{\left(c x\right)^{\frac{3}{2}}}{\sqrt{- 2 a x^{2} + 3 a}}$ |
| partial | parametric | `sqrt(c*x)/sqrt(-2*a*x**2 + 3*a)` | $\frac{\sqrt{c x}}{\sqrt{- 2 a x^{2} + 3 a}}$ |
| partial | parametric | `1/(sqrt(c*x)*sqrt(-2*a*x**2 + 3*a))` | $\frac{1}{\sqrt{c x} \sqrt{- 2 a x^{2} + 3 a}}$ |
| partial | parametric | `1/((c*x)**(3/2)*sqrt(-2*a*x**2 + 3*a))` | $\frac{1}{\left(c x\right)^{\frac{3}{2}} \sqrt{- 2 a x^{2} + 3 a}}$ |
| partial | parametric | `1/((c*x)**(5/2)*sqrt(-2*a*x**2 + 3*a))` | $\frac{1}{\left(c x\right)^{\frac{5}{2}} \sqrt{- 2 a x^{2} + 3 a}}$ |
| partial | parametric | `(c*x)**(5/2)/(-2*a*x**2 + 3*a)**(3/2)` | $\frac{\left(c x\right)^{\frac{5}{2}}}{\left(- 2 a x^{2} + 3 a\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c*x)**(3/2)/(-2*a*x**2 + 3*a)**(3/2)` | $\frac{\left(c x\right)^{\frac{3}{2}}}{\left(- 2 a x^{2} + 3 a\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(c*x)/(-2*a*x**2 + 3*a)**(3/2)` | $\frac{\sqrt{c x}}{\left(- 2 a x^{2} + 3 a\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(c*x)*(-2*a*x**2 + 3*a)**(3/2))` | $\frac{1}{\sqrt{c x} \left(- 2 a x^{2} + 3 a\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((c*x)**(3/2)*(-2*a*x**2 + 3*a)**(3/2))` | $\frac{1}{\left(c x\right)^{\frac{3}{2}} \left(- 2 a x^{2} + 3 a\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((c*x)**(5/2)*(-2*a*x**2 + 3*a)**(3/2))` | $\frac{1}{\left(c x\right)^{\frac{5}{2}} \left(- 2 a x^{2} + 3 a\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(-a**2*x**2 + 1))` | $\frac{1}{\sqrt{x} \sqrt{- a^{2} x^{2} + 1}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(a*x**2 + 1))` | $\frac{1}{\sqrt{x} \sqrt{a x^{2} + 1}}$ |
| SOLVED-both | parametric | `x**7*(a + b*x**2)**(1/3)` | $x^{7} \sqrt[3]{a + b x^{2}}$ |
| SOLVED-both | parametric | `x**5*(a + b*x**2)**(1/3)` | $x^{5} \sqrt[3]{a + b x^{2}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)**(1/3)` | $x^{3} \sqrt[3]{a + b x^{2}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)**(1/3)` | $x \sqrt[3]{a + b x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/3)/x` | $\frac{\sqrt[3]{a + b x^{2}}}{x}$ |
| partial | parametric | `(a + b*x**2)**(1/3)/x**3` | $\frac{\sqrt[3]{a + b x^{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**2)**(1/3)/x**5` | $\frac{\sqrt[3]{a + b x^{2}}}{x^{5}}$ |
| partial | parametric | `x**4*(a + b*x**2)**(1/3)` | $x^{4} \sqrt[3]{a + b x^{2}}$ |
| partial | parametric | `x**2*(a + b*x**2)**(1/3)` | $x^{2} \sqrt[3]{a + b x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/3)` | $\sqrt[3]{a + b x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/3)/x**2` | $\frac{\sqrt[3]{a + b x^{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/3)/x**4` | $\frac{\sqrt[3]{a + b x^{2}}}{x^{4}}$ |
| SOLVED-both | parametric | `x**7*(a + b*x**2)**(2/3)` | $x^{7} \left(a + b x^{2}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `x**5*(a + b*x**2)**(2/3)` | $x^{5} \left(a + b x^{2}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)**(2/3)` | $x^{3} \left(a + b x^{2}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)**(2/3)` | $x \left(a + b x^{2}\right)^{\frac{2}{3}}$ |
| partial | parametric | `(a + b*x**2)**(2/3)/x` | $\frac{\left(a + b x^{2}\right)^{\frac{2}{3}}}{x}$ |
| partial | parametric | `(a + b*x**2)**(2/3)/x**3` | $\frac{\left(a + b x^{2}\right)^{\frac{2}{3}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**2)**(2/3)/x**5` | $\frac{\left(a + b x^{2}\right)^{\frac{2}{3}}}{x^{5}}$ |
| partial | parametric | `x**4*(a + b*x**2)**(2/3)` | $x^{4} \left(a + b x^{2}\right)^{\frac{2}{3}}$ |
| partial | parametric | `x**2*(a + b*x**2)**(2/3)` | $x^{2} \left(a + b x^{2}\right)^{\frac{2}{3}}$ |
| partial | parametric | `(a + b*x**2)**(2/3)` | $\left(a + b x^{2}\right)^{\frac{2}{3}}$ |
| partial | parametric | `(a + b*x**2)**(2/3)/x**2` | $\frac{\left(a + b x^{2}\right)^{\frac{2}{3}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(2/3)/x**4` | $\frac{\left(a + b x^{2}\right)^{\frac{2}{3}}}{x^{4}}$ |
| SOLVED-both | parametric | `x**7*(a + b*x**2)**(4/3)` | $x^{7} \left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| SOLVED-both | parametric | `x**5*(a + b*x**2)**(4/3)` | $x^{5} \left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)**(4/3)` | $x^{3} \left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)**(4/3)` | $x \left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/x` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{x}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/x**3` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/x**5` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{x^{5}}$ |
| partial | parametric | `x**4*(a + b*x**2)**(4/3)` | $x^{4} \left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `x**2*(a + b*x**2)**(4/3)` | $x^{2} \left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)` | $\left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/x**2` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/x**4` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{x^{4}}$ |
| SOLVED-both | concrete | `x*(x**2 - 1)**(7/3)` | $x \left(x^{2} - 1\right)^{\frac{7}{3}}$ |
| SOLVED-both | parametric | `x**7/(a + b*x**2)**(1/3)` | $\frac{x^{7}}{\sqrt[3]{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x**5/(a + b*x**2)**(1/3)` | $\frac{x^{5}}{\sqrt[3]{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x**2)**(1/3)` | $\frac{x^{3}}{\sqrt[3]{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x/(a + b*x**2)**(1/3)` | $\frac{x}{\sqrt[3]{a + b x^{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**2)**(1/3))` | $\frac{1}{x \sqrt[3]{a + b x^{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2)**(1/3))` | $\frac{1}{x^{3} \sqrt[3]{a + b x^{2}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**2)**(1/3))` | $\frac{1}{x^{5} \sqrt[3]{a + b x^{2}}}$ |
| partial | parametric | `x**4/(a + b*x**2)**(1/3)` | $\frac{x^{4}}{\sqrt[3]{a + b x^{2}}}$ |
| partial | parametric | `x**2/(a + b*x**2)**(1/3)` | $\frac{x^{2}}{\sqrt[3]{a + b x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(-1/3)` | $\frac{1}{\sqrt[3]{a + b x^{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)**(1/3))` | $\frac{1}{x^{2} \sqrt[3]{a + b x^{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)**(1/3))` | $\frac{1}{x^{4} \sqrt[3]{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x**7/(a + b*x**2)**(2/3)` | $\frac{x^{7}}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `x**5/(a + b*x**2)**(2/3)` | $\frac{x^{5}}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x**2)**(2/3)` | $\frac{x^{3}}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `x/(a + b*x**2)**(2/3)` | $\frac{x}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x*(a + b*x**2)**(2/3))` | $\frac{1}{x \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2)**(2/3))` | $\frac{1}{x^{3} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**2)**(2/3))` | $\frac{1}{x^{5} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `x**4/(a + b*x**2)**(2/3)` | $\frac{x^{4}}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `x**2/(a + b*x**2)**(2/3)` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a + b*x**2)**(-2/3)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)**(2/3))` | $\frac{1}{x^{2} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)**(2/3))` | $\frac{1}{x^{4} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `x**7/(a + b*x**2)**(4/3)` | $\frac{x^{7}}{\left(a + b x^{2}\right)^{\frac{4}{3}}}$ |
| SOLVED-both | parametric | `x**5/(a + b*x**2)**(4/3)` | $\frac{x^{5}}{\left(a + b x^{2}\right)^{\frac{4}{3}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x**2)**(4/3)` | $\frac{x^{3}}{\left(a + b x^{2}\right)^{\frac{4}{3}}}$ |
| SOLVED-both | parametric | `x/(a + b*x**2)**(4/3)` | $\frac{x}{\left(a + b x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/(x*(a + b*x**2)**(4/3))` | $\frac{1}{x \left(a + b x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2)**(4/3))` | $\frac{1}{x^{3} \left(a + b x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**2)**(4/3))` | $\frac{1}{x^{5} \left(a + b x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `x**4/(a + b*x**2)**(4/3)` | $\frac{x^{4}}{\left(a + b x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `x**2/(a + b*x**2)**(4/3)` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(a + b*x**2)**(-4/3)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)**(4/3))` | $\frac{1}{x^{2} \left(a + b x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)**(4/3))` | $\frac{1}{x^{4} \left(a + b x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(c*x)**(13/3)*(a + b*x**2)**(1/3)` | $\left(c x\right)^{\frac{13}{3}} \sqrt[3]{a + b x^{2}}$ |
| partial | parametric | `(c*x)**(7/3)*(a + b*x**2)**(1/3)` | $\left(c x\right)^{\frac{7}{3}} \sqrt[3]{a + b x^{2}}$ |
| partial | parametric | `(c*x)**(1/3)*(a + b*x**2)**(1/3)` | $\sqrt[3]{c x} \sqrt[3]{a + b x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/3)/(c*x)**(5/3)` | $\frac{\sqrt[3]{a + b x^{2}}}{\left(c x\right)^{\frac{5}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**(1/3)/(c*x)**(11/3)` | $\frac{\sqrt[3]{a + b x^{2}}}{\left(c x\right)^{\frac{11}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**(1/3)/(c*x)**(17/3)` | $\frac{\sqrt[3]{a + b x^{2}}}{\left(c x\right)^{\frac{17}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**(1/3)/(c*x)**(23/3)` | $\frac{\sqrt[3]{a + b x^{2}}}{\left(c x\right)^{\frac{23}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**(1/3)/(c*x)**(29/3)` | $\frac{\sqrt[3]{a + b x^{2}}}{\left(c x\right)^{\frac{29}{3}}}$ |
| partial | parametric | `(c*x)**(10/3)*(a + b*x**2)**(1/3)` | $\left(c x\right)^{\frac{10}{3}} \sqrt[3]{a + b x^{2}}$ |
| partial | parametric | `(c*x)**(4/3)*(a + b*x**2)**(1/3)` | $\left(c x\right)^{\frac{4}{3}} \sqrt[3]{a + b x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/3)/(c*x)**(2/3)` | $\frac{\sqrt[3]{a + b x^{2}}}{\left(c x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a + b*x**2)**(1/3)/(c*x)**(8/3)` | $\frac{\sqrt[3]{a + b x^{2}}}{\left(c x\right)^{\frac{8}{3}}}$ |
| partial | parametric | `(a + b*x**2)**(1/3)/(c*x)**(14/3)` | $\frac{\sqrt[3]{a + b x^{2}}}{\left(c x\right)^{\frac{14}{3}}}$ |
| partial | parametric | `(c*x)**(2/3)*(a + b*x**2)**(1/3)` | $\left(c x\right)^{\frac{2}{3}} \sqrt[3]{a + b x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/3)/(c*x)**(1/3)` | $\frac{\sqrt[3]{a + b x^{2}}}{\sqrt[3]{c x}}$ |
| partial | parametric | `(a + b*x**2)**(1/3)/(c*x)**(4/3)` | $\frac{\sqrt[3]{a + b x^{2}}}{\left(c x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(c*x)**(13/3)*(a + b*x**2)**(4/3)` | $\left(c x\right)^{\frac{13}{3}} \left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(c*x)**(7/3)*(a + b*x**2)**(4/3)` | $\left(c x\right)^{\frac{7}{3}} \left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(c*x)**(1/3)*(a + b*x**2)**(4/3)` | $\sqrt[3]{c x} \left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/(c*x)**(5/3)` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{\left(c x\right)^{\frac{5}{3}}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/(c*x)**(11/3)` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{\left(c x\right)^{\frac{11}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**(4/3)/(c*x)**(17/3)` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{\left(c x\right)^{\frac{17}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**(4/3)/(c*x)**(23/3)` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{\left(c x\right)^{\frac{23}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**(4/3)/(c*x)**(29/3)` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{\left(c x\right)^{\frac{29}{3}}}$ |
| partial | parametric | `(c*x)**(10/3)*(a + b*x**2)**(4/3)` | $\left(c x\right)^{\frac{10}{3}} \left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(c*x)**(4/3)*(a + b*x**2)**(4/3)` | $\left(c x\right)^{\frac{4}{3}} \left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/(c*x)**(2/3)` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{\left(c x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/(c*x)**(8/3)` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{\left(c x\right)^{\frac{8}{3}}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/(c*x)**(14/3)` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{\left(c x\right)^{\frac{14}{3}}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/(c*x)**(20/3)` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{\left(c x\right)^{\frac{20}{3}}}$ |
| partial | parametric | `(c*x)**(2/3)*(a + b*x**2)**(4/3)` | $\left(c x\right)^{\frac{2}{3}} \left(a + b x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/(c*x)**(1/3)` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{\sqrt[3]{c x}}$ |
| partial | parametric | `(a + b*x**2)**(4/3)/(c*x)**(4/3)` | $\frac{\left(a + b x^{2}\right)^{\frac{4}{3}}}{\left(c x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(c*x)**(19/3)/(a + b*x**2)**(2/3)` | $\frac{\left(c x\right)^{\frac{19}{3}}}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(c*x)**(13/3)/(a + b*x**2)**(2/3)` | $\frac{\left(c x\right)^{\frac{13}{3}}}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(c*x)**(7/3)/(a + b*x**2)**(2/3)` | $\frac{\left(c x\right)^{\frac{7}{3}}}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(c*x)**(1/3)/(a + b*x**2)**(2/3)` | $\frac{\sqrt[3]{c x}}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `1/((c*x)**(5/3)*(a + b*x**2)**(2/3))` | $\frac{1}{\left(c x\right)^{\frac{5}{3}} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| **SOLVED-NEW** | parametric | `1/((c*x)**(11/3)*(a + b*x**2)**(2/3))` | $\frac{1}{\left(c x\right)^{\frac{11}{3}} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| **SOLVED-NEW** | parametric | `1/((c*x)**(17/3)*(a + b*x**2)**(2/3))` | $\frac{1}{\left(c x\right)^{\frac{17}{3}} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| **SOLVED-NEW** | parametric | `1/((c*x)**(23/3)*(a + b*x**2)**(2/3))` | $\frac{1}{\left(c x\right)^{\frac{23}{3}} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(c*x)**(10/3)/(a + b*x**2)**(2/3)` | $\frac{\left(c x\right)^{\frac{10}{3}}}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(c*x)**(4/3)/(a + b*x**2)**(2/3)` | $\frac{\left(c x\right)^{\frac{4}{3}}}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((c*x)**(2/3)*(a + b*x**2)**(2/3))` | $\frac{1}{\left(c x\right)^{\frac{2}{3}} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((c*x)**(8/3)*(a + b*x**2)**(2/3))` | $\frac{1}{\left(c x\right)^{\frac{8}{3}} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((c*x)**(14/3)*(a + b*x**2)**(2/3))` | $\frac{1}{\left(c x\right)^{\frac{14}{3}} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(c*x)**(2/3)/(a + b*x**2)**(2/3)` | $\frac{\left(c x\right)^{\frac{2}{3}}}{\left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((c*x)**(1/3)*(a + b*x**2)**(2/3))` | $\frac{1}{\sqrt[3]{c x} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((c*x)**(4/3)*(a + b*x**2)**(2/3))` | $\frac{1}{\left(c x\right)^{\frac{4}{3}} \left(a + b x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `x**4*(a + b*x**2)**(1/4)` | $x^{4} \sqrt[4]{a + b x^{2}}$ |
| partial | parametric | `x**2*(a + b*x**2)**(1/4)` | $x^{2} \sqrt[4]{a + b x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/4)` | $\sqrt[4]{a + b x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/4)/x**2` | $\frac{\sqrt[4]{a + b x^{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/4)/x**4` | $\frac{\sqrt[4]{a + b x^{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**2)**(1/4)/x**6` | $\frac{\sqrt[4]{a + b x^{2}}}{x^{6}}$ |
| partial | parametric | `x**4*(a - b*x**2)**(1/4)` | $x^{4} \sqrt[4]{a - b x^{2}}$ |
| partial | parametric | `x**2*(a - b*x**2)**(1/4)` | $x^{2} \sqrt[4]{a - b x^{2}}$ |
| partial | parametric | `(a - b*x**2)**(1/4)` | $\sqrt[4]{a - b x^{2}}$ |
| partial | parametric | `(a - b*x**2)**(1/4)/x**2` | $\frac{\sqrt[4]{a - b x^{2}}}{x^{2}}$ |
| partial | parametric | `(a - b*x**2)**(1/4)/x**4` | $\frac{\sqrt[4]{a - b x^{2}}}{x^{4}}$ |
| partial | parametric | `(a - b*x**2)**(1/4)/x**6` | $\frac{\sqrt[4]{a - b x^{2}}}{x^{6}}$ |
| partial | parametric | `x**4*(a + b*x**2)**(3/4)` | $x^{4} \left(a + b x^{2}\right)^{\frac{3}{4}}$ |
| partial | parametric | `x**2*(a + b*x**2)**(3/4)` | $x^{2} \left(a + b x^{2}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(a + b*x**2)**(3/4)` | $\left(a + b x^{2}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(a + b*x**2)**(3/4)/x**2` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{4}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(3/4)/x**4` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{4}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**2)**(3/4)/x**6` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{4}}}{x^{6}}$ |
| partial | parametric | `x**4*(a - b*x**2)**(3/4)` | $x^{4} \left(a - b x^{2}\right)^{\frac{3}{4}}$ |
| partial | parametric | `x**2*(a - b*x**2)**(3/4)` | $x^{2} \left(a - b x^{2}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(a - b*x**2)**(3/4)` | $\left(a - b x^{2}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(a - b*x**2)**(3/4)/x**2` | $\frac{\left(a - b x^{2}\right)^{\frac{3}{4}}}{x^{2}}$ |
| partial | parametric | `(a - b*x**2)**(3/4)/x**4` | $\frac{\left(a - b x^{2}\right)^{\frac{3}{4}}}{x^{4}}$ |
| partial | parametric | `(a - b*x**2)**(3/4)/x**6` | $\frac{\left(a - b x^{2}\right)^{\frac{3}{4}}}{x^{6}}$ |
| partial | parametric | `(a + b*x**2)**(5/4)` | $\left(a + b x^{2}\right)^{\frac{5}{4}}$ |
| partial | parametric | `(a - b*x**2)**(5/4)` | $\left(a - b x^{2}\right)^{\frac{5}{4}}$ |
| partial | parametric | `(a + b*x**2)**(7/4)` | $\left(a + b x^{2}\right)^{\frac{7}{4}}$ |
| partial | parametric | `(a - b*x**2)**(7/4)` | $\left(a - b x^{2}\right)^{\frac{7}{4}}$ |
| partial | parametric | `x**6/(a + b*x**2)**(1/4)` | $\frac{x^{6}}{\sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `x**4/(a + b*x**2)**(1/4)` | $\frac{x^{4}}{\sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `x**2/(a + b*x**2)**(1/4)` | $\frac{x^{2}}{\sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(-1/4)` | $\frac{1}{\sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)**(1/4))` | $\frac{1}{x^{2} \sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)**(1/4))` | $\frac{1}{x^{4} \sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `1/(x**6*(a + b*x**2)**(1/4))` | $\frac{1}{x^{6} \sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `x**6/(a - b*x**2)**(1/4)` | $\frac{x^{6}}{\sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `x**4/(a - b*x**2)**(1/4)` | $\frac{x^{4}}{\sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `x**2/(a - b*x**2)**(1/4)` | $\frac{x^{2}}{\sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `(a - b*x**2)**(-1/4)` | $\frac{1}{\sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `1/(x**2*(a - b*x**2)**(1/4))` | $\frac{1}{x^{2} \sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `1/(x**4*(a - b*x**2)**(1/4))` | $\frac{1}{x^{4} \sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `1/(x**6*(a - b*x**2)**(1/4))` | $\frac{1}{x^{6} \sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `x**6/(a + b*x**2)**(3/4)` | $\frac{x^{6}}{\left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**4/(a + b*x**2)**(3/4)` | $\frac{x^{4}}{\left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**2/(a + b*x**2)**(3/4)` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(a + b*x**2)**(-3/4)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)**(3/4))` | $\frac{1}{x^{2} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)**(3/4))` | $\frac{1}{x^{4} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**6*(a + b*x**2)**(3/4))` | $\frac{1}{x^{6} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**6/(a - b*x**2)**(3/4)` | $\frac{x^{6}}{\left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**4/(a - b*x**2)**(3/4)` | $\frac{x^{4}}{\left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**2/(a - b*x**2)**(3/4)` | $\frac{x^{2}}{\left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(a - b*x**2)**(-3/4)` | $\frac{1}{\left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**2*(a - b*x**2)**(3/4))` | $\frac{1}{x^{2} \left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**4*(a - b*x**2)**(3/4))` | $\frac{1}{x^{4} \left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**6*(a - b*x**2)**(3/4))` | $\frac{1}{x^{6} \left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**6/(a + b*x**2)**(5/4)` | $\frac{x^{6}}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**4/(a + b*x**2)**(5/4)` | $\frac{x^{4}}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**2/(a + b*x**2)**(5/4)` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(a + b*x**2)**(-5/4)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)**(5/4))` | $\frac{1}{x^{2} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)**(5/4))` | $\frac{1}{x^{4} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**6*(a + b*x**2)**(5/4))` | $\frac{1}{x^{6} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**6/(a - b*x**2)**(5/4)` | $\frac{x^{6}}{\left(a - b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**4/(a - b*x**2)**(5/4)` | $\frac{x^{4}}{\left(a - b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**2/(a - b*x**2)**(5/4)` | $\frac{x^{2}}{\left(a - b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(a - b*x**2)**(-5/4)` | $\frac{1}{\left(a - b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**2*(a - b*x**2)**(5/4))` | $\frac{1}{x^{2} \left(a - b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**4*(a - b*x**2)**(5/4))` | $\frac{1}{x^{4} \left(a - b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**6*(a - b*x**2)**(5/4))` | $\frac{1}{x^{6} \left(a - b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(a + b*x**2)**(-7/4)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(a + b*x**2)**(-9/4)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(a + b*x**2)**(-11/4)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{11}{4}}}$ |
| partial | parametric | `(a - b*x**2)**(-7/4)` | $\frac{1}{\left(a - b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(a - b*x**2)**(-9/4)` | $\frac{1}{\left(a - b x^{2}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(a - b*x**2)**(-11/4)` | $\frac{1}{\left(a - b x^{2}\right)^{\frac{11}{4}}}$ |
| partial | concrete | `x**6/(3*x**2 + 2)**(1/4)` | $\frac{x^{6}}{\sqrt[4]{3 x^{2} + 2}}$ |
| partial | concrete | `x**4/(3*x**2 + 2)**(1/4)` | $\frac{x^{4}}{\sqrt[4]{3 x^{2} + 2}}$ |
| partial | concrete | `x**2/(3*x**2 + 2)**(1/4)` | $\frac{x^{2}}{\sqrt[4]{3 x^{2} + 2}}$ |
| partial | concrete | `(3*x**2 + 2)**(-1/4)` | $\frac{1}{\sqrt[4]{3 x^{2} + 2}}$ |
| partial | concrete | `1/(x**2*(3*x**2 + 2)**(1/4))` | $\frac{1}{x^{2} \sqrt[4]{3 x^{2} + 2}}$ |
| partial | concrete | `1/(x**4*(3*x**2 + 2)**(1/4))` | $\frac{1}{x^{4} \sqrt[4]{3 x^{2} + 2}}$ |
| partial | concrete | `1/(x**6*(3*x**2 + 2)**(1/4))` | $\frac{1}{x^{6} \sqrt[4]{3 x^{2} + 2}}$ |
| partial | concrete | `x**6/(2 - 3*x**2)**(1/4)` | $\frac{x^{6}}{\sqrt[4]{2 - 3 x^{2}}}$ |
| partial | concrete | `x**4/(2 - 3*x**2)**(1/4)` | $\frac{x^{4}}{\sqrt[4]{2 - 3 x^{2}}}$ |
| partial | concrete | `x**2/(2 - 3*x**2)**(1/4)` | $\frac{x^{2}}{\sqrt[4]{2 - 3 x^{2}}}$ |
| partial | concrete | `(2 - 3*x**2)**(-1/4)` | $\frac{1}{\sqrt[4]{2 - 3 x^{2}}}$ |
| partial | concrete | `1/(x**2*(2 - 3*x**2)**(1/4))` | $\frac{1}{x^{2} \sqrt[4]{2 - 3 x^{2}}}$ |
| partial | concrete | `1/(x**4*(2 - 3*x**2)**(1/4))` | $\frac{1}{x^{4} \sqrt[4]{2 - 3 x^{2}}}$ |
| partial | concrete | `1/(x**6*(2 - 3*x**2)**(1/4))` | $\frac{1}{x^{6} \sqrt[4]{2 - 3 x^{2}}}$ |
| partial | concrete | `x**6/(3*x**2 + 2)**(3/4)` | $\frac{x^{6}}{\left(3 x^{2} + 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**4/(3*x**2 + 2)**(3/4)` | $\frac{x^{4}}{\left(3 x^{2} + 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**2/(3*x**2 + 2)**(3/4)` | $\frac{x^{2}}{\left(3 x^{2} + 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `(3*x**2 + 2)**(-3/4)` | $\frac{1}{\left(3 x^{2} + 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**2*(3*x**2 + 2)**(3/4))` | $\frac{1}{x^{2} \left(3 x^{2} + 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**4*(3*x**2 + 2)**(3/4))` | $\frac{1}{x^{4} \left(3 x^{2} + 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**6*(3*x**2 + 2)**(3/4))` | $\frac{1}{x^{6} \left(3 x^{2} + 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**6/(2 - 3*x**2)**(3/4)` | $\frac{x^{6}}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**4/(2 - 3*x**2)**(3/4)` | $\frac{x^{4}}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**2/(2 - 3*x**2)**(3/4)` | $\frac{x^{2}}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}}}$ |
| partial | concrete | `(2 - 3*x**2)**(-3/4)` | $\frac{1}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**2*(2 - 3*x**2)**(3/4))` | $\frac{1}{x^{2} \left(2 - 3 x^{2}\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**4*(2 - 3*x**2)**(3/4))` | $\frac{1}{x^{4} \left(2 - 3 x^{2}\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**6*(2 - 3*x**2)**(3/4))` | $\frac{1}{x^{6} \left(2 - 3 x^{2}\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**6/(3*x**2 - 2)**(1/4)` | $\frac{x^{6}}{\sqrt[4]{3 x^{2} - 2}}$ |
| partial | concrete | `x**4/(3*x**2 - 2)**(1/4)` | $\frac{x^{4}}{\sqrt[4]{3 x^{2} - 2}}$ |
| partial | concrete | `x**2/(3*x**2 - 2)**(1/4)` | $\frac{x^{2}}{\sqrt[4]{3 x^{2} - 2}}$ |
| partial | concrete | `(3*x**2 - 2)**(-1/4)` | $\frac{1}{\sqrt[4]{3 x^{2} - 2}}$ |
| partial | concrete | `1/(x**2*(3*x**2 - 2)**(1/4))` | $\frac{1}{x^{2} \sqrt[4]{3 x^{2} - 2}}$ |
| partial | concrete | `1/(x**4*(3*x**2 - 2)**(1/4))` | $\frac{1}{x^{4} \sqrt[4]{3 x^{2} - 2}}$ |
| partial | concrete | `1/(x**6*(3*x**2 - 2)**(1/4))` | $\frac{1}{x^{6} \sqrt[4]{3 x^{2} - 2}}$ |
| partial | concrete | `x**6/(-3*x**2 - 2)**(1/4)` | $\frac{x^{6}}{\sqrt[4]{- 3 x^{2} - 2}}$ |
| partial | concrete | `x**4/(-3*x**2 - 2)**(1/4)` | $\frac{x^{4}}{\sqrt[4]{- 3 x^{2} - 2}}$ |
| partial | concrete | `x**2/(-3*x**2 - 2)**(1/4)` | $\frac{x^{2}}{\sqrt[4]{- 3 x^{2} - 2}}$ |
| partial | concrete | `(-3*x**2 - 2)**(-1/4)` | $\frac{1}{\sqrt[4]{- 3 x^{2} - 2}}$ |
| partial | concrete | `1/(x**2*(-3*x**2 - 2)**(1/4))` | $\frac{1}{x^{2} \sqrt[4]{- 3 x^{2} - 2}}$ |
| partial | concrete | `1/(x**4*(-3*x**2 - 2)**(1/4))` | $\frac{1}{x^{4} \sqrt[4]{- 3 x^{2} - 2}}$ |
| partial | concrete | `1/(x**6*(-3*x**2 - 2)**(1/4))` | $\frac{1}{x^{6} \sqrt[4]{- 3 x^{2} - 2}}$ |
| partial | concrete | `x**6/(3*x**2 - 2)**(3/4)` | $\frac{x^{6}}{\left(3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**4/(3*x**2 - 2)**(3/4)` | $\frac{x^{4}}{\left(3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**2/(3*x**2 - 2)**(3/4)` | $\frac{x^{2}}{\left(3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `(3*x**2 - 2)**(-3/4)` | $\frac{1}{\left(3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**2*(3*x**2 - 2)**(3/4))` | $\frac{1}{x^{2} \left(3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**4*(3*x**2 - 2)**(3/4))` | $\frac{1}{x^{4} \left(3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**6*(3*x**2 - 2)**(3/4))` | $\frac{1}{x^{6} \left(3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**6/(-3*x**2 - 2)**(3/4)` | $\frac{x^{6}}{\left(- 3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**4/(-3*x**2 - 2)**(3/4)` | $\frac{x^{4}}{\left(- 3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**2/(-3*x**2 - 2)**(3/4)` | $\frac{x^{2}}{\left(- 3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `(-3*x**2 - 2)**(-3/4)` | $\frac{1}{\left(- 3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**2*(-3*x**2 - 2)**(3/4))` | $\frac{1}{x^{2} \left(- 3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**4*(-3*x**2 - 2)**(3/4))` | $\frac{1}{x^{4} \left(- 3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**6*(-3*x**2 - 2)**(3/4))` | $\frac{1}{x^{6} \left(- 3 x^{2} - 2\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(c*x)**(7/2)*(a + b*x**2)**(1/4)` | $\left(c x\right)^{\frac{7}{2}} \sqrt[4]{a + b x^{2}}$ |
| partial | parametric | `(c*x)**(3/2)*(a + b*x**2)**(1/4)` | $\left(c x\right)^{\frac{3}{2}} \sqrt[4]{a + b x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/4)/sqrt(c*x)` | $\frac{\sqrt[4]{a + b x^{2}}}{\sqrt{c x}}$ |
| partial | parametric | `(a + b*x**2)**(1/4)/(c*x)**(5/2)` | $\frac{\sqrt[4]{a + b x^{2}}}{\left(c x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)**(1/4)/(c*x)**(9/2)` | $\frac{\sqrt[4]{a + b x^{2}}}{\left(c x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x**2)**(1/4)/(c*x)**(13/2)` | $\frac{\sqrt[4]{a + b x^{2}}}{\left(c x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(c*x)**(5/2)*(a + b*x**2)**(1/4)` | $\left(c x\right)^{\frac{5}{2}} \sqrt[4]{a + b x^{2}}$ |
| partial | parametric | `sqrt(c*x)*(a + b*x**2)**(1/4)` | $\sqrt{c x} \sqrt[4]{a + b x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/4)/(c*x)**(3/2)` | $\frac{\sqrt[4]{a + b x^{2}}}{\left(c x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(1/4)/(c*x)**(7/2)` | $\frac{\sqrt[4]{a + b x^{2}}}{\left(c x\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**(1/4)/(c*x)**(11/2)` | $\frac{\sqrt[4]{a + b x^{2}}}{\left(c x\right)^{\frac{11}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**(1/4)/(c*x)**(15/2)` | $\frac{\sqrt[4]{a + b x^{2}}}{\left(c x\right)^{\frac{15}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**(1/4)/(c*x)**(19/2)` | $\frac{\sqrt[4]{a + b x^{2}}}{\left(c x\right)^{\frac{19}{2}}}$ |
| partial | parametric | `(c*x)**(3/2)*(a - b*x**2)**(1/4)` | $\left(c x\right)^{\frac{3}{2}} \sqrt[4]{a - b x^{2}}$ |
| partial | parametric | `(a - b*x**2)**(1/4)/sqrt(c*x)` | $\frac{\sqrt[4]{a - b x^{2}}}{\sqrt{c x}}$ |
| partial | parametric | `(a - b*x**2)**(1/4)/(c*x)**(5/2)` | $\frac{\sqrt[4]{a - b x^{2}}}{\left(c x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a - b*x**2)**(1/4)/(c*x)**(9/2)` | $\frac{\sqrt[4]{a - b x^{2}}}{\left(c x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a - b*x**2)**(1/4)/(c*x)**(13/2)` | $\frac{\sqrt[4]{a - b x^{2}}}{\left(c x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(c*x)**(5/2)*(a - b*x**2)**(1/4)` | $\left(c x\right)^{\frac{5}{2}} \sqrt[4]{a - b x^{2}}$ |
| partial | parametric | `sqrt(c*x)*(a - b*x**2)**(1/4)` | $\sqrt{c x} \sqrt[4]{a - b x^{2}}$ |
| partial | parametric | `(a - b*x**2)**(1/4)/(c*x)**(3/2)` | $\frac{\sqrt[4]{a - b x^{2}}}{\left(c x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a - b*x**2)**(1/4)/(c*x)**(7/2)` | $\frac{\sqrt[4]{a - b x^{2}}}{\left(c x\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a - b*x**2)**(1/4)/(c*x)**(11/2)` | $\frac{\sqrt[4]{a - b x^{2}}}{\left(c x\right)^{\frac{11}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a - b*x**2)**(1/4)/(c*x)**(15/2)` | $\frac{\sqrt[4]{a - b x^{2}}}{\left(c x\right)^{\frac{15}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a - b*x**2)**(1/4)/(c*x)**(19/2)` | $\frac{\sqrt[4]{a - b x^{2}}}{\left(c x\right)^{\frac{19}{2}}}$ |
| partial | parametric | `(c*x)**(3/2)/(a + b*x**2)**(1/4)` | $\frac{\left(c x\right)^{\frac{3}{2}}}{\sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `1/(sqrt(c*x)*(a + b*x**2)**(1/4))` | $\frac{1}{\sqrt{c x} \sqrt[4]{a + b x^{2}}}$ |
| SOLVED-both | parametric | `1/((c*x)**(5/2)*(a + b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{5}{2}} \sqrt[4]{a + b x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((c*x)**(9/2)*(a + b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{9}{2}} \sqrt[4]{a + b x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((c*x)**(13/2)*(a + b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{13}{2}} \sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `(c*x)**(9/2)/(a + b*x**2)**(1/4)` | $\frac{\left(c x\right)^{\frac{9}{2}}}{\sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `(c*x)**(5/2)/(a + b*x**2)**(1/4)` | $\frac{\left(c x\right)^{\frac{5}{2}}}{\sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `sqrt(c*x)/(a + b*x**2)**(1/4)` | $\frac{\sqrt{c x}}{\sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `1/((c*x)**(3/2)*(a + b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{3}{2}} \sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `1/((c*x)**(7/2)*(a + b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{7}{2}} \sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `1/((c*x)**(11/2)*(a + b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{11}{2}} \sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `(c*x)**(3/2)/(a - b*x**2)**(1/4)` | $\frac{\left(c x\right)^{\frac{3}{2}}}{\sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `1/(sqrt(c*x)*(a - b*x**2)**(1/4))` | $\frac{1}{\sqrt{c x} \sqrt[4]{a - b x^{2}}}$ |
| SOLVED-both | parametric | `1/((c*x)**(5/2)*(a - b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{5}{2}} \sqrt[4]{a - b x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((c*x)**(9/2)*(a - b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{9}{2}} \sqrt[4]{a - b x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((c*x)**(13/2)*(a - b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{13}{2}} \sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `(c*x)**(5/2)/(a - b*x**2)**(1/4)` | $\frac{\left(c x\right)^{\frac{5}{2}}}{\sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `sqrt(c*x)/(a - b*x**2)**(1/4)` | $\frac{\sqrt{c x}}{\sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `1/((c*x)**(3/2)*(a - b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{3}{2}} \sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `1/((c*x)**(7/2)*(a - b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{7}{2}} \sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `1/((c*x)**(11/2)*(a - b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{11}{2}} \sqrt[4]{a - b x^{2}}}$ |
| partial | parametric | `(c*x)**(3/2)/(a + b*x**2)**(3/4)` | $\frac{\left(c x\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(sqrt(c*x)*(a + b*x**2)**(3/4))` | $\frac{1}{\sqrt{c x} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((c*x)**(5/2)*(a + b*x**2)**(3/4))` | $\frac{1}{\left(c x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((c*x)**(9/2)*(a + b*x**2)**(3/4))` | $\frac{1}{\left(c x\right)^{\frac{9}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((c*x)**(13/2)*(a + b*x**2)**(3/4))` | $\frac{1}{\left(c x\right)^{\frac{13}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(c*x)**(5/2)/(a + b*x**2)**(3/4)` | $\frac{\left(c x\right)^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `sqrt(c*x)/(a + b*x**2)**(3/4)` | $\frac{\sqrt{c x}}{\left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `1/((c*x)**(3/2)*(a + b*x**2)**(3/4))` | $\frac{1}{\left(c x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `1/((c*x)**(7/2)*(a + b*x**2)**(3/4))` | $\frac{1}{\left(c x\right)^{\frac{7}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| **SOLVED-NEW** | parametric | `1/((c*x)**(11/2)*(a + b*x**2)**(3/4))` | $\frac{1}{\left(c x\right)^{\frac{11}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(c*x)**(3/2)/(a - b*x**2)**(3/4)` | $\frac{\left(c x\right)^{\frac{3}{2}}}{\left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(sqrt(c*x)*(a - b*x**2)**(3/4))` | $\frac{1}{\sqrt{c x} \left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((c*x)**(5/2)*(a - b*x**2)**(3/4))` | $\frac{1}{\left(c x\right)^{\frac{5}{2}} \left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((c*x)**(9/2)*(a - b*x**2)**(3/4))` | $\frac{1}{\left(c x\right)^{\frac{9}{2}} \left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((c*x)**(13/2)*(a - b*x**2)**(3/4))` | $\frac{1}{\left(c x\right)^{\frac{13}{2}} \left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(c*x)**(5/2)/(a - b*x**2)**(3/4)` | $\frac{\left(c x\right)^{\frac{5}{2}}}{\left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `sqrt(c*x)/(a - b*x**2)**(3/4)` | $\frac{\sqrt{c x}}{\left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `1/((c*x)**(3/2)*(a - b*x**2)**(3/4))` | $\frac{1}{\left(c x\right)^{\frac{3}{2}} \left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `1/((c*x)**(7/2)*(a - b*x**2)**(3/4))` | $\frac{1}{\left(c x\right)^{\frac{7}{2}} \left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| **SOLVED-NEW** | parametric | `1/((c*x)**(11/2)*(a - b*x**2)**(3/4))` | $\frac{1}{\left(c x\right)^{\frac{11}{2}} \left(a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(c*x)**(7/2)/(a + b*x**2)**(5/4)` | $\frac{\left(c x\right)^{\frac{7}{2}}}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(c*x)**(3/2)/(a + b*x**2)**(5/4)` | $\frac{\left(c x\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| SOLVED-both | parametric | `1/(sqrt(c*x)*(a + b*x**2)**(5/4))` | $\frac{1}{\sqrt{c x} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| SOLVED-both | parametric | `1/((c*x)**(5/2)*(a + b*x**2)**(5/4))` | $\frac{1}{\left(c x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| **SOLVED-NEW** | parametric | `1/((c*x)**(9/2)*(a + b*x**2)**(5/4))` | $\frac{1}{\left(c x\right)^{\frac{9}{2}} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| **SOLVED-NEW** | parametric | `1/((c*x)**(13/2)*(a + b*x**2)**(5/4))` | $\frac{1}{\left(c x\right)^{\frac{13}{2}} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(c*x)**(13/2)/(a + b*x**2)**(5/4)` | $\frac{\left(c x\right)^{\frac{13}{2}}}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(c*x)**(9/2)/(a + b*x**2)**(5/4)` | $\frac{\left(c x\right)^{\frac{9}{2}}}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(c*x)**(5/2)/(a + b*x**2)**(5/4)` | $\frac{\left(c x\right)^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `sqrt(c*x)/(a + b*x**2)**(5/4)` | $\frac{\sqrt{c x}}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((c*x)**(3/2)*(a + b*x**2)**(5/4))` | $\frac{1}{\left(c x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((c*x)**(7/2)*(a + b*x**2)**(5/4))` | $\frac{1}{\left(c x\right)^{\frac{7}{2}} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((c*x)**(11/2)*(a + b*x**2)**(5/4))` | $\frac{1}{\left(c x\right)^{\frac{11}{2}} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(c*x)**(5/4)/(a + b*x**2)**(1/4)` | $\frac{\left(c x\right)^{\frac{5}{4}}}{\sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `(c*x)**(3/4)/(a + b*x**2)**(1/4)` | $\frac{\left(c x\right)^{\frac{3}{4}}}{\sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `(c*x)**(1/4)/(a + b*x**2)**(1/4)` | $\frac{\sqrt[4]{c x}}{\sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `1/((c*x)**(1/4)*(a + b*x**2)**(1/4))` | $\frac{1}{\sqrt[4]{c x} \sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `1/((c*x)**(3/4)*(a + b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{3}{4}} \sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `1/((c*x)**(5/4)*(a + b*x**2)**(1/4))` | $\frac{1}{\left(c x\right)^{\frac{5}{4}} \sqrt[4]{a + b x^{2}}}$ |
| partial | parametric | `(c*x)**(5/4)/(a + b*x**2)**(7/4)` | $\frac{\left(c x\right)^{\frac{5}{4}}}{\left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(c*x)**(3/4)/(a + b*x**2)**(7/4)` | $\frac{\left(c x\right)^{\frac{3}{4}}}{\left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(c*x)**(1/4)/(a + b*x**2)**(7/4)` | $\frac{\sqrt[4]{c x}}{\left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/((c*x)**(1/4)*(a + b*x**2)**(7/4))` | $\frac{1}{\sqrt[4]{c x} \left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/((c*x)**(3/4)*(a + b*x**2)**(7/4))` | $\frac{1}{\left(c x\right)^{\frac{3}{4}} \left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `1/((c*x)**(5/4)*(a + b*x**2)**(7/4))` | $\frac{1}{\left(c x\right)^{\frac{5}{4}} \left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `x**6*(a + b*x**2)**(1/6)` | $x^{6} \sqrt[6]{a + b x^{2}}$ |
| partial | parametric | `x**4*(a + b*x**2)**(1/6)` | $x^{4} \sqrt[6]{a + b x^{2}}$ |
| partial | parametric | `x**2*(a + b*x**2)**(1/6)` | $x^{2} \sqrt[6]{a + b x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/6)` | $\sqrt[6]{a + b x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/6)/x**2` | $\frac{\sqrt[6]{a + b x^{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/6)/x**4` | $\frac{\sqrt[6]{a + b x^{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**2)**(1/6)/x**6` | $\frac{\sqrt[6]{a + b x^{2}}}{x^{6}}$ |
| partial | parametric | `(a + b*x**2)**(1/6)/x**8` | $\frac{\sqrt[6]{a + b x^{2}}}{x^{8}}$ |
| partial | parametric | `x**6/(a + b*x**2)**(1/6)` | $\frac{x^{6}}{\sqrt[6]{a + b x^{2}}}$ |
| partial | parametric | `x**4/(a + b*x**2)**(1/6)` | $\frac{x^{4}}{\sqrt[6]{a + b x^{2}}}$ |
| partial | parametric | `x**2/(a + b*x**2)**(1/6)` | $\frac{x^{2}}{\sqrt[6]{a + b x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(-1/6)` | $\frac{1}{\sqrt[6]{a + b x^{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)**(1/6))` | $\frac{1}{x^{2} \sqrt[6]{a + b x^{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)**(1/6))` | $\frac{1}{x^{4} \sqrt[6]{a + b x^{2}}}$ |
| partial | parametric | `1/(x**6*(a + b*x**2)**(1/6))` | $\frac{1}{x^{6} \sqrt[6]{a + b x^{2}}}$ |
| partial | parametric | `x**6/(a + b*x**2)**(5/6)` | $\frac{x^{6}}{\left(a + b x^{2}\right)^{\frac{5}{6}}}$ |
| partial | parametric | `x**4/(a + b*x**2)**(5/6)` | $\frac{x^{4}}{\left(a + b x^{2}\right)^{\frac{5}{6}}}$ |
| partial | parametric | `x**2/(a + b*x**2)**(5/6)` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{\frac{5}{6}}}$ |
| partial | parametric | `(a + b*x**2)**(-5/6)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{5}{6}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)**(5/6))` | $\frac{1}{x^{2} \left(a + b x^{2}\right)^{\frac{5}{6}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)**(5/6))` | $\frac{1}{x^{4} \left(a + b x^{2}\right)^{\frac{5}{6}}}$ |
| partial | parametric | `1/(x**6*(a + b*x**2)**(5/6))` | $\frac{1}{x^{6} \left(a + b x^{2}\right)^{\frac{5}{6}}}$ |
| partial | parametric | `x**6/(a + b*x**2)**(7/6)` | $\frac{x^{6}}{\left(a + b x^{2}\right)^{\frac{7}{6}}}$ |
| partial | parametric | `x**4/(a + b*x**2)**(7/6)` | $\frac{x^{4}}{\left(a + b x^{2}\right)^{\frac{7}{6}}}$ |
| partial | parametric | `x**2/(a + b*x**2)**(7/6)` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{\frac{7}{6}}}$ |
| partial | parametric | `(a + b*x**2)**(-7/6)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{7}{6}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)**(7/6))` | $\frac{1}{x^{2} \left(a + b x^{2}\right)^{\frac{7}{6}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)**(7/6))` | $\frac{1}{x^{4} \left(a + b x^{2}\right)^{\frac{7}{6}}}$ |
| partial | parametric | `1/(x**6*(a + b*x**2)**(7/6))` | $\frac{1}{x^{6} \left(a + b x^{2}\right)^{\frac{7}{6}}}$ |
| partial | parametric | `sqrt(a + b*x**2)*(c + d*x**2)**3` | $\sqrt{a + b x^{2}} \left(c + d x^{2}\right)^{3}$ |
| partial | parametric | `sqrt(a + b*x**2)*(c + d*x**2)**2` | $\sqrt{a + b x^{2}} \left(c + d x^{2}\right)^{2}$ |
| partial | parametric | `sqrt(a + b*x**2)*(c + d*x**2)` | $\sqrt{a + b x^{2}} \left(c + d x^{2}\right)$ |
| partial | parametric | `sqrt(a + b*x**2)` | $\sqrt{a + b x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(c + d*x**2)` | $\frac{\sqrt{a + b x^{2}}}{c + d x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(c + d*x**2)**2` | $\frac{\sqrt{a + b x^{2}}}{\left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(c + d*x**2)**3` | $\frac{\sqrt{a + b x^{2}}}{\left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(c + d*x**2)**4` | $\frac{\sqrt{a + b x^{2}}}{\left(c + d x^{2}\right)^{4}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)*(c + d*x**2)**3` | $\left(a + b x^{2}\right)^{\frac{3}{2}} \left(c + d x^{2}\right)^{3}$ |
| partial | parametric | `(a + b*x**2)**(3/2)*(c + d*x**2)**2` | $\left(a + b x^{2}\right)^{\frac{3}{2}} \left(c + d x^{2}\right)^{2}$ |
| partial | parametric | `(a + b*x**2)**(3/2)*(c + d*x**2)` | $\left(a + b x^{2}\right)^{\frac{3}{2}} \left(c + d x^{2}\right)$ |
| partial | parametric | `(a + b*x**2)**(3/2)` | $\left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(c + d*x**2)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{c + d x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(c + d*x**2)**2` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(c + d*x**2)**3` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(c + d*x**2)**4` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(c + d x^{2}\right)^{4}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(c + d*x**2)**5` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(c + d x^{2}\right)^{5}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)*(c + d*x**2)**3` | $\left(a + b x^{2}\right)^{\frac{5}{2}} \left(c + d x^{2}\right)^{3}$ |
| partial | parametric | `(a + b*x**2)**(5/2)*(c + d*x**2)**2` | $\left(a + b x^{2}\right)^{\frac{5}{2}} \left(c + d x^{2}\right)^{2}$ |
| partial | parametric | `(a + b*x**2)**(5/2)*(c + d*x**2)` | $\left(a + b x^{2}\right)^{\frac{5}{2}} \left(c + d x^{2}\right)$ |
| partial | parametric | `(a + b*x**2)**(5/2)` | $\left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/(c + d*x**2)` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{c + d x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/(c + d*x**2)**2` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{\left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/(c + d*x**2)**3` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{\left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/(c + d*x**2)**4` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{\left(c + d x^{2}\right)^{4}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/(c + d*x**2)**5` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{\left(c + d x^{2}\right)^{5}}$ |
| partial | concrete | `sqrt(1 - x**2)/(x**2 + 1)` | $\frac{\sqrt{1 - x^{2}}}{x^{2} + 1}$ |
| partial | concrete | `sqrt(x**2 + 1)/(x**2 - 1)` | $\frac{\sqrt{x^{2} + 1}}{x^{2} - 1}$ |
| partial | concrete | `sqrt(1 - x**2)/(2*x**2 - 1)` | $\frac{\sqrt{1 - x^{2}}}{2 x^{2} - 1}$ |
| partial | parametric | `(c + d*x**2)**3/sqrt(a + b*x**2)` | $\frac{\left(c + d x^{2}\right)^{3}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c + d*x**2)**2/sqrt(a + b*x**2)` | $\frac{\left(c + d x^{2}\right)^{2}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c + d*x**2)/sqrt(a + b*x**2)` | $\frac{c + d x^{2}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/sqrt(a + b*x**2)` | $\frac{1}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/(sqrt(a + b*x**2)*(c + d*x**2))` | $\frac{1}{\sqrt{a + b x^{2}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `1/(sqrt(a + b*x**2)*(c + d*x**2)**2)` | $\frac{1}{\sqrt{a + b x^{2}} \left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(a + b*x**2)*(c + d*x**2)**3)` | $\frac{1}{\sqrt{a + b x^{2}} \left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `(c + d*x**2)**4/(a + b*x**2)**(3/2)` | $\frac{\left(c + d x^{2}\right)^{4}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x**2)**3/(a + b*x**2)**(3/2)` | $\frac{\left(c + d x^{2}\right)^{3}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x**2)/(a + b*x**2)**(3/2)` | $\frac{c + d x^{2}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(-3/2)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x**2)**(3/2)*(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{3}{2}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `1/((a + b*x**2)**(3/2)*(c + d*x**2)**2)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{3}{2}} \left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**2)**(3/2)*(c + d*x**2)**3)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{3}{2}} \left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `(c + d*x**2)**4/(a + b*x**2)**(5/2)` | $\frac{\left(c + d x^{2}\right)^{4}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d*x**2)**3/(a + b*x**2)**(5/2)` | $\frac{\left(c + d x^{2}\right)^{3}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d*x**2)**2/(a + b*x**2)**(5/2)` | $\frac{\left(c + d x^{2}\right)^{2}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(c + d*x**2)/(a + b*x**2)**(5/2)` | $\frac{c + d x^{2}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**(-5/2)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((a + b*x**2)**(5/2)*(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{5}{2}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `1/((a + b*x**2)**(5/2)*(c + d*x**2)**2)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{5}{2}} \left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**2)**(5/2)*(c + d*x**2)**3)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{5}{2}} \left(c + d x^{2}\right)^{3}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**3/(c + d*x**2)**(11/2)` | $\frac{\left(a + b x^{2}\right)^{3}}{\left(c + d x^{2}\right)^{\frac{11}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2/(c + d*x**2)**(9/2)` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)/(c + d*x**2)**(7/2)` | $\frac{a + b x^{2}}{\left(c + d x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(c + d*x**2)**(-5/2)` | $\frac{1}{\left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{1}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x**2)**2*sqrt(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(c + d*x**2)/(a + b*x**2)**3` | $\frac{\sqrt{c + d x^{2}}}{\left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(a + b*x**2)**4` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `1/(sqrt(c + d*x**2)*(b*c/d + b*x**2))` | $\frac{1}{\sqrt{c + d x^{2}} \left(\frac{b c}{d} + b x^{2}\right)}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*(x**2 + 1))` | $\frac{1}{\sqrt{1 - x^{2}} \left(x^{2} + 1\right)}$ |
| partial | parametric | `1/((a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| partial | concrete | `(x**2 - 1)/(x**2 + 1)**(3/2)` | $\frac{x^{2} - 1}{\left(x^{2} + 1\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a - b*x**2)**(2/3)*(3*a + b*x**2)**3` | $\left(a - b x^{2}\right)^{\frac{2}{3}} \left(3 a + b x^{2}\right)^{3}$ |
| partial | parametric | `(a - b*x**2)**(2/3)*(3*a + b*x**2)**2` | $\left(a - b x^{2}\right)^{\frac{2}{3}} \left(3 a + b x^{2}\right)^{2}$ |
| partial | parametric | `(a - b*x**2)**(2/3)*(3*a + b*x**2)` | $\left(a - b x^{2}\right)^{\frac{2}{3}} \left(3 a + b x^{2}\right)$ |
| partial | parametric | `(a - b*x**2)**(2/3)/(3*a + b*x**2)` | $\frac{\left(a - b x^{2}\right)^{\frac{2}{3}}}{3 a + b x^{2}}$ |
| partial | parametric | `(a - b*x**2)**(2/3)/(3*a + b*x**2)**2` | $\frac{\left(a - b x^{2}\right)^{\frac{2}{3}}}{\left(3 a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(a - b*x**2)**(2/3)/(3*a + b*x**2)**3` | $\frac{\left(a - b x^{2}\right)^{\frac{2}{3}}}{\left(3 a + b x^{2}\right)^{3}}$ |
| partial | parametric | `(a - b*x**2)**(2/3)/(3*a + b*x**2)**4` | $\frac{\left(a - b x^{2}\right)^{\frac{2}{3}}}{\left(3 a + b x^{2}\right)^{4}}$ |
| partial | parametric | `(a - b*x**2)**(5/3)*(3*a + b*x**2)**3` | $\left(a - b x^{2}\right)^{\frac{5}{3}} \left(3 a + b x^{2}\right)^{3}$ |
| partial | parametric | `(a - b*x**2)**(5/3)*(3*a + b*x**2)**2` | $\left(a - b x^{2}\right)^{\frac{5}{3}} \left(3 a + b x^{2}\right)^{2}$ |
| partial | parametric | `(a - b*x**2)**(5/3)*(3*a + b*x**2)` | $\left(a - b x^{2}\right)^{\frac{5}{3}} \left(3 a + b x^{2}\right)$ |
| partial | parametric | `(a - b*x**2)**(5/3)/(3*a + b*x**2)` | $\frac{\left(a - b x^{2}\right)^{\frac{5}{3}}}{3 a + b x^{2}}$ |
| partial | parametric | `(a - b*x**2)**(5/3)/(3*a + b*x**2)**2` | $\frac{\left(a - b x^{2}\right)^{\frac{5}{3}}}{\left(3 a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(a - b*x**2)**(5/3)/(3*a + b*x**2)**3` | $\frac{\left(a - b x^{2}\right)^{\frac{5}{3}}}{\left(3 a + b x^{2}\right)^{3}}$ |
| partial | parametric | `(3*a + b*x**2)**4/(a - b*x**2)**(1/3)` | $\frac{\left(3 a + b x^{2}\right)^{4}}{\sqrt[3]{a - b x^{2}}}$ |
| partial | parametric | `(3*a + b*x**2)**3/(a - b*x**2)**(1/3)` | $\frac{\left(3 a + b x^{2}\right)^{3}}{\sqrt[3]{a - b x^{2}}}$ |
| partial | parametric | `(3*a + b*x**2)**2/(a - b*x**2)**(1/3)` | $\frac{\left(3 a + b x^{2}\right)^{2}}{\sqrt[3]{a - b x^{2}}}$ |
| partial | parametric | `(3*a + b*x**2)/(a - b*x**2)**(1/3)` | $\frac{3 a + b x^{2}}{\sqrt[3]{a - b x^{2}}}$ |
| partial | parametric | `1/((a - b*x**2)**(1/3)*(3*a + b*x**2))` | $\frac{1}{\sqrt[3]{a - b x^{2}} \left(3 a + b x^{2}\right)}$ |
| partial | parametric | `1/((a - b*x**2)**(1/3)*(3*a + b*x**2)**2)` | $\frac{1}{\sqrt[3]{a - b x^{2}} \left(3 a + b x^{2}\right)^{2}}$ |
| partial | parametric | `1/((a - b*x**2)**(1/3)*(3*a + b*x**2)**3)` | $\frac{1}{\sqrt[3]{a - b x^{2}} \left(3 a + b x^{2}\right)^{3}}$ |
| partial | parametric | `(3*a + b*x**2)**3/(a - b*x**2)**(4/3)` | $\frac{\left(3 a + b x^{2}\right)^{3}}{\left(a - b x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(3*a + b*x**2)**2/(a - b*x**2)**(4/3)` | $\frac{\left(3 a + b x^{2}\right)^{2}}{\left(a - b x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(3*a + b*x**2)/(a - b*x**2)**(4/3)` | $\frac{3 a + b x^{2}}{\left(a - b x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/((a - b*x**2)**(4/3)*(3*a + b*x**2))` | $\frac{1}{\left(a - b x^{2}\right)^{\frac{4}{3}} \left(3 a + b x^{2}\right)}$ |
| partial | parametric | `1/((a - b*x**2)**(4/3)*(3*a + b*x**2)**2)` | $\frac{1}{\left(a - b x^{2}\right)^{\frac{4}{3}} \left(3 a + b x^{2}\right)^{2}}$ |
| partial | parametric | `1/((a - b*x**2)**(4/3)*(3*a + b*x**2)**3)` | $\frac{1}{\left(a - b x^{2}\right)^{\frac{4}{3}} \left(3 a + b x^{2}\right)^{3}}$ |
| partial | parametric | `(3*a + b*x**2)**4/(a - b*x**2)**(7/3)` | $\frac{\left(3 a + b x^{2}\right)^{4}}{\left(a - b x^{2}\right)^{\frac{7}{3}}}$ |
| partial | parametric | `(3*a + b*x**2)**3/(a - b*x**2)**(7/3)` | $\frac{\left(3 a + b x^{2}\right)^{3}}{\left(a - b x^{2}\right)^{\frac{7}{3}}}$ |
| **SOLVED-NEW** | parametric | `(3*a + b*x**2)**2/(a - b*x**2)**(7/3)` | $\frac{\left(3 a + b x^{2}\right)^{2}}{\left(a - b x^{2}\right)^{\frac{7}{3}}}$ |
| partial | parametric | `(3*a + b*x**2)/(a - b*x**2)**(7/3)` | $\frac{3 a + b x^{2}}{\left(a - b x^{2}\right)^{\frac{7}{3}}}$ |
| partial | parametric | `1/((a - b*x**2)**(7/3)*(3*a + b*x**2))` | $\frac{1}{\left(a - b x^{2}\right)^{\frac{7}{3}} \left(3 a + b x^{2}\right)}$ |
| partial | parametric | `1/((a - b*x**2)**(7/3)*(3*a + b*x**2)**2)` | $\frac{1}{\left(a - b x^{2}\right)^{\frac{7}{3}} \left(3 a + b x^{2}\right)^{2}}$ |
| partial | parametric | `1/((-3*a - b*x**2)*(-a + b*x**2)**(1/3))` | $\frac{1}{\left(- 3 a - b x^{2}\right) \sqrt[3]{- a + b x^{2}}}$ |
| partial | parametric | `1/((a + b*x**2)**(1/3)*(3*a - b*x**2))` | $\frac{1}{\sqrt[3]{a + b x^{2}} \left(3 a - b x^{2}\right)}$ |
| partial | parametric | `1/((c - d*x**2)*(c + 3*d*x**2)**(1/3))` | $\frac{1}{\left(c - d x^{2}\right) \sqrt[3]{c + 3 d x^{2}}}$ |
| partial | parametric | `1/((a - b*x**2)**(1/3)*(3*a + b*x**2))` | $\frac{1}{\sqrt[3]{a - b x^{2}} \left(3 a + b x^{2}\right)}$ |
| partial | parametric | `1/((c - 3*d*x**2)**(1/3)*(c + d*x**2))` | $\frac{1}{\sqrt[3]{c - 3 d x^{2}} \left(c + d x^{2}\right)}$ |
| partial | concrete | `1/((1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{1}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `1/((3 - x**2)*(x**2 + 1)**(1/3))` | $\frac{1}{\left(3 - x^{2}\right) \sqrt[3]{x^{2} + 1}}$ |
| partial | concrete | `(3 - x)/((1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{3 - x}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `(x + 3)/((1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{x + 3}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | parametric | `1/((a + b*x**2)**(1/3)*(9*a*d/b + d*x**2))` | $\frac{1}{\sqrt[3]{a + b x^{2}} \left(\frac{9 a d}{b} + d x^{2}\right)}$ |
| partial | parametric | `1/((a - b*x**2)**(1/3)*(-9*a*d/b + d*x**2))` | $\frac{1}{\sqrt[3]{a - b x^{2}} \left(- \frac{9 a d}{b} + d x^{2}\right)}$ |
| partial | parametric | `1/((-a + b*x**2)**(1/3)*(-9*a*d/b + d*x**2))` | $\frac{1}{\sqrt[3]{- a + b x^{2}} \left(- \frac{9 a d}{b} + d x^{2}\right)}$ |
| partial | parametric | `1/((-a - b*x**2)**(1/3)*(9*a*d/b + d*x**2))` | $\frac{1}{\sqrt[3]{- a - b x^{2}} \left(\frac{9 a d}{b} + d x^{2}\right)}$ |
| partial | parametric | `1/((b*x**2 + 2)**(1/3)*(d*x**2 + 18*d/b))` | $\frac{1}{\sqrt[3]{b x^{2} + 2} \left(d x^{2} + \frac{18 d}{b}\right)}$ |
| partial | parametric | `1/((b*x**2 - 2)**(1/3)*(d*x**2 - 18*d/b))` | $\frac{1}{\sqrt[3]{b x^{2} - 2} \left(d x^{2} - \frac{18 d}{b}\right)}$ |
| partial | parametric | `1/((3*x**2 + 2)**(1/3)*(d*x**2 + 6*d))` | $\frac{1}{\sqrt[3]{3 x^{2} + 2} \left(d x^{2} + 6 d\right)}$ |
| partial | parametric | `1/((2 - 3*x**2)**(1/3)*(d*x**2 - 6*d))` | $\frac{1}{\sqrt[3]{2 - 3 x^{2}} \left(d x^{2} - 6 d\right)}$ |
| partial | parametric | `1/((3*x**2 - 2)**(1/3)*(d*x**2 - 6*d))` | $\frac{1}{\sqrt[3]{3 x^{2} - 2} \left(d x^{2} - 6 d\right)}$ |
| partial | parametric | `1/((-3*x**2 - 2)**(1/3)*(d*x**2 + 6*d))` | $\frac{1}{\sqrt[3]{- 3 x^{2} - 2} \left(d x^{2} + 6 d\right)}$ |
| partial | concrete | `1/((x**2 + 1)**(1/3)*(x**2 + 9))` | $\frac{1}{\sqrt[3]{x^{2} + 1} \left(x^{2} + 9\right)}$ |
| partial | parametric | `1/((b*x**2 + 1)**(1/3)*(b*x**2 + 9))` | $\frac{1}{\sqrt[3]{b x^{2} + 1} \left(b x^{2} + 9\right)}$ |
| partial | concrete | `1/((1 - x**2)**(1/3)*(9 - x**2))` | $\frac{1}{\sqrt[3]{1 - x^{2}} \left(9 - x^{2}\right)}$ |
| partial | parametric | `(a + b*x**2)**(3/2)*sqrt(c + d*x**2)` | $\left(a + b x^{2}\right)^{\frac{3}{2}} \sqrt{c + d x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**2)*sqrt(c + d*x**2)` | $\sqrt{a + b x^{2}} \sqrt{c + d x^{2}}$ |
| partial | parametric | `sqrt(c + d*x**2)/sqrt(a + b*x**2)` | $\frac{\sqrt{c + d x^{2}}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `sqrt(c + d*x**2)/(a + b*x**2)**(3/2)` | $\frac{\sqrt{c + d x^{2}}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(c + d*x**2)/(a + b*x**2)**(5/2)` | $\frac{\sqrt{c + d x^{2}}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(c + d*x**2)/(a + b*x**2)**(7/2)` | $\frac{\sqrt{c + d x^{2}}}{\left(a + b x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)*(c + d*x**2)**(3/2)` | $\left(a + b x^{2}\right)^{\frac{3}{2}} \left(c + d x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(a + b*x**2)*(c + d*x**2)**(3/2)` | $\sqrt{a + b x^{2}} \left(c + d x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/sqrt(a + b*x**2)` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(a + b*x**2)**(3/2)` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(a + b*x**2)**(5/2)` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(a + b*x**2)**(7/2)` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `sqrt(b*x**2 + 2)*sqrt(d*x**2 + 3)` | $\sqrt{b x^{2} + 2} \sqrt{d x^{2} + 3}$ |
| partial | concrete | `sqrt(3 - 6*x**2)*sqrt(4*x**2 + 2)` | $\sqrt{3 - 6 x^{2}} \sqrt{4 x^{2} + 2}$ |
| SOLVED-both | concrete | `sqrt(4*x**2 + 2)*sqrt(6*x**2 + 3)` | $\sqrt{4 x^{2} + 2} \sqrt{6 x^{2} + 3}$ |
| partial | parametric | `sqrt(b*x**2 + 2)/sqrt(d*x**2 + 3)` | $\frac{\sqrt{b x^{2} + 2}}{\sqrt{d x^{2} + 3}}$ |
| partial | parametric | `sqrt(4 - x**2)/sqrt(c + d*x**2)` | $\frac{\sqrt{4 - x^{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(x**2 + 4)/sqrt(c + d*x**2)` | $\frac{\sqrt{x^{2} + 4}}{\sqrt{c + d x^{2}}}$ |
| partial | concrete | `sqrt(1 - x**2)/sqrt(2 - 3*x**2)` | $\frac{\sqrt{1 - x^{2}}}{\sqrt{2 - 3 x^{2}}}$ |
| partial | concrete | `sqrt(4 - x**2)/sqrt(2 - 3*x**2)` | $\frac{\sqrt{4 - x^{2}}}{\sqrt{2 - 3 x^{2}}}$ |
| partial | concrete | `sqrt(1 - 4*x**2)/sqrt(2 - 3*x**2)` | $\frac{\sqrt{1 - 4 x^{2}}}{\sqrt{2 - 3 x^{2}}}$ |
| partial | concrete | `sqrt(x**2 + 1)/sqrt(1 - x**2)` | $\frac{\sqrt{x^{2} + 1}}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `sqrt(x**2 + 1)/sqrt(2 - 3*x**2)` | $\frac{\sqrt{x^{2} + 1}}{\sqrt{2 - 3 x^{2}}}$ |
| partial | concrete | `sqrt(x**2 + 4)/sqrt(2 - 3*x**2)` | $\frac{\sqrt{x^{2} + 4}}{\sqrt{2 - 3 x^{2}}}$ |
| partial | concrete | `sqrt(4*x**2 + 1)/sqrt(2 - 3*x**2)` | $\frac{\sqrt{4 x^{2} + 1}}{\sqrt{2 - 3 x^{2}}}$ |
| partial | concrete | `sqrt(1 - x**2)/sqrt(x**2 + 1)` | $\frac{\sqrt{1 - x^{2}}}{\sqrt{x^{2} + 1}}$ |
| partial | concrete | `sqrt(1 - x**2)/sqrt(3*x**2 + 2)` | $\frac{\sqrt{1 - x^{2}}}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `sqrt(4 - x**2)/sqrt(3*x**2 + 2)` | $\frac{\sqrt{4 - x^{2}}}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `sqrt(1 - 4*x**2)/sqrt(3*x**2 + 2)` | $\frac{\sqrt{1 - 4 x^{2}}}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `sqrt(x**2 + 1)/sqrt(3*x**2 + 2)` | $\frac{\sqrt{x^{2} + 1}}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `sqrt(x**2 + 4)/sqrt(3*x**2 + 2)` | $\frac{\sqrt{x^{2} + 4}}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `sqrt(4*x**2 + 1)/sqrt(3*x**2 + 2)` | $\frac{\sqrt{4 x^{2} + 1}}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `sqrt(1 - x**2)/sqrt(2*x**2 - 1)` | $\frac{\sqrt{1 - x^{2}}}{\sqrt{2 x^{2} - 1}}$ |
| partial | parametric | `(a + b*x**2)**(7/2)/sqrt(c + d*x**2)` | $\frac{\left(a + b x^{2}\right)^{\frac{7}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/sqrt(c + d*x**2)` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/sqrt(c + d*x**2)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/sqrt(c + d*x**2)` | $\frac{\sqrt{a + b x^{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{\sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/((a + b*x**2)**(3/2)*sqrt(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{3}{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/((a + b*x**2)**(5/2)*sqrt(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{5}{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/((a + b*x**2)**(7/2)*sqrt(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{7}{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(7/2)/(c + d*x**2)**(3/2)` | $\frac{\left(a + b x^{2}\right)^{\frac{7}{2}}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/(c + d*x**2)**(3/2)` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(c + d*x**2)**(3/2)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(c + d*x**2)**(3/2)` | $\frac{\sqrt{a + b x^{2}}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{1}{\sqrt{a + b x^{2}} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x**2)**(3/2)*(c + d*x**2)**(3/2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{3}{2}} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x**2)**(5/2)*(c + d*x**2)**(3/2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{5}{2}} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{\sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(sqrt(a - b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{\sqrt{a - b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(sqrt(a + b*x**2)*sqrt(c - d*x**2))` | $\frac{1}{\sqrt{a + b x^{2}} \sqrt{c - d x^{2}}}$ |
| partial | parametric | `1/(sqrt(a - b*x**2)*sqrt(c - d*x**2))` | $\frac{1}{\sqrt{a - b x^{2}} \sqrt{c - d x^{2}}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(5*x**2 + 2))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{5 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(4*x**2 + 2))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{4 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(3*x**2 + 2))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(2*x**2 + 2))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{2 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(x**2 + 2))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(2 - x**2))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{2 - x^{2}}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(2 - 2*x**2))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{2 - 2 x^{2}}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(2 - 3*x**2))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{2 - 3 x^{2}}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(2 - 4*x**2))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{2 - 4 x^{2}}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(2 - 5*x**2))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{2 - 5 x^{2}}}$ |
| partial | concrete | `1/(sqrt(x**2 + 1)*sqrt(5*x**2 + 2))` | $\frac{1}{\sqrt{x^{2} + 1} \sqrt{5 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(x**2 + 1)*sqrt(4*x**2 + 2))` | $\frac{1}{\sqrt{x^{2} + 1} \sqrt{4 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(x**2 + 1)*sqrt(3*x**2 + 2))` | $\frac{1}{\sqrt{x^{2} + 1} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(x**2 + 1)*sqrt(2*x**2 + 2))` | $\frac{1}{\sqrt{x^{2} + 1} \sqrt{2 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(x**2 + 1)*sqrt(x**2 + 2))` | $\frac{1}{\sqrt{x^{2} + 1} \sqrt{x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(2 - x**2)*sqrt(x**2 + 1))` | $\frac{1}{\sqrt{2 - x^{2}} \sqrt{x^{2} + 1}}$ |
| partial | concrete | `1/(sqrt(2 - 2*x**2)*sqrt(x**2 + 1))` | $\frac{1}{\sqrt{2 - 2 x^{2}} \sqrt{x^{2} + 1}}$ |
| partial | concrete | `1/(sqrt(2 - 3*x**2)*sqrt(x**2 + 1))` | $\frac{1}{\sqrt{2 - 3 x^{2}} \sqrt{x^{2} + 1}}$ |
| partial | concrete | `1/(sqrt(2 - 4*x**2)*sqrt(x**2 + 1))` | $\frac{1}{\sqrt{2 - 4 x^{2}} \sqrt{x^{2} + 1}}$ |
| partial | concrete | `1/(sqrt(2 - 5*x**2)*sqrt(x**2 + 1))` | $\frac{1}{\sqrt{2 - 5 x^{2}} \sqrt{x^{2} + 1}}$ |
| partial | concrete | `1/(sqrt(x**2 - 1)*sqrt(5*x**2 + 2))` | $\frac{1}{\sqrt{x^{2} - 1} \sqrt{5 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(x**2 - 1)*sqrt(4*x**2 + 2))` | $\frac{1}{\sqrt{x^{2} - 1} \sqrt{4 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(x**2 - 1)*sqrt(3*x**2 + 2))` | $\frac{1}{\sqrt{x^{2} - 1} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(x**2 - 1)*sqrt(2*x**2 + 2))` | $\frac{1}{\sqrt{x^{2} - 1} \sqrt{2 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(x**2 - 1)*sqrt(x**2 + 2))` | $\frac{1}{\sqrt{x^{2} - 1} \sqrt{x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(2 - x**2)*sqrt(x**2 - 1))` | $\frac{1}{\sqrt{2 - x^{2}} \sqrt{x^{2} - 1}}$ |
| partial | concrete | `1/(sqrt(2 - 2*x**2)*sqrt(x**2 - 1))` | $\frac{1}{\sqrt{2 - 2 x^{2}} \sqrt{x^{2} - 1}}$ |
| partial | concrete | `1/(sqrt(2 - 3*x**2)*sqrt(x**2 - 1))` | $\frac{1}{\sqrt{2 - 3 x^{2}} \sqrt{x^{2} - 1}}$ |
| partial | concrete | `1/(sqrt(2 - 4*x**2)*sqrt(x**2 - 1))` | $\frac{1}{\sqrt{2 - 4 x^{2}} \sqrt{x^{2} - 1}}$ |
| partial | concrete | `1/(sqrt(2 - 5*x**2)*sqrt(x**2 - 1))` | $\frac{1}{\sqrt{2 - 5 x^{2}} \sqrt{x^{2} - 1}}$ |
| partial | concrete | `1/(sqrt(-x**2 - 1)*sqrt(5*x**2 + 2))` | $\frac{1}{\sqrt{- x^{2} - 1} \sqrt{5 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(-x**2 - 1)*sqrt(4*x**2 + 2))` | $\frac{1}{\sqrt{- x^{2} - 1} \sqrt{4 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(-x**2 - 1)*sqrt(3*x**2 + 2))` | $\frac{1}{\sqrt{- x^{2} - 1} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(-x**2 - 1)*sqrt(2*x**2 + 2))` | $\frac{1}{\sqrt{- x^{2} - 1} \sqrt{2 x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(-x**2 - 1)*sqrt(x**2 + 2))` | $\frac{1}{\sqrt{- x^{2} - 1} \sqrt{x^{2} + 2}}$ |
| partial | concrete | `1/(sqrt(2 - x**2)*sqrt(-x**2 - 1))` | $\frac{1}{\sqrt{2 - x^{2}} \sqrt{- x^{2} - 1}}$ |
| partial | concrete | `1/(sqrt(2 - 3*x**2)*sqrt(-x**2 - 1))` | $\frac{1}{\sqrt{2 - 3 x^{2}} \sqrt{- x^{2} - 1}}$ |
| partial | concrete | `1/(sqrt(2 - 4*x**2)*sqrt(-x**2 - 1))` | $\frac{1}{\sqrt{2 - 4 x^{2}} \sqrt{- x^{2} - 1}}$ |
| partial | concrete | `1/(sqrt(2 - 5*x**2)*sqrt(-x**2 - 1))` | $\frac{1}{\sqrt{2 - 5 x^{2}} \sqrt{- x^{2} - 1}}$ |
| partial | parametric | `sqrt(a + b*x**2)/sqrt(c - d*x**2)` | $\frac{\sqrt{a + b x^{2}}}{\sqrt{c - d x^{2}}}$ |
| partial | parametric | `sqrt(-a - b*x**2)/sqrt(c - d*x**2)` | $\frac{\sqrt{- a - b x^{2}}}{\sqrt{c - d x^{2}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/sqrt(-c + d*x**2)` | $\frac{\sqrt{a + b x^{2}}}{\sqrt{- c + d x^{2}}}$ |
| partial | parametric | `sqrt(-a - b*x**2)/sqrt(-c + d*x**2)` | $\frac{\sqrt{- a - b x^{2}}}{\sqrt{- c + d x^{2}}}$ |
| partial | parametric | `sqrt(a - b*x**2)/sqrt(c - d*x**2)` | $\frac{\sqrt{a - b x^{2}}}{\sqrt{c - d x^{2}}}$ |
| partial | parametric | `sqrt(-a + b*x**2)/sqrt(c - d*x**2)` | $\frac{\sqrt{- a + b x^{2}}}{\sqrt{c - d x^{2}}}$ |
| partial | parametric | `sqrt(a - b*x**2)/sqrt(-c + d*x**2)` | $\frac{\sqrt{a - b x^{2}}}{\sqrt{- c + d x^{2}}}$ |
| partial | parametric | `sqrt(-a + b*x**2)/sqrt(-c + d*x**2)` | $\frac{\sqrt{- a + b x^{2}}}{\sqrt{- c + d x^{2}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/sqrt(c + d*x**2)` | $\frac{\sqrt{a + b x^{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(-a - b*x**2)/sqrt(c + d*x**2)` | $\frac{\sqrt{- a - b x^{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/sqrt(-c - d*x**2)` | $\frac{\sqrt{a + b x^{2}}}{\sqrt{- c - d x^{2}}}$ |
| partial | parametric | `sqrt(-a - b*x**2)/sqrt(-c - d*x**2)` | $\frac{\sqrt{- a - b x^{2}}}{\sqrt{- c - d x^{2}}}$ |
| partial | parametric | `sqrt(a - b*x**2)/sqrt(c + d*x**2)` | $\frac{\sqrt{a - b x^{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(-a + b*x**2)/sqrt(c + d*x**2)` | $\frac{\sqrt{- a + b x^{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(a - b*x**2)/sqrt(-c - d*x**2)` | $\frac{\sqrt{a - b x^{2}}}{\sqrt{- c - d x^{2}}}$ |
| partial | parametric | `sqrt(-a + b*x**2)/sqrt(-c - d*x**2)` | $\frac{\sqrt{- a + b x^{2}}}{\sqrt{- c - d x^{2}}}$ |
| partial | parametric | `sqrt(c + d*x**2)/sqrt(a - b*x**2)` | $\frac{\sqrt{c + d x^{2}}}{\sqrt{a - b x^{2}}}$ |
| partial | parametric | `sqrt(-c - d*x**2)/sqrt(a - b*x**2)` | $\frac{\sqrt{- c - d x^{2}}}{\sqrt{a - b x^{2}}}$ |
| partial | parametric | `sqrt(c + d*x**2)/sqrt(-a + b*x**2)` | $\frac{\sqrt{c + d x^{2}}}{\sqrt{- a + b x^{2}}}$ |
| partial | parametric | `sqrt(-c - d*x**2)/sqrt(-a + b*x**2)` | $\frac{\sqrt{- c - d x^{2}}}{\sqrt{- a + b x^{2}}}$ |
| partial | parametric | `sqrt(c - d*x**2)/sqrt(a - b*x**2)` | $\frac{\sqrt{c - d x^{2}}}{\sqrt{a - b x^{2}}}$ |
| partial | parametric | `sqrt(-c + d*x**2)/sqrt(a - b*x**2)` | $\frac{\sqrt{- c + d x^{2}}}{\sqrt{a - b x^{2}}}$ |
| partial | parametric | `sqrt(c - d*x**2)/sqrt(-a + b*x**2)` | $\frac{\sqrt{c - d x^{2}}}{\sqrt{- a + b x^{2}}}$ |
| partial | parametric | `sqrt(-c + d*x**2)/sqrt(-a + b*x**2)` | $\frac{\sqrt{- c + d x^{2}}}{\sqrt{- a + b x^{2}}}$ |
| partial | parametric | `sqrt(c + d*x**2)/sqrt(a + b*x**2)` | $\frac{\sqrt{c + d x^{2}}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `sqrt(-c - d*x**2)/sqrt(a + b*x**2)` | $\frac{\sqrt{- c - d x^{2}}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `sqrt(c + d*x**2)/sqrt(-a - b*x**2)` | $\frac{\sqrt{c + d x^{2}}}{\sqrt{- a - b x^{2}}}$ |
| partial | parametric | `sqrt(-c - d*x**2)/sqrt(-a - b*x**2)` | $\frac{\sqrt{- c - d x^{2}}}{\sqrt{- a - b x^{2}}}$ |
| partial | parametric | `sqrt(c - d*x**2)/sqrt(a + b*x**2)` | $\frac{\sqrt{c - d x^{2}}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `sqrt(-c + d*x**2)/sqrt(a + b*x**2)` | $\frac{\sqrt{- c + d x^{2}}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `sqrt(c - d*x**2)/sqrt(-a - b*x**2)` | $\frac{\sqrt{c - d x^{2}}}{\sqrt{- a - b x^{2}}}$ |
| partial | parametric | `sqrt(-c + d*x**2)/sqrt(-a - b*x**2)` | $\frac{\sqrt{- c + d x^{2}}}{\sqrt{- a - b x^{2}}}$ |
| partial | parametric | `1/(sqrt(b*x**2 + 2)*sqrt(d*x**2 + 3))` | $\frac{1}{\sqrt{b x^{2} + 2} \sqrt{d x^{2} + 3}}$ |
| partial | parametric | `1/(sqrt(4 - x**2)*sqrt(c + d*x**2))` | $\frac{1}{\sqrt{4 - x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(sqrt(c + d*x**2)*sqrt(x**2 + 4))` | $\frac{1}{\sqrt{c + d x^{2}} \sqrt{x^{2} + 4}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(2*x**2 - 1))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{2 x^{2} - 1}}$ |
| partial | parametric | `sqrt(-c**2*x**2 + 1)/sqrt(c**2*x**2 + 1)` | $\frac{\sqrt{- c^{2} x^{2} + 1}}{\sqrt{c^{2} x^{2} + 1}}$ |
| partial | parametric | `sqrt(b*x**2 + 2)/sqrt(d*x**2 + 3)` | $\frac{\sqrt{b x^{2} + 2}}{\sqrt{d x^{2} + 3}}$ |
| partial | concrete | `sqrt(3*x**2 - 1)/sqrt(2 - 3*x**2)` | $\frac{\sqrt{3 x^{2} - 1}}{\sqrt{2 - 3 x^{2}}}$ |
| timeout | parametric | `sqrt(2*c*x**2/(b - sqrt(-4*a*c + b**2)) + 1)/sqrt(-2*c*x**2/(b + sqrt(-4*a*c + b**2)) + 1)` | $\frac{\sqrt{\frac{2 c x^{2}}{b - \sqrt{- 4 a c + b^{2}}} + 1}}{\sqrt{- \frac{2 c x^{2}}{b + \sqrt{- 4 a c + b^{2}}} + 1}}$ |
| timeout | parametric | `sqrt(-2*c*x**2/(b - sqrt(-4*a*c + b**2)) + 1)/sqrt(-2*c*x**2/(b + sqrt(-4*a*c + b**2)) + 1)` | $\frac{\sqrt{- \frac{2 c x^{2}}{b - \sqrt{- 4 a c + b^{2}}} + 1}}{\sqrt{- \frac{2 c x^{2}}{b + \sqrt{- 4 a c + b^{2}}} + 1}}$ |
| timeout | parametric | `sqrt(2*c*x**2/(b - sqrt(-4*a*c + b**2)) + 1)/sqrt(2*c*x**2/(b + sqrt(-4*a*c + b**2)) + 1)` | $\frac{\sqrt{\frac{2 c x^{2}}{b - \sqrt{- 4 a c + b^{2}}} + 1}}{\sqrt{\frac{2 c x^{2}}{b + \sqrt{- 4 a c + b^{2}}} + 1}}$ |
| timeout | parametric | `sqrt(-2*c*x**2/(b - sqrt(-4*a*c + b**2)) + 1)/sqrt(2*c*x**2/(b + sqrt(-4*a*c + b**2)) + 1)` | $\frac{\sqrt{- \frac{2 c x^{2}}{b - \sqrt{- 4 a c + b^{2}}} + 1}}{\sqrt{\frac{2 c x^{2}}{b + \sqrt{- 4 a c + b^{2}}} + 1}}$ |
| NIE | concrete | `1/(sqrt(x**2 - 1)*sqrt(x**2 - 4*sqrt(3) + 7))` | $\frac{1}{\sqrt{x^{2} - 1} \sqrt{x^{2} - 4 \sqrt{3} + 7}}$ |
| NIE | concrete | `1/(sqrt(x**2*(-3 + sqrt(3)) + 3)*sqrt(2*sqrt(3)*x**2 - 3*sqrt(3) + 3))` | $\frac{1}{\sqrt{x^{2} \left(-3 + \sqrt{3}\right) + 3} \sqrt{2 \sqrt{3} x^{2} - 3 \sqrt{3} + 3}}$ |
| partial | concrete | `1/((3*x**2 + 2)**(1/4)*(3*x**2 + 4))` | $\frac{1}{\sqrt[4]{3 x^{2} + 2} \left(3 x^{2} + 4\right)}$ |
| partial | concrete | `1/((2 - 3*x**2)**(1/4)*(4 - 3*x**2))` | $\frac{1}{\sqrt[4]{2 - 3 x^{2}} \left(4 - 3 x^{2}\right)}$ |
| partial | parametric | `1/((b*x**2 + 2)**(1/4)*(b*x**2 + 4))` | $\frac{1}{\sqrt[4]{b x^{2} + 2} \left(b x^{2} + 4\right)}$ |
| partial | parametric | `1/((-b*x**2 + 2)**(1/4)*(-b*x**2 + 4))` | $\frac{1}{\sqrt[4]{- b x^{2} + 2} \left(- b x^{2} + 4\right)}$ |
| partial | parametric | `1/((a + 3*x**2)**(1/4)*(2*a + 3*x**2))` | $\frac{1}{\sqrt[4]{a + 3 x^{2}} \left(2 a + 3 x^{2}\right)}$ |
| partial | parametric | `1/((a - 3*x**2)**(1/4)*(2*a - 3*x**2))` | $\frac{1}{\sqrt[4]{a - 3 x^{2}} \left(2 a - 3 x^{2}\right)}$ |
| partial | parametric | `1/((a + b*x**2)**(1/4)*(2*a + b*x**2))` | $\frac{1}{\sqrt[4]{a + b x^{2}} \left(2 a + b x^{2}\right)}$ |
| partial | parametric | `1/((a - b*x**2)**(1/4)*(2*a - b*x**2))` | $\frac{1}{\sqrt[4]{a - b x^{2}} \left(2 a - b x^{2}\right)}$ |
| partial | concrete | `1/((3*x**2 - 2)*(3*x**2 - 1)**(1/4))` | $\frac{1}{\left(3 x^{2} - 2\right) \sqrt[4]{3 x^{2} - 1}}$ |
| partial | concrete | `1/((-3*x**2 - 2)*(-3*x**2 - 1)**(1/4))` | $\frac{1}{\left(- 3 x^{2} - 2\right) \sqrt[4]{- 3 x^{2} - 1}}$ |
| partial | parametric | `1/((b*x**2 - 2)*(b*x**2 - 1)**(1/4))` | $\frac{1}{\left(b x^{2} - 2\right) \sqrt[4]{b x^{2} - 1}}$ |
| partial | parametric | `1/((-b*x**2 - 2)*(-b*x**2 - 1)**(1/4))` | $\frac{1}{\left(- b x^{2} - 2\right) \sqrt[4]{- b x^{2} - 1}}$ |
| partial | parametric | `1/((-2*a + 3*x**2)*(-a + 3*x**2)**(1/4))` | $\frac{1}{\left(- 2 a + 3 x^{2}\right) \sqrt[4]{- a + 3 x^{2}}}$ |
| partial | parametric | `1/((-2*a - 3*x**2)*(-a - 3*x**2)**(1/4))` | $\frac{1}{\left(- 2 a - 3 x^{2}\right) \sqrt[4]{- a - 3 x^{2}}}$ |
| partial | parametric | `1/((-2*a + b*x**2)*(-a + b*x**2)**(1/4))` | $\frac{1}{\left(- 2 a + b x^{2}\right) \sqrt[4]{- a + b x^{2}}}$ |
| partial | parametric | `1/((-2*a - b*x**2)*(-a - b*x**2)**(1/4))` | $\frac{1}{\left(- 2 a - b x^{2}\right) \sqrt[4]{- a - b x^{2}}}$ |
| partial | concrete | `1/((2 - x**2)*(x**2 - 1)**(1/4))` | $\frac{1}{\left(2 - x^{2}\right) \sqrt[4]{x^{2} - 1}}$ |
| partial | parametric | `(a + b*x**2)**(7/4)/(c + d*x**2)` | $\frac{\left(a + b x^{2}\right)^{\frac{7}{4}}}{c + d x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(5/4)/(c + d*x**2)` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{4}}}{c + d x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(3/4)/(c + d*x**2)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{4}}}{c + d x^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/4)/(c + d*x**2)` | $\frac{\sqrt[4]{a + b x^{2}}}{c + d x^{2}}$ |
| partial | parametric | `1/((a + b*x**2)**(1/4)*(c + d*x**2))` | $\frac{1}{\sqrt[4]{a + b x^{2}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `1/((a + b*x**2)**(3/4)*(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{3}{4}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `1/((a + b*x**2)**(5/4)*(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{5}{4}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `1/((a + b*x**2)**(7/4)*(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{7}{4}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `1/((a + b*x**2)**(9/4)*(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{9}{4}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `1/((a + b*x**2)**(11/4)*(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{11}{4}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `(a + b*x**2)**(7/4)/(c + d*x**2)**2` | $\frac{\left(a + b x^{2}\right)^{\frac{7}{4}}}{\left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x**2)**(5/4)/(c + d*x**2)**2` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{4}}}{\left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x**2)**(3/4)/(c + d*x**2)**2` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{4}}}{\left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x**2)**(1/4)/(c + d*x**2)**2` | $\frac{\sqrt[4]{a + b x^{2}}}{\left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**2)**(1/4)*(c + d*x**2)**2)` | $\frac{1}{\sqrt[4]{a + b x^{2}} \left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**2)**(3/4)*(c + d*x**2)**2)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{3}{4}} \left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**2)**(5/4)*(c + d*x**2)**2)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{5}{4}} \left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**2)**(7/4)*(c + d*x**2)**2)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{7}{4}} \left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**2)**(9/4)*(c + d*x**2)**2)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{9}{4}} \left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**2)**(11/4)*(c + d*x**2)**2)` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{11}{4}} \left(c + d x^{2}\right)^{2}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x**2)*(a + b*x**2)` | $x^{\frac{7}{2}} \left(A + B x^{2}\right) \left(a + b x^{2}\right)$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x**2)*(a + b*x**2)` | $x^{\frac{5}{2}} \left(A + B x^{2}\right) \left(a + b x^{2}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x**2)*(a + b*x**2)` | $x^{\frac{3}{2}} \left(A + B x^{2}\right) \left(a + b x^{2}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x**2)*(a + b*x**2)` | $\sqrt{x} \left(A + B x^{2}\right) \left(a + b x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)/sqrt(x)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)/x**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)/x**(5/2)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)/x**(7/2)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x**2)*(a + b*x**2)**2` | $x^{\frac{7}{2}} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x**2)*(a + b*x**2)**2` | $x^{\frac{5}{2}} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x**2)*(a + b*x**2)**2` | $x^{\frac{3}{2}} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x**2)*(a + b*x**2)**2` | $\sqrt{x} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)**2/sqrt(x)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)**2/x**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)**2/x**(5/2)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)**2/x**(7/2)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x**2)*(a + b*x**2)**3` | $x^{\frac{7}{2}} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x**2)*(a + b*x**2)**3` | $x^{\frac{5}{2}} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x**2)*(a + b*x**2)**3` | $x^{\frac{3}{2}} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x**2)*(a + b*x**2)**3` | $\sqrt{x} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)**3/sqrt(x)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)**3/x**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)**3/x**(5/2)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)**3/x**(7/2)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{3}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x**2)/(a + b*x**2)` | $\frac{x^{\frac{7}{2}} \left(A + B x^{2}\right)}{a + b x^{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**2)/(a + b*x**2)` | $\frac{x^{\frac{5}{2}} \left(A + B x^{2}\right)}{a + b x^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**2)/(a + b*x**2)` | $\frac{x^{\frac{3}{2}} \left(A + B x^{2}\right)}{a + b x^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**2)/(a + b*x**2)` | $\frac{\sqrt{x} \left(A + B x^{2}\right)}{a + b x^{2}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(x)*(a + b*x**2))` | $\frac{A + B x^{2}}{\sqrt{x} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(A + B*x**2)/(x**(3/2)*(a + b*x**2))` | $\frac{A + B x^{2}}{x^{\frac{3}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(A + B*x**2)/(x**(5/2)*(a + b*x**2))` | $\frac{A + B x^{2}}{x^{\frac{5}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(A + B*x**2)/(x**(7/2)*(a + b*x**2))` | $\frac{A + B x^{2}}{x^{\frac{7}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `x**(7/2)*(A + B*x**2)/(a + b*x**2)**2` | $\frac{x^{\frac{7}{2}} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**2)/(a + b*x**2)**2` | $\frac{x^{\frac{5}{2}} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**2)/(a + b*x**2)**2` | $\frac{x^{\frac{3}{2}} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**2)/(a + b*x**2)**2` | $\frac{\sqrt{x} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(x)*(a + b*x**2)**2)` | $\frac{A + B x^{2}}{\sqrt{x} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x**2)/(x**(3/2)*(a + b*x**2)**2)` | $\frac{A + B x^{2}}{x^{\frac{3}{2}} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x**2)/(x**(5/2)*(a + b*x**2)**2)` | $\frac{A + B x^{2}}{x^{\frac{5}{2}} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x**2)/(x**(7/2)*(a + b*x**2)**2)` | $\frac{A + B x^{2}}{x^{\frac{7}{2}} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**(7/2)*(A + B*x**2)/(a + b*x**2)**3` | $\frac{x^{\frac{7}{2}} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**2)/(a + b*x**2)**3` | $\frac{x^{\frac{5}{2}} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**2)/(a + b*x**2)**3` | $\frac{x^{\frac{3}{2}} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**2)/(a + b*x**2)**3` | $\frac{\sqrt{x} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(x)*(a + b*x**2)**3)` | $\frac{A + B x^{2}}{\sqrt{x} \left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x**2)/(x**(3/2)*(a + b*x**2)**3)` | $\frac{A + B x^{2}}{x^{\frac{3}{2}} \left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x**2)/(x**(5/2)*(a + b*x**2)**3)` | $\frac{A + B x^{2}}{x^{\frac{5}{2}} \left(a + b x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x**2)/(x**(7/2)*(a + b*x**2)**3)` | $\frac{A + B x^{2}}{x^{\frac{7}{2}} \left(a + b x^{2}\right)^{3}}$ |
| SOLVED-both | parametric | `x**(7/2)*(a + b*x**2)**2*(c + d*x**2)` | $x^{\frac{7}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b*x**2)**2*(c + d*x**2)` | $x^{\frac{5}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b*x**2)**2*(c + d*x**2)` | $x^{\frac{3}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b*x**2)**2*(c + d*x**2)` | $\sqrt{x} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*(c + d*x**2)/sqrt(x)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*(c + d*x**2)/x**(3/2)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*(c + d*x**2)/x**(5/2)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*(c + d*x**2)/x**(7/2)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(a + b*x**2)**2*(c + d*x**2)**2` | $x^{\frac{7}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b*x**2)**2*(c + d*x**2)**2` | $x^{\frac{5}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b*x**2)**2*(c + d*x**2)**2` | $x^{\frac{3}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b*x**2)**2*(c + d*x**2)**2` | $\sqrt{x} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*(c + d*x**2)**2/sqrt(x)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*(c + d*x**2)**2/x**(3/2)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*(c + d*x**2)**2/x**(5/2)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*(c + d*x**2)**2/x**(7/2)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(a + b*x**2)**2*(c + d*x**2)**3` | $x^{\frac{7}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b*x**2)**2*(c + d*x**2)**3` | $x^{\frac{5}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b*x**2)**2*(c + d*x**2)**3` | $x^{\frac{3}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b*x**2)**2*(c + d*x**2)**3` | $\sqrt{x} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*(c + d*x**2)**3/sqrt(x)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*(c + d*x**2)**3/x**(3/2)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*(c + d*x**2)**3/x**(5/2)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*(c + d*x**2)**3/x**(7/2)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `x**(7/2)*(a + b*x**2)**2/(c + d*x**2)` | $\frac{x^{\frac{7}{2}} \left(a + b x^{2}\right)^{2}}{c + d x^{2}}$ |
| partial | parametric | `x**(5/2)*(a + b*x**2)**2/(c + d*x**2)` | $\frac{x^{\frac{5}{2}} \left(a + b x^{2}\right)^{2}}{c + d x^{2}}$ |
| partial | parametric | `x**(3/2)*(a + b*x**2)**2/(c + d*x**2)` | $\frac{x^{\frac{3}{2}} \left(a + b x^{2}\right)^{2}}{c + d x^{2}}$ |
| partial | parametric | `sqrt(x)*(a + b*x**2)**2/(c + d*x**2)` | $\frac{\sqrt{x} \left(a + b x^{2}\right)^{2}}{c + d x^{2}}$ |
| partial | parametric | `(a + b*x**2)**2/(sqrt(x)*(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\sqrt{x} \left(c + d x^{2}\right)}$ |
| partial | parametric | `(a + b*x**2)**2/(x**(3/2)*(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{3}{2}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `(a + b*x**2)**2/(x**(5/2)*(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{5}{2}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `(a + b*x**2)**2/(x**(7/2)*(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{7}{2}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `(a + b*x**2)**2/(x**(9/2)*(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{9}{2}} \left(c + d x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**2/(x**(11/2)*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{2}}{x^{\frac{11}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `x**(7/2)*(a + b*x**2)**2/(c + d*x**2)**2` | $\frac{x^{\frac{7}{2}} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `x**(5/2)*(a + b*x**2)**2/(c + d*x**2)**2` | $\frac{x^{\frac{5}{2}} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `x**(3/2)*(a + b*x**2)**2/(c + d*x**2)**2` | $\frac{x^{\frac{3}{2}} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(x)*(a + b*x**2)**2/(c + d*x**2)**2` | $\frac{\sqrt{x} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x**2)**2/(sqrt(x)*(c + d*x**2)**2)` | $\frac{\left(a + b x^{2}\right)^{2}}{\sqrt{x} \left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**(3/2)*(c + d*x**2)**2)` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{3}{2}} \left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**(5/2)*(c + d*x**2)**2)` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{5}{2}} \left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**(7/2)*(c + d*x**2)**2)` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{7}{2}} \left(c + d x^{2}\right)^{2}}$ |
| partial | parametric | `x**(7/2)*(a + b*x**2)**2/(c + d*x**2)**3` | $\frac{x^{\frac{7}{2}} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `x**(5/2)*(a + b*x**2)**2/(c + d*x**2)**3` | $\frac{x^{\frac{5}{2}} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `x**(3/2)*(a + b*x**2)**2/(c + d*x**2)**3` | $\frac{x^{\frac{3}{2}} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(x)*(a + b*x**2)**2/(c + d*x**2)**3` | $\frac{\sqrt{x} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x**2)**2/(sqrt(x)*(c + d*x**2)**3)` | $\frac{\left(a + b x^{2}\right)^{2}}{\sqrt{x} \left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**(3/2)*(c + d*x**2)**3)` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{3}{2}} \left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**(5/2)*(c + d*x**2)**3)` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{5}{2}} \left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**(7/2)*(c + d*x**2)**3)` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{\frac{7}{2}} \left(c + d x^{2}\right)^{3}}$ |
| partial | parametric | `x**(5/2)*(c + d*x**2)**3/(a + b*x**2)` | $\frac{x^{\frac{5}{2}} \left(c + d x^{2}\right)^{3}}{a + b x^{2}}$ |
| partial | parametric | `x**(3/2)*(c + d*x**2)**3/(a + b*x**2)` | $\frac{x^{\frac{3}{2}} \left(c + d x^{2}\right)^{3}}{a + b x^{2}}$ |
| partial | parametric | `sqrt(x)*(c + d*x**2)**3/(a + b*x**2)` | $\frac{\sqrt{x} \left(c + d x^{2}\right)^{3}}{a + b x^{2}}$ |
| partial | parametric | `(c + d*x**2)**3/(sqrt(x)*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{3}}{\sqrt{x} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**3/(x**(3/2)*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{3}}{x^{\frac{3}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**3/(x**(5/2)*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{3}}{x^{\frac{5}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**3/(x**(7/2)*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{3}}{x^{\frac{7}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**3/(x**(9/2)*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{3}}{x^{\frac{9}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**3/(x**(11/2)*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{3}}{x^{\frac{11}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**3/(x**(13/2)*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{3}}{x^{\frac{13}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**3/(x**(15/2)*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{3}}{x^{\frac{15}{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `x**(7/2)*(c + d*x**2)**3/(a + b*x**2)**2` | $\frac{x^{\frac{7}{2}} \left(c + d x^{2}\right)^{3}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**(5/2)*(c + d*x**2)**3/(a + b*x**2)**2` | $\frac{x^{\frac{5}{2}} \left(c + d x^{2}\right)^{3}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**(3/2)*(c + d*x**2)**3/(a + b*x**2)**2` | $\frac{x^{\frac{3}{2}} \left(c + d x^{2}\right)^{3}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(x)*(c + d*x**2)**3/(a + b*x**2)**2` | $\frac{\sqrt{x} \left(c + d x^{2}\right)^{3}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**3/(sqrt(x)*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{3}}{\sqrt{x} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**3/(x**(3/2)*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{3}}{x^{\frac{3}{2}} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**3/(x**(5/2)*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{3}}{x^{\frac{5}{2}} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**3/(x**(7/2)*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{3}}{x^{\frac{7}{2}} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**3/(x**(9/2)*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{3}}{x^{\frac{9}{2}} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**(9/2)/((a + b*x**2)*(c + d*x**2))` | $\frac{x^{\frac{9}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)}$ |
| partial | parametric | `x**(7/2)/((a + b*x**2)*(c + d*x**2))` | $\frac{x^{\frac{7}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)}$ |
| partial | parametric | `x**(5/2)/((a + b*x**2)*(c + d*x**2))` | $\frac{x^{\frac{5}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)}$ |
| partial | parametric | `x**(3/2)/((a + b*x**2)*(c + d*x**2))` | $\frac{x^{\frac{3}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)}$ |
| partial | parametric | `sqrt(x)/((a + b*x**2)*(c + d*x**2))` | $\frac{\sqrt{x}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)}$ |
| partial | parametric | `1/(sqrt(x)*(a + b*x**2)*(c + d*x**2))` | $\frac{1}{\sqrt{x} \left(a + b x^{2}\right) \left(c + d x^{2}\right)}$ |
| partial | parametric | `1/(x**(3/2)*(a + b*x**2)*(c + d*x**2))` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x^{2}\right) \left(c + d x^{2}\right)}$ |
| partial | parametric | `1/(x**(5/2)*(a + b*x**2)*(c + d*x**2))` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x^{2}\right) \left(c + d x^{2}\right)}$ |
| partial | parametric | `1/(x**(7/2)*(a + b*x**2)*(c + d*x**2))` | $\frac{1}{x^{\frac{7}{2}} \left(a + b x^{2}\right) \left(c + d x^{2}\right)}$ |
| timeout | parametric | `x**(11/2)/((a + b*x**2)*(c + d*x**2)**2)` | $\frac{x^{\frac{11}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `x**(9/2)/((a + b*x**2)*(c + d*x**2)**2)` | $\frac{x^{\frac{9}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `x**(7/2)/((a + b*x**2)*(c + d*x**2)**2)` | $\frac{x^{\frac{7}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `x**(5/2)/((a + b*x**2)*(c + d*x**2)**2)` | $\frac{x^{\frac{5}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `x**(3/2)/((a + b*x**2)*(c + d*x**2)**2)` | $\frac{x^{\frac{3}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `sqrt(x)/((a + b*x**2)*(c + d*x**2)**2)` | $\frac{\sqrt{x}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `1/(sqrt(x)*(a + b*x**2)*(c + d*x**2)**2)` | $\frac{1}{\sqrt{x} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `1/(x**(3/2)*(a + b*x**2)*(c + d*x**2)**2)` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `1/(x**(5/2)*(a + b*x**2)*(c + d*x**2)**2)` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `1/(x**(7/2)*(a + b*x**2)*(c + d*x**2)**2)` | $\frac{1}{x^{\frac{7}{2}} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `x**(7/2)/((a + b*x**2)*(c + d*x**2)**3)` | $\frac{x^{\frac{7}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `x**(5/2)/((a + b*x**2)*(c + d*x**2)**3)` | $\frac{x^{\frac{5}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `x**(3/2)/((a + b*x**2)*(c + d*x**2)**3)` | $\frac{x^{\frac{3}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `sqrt(x)/((a + b*x**2)*(c + d*x**2)**3)` | $\frac{\sqrt{x}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `1/(sqrt(x)*(a + b*x**2)*(c + d*x**2)**3)` | $\frac{1}{\sqrt{x} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `1/(x**(3/2)*(a + b*x**2)*(c + d*x**2)**3)` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `1/(x**(5/2)*(a + b*x**2)*(c + d*x**2)**3)` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `1/(x**(7/2)*(a + b*x**2)*(c + d*x**2)**3)` | $\frac{1}{x^{\frac{7}{2}} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `x**(7/2)/((a + b*x**2)**2*(c + d*x**2)**2)` | $\frac{x^{\frac{7}{2}}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `x**(5/2)/((a + b*x**2)**2*(c + d*x**2)**2)` | $\frac{x^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `x**(3/2)/((a + b*x**2)**2*(c + d*x**2)**2)` | $\frac{x^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `sqrt(x)/((a + b*x**2)**2*(c + d*x**2)**2)` | $\frac{\sqrt{x}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `1/(sqrt(x)*(a + b*x**2)**2*(c + d*x**2)**2)` | $\frac{1}{\sqrt{x} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `1/(x**(3/2)*(a + b*x**2)**2*(c + d*x**2)**2)` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `1/(x**(5/2)*(a + b*x**2)**2*(c + d*x**2)**2)` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `1/(x**(7/2)*(a + b*x**2)**2*(c + d*x**2)**2)` | $\frac{1}{x^{\frac{7}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{2}}$ |
| timeout | parametric | `x**(7/2)/((a + b*x**2)**2*(c + d*x**2)**3)` | $\frac{x^{\frac{7}{2}}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `x**(5/2)/((a + b*x**2)**2*(c + d*x**2)**3)` | $\frac{x^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `x**(3/2)/((a + b*x**2)**2*(c + d*x**2)**3)` | $\frac{x^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `sqrt(x)/((a + b*x**2)**2*(c + d*x**2)**3)` | $\frac{\sqrt{x}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `1/(sqrt(x)*(a + b*x**2)**2*(c + d*x**2)**3)` | $\frac{1}{\sqrt{x} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `1/(x**(3/2)*(a + b*x**2)**2*(c + d*x**2)**3)` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `1/(x**(5/2)*(a + b*x**2)**2*(c + d*x**2)**3)` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}}$ |
| timeout | parametric | `1/(x**(7/2)*(a + b*x**2)**2*(c + d*x**2)**3)` | $\frac{1}{x^{\frac{7}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{3}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x**2)*sqrt(a + b*x**2)` | $x^{5} \left(A + B x^{2}\right) \sqrt{a + b x^{2}}$ |
| partial | parametric | `x**4*(A + B*x**2)*sqrt(a + b*x**2)` | $x^{4} \left(A + B x^{2}\right) \sqrt{a + b x^{2}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x**2)*sqrt(a + b*x**2)` | $x^{3} \left(A + B x^{2}\right) \sqrt{a + b x^{2}}$ |
| partial | parametric | `x**2*(A + B*x**2)*sqrt(a + b*x**2)` | $x^{2} \left(A + B x^{2}\right) \sqrt{a + b x^{2}}$ |
| SOLVED-both | parametric | `x*(A + B*x**2)*sqrt(a + b*x**2)` | $x \left(A + B x^{2}\right) \sqrt{a + b x^{2}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)` | $\left(A + B x^{2}\right) \sqrt{a + b x^{2}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**2` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**3` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**4` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**5` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{5}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**6` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**7` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{7}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**8` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{8}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**9` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{9}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**10` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{10}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**11` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{11}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x**2)*(a + b*x**2)**(3/2)` | $x^{5} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**4*(A + B*x**2)*(a + b*x**2)**(3/2)` | $x^{4} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x**2)*(a + b*x**2)**(3/2)` | $x^{3} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(A + B*x**2)*(a + b*x**2)**(3/2)` | $x^{2} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x*(A + B*x**2)*(a + b*x**2)**(3/2)` | $x \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)` | $\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/x` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/x**2` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/x**3` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/x**4` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/x**5` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/x**6` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/x**7` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{7}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/x**8` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{8}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/x**9` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{9}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/x**10` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{10}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/x**11` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{11}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x**2)*(a + b*x**2)**(5/2)` | $x^{5} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**4*(A + B*x**2)*(a + b*x**2)**(5/2)` | $x^{4} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x**2)*(a + b*x**2)**(5/2)` | $x^{3} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**2*(A + B*x**2)*(a + b*x**2)**(5/2)` | $x^{2} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x*(A + B*x**2)*(a + b*x**2)**(5/2)` | $x \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(5/2)` | $\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(5/2)/x` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(5/2)/x**2` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(5/2)/x**3` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(5/2)/x**4` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(5/2)/x**5` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(5/2)/x**6` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(5/2)/x**7` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{7}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(5/2)/x**8` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{8}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(5/2)/x**9` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{9}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(a + b*x**2)**(5/2)/x**10` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{10}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(5/2)/x**11` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{11}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x**2)/sqrt(a + b*x**2)` | $\frac{x^{5} \left(A + B x^{2}\right)}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**4*(A + B*x**2)/sqrt(a + b*x**2)` | $\frac{x^{4} \left(A + B x^{2}\right)}{\sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x**2)/sqrt(a + b*x**2)` | $\frac{x^{3} \left(A + B x^{2}\right)}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**2*(A + B*x**2)/sqrt(a + b*x**2)` | $\frac{x^{2} \left(A + B x^{2}\right)}{\sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x**2)/sqrt(a + b*x**2)` | $\frac{x \left(A + B x^{2}\right)}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x**2)/sqrt(a + b*x**2)` | $\frac{A + B x^{2}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x*sqrt(a + b*x**2))` | $\frac{A + B x^{2}}{x \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x**2*sqrt(a + b*x**2))` | $\frac{A + B x^{2}}{x^{2} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x**3*sqrt(a + b*x**2))` | $\frac{A + B x^{2}}{x^{3} \sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)/(x**4*sqrt(a + b*x**2))` | $\frac{A + B x^{2}}{x^{4} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x**5*sqrt(a + b*x**2))` | $\frac{A + B x^{2}}{x^{5} \sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)/(x**6*sqrt(a + b*x**2))` | $\frac{A + B x^{2}}{x^{6} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x**7*sqrt(a + b*x**2))` | $\frac{A + B x^{2}}{x^{7} \sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)/(x**8*sqrt(a + b*x**2))` | $\frac{A + B x^{2}}{x^{8} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**6*(A + B*x**2)/(a + b*x**2)**(3/2)` | $\frac{x^{6} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x**2)/(a + b*x**2)**(3/2)` | $\frac{x^{5} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4*(A + B*x**2)/(a + b*x**2)**(3/2)` | $\frac{x^{4} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x**2)/(a + b*x**2)**(3/2)` | $\frac{x^{3} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(A + B*x**2)/(a + b*x**2)**(3/2)` | $\frac{x^{2} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x**2)/(a + b*x**2)**(3/2)` | $\frac{x \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(a + b*x**2)**(3/2)` | $\frac{A + B x^{2}}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x*(a + b*x**2)**(3/2))` | $\frac{A + B x^{2}}{x \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)/(x**2*(a + b*x**2)**(3/2))` | $\frac{A + B x^{2}}{x^{2} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x**3*(a + b*x**2)**(3/2))` | $\frac{A + B x^{2}}{x^{3} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)/(x**4*(a + b*x**2)**(3/2))` | $\frac{A + B x^{2}}{x^{4} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x**5*(a + b*x**2)**(3/2))` | $\frac{A + B x^{2}}{x^{5} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)/(x**6*(a + b*x**2)**(3/2))` | $\frac{A + B x^{2}}{x^{6} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x**7*(a + b*x**2)**(3/2))` | $\frac{A + B x^{2}}{x^{7} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)/(x**8*(a + b*x**2)**(3/2))` | $\frac{A + B x^{2}}{x^{8} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**7*(A + B*x**2)/(a + b*x**2)**(5/2)` | $\frac{x^{7} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**6*(A + B*x**2)/(a + b*x**2)**(5/2)` | $\frac{x^{6} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x**2)/(a + b*x**2)**(5/2)` | $\frac{x^{5} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4*(A + B*x**2)/(a + b*x**2)**(5/2)` | $\frac{x^{4} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x**2)/(a + b*x**2)**(5/2)` | $\frac{x^{3} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2*(A + B*x**2)/(a + b*x**2)**(5/2)` | $\frac{x^{2} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x**2)/(a + b*x**2)**(5/2)` | $\frac{x \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)/(a + b*x**2)**(5/2)` | $\frac{A + B x^{2}}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x*(a + b*x**2)**(5/2))` | $\frac{A + B x^{2}}{x \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)/(x**2*(a + b*x**2)**(5/2))` | $\frac{A + B x^{2}}{x^{2} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x**3*(a + b*x**2)**(5/2))` | $\frac{A + B x^{2}}{x^{3} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)/(x**4*(a + b*x**2)**(5/2))` | $\frac{A + B x^{2}}{x^{4} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x**5*(a + b*x**2)**(5/2))` | $\frac{A + B x^{2}}{x^{5} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)/(x**6*(a + b*x**2)**(5/2))` | $\frac{A + B x^{2}}{x^{6} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**5*(a + b*x**2)**2*sqrt(c + d*x**2)` | $x^{5} \left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)**2*sqrt(c + d*x**2)` | $x^{3} \left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)**2*sqrt(c + d*x**2)` | $x \left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**3` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**5` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{5}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**7` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{7}}$ |
| partial | parametric | `x**2*(a + b*x**2)**2*sqrt(c + d*x**2)` | $x^{2} \left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)` | $\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**2` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**4` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**6` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**8` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{8}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**10` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{10}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**12` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{12}}$ |
| partial | parametric | `x**4*(a + b*x**2)**2*(c + d*x**2)**(3/2)` | $x^{4} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)**2*(c + d*x**2)**(3/2)` | $x^{3} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(a + b*x**2)**2*(c + d*x**2)**(3/2)` | $x^{2} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)**2*(c + d*x**2)**(3/2)` | $x \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(3/2)` | $\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(3/2)/x` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(3/2)/x**2` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(3/2)/x**3` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(3/2)/x**4` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(3/2)/x**5` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(3/2)/x**6` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(3/2)/x**7` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{x^{7}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)**2*(c + d*x**2)**(5/2)` | $x^{3} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**2*(a + b*x**2)**2*(c + d*x**2)**(5/2)` | $x^{2} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)**2*(c + d*x**2)**(5/2)` | $x \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(5/2)` | $\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(5/2)/x` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(5/2)/x**2` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(5/2)/x**3` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(5/2)/x**4` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(5/2)/x**5` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}{x^{5}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(5/2)/x**6` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}{x^{6}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(5/2)/x**7` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}{x^{7}}$ |
| partial | parametric | `x**4*(a + b*x**2)**2/sqrt(c + d*x**2)` | $\frac{x^{4} \left(a + b x^{2}\right)^{2}}{\sqrt{c + d x^{2}}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)**2/sqrt(c + d*x**2)` | $\frac{x^{3} \left(a + b x^{2}\right)^{2}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**2*(a + b*x**2)**2/sqrt(c + d*x**2)` | $\frac{x^{2} \left(a + b x^{2}\right)^{2}}{\sqrt{c + d x^{2}}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)**2/sqrt(c + d*x**2)` | $\frac{x \left(a + b x^{2}\right)^{2}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/sqrt(c + d*x**2)` | $\frac{\left(a + b x^{2}\right)^{2}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**2*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**3*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{3} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**4*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{4} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**5*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{5} \sqrt{c + d x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2)**2/(x**6*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{6} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**7*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{7} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**4*(a + b*x**2)**2/(c + d*x**2)**(3/2)` | $\frac{x^{4} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)**2/(c + d*x**2)**(3/2)` | $\frac{x^{3} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(a + b*x**2)**2/(c + d*x**2)**(3/2)` | $\frac{x^{2} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)**2/(c + d*x**2)**(3/2)` | $\frac{x \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(c + d*x**2)**(3/2)` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x*(c + d*x**2)**(3/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**2*(c + d*x**2)**(3/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**3*(c + d*x**2)**(3/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{3} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**2/(x**4*(c + d*x**2)**(3/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{4} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**5*(c + d*x**2)**(3/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{5} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**2/(x**6*(c + d*x**2)**(3/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{6} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**7*(c + d*x**2)**(3/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{7} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4*(a + b*x**2)**2/(c + d*x**2)**(5/2)` | $\frac{x^{4} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)**2/(c + d*x**2)**(5/2)` | $\frac{x^{3} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2*(a + b*x**2)**2/(c + d*x**2)**(5/2)` | $\frac{x^{2} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)**2/(c + d*x**2)**(5/2)` | $\frac{x \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(c + d*x**2)**(5/2)` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x*(c + d*x**2)**(5/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**2/(x**2*(c + d*x**2)**(5/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**3*(c + d*x**2)**(5/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{3} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**2/(x**4*(c + d*x**2)**(5/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{4} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(x**5*(c + d*x**2)**(5/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{5} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)**2/(x**6*(c + d*x**2)**(5/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{x^{6} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**5/(sqrt(d*x**2)*(a + b*x**2))` | $\frac{x^{5}}{\sqrt{d x^{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `x**3/(sqrt(d*x**2)*(a + b*x**2))` | $\frac{x^{3}}{\sqrt{d x^{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `x/(sqrt(d*x**2)*(a + b*x**2))` | $\frac{x}{\sqrt{d x^{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `1/(x*sqrt(d*x**2)*(a + b*x**2))` | $\frac{1}{x \sqrt{d x^{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `1/(x**3*sqrt(d*x**2)*(a + b*x**2))` | $\frac{1}{x^{3} \sqrt{d x^{2}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `x**4*sqrt(c + d*x**2)/(a + b*x**2)` | $\frac{x^{4} \sqrt{c + d x^{2}}}{a + b x^{2}}$ |
| partial | parametric | `x**3*sqrt(c + d*x**2)/(a + b*x**2)` | $\frac{x^{3} \sqrt{c + d x^{2}}}{a + b x^{2}}$ |
| partial | parametric | `x**2*sqrt(c + d*x**2)/(a + b*x**2)` | $\frac{x^{2} \sqrt{c + d x^{2}}}{a + b x^{2}}$ |
| partial | parametric | `x*sqrt(c + d*x**2)/(a + b*x**2)` | $\frac{x \sqrt{c + d x^{2}}}{a + b x^{2}}$ |
| partial | parametric | `sqrt(c + d*x**2)/(a + b*x**2)` | $\frac{\sqrt{c + d x^{2}}}{a + b x^{2}}$ |
| partial | parametric | `sqrt(c + d*x**2)/(x*(a + b*x**2))` | $\frac{\sqrt{c + d x^{2}}}{x \left(a + b x^{2}\right)}$ |
| partial | parametric | `sqrt(c + d*x**2)/(x**2*(a + b*x**2))` | $\frac{\sqrt{c + d x^{2}}}{x^{2} \left(a + b x^{2}\right)}$ |
| partial | parametric | `sqrt(c + d*x**2)/(x**3*(a + b*x**2))` | $\frac{\sqrt{c + d x^{2}}}{x^{3} \left(a + b x^{2}\right)}$ |
| partial | parametric | `sqrt(c + d*x**2)/(x**4*(a + b*x**2))` | $\frac{\sqrt{c + d x^{2}}}{x^{4} \left(a + b x^{2}\right)}$ |
| partial | parametric | `x**4*(c + d*x**2)**(3/2)/(a + b*x**2)` | $\frac{x^{4} \left(c + d x^{2}\right)^{\frac{3}{2}}}{a + b x^{2}}$ |
| partial | parametric | `x**3*(c + d*x**2)**(3/2)/(a + b*x**2)` | $\frac{x^{3} \left(c + d x^{2}\right)^{\frac{3}{2}}}{a + b x^{2}}$ |
| partial | parametric | `x**2*(c + d*x**2)**(3/2)/(a + b*x**2)` | $\frac{x^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{a + b x^{2}}$ |
| partial | parametric | `x*(c + d*x**2)**(3/2)/(a + b*x**2)` | $\frac{x \left(c + d x^{2}\right)^{\frac{3}{2}}}{a + b x^{2}}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(a + b*x**2)` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{a + b x^{2}}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(x*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{x \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(x**2*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{x^{2} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(x**3*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{x^{3} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(x**4*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{x^{4} \left(a + b x^{2}\right)}$ |
| partial | parametric | `x**4*(c + d*x**2)**(5/2)/(a + b*x**2)` | $\frac{x^{4} \left(c + d x^{2}\right)^{\frac{5}{2}}}{a + b x^{2}}$ |
| partial | parametric | `x**3*(c + d*x**2)**(5/2)/(a + b*x**2)` | $\frac{x^{3} \left(c + d x^{2}\right)^{\frac{5}{2}}}{a + b x^{2}}$ |
| partial | parametric | `x**2*(c + d*x**2)**(5/2)/(a + b*x**2)` | $\frac{x^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}{a + b x^{2}}$ |
| partial | parametric | `x*(c + d*x**2)**(5/2)/(a + b*x**2)` | $\frac{x \left(c + d x^{2}\right)^{\frac{5}{2}}}{a + b x^{2}}$ |
| partial | parametric | `(c + d*x**2)**(5/2)/(a + b*x**2)` | $\frac{\left(c + d x^{2}\right)^{\frac{5}{2}}}{a + b x^{2}}$ |
| partial | parametric | `(c + d*x**2)**(5/2)/(x*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{\frac{5}{2}}}{x \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**(5/2)/(x**2*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{\frac{5}{2}}}{x^{2} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**(5/2)/(x**3*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{\frac{5}{2}}}{x^{3} \left(a + b x^{2}\right)}$ |
| partial | parametric | `(c + d*x**2)**(5/2)/(x**4*(a + b*x**2))` | $\frac{\left(c + d x^{2}\right)^{\frac{5}{2}}}{x^{4} \left(a + b x^{2}\right)}$ |
| partial | parametric | `x**5/((a + b*x**2)*sqrt(c + d*x**2))` | $\frac{x^{5}}{\left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**3/((a + b*x**2)*sqrt(c + d*x**2))` | $\frac{x^{3}}{\left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x/((a + b*x**2)*sqrt(c + d*x**2))` | $\frac{x}{\left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{x \left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{x^{3} \left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**4/((a + b*x**2)*sqrt(c + d*x**2))` | $\frac{x^{4}}{\left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**2/((a + b*x**2)*sqrt(c + d*x**2))` | $\frac{x^{2}}{\left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/((a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{x^{2} \left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{x^{4} \left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**4/((a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{x^{4}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/((a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{x^{3}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/((a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{x^{2}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/((a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{x}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{1}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{1}{x \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{1}{x^{2} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{1}{x^{3} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{1}{x^{4} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/((a + b*x**2)*(c + d*x**2)**(5/2))` | $\frac{x^{4}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3/((a + b*x**2)*(c + d*x**2)**(5/2))` | $\frac{x^{3}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2/((a + b*x**2)*(c + d*x**2)**(5/2))` | $\frac{x^{2}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x/((a + b*x**2)*(c + d*x**2)**(5/2))` | $\frac{x}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((a + b*x**2)*(c + d*x**2)**(5/2))` | $\frac{1}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**2)*(c + d*x**2)**(5/2))` | $\frac{1}{x \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)*(c + d*x**2)**(5/2))` | $\frac{1}{x^{2} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2)*(c + d*x**2)**(5/2))` | $\frac{1}{x^{3} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)*(c + d*x**2)**(5/2))` | $\frac{1}{x^{4} \left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4*sqrt(c + d*x**2)/(a + b*x**2)**2` | $\frac{x^{4} \sqrt{c + d x^{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**3*sqrt(c + d*x**2)/(a + b*x**2)**2` | $\frac{x^{3} \sqrt{c + d x^{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**2*sqrt(c + d*x**2)/(a + b*x**2)**2` | $\frac{x^{2} \sqrt{c + d x^{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x*sqrt(c + d*x**2)/(a + b*x**2)**2` | $\frac{x \sqrt{c + d x^{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**2)/(a + b*x**2)**2` | $\frac{\sqrt{c + d x^{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**2)/(x*(a + b*x**2)**2)` | $\frac{\sqrt{c + d x^{2}}}{x \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**2)/(x**2*(a + b*x**2)**2)` | $\frac{\sqrt{c + d x^{2}}}{x^{2} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**2)/(x**3*(a + b*x**2)**2)` | $\frac{\sqrt{c + d x^{2}}}{x^{3} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**2)/(x**4*(a + b*x**2)**2)` | $\frac{\sqrt{c + d x^{2}}}{x^{4} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**4*(c + d*x**2)**(3/2)/(a + b*x**2)**2` | $\frac{x^{4} \left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**3*(c + d*x**2)**(3/2)/(a + b*x**2)**2` | $\frac{x^{3} \left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**2*(c + d*x**2)**(3/2)/(a + b*x**2)**2` | $\frac{x^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x*(c + d*x**2)**(3/2)/(a + b*x**2)**2` | $\frac{x \left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(a + b*x**2)**2` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(x*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{x \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(x**2*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{x^{2} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(x**3*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{x^{3} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**(3/2)/(x**4*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{x^{4} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**4*(c + d*x**2)**(5/2)/(a + b*x**2)**2` | $\frac{x^{4} \left(c + d x^{2}\right)^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**3*(c + d*x**2)**(5/2)/(a + b*x**2)**2` | $\frac{x^{3} \left(c + d x^{2}\right)^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**2*(c + d*x**2)**(5/2)/(a + b*x**2)**2` | $\frac{x^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x*(c + d*x**2)**(5/2)/(a + b*x**2)**2` | $\frac{x \left(c + d x^{2}\right)^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**(5/2)/(a + b*x**2)**2` | $\frac{\left(c + d x^{2}\right)^{\frac{5}{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**(5/2)/(x*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{\frac{5}{2}}}{x \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**(5/2)/(x**2*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{\frac{5}{2}}}{x^{2} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**(5/2)/(x**3*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{\frac{5}{2}}}{x^{3} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `(c + d*x**2)**(5/2)/(x**4*(a + b*x**2)**2)` | $\frac{\left(c + d x^{2}\right)^{\frac{5}{2}}}{x^{4} \left(a + b x^{2}\right)^{2}}$ |
| partial | parametric | `x**4/((a + b*x**2)**2*sqrt(c + d*x**2))` | $\frac{x^{4}}{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**3/((a + b*x**2)**2*sqrt(c + d*x**2))` | $\frac{x^{3}}{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**2/((a + b*x**2)**2*sqrt(c + d*x**2))` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x/((a + b*x**2)**2*sqrt(c + d*x**2))` | $\frac{x}{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/((a + b*x**2)**2*sqrt(c + d*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**2)**2*sqrt(c + d*x**2))` | $\frac{1}{x \left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)**2*sqrt(c + d*x**2))` | $\frac{1}{x^{2} \left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2)**2*sqrt(c + d*x**2))` | $\frac{1}{x^{3} \left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)**2*sqrt(c + d*x**2))` | $\frac{1}{x^{4} \left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**4/((a + b*x**2)**2*(c + d*x**2)**(3/2))` | $\frac{x^{4}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/((a + b*x**2)**2*(c + d*x**2)**(3/2))` | $\frac{x^{3}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/((a + b*x**2)**2*(c + d*x**2)**(3/2))` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/((a + b*x**2)**2*(c + d*x**2)**(3/2))` | $\frac{x}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x**2)**2*(c + d*x**2)**(3/2))` | $\frac{1}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**2)**2*(c + d*x**2)**(3/2))` | $\frac{1}{x \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)**2*(c + d*x**2)**(3/2))` | $\frac{1}{x^{2} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2)**2*(c + d*x**2)**(3/2))` | $\frac{1}{x^{3} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)**2*(c + d*x**2)**(3/2))` | $\frac{1}{x^{4} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/((a + b*x**2)**2*(c + d*x**2)**(5/2))` | $\frac{x^{4}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3/((a + b*x**2)**2*(c + d*x**2)**(5/2))` | $\frac{x^{3}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2/((a + b*x**2)**2*(c + d*x**2)**(5/2))` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x/((a + b*x**2)**2*(c + d*x**2)**(5/2))` | $\frac{x}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((a + b*x**2)**2*(c + d*x**2)**(5/2))` | $\frac{1}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**2)**2*(c + d*x**2)**(5/2))` | $\frac{1}{x \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2)**2*(c + d*x**2)**(5/2))` | $\frac{1}{x^{2} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2)**2*(c + d*x**2)**(5/2))` | $\frac{1}{x^{3} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**2)**2*(c + d*x**2)**(5/2))` | $\frac{1}{x^{4} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x**2)*sqrt(a + b*x**2)` | $\left(e x\right)^{\frac{3}{2}} \left(A + B x^{2}\right) \sqrt{a + b x^{2}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x**2)*sqrt(a + b*x**2)` | $\sqrt{e x} \left(A + B x^{2}\right) \sqrt{a + b x^{2}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/sqrt(e*x)` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{\sqrt{e x}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/(e*x)**(3/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{\left(e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/(e*x)**(5/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{\left(e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/(e*x)**(7/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{\left(e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**(9/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**(11/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)/x**(13/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}}}{x^{\frac{13}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x**2)*(a + b*x**2)**(3/2)` | $\left(e x\right)^{\frac{3}{2}} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x**2)*(a + b*x**2)**(3/2)` | $\sqrt{e x} \left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/sqrt(e*x)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{\sqrt{e x}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/(e*x)**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/(e*x)**(5/2)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)**(3/2)/(e*x)**(7/2)` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x**2)/sqrt(a + b*x**2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(A + B x^{2}\right)}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x**2)/sqrt(a + b*x**2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(A + B x^{2}\right)}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x**2)/sqrt(a + b*x**2)` | $\frac{\sqrt{e x} \left(A + B x^{2}\right)}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(e*x)*sqrt(a + b*x**2))` | $\frac{A + B x^{2}}{\sqrt{e x} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x**2)/((e*x)**(3/2)*sqrt(a + b*x**2))` | $\frac{A + B x^{2}}{\left(e x\right)^{\frac{3}{2}} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x**2)/((e*x)**(5/2)*sqrt(a + b*x**2))` | $\frac{A + B x^{2}}{\left(e x\right)^{\frac{5}{2}} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x**2)/((e*x)**(7/2)*sqrt(a + b*x**2))` | $\frac{A + B x^{2}}{\left(e x\right)^{\frac{7}{2}} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*(A + B*x**2)/(a + b*x**2)**(3/2)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x**2)/(a + b*x**2)**(3/2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x**2)/(a + b*x**2)**(3/2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x**2)/(a + b*x**2)**(3/2)` | $\frac{\sqrt{e x} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(e*x)*(a + b*x**2)**(3/2))` | $\frac{A + B x^{2}}{\sqrt{e x} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/((e*x)**(3/2)*(a + b*x**2)**(3/2))` | $\frac{A + B x^{2}}{\left(e x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/((e*x)**(5/2)*(a + b*x**2)**(3/2))` | $\frac{A + B x^{2}}{\left(e x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/((e*x)**(7/2)*(a + b*x**2)**(3/2))` | $\frac{A + B x^{2}}{\left(e x\right)^{\frac{7}{2}} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*(A + B*x**2)/(a + b*x**2)**(5/2)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x**2)/(a + b*x**2)**(5/2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x**2)/(a + b*x**2)**(5/2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x**2)/(a + b*x**2)**(5/2)` | $\frac{\sqrt{e x} \left(A + B x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(e*x)*(a + b*x**2)**(5/2))` | $\frac{A + B x^{2}}{\sqrt{e x} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**2)/((e*x)**(3/2)*(a + b*x**2)**(5/2))` | $\frac{A + B x^{2}}{\left(e x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**2)/((e*x)**(5/2)*(a + b*x**2)**(5/2))` | $\frac{A + B x^{2}}{\left(e x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(a + b*x**2)**2*sqrt(c + d*x**2)` | $\left(e x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}$ |
| partial | parametric | `sqrt(e*x)*(a + b*x**2)**2*sqrt(c + d*x**2)` | $\sqrt{e x} \left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/sqrt(e*x)` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{\sqrt{e x}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/(e*x)**(3/2)` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{\left(e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/(e*x)**(5/2)` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{\left(e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/(e*x)**(7/2)` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{\left(e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**(9/2)` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**(11/2)` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**(13/2)` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{\frac{13}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2*sqrt(c + d*x**2)/x**(15/2)` | $\frac{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}}}{x^{\frac{15}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(a + b*x**2)**2*(c + d*x**2)**(3/2)` | $\left(e x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(e*x)**(3/2)*(a + b*x**2)**2*(c + d*x**2)**(3/2)` | $\left(e x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(e*x)*(a + b*x**2)**2*(c + d*x**2)**(3/2)` | $\sqrt{e x} \left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(3/2)/sqrt(e*x)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{\sqrt{e x}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(3/2)/(e*x)**(3/2)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(3/2)/(e*x)**(5/2)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2*(c + d*x**2)**(3/2)/(e*x)**(7/2)` | $\frac{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(a + b*x**2)**2/sqrt(c + d*x**2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{2}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(a + b*x**2)**2/sqrt(c + d*x**2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{2}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(e*x)*(a + b*x**2)**2/sqrt(c + d*x**2)` | $\frac{\sqrt{e x} \left(a + b x^{2}\right)^{2}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(sqrt(e*x)*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\sqrt{e x} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((e*x)**(3/2)*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(e x\right)^{\frac{3}{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((e*x)**(5/2)*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(e x\right)^{\frac{5}{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((e*x)**(7/2)*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(e x\right)^{\frac{7}{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((e*x)**(9/2)*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(e x\right)^{\frac{9}{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((e*x)**(11/2)*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(e x\right)^{\frac{11}{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((e*x)**(13/2)*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(e x\right)^{\frac{13}{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*(a + b*x**2)**2/(c + d*x**2)**(3/2)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(a + b*x**2)**2/(c + d*x**2)**(3/2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(a + b*x**2)**2/(c + d*x**2)**(3/2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(e*x)*(a + b*x**2)**2/(c + d*x**2)**(3/2)` | $\frac{\sqrt{e x} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(sqrt(e*x)*(c + d*x**2)**(3/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\sqrt{e x} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((e*x)**(3/2)*(c + d*x**2)**(3/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(e x\right)^{\frac{3}{2}} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((e*x)**(5/2)*(c + d*x**2)**(3/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(e x\right)^{\frac{5}{2}} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((e*x)**(7/2)*(c + d*x**2)**(3/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(e x\right)^{\frac{7}{2}} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*(a + b*x**2)**2/(c + d*x**2)**(5/2)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(a + b*x**2)**2/(c + d*x**2)**(5/2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(a + b*x**2)**2/(c + d*x**2)**(5/2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(e*x)*(a + b*x**2)**2/(c + d*x**2)**(5/2)` | $\frac{\sqrt{e x} \left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/(sqrt(e*x)*(c + d*x**2)**(5/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\sqrt{e x} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((e*x)**(3/2)*(c + d*x**2)**(5/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(e x\right)^{\frac{3}{2}} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((e*x)**(5/2)*(c + d*x**2)**(5/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(e x\right)^{\frac{5}{2}} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((e*x)**(7/2)*(c + d*x**2)**(5/2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(e x\right)^{\frac{7}{2}} \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*sqrt(c - d*x**2)/(a - b*x**2)` | $\frac{\left(e x\right)^{\frac{7}{2}} \sqrt{c - d x^{2}}}{a - b x^{2}}$ |
| partial | parametric | `(e*x)**(5/2)*sqrt(c - d*x**2)/(a - b*x**2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \sqrt{c - d x^{2}}}{a - b x^{2}}$ |
| partial | parametric | `(e*x)**(3/2)*sqrt(c - d*x**2)/(a - b*x**2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \sqrt{c - d x^{2}}}{a - b x^{2}}$ |
| partial | parametric | `sqrt(e*x)*sqrt(c - d*x**2)/(a - b*x**2)` | $\frac{\sqrt{e x} \sqrt{c - d x^{2}}}{a - b x^{2}}$ |
| partial | parametric | `sqrt(c - d*x**2)/(sqrt(e*x)*(a - b*x**2))` | $\frac{\sqrt{c - d x^{2}}}{\sqrt{e x} \left(a - b x^{2}\right)}$ |
| partial | parametric | `sqrt(c - d*x**2)/((e*x)**(3/2)*(a - b*x**2))` | $\frac{\sqrt{c - d x^{2}}}{\left(e x\right)^{\frac{3}{2}} \left(a - b x^{2}\right)}$ |
| partial | parametric | `sqrt(c - d*x**2)/((e*x)**(5/2)*(a - b*x**2))` | $\frac{\sqrt{c - d x^{2}}}{\left(e x\right)^{\frac{5}{2}} \left(a - b x^{2}\right)}$ |
| partial | parametric | `sqrt(c - d*x**2)/((e*x)**(7/2)*(a - b*x**2))` | $\frac{\sqrt{c - d x^{2}}}{\left(e x\right)^{\frac{7}{2}} \left(a - b x^{2}\right)}$ |
| partial | parametric | `(e*x)**(5/2)*(c - d*x**2)**(3/2)/(a - b*x**2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(c - d x^{2}\right)^{\frac{3}{2}}}{a - b x^{2}}$ |
| partial | parametric | `(e*x)**(3/2)*(c - d*x**2)**(3/2)/(a - b*x**2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(c - d x^{2}\right)^{\frac{3}{2}}}{a - b x^{2}}$ |
| partial | parametric | `sqrt(e*x)*(c - d*x**2)**(3/2)/(a - b*x**2)` | $\frac{\sqrt{e x} \left(c - d x^{2}\right)^{\frac{3}{2}}}{a - b x^{2}}$ |
| partial | parametric | `(c - d*x**2)**(3/2)/(sqrt(e*x)*(a - b*x**2))` | $\frac{\left(c - d x^{2}\right)^{\frac{3}{2}}}{\sqrt{e x} \left(a - b x^{2}\right)}$ |
| partial | parametric | `(c - d*x**2)**(3/2)/((e*x)**(3/2)*(a - b*x**2))` | $\frac{\left(c - d x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{3}{2}} \left(a - b x^{2}\right)}$ |
| partial | parametric | `(c - d*x**2)**(3/2)/((e*x)**(5/2)*(a - b*x**2))` | $\frac{\left(c - d x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{5}{2}} \left(a - b x^{2}\right)}$ |
| partial | parametric | `(c - d*x**2)**(3/2)/((e*x)**(7/2)*(a - b*x**2))` | $\frac{\left(c - d x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{7}{2}} \left(a - b x^{2}\right)}$ |
| partial | parametric | `(e*x)**(7/2)/((a - b*x**2)*sqrt(c - d*x**2))` | $\frac{\left(e x\right)^{\frac{7}{2}}}{\left(a - b x^{2}\right) \sqrt{c - d x^{2}}}$ |
| partial | parametric | `(e*x)**(5/2)/((a - b*x**2)*sqrt(c - d*x**2))` | $\frac{\left(e x\right)^{\frac{5}{2}}}{\left(a - b x^{2}\right) \sqrt{c - d x^{2}}}$ |
| partial | parametric | `(e*x)**(3/2)/((a - b*x**2)*sqrt(c - d*x**2))` | $\frac{\left(e x\right)^{\frac{3}{2}}}{\left(a - b x^{2}\right) \sqrt{c - d x^{2}}}$ |
| partial | parametric | `sqrt(e*x)/((a - b*x**2)*sqrt(c - d*x**2))` | $\frac{\sqrt{e x}}{\left(a - b x^{2}\right) \sqrt{c - d x^{2}}}$ |
| partial | parametric | `1/(sqrt(e*x)*(a - b*x**2)*sqrt(c - d*x**2))` | $\frac{1}{\sqrt{e x} \left(a - b x^{2}\right) \sqrt{c - d x^{2}}}$ |
| partial | parametric | `1/((e*x)**(3/2)*(a - b*x**2)*sqrt(c - d*x**2))` | $\frac{1}{\left(e x\right)^{\frac{3}{2}} \left(a - b x^{2}\right) \sqrt{c - d x^{2}}}$ |
| partial | parametric | `1/((e*x)**(5/2)*(a - b*x**2)*sqrt(c - d*x**2))` | $\frac{1}{\left(e x\right)^{\frac{5}{2}} \left(a - b x^{2}\right) \sqrt{c - d x^{2}}}$ |
| partial | parametric | `1/((e*x)**(7/2)*(a - b*x**2)*sqrt(c - d*x**2))` | $\frac{1}{\left(e x\right)^{\frac{7}{2}} \left(a - b x^{2}\right) \sqrt{c - d x^{2}}}$ |
| partial | parametric | `(e*x)**(9/2)/((a - b*x**2)*(c - d*x**2)**(3/2))` | $\frac{\left(e x\right)^{\frac{9}{2}}}{\left(a - b x^{2}\right) \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)/((a - b*x**2)*(c - d*x**2)**(3/2))` | $\frac{\left(e x\right)^{\frac{7}{2}}}{\left(a - b x^{2}\right) \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)/((a - b*x**2)*(c - d*x**2)**(3/2))` | $\frac{\left(e x\right)^{\frac{5}{2}}}{\left(a - b x^{2}\right) \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)/((a - b*x**2)*(c - d*x**2)**(3/2))` | $\frac{\left(e x\right)^{\frac{3}{2}}}{\left(a - b x^{2}\right) \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(e*x)/((a - b*x**2)*(c - d*x**2)**(3/2))` | $\frac{\sqrt{e x}}{\left(a - b x^{2}\right) \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(e*x)*(a - b*x**2)*(c - d*x**2)**(3/2))` | $\frac{1}{\sqrt{e x} \left(a - b x^{2}\right) \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((e*x)**(3/2)*(a - b*x**2)*(c - d*x**2)**(3/2))` | $\frac{1}{\left(e x\right)^{\frac{3}{2}} \left(a - b x^{2}\right) \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((e*x)**(5/2)*(a - b*x**2)*(c - d*x**2)**(3/2))` | $\frac{1}{\left(e x\right)^{\frac{5}{2}} \left(a - b x^{2}\right) \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*sqrt(c - d*x**2)/(a - b*x**2)**2` | $\frac{\left(e x\right)^{\frac{7}{2}} \sqrt{c - d x^{2}}}{\left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `(e*x)**(5/2)*sqrt(c - d*x**2)/(a - b*x**2)**2` | $\frac{\left(e x\right)^{\frac{5}{2}} \sqrt{c - d x^{2}}}{\left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `(e*x)**(3/2)*sqrt(c - d*x**2)/(a - b*x**2)**2` | $\frac{\left(e x\right)^{\frac{3}{2}} \sqrt{c - d x^{2}}}{\left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(e*x)*sqrt(c - d*x**2)/(a - b*x**2)**2` | $\frac{\sqrt{e x} \sqrt{c - d x^{2}}}{\left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(c - d*x**2)/(sqrt(e*x)*(a - b*x**2)**2)` | $\frac{\sqrt{c - d x^{2}}}{\sqrt{e x} \left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(c - d*x**2)/((e*x)**(3/2)*(a - b*x**2)**2)` | $\frac{\sqrt{c - d x^{2}}}{\left(e x\right)^{\frac{3}{2}} \left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(c - d*x**2)/((e*x)**(5/2)*(a - b*x**2)**2)` | $\frac{\sqrt{c - d x^{2}}}{\left(e x\right)^{\frac{5}{2}} \left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `(e*x)**(7/2)*(c - d*x**2)**(3/2)/(a - b*x**2)**2` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(c - d x^{2}\right)^{\frac{3}{2}}}{\left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `(e*x)**(5/2)*(c - d*x**2)**(3/2)/(a - b*x**2)**2` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(c - d x^{2}\right)^{\frac{3}{2}}}{\left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `(e*x)**(3/2)*(c - d*x**2)**(3/2)/(a - b*x**2)**2` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(c - d x^{2}\right)^{\frac{3}{2}}}{\left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(e*x)*(c - d*x**2)**(3/2)/(a - b*x**2)**2` | $\frac{\sqrt{e x} \left(c - d x^{2}\right)^{\frac{3}{2}}}{\left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `(c - d*x**2)**(3/2)/(sqrt(e*x)*(a - b*x**2)**2)` | $\frac{\left(c - d x^{2}\right)^{\frac{3}{2}}}{\sqrt{e x} \left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `(c - d*x**2)**(3/2)/((e*x)**(3/2)*(a - b*x**2)**2)` | $\frac{\left(c - d x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{3}{2}} \left(a - b x^{2}\right)^{2}}$ |
| partial | parametric | `(c - d*x**2)**(3/2)/((e*x)**(5/2)*(a - b*x**2)**2)` | $\frac{\left(c - d x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{5}{2}} \left(a - b x^{2}\right)^{2}}$ |
| timeout | parametric | `(e*x)**(9/2)/((a - b*x**2)**2*sqrt(c - d*x**2))` | $\frac{\left(e x\right)^{\frac{9}{2}}}{\left(a - b x^{2}\right)^{2} \sqrt{c - d x^{2}}}$ |
| partial | parametric | `(e*x)**(7/2)/((a - b*x**2)**2*sqrt(c - d*x**2))` | $\frac{\left(e x\right)^{\frac{7}{2}}}{\left(a - b x^{2}\right)^{2} \sqrt{c - d x^{2}}}$ |
| partial | parametric | `(e*x)**(5/2)/((a - b*x**2)**2*sqrt(c - d*x**2))` | $\frac{\left(e x\right)^{\frac{5}{2}}}{\left(a - b x^{2}\right)^{2} \sqrt{c - d x^{2}}}$ |
| partial | parametric | `(e*x)**(3/2)/((a - b*x**2)**2*sqrt(c - d*x**2))` | $\frac{\left(e x\right)^{\frac{3}{2}}}{\left(a - b x^{2}\right)^{2} \sqrt{c - d x^{2}}}$ |
| partial | parametric | `sqrt(e*x)/((a - b*x**2)**2*sqrt(c - d*x**2))` | $\frac{\sqrt{e x}}{\left(a - b x^{2}\right)^{2} \sqrt{c - d x^{2}}}$ |
| partial | parametric | `1/(sqrt(e*x)*(a - b*x**2)**2*sqrt(c - d*x**2))` | $\frac{1}{\sqrt{e x} \left(a - b x^{2}\right)^{2} \sqrt{c - d x^{2}}}$ |
| partial | parametric | `1/((e*x)**(3/2)*(a - b*x**2)**2*sqrt(c - d*x**2))` | $\frac{1}{\left(e x\right)^{\frac{3}{2}} \left(a - b x^{2}\right)^{2} \sqrt{c - d x^{2}}}$ |
| partial | parametric | `1/((e*x)**(5/2)*(a - b*x**2)**2*sqrt(c - d*x**2))` | $\frac{1}{\left(e x\right)^{\frac{5}{2}} \left(a - b x^{2}\right)^{2} \sqrt{c - d x^{2}}}$ |
| timeout | parametric | `(e*x)**(9/2)/((a - b*x**2)**2*(c - d*x**2)**(3/2))` | $\frac{\left(e x\right)^{\frac{9}{2}}}{\left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)/((a - b*x**2)**2*(c - d*x**2)**(3/2))` | $\frac{\left(e x\right)^{\frac{7}{2}}}{\left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)/((a - b*x**2)**2*(c - d*x**2)**(3/2))` | $\frac{\left(e x\right)^{\frac{5}{2}}}{\left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)/((a - b*x**2)**2*(c - d*x**2)**(3/2))` | $\frac{\left(e x\right)^{\frac{3}{2}}}{\left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(e*x)/((a - b*x**2)**2*(c - d*x**2)**(3/2))` | $\frac{\sqrt{e x}}{\left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(e*x)*(a - b*x**2)**2*(c - d*x**2)**(3/2))` | $\frac{1}{\sqrt{e x} \left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((e*x)**(3/2)*(a - b*x**2)**2*(c - d*x**2)**(3/2))` | $\frac{1}{\left(e x\right)^{\frac{3}{2}} \left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((e*x)**(5/2)*(a - b*x**2)**2*(c - d*x**2)**(3/2))` | $\frac{1}{\left(e x\right)^{\frac{5}{2}} \left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(e*x)**(9/2)/((a - b*x**2)**2*(c - d*x**2)**(5/2))` | $\frac{\left(e x\right)^{\frac{9}{2}}}{\left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)/((a - b*x**2)**2*(c - d*x**2)**(5/2))` | $\frac{\left(e x\right)^{\frac{7}{2}}}{\left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)/((a - b*x**2)**2*(c - d*x**2)**(5/2))` | $\frac{\left(e x\right)^{\frac{5}{2}}}{\left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)/((a - b*x**2)**2*(c - d*x**2)**(5/2))` | $\frac{\left(e x\right)^{\frac{3}{2}}}{\left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(e*x)/((a - b*x**2)**2*(c - d*x**2)**(5/2))` | $\frac{\sqrt{e x}}{\left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(e*x)*(a - b*x**2)**2*(c - d*x**2)**(5/2))` | $\frac{1}{\sqrt{e x} \left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((e*x)**(3/2)*(a - b*x**2)**2*(c - d*x**2)**(5/2))` | $\frac{1}{\left(e x\right)^{\frac{3}{2}} \left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((e*x)**(5/2)*(a - b*x**2)**2*(c - d*x**2)**(5/2))` | $\frac{1}{\left(e x\right)^{\frac{5}{2}} \left(a - b x^{2}\right)^{2} \left(c - d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**5*sqrt(a + b*x**2)/sqrt(c + d*x**2)` | $\frac{x^{5} \sqrt{a + b x^{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**3*sqrt(a + b*x**2)/sqrt(c + d*x**2)` | $\frac{x^{3} \sqrt{a + b x^{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `x*sqrt(a + b*x**2)/sqrt(c + d*x**2)` | $\frac{x \sqrt{a + b x^{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(x*sqrt(c + d*x**2))` | $\frac{\sqrt{a + b x^{2}}}{x \sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(x**3*sqrt(c + d*x**2))` | $\frac{\sqrt{a + b x^{2}}}{x^{3} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(x**5*sqrt(c + d*x**2))` | $\frac{\sqrt{a + b x^{2}}}{x^{5} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**4*sqrt(a + b*x**2)/sqrt(c + d*x**2)` | $\frac{x^{4} \sqrt{a + b x^{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**2*sqrt(a + b*x**2)/sqrt(c + d*x**2)` | $\frac{x^{2} \sqrt{a + b x^{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(x**2*sqrt(c + d*x**2))` | $\frac{\sqrt{a + b x^{2}}}{x^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/(x**4*sqrt(c + d*x**2))` | $\frac{\sqrt{a + b x^{2}}}{x^{4} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**5*(a + b*x**2)**(3/2)/sqrt(c + d*x**2)` | $\frac{x^{5} \left(a + b x^{2}\right)^{\frac{3}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**3*(a + b*x**2)**(3/2)/sqrt(c + d*x**2)` | $\frac{x^{3} \left(a + b x^{2}\right)^{\frac{3}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `x*(a + b*x**2)**(3/2)/sqrt(c + d*x**2)` | $\frac{x \left(a + b x^{2}\right)^{\frac{3}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(x*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(x**3*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{3} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(x**5*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{5} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**4*(a + b*x**2)**(3/2)/sqrt(c + d*x**2)` | $\frac{x^{4} \left(a + b x^{2}\right)^{\frac{3}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**2*(a + b*x**2)**(3/2)/sqrt(c + d*x**2)` | $\frac{x^{2} \left(a + b x^{2}\right)^{\frac{3}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(x**2*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/(x**4*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{4} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**5*(a + b*x**2)**(5/2)/sqrt(c + d*x**2)` | $\frac{x^{5} \left(a + b x^{2}\right)^{\frac{5}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**3*(a + b*x**2)**(5/2)/sqrt(c + d*x**2)` | $\frac{x^{3} \left(a + b x^{2}\right)^{\frac{5}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `x*(a + b*x**2)**(5/2)/sqrt(c + d*x**2)` | $\frac{x \left(a + b x^{2}\right)^{\frac{5}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/(x*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/(x**3*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{3} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/(x**5*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{5} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**4*(a + b*x**2)**(5/2)/sqrt(c + d*x**2)` | $\frac{x^{4} \left(a + b x^{2}\right)^{\frac{5}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**2*(a + b*x**2)**(5/2)/sqrt(c + d*x**2)` | $\frac{x^{2} \left(a + b x^{2}\right)^{\frac{5}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/(x**2*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{2} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/(x**4*sqrt(c + d*x**2))` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{4} \sqrt{c + d x^{2}}}$ |
| partial | concrete | `x**4*sqrt(3*x**2 - 1)/sqrt(2 - 3*x**2)` | $\frac{x^{4} \sqrt{3 x^{2} - 1}}{\sqrt{2 - 3 x^{2}}}$ |
| partial | concrete | `x**3*sqrt(3*x**2 - 1)/sqrt(2 - 3*x**2)` | $\frac{x^{3} \sqrt{3 x^{2} - 1}}{\sqrt{2 - 3 x^{2}}}$ |
| partial | concrete | `x**2*sqrt(3*x**2 - 1)/sqrt(2 - 3*x**2)` | $\frac{x^{2} \sqrt{3 x^{2} - 1}}{\sqrt{2 - 3 x^{2}}}$ |
| partial | concrete | `x*sqrt(3*x**2 - 1)/sqrt(2 - 3*x**2)` | $\frac{x \sqrt{3 x^{2} - 1}}{\sqrt{2 - 3 x^{2}}}$ |
| partial | parametric | `x**2*sqrt(b*x**2 + 2)/sqrt(d*x**2 + 3)` | $\frac{x^{2} \sqrt{b x^{2} + 2}}{\sqrt{d x^{2} + 3}}$ |
| partial | parametric | `x**5/(sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{x^{5}}{\sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**3/(sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{x^{3}}{\sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x/(sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{x}{\sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{x \sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x**3*sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{x^{3} \sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x**5*sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{x^{5} \sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**6/(sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{x^{6}}{\sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**4/(sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{x^{4}}{\sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**2/(sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{x^{2}}{\sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{x^{2} \sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `1/(x**4*sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{1}{x^{4} \sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**5/((a + b*x**2)**(3/2)*sqrt(c + d*x**2))` | $\frac{x^{5}}{\left(a + b x^{2}\right)^{\frac{3}{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**3/((a + b*x**2)**(3/2)*sqrt(c + d*x**2))` | $\frac{x^{3}}{\left(a + b x^{2}\right)^{\frac{3}{2}} \sqrt{c + d x^{2}}}$ |
| **SOLVED-NEW** | parametric | `x/((a + b*x**2)**(3/2)*sqrt(c + d*x**2))` | $\frac{x}{\left(a + b x^{2}\right)^{\frac{3}{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**5/((a + b*x**2)**(5/2)*sqrt(c + d*x**2))` | $\frac{x^{5}}{\left(a + b x^{2}\right)^{\frac{5}{2}} \sqrt{c + d x^{2}}}$ |
| **SOLVED-NEW** | parametric | `x**3/((a + b*x**2)**(5/2)*sqrt(c + d*x**2))` | $\frac{x^{3}}{\left(a + b x^{2}\right)^{\frac{5}{2}} \sqrt{c + d x^{2}}}$ |
| **SOLVED-NEW** | parametric | `x/((a + b*x**2)**(5/2)*sqrt(c + d*x**2))` | $\frac{x}{\left(a + b x^{2}\right)^{\frac{5}{2}} \sqrt{c + d x^{2}}}$ |
| **SOLVED-NEW** | parametric | `x**5/((a + b*x**2)**(7/2)*sqrt(c + d*x**2))` | $\frac{x^{5}}{\left(a + b x^{2}\right)^{\frac{7}{2}} \sqrt{c + d x^{2}}}$ |
| **SOLVED-NEW** | parametric | `x**3/((a + b*x**2)**(7/2)*sqrt(c + d*x**2))` | $\frac{x^{3}}{\left(a + b x^{2}\right)^{\frac{7}{2}} \sqrt{c + d x^{2}}}$ |
| **SOLVED-NEW** | parametric | `x/((a + b*x**2)**(7/2)*sqrt(c + d*x**2))` | $\frac{x}{\left(a + b x^{2}\right)^{\frac{7}{2}} \sqrt{c + d x^{2}}}$ |
| **SOLVED-NEW** | parametric | `x**5/((a + b*x**2)**(9/2)*sqrt(c + d*x**2))` | $\frac{x^{5}}{\left(a + b x^{2}\right)^{\frac{9}{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x/(sqrt(a - b*x**2)*sqrt(c + d*x**2))` | $\frac{x}{\sqrt{a - b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x/(sqrt(a - b*x**2)*sqrt(c - d*x**2))` | $\frac{x}{\sqrt{a - b x^{2}} \sqrt{c - d x^{2}}}$ |
| partial | parametric | `x**2/(sqrt(b*x**2 + 2)*sqrt(d*x**2 + 3))` | $\frac{x^{2}}{\sqrt{b x^{2} + 2} \sqrt{d x^{2} + 3}}$ |
| partial | parametric | `x**2/(sqrt(4 - x**2)*sqrt(c + d*x**2))` | $\frac{x^{2}}{\sqrt{4 - x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | parametric | `x**2/(sqrt(c + d*x**2)*sqrt(x**2 + 4))` | $\frac{x^{2}}{\sqrt{c + d x^{2}} \sqrt{x^{2} + 4}}$ |
| partial | concrete | `x**2/(sqrt(1 - x**2)*sqrt(3*x**2 + 2))` | $\frac{x^{2}}{\sqrt{1 - x^{2}} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `x**2/(sqrt(1 - x**2)*sqrt(2 - 3*x**2))` | $\frac{x^{2}}{\sqrt{1 - x^{2}} \sqrt{2 - 3 x^{2}}}$ |
| partial | concrete | `x**2/(sqrt(4 - x**2)*sqrt(3*x**2 + 2))` | $\frac{x^{2}}{\sqrt{4 - x^{2}} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `x**2/(sqrt(2 - 3*x**2)*sqrt(4 - x**2))` | $\frac{x^{2}}{\sqrt{2 - 3 x^{2}} \sqrt{4 - x^{2}}}$ |
| partial | concrete | `x**2/(sqrt(1 - 4*x**2)*sqrt(3*x**2 + 2))` | $\frac{x^{2}}{\sqrt{1 - 4 x^{2}} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `x**2/(sqrt(1 - 4*x**2)*sqrt(2 - 3*x**2))` | $\frac{x^{2}}{\sqrt{1 - 4 x^{2}} \sqrt{2 - 3 x^{2}}}$ |
| partial | concrete | `x**2/(sqrt(2 - 3*x**2)*sqrt(x**2 + 1))` | $\frac{x^{2}}{\sqrt{2 - 3 x^{2}} \sqrt{x^{2} + 1}}$ |
| partial | concrete | `x**2/(sqrt(2 - 3*x**2)*sqrt(x**2 + 4))` | $\frac{x^{2}}{\sqrt{2 - 3 x^{2}} \sqrt{x^{2} + 4}}$ |
| partial | concrete | `x**2/(sqrt(2 - 3*x**2)*sqrt(4*x**2 + 1))` | $\frac{x^{2}}{\sqrt{2 - 3 x^{2}} \sqrt{4 x^{2} + 1}}$ |
| partial | concrete | `x**2/(sqrt(x**2 + 1)*sqrt(3*x**2 + 2))` | $\frac{x^{2}}{\sqrt{x^{2} + 1} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `x**2/(sqrt(x**2 + 4)*sqrt(3*x**2 + 2))` | $\frac{x^{2}}{\sqrt{x^{2} + 4} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `x**2/(sqrt(3*x**2 + 2)*sqrt(4*x**2 + 1))` | $\frac{x^{2}}{\sqrt{3 x^{2} + 2} \sqrt{4 x^{2} + 1}}$ |
| partial | concrete | `x**2/(sqrt(1 - x**2)*sqrt(2*x**2 - 1))` | $\frac{x^{2}}{\sqrt{1 - x^{2}} \sqrt{2 x^{2} - 1}}$ |
| partial | concrete | `x**5/((1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{x^{5}}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `x**3/((1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{x^{3}}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `x/((1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{x}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `1/(x*(1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{1}{x \sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `1/(x**3*(1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{1}{x^{3} \sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `1/(x**5*(1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{1}{x^{5} \sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `x**4/((1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{x^{4}}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `x**2/((1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{x^{2}}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `1/((1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{1}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `1/(x**2*(1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{1}{x^{2} \sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `1/(x**4*(1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{1}{x^{4} \sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `x**7/((1 - x**2)**(1/3)*(x**2 + 3)**2)` | $\frac{x^{7}}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)^{2}}$ |
| partial | concrete | `x**5/((1 - x**2)**(1/3)*(x**2 + 3)**2)` | $\frac{x^{5}}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)^{2}}$ |
| partial | concrete | `x**3/((1 - x**2)**(1/3)*(x**2 + 3)**2)` | $\frac{x^{3}}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)^{2}}$ |
| partial | concrete | `x/((1 - x**2)**(1/3)*(x**2 + 3)**2)` | $\frac{x}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)^{2}}$ |
| partial | concrete | `1/(x*(1 - x**2)**(1/3)*(x**2 + 3)**2)` | $\frac{1}{x \sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)^{2}}$ |
| partial | concrete | `1/(x**3*(1 - x**2)**(1/3)*(x**2 + 3)**2)` | $\frac{1}{x^{3} \sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)^{2}}$ |
| partial | concrete | `1/(x**5*(1 - x**2)**(1/3)*(x**2 + 3)**2)` | $\frac{1}{x^{5} \sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)^{2}}$ |
| partial | concrete | `x**4/((1 - x**2)**(1/3)*(x**2 + 3)**2)` | $\frac{x^{4}}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)^{2}}$ |
| partial | concrete | `x**2/((1 - x**2)**(1/3)*(x**2 + 3)**2)` | $\frac{x^{2}}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)^{2}}$ |
| partial | concrete | `1/((1 - x**2)**(1/3)*(x**2 + 3)**2)` | $\frac{1}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)^{2}}$ |
| partial | concrete | `1/(x**2*(1 - x**2)**(1/3)*(x**2 + 3)**2)` | $\frac{1}{x^{2} \sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)^{2}}$ |
| partial | concrete | `1/(x**4*(1 - x**2)**(1/3)*(x**2 + 3)**2)` | $\frac{1}{x^{4} \sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)^{2}}$ |
| partial | concrete | `x**7/((2 - 3*x**2)**(1/4)*(4 - 3*x**2))` | $\frac{x^{7}}{\sqrt[4]{2 - 3 x^{2}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x**5/((2 - 3*x**2)**(1/4)*(4 - 3*x**2))` | $\frac{x^{5}}{\sqrt[4]{2 - 3 x^{2}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x**3/((2 - 3*x**2)**(1/4)*(4 - 3*x**2))` | $\frac{x^{3}}{\sqrt[4]{2 - 3 x^{2}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x/((2 - 3*x**2)**(1/4)*(4 - 3*x**2))` | $\frac{x}{\sqrt[4]{2 - 3 x^{2}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `1/(x*(2 - 3*x**2)**(1/4)*(4 - 3*x**2))` | $\frac{1}{x \sqrt[4]{2 - 3 x^{2}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `1/(x**3*(2 - 3*x**2)**(1/4)*(4 - 3*x**2))` | $\frac{1}{x^{3} \sqrt[4]{2 - 3 x^{2}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x**4/((2 - 3*x**2)**(1/4)*(4 - 3*x**2))` | $\frac{x^{4}}{\sqrt[4]{2 - 3 x^{2}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x**2/((2 - 3*x**2)**(1/4)*(4 - 3*x**2))` | $\frac{x^{2}}{\sqrt[4]{2 - 3 x^{2}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `1/((2 - 3*x**2)**(1/4)*(4 - 3*x**2))` | $\frac{1}{\sqrt[4]{2 - 3 x^{2}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `1/(x**2*(2 - 3*x**2)**(1/4)*(4 - 3*x**2))` | $\frac{1}{x^{2} \sqrt[4]{2 - 3 x^{2}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `1/(x**4*(2 - 3*x**2)**(1/4)*(4 - 3*x**2))` | $\frac{1}{x^{4} \sqrt[4]{2 - 3 x^{2}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x**7/((3*x**2 - 2)*(3*x**2 - 1)**(1/4))` | $\frac{x^{7}}{\left(3 x^{2} - 2\right) \sqrt[4]{3 x^{2} - 1}}$ |
| partial | concrete | `x**5/((3*x**2 - 2)*(3*x**2 - 1)**(1/4))` | $\frac{x^{5}}{\left(3 x^{2} - 2\right) \sqrt[4]{3 x^{2} - 1}}$ |
| partial | concrete | `x**3/((3*x**2 - 2)*(3*x**2 - 1)**(1/4))` | $\frac{x^{3}}{\left(3 x^{2} - 2\right) \sqrt[4]{3 x^{2} - 1}}$ |
| partial | concrete | `x/((3*x**2 - 2)*(3*x**2 - 1)**(1/4))` | $\frac{x}{\left(3 x^{2} - 2\right) \sqrt[4]{3 x^{2} - 1}}$ |
| partial | concrete | `1/(x*(3*x**2 - 2)*(3*x**2 - 1)**(1/4))` | $\frac{1}{x \left(3 x^{2} - 2\right) \sqrt[4]{3 x^{2} - 1}}$ |
| partial | concrete | `1/(x**3*(3*x**2 - 2)*(3*x**2 - 1)**(1/4))` | $\frac{1}{x^{3} \left(3 x^{2} - 2\right) \sqrt[4]{3 x^{2} - 1}}$ |
| partial | concrete | `x**4/((3*x**2 - 2)*(3*x**2 - 1)**(1/4))` | $\frac{x^{4}}{\left(3 x^{2} - 2\right) \sqrt[4]{3 x^{2} - 1}}$ |
| partial | concrete | `x**2/((3*x**2 - 2)*(3*x**2 - 1)**(1/4))` | $\frac{x^{2}}{\left(3 x^{2} - 2\right) \sqrt[4]{3 x^{2} - 1}}$ |
| partial | concrete | `1/((3*x**2 - 2)*(3*x**2 - 1)**(1/4))` | $\frac{1}{\left(3 x^{2} - 2\right) \sqrt[4]{3 x^{2} - 1}}$ |
| partial | concrete | `1/(x**2*(3*x**2 - 2)*(3*x**2 - 1)**(1/4))` | $\frac{1}{x^{2} \left(3 x^{2} - 2\right) \sqrt[4]{3 x^{2} - 1}}$ |
| partial | concrete | `1/(x**4*(3*x**2 - 2)*(3*x**2 - 1)**(1/4))` | $\frac{1}{x^{4} \left(3 x^{2} - 2\right) \sqrt[4]{3 x^{2} - 1}}$ |
| partial | concrete | `x**2/((3*x**2 + 2)**(3/4)*(3*x**2 + 4))` | $\frac{x^{2}}{\left(3 x^{2} + 2\right)^{\frac{3}{4}} \left(3 x^{2} + 4\right)}$ |
| partial | concrete | `x**2/((2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{x^{2}}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | parametric | `x**2/((b*x**2 + 2)**(3/4)*(b*x**2 + 4))` | $\frac{x^{2}}{\left(b x^{2} + 2\right)^{\frac{3}{4}} \left(b x^{2} + 4\right)}$ |
| partial | parametric | `x**2/((-b*x**2 + 2)**(3/4)*(-b*x**2 + 4))` | $\frac{x^{2}}{\left(- b x^{2} + 2\right)^{\frac{3}{4}} \left(- b x^{2} + 4\right)}$ |
| partial | parametric | `x**2/((a + 3*x**2)**(3/4)*(2*a + 3*x**2))` | $\frac{x^{2}}{\left(a + 3 x^{2}\right)^{\frac{3}{4}} \left(2 a + 3 x^{2}\right)}$ |
| partial | parametric | `x**2/((a - 3*x**2)**(3/4)*(2*a - 3*x**2))` | $\frac{x^{2}}{\left(a - 3 x^{2}\right)^{\frac{3}{4}} \left(2 a - 3 x^{2}\right)}$ |
| partial | parametric | `x**2/((a + b*x**2)**(3/4)*(2*a + b*x**2))` | $\frac{x^{2}}{\left(a + b x^{2}\right)^{\frac{3}{4}} \left(2 a + b x^{2}\right)}$ |
| partial | parametric | `x**2/((a - b*x**2)**(3/4)*(2*a - b*x**2))` | $\frac{x^{2}}{\left(a - b x^{2}\right)^{\frac{3}{4}} \left(2 a - b x^{2}\right)}$ |
| partial | concrete | `x**7/((2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{x^{7}}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x**5/((2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{x^{5}}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x**3/((2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{x^{3}}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x/((2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{x}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `1/(x*(2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{1}{x \left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `1/(x**3*(2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{1}{x^{3} \left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x**6/((2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{x^{6}}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x**4/((2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{x^{4}}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x**2/((2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{x^{2}}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `1/((2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{1}{\left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `1/(x**2*(2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{1}{x^{2} \left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `1/(x**4*(2 - 3*x**2)**(3/4)*(4 - 3*x**2))` | $\frac{1}{x^{4} \left(2 - 3 x^{2}\right)^{\frac{3}{4}} \left(4 - 3 x^{2}\right)}$ |
| partial | concrete | `x**2/((3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{x^{2}}{\left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**2/((-3*x**2 - 2)*(-3*x**2 - 1)**(3/4))` | $\frac{x^{2}}{\left(- 3 x^{2} - 2\right) \left(- 3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**2/((b*x**2 - 2)*(b*x**2 - 1)**(3/4))` | $\frac{x^{2}}{\left(b x^{2} - 2\right) \left(b x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**2/((-b*x**2 - 2)*(-b*x**2 - 1)**(3/4))` | $\frac{x^{2}}{\left(- b x^{2} - 2\right) \left(- b x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**2/((-2*a + 3*x**2)*(-a + 3*x**2)**(3/4))` | $\frac{x^{2}}{\left(- 2 a + 3 x^{2}\right) \left(- a + 3 x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**2/((-2*a - 3*x**2)*(-a - 3*x**2)**(3/4))` | $\frac{x^{2}}{\left(- 2 a - 3 x^{2}\right) \left(- a - 3 x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**2/((-2*a + b*x**2)*(-a + b*x**2)**(3/4))` | $\frac{x^{2}}{\left(- 2 a + b x^{2}\right) \left(- a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**2/((-2*a - b*x**2)*(-a - b*x**2)**(3/4))` | $\frac{x^{2}}{\left(- 2 a - b x^{2}\right) \left(- a - b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**7/((3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{x^{7}}{\left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**5/((3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{x^{5}}{\left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**3/((3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{x^{3}}{\left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x/((3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{x}{\left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x*(3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{1}{x \left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**3*(3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{1}{x^{3} \left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**6/((3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{x^{6}}{\left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**4/((3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{x^{4}}{\left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `x**2/((3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{x^{2}}{\left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/((3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{1}{\left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**2*(3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{1}{x^{2} \left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/(x**4*(3*x**2 - 2)*(3*x**2 - 1)**(3/4))` | $\frac{1}{x^{4} \left(3 x^{2} - 2\right) \left(3 x^{2} - 1\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(e*x)**(5/2)*(c + d*x**2)/(a + b*x**2)**(3/4)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `sqrt(e*x)*(c + d*x**2)/(a + b*x**2)**(3/4)` | $\frac{\sqrt{e x} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(c + d*x**2)/((e*x)**(3/2)*(a + b*x**2)**(3/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/((e*x)**(7/2)*(a + b*x**2)**(3/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{7}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/((e*x)**(11/2)*(a + b*x**2)**(3/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{11}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/((e*x)**(15/2)*(a + b*x**2)**(3/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{15}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(e*x)**(7/2)*(c + d*x**2)/(a + b*x**2)**(3/4)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(e*x)**(3/2)*(c + d*x**2)/(a + b*x**2)**(3/4)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(c + d*x**2)/(sqrt(e*x)*(a + b*x**2)**(3/4))` | $\frac{c + d x^{2}}{\sqrt{e x} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(c + d*x**2)/((e*x)**(5/2)*(a + b*x**2)**(3/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(c + d*x**2)/((e*x)**(9/2)*(a + b*x**2)**(3/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{9}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(c + d*x**2)/((e*x)**(13/2)*(a + b*x**2)**(3/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{13}{2}} \left(a + b x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(e*x)**(3/2)*(c + d*x**2)/(a + b*x**2)**(5/4)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(c + d*x**2)/(sqrt(e*x)*(a + b*x**2)**(5/4))` | $\frac{c + d x^{2}}{\sqrt{e x} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/((e*x)**(5/2)*(a + b*x**2)**(5/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/((e*x)**(9/2)*(a + b*x**2)**(5/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{9}{2}} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/((e*x)**(13/2)*(a + b*x**2)**(5/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{13}{2}} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(e*x)**(9/2)*(c + d*x**2)/(a + b*x**2)**(5/4)` | $\frac{\left(e x\right)^{\frac{9}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(e*x)**(5/2)*(c + d*x**2)/(a + b*x**2)**(5/4)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `sqrt(e*x)*(c + d*x**2)/(a + b*x**2)**(5/4)` | $\frac{\sqrt{e x} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(c + d*x**2)/((e*x)**(3/2)*(a + b*x**2)**(5/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(c + d*x**2)/((e*x)**(7/2)*(a + b*x**2)**(5/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{7}{2}} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(c + d*x**2)/((e*x)**(11/2)*(a + b*x**2)**(5/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{11}{2}} \left(a + b x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(e*x)**(5/2)*(c + d*x**2)/(a + b*x**2)**(7/4)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `sqrt(e*x)*(c + d*x**2)/(a + b*x**2)**(7/4)` | $\frac{\sqrt{e x} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/((e*x)**(3/2)*(a + b*x**2)**(7/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/((e*x)**(7/2)*(a + b*x**2)**(7/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{7}{2}} \left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/((e*x)**(11/2)*(a + b*x**2)**(7/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{11}{2}} \left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(e*x)**(7/2)*(c + d*x**2)/(a + b*x**2)**(7/4)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(e*x)**(3/2)*(c + d*x**2)/(a + b*x**2)**(7/4)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(c + d*x**2)/(sqrt(e*x)*(a + b*x**2)**(7/4))` | $\frac{c + d x^{2}}{\sqrt{e x} \left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(c + d*x**2)/((e*x)**(5/2)*(a + b*x**2)**(7/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(c + d*x**2)/((e*x)**(9/2)*(a + b*x**2)**(7/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{9}{2}} \left(a + b x^{2}\right)^{\frac{7}{4}}}$ |
| partial | parametric | `(e*x)**(7/2)*(c + d*x**2)/(a + b*x**2)**(9/4)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(e*x)**(3/2)*(c + d*x**2)/(a + b*x**2)**(9/4)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/(sqrt(e*x)*(a + b*x**2)**(9/4))` | $\frac{c + d x^{2}}{\sqrt{e x} \left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/((e*x)**(5/2)*(a + b*x**2)**(9/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{5}{2}} \left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/((e*x)**(9/2)*(a + b*x**2)**(9/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{9}{2}} \left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| **SOLVED-NEW** | parametric | `(c + d*x**2)/((e*x)**(13/2)*(a + b*x**2)**(9/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{13}{2}} \left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(e*x)**(13/2)*(c + d*x**2)/(a + b*x**2)**(9/4)` | $\frac{\left(e x\right)^{\frac{13}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(e*x)**(9/2)*(c + d*x**2)/(a + b*x**2)**(9/4)` | $\frac{\left(e x\right)^{\frac{9}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(e*x)**(5/2)*(c + d*x**2)/(a + b*x**2)**(9/4)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `sqrt(e*x)*(c + d*x**2)/(a + b*x**2)**(9/4)` | $\frac{\sqrt{e x} \left(c + d x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(c + d*x**2)/((e*x)**(3/2)*(a + b*x**2)**(9/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{3}{2}} \left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(c + d*x**2)/((e*x)**(7/2)*(a + b*x**2)**(9/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{7}{2}} \left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(c + d*x**2)/((e*x)**(11/2)*(a + b*x**2)**(9/4))` | $\frac{c + d x^{2}}{\left(e x\right)^{\frac{11}{2}} \left(a + b x^{2}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(a + b*x**2)*(c + d*x**2)**(3/2)*sqrt(e + f*x**2)` | $\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}} \sqrt{e + f x^{2}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(c + d*x**2)*sqrt(e + f*x**2)` | $\left(a + b x^{2}\right) \sqrt{c + d x^{2}} \sqrt{e + f x^{2}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(e + f*x**2)/sqrt(c + d*x**2)` | $\frac{\left(a + b x^{2}\right) \sqrt{e + f x^{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(e + f*x**2)/(c + d*x**2)**(3/2)` | $\frac{\left(a + b x^{2}\right) \sqrt{e + f x^{2}}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(e + f*x**2)/(c + d*x**2)**(5/2)` | $\frac{\left(a + b x^{2}\right) \sqrt{e + f x^{2}}}{\left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(e + f*x**2)/(c + d*x**2)**(7/2)` | $\frac{\left(a + b x^{2}\right) \sqrt{e + f x^{2}}}{\left(c + d x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(c + d*x**2)*(e + f*x**2)**(3/2)` | $\left(a + b x^{2}\right) \sqrt{c + d x^{2}} \left(e + f x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2)*(e + f*x**2)**(3/2)/sqrt(c + d*x**2)` | $\frac{\left(a + b x^{2}\right) \left(e + f x^{2}\right)^{\frac{3}{2}}}{\sqrt{c + d x^{2}}}$ |
| partial | parametric | `(a + b*x**2)*(e + f*x**2)**(3/2)/(c + d*x**2)**(3/2)` | $\frac{\left(a + b x^{2}\right) \left(e + f x^{2}\right)^{\frac{3}{2}}}{\left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)*(e + f*x**2)**(3/2)/(c + d*x**2)**(5/2)` | $\frac{\left(a + b x^{2}\right) \left(e + f x^{2}\right)^{\frac{3}{2}}}{\left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**2)*(e + f*x**2)**(3/2)/(c + d*x**2)**(7/2)` | $\frac{\left(a + b x^{2}\right) \left(e + f x^{2}\right)^{\frac{3}{2}}}{\left(c + d x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x**2)*(e + f*x**2)**(3/2)/(c + d*x**2)**(9/2)` | $\frac{\left(a + b x^{2}\right) \left(e + f x^{2}\right)^{\frac{3}{2}}}{\left(c + d x^{2}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x**2)*(c + d*x**2)**(5/2)/sqrt(e + f*x**2)` | $\frac{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}{\sqrt{e + f x^{2}}}$ |
| partial | parametric | `(a + b*x**2)*(c + d*x**2)**(3/2)/sqrt(e + f*x**2)` | $\frac{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}{\sqrt{e + f x^{2}}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(c + d*x**2)/sqrt(e + f*x**2)` | $\frac{\left(a + b x^{2}\right) \sqrt{c + d x^{2}}}{\sqrt{e + f x^{2}}}$ |
| partial | parametric | `(a + b*x**2)/(sqrt(c + d*x**2)*sqrt(e + f*x**2))` | $\frac{a + b x^{2}}{\sqrt{c + d x^{2}} \sqrt{e + f x^{2}}}$ |
| partial | parametric | `(a + b*x**2)/((c + d*x**2)**(3/2)*sqrt(e + f*x**2))` | $\frac{a + b x^{2}}{\left(c + d x^{2}\right)^{\frac{3}{2}} \sqrt{e + f x^{2}}}$ |
| partial | parametric | `(a + b*x**2)/((c + d*x**2)**(5/2)*sqrt(e + f*x**2))` | $\frac{a + b x^{2}}{\left(c + d x^{2}\right)^{\frac{5}{2}} \sqrt{e + f x^{2}}}$ |
| partial | parametric | `(a + b*x**2)/((c + d*x**2)**(7/2)*sqrt(e + f*x**2))` | $\frac{a + b x^{2}}{\left(c + d x^{2}\right)^{\frac{7}{2}} \sqrt{e + f x^{2}}}$ |
| partial | parametric | `(a + b*x**2)*(c + d*x**2)**(5/2)/(e + f*x**2)**(3/2)` | $\frac{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}{\left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)*(c + d*x**2)**(3/2)/(e + f*x**2)**(3/2)` | $\frac{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(c + d*x**2)/(e + f*x**2)**(3/2)` | $\frac{\left(a + b x^{2}\right) \sqrt{c + d x^{2}}}{\left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)/(sqrt(c + d*x**2)*(e + f*x**2)**(3/2))` | $\frac{a + b x^{2}}{\sqrt{c + d x^{2}} \left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)/((c + d*x**2)**(3/2)*(e + f*x**2)**(3/2))` | $\frac{a + b x^{2}}{\left(c + d x^{2}\right)^{\frac{3}{2}} \left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)/((c + d*x**2)**(5/2)*(e + f*x**2)**(3/2))` | $\frac{a + b x^{2}}{\left(c + d x^{2}\right)^{\frac{5}{2}} \left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e + f*x**2)/(sqrt(a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{e + f x^{2}}{\sqrt{a + b x^{2}} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e + f*x**2)/(sqrt(a - b*x**2)*(c + d*x**2)**(3/2))` | $\frac{e + f x^{2}}{\sqrt{a - b x^{2}} \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e + f*x**2)/(sqrt(a + b*x**2)*(c - d*x**2)**(3/2))` | $\frac{e + f x^{2}}{\sqrt{a + b x^{2}} \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e + f*x**2)/(sqrt(a - b*x**2)*(c - d*x**2)**(3/2))` | $\frac{e + f x^{2}}{\sqrt{a - b x^{2}} \left(c - d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)/(sqrt(d*x**2 + 2)*sqrt(f*x**2 + 3))` | $\frac{a + b x^{2}}{\sqrt{d x^{2} + 2} \sqrt{f x^{2} + 3}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(d*x**2 + 2)/sqrt(f*x**2 + 3)` | $\frac{\left(a + b x^{2}\right) \sqrt{d x^{2} + 2}}{\sqrt{f x^{2} + 3}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(d*x**2 + 2)*sqrt(f*x**2 + 3)` | $\left(a + b x^{2}\right) \sqrt{d x^{2} + 2} \sqrt{f x^{2} + 3}$ |
| timeout | parametric | `(-b + 2*c*x**2 - sqrt(-4*a*c + b**2))/(sqrt(2*c*x**2/(-b - sqrt(-4*a*c + b**2)) + 1)*sqrt(2*c*x**2/(-b + sqrt(-4*a*c + b**2)) + 1))` | $\frac{- b + 2 c x^{2} - \sqrt{- 4 a c + b^{2}}}{\sqrt{\frac{2 c x^{2}}{- b - \sqrt{- 4 a c + b^{2}}} + 1} \sqrt{\frac{2 c x^{2}}{- b + \sqrt{- 4 a c + b^{2}}} + 1}}$ |
| timeout | parametric | `(b + 2*c*x**2 - sqrt(-4*a*c + b**2))/(sqrt(2*c*x**2/(b - sqrt(-4*a*c + b**2)) + 1)*sqrt(2*c*x**2/(b + sqrt(-4*a*c + b**2)) + 1))` | $\frac{b + 2 c x^{2} - \sqrt{- 4 a c + b^{2}}}{\sqrt{\frac{2 c x^{2}}{b - \sqrt{- 4 a c + b^{2}}} + 1} \sqrt{\frac{2 c x^{2}}{b + \sqrt{- 4 a c + b^{2}}} + 1}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(c + d*x**2)/(e + f*x**2)` | $\frac{\left(a + b x^{2}\right) \sqrt{c + d x^{2}}}{e + f x^{2}}$ |
| partial | parametric | `(a + b*x**2)**3/((c + d*x**2)*sqrt(e + f*x**2))` | $\frac{\left(a + b x^{2}\right)^{3}}{\left(c + d x^{2}\right) \sqrt{e + f x^{2}}}$ |
| partial | parametric | `(a + b*x**2)**2/((c + d*x**2)*sqrt(e + f*x**2))` | $\frac{\left(a + b x^{2}\right)^{2}}{\left(c + d x^{2}\right) \sqrt{e + f x^{2}}}$ |
| partial | parametric | `(a + b*x**2)/((c + d*x**2)*sqrt(e + f*x**2))` | $\frac{a + b x^{2}}{\left(c + d x^{2}\right) \sqrt{e + f x^{2}}}$ |
| partial | parametric | `1/((c + d*x**2)*sqrt(e + f*x**2))` | $\frac{1}{\left(c + d x^{2}\right) \sqrt{e + f x^{2}}}$ |
| partial | parametric | `1/((a + b*x**2)*(c + d*x**2)*sqrt(e + f*x**2))` | $\frac{1}{\left(a + b x^{2}\right) \left(c + d x^{2}\right) \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `1/((a + b*x**2)**2*(c + d*x**2)*sqrt(e + f*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{2} \left(c + d x^{2}\right) \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `(c + d*x**2)**(3/2)*sqrt(e + f*x**2)/(a + b*x**2)` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}} \sqrt{e + f x^{2}}}{a + b x^{2}}$ |
| timeout | parametric | `sqrt(c + d*x**2)*sqrt(e + f*x**2)/(a + b*x**2)` | $\frac{\sqrt{c + d x^{2}} \sqrt{e + f x^{2}}}{a + b x^{2}}$ |
| timeout | parametric | `sqrt(e + f*x**2)/((a + b*x**2)*sqrt(c + d*x**2))` | $\frac{\sqrt{e + f x^{2}}}{\left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| timeout | parametric | `sqrt(e + f*x**2)/((a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{\sqrt{e + f x^{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(e + f*x**2)/((a + b*x**2)*(c + d*x**2)**(5/2))` | $\frac{\sqrt{e + f x^{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `sqrt(e + f*x**2)/((a + b*x**2)*(c + d*x**2)**(7/2))` | $\frac{\sqrt{e + f x^{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{7}{2}}}$ |
| timeout | parametric | `sqrt(c + d*x**2)*(e + f*x**2)**(3/2)/(a + b*x**2)` | $\frac{\sqrt{c + d x^{2}} \left(e + f x^{2}\right)^{\frac{3}{2}}}{a + b x^{2}}$ |
| timeout | parametric | `(e + f*x**2)**(3/2)/((a + b*x**2)*sqrt(c + d*x**2))` | $\frac{\left(e + f x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right) \sqrt{c + d x^{2}}}$ |
| timeout | parametric | `(e + f*x**2)**(3/2)/((a + b*x**2)*(c + d*x**2)**(3/2))` | $\frac{\left(e + f x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(e + f*x**2)**(3/2)/((a + b*x**2)*(c + d*x**2)**(5/2))` | $\frac{\left(e + f x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(e + f*x**2)**(3/2)/((a + b*x**2)*(c + d*x**2)**(7/2))` | $\frac{\left(e + f x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{7}{2}}}$ |
| timeout | parametric | `(c + d*x**2)**(5/2)/((a + b*x**2)*sqrt(e + f*x**2))` | $\frac{\left(c + d x^{2}\right)^{\frac{5}{2}}}{\left(a + b x^{2}\right) \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `(c + d*x**2)**(3/2)/((a + b*x**2)*sqrt(e + f*x**2))` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right) \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `sqrt(c + d*x**2)/((a + b*x**2)*sqrt(e + f*x**2))` | $\frac{\sqrt{c + d x^{2}}}{\left(a + b x^{2}\right) \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `1/((a + b*x**2)*sqrt(c + d*x**2)*sqrt(e + f*x**2))` | $\frac{1}{\left(a + b x^{2}\right) \sqrt{c + d x^{2}} \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `1/((a + b*x**2)*(c + d*x**2)**(3/2)*sqrt(e + f*x**2))` | $\frac{1}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}} \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `1/((a + b*x**2)*(c + d*x**2)**(5/2)*sqrt(e + f*x**2))` | $\frac{1}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}} \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `(c + d*x**2)**(5/2)/((a + b*x**2)*(e + f*x**2)**(3/2))` | $\frac{\left(c + d x^{2}\right)^{\frac{5}{2}}}{\left(a + b x^{2}\right) \left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(c + d*x**2)**(3/2)/((a + b*x**2)*(e + f*x**2)**(3/2))` | $\frac{\left(c + d x^{2}\right)^{\frac{3}{2}}}{\left(a + b x^{2}\right) \left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(c + d*x**2)/((a + b*x**2)*(e + f*x**2)**(3/2))` | $\frac{\sqrt{c + d x^{2}}}{\left(a + b x^{2}\right) \left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/((a + b*x**2)*sqrt(c + d*x**2)*(e + f*x**2)**(3/2))` | $\frac{1}{\left(a + b x^{2}\right) \sqrt{c + d x^{2}} \left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/((a + b*x**2)*(c + d*x**2)**(3/2)*(e + f*x**2)**(3/2))` | $\frac{1}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{3}{2}} \left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/((a + b*x**2)*(c + d*x**2)**(5/2)*(e + f*x**2)**(3/2))` | $\frac{1}{\left(a + b x^{2}\right) \left(c + d x^{2}\right)^{\frac{5}{2}} \left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x**2 + 1)*sqrt(x**2 + 2)/(a + b*x**2)` | $\frac{\sqrt{x^{2} + 1} \sqrt{x^{2} + 2}}{a + b x^{2}}$ |
| partial | parametric | `sqrt(x**2 + 2)/((a + b*x**2)*sqrt(x**2 + 1))` | $\frac{\sqrt{x^{2} + 2}}{\left(a + b x^{2}\right) \sqrt{x^{2} + 1}}$ |
| partial | parametric | `sqrt(x**2 + 2)/((a + b*x**2)*(x**2 + 1)**(3/2))` | $\frac{\sqrt{x^{2} + 2}}{\left(a + b x^{2}\right) \left(x^{2} + 1\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(x**2 + 2)/((a + b*x**2)*(x**2 + 1)**(5/2))` | $\frac{\sqrt{x^{2} + 2}}{\left(a + b x^{2}\right) \left(x^{2} + 1\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `sqrt(d*x**2 + 2)*sqrt(f*x**2 + 3)/(a + b*x**2)` | $\frac{\sqrt{d x^{2} + 2} \sqrt{f x^{2} + 3}}{a + b x^{2}}$ |
| timeout | parametric | `sqrt(d*x**2 + 2)/((a + b*x**2)*sqrt(f*x**2 + 3))` | $\frac{\sqrt{d x^{2} + 2}}{\left(a + b x^{2}\right) \sqrt{f x^{2} + 3}}$ |
| timeout | parametric | `1/((a + b*x**2)*sqrt(d*x**2 + 2)*sqrt(f*x**2 + 3))` | $\frac{1}{\left(a + b x^{2}\right) \sqrt{d x^{2} + 2} \sqrt{f x^{2} + 3}}$ |
| partial | parametric | `sqrt(1 - x**2)/(sqrt(a + b*x**2)*(x**2 - 1))` | $\frac{\sqrt{1 - x^{2}}}{\sqrt{a + b x^{2}} \left(x^{2} - 1\right)}$ |
| partial | parametric | `(a + b*x**2)/(sqrt(c + d*x**2)*(e + f*x**2)**2)` | $\frac{a + b x^{2}}{\sqrt{c + d x^{2}} \left(e + f x^{2}\right)^{2}}$ |
| timeout | parametric | `sqrt(c - d*x**2)*sqrt(e + f*x**2)/(a + b*x**2)**2` | $\frac{\sqrt{c - d x^{2}} \sqrt{e + f x^{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| timeout | parametric | `sqrt(c + d*x**2)*sqrt(e + f*x**2)/(a + b*x**2)**2` | $\frac{\sqrt{c + d x^{2}} \sqrt{e + f x^{2}}}{\left(a + b x^{2}\right)^{2}}$ |
| timeout | parametric | `1/((a + b*x**2)**2*sqrt(c - d*x**2)*sqrt(e + f*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{2} \sqrt{c - d x^{2}} \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `1/((a + b*x**2)**2*sqrt(c + d*x**2)*sqrt(e + f*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{2} \sqrt{c + d x^{2}} \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `(a + b*x**2)**(3/2)*sqrt(c + d*x**2)/sqrt(e + f*x**2)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}} \sqrt{c + d x^{2}}}{\sqrt{e + f x^{2}}}$ |
| timeout | parametric | `sqrt(a + b*x**2)*sqrt(c + d*x**2)/sqrt(e + f*x**2)` | $\frac{\sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}{\sqrt{e + f x^{2}}}$ |
| timeout | parametric | `sqrt(c + d*x**2)/(sqrt(a + b*x**2)*sqrt(e + f*x**2))` | $\frac{\sqrt{c + d x^{2}}}{\sqrt{a + b x^{2}} \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `sqrt(c + d*x**2)/((a + b*x**2)**(3/2)*sqrt(e + f*x**2))` | $\frac{\sqrt{c + d x^{2}}}{\left(a + b x^{2}\right)^{\frac{3}{2}} \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `(a + b*x**2)**(3/2)*sqrt(c + d*x**2)/(e + f*x**2)**(3/2)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}} \sqrt{c + d x^{2}}}{\left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(a + b*x**2)*sqrt(c + d*x**2)/(e + f*x**2)**(3/2)` | $\frac{\sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}{\left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(c + d*x**2)/(sqrt(a + b*x**2)*(e + f*x**2)**(3/2))` | $\frac{\sqrt{c + d x^{2}}}{\sqrt{a + b x^{2}} \left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(c + d*x**2)/((a + b*x**2)**(3/2)*(e + f*x**2)**(3/2))` | $\frac{\sqrt{c + d x^{2}}}{\left(a + b x^{2}\right)^{\frac{3}{2}} \left(e + f x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(c + d*x**2)*sqrt(e + f*x**2)/sqrt(a + b*x**2)` | $\frac{\sqrt{c + d x^{2}} \sqrt{e + f x^{2}}}{\sqrt{a + b x^{2}}}$ |
| timeout | parametric | `(a + b*x**2)**(3/2)/(sqrt(c + d*x**2)*sqrt(e + f*x**2))` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\sqrt{c + d x^{2}} \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `sqrt(a + b*x**2)/(sqrt(c + d*x**2)*sqrt(e + f*x**2))` | $\frac{\sqrt{a + b x^{2}}}{\sqrt{c + d x^{2}} \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `1/(sqrt(a + b*x**2)*sqrt(c + d*x**2)*sqrt(e + f*x**2))` | $\frac{1}{\sqrt{a + b x^{2}} \sqrt{c + d x^{2}} \sqrt{e + f x^{2}}}$ |
| timeout | parametric | `1/((a + b*x**2)**(3/2)*sqrt(c + d*x**2)*sqrt(e + f*x**2))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{3}{2}} \sqrt{c + d x^{2}} \sqrt{e + f x^{2}}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(a + b*x**2)*(c + d*x**2)/x` | $\frac{\left(A + B x^{2}\right) \sqrt{a + b x^{2}} \left(c + d x^{2}\right)}{x}$ |
| partial | parametric | `(A + B*x**2)*(a + b*x**2)*sqrt(c + d*x**2)/x` | $\frac{\left(A + B x^{2}\right) \left(a + b x^{2}\right) \sqrt{c + d x^{2}}}{x}$ |
| partial | parametric | `x**3*(A + B*x)*sqrt(a + b*x**2)` | $x^{3} \left(A + B x\right) \sqrt{a + b x^{2}}$ |
| partial | parametric | `x**2*(A + B*x)*sqrt(a + b*x**2)` | $x^{2} \left(A + B x\right) \sqrt{a + b x^{2}}$ |
| partial | parametric | `x*(A + B*x)*sqrt(a + b*x**2)` | $x \left(A + B x\right) \sqrt{a + b x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x**2)` | $\left(A + B x\right) \sqrt{a + b x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x**2)/x` | $\frac{\left(A + B x\right) \sqrt{a + b x^{2}}}{x}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x**2)/x**2` | $\frac{\left(A + B x\right) \sqrt{a + b x^{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x**2)/x**3` | $\frac{\left(A + B x\right) \sqrt{a + b x^{2}}}{x^{3}}$ |
| partial | parametric | `x**3*(A + B*x)*(a + b*x**2)**(3/2)` | $x^{3} \left(A + B x\right) \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(A + B*x)*(a + b*x**2)**(3/2)` | $x^{2} \left(A + B x\right) \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(A + B*x)*(a + b*x**2)**(3/2)` | $x \left(A + B x\right) \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x**2)**(3/2)` | $\left(A + B x\right) \left(a + b x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x**2)**(3/2)/x` | $\frac{\left(A + B x\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(A + B*x)*(a + b*x**2)**(3/2)/x**2` | $\frac{\left(A + B x\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x**2)**(3/2)/x**3` | $\frac{\left(A + B x\right) \left(a + b x^{2}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `x**3*(A + B*x)*(a + b*x**2)**(5/2)` | $x^{3} \left(A + B x\right) \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**2*(A + B*x)*(a + b*x**2)**(5/2)` | $x^{2} \left(A + B x\right) \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x*(A + B*x)*(a + b*x**2)**(5/2)` | $x \left(A + B x\right) \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x**2)**(5/2)` | $\left(A + B x\right) \left(a + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x**2)**(5/2)/x` | $\frac{\left(A + B x\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(A + B*x)*(a + b*x**2)**(5/2)/x**2` | $\frac{\left(A + B x\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x**2)**(5/2)/x**3` | $\frac{\left(A + B x\right) \left(a + b x^{2}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `x**3*(A + B*x)/sqrt(a + b*x**2)` | $\frac{x^{3} \left(A + B x\right)}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**2*(A + B*x)/sqrt(a + b*x**2)` | $\frac{x^{2} \left(A + B x\right)}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `x*(A + B*x)/sqrt(a + b*x**2)` | $\frac{x \left(A + B x\right)}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x)/sqrt(a + b*x**2)` | $\frac{A + B x}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x*sqrt(a + b*x**2))` | $\frac{A + B x}{x \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*sqrt(a + b*x**2))` | $\frac{A + B x}{x^{2} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*sqrt(a + b*x**2))` | $\frac{A + B x}{x^{3} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**3*(A + B*x)/(a + b*x**2)**(3/2)` | $\frac{x^{3} \left(A + B x\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(A + B*x)/(a + b*x**2)**(3/2)` | $\frac{x^{2} \left(A + B x\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(A + B*x)/(a + b*x**2)**(3/2)` | $\frac{x \left(A + B x\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a + b*x**2)**(3/2)` | $\frac{A + B x}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x*(a + b*x**2)**(3/2))` | $\frac{A + B x}{x \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*(a + b*x**2)**(3/2))` | $\frac{A + B x}{x^{2} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*(a + b*x**2)**(3/2))` | $\frac{A + B x}{x^{3} \left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*(A + B*x)/(a + b*x**2)**(5/2)` | $\frac{x^{3} \left(A + B x\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)/(a + b*x**2)**(5/2)` | $\frac{x^{2} \left(A + B x\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x)/(a + b*x**2)**(5/2)` | $\frac{x \left(A + B x\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a + b*x**2)**(5/2)` | $\frac{A + B x}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x*(a + b*x**2)**(5/2))` | $\frac{A + B x}{x \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*(a + b*x**2)**(5/2))` | $\frac{A + B x}{x^{2} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*(a + b*x**2)**(5/2))` | $\frac{A + B x}{x^{3} \left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x*(1 - x)/sqrt(1 - x**2)` | $\frac{x \left(1 - x\right)}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `(-x**2 + x)/sqrt(1 - x**2)` | $\frac{- x^{2} + x}{\sqrt{1 - x^{2}}}$ |
| partial | parametric | `x**7*(A + B*x + C*x**2)/(a + b*x**2)**(9/2)` | $\frac{x^{7} \left(A + B x + C x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `x**6*(A + B*x + C*x**2)/(a + b*x**2)**(9/2)` | $\frac{x^{6} \left(A + B x + C x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x + C*x**2)/(a + b*x**2)**(9/2)` | $\frac{x^{5} \left(A + B x + C x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x + C*x**2)/(a + b*x**2)**(9/2)` | $\frac{x^{4} \left(A + B x + C x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x + C*x**2)/(a + b*x**2)**(9/2)` | $\frac{x^{3} \left(A + B x + C x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x + C*x**2)/(a + b*x**2)**(9/2)` | $\frac{x^{2} \left(A + B x + C x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x + C*x**2)/(a + b*x**2)**(9/2)` | $\frac{x \left(A + B x + C x^{2}\right)}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x + C*x**2)/(a + b*x**2)**(9/2)` | $\frac{A + B x + C x^{2}}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)/(x*(a + b*x**2)**(9/2))` | $\frac{A + B x + C x^{2}}{x \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)/(x**2*(a + b*x**2)**(9/2))` | $\frac{A + B x + C x^{2}}{x^{2} \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)/(x**3*(a + b*x**2)**(9/2))` | $\frac{A + B x + C x^{2}}{x^{3} \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | concrete | `(x**3 - x)/sqrt(x**2 - 2)` | $\frac{x^{3} - x}{\sqrt{x^{2} - 2}}$ |
| SOLVED-both | parametric | `x**5*(c + d*x**2 + e*x**4 + f*x**6)/sqrt(a + b*x**2)` | $\frac{x^{5} \left(c + d x^{2} + e x^{4} + f x^{6}\right)}{\sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x**3*(c + d*x**2 + e*x**4 + f*x**6)/sqrt(a + b*x**2)` | $\frac{x^{3} \left(c + d x^{2} + e x^{4} + f x^{6}\right)}{\sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x*(c + d*x**2 + e*x**4 + f*x**6)/sqrt(a + b*x**2)` | $\frac{x \left(c + d x^{2} + e x^{4} + f x^{6}\right)}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c + d*x**2 + e*x**4 + f*x**6)/(x*sqrt(a + b*x**2))` | $\frac{c + d x^{2} + e x^{4} + f x^{6}}{x \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c + d*x**2 + e*x**4 + f*x**6)/(x**3*sqrt(a + b*x**2))` | $\frac{c + d x^{2} + e x^{4} + f x^{6}}{x^{3} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c + d*x**2 + e*x**4 + f*x**6)/(x**5*sqrt(a + b*x**2))` | $\frac{c + d x^{2} + e x^{4} + f x^{6}}{x^{5} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c + d*x**2 + e*x**4 + f*x**6)/(x**7*sqrt(a + b*x**2))` | $\frac{c + d x^{2} + e x^{4} + f x^{6}}{x^{7} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c + d*x**2 + e*x**4 + f*x**6)/(x**9*sqrt(a + b*x**2))` | $\frac{c + d x^{2} + e x^{4} + f x^{6}}{x^{9} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**4*(c + d*x**2 + e*x**4 + f*x**6)/sqrt(a + b*x**2)` | $\frac{x^{4} \left(c + d x^{2} + e x^{4} + f x^{6}\right)}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**2*(c + d*x**2 + e*x**4 + f*x**6)/sqrt(a + b*x**2)` | $\frac{x^{2} \left(c + d x^{2} + e x^{4} + f x^{6}\right)}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c + d*x**2 + e*x**4 + f*x**6)/sqrt(a + b*x**2)` | $\frac{c + d x^{2} + e x^{4} + f x^{6}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c + d*x**2 + e*x**4 + f*x**6)/(x**2*sqrt(a + b*x**2))` | $\frac{c + d x^{2} + e x^{4} + f x^{6}}{x^{2} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c + d*x**2 + e*x**4 + f*x**6)/(x**4*sqrt(a + b*x**2))` | $\frac{c + d x^{2} + e x^{4} + f x^{6}}{x^{4} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `(c + d*x**2 + e*x**4 + f*x**6)/(x**6*sqrt(a + b*x**2))` | $\frac{c + d x^{2} + e x^{4} + f x^{6}}{x^{6} \sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `(c + d*x**2 + e*x**4 + f*x**6)/(x**8*sqrt(a + b*x**2))` | $\frac{c + d x^{2} + e x^{4} + f x^{6}}{x^{8} \sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `(c + d*x**2 + e*x**4 + f*x**6)/(x**10*sqrt(a + b*x**2))` | $\frac{c + d x^{2} + e x^{4} + f x^{6}}{x^{10} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**8*(A + B*x**2 + C*x**4 + D*x**6)/(a + b*x**2)**(9/2)` | $\frac{x^{8} \left(A + B x^{2} + C x^{4} + D x^{6}\right)}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `x**6*(A + B*x**2 + C*x**4 + D*x**6)/(a + b*x**2)**(9/2)` | $\frac{x^{6} \left(A + B x^{2} + C x^{4} + D x^{6}\right)}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `x**4*(A + B*x**2 + C*x**4 + D*x**6)/(a + b*x**2)**(9/2)` | $\frac{x^{4} \left(A + B x^{2} + C x^{4} + D x^{6}\right)}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2 + C*x**4 + D*x**6)/(a + b*x**2)**(9/2)` | $\frac{A + B x^{2} + C x^{4} + D x^{6}}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2 + C*x**4 + D*x**6)/(x**2*(a + b*x**2)**(9/2))` | $\frac{A + B x^{2} + C x^{4} + D x^{6}}{x^{2} \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2 + C*x**4 + D*x**6)/(x**4*(a + b*x**2)**(9/2))` | $\frac{A + B x^{2} + C x^{4} + D x^{6}}{x^{4} \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2 + C*x**4 + D*x**6)/(x**6*(a + b*x**2)**(9/2))` | $\frac{A + B x^{2} + C x^{4} + D x^{6}}{x^{6} \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2 + C*x**4 + D*x**6)/(x**8*(a + b*x**2)**(9/2))` | $\frac{A + B x^{2} + C x^{4} + D x^{6}}{x^{8} \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2 + C*x**4 + D*x**6)/(x**10*(a + b*x**2)**(9/2))` | $\frac{A + B x^{2} + C x^{4} + D x^{6}}{x^{10} \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(c*x**5 + d*x**7 + e*x**9 + f*x**11)/sqrt(a + b*x**2)` | $\frac{c x^{5} + d x^{7} + e x^{9} + f x^{11}}{\sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `(c*x**3 + d*x**5 + e*x**7 + f*x**9)/sqrt(a + b*x**2)` | $\frac{c x^{3} + d x^{5} + e x^{7} + f x^{9}}{\sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `(c*x + d*x**3 + e*x**5 + f*x**7)/sqrt(a + b*x**2)` | $\frac{c x + d x^{3} + e x^{5} + f x^{7}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**2*(A + B*x**2 + C*x**4 + D*x**6 + F*x**8)/(a + b*x**2)**(9/2)` | $\frac{x^{2} \left(A + B x^{2} + C x^{4} + D x^{6} + F x^{8}\right)}{\left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2 + C*x**4 + D*x**6 + F*x**8)/(x**2*(a + b*x**2)**(9/2))` | $\frac{A + B x^{2} + C x^{4} + D x^{6} + F x^{8}}{x^{2} \left(a + b x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**3*sqrt(b*x**2)` | $x^{3} \sqrt{b x^{2}}$ |
| SOLVED-both | parametric | `x**2*sqrt(b*x**2)` | $x^{2} \sqrt{b x^{2}}$ |
| SOLVED-both | parametric | `x*sqrt(b*x**2)` | $x \sqrt{b x^{2}}$ |
| SOLVED-both | parametric | `sqrt(b*x**2)` | $\sqrt{b x^{2}}$ |
| SOLVED-both | parametric | `sqrt(b*x**2)/x` | $\frac{\sqrt{b x^{2}}}{x}$ |
| SOLVED-both | parametric | `sqrt(b*x**2)/x**2` | $\frac{\sqrt{b x^{2}}}{x^{2}}$ |
| SOLVED-both | parametric | `sqrt(b*x**2)/x**3` | $\frac{\sqrt{b x^{2}}}{x^{3}}$ |
| SOLVED-both | parametric | `sqrt(b*x**2)/x**4` | $\frac{\sqrt{b x^{2}}}{x^{4}}$ |
| SOLVED-both | parametric | `sqrt(b*x**2)/x**5` | $\frac{\sqrt{b x^{2}}}{x^{5}}$ |
| SOLVED-both | concrete | `x**2*sqrt(x**2)` | $x^{2} \sqrt{x^{2}}$ |
| SOLVED-both | parametric | `x**2*(b*x**2)**(3/2)` | $x^{2} \left(b x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x*(b*x**2)**(3/2)` | $x \left(b x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(b*x**2)**(3/2)` | $\left(b x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(b*x**2)**(3/2)/x` | $\frac{\left(b x^{2}\right)^{\frac{3}{2}}}{x}$ |
| SOLVED-both | parametric | `(b*x**2)**(3/2)/x**2` | $\frac{\left(b x^{2}\right)^{\frac{3}{2}}}{x^{2}}$ |
| SOLVED-both | parametric | `(b*x**2)**(3/2)/x**3` | $\frac{\left(b x^{2}\right)^{\frac{3}{2}}}{x^{3}}$ |
| SOLVED-both | parametric | `(b*x**2)**(3/2)/x**4` | $\frac{\left(b x^{2}\right)^{\frac{3}{2}}}{x^{4}}$ |
| SOLVED-both | parametric | `(b*x**2)**(3/2)/x**5` | $\frac{\left(b x^{2}\right)^{\frac{3}{2}}}{x^{5}}$ |
| SOLVED-both | parametric | `(b*x**2)**(3/2)/x**6` | $\frac{\left(b x^{2}\right)^{\frac{3}{2}}}{x^{6}}$ |
| SOLVED-both | parametric | `(b*x**2)**(3/2)/x**7` | $\frac{\left(b x^{2}\right)^{\frac{3}{2}}}{x^{7}}$ |
| SOLVED-both | concrete | `x**2*(x**2)**(3/2)` | $x^{2} \left(x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x*(b*x**2)**(5/2)` | $x \left(b x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(b*x**2)**(5/2)` | $\left(b x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(b*x**2)**(5/2)/x` | $\frac{\left(b x^{2}\right)^{\frac{5}{2}}}{x}$ |
| SOLVED-both | parametric | `(b*x**2)**(5/2)/x**2` | $\frac{\left(b x^{2}\right)^{\frac{5}{2}}}{x^{2}}$ |
| SOLVED-both | parametric | `(b*x**2)**(5/2)/x**3` | $\frac{\left(b x^{2}\right)^{\frac{5}{2}}}{x^{3}}$ |
| SOLVED-both | parametric | `(b*x**2)**(5/2)/x**4` | $\frac{\left(b x^{2}\right)^{\frac{5}{2}}}{x^{4}}$ |
| SOLVED-both | parametric | `(b*x**2)**(5/2)/x**5` | $\frac{\left(b x^{2}\right)^{\frac{5}{2}}}{x^{5}}$ |
| SOLVED-both | parametric | `(b*x**2)**(5/2)/x**6` | $\frac{\left(b x^{2}\right)^{\frac{5}{2}}}{x^{6}}$ |
| SOLVED-both | parametric | `(b*x**2)**(5/2)/x**7` | $\frac{\left(b x^{2}\right)^{\frac{5}{2}}}{x^{7}}$ |
| SOLVED-both | parametric | `(b*x**2)**(5/2)/x**8` | $\frac{\left(b x^{2}\right)^{\frac{5}{2}}}{x^{8}}$ |
| SOLVED-both | parametric | `(b*x**2)**(5/2)/x**9` | $\frac{\left(b x^{2}\right)^{\frac{5}{2}}}{x^{9}}$ |
| SOLVED-both | concrete | `x**2*(x**2)**(5/2)` | $x^{2} \left(x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**3/sqrt(b*x**2)` | $\frac{x^{3}}{\sqrt{b x^{2}}}$ |
| SOLVED-both | parametric | `x/sqrt(b*x**2)` | $\frac{x}{\sqrt{b x^{2}}}$ |
| SOLVED-both | parametric | `1/(x*sqrt(b*x**2))` | $\frac{1}{x \sqrt{b x^{2}}}$ |
| SOLVED-both | parametric | `1/(x**3*sqrt(b*x**2))` | $\frac{1}{x^{3} \sqrt{b x^{2}}}$ |
| SOLVED-both | parametric | `x**2/sqrt(b*x**2)` | $\frac{x^{2}}{\sqrt{b x^{2}}}$ |
| SOLVED-both | parametric | `1/sqrt(b*x**2)` | $\frac{1}{\sqrt{b x^{2}}}$ |
| SOLVED-both | parametric | `1/(x**2*sqrt(b*x**2))` | $\frac{1}{x^{2} \sqrt{b x^{2}}}$ |
| SOLVED-both | parametric | `x**5/(b*x**2)**(3/2)` | $\frac{x^{5}}{\left(b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**3/(b*x**2)**(3/2)` | $\frac{x^{3}}{\left(b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x/(b*x**2)**(3/2)` | $\frac{x}{\left(b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x*(b*x**2)**(3/2))` | $\frac{1}{x \left(b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**3*(b*x**2)**(3/2))` | $\frac{1}{x^{3} \left(b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**6/(b*x**2)**(3/2)` | $\frac{x^{6}}{\left(b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**4/(b*x**2)**(3/2)` | $\frac{x^{4}}{\left(b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**2/(b*x**2)**(3/2)` | $\frac{x^{2}}{\left(b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*x**2)**(-3/2)` | $\frac{1}{\left(b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**2*(b*x**2)**(3/2))` | $\frac{1}{x^{2} \left(b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**7/(b*x**2)**(5/2)` | $\frac{x^{7}}{\left(b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**5/(b*x**2)**(5/2)` | $\frac{x^{5}}{\left(b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**3/(b*x**2)**(5/2)` | $\frac{x^{3}}{\left(b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x/(b*x**2)**(5/2)` | $\frac{x}{\left(b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x*(b*x**2)**(5/2))` | $\frac{1}{x \left(b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**6/(b*x**2)**(5/2)` | $\frac{x^{6}}{\left(b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**4/(b*x**2)**(5/2)` | $\frac{x^{4}}{\left(b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2/(b*x**2)**(5/2)` | $\frac{x^{2}}{\left(b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b*x**2)**(-5/2)` | $\frac{1}{\left(b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**2*(b*x**2)**(5/2))` | $\frac{1}{x^{2} \left(b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `sqrt(b*x**3)` | $\sqrt{b x^{3}}$ |
| SOLVED-both | parametric | `sqrt(b*x**2)` | $\sqrt{b x^{2}}$ |
| SOLVED-both | parametric | `sqrt(b*x)` | $\sqrt{b x}$ |
| SOLVED-both | parametric | `sqrt(b/x)` | $\sqrt{\frac{b}{x}}$ |
| SOLVED-both | parametric | `sqrt(b/x**2)` | $\sqrt{\frac{b}{x^{2}}}$ |
| SOLVED-both | parametric | `sqrt(b/x**3)` | $\sqrt{\frac{b}{x^{3}}}$ |
| SOLVED-both | parametric | `(b*x**3)**(3/2)` | $\left(b x^{3}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(b*x**2)**(3/2)` | $\left(b x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(b*x)**(3/2)` | $\left(b x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(b/x)**(3/2)` | $\left(\frac{b}{x}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(b/x**2)**(3/2)` | $\left(\frac{b}{x^{2}}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(b/x**3)**(3/2)` | $\left(\frac{b}{x^{3}}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `1/sqrt(b*x**3)` | $\frac{1}{\sqrt{b x^{3}}}$ |
| SOLVED-both | parametric | `1/sqrt(b*x**2)` | $\frac{1}{\sqrt{b x^{2}}}$ |
| SOLVED-both | parametric | `1/sqrt(b*x)` | $\frac{1}{\sqrt{b x}}$ |
| SOLVED-both | parametric | `1/sqrt(b/x)` | $\frac{1}{\sqrt{\frac{b}{x}}}$ |
| SOLVED-both | parametric | `1/sqrt(b/x**2)` | $\frac{1}{\sqrt{\frac{b}{x^{2}}}}$ |
| SOLVED-both | parametric | `1/sqrt(b/x**3)` | $\frac{1}{\sqrt{\frac{b}{x^{3}}}}$ |
| SOLVED-both | parametric | `(b*x**3)**(-3/2)` | $\frac{1}{\left(b x^{3}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*x**2)**(-3/2)` | $\frac{1}{\left(b x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*x)**(-3/2)` | $\frac{1}{\left(b x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b/x)**(-3/2)` | $\frac{1}{\left(\frac{b}{x}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b/x**2)**(-3/2)` | $\frac{1}{\left(\frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b/x**3)**(-3/2)` | $\frac{1}{\left(\frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*x**3)**(1/3)` | $\sqrt[3]{b x^{3}}$ |
| SOLVED-both | parametric | `(b*x**2)**(1/3)` | $\sqrt[3]{b x^{2}}$ |
| SOLVED-both | parametric | `(b*x)**(1/3)` | $\sqrt[3]{b x}$ |
| SOLVED-both | parametric | `(b/x)**(1/3)` | $\sqrt[3]{\frac{b}{x}}$ |
| SOLVED-both | parametric | `(b/x**2)**(1/3)` | $\sqrt[3]{\frac{b}{x^{2}}}$ |
| SOLVED-both | parametric | `(b/x**3)**(1/3)` | $\sqrt[3]{\frac{b}{x^{3}}}$ |
| SOLVED-both | parametric | `(b/x**4)**(1/3)` | $\sqrt[3]{\frac{b}{x^{4}}}$ |
| SOLVED-both | parametric | `(b*x**2)**(2/3)` | $\left(b x^{2}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `(b*x)**(2/3)` | $\left(b x\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `(b/x)**(2/3)` | $\left(\frac{b}{x}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `(b/x**2)**(2/3)` | $\left(\frac{b}{x^{2}}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `(b/x**3)**(2/3)` | $\left(\frac{b}{x^{3}}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `(b/x**4)**(2/3)` | $\left(\frac{b}{x^{4}}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `(b*x**4)**(-1/3)` | $\frac{1}{\sqrt[3]{b x^{4}}}$ |
| SOLVED-both | parametric | `(b*x**3)**(-1/3)` | $\frac{1}{\sqrt[3]{b x^{3}}}$ |
| SOLVED-both | parametric | `(b*x**2)**(-1/3)` | $\frac{1}{\sqrt[3]{b x^{2}}}$ |
| SOLVED-both | parametric | `(b*x)**(-1/3)` | $\frac{1}{\sqrt[3]{b x}}$ |
| SOLVED-both | parametric | `(b/x)**(-1/3)` | $\frac{1}{\sqrt[3]{\frac{b}{x}}}$ |
| SOLVED-both | parametric | `(b/x**2)**(-1/3)` | $\frac{1}{\sqrt[3]{\frac{b}{x^{2}}}}$ |
| SOLVED-both | parametric | `(b/x**3)**(-1/3)` | $\frac{1}{\sqrt[3]{\frac{b}{x^{3}}}}$ |
| SOLVED-both | parametric | `(b*x**3)**(-2/3)` | $\frac{1}{\left(b x^{3}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `(b*x**2)**(-2/3)` | $\frac{1}{\left(b x^{2}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `(b*x)**(-2/3)` | $\frac{1}{\left(b x\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `(b/x)**(-2/3)` | $\frac{1}{\left(\frac{b}{x}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `(b/x**2)**(-2/3)` | $\frac{1}{\left(\frac{b}{x^{2}}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `(b/x**3)**(-2/3)` | $\frac{1}{\left(\frac{b}{x^{3}}\right)^{\frac{2}{3}}}$ |
| partial | concrete | `sqrt(x)/(x**3 + 1)` | $\frac{\sqrt{x}}{x^{3} + 1}$ |
| SOLVED-both | parametric | `x**11*sqrt(a + b*x**3)` | $x^{11} \sqrt{a + b x^{3}}$ |
| SOLVED-both | parametric | `x**8*sqrt(a + b*x**3)` | $x^{8} \sqrt{a + b x^{3}}$ |
| SOLVED-both | parametric | `x**5*sqrt(a + b*x**3)` | $x^{5} \sqrt{a + b x^{3}}$ |
| SOLVED-both | parametric | `x**2*sqrt(a + b*x**3)` | $x^{2} \sqrt{a + b x^{3}}$ |
| partial | parametric | `sqrt(a + b*x**3)/x` | $\frac{\sqrt{a + b x^{3}}}{x}$ |
| partial | parametric | `sqrt(a + b*x**3)/x**4` | $\frac{\sqrt{a + b x^{3}}}{x^{4}}$ |
| partial | parametric | `sqrt(a + b*x**3)/x**7` | $\frac{\sqrt{a + b x^{3}}}{x^{7}}$ |
| partial | parametric | `sqrt(a + b*x**3)/x**10` | $\frac{\sqrt{a + b x^{3}}}{x^{10}}$ |
| partial | parametric | `x**6*sqrt(a + b*x**3)` | $x^{6} \sqrt{a + b x^{3}}$ |
| partial | parametric | `x**3*sqrt(a + b*x**3)` | $x^{3} \sqrt{a + b x^{3}}$ |
| partial | parametric | `sqrt(a + b*x**3)` | $\sqrt{a + b x^{3}}$ |
| partial | parametric | `sqrt(a + b*x**3)/x**3` | $\frac{\sqrt{a + b x^{3}}}{x^{3}}$ |
| partial | parametric | `sqrt(a + b*x**3)/x**6` | $\frac{\sqrt{a + b x^{3}}}{x^{6}}$ |
| partial | parametric | `sqrt(a + b*x**3)/x**9` | $\frac{\sqrt{a + b x^{3}}}{x^{9}}$ |
| partial | parametric | `x**7*sqrt(a + b*x**3)` | $x^{7} \sqrt{a + b x^{3}}$ |
| partial | parametric | `x**4*sqrt(a + b*x**3)` | $x^{4} \sqrt{a + b x^{3}}$ |
| partial | parametric | `x*sqrt(a + b*x**3)` | $x \sqrt{a + b x^{3}}$ |
| partial | parametric | `sqrt(a + b*x**3)/x**2` | $\frac{\sqrt{a + b x^{3}}}{x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**3)/x**5` | $\frac{\sqrt{a + b x^{3}}}{x^{5}}$ |
| SOLVED-both | parametric | `x**11*(a + b*x**3)**(3/2)` | $x^{11} \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**8*(a + b*x**3)**(3/2)` | $x^{8} \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**5*(a + b*x**3)**(3/2)` | $x^{5} \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x**3)**(3/2)` | $x^{2} \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)/x` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a + b*x**3)**(3/2)/x**4` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)/x**7` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `x**6*(a + b*x**3)**(3/2)` | $x^{6} \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**3*(a + b*x**3)**(3/2)` | $x^{3} \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)` | $\left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)/x**3` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)/x**6` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `x**7*(a + b*x**3)**(3/2)` | $x^{7} \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**4*(a + b*x**3)**(3/2)` | $x^{4} \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a + b*x**3)**(3/2)` | $x \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)/x**2` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)/x**5` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{5}}$ |
| SOLVED-both | parametric | `x**11/sqrt(a + b*x**3)` | $\frac{x^{11}}{\sqrt{a + b x^{3}}}$ |
| SOLVED-both | parametric | `x**8/sqrt(a + b*x**3)` | $\frac{x^{8}}{\sqrt{a + b x^{3}}}$ |
| SOLVED-both | parametric | `x**5/sqrt(a + b*x**3)` | $\frac{x^{5}}{\sqrt{a + b x^{3}}}$ |
| SOLVED-both | parametric | `x**2/sqrt(a + b*x**3)` | $\frac{x^{2}}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x**3))` | $\frac{1}{x \sqrt{a + b x^{3}}}$ |
| partial | parametric | `1/(x**4*sqrt(a + b*x**3))` | $\frac{1}{x^{4} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `1/(x**7*sqrt(a + b*x**3))` | $\frac{1}{x^{7} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `x**6/sqrt(a + b*x**3)` | $\frac{x^{6}}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `x**3/sqrt(a + b*x**3)` | $\frac{x^{3}}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `1/sqrt(a + b*x**3)` | $\frac{1}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `1/(x**3*sqrt(a + b*x**3))` | $\frac{1}{x^{3} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `1/(x**6*sqrt(a + b*x**3))` | $\frac{1}{x^{6} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `x**7/sqrt(a + b*x**3)` | $\frac{x^{7}}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `x**4/sqrt(a + b*x**3)` | $\frac{x^{4}}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `x/sqrt(a + b*x**3)` | $\frac{x}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b*x**3))` | $\frac{1}{x^{2} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `1/(x**5*sqrt(a + b*x**3))` | $\frac{1}{x^{5} \sqrt{a + b x^{3}}}$ |
| SOLVED-both | parametric | `x**11/(a + b*x**3)**(3/2)` | $\frac{x^{11}}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**8/(a + b*x**3)**(3/2)` | $\frac{x^{8}}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**5/(a + b*x**3)**(3/2)` | $\frac{x^{5}}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**2/(a + b*x**3)**(3/2)` | $\frac{x^{2}}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**3)**(3/2))` | $\frac{1}{x \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**3)**(3/2))` | $\frac{1}{x^{4} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**7*(a + b*x**3)**(3/2))` | $\frac{1}{x^{7} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**6/(a + b*x**3)**(3/2)` | $\frac{x^{6}}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/(a + b*x**3)**(3/2)` | $\frac{x^{3}}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**3)**(-3/2)` | $\frac{1}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**3)**(3/2))` | $\frac{1}{x^{3} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**6*(a + b*x**3)**(3/2))` | $\frac{1}{x^{6} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**7/(a + b*x**3)**(3/2)` | $\frac{x^{7}}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/(a + b*x**3)**(3/2)` | $\frac{x^{4}}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a + b*x**3)**(3/2)` | $\frac{x}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**3)**(3/2))` | $\frac{1}{x^{2} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**3)**(3/2))` | $\frac{1}{x^{5} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x**11/sqrt(x**3 + 1)` | $\frac{x^{11}}{\sqrt{x^{3} + 1}}$ |
| SOLVED-both | concrete | `x**8/sqrt(x**3 + 1)` | $\frac{x^{8}}{\sqrt{x^{3} + 1}}$ |
| SOLVED-both | concrete | `x**5/sqrt(x**3 + 1)` | $\frac{x^{5}}{\sqrt{x^{3} + 1}}$ |
| SOLVED-both | concrete | `x**2/sqrt(x**3 + 1)` | $\frac{x^{2}}{\sqrt{x^{3} + 1}}$ |
| partial | concrete | `1/(x*sqrt(x**3 + 1))` | $\frac{1}{x \sqrt{x^{3} + 1}}$ |
| partial | concrete | `1/(x**4*sqrt(x**3 + 1))` | $\frac{1}{x^{4} \sqrt{x^{3} + 1}}$ |
| partial | concrete | `1/(x**7*sqrt(x**3 + 1))` | $\frac{1}{x^{7} \sqrt{x^{3} + 1}}$ |
| partial | concrete | `1/(x**10*sqrt(x**3 + 1))` | $\frac{1}{x^{10} \sqrt{x^{3} + 1}}$ |
| partial | concrete | `x**6/sqrt(x**3 + 1)` | $\frac{x^{6}}{\sqrt{x^{3} + 1}}$ |
| partial | concrete | `x**3/sqrt(x**3 + 1)` | $\frac{x^{3}}{\sqrt{x^{3} + 1}}$ |
| partial | concrete | `1/sqrt(x**3 + 1)` | $\frac{1}{\sqrt{x^{3} + 1}}$ |
| partial | concrete | `1/(x**3*sqrt(x**3 + 1))` | $\frac{1}{x^{3} \sqrt{x^{3} + 1}}$ |
| partial | concrete | `1/(x**6*sqrt(x**3 + 1))` | $\frac{1}{x^{6} \sqrt{x^{3} + 1}}$ |
| partial | concrete | `x**7/sqrt(x**3 + 1)` | $\frac{x^{7}}{\sqrt{x^{3} + 1}}$ |
| partial | concrete | `x**4/sqrt(x**3 + 1)` | $\frac{x^{4}}{\sqrt{x^{3} + 1}}$ |
| partial | concrete | `x/sqrt(x**3 + 1)` | $\frac{x}{\sqrt{x^{3} + 1}}$ |
| partial | concrete | `1/(x**2*sqrt(x**3 + 1))` | $\frac{1}{x^{2} \sqrt{x^{3} + 1}}$ |
| partial | concrete | `1/(x**5*sqrt(x**3 + 1))` | $\frac{1}{x^{5} \sqrt{x^{3} + 1}}$ |
| SOLVED-both | concrete | `x**11/sqrt(1 - x**3)` | $\frac{x^{11}}{\sqrt{1 - x^{3}}}$ |
| SOLVED-both | concrete | `x**8/sqrt(1 - x**3)` | $\frac{x^{8}}{\sqrt{1 - x^{3}}}$ |
| SOLVED-both | concrete | `x**5/sqrt(1 - x**3)` | $\frac{x^{5}}{\sqrt{1 - x^{3}}}$ |
| SOLVED-both | concrete | `x**2/sqrt(1 - x**3)` | $\frac{x^{2}}{\sqrt{1 - x^{3}}}$ |
| partial | concrete | `1/(x*sqrt(1 - x**3))` | $\frac{1}{x \sqrt{1 - x^{3}}}$ |
| partial | concrete | `1/(x**4*sqrt(1 - x**3))` | $\frac{1}{x^{4} \sqrt{1 - x^{3}}}$ |
| partial | concrete | `1/(x**7*sqrt(1 - x**3))` | $\frac{1}{x^{7} \sqrt{1 - x^{3}}}$ |
| partial | concrete | `1/(x**10*sqrt(1 - x**3))` | $\frac{1}{x^{10} \sqrt{1 - x^{3}}}$ |
| partial | concrete | `x**6/sqrt(1 - x**3)` | $\frac{x^{6}}{\sqrt{1 - x^{3}}}$ |
| partial | concrete | `x**3/sqrt(1 - x**3)` | $\frac{x^{3}}{\sqrt{1 - x^{3}}}$ |
| partial | concrete | `1/sqrt(1 - x**3)` | $\frac{1}{\sqrt{1 - x^{3}}}$ |
| partial | concrete | `1/(x**3*sqrt(1 - x**3))` | $\frac{1}{x^{3} \sqrt{1 - x^{3}}}$ |
| partial | concrete | `1/(x**6*sqrt(1 - x**3))` | $\frac{1}{x^{6} \sqrt{1 - x^{3}}}$ |
| partial | concrete | `x**7/sqrt(1 - x**3)` | $\frac{x^{7}}{\sqrt{1 - x^{3}}}$ |
| partial | concrete | `x**4/sqrt(1 - x**3)` | $\frac{x^{4}}{\sqrt{1 - x^{3}}}$ |
| partial | concrete | `x/sqrt(1 - x**3)` | $\frac{x}{\sqrt{1 - x^{3}}}$ |
| partial | concrete | `1/(x**2*sqrt(1 - x**3))` | $\frac{1}{x^{2} \sqrt{1 - x^{3}}}$ |
| partial | concrete | `1/(x**5*sqrt(1 - x**3))` | $\frac{1}{x^{5} \sqrt{1 - x^{3}}}$ |
| SOLVED-both | concrete | `x**11/sqrt(x**3 - 1)` | $\frac{x^{11}}{\sqrt{x^{3} - 1}}$ |
| SOLVED-both | concrete | `x**8/sqrt(x**3 - 1)` | $\frac{x^{8}}{\sqrt{x^{3} - 1}}$ |
| SOLVED-both | concrete | `x**5/sqrt(x**3 - 1)` | $\frac{x^{5}}{\sqrt{x^{3} - 1}}$ |
| SOLVED-both | concrete | `x**2/sqrt(x**3 - 1)` | $\frac{x^{2}}{\sqrt{x^{3} - 1}}$ |
| partial | concrete | `1/(x*sqrt(x**3 - 1))` | $\frac{1}{x \sqrt{x^{3} - 1}}$ |
| partial | concrete | `1/(x**4*sqrt(x**3 - 1))` | $\frac{1}{x^{4} \sqrt{x^{3} - 1}}$ |
| partial | concrete | `1/(x**7*sqrt(x**3 - 1))` | $\frac{1}{x^{7} \sqrt{x^{3} - 1}}$ |
| partial | concrete | `1/(x**10*sqrt(x**3 - 1))` | $\frac{1}{x^{10} \sqrt{x^{3} - 1}}$ |
| partial | concrete | `x**6/sqrt(x**3 - 1)` | $\frac{x^{6}}{\sqrt{x^{3} - 1}}$ |
| partial | concrete | `x**3/sqrt(x**3 - 1)` | $\frac{x^{3}}{\sqrt{x^{3} - 1}}$ |
| partial | concrete | `1/sqrt(x**3 - 1)` | $\frac{1}{\sqrt{x^{3} - 1}}$ |
| partial | concrete | `1/(x**3*sqrt(x**3 - 1))` | $\frac{1}{x^{3} \sqrt{x^{3} - 1}}$ |
| partial | concrete | `1/(x**6*sqrt(x**3 - 1))` | $\frac{1}{x^{6} \sqrt{x^{3} - 1}}$ |
| partial | concrete | `x**7/sqrt(x**3 - 1)` | $\frac{x^{7}}{\sqrt{x^{3} - 1}}$ |
| partial | concrete | `x**4/sqrt(x**3 - 1)` | $\frac{x^{4}}{\sqrt{x^{3} - 1}}$ |
| partial | concrete | `x/sqrt(x**3 - 1)` | $\frac{x}{\sqrt{x^{3} - 1}}$ |
| partial | concrete | `1/(x**2*sqrt(x**3 - 1))` | $\frac{1}{x^{2} \sqrt{x^{3} - 1}}$ |
| partial | concrete | `1/(x**5*sqrt(x**3 - 1))` | $\frac{1}{x^{5} \sqrt{x^{3} - 1}}$ |
| SOLVED-both | concrete | `x**11/sqrt(-x**3 - 1)` | $\frac{x^{11}}{\sqrt{- x^{3} - 1}}$ |
| SOLVED-both | concrete | `x**8/sqrt(-x**3 - 1)` | $\frac{x^{8}}{\sqrt{- x^{3} - 1}}$ |
| SOLVED-both | concrete | `x**5/sqrt(-x**3 - 1)` | $\frac{x^{5}}{\sqrt{- x^{3} - 1}}$ |
| SOLVED-both | concrete | `x**2/sqrt(-x**3 - 1)` | $\frac{x^{2}}{\sqrt{- x^{3} - 1}}$ |
| partial | concrete | `1/(x*sqrt(-x**3 - 1))` | $\frac{1}{x \sqrt{- x^{3} - 1}}$ |
| partial | concrete | `1/(x**4*sqrt(-x**3 - 1))` | $\frac{1}{x^{4} \sqrt{- x^{3} - 1}}$ |
| partial | concrete | `1/(x**7*sqrt(-x**3 - 1))` | $\frac{1}{x^{7} \sqrt{- x^{3} - 1}}$ |
| partial | concrete | `1/(x**10*sqrt(-x**3 - 1))` | $\frac{1}{x^{10} \sqrt{- x^{3} - 1}}$ |
| partial | concrete | `x**6/sqrt(-x**3 - 1)` | $\frac{x^{6}}{\sqrt{- x^{3} - 1}}$ |
| partial | concrete | `x**3/sqrt(-x**3 - 1)` | $\frac{x^{3}}{\sqrt{- x^{3} - 1}}$ |
| partial | concrete | `1/sqrt(-x**3 - 1)` | $\frac{1}{\sqrt{- x^{3} - 1}}$ |
| partial | concrete | `1/(x**3*sqrt(-x**3 - 1))` | $\frac{1}{x^{3} \sqrt{- x^{3} - 1}}$ |
| partial | concrete | `1/(x**6*sqrt(-x**3 - 1))` | $\frac{1}{x^{6} \sqrt{- x^{3} - 1}}$ |
| partial | concrete | `x**7/sqrt(-x**3 - 1)` | $\frac{x^{7}}{\sqrt{- x^{3} - 1}}$ |
| partial | concrete | `x**4/sqrt(-x**3 - 1)` | $\frac{x^{4}}{\sqrt{- x^{3} - 1}}$ |
| partial | concrete | `x/sqrt(-x**3 - 1)` | $\frac{x}{\sqrt{- x^{3} - 1}}$ |
| partial | concrete | `1/(x**2*sqrt(-x**3 - 1))` | $\frac{1}{x^{2} \sqrt{- x^{3} - 1}}$ |
| partial | concrete | `1/(x**5*sqrt(-x**3 - 1))` | $\frac{1}{x^{5} \sqrt{- x^{3} - 1}}$ |
| SOLVED-both | parametric | `x**11*(a + b*x**3)**(1/3)` | $x^{11} \sqrt[3]{a + b x^{3}}$ |
| SOLVED-both | parametric | `x**8*(a + b*x**3)**(1/3)` | $x^{8} \sqrt[3]{a + b x^{3}}$ |
| SOLVED-both | parametric | `x**5*(a + b*x**3)**(1/3)` | $x^{5} \sqrt[3]{a + b x^{3}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x**3)**(1/3)` | $x^{2} \sqrt[3]{a + b x^{3}}$ |
| partial | parametric | `(a + b*x**3)**(1/3)/x` | $\frac{\sqrt[3]{a + b x^{3}}}{x}$ |
| partial | parametric | `(a + b*x**3)**(1/3)/x**4` | $\frac{\sqrt[3]{a + b x^{3}}}{x^{4}}$ |
| partial | parametric | `x**4*(a + b*x**3)**(1/3)` | $x^{4} \sqrt[3]{a + b x^{3}}$ |
| partial | parametric | `x*(a + b*x**3)**(1/3)` | $x \sqrt[3]{a + b x^{3}}$ |
| partial | parametric | `(a + b*x**3)**(1/3)/x**2` | $\frac{\sqrt[3]{a + b x^{3}}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x**3)**(1/3)/x**5` | $\frac{\sqrt[3]{a + b x^{3}}}{x^{5}}$ |
| SOLVED-both | parametric | `(a + b*x**3)**(1/3)/x**8` | $\frac{\sqrt[3]{a + b x^{3}}}{x^{8}}$ |
| SOLVED-both | parametric | `(a + b*x**3)**(1/3)/x**11` | $\frac{\sqrt[3]{a + b x^{3}}}{x^{11}}$ |
| SOLVED-both | parametric | `x**11*(a + b*x**3)**(2/3)` | $x^{11} \left(a + b x^{3}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `x**8*(a + b*x**3)**(2/3)` | $x^{8} \left(a + b x^{3}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `x**5*(a + b*x**3)**(2/3)` | $x^{5} \left(a + b x^{3}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `x**2*(a + b*x**3)**(2/3)` | $x^{2} \left(a + b x^{3}\right)^{\frac{2}{3}}$ |
| partial | parametric | `(a + b*x**3)**(2/3)/x` | $\frac{\left(a + b x^{3}\right)^{\frac{2}{3}}}{x}$ |
| partial | parametric | `(a + b*x**3)**(2/3)/x**4` | $\frac{\left(a + b x^{3}\right)^{\frac{2}{3}}}{x^{4}}$ |
| partial | parametric | `x**3*(a + b*x**3)**(2/3)` | $x^{3} \left(a + b x^{3}\right)^{\frac{2}{3}}$ |
| partial | parametric | `(a + b*x**3)**(2/3)` | $\left(a + b x^{3}\right)^{\frac{2}{3}}$ |
| partial | parametric | `(a + b*x**3)**(2/3)/x**3` | $\frac{\left(a + b x^{3}\right)^{\frac{2}{3}}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*x**3)**(2/3)/x**6` | $\frac{\left(a + b x^{3}\right)^{\frac{2}{3}}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b*x**3)**(2/3)/x**9` | $\frac{\left(a + b x^{3}\right)^{\frac{2}{3}}}{x^{9}}$ |
| SOLVED-both | parametric | `(a + b*x**3)**(2/3)/x**12` | $\frac{\left(a + b x^{3}\right)^{\frac{2}{3}}}{x^{12}}$ |
| SOLVED-both | concrete | `x**8*(1 - x**3)**(6/5)` | $x^{8} \left(1 - x^{3}\right)^{\frac{6}{5}}$ |
| SOLVED-both | parametric | `x**11/(a + b*x**3)**(1/3)` | $\frac{x^{11}}{\sqrt[3]{a + b x^{3}}}$ |
| SOLVED-both | parametric | `x**8/(a + b*x**3)**(1/3)` | $\frac{x^{8}}{\sqrt[3]{a + b x^{3}}}$ |
| SOLVED-both | parametric | `x**5/(a + b*x**3)**(1/3)` | $\frac{x^{5}}{\sqrt[3]{a + b x^{3}}}$ |
| SOLVED-both | parametric | `x**2/(a + b*x**3)**(1/3)` | $\frac{x^{2}}{\sqrt[3]{a + b x^{3}}}$ |
| partial | parametric | `1/(x*(a + b*x**3)**(1/3))` | $\frac{1}{x \sqrt[3]{a + b x^{3}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**3)**(1/3))` | $\frac{1}{x^{4} \sqrt[3]{a + b x^{3}}}$ |
| partial | parametric | `x**3/(a + b*x**3)**(1/3)` | $\frac{x^{3}}{\sqrt[3]{a + b x^{3}}}$ |
| partial | parametric | `(a + b*x**3)**(-1/3)` | $\frac{1}{\sqrt[3]{a + b x^{3}}}$ |
| SOLVED-both | parametric | `1/(x**3*(a + b*x**3)**(1/3))` | $\frac{1}{x^{3} \sqrt[3]{a + b x^{3}}}$ |
| SOLVED-both | parametric | `1/(x**6*(a + b*x**3)**(1/3))` | $\frac{1}{x^{6} \sqrt[3]{a + b x^{3}}}$ |
| SOLVED-both | parametric | `1/(x**9*(a + b*x**3)**(1/3))` | $\frac{1}{x^{9} \sqrt[3]{a + b x^{3}}}$ |
| SOLVED-both | parametric | `1/(x**12*(a + b*x**3)**(1/3))` | $\frac{1}{x^{12} \sqrt[3]{a + b x^{3}}}$ |
| SOLVED-both | parametric | `x**11/(a + b*x**3)**(2/3)` | $\frac{x^{11}}{\left(a + b x^{3}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `x**8/(a + b*x**3)**(2/3)` | $\frac{x^{8}}{\left(a + b x^{3}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `x**5/(a + b*x**3)**(2/3)` | $\frac{x^{5}}{\left(a + b x^{3}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `x**2/(a + b*x**3)**(2/3)` | $\frac{x^{2}}{\left(a + b x^{3}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x*(a + b*x**3)**(2/3))` | $\frac{1}{x \left(a + b x^{3}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**3)**(2/3))` | $\frac{1}{x^{4} \left(a + b x^{3}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `x**4/(a + b*x**3)**(2/3)` | $\frac{x^{4}}{\left(a + b x^{3}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `1/(x**2*(a + b*x**3)**(2/3))` | $\frac{1}{x^{2} \left(a + b x^{3}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `1/(x**5*(a + b*x**3)**(2/3))` | $\frac{1}{x^{5} \left(a + b x^{3}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `1/(x**8*(a + b*x**3)**(2/3))` | $\frac{1}{x^{8} \left(a + b x^{3}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `1/(x**11*(a + b*x**3)**(2/3))` | $\frac{1}{x^{11} \left(a + b x^{3}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a - b*x**3)**(-1/3)` | $\frac{1}{\sqrt[3]{a - b x^{3}}}$ |
| partial | concrete | `(x**3 + 2)**(-1/3)` | $\frac{1}{\sqrt[3]{x^{3} + 2}}$ |
| SOLVED-both | concrete | `x**2/(x**3 + 2)**(1/4)` | $\frac{x^{2}}{\sqrt[4]{x^{3} + 2}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + c*x**4)` | $x^{\frac{5}{2}} \left(a + c x^{4}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(a + c*x**4)` | $x^{\frac{3}{2}} \left(a + c x^{4}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(a + c*x**4)` | $\sqrt{x} \left(a + c x^{4}\right)$ |
| SOLVED-both | parametric | `(a + c*x**4)/sqrt(x)` | $\frac{a + c x^{4}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + c*x**4)/x**(3/2)` | $\frac{a + c x^{4}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**4)/x**(5/2)` | $\frac{a + c x^{4}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**4)/x**(7/2)` | $\frac{a + c x^{4}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + c*x**4)**2` | $x^{\frac{5}{2}} \left(a + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + c*x**4)**2` | $x^{\frac{3}{2}} \left(a + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(a + c*x**4)**2` | $\sqrt{x} \left(a + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `(a + c*x**4)**2/sqrt(x)` | $\frac{\left(a + c x^{4}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + c*x**4)**2/x**(3/2)` | $\frac{\left(a + c x^{4}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**4)**2/x**(5/2)` | $\frac{\left(a + c x^{4}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**4)**2/x**(7/2)` | $\frac{\left(a + c x^{4}\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + c*x**4)**3` | $x^{\frac{5}{2}} \left(a + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + c*x**4)**3` | $x^{\frac{3}{2}} \left(a + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(a + c*x**4)**3` | $\sqrt{x} \left(a + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `(a + c*x**4)**3/sqrt(x)` | $\frac{\left(a + c x^{4}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + c*x**4)**3/x**(3/2)` | $\frac{\left(a + c x^{4}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**4)**3/x**(5/2)` | $\frac{\left(a + c x^{4}\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**4)**3/x**(7/2)` | $\frac{\left(a + c x^{4}\right)^{3}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `x**(9/2)/(a + c*x**4)` | $\frac{x^{\frac{9}{2}}}{a + c x^{4}}$ |
| partial | parametric | `x**(7/2)/(a + c*x**4)` | $\frac{x^{\frac{7}{2}}}{a + c x^{4}}$ |
| partial | parametric | `x**(5/2)/(a + c*x**4)` | $\frac{x^{\frac{5}{2}}}{a + c x^{4}}$ |
| partial | parametric | `x**(3/2)/(a + c*x**4)` | $\frac{x^{\frac{3}{2}}}{a + c x^{4}}$ |
| partial | parametric | `sqrt(x)/(a + c*x**4)` | $\frac{\sqrt{x}}{a + c x^{4}}$ |
| partial | parametric | `1/(sqrt(x)*(a + c*x**4))` | $\frac{1}{\sqrt{x} \left(a + c x^{4}\right)}$ |
| partial | parametric | `1/(x**(3/2)*(a + c*x**4))` | $\frac{1}{x^{\frac{3}{2}} \left(a + c x^{4}\right)}$ |
| partial | parametric | `1/(x**(5/2)*(a + c*x**4))` | $\frac{1}{x^{\frac{5}{2}} \left(a + c x^{4}\right)}$ |
| partial | parametric | `x**(13/2)/(a + c*x**4)**2` | $\frac{x^{\frac{13}{2}}}{\left(a + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(11/2)/(a + c*x**4)**2` | $\frac{x^{\frac{11}{2}}}{\left(a + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(9/2)/(a + c*x**4)**2` | $\frac{x^{\frac{9}{2}}}{\left(a + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(7/2)/(a + c*x**4)**2` | $\frac{x^{\frac{7}{2}}}{\left(a + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(5/2)/(a + c*x**4)**2` | $\frac{x^{\frac{5}{2}}}{\left(a + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(3/2)/(a + c*x**4)**2` | $\frac{x^{\frac{3}{2}}}{\left(a + c x^{4}\right)^{2}}$ |
| partial | parametric | `sqrt(x)/(a + c*x**4)**2` | $\frac{\sqrt{x}}{\left(a + c x^{4}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(x)*(a + c*x**4)**2)` | $\frac{1}{\sqrt{x} \left(a + c x^{4}\right)^{2}}$ |
| partial | parametric | `1/(x**(3/2)*(a + c*x**4)**2)` | $\frac{1}{x^{\frac{3}{2}} \left(a + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(15/2)/(a + c*x**4)**3` | $\frac{x^{\frac{15}{2}}}{\left(a + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(13/2)/(a + c*x**4)**3` | $\frac{x^{\frac{13}{2}}}{\left(a + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(11/2)/(a + c*x**4)**3` | $\frac{x^{\frac{11}{2}}}{\left(a + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(9/2)/(a + c*x**4)**3` | $\frac{x^{\frac{9}{2}}}{\left(a + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(7/2)/(a + c*x**4)**3` | $\frac{x^{\frac{7}{2}}}{\left(a + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(5/2)/(a + c*x**4)**3` | $\frac{x^{\frac{5}{2}}}{\left(a + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(3/2)/(a + c*x**4)**3` | $\frac{x^{\frac{3}{2}}}{\left(a + c x^{4}\right)^{3}}$ |
| partial | parametric | `sqrt(x)/(a + c*x**4)**3` | $\frac{\sqrt{x}}{\left(a + c x^{4}\right)^{3}}$ |
| partial | parametric | `1/(sqrt(x)*(a + c*x**4)**3)` | $\frac{1}{\sqrt{x} \left(a + c x^{4}\right)^{3}}$ |
| SOLVED-both | parametric | `x**11*sqrt(a + c*x**4)` | $x^{11} \sqrt{a + c x^{4}}$ |
| SOLVED-both | parametric | `x**7*sqrt(a + c*x**4)` | $x^{7} \sqrt{a + c x^{4}}$ |
| SOLVED-both | parametric | `x**3*sqrt(a + c*x**4)` | $x^{3} \sqrt{a + c x^{4}}$ |
| partial | parametric | `sqrt(a + c*x**4)/x` | $\frac{\sqrt{a + c x^{4}}}{x}$ |
| partial | parametric | `sqrt(a + c*x**4)/x**5` | $\frac{\sqrt{a + c x^{4}}}{x^{5}}$ |
| partial | parametric | `sqrt(a + c*x**4)/x**9` | $\frac{\sqrt{a + c x^{4}}}{x^{9}}$ |
| partial | parametric | `x**5*sqrt(a + c*x**4)` | $x^{5} \sqrt{a + c x^{4}}$ |
| partial | parametric | `x*sqrt(a + c*x**4)` | $x \sqrt{a + c x^{4}}$ |
| partial | parametric | `sqrt(a + c*x**4)/x**3` | $\frac{\sqrt{a + c x^{4}}}{x^{3}}$ |
| SOLVED-both | parametric | `sqrt(a + c*x**4)/x**7` | $\frac{\sqrt{a + c x^{4}}}{x^{7}}$ |
| SOLVED-both | parametric | `sqrt(a + c*x**4)/x**11` | $\frac{\sqrt{a + c x^{4}}}{x^{11}}$ |
| SOLVED-both | parametric | `sqrt(a + c*x**4)/x**15` | $\frac{\sqrt{a + c x^{4}}}{x^{15}}$ |
| partial | parametric | `x**4*sqrt(a + c*x**4)` | $x^{4} \sqrt{a + c x^{4}}$ |
| partial | parametric | `sqrt(a + c*x**4)` | $\sqrt{a + c x^{4}}$ |
| partial | parametric | `sqrt(a + c*x**4)/x**4` | $\frac{\sqrt{a + c x^{4}}}{x^{4}}$ |
| partial | parametric | `sqrt(a + c*x**4)/x**8` | $\frac{\sqrt{a + c x^{4}}}{x^{8}}$ |
| partial | parametric | `x**2*sqrt(a + c*x**4)` | $x^{2} \sqrt{a + c x^{4}}$ |
| partial | parametric | `sqrt(a + c*x**4)/x**2` | $\frac{\sqrt{a + c x^{4}}}{x^{2}}$ |
| partial | parametric | `sqrt(a + c*x**4)/x**6` | $\frac{\sqrt{a + c x^{4}}}{x^{6}}$ |
| SOLVED-both | parametric | `x**11*(a + c*x**4)**(3/2)` | $x^{11} \left(a + c x^{4}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**7*(a + c*x**4)**(3/2)` | $x^{7} \left(a + c x^{4}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**3*(a + c*x**4)**(3/2)` | $x^{3} \left(a + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + c*x**4)**(3/2)/x` | $\frac{\left(a + c x^{4}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a + c*x**4)**(3/2)/x**5` | $\frac{\left(a + c x^{4}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(a + c*x**4)**(3/2)/x**9` | $\frac{\left(a + c x^{4}\right)^{\frac{3}{2}}}{x^{9}}$ |
| partial | parametric | `x**5*(a + c*x**4)**(3/2)` | $x^{5} \left(a + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a + c*x**4)**(3/2)` | $x \left(a + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + c*x**4)**(3/2)/x**3` | $\frac{\left(a + c x^{4}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a + c*x**4)**(3/2)/x**7` | $\frac{\left(a + c x^{4}\right)^{\frac{3}{2}}}{x^{7}}$ |
| SOLVED-both | parametric | `(a + c*x**4)**(3/2)/x**11` | $\frac{\left(a + c x^{4}\right)^{\frac{3}{2}}}{x^{11}}$ |
| SOLVED-both | parametric | `(a + c*x**4)**(3/2)/x**15` | $\frac{\left(a + c x^{4}\right)^{\frac{3}{2}}}{x^{15}}$ |
| SOLVED-both | parametric | `(a + c*x**4)**(3/2)/x**19` | $\frac{\left(a + c x^{4}\right)^{\frac{3}{2}}}{x^{19}}$ |
| partial | parametric | `x**4*(a + c*x**4)**(3/2)` | $x^{4} \left(a + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + c*x**4)**(3/2)` | $\left(a + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + c*x**4)**(3/2)/x**4` | $\frac{\left(a + c x^{4}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(a + c*x**4)**(3/2)/x**8` | $\frac{\left(a + c x^{4}\right)^{\frac{3}{2}}}{x^{8}}$ |
| partial | parametric | `x**2*(a + c*x**4)**(3/2)` | $x^{2} \left(a + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + c*x**4)**(3/2)/x**2` | $\frac{\left(a + c x^{4}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a + c*x**4)**(3/2)/x**6` | $\frac{\left(a + c x^{4}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | concrete | `(x**4 + 1)**(3/2)` | $\left(x^{4} + 1\right)^{\frac{3}{2}}$ |
| partial | concrete | `(1 - x**4)**(3/2)` | $\left(1 - x^{4}\right)^{\frac{3}{2}}$ |
| SOLVED-both | concrete | `x**7*sqrt(3*x**4 + 5)` | $x^{7} \sqrt{3 x^{4} + 5}$ |
| SOLVED-both | concrete | `x**3*sqrt(x**4 + 5)` | $x^{3} \sqrt{x^{4} + 5}$ |
| partial | concrete | `x*sqrt(2*x**4 + 3)` | $x \sqrt{2 x^{4} + 3}$ |
| partial | concrete | `x*sqrt(x**4 - 2)` | $x \sqrt{x^{4} - 2}$ |
| partial | concrete | `sqrt(x**4 + 1)` | $\sqrt{x^{4} + 1}$ |
| partial | concrete | `sqrt(1 - x**4)` | $\sqrt{1 - x^{4}}$ |
| SOLVED-both | parametric | `x**11/sqrt(a + b*x**4)` | $\frac{x^{11}}{\sqrt{a + b x^{4}}}$ |
| SOLVED-both | parametric | `x**7/sqrt(a + b*x**4)` | $\frac{x^{7}}{\sqrt{a + b x^{4}}}$ |
| SOLVED-both | parametric | `x**3/sqrt(a + b*x**4)` | $\frac{x^{3}}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x**4))` | $\frac{1}{x \sqrt{a + b x^{4}}}$ |
| partial | parametric | `1/(x**5*sqrt(a + b*x**4))` | $\frac{1}{x^{5} \sqrt{a + b x^{4}}}$ |
| partial | parametric | `x**5/sqrt(a + b*x**4)` | $\frac{x^{5}}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `x/sqrt(a + b*x**4)` | $\frac{x}{\sqrt{a + b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**3*sqrt(a + b*x**4))` | $\frac{1}{x^{3} \sqrt{a + b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**7*sqrt(a + b*x**4))` | $\frac{1}{x^{7} \sqrt{a + b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**11*sqrt(a + b*x**4))` | $\frac{1}{x^{11} \sqrt{a + b x^{4}}}$ |
| partial | parametric | `x**8/sqrt(a + b*x**4)` | $\frac{x^{8}}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `x**4/sqrt(a + b*x**4)` | $\frac{x^{4}}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `1/sqrt(a + b*x**4)` | $\frac{1}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `1/(x**4*sqrt(a + b*x**4))` | $\frac{1}{x^{4} \sqrt{a + b x^{4}}}$ |
| partial | parametric | `1/(x**8*sqrt(a + b*x**4))` | $\frac{1}{x^{8} \sqrt{a + b x^{4}}}$ |
| partial | parametric | `x**10/sqrt(a + b*x**4)` | $\frac{x^{10}}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `x**6/sqrt(a + b*x**4)` | $\frac{x^{6}}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `x**2/sqrt(a + b*x**4)` | $\frac{x^{2}}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b*x**4))` | $\frac{1}{x^{2} \sqrt{a + b x^{4}}}$ |
| partial | parametric | `1/(x**6*sqrt(a + b*x**4))` | $\frac{1}{x^{6} \sqrt{a + b x^{4}}}$ |
| SOLVED-both | parametric | `x**11/sqrt(a - b*x**4)` | $\frac{x^{11}}{\sqrt{a - b x^{4}}}$ |
| SOLVED-both | parametric | `x**7/sqrt(a - b*x**4)` | $\frac{x^{7}}{\sqrt{a - b x^{4}}}$ |
| SOLVED-both | parametric | `x**3/sqrt(a - b*x**4)` | $\frac{x^{3}}{\sqrt{a - b x^{4}}}$ |
| partial | parametric | `1/(x*sqrt(a - b*x**4))` | $\frac{1}{x \sqrt{a - b x^{4}}}$ |
| partial | parametric | `1/(x**5*sqrt(a - b*x**4))` | $\frac{1}{x^{5} \sqrt{a - b x^{4}}}$ |
| partial | parametric | `x**5/sqrt(a - b*x**4)` | $\frac{x^{5}}{\sqrt{a - b x^{4}}}$ |
| partial | parametric | `x/sqrt(a - b*x**4)` | $\frac{x}{\sqrt{a - b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**3*sqrt(a - b*x**4))` | $\frac{1}{x^{3} \sqrt{a - b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**7*sqrt(a - b*x**4))` | $\frac{1}{x^{7} \sqrt{a - b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**11*sqrt(a - b*x**4))` | $\frac{1}{x^{11} \sqrt{a - b x^{4}}}$ |
| partial | parametric | `x**8/sqrt(a - b*x**4)` | $\frac{x^{8}}{\sqrt{a - b x^{4}}}$ |
| partial | parametric | `x**4/sqrt(a - b*x**4)` | $\frac{x^{4}}{\sqrt{a - b x^{4}}}$ |
| partial | parametric | `1/sqrt(a - b*x**4)` | $\frac{1}{\sqrt{a - b x^{4}}}$ |
| partial | parametric | `1/(x**4*sqrt(a - b*x**4))` | $\frac{1}{x^{4} \sqrt{a - b x^{4}}}$ |
| partial | parametric | `1/(x**8*sqrt(a - b*x**4))` | $\frac{1}{x^{8} \sqrt{a - b x^{4}}}$ |
| partial | parametric | `x**10/sqrt(a - b*x**4)` | $\frac{x^{10}}{\sqrt{a - b x^{4}}}$ |
| partial | parametric | `x**6/sqrt(a - b*x**4)` | $\frac{x^{6}}{\sqrt{a - b x^{4}}}$ |
| partial | parametric | `x**2/sqrt(a - b*x**4)` | $\frac{x^{2}}{\sqrt{a - b x^{4}}}$ |
| partial | parametric | `1/(x**2*sqrt(a - b*x**4))` | $\frac{1}{x^{2} \sqrt{a - b x^{4}}}$ |
| partial | parametric | `1/(x**6*sqrt(a - b*x**4))` | $\frac{1}{x^{6} \sqrt{a - b x^{4}}}$ |
| SOLVED-both | parametric | `x**11/(a + b*x**4)**(3/2)` | $\frac{x^{11}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**7/(a + b*x**4)**(3/2)` | $\frac{x^{7}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x**4)**(3/2)` | $\frac{x^{3}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**4)**(3/2))` | $\frac{1}{x \left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**4)**(3/2))` | $\frac{1}{x^{5} \left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**9/(a + b*x**4)**(3/2)` | $\frac{x^{9}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5/(a + b*x**4)**(3/2)` | $\frac{x^{5}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x/(a + b*x**4)**(3/2)` | $\frac{x}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**3*(a + b*x**4)**(3/2))` | $\frac{1}{x^{3} \left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**7*(a + b*x**4)**(3/2))` | $\frac{1}{x^{7} \left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**12/(a + b*x**4)**(3/2)` | $\frac{x^{12}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**8/(a + b*x**4)**(3/2)` | $\frac{x^{8}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/(a + b*x**4)**(3/2)` | $\frac{x^{4}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**4)**(-3/2)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**4)**(3/2))` | $\frac{1}{x^{4} \left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**8*(a + b*x**4)**(3/2))` | $\frac{1}{x^{8} \left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**14/(a + b*x**4)**(3/2)` | $\frac{x^{14}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**10/(a + b*x**4)**(3/2)` | $\frac{x^{10}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**6/(a + b*x**4)**(3/2)` | $\frac{x^{6}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a + b*x**4)**(3/2)` | $\frac{x^{2}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**4)**(3/2))` | $\frac{1}{x^{2} \left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**6*(a + b*x**4)**(3/2))` | $\frac{1}{x^{6} \left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**4)**(-5/2)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `x**11/sqrt(1 - x**4)` | $\frac{x^{11}}{\sqrt{1 - x^{4}}}$ |
| SOLVED-both | concrete | `x**7/sqrt(1 - x**4)` | $\frac{x^{7}}{\sqrt{1 - x^{4}}}$ |
| SOLVED-both | concrete | `x**3/sqrt(1 - x**4)` | $\frac{x^{3}}{\sqrt{1 - x^{4}}}$ |
| partial | concrete | `1/(x*sqrt(1 - x**4))` | $\frac{1}{x \sqrt{1 - x^{4}}}$ |
| partial | concrete | `1/(x**5*sqrt(1 - x**4))` | $\frac{1}{x^{5} \sqrt{1 - x^{4}}}$ |
| partial | concrete | `x**5/sqrt(1 - x**4)` | $\frac{x^{5}}{\sqrt{1 - x^{4}}}$ |
| partial | concrete | `x/sqrt(1 - x**4)` | $\frac{x}{\sqrt{1 - x^{4}}}$ |
| SOLVED-both | concrete | `1/(x**3*sqrt(1 - x**4))` | $\frac{1}{x^{3} \sqrt{1 - x^{4}}}$ |
| SOLVED-both | concrete | `1/(x**7*sqrt(1 - x**4))` | $\frac{1}{x^{7} \sqrt{1 - x^{4}}}$ |
| SOLVED-both | concrete | `1/(x**11*sqrt(1 - x**4))` | $\frac{1}{x^{11} \sqrt{1 - x^{4}}}$ |
| partial | concrete | `x**8/sqrt(1 - x**4)` | $\frac{x^{8}}{\sqrt{1 - x^{4}}}$ |
| partial | concrete | `x**4/sqrt(1 - x**4)` | $\frac{x^{4}}{\sqrt{1 - x^{4}}}$ |
| partial | concrete | `1/sqrt(1 - x**4)` | $\frac{1}{\sqrt{1 - x^{4}}}$ |
| partial | concrete | `1/(x**4*sqrt(1 - x**4))` | $\frac{1}{x^{4} \sqrt{1 - x^{4}}}$ |
| partial | concrete | `1/(x**8*sqrt(1 - x**4))` | $\frac{1}{x^{8} \sqrt{1 - x^{4}}}$ |
| partial | concrete | `x**10/sqrt(1 - x**4)` | $\frac{x^{10}}{\sqrt{1 - x^{4}}}$ |
| partial | concrete | `x**6/sqrt(1 - x**4)` | $\frac{x^{6}}{\sqrt{1 - x^{4}}}$ |
| partial | concrete | `x**2/sqrt(1 - x**4)` | $\frac{x^{2}}{\sqrt{1 - x^{4}}}$ |
| partial | concrete | `1/(x**2*sqrt(1 - x**4))` | $\frac{1}{x^{2} \sqrt{1 - x^{4}}}$ |
| partial | concrete | `1/(x**6*sqrt(1 - x**4))` | $\frac{1}{x^{6} \sqrt{1 - x^{4}}}$ |
| SOLVED-both | concrete | `x**11/(1 - x**4)**(3/2)` | $\frac{x^{11}}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x**7/(1 - x**4)**(3/2)` | $\frac{x^{7}}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x**3/(1 - x**4)**(3/2)` | $\frac{x^{3}}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x*(1 - x**4)**(3/2))` | $\frac{1}{x \left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**5*(1 - x**4)**(3/2))` | $\frac{1}{x^{5} \left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**9/(1 - x**4)**(3/2)` | $\frac{x^{9}}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**5/(1 - x**4)**(3/2)` | $\frac{x^{5}}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x/(1 - x**4)**(3/2)` | $\frac{x}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/(x**3*(1 - x**4)**(3/2))` | $\frac{1}{x^{3} \left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/(x**7*(1 - x**4)**(3/2))` | $\frac{1}{x^{7} \left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**12/(1 - x**4)**(3/2)` | $\frac{x^{12}}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**8/(1 - x**4)**(3/2)` | $\frac{x^{8}}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**4/(1 - x**4)**(3/2)` | $\frac{x^{4}}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - x**4)**(-3/2)` | $\frac{1}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**4*(1 - x**4)**(3/2))` | $\frac{1}{x^{4} \left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**8*(1 - x**4)**(3/2))` | $\frac{1}{x^{8} \left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**14/(1 - x**4)**(3/2)` | $\frac{x^{14}}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**10/(1 - x**4)**(3/2)` | $\frac{x^{10}}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**6/(1 - x**4)**(3/2)` | $\frac{x^{6}}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**2/(1 - x**4)**(3/2)` | $\frac{x^{2}}{\left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**2*(1 - x**4)**(3/2))` | $\frac{1}{x^{2} \left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**6*(1 - x**4)**(3/2))` | $\frac{1}{x^{6} \left(1 - x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(1 - x**4)**(-5/2)` | $\frac{1}{\left(1 - x^{4}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `x**11/sqrt(x**4 + 1)` | $\frac{x^{11}}{\sqrt{x^{4} + 1}}$ |
| SOLVED-both | concrete | `x**7/sqrt(x**4 + 1)` | $\frac{x^{7}}{\sqrt{x^{4} + 1}}$ |
| SOLVED-both | concrete | `x**3/sqrt(x**4 + 1)` | $\frac{x^{3}}{\sqrt{x^{4} + 1}}$ |
| partial | concrete | `1/(x*sqrt(x**4 + 1))` | $\frac{1}{x \sqrt{x^{4} + 1}}$ |
| partial | concrete | `1/(x**5*sqrt(x**4 + 1))` | $\frac{1}{x^{5} \sqrt{x^{4} + 1}}$ |
| partial | concrete | `x**5/sqrt(x**4 + 1)` | $\frac{x^{5}}{\sqrt{x^{4} + 1}}$ |
| partial | concrete | `x/sqrt(x**4 + 1)` | $\frac{x}{\sqrt{x^{4} + 1}}$ |
| SOLVED-both | concrete | `1/(x**3*sqrt(x**4 + 1))` | $\frac{1}{x^{3} \sqrt{x^{4} + 1}}$ |
| SOLVED-both | concrete | `1/(x**7*sqrt(x**4 + 1))` | $\frac{1}{x^{7} \sqrt{x^{4} + 1}}$ |
| SOLVED-both | concrete | `1/(x**11*sqrt(x**4 + 1))` | $\frac{1}{x^{11} \sqrt{x^{4} + 1}}$ |
| partial | concrete | `x**8/sqrt(x**4 + 1)` | $\frac{x^{8}}{\sqrt{x^{4} + 1}}$ |
| partial | concrete | `x**4/sqrt(x**4 + 1)` | $\frac{x^{4}}{\sqrt{x^{4} + 1}}$ |
| partial | concrete | `1/sqrt(x**4 + 1)` | $\frac{1}{\sqrt{x^{4} + 1}}$ |
| partial | concrete | `1/(x**4*sqrt(x**4 + 1))` | $\frac{1}{x^{4} \sqrt{x^{4} + 1}}$ |
| partial | concrete | `1/(x**8*sqrt(x**4 + 1))` | $\frac{1}{x^{8} \sqrt{x^{4} + 1}}$ |
| partial | concrete | `x**10/sqrt(x**4 + 1)` | $\frac{x^{10}}{\sqrt{x^{4} + 1}}$ |
| partial | concrete | `x**6/sqrt(x**4 + 1)` | $\frac{x^{6}}{\sqrt{x^{4} + 1}}$ |
| partial | concrete | `x**2/sqrt(x**4 + 1)` | $\frac{x^{2}}{\sqrt{x^{4} + 1}}$ |
| partial | concrete | `1/(x**2*sqrt(x**4 + 1))` | $\frac{1}{x^{2} \sqrt{x^{4} + 1}}$ |
| partial | concrete | `1/(x**6*sqrt(x**4 + 1))` | $\frac{1}{x^{6} \sqrt{x^{4} + 1}}$ |
| SOLVED-both | concrete | `x**11/(x**4 + 1)**(3/2)` | $\frac{x^{11}}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x**7/(x**4 + 1)**(3/2)` | $\frac{x^{7}}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x**3/(x**4 + 1)**(3/2)` | $\frac{x^{3}}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x*(x**4 + 1)**(3/2))` | $\frac{1}{x \left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**5*(x**4 + 1)**(3/2))` | $\frac{1}{x^{5} \left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**9/(x**4 + 1)**(3/2)` | $\frac{x^{9}}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**5/(x**4 + 1)**(3/2)` | $\frac{x^{5}}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x/(x**4 + 1)**(3/2)` | $\frac{x}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/(x**3*(x**4 + 1)**(3/2))` | $\frac{1}{x^{3} \left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/(x**7*(x**4 + 1)**(3/2))` | $\frac{1}{x^{7} \left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**12/(x**4 + 1)**(3/2)` | $\frac{x^{12}}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**8/(x**4 + 1)**(3/2)` | $\frac{x^{8}}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**4/(x**4 + 1)**(3/2)` | $\frac{x^{4}}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x**4 + 1)**(-3/2)` | $\frac{1}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**4*(x**4 + 1)**(3/2))` | $\frac{1}{x^{4} \left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**8*(x**4 + 1)**(3/2))` | $\frac{1}{x^{8} \left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**14/(x**4 + 1)**(3/2)` | $\frac{x^{14}}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**10/(x**4 + 1)**(3/2)` | $\frac{x^{10}}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**6/(x**4 + 1)**(3/2)` | $\frac{x^{6}}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**2/(x**4 + 1)**(3/2)` | $\frac{x^{2}}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**2*(x**4 + 1)**(3/2))` | $\frac{1}{x^{2} \left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**6*(x**4 + 1)**(3/2))` | $\frac{1}{x^{6} \left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x**4 + 1)**(-5/2)` | $\frac{1}{\left(x^{4} + 1\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `x**7/sqrt(16 - x**4)` | $\frac{x^{7}}{\sqrt{16 - x^{4}}}$ |
| partial | concrete | `x**5/sqrt(16 - x**4)` | $\frac{x^{5}}{\sqrt{16 - x^{4}}}$ |
| SOLVED-both | concrete | `x**3/sqrt(16 - x**4)` | $\frac{x^{3}}{\sqrt{16 - x^{4}}}$ |
| partial | concrete | `x/sqrt(16 - x**4)` | $\frac{x}{\sqrt{16 - x^{4}}}$ |
| partial | concrete | `1/(x*sqrt(16 - x**4))` | $\frac{1}{x \sqrt{16 - x^{4}}}$ |
| SOLVED-both | concrete | `1/(x**3*sqrt(16 - x**4))` | $\frac{1}{x^{3} \sqrt{16 - x^{4}}}$ |
| partial | concrete | `1/(x**5*sqrt(16 - x**4))` | $\frac{1}{x^{5} \sqrt{16 - x^{4}}}$ |
| SOLVED-both | concrete | `1/(x**7*sqrt(16 - x**4))` | $\frac{1}{x^{7} \sqrt{16 - x^{4}}}$ |
| partial | concrete | `x**6/sqrt(16 - x**4)` | $\frac{x^{6}}{\sqrt{16 - x^{4}}}$ |
| partial | concrete | `x**4/sqrt(16 - x**4)` | $\frac{x^{4}}{\sqrt{16 - x^{4}}}$ |
| partial | concrete | `x**2/sqrt(16 - x**4)` | $\frac{x^{2}}{\sqrt{16 - x^{4}}}$ |
| partial | concrete | `1/sqrt(16 - x**4)` | $\frac{1}{\sqrt{16 - x^{4}}}$ |
| partial | concrete | `1/(x**2*sqrt(16 - x**4))` | $\frac{1}{x^{2} \sqrt{16 - x^{4}}}$ |
| partial | concrete | `1/(x**4*sqrt(16 - x**4))` | $\frac{1}{x^{4} \sqrt{16 - x^{4}}}$ |
| partial | concrete | `x/sqrt(x**4 - 4)` | $\frac{x}{\sqrt{x^{4} - 4}}$ |
| partial | concrete | `x/sqrt(x**4 + 4)` | $\frac{x}{\sqrt{x^{4} + 4}}$ |
| partial | concrete | `1/(x*sqrt(x**4 - 1))` | $\frac{1}{x \sqrt{x^{4} - 1}}$ |
| partial | concrete | `x**4/sqrt(x**4 - 1)` | $\frac{x^{4}}{\sqrt{x^{4} - 1}}$ |
| partial | concrete | `1/sqrt(x**4 - 1)` | $\frac{1}{\sqrt{x^{4} - 1}}$ |
| partial | concrete | `1/(x**4*sqrt(x**4 - 1))` | $\frac{1}{x^{4} \sqrt{x^{4} - 1}}$ |
| partial | concrete | `x**6/sqrt(x**4 - 1)` | $\frac{x^{6}}{\sqrt{x^{4} - 1}}$ |
| partial | concrete | `x**2/sqrt(x**4 - 1)` | $\frac{x^{2}}{\sqrt{x^{4} - 1}}$ |
| partial | concrete | `1/(x**2*sqrt(x**4 - 1))` | $\frac{1}{x^{2} \sqrt{x^{4} - 1}}$ |
| partial | concrete | `x**2/sqrt(3 - 2*x**4)` | $\frac{x^{2}}{\sqrt{3 - 2 x^{4}}}$ |
| partial | parametric | `x**2/sqrt(-b*x**4 + 3)` | $\frac{x^{2}}{\sqrt{- b x^{4} + 3}}$ |
| SOLVED-both | concrete | `x**7*(x**4 + 1)**(1/3)` | $x^{7} \sqrt[3]{x^{4} + 1}$ |
| SOLVED-both | concrete | `x**3/(x**4 + 1)**(4/3)` | $\frac{x^{3}}{\left(x^{4} + 1\right)^{\frac{4}{3}}}$ |
| SOLVED-both | concrete | `x**3/(x**4 + 1)**(1/3)` | $\frac{x^{3}}{\sqrt[3]{x^{4} + 1}}$ |
| SOLVED-both | parametric | `x**19*(a + b*x**4)**(1/4)` | $x^{19} \sqrt[4]{a + b x^{4}}$ |
| SOLVED-both | parametric | `x**15*(a + b*x**4)**(1/4)` | $x^{15} \sqrt[4]{a + b x^{4}}$ |
| SOLVED-both | parametric | `x**11*(a + b*x**4)**(1/4)` | $x^{11} \sqrt[4]{a + b x^{4}}$ |
| SOLVED-both | parametric | `x**7*(a + b*x**4)**(1/4)` | $x^{7} \sqrt[4]{a + b x^{4}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**4)**(1/4)` | $x^{3} \sqrt[4]{a + b x^{4}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/x` | $\frac{\sqrt[4]{a + b x^{4}}}{x}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/x**5` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{5}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/x**9` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{9}}$ |
| partial | parametric | `x**9*(a + b*x**4)**(1/4)` | $x^{9} \sqrt[4]{a + b x^{4}}$ |
| partial | parametric | `x**5*(a + b*x**4)**(1/4)` | $x^{5} \sqrt[4]{a + b x^{4}}$ |
| partial | parametric | `x*(a + b*x**4)**(1/4)` | $x \sqrt[4]{a + b x^{4}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/x**3` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/x**7` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{7}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/x**11` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{11}}$ |
| partial | parametric | `x**6*(a + b*x**4)**(1/4)` | $x^{6} \sqrt[4]{a + b x^{4}}$ |
| partial | parametric | `x**2*(a + b*x**4)**(1/4)` | $x^{2} \sqrt[4]{a + b x^{4}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/x**2` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(1/4)/x**6` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(1/4)/x**10` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{10}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(1/4)/x**14` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{14}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(1/4)/x**18` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{18}}$ |
| partial | parametric | `x**12*(a + b*x**4)**(1/4)` | $x^{12} \sqrt[4]{a + b x^{4}}$ |
| partial | parametric | `x**8*(a + b*x**4)**(1/4)` | $x^{8} \sqrt[4]{a + b x^{4}}$ |
| partial | parametric | `x**4*(a + b*x**4)**(1/4)` | $x^{4} \sqrt[4]{a + b x^{4}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)` | $\sqrt[4]{a + b x^{4}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/x**4` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/x**8` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{8}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/x**12` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{12}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/x**16` | $\frac{\sqrt[4]{a + b x^{4}}}{x^{16}}$ |
| SOLVED-both | parametric | `x**19*(a + b*x**4)**(3/4)` | $x^{19} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| SOLVED-both | parametric | `x**15*(a + b*x**4)**(3/4)` | $x^{15} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| SOLVED-both | parametric | `x**11*(a + b*x**4)**(3/4)` | $x^{11} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| SOLVED-both | parametric | `x**7*(a + b*x**4)**(3/4)` | $x^{7} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**4)**(3/4)` | $x^{3} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/x` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/x**5` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{5}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/x**9` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{9}}$ |
| partial | parametric | `x**9*(a + b*x**4)**(3/4)` | $x^{9} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| partial | parametric | `x**5*(a + b*x**4)**(3/4)` | $x^{5} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| partial | parametric | `x*(a + b*x**4)**(3/4)` | $x \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/x**3` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/x**7` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{7}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/x**11` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{11}}$ |
| partial | parametric | `x**12*(a + b*x**4)**(3/4)` | $x^{12} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| partial | parametric | `x**8*(a + b*x**4)**(3/4)` | $x^{8} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| partial | parametric | `x**4*(a + b*x**4)**(3/4)` | $x^{4} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)` | $\left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/x**4` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(3/4)/x**8` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{8}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(3/4)/x**12` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{12}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(3/4)/x**16` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{16}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(3/4)/x**20` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{20}}$ |
| partial | parametric | `x**10*(a + b*x**4)**(3/4)` | $x^{10} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| partial | parametric | `x**6*(a + b*x**4)**(3/4)` | $x^{6} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| partial | parametric | `x**2*(a + b*x**4)**(3/4)` | $x^{2} \left(a + b x^{4}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/x**2` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/x**6` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{6}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/x**10` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{10}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/x**14` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{x^{14}}$ |
| SOLVED-both | parametric | `x**19*(a + b*x**4)**(5/4)` | $x^{19} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| SOLVED-both | parametric | `x**15*(a + b*x**4)**(5/4)` | $x^{15} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| SOLVED-both | parametric | `x**11*(a + b*x**4)**(5/4)` | $x^{11} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| SOLVED-both | parametric | `x**7*(a + b*x**4)**(5/4)` | $x^{7} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**4)**(5/4)` | $x^{3} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x**5` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{5}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x**9` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{9}}$ |
| partial | parametric | `x**9*(a + b*x**4)**(5/4)` | $x^{9} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| partial | parametric | `x**5*(a + b*x**4)**(5/4)` | $x^{5} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| partial | parametric | `x*(a + b*x**4)**(5/4)` | $x \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x**3` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x**7` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{7}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x**11` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{11}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x**15` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{15}}$ |
| partial | parametric | `x**10*(a + b*x**4)**(5/4)` | $x^{10} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| partial | parametric | `x**6*(a + b*x**4)**(5/4)` | $x^{6} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| partial | parametric | `x**2*(a + b*x**4)**(5/4)` | $x^{2} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x**2` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x**6` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(5/4)/x**10` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{10}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(5/4)/x**14` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{14}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(5/4)/x**18` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{18}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(5/4)/x**22` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{22}}$ |
| partial | parametric | `x**12*(a + b*x**4)**(5/4)` | $x^{12} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| partial | parametric | `x**8*(a + b*x**4)**(5/4)` | $x^{8} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| partial | parametric | `x**4*(a + b*x**4)**(5/4)` | $x^{4} \left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)` | $\left(a + b x^{4}\right)^{\frac{5}{4}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x**4` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x**8` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{8}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x**12` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{12}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/x**16` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{x^{16}}$ |
| partial | parametric | `(a + b*x**4)**(7/4)` | $\left(a + b x^{4}\right)^{\frac{7}{4}}$ |
| SOLVED-both | parametric | `x**19/(a + b*x**4)**(1/4)` | $\frac{x^{19}}{\sqrt[4]{a + b x^{4}}}$ |
| SOLVED-both | parametric | `x**15/(a + b*x**4)**(1/4)` | $\frac{x^{15}}{\sqrt[4]{a + b x^{4}}}$ |
| SOLVED-both | parametric | `x**11/(a + b*x**4)**(1/4)` | $\frac{x^{11}}{\sqrt[4]{a + b x^{4}}}$ |
| SOLVED-both | parametric | `x**7/(a + b*x**4)**(1/4)` | $\frac{x^{7}}{\sqrt[4]{a + b x^{4}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x**4)**(1/4)` | $\frac{x^{3}}{\sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `1/(x*(a + b*x**4)**(1/4))` | $\frac{1}{x \sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**4)**(1/4))` | $\frac{1}{x^{5} \sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `1/(x**9*(a + b*x**4)**(1/4))` | $\frac{1}{x^{9} \sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `x**13/(a + b*x**4)**(1/4)` | $\frac{x^{13}}{\sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `x**9/(a + b*x**4)**(1/4)` | $\frac{x^{9}}{\sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `x**5/(a + b*x**4)**(1/4)` | $\frac{x^{5}}{\sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `x/(a + b*x**4)**(1/4)` | $\frac{x}{\sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**4)**(1/4))` | $\frac{1}{x^{3} \sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `1/(x**7*(a + b*x**4)**(1/4))` | $\frac{1}{x^{7} \sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `1/(x**11*(a + b*x**4)**(1/4))` | $\frac{1}{x^{11} \sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `x**8/(a + b*x**4)**(1/4)` | $\frac{x^{8}}{\sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `x**4/(a + b*x**4)**(1/4)` | $\frac{x^{4}}{\sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `(a + b*x**4)**(-1/4)` | $\frac{1}{\sqrt[4]{a + b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**4*(a + b*x**4)**(1/4))` | $\frac{1}{x^{4} \sqrt[4]{a + b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**8*(a + b*x**4)**(1/4))` | $\frac{1}{x^{8} \sqrt[4]{a + b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**12*(a + b*x**4)**(1/4))` | $\frac{1}{x^{12} \sqrt[4]{a + b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**16*(a + b*x**4)**(1/4))` | $\frac{1}{x^{16} \sqrt[4]{a + b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**20*(a + b*x**4)**(1/4))` | $\frac{1}{x^{20} \sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `x**10/(a + b*x**4)**(1/4)` | $\frac{x^{10}}{\sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `x**6/(a + b*x**4)**(1/4)` | $\frac{x^{6}}{\sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `x**2/(a + b*x**4)**(1/4)` | $\frac{x^{2}}{\sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**4)**(1/4))` | $\frac{1}{x^{2} \sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `1/(x**6*(a + b*x**4)**(1/4))` | $\frac{1}{x^{6} \sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `1/(x**10*(a + b*x**4)**(1/4))` | $\frac{1}{x^{10} \sqrt[4]{a + b x^{4}}}$ |
| partial | parametric | `1/(x**14*(a + b*x**4)**(1/4))` | $\frac{1}{x^{14} \sqrt[4]{a + b x^{4}}}$ |
| SOLVED-both | parametric | `x**19/(a + b*x**4)**(3/4)` | $\frac{x^{19}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `x**15/(a + b*x**4)**(3/4)` | $\frac{x^{15}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `x**11/(a + b*x**4)**(3/4)` | $\frac{x^{11}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `x**7/(a + b*x**4)**(3/4)` | $\frac{x^{7}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x**4)**(3/4)` | $\frac{x^{3}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x*(a + b*x**4)**(3/4))` | $\frac{1}{x \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**4)**(3/4))` | $\frac{1}{x^{5} \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**9*(a + b*x**4)**(3/4))` | $\frac{1}{x^{9} \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**13/(a + b*x**4)**(3/4)` | $\frac{x^{13}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**9/(a + b*x**4)**(3/4)` | $\frac{x^{9}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**5/(a + b*x**4)**(3/4)` | $\frac{x^{5}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x/(a + b*x**4)**(3/4)` | $\frac{x}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**4)**(3/4))` | $\frac{1}{x^{3} \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**7*(a + b*x**4)**(3/4))` | $\frac{1}{x^{7} \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**11*(a + b*x**4)**(3/4))` | $\frac{1}{x^{11} \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**10/(a + b*x**4)**(3/4)` | $\frac{x^{10}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**6/(a + b*x**4)**(3/4)` | $\frac{x^{6}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**2/(a + b*x**4)**(3/4)` | $\frac{x^{2}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `1/(x**2*(a + b*x**4)**(3/4))` | $\frac{1}{x^{2} \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `1/(x**6*(a + b*x**4)**(3/4))` | $\frac{1}{x^{6} \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `1/(x**10*(a + b*x**4)**(3/4))` | $\frac{1}{x^{10} \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `1/(x**14*(a + b*x**4)**(3/4))` | $\frac{1}{x^{14} \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**12/(a + b*x**4)**(3/4)` | $\frac{x^{12}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**8/(a + b*x**4)**(3/4)` | $\frac{x^{8}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**4/(a + b*x**4)**(3/4)` | $\frac{x^{4}}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(a + b*x**4)**(-3/4)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**4)**(3/4))` | $\frac{1}{x^{4} \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**8*(a + b*x**4)**(3/4))` | $\frac{1}{x^{8} \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**12*(a + b*x**4)**(3/4))` | $\frac{1}{x^{12} \left(a + b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `x**19/(a + b*x**4)**(5/4)` | $\frac{x^{19}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| SOLVED-both | parametric | `x**15/(a + b*x**4)**(5/4)` | $\frac{x^{15}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| SOLVED-both | parametric | `x**11/(a + b*x**4)**(5/4)` | $\frac{x^{11}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| SOLVED-both | parametric | `x**7/(a + b*x**4)**(5/4)` | $\frac{x^{7}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| SOLVED-both | parametric | `x**3/(a + b*x**4)**(5/4)` | $\frac{x^{3}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x*(a + b*x**4)**(5/4))` | $\frac{1}{x \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**4)**(5/4))` | $\frac{1}{x^{5} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**9*(a + b*x**4)**(5/4))` | $\frac{1}{x^{9} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**13/(a + b*x**4)**(5/4)` | $\frac{x^{13}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**9/(a + b*x**4)**(5/4)` | $\frac{x^{9}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**5/(a + b*x**4)**(5/4)` | $\frac{x^{5}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x/(a + b*x**4)**(5/4)` | $\frac{x}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**4)**(5/4))` | $\frac{1}{x^{3} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**7*(a + b*x**4)**(5/4))` | $\frac{1}{x^{7} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**11*(a + b*x**4)**(5/4))` | $\frac{1}{x^{11} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**12/(a + b*x**4)**(5/4)` | $\frac{x^{12}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**8/(a + b*x**4)**(5/4)` | $\frac{x^{8}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**4/(a + b*x**4)**(5/4)` | $\frac{x^{4}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(-5/4)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| SOLVED-both | parametric | `1/(x**4*(a + b*x**4)**(5/4))` | $\frac{1}{x^{4} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| SOLVED-both | parametric | `1/(x**8*(a + b*x**4)**(5/4))` | $\frac{1}{x^{8} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| SOLVED-both | parametric | `1/(x**12*(a + b*x**4)**(5/4))` | $\frac{1}{x^{12} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| SOLVED-both | parametric | `1/(x**16*(a + b*x**4)**(5/4))` | $\frac{1}{x^{16} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**14/(a + b*x**4)**(5/4)` | $\frac{x^{14}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**10/(a + b*x**4)**(5/4)` | $\frac{x^{10}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**6/(a + b*x**4)**(5/4)` | $\frac{x^{6}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**2/(a + b*x**4)**(5/4)` | $\frac{x^{2}}{\left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**4)**(5/4))` | $\frac{1}{x^{2} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**6*(a + b*x**4)**(5/4))` | $\frac{1}{x^{6} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**10*(a + b*x**4)**(5/4))` | $\frac{1}{x^{10} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/(x**14*(a + b*x**4)**(5/4))` | $\frac{1}{x^{14} \left(a + b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(a + b*x**4)**(-7/4)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{7}{4}}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(-9/4)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(a + b*x**4)**(-11/4)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{11}{4}}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(-13/4)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{13}{4}}}$ |
| SOLVED-both | parametric | `(a + b*x**4)**(-17/4)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{17}{4}}}$ |
| SOLVED-both | parametric | `x**19*(a - b*x**4)**(1/4)` | $x^{19} \sqrt[4]{a - b x^{4}}$ |
| SOLVED-both | parametric | `x**15*(a - b*x**4)**(1/4)` | $x^{15} \sqrt[4]{a - b x^{4}}$ |
| SOLVED-both | parametric | `x**11*(a - b*x**4)**(1/4)` | $x^{11} \sqrt[4]{a - b x^{4}}$ |
| SOLVED-both | parametric | `x**7*(a - b*x**4)**(1/4)` | $x^{7} \sqrt[4]{a - b x^{4}}$ |
| SOLVED-both | parametric | `x**3*(a - b*x**4)**(1/4)` | $x^{3} \sqrt[4]{a - b x^{4}}$ |
| partial | parametric | `(a - b*x**4)**(1/4)/x` | $\frac{\sqrt[4]{a - b x^{4}}}{x}$ |
| partial | parametric | `(a - b*x**4)**(1/4)/x**5` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{5}}$ |
| partial | parametric | `(a - b*x**4)**(1/4)/x**9` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{9}}$ |
| partial | parametric | `x**9*(a - b*x**4)**(1/4)` | $x^{9} \sqrt[4]{a - b x^{4}}$ |
| partial | parametric | `x**5*(a - b*x**4)**(1/4)` | $x^{5} \sqrt[4]{a - b x^{4}}$ |
| partial | parametric | `x*(a - b*x**4)**(1/4)` | $x \sqrt[4]{a - b x^{4}}$ |
| partial | parametric | `(a - b*x**4)**(1/4)/x**3` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{3}}$ |
| partial | parametric | `(a - b*x**4)**(1/4)/x**7` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{7}}$ |
| partial | parametric | `(a - b*x**4)**(1/4)/x**11` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{11}}$ |
| partial | parametric | `x**6*(a - b*x**4)**(1/4)` | $x^{6} \sqrt[4]{a - b x^{4}}$ |
| partial | parametric | `x**2*(a - b*x**4)**(1/4)` | $x^{2} \sqrt[4]{a - b x^{4}}$ |
| partial | parametric | `(a - b*x**4)**(1/4)/x**2` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{2}}$ |
| SOLVED-both | parametric | `(a - b*x**4)**(1/4)/x**6` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{6}}$ |
| SOLVED-both | parametric | `(a - b*x**4)**(1/4)/x**10` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{10}}$ |
| SOLVED-both | parametric | `(a - b*x**4)**(1/4)/x**14` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{14}}$ |
| SOLVED-both | parametric | `(a - b*x**4)**(1/4)/x**18` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{18}}$ |
| partial | parametric | `x**12*(a - b*x**4)**(1/4)` | $x^{12} \sqrt[4]{a - b x^{4}}$ |
| partial | parametric | `x**8*(a - b*x**4)**(1/4)` | $x^{8} \sqrt[4]{a - b x^{4}}$ |
| partial | parametric | `x**4*(a - b*x**4)**(1/4)` | $x^{4} \sqrt[4]{a - b x^{4}}$ |
| partial | parametric | `(a - b*x**4)**(1/4)` | $\sqrt[4]{a - b x^{4}}$ |
| partial | parametric | `(a - b*x**4)**(1/4)/x**4` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{4}}$ |
| partial | parametric | `(a - b*x**4)**(1/4)/x**8` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{8}}$ |
| partial | parametric | `(a - b*x**4)**(1/4)/x**12` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{12}}$ |
| partial | parametric | `(a - b*x**4)**(1/4)/x**16` | $\frac{\sqrt[4]{a - b x^{4}}}{x^{16}}$ |
| SOLVED-both | parametric | `x**19/(a - b*x**4)**(1/4)` | $\frac{x^{19}}{\sqrt[4]{a - b x^{4}}}$ |
| SOLVED-both | parametric | `x**15/(a - b*x**4)**(1/4)` | $\frac{x^{15}}{\sqrt[4]{a - b x^{4}}}$ |
| SOLVED-both | parametric | `x**11/(a - b*x**4)**(1/4)` | $\frac{x^{11}}{\sqrt[4]{a - b x^{4}}}$ |
| SOLVED-both | parametric | `x**7/(a - b*x**4)**(1/4)` | $\frac{x^{7}}{\sqrt[4]{a - b x^{4}}}$ |
| SOLVED-both | parametric | `x**3/(a - b*x**4)**(1/4)` | $\frac{x^{3}}{\sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `1/(x*(a - b*x**4)**(1/4))` | $\frac{1}{x \sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `1/(x**5*(a - b*x**4)**(1/4))` | $\frac{1}{x^{5} \sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `1/(x**9*(a - b*x**4)**(1/4))` | $\frac{1}{x^{9} \sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `x**13/(a - b*x**4)**(1/4)` | $\frac{x^{13}}{\sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `x**9/(a - b*x**4)**(1/4)` | $\frac{x^{9}}{\sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `x**5/(a - b*x**4)**(1/4)` | $\frac{x^{5}}{\sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `x/(a - b*x**4)**(1/4)` | $\frac{x}{\sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `1/(x**3*(a - b*x**4)**(1/4))` | $\frac{1}{x^{3} \sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `1/(x**7*(a - b*x**4)**(1/4))` | $\frac{1}{x^{7} \sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `1/(x**11*(a - b*x**4)**(1/4))` | $\frac{1}{x^{11} \sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `x**8/(a - b*x**4)**(1/4)` | $\frac{x^{8}}{\sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `x**4/(a - b*x**4)**(1/4)` | $\frac{x^{4}}{\sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `(a - b*x**4)**(-1/4)` | $\frac{1}{\sqrt[4]{a - b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**4*(a - b*x**4)**(1/4))` | $\frac{1}{x^{4} \sqrt[4]{a - b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**8*(a - b*x**4)**(1/4))` | $\frac{1}{x^{8} \sqrt[4]{a - b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**12*(a - b*x**4)**(1/4))` | $\frac{1}{x^{12} \sqrt[4]{a - b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**16*(a - b*x**4)**(1/4))` | $\frac{1}{x^{16} \sqrt[4]{a - b x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**20*(a - b*x**4)**(1/4))` | $\frac{1}{x^{20} \sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `x**10/(a - b*x**4)**(1/4)` | $\frac{x^{10}}{\sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `x**6/(a - b*x**4)**(1/4)` | $\frac{x^{6}}{\sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `x**2/(a - b*x**4)**(1/4)` | $\frac{x^{2}}{\sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `1/(x**2*(a - b*x**4)**(1/4))` | $\frac{1}{x^{2} \sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `1/(x**6*(a - b*x**4)**(1/4))` | $\frac{1}{x^{6} \sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `1/(x**10*(a - b*x**4)**(1/4))` | $\frac{1}{x^{10} \sqrt[4]{a - b x^{4}}}$ |
| partial | parametric | `1/(x**14*(a - b*x**4)**(1/4))` | $\frac{1}{x^{14} \sqrt[4]{a - b x^{4}}}$ |
| SOLVED-both | parametric | `x**19/(a - b*x**4)**(3/4)` | $\frac{x^{19}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `x**15/(a - b*x**4)**(3/4)` | $\frac{x^{15}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `x**11/(a - b*x**4)**(3/4)` | $\frac{x^{11}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `x**7/(a - b*x**4)**(3/4)` | $\frac{x^{7}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `x**3/(a - b*x**4)**(3/4)` | $\frac{x^{3}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x*(a - b*x**4)**(3/4))` | $\frac{1}{x \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**5*(a - b*x**4)**(3/4))` | $\frac{1}{x^{5} \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**9*(a - b*x**4)**(3/4))` | $\frac{1}{x^{9} \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**13/(a - b*x**4)**(3/4)` | $\frac{x^{13}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**9/(a - b*x**4)**(3/4)` | $\frac{x^{9}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**5/(a - b*x**4)**(3/4)` | $\frac{x^{5}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x/(a - b*x**4)**(3/4)` | $\frac{x}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**3*(a - b*x**4)**(3/4))` | $\frac{1}{x^{3} \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**7*(a - b*x**4)**(3/4))` | $\frac{1}{x^{7} \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**11*(a - b*x**4)**(3/4))` | $\frac{1}{x^{11} \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**10/(a - b*x**4)**(3/4)` | $\frac{x^{10}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**6/(a - b*x**4)**(3/4)` | $\frac{x^{6}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**2/(a - b*x**4)**(3/4)` | $\frac{x^{2}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `1/(x**2*(a - b*x**4)**(3/4))` | $\frac{1}{x^{2} \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `1/(x**6*(a - b*x**4)**(3/4))` | $\frac{1}{x^{6} \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `1/(x**10*(a - b*x**4)**(3/4))` | $\frac{1}{x^{10} \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| SOLVED-both | parametric | `1/(x**14*(a - b*x**4)**(3/4))` | $\frac{1}{x^{14} \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**12/(a - b*x**4)**(3/4)` | $\frac{x^{12}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**8/(a - b*x**4)**(3/4)` | $\frac{x^{8}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**4/(a - b*x**4)**(3/4)` | $\frac{x^{4}}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(a - b*x**4)**(-3/4)` | $\frac{1}{\left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**4*(a - b*x**4)**(3/4))` | $\frac{1}{x^{4} \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**8*(a - b*x**4)**(3/4))` | $\frac{1}{x^{8} \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/(x**12*(a - b*x**4)**(3/4))` | $\frac{1}{x^{12} \left(a - b x^{4}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `x**2/(a - b*x**4)**(5/4)` | $\frac{x^{2}}{\left(a - b x^{4}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `x**(23/2)/sqrt(a + b*x**5)` | $\frac{x^{\frac{23}{2}}}{\sqrt{a + b x^{5}}}$ |
| partial | parametric | `x**(13/2)/sqrt(a + b*x**5)` | $\frac{x^{\frac{13}{2}}}{\sqrt{a + b x^{5}}}$ |
| partial | parametric | `x**(3/2)/sqrt(a + b*x**5)` | $\frac{x^{\frac{3}{2}}}{\sqrt{a + b x^{5}}}$ |
| SOLVED-both | parametric | `1/(x**(7/2)*sqrt(a + b*x**5))` | $\frac{1}{x^{\frac{7}{2}} \sqrt{a + b x^{5}}}$ |
| SOLVED-both | parametric | `1/(x**(17/2)*sqrt(a + b*x**5))` | $\frac{1}{x^{\frac{17}{2}} \sqrt{a + b x^{5}}}$ |
| partial | concrete | `x**(23/2)/sqrt(x**5 + 1)` | $\frac{x^{\frac{23}{2}}}{\sqrt{x^{5} + 1}}$ |
| partial | concrete | `x**(13/2)/sqrt(x**5 + 1)` | $\frac{x^{\frac{13}{2}}}{\sqrt{x^{5} + 1}}$ |
| partial | concrete | `x**(3/2)/sqrt(x**5 + 1)` | $\frac{x^{\frac{3}{2}}}{\sqrt{x^{5} + 1}}$ |
| SOLVED-both | concrete | `1/(x**(7/2)*sqrt(x**5 + 1))` | $\frac{1}{x^{\frac{7}{2}} \sqrt{x^{5} + 1}}$ |
| SOLVED-both | concrete | `1/(x**(17/2)*sqrt(x**5 + 1))` | $\frac{1}{x^{\frac{17}{2}} \sqrt{x^{5} + 1}}$ |
| partial | concrete | `x**(1/3)/(1 - x**6)` | $\frac{\sqrt[3]{x}}{1 - x^{6}}$ |
| partial | concrete | `x**8*sqrt(4*x**6 - 1)` | $x^{8} \sqrt{4 x^{6} - 1}$ |
| SOLVED-both | parametric | `x**5*sqrt(a**6 - x**6)` | $x^{5} \sqrt{a^{6} - x^{6}}$ |
| partial | concrete | `x**2*sqrt(x**6 - 2)` | $x^{2} \sqrt{x^{6} - 2}$ |
| SOLVED-both | concrete | `x**23/sqrt(x**6 + 2)` | $\frac{x^{23}}{\sqrt{x^{6} + 2}}$ |
| SOLVED-both | concrete | `x**17/sqrt(x**6 + 2)` | $\frac{x^{17}}{\sqrt{x^{6} + 2}}$ |
| SOLVED-both | concrete | `x**11/sqrt(x**6 + 2)` | $\frac{x^{11}}{\sqrt{x^{6} + 2}}$ |
| SOLVED-both | concrete | `x**5/sqrt(x**6 + 2)` | $\frac{x^{5}}{\sqrt{x^{6} + 2}}$ |
| partial | concrete | `1/(x*sqrt(x**6 + 2))` | $\frac{1}{x \sqrt{x^{6} + 2}}$ |
| partial | concrete | `1/(x**7*sqrt(x**6 + 2))` | $\frac{1}{x^{7} \sqrt{x^{6} + 2}}$ |
| partial | concrete | `1/(x**13*sqrt(x**6 + 2))` | $\frac{1}{x^{13} \sqrt{x^{6} + 2}}$ |
| partial | concrete | `x**14/sqrt(x**6 + 2)` | $\frac{x^{14}}{\sqrt{x^{6} + 2}}$ |
| partial | concrete | `x**8/sqrt(x**6 + 2)` | $\frac{x^{8}}{\sqrt{x^{6} + 2}}$ |
| partial | concrete | `x**2/sqrt(x**6 + 2)` | $\frac{x^{2}}{\sqrt{x^{6} + 2}}$ |
| SOLVED-both | concrete | `1/(x**4*sqrt(x**6 + 2))` | $\frac{1}{x^{4} \sqrt{x^{6} + 2}}$ |
| SOLVED-both | concrete | `1/(x**10*sqrt(x**6 + 2))` | $\frac{1}{x^{10} \sqrt{x^{6} + 2}}$ |
| SOLVED-both | concrete | `1/(x**16*sqrt(x**6 + 2))` | $\frac{1}{x^{16} \sqrt{x^{6} + 2}}$ |
| partial | concrete | `x**7/sqrt(x**6 + 2)` | $\frac{x^{7}}{\sqrt{x^{6} + 2}}$ |
| partial | concrete | `x/sqrt(x**6 + 2)` | $\frac{x}{\sqrt{x^{6} + 2}}$ |
| partial | concrete | `1/(x**5*sqrt(x**6 + 2))` | $\frac{1}{x^{5} \sqrt{x^{6} + 2}}$ |
| partial | concrete | `x**6/sqrt(x**6 + 2)` | $\frac{x^{6}}{\sqrt{x^{6} + 2}}$ |
| partial | concrete | `1/sqrt(x**6 + 2)` | $\frac{1}{\sqrt{x^{6} + 2}}$ |
| partial | concrete | `1/(x**6*sqrt(x**6 + 2))` | $\frac{1}{x^{6} \sqrt{x^{6} + 2}}$ |
| partial | concrete | `x**9/sqrt(x**6 + 2)` | $\frac{x^{9}}{\sqrt{x^{6} + 2}}$ |
| partial | concrete | `x**3/sqrt(x**6 + 2)` | $\frac{x^{3}}{\sqrt{x^{6} + 2}}$ |
| partial | concrete | `1/(x**3*sqrt(x**6 + 2))` | $\frac{1}{x^{3} \sqrt{x^{6} + 2}}$ |
| partial | concrete | `x**10/sqrt(x**6 + 2)` | $\frac{x^{10}}{\sqrt{x^{6} + 2}}$ |
| partial | concrete | `x**4/sqrt(x**6 + 2)` | $\frac{x^{4}}{\sqrt{x^{6} + 2}}$ |
| partial | concrete | `1/(x**2*sqrt(x**6 + 2))` | $\frac{1}{x^{2} \sqrt{x^{6} + 2}}$ |
| SOLVED-both | concrete | `x**23/(x**6 + 2)**(3/2)` | $\frac{x^{23}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x**17/(x**6 + 2)**(3/2)` | $\frac{x^{17}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x**11/(x**6 + 2)**(3/2)` | $\frac{x^{11}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x**5/(x**6 + 2)**(3/2)` | $\frac{x^{5}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x*(x**6 + 2)**(3/2))` | $\frac{1}{x \left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**7*(x**6 + 2)**(3/2))` | $\frac{1}{x^{7} \left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**13*(x**6 + 2)**(3/2))` | $\frac{1}{x^{13} \left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**14/(x**6 + 2)**(3/2)` | $\frac{x^{14}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**8/(x**6 + 2)**(3/2)` | $\frac{x^{8}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x**2/(x**6 + 2)**(3/2)` | $\frac{x^{2}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/(x**4*(x**6 + 2)**(3/2))` | $\frac{1}{x^{4} \left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `1/(x**10*(x**6 + 2)**(3/2))` | $\frac{1}{x^{10} \left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**13/(x**6 + 2)**(3/2)` | $\frac{x^{13}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**7/(x**6 + 2)**(3/2)` | $\frac{x^{7}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x/(x**6 + 2)**(3/2)` | $\frac{x}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**5*(x**6 + 2)**(3/2))` | $\frac{1}{x^{5} \left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**12/(x**6 + 2)**(3/2)` | $\frac{x^{12}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**6/(x**6 + 2)**(3/2)` | $\frac{x^{6}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x**6 + 2)**(-3/2)` | $\frac{1}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**6*(x**6 + 2)**(3/2))` | $\frac{1}{x^{6} \left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**15/(x**6 + 2)**(3/2)` | $\frac{x^{15}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**9/(x**6 + 2)**(3/2)` | $\frac{x^{9}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**3/(x**6 + 2)**(3/2)` | $\frac{x^{3}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**3*(x**6 + 2)**(3/2))` | $\frac{1}{x^{3} \left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**10/(x**6 + 2)**(3/2)` | $\frac{x^{10}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**4/(x**6 + 2)**(3/2)` | $\frac{x^{4}}{\left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**2*(x**6 + 2)**(3/2))` | $\frac{1}{x^{2} \left(x^{6} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**3*sqrt(x**8 + 1)` | $x^{3} \sqrt{x^{8} + 1}$ |
| partial | concrete | `x*sqrt(x**8 + 1)` | $x \sqrt{x^{8} + 1}$ |
| partial | concrete | `sqrt(x**8 + 1)/x` | $\frac{\sqrt{x^{8} + 1}}{x}$ |
| partial | concrete | `sqrt(x**8 + 1)/x**3` | $\frac{\sqrt{x^{8} + 1}}{x^{3}}$ |
| partial | concrete | `x**3*sqrt(x**8 - 2)` | $x^{3} \sqrt{x^{8} - 2}$ |
| partial | concrete | `x**19/sqrt(x**8 + 1)` | $\frac{x^{19}}{\sqrt{x^{8} + 1}}$ |
| SOLVED-both | concrete | `x**15/sqrt(x**8 + 1)` | $\frac{x^{15}}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `x**11/sqrt(x**8 + 1)` | $\frac{x^{11}}{\sqrt{x^{8} + 1}}$ |
| SOLVED-both | concrete | `x**7/sqrt(x**8 + 1)` | $\frac{x^{7}}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `x**3/sqrt(x**8 + 1)` | $\frac{x^{3}}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `1/(x*sqrt(x**8 + 1))` | $\frac{1}{x \sqrt{x^{8} + 1}}$ |
| SOLVED-both | concrete | `1/(x**5*sqrt(x**8 + 1))` | $\frac{1}{x^{5} \sqrt{x^{8} + 1}}$ |
| partial | concrete | `1/(x**9*sqrt(x**8 + 1))` | $\frac{1}{x^{9} \sqrt{x^{8} + 1}}$ |
| SOLVED-both | concrete | `1/(x**13*sqrt(x**8 + 1))` | $\frac{1}{x^{13} \sqrt{x^{8} + 1}}$ |
| partial | concrete | `1/(x**17*sqrt(x**8 + 1))` | $\frac{1}{x^{17} \sqrt{x^{8} + 1}}$ |
| partial | concrete | `x**13/sqrt(x**8 + 1)` | $\frac{x^{13}}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `x**9/sqrt(x**8 + 1)` | $\frac{x^{9}}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `x**5/sqrt(x**8 + 1)` | $\frac{x^{5}}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `x/sqrt(x**8 + 1)` | $\frac{x}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `1/(x**3*sqrt(x**8 + 1))` | $\frac{1}{x^{3} \sqrt{x^{8} + 1}}$ |
| partial | concrete | `1/(x**7*sqrt(x**8 + 1))` | $\frac{1}{x^{7} \sqrt{x^{8} + 1}}$ |
| partial | concrete | `x**10/sqrt(x**8 + 1)` | $\frac{x^{10}}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `x**8/sqrt(x**8 + 1)` | $\frac{x^{8}}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `x**6/sqrt(x**8 + 1)` | $\frac{x^{6}}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `x**4/sqrt(x**8 + 1)` | $\frac{x^{4}}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `x**2/sqrt(x**8 + 1)` | $\frac{x^{2}}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `1/sqrt(x**8 + 1)` | $\frac{1}{\sqrt{x^{8} + 1}}$ |
| partial | concrete | `1/(x**2*sqrt(x**8 + 1))` | $\frac{1}{x^{2} \sqrt{x^{8} + 1}}$ |
| partial | concrete | `1/(x**4*sqrt(x**8 + 1))` | $\frac{1}{x^{4} \sqrt{x^{8} + 1}}$ |
| partial | concrete | `1/(x**6*sqrt(x**8 + 1))` | $\frac{1}{x^{6} \sqrt{x^{8} + 1}}$ |
| partial | concrete | `1/(x**8*sqrt(x**8 + 1))` | $\frac{1}{x^{8} \sqrt{x^{8} + 1}}$ |
| partial | concrete | `x**4/sqrt(1 - x**10)` | $\frac{x^{4}}{\sqrt{1 - x^{10}}}$ |
| partial | concrete | `x**4/sqrt(x**10 - 2)` | $\frac{x^{4}}{\sqrt{x^{10} - 2}}$ |
| partial | concrete | `x**5*sqrt(x**12 + 9)` | $x^{5} \sqrt{x^{12} + 9}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b/x)` | $x^{\frac{5}{2}} \left(a + \frac{b}{x}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b/x)` | $x^{\frac{3}{2}} \left(a + \frac{b}{x}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b/x)` | $\sqrt{x} \left(a + \frac{b}{x}\right)$ |
| SOLVED-both | parametric | `(a + b/x)/sqrt(x)` | $\frac{a + \frac{b}{x}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b/x)/x**(3/2)` | $\frac{a + \frac{b}{x}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b/x)/x**(5/2)` | $\frac{a + \frac{b}{x}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b/x)**2` | $x^{\frac{5}{2}} \left(a + \frac{b}{x}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b/x)**2` | $x^{\frac{3}{2}} \left(a + \frac{b}{x}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b/x)**2` | $\sqrt{x} \left(a + \frac{b}{x}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b/x)**2/sqrt(x)` | $\frac{\left(a + \frac{b}{x}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b/x)**2/x**(3/2)` | $\frac{\left(a + \frac{b}{x}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b/x)**2/x**(5/2)` | $\frac{\left(a + \frac{b}{x}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b/x)**3` | $x^{\frac{5}{2}} \left(a + \frac{b}{x}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b/x)**3` | $x^{\frac{3}{2}} \left(a + \frac{b}{x}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b/x)**3` | $\sqrt{x} \left(a + \frac{b}{x}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b/x)**3/sqrt(x)` | $\frac{\left(a + \frac{b}{x}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b/x)**3/x**(3/2)` | $\frac{\left(a + \frac{b}{x}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b/x)**3/x**(5/2)` | $\frac{\left(a + \frac{b}{x}\right)^{3}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)/(a + b/x)` | $\frac{x^{\frac{5}{2}}}{a + \frac{b}{x}}$ |
| partial | parametric | `x**(3/2)/(a + b/x)` | $\frac{x^{\frac{3}{2}}}{a + \frac{b}{x}}$ |
| partial | parametric | `sqrt(x)/(a + b/x)` | $\frac{\sqrt{x}}{a + \frac{b}{x}}$ |
| partial | parametric | `1/(sqrt(x)*(a + b/x))` | $\frac{1}{\sqrt{x} \left(a + \frac{b}{x}\right)}$ |
| partial | parametric | `1/(x**(3/2)*(a + b/x))` | $\frac{1}{x^{\frac{3}{2}} \left(a + \frac{b}{x}\right)}$ |
| partial | parametric | `1/(x**(5/2)*(a + b/x))` | $\frac{1}{x^{\frac{5}{2}} \left(a + \frac{b}{x}\right)}$ |
| partial | parametric | `1/(x**(7/2)*(a + b/x))` | $\frac{1}{x^{\frac{7}{2}} \left(a + \frac{b}{x}\right)}$ |
| partial | parametric | `1/(x**(9/2)*(a + b/x))` | $\frac{1}{x^{\frac{9}{2}} \left(a + \frac{b}{x}\right)}$ |
| partial | parametric | `x**(5/2)/(a + b/x)**2` | $\frac{x^{\frac{5}{2}}}{\left(a + \frac{b}{x}\right)^{2}}$ |
| partial | parametric | `x**(3/2)/(a + b/x)**2` | $\frac{x^{\frac{3}{2}}}{\left(a + \frac{b}{x}\right)^{2}}$ |
| partial | parametric | `sqrt(x)/(a + b/x)**2` | $\frac{\sqrt{x}}{\left(a + \frac{b}{x}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(x)*(a + b/x)**2)` | $\frac{1}{\sqrt{x} \left(a + \frac{b}{x}\right)^{2}}$ |
| partial | parametric | `1/(x**(3/2)*(a + b/x)**2)` | $\frac{1}{x^{\frac{3}{2}} \left(a + \frac{b}{x}\right)^{2}}$ |
| partial | parametric | `1/(x**(5/2)*(a + b/x)**2)` | $\frac{1}{x^{\frac{5}{2}} \left(a + \frac{b}{x}\right)^{2}}$ |
| partial | parametric | `1/(x**(7/2)*(a + b/x)**2)` | $\frac{1}{x^{\frac{7}{2}} \left(a + \frac{b}{x}\right)^{2}}$ |
| partial | parametric | `1/(x**(9/2)*(a + b/x)**2)` | $\frac{1}{x^{\frac{9}{2}} \left(a + \frac{b}{x}\right)^{2}}$ |
| partial | parametric | `1/(x**(11/2)*(a + b/x)**2)` | $\frac{1}{x^{\frac{11}{2}} \left(a + \frac{b}{x}\right)^{2}}$ |
| partial | parametric | `x**(3/2)/(a + b/x)**3` | $\frac{x^{\frac{3}{2}}}{\left(a + \frac{b}{x}\right)^{3}}$ |
| partial | parametric | `sqrt(x)/(a + b/x)**3` | $\frac{\sqrt{x}}{\left(a + \frac{b}{x}\right)^{3}}$ |
| partial | parametric | `1/(sqrt(x)*(a + b/x)**3)` | $\frac{1}{\sqrt{x} \left(a + \frac{b}{x}\right)^{3}}$ |
| partial | parametric | `1/(x**(3/2)*(a + b/x)**3)` | $\frac{1}{x^{\frac{3}{2}} \left(a + \frac{b}{x}\right)^{3}}$ |
| partial | parametric | `1/(x**(5/2)*(a + b/x)**3)` | $\frac{1}{x^{\frac{5}{2}} \left(a + \frac{b}{x}\right)^{3}}$ |
| partial | parametric | `1/(x**(7/2)*(a + b/x)**3)` | $\frac{1}{x^{\frac{7}{2}} \left(a + \frac{b}{x}\right)^{3}}$ |
| partial | parametric | `1/(x**(9/2)*(a + b/x)**3)` | $\frac{1}{x^{\frac{9}{2}} \left(a + \frac{b}{x}\right)^{3}}$ |
| partial | parametric | `1/(x**(11/2)*(a + b/x)**3)` | $\frac{1}{x^{\frac{11}{2}} \left(a + \frac{b}{x}\right)^{3}}$ |
| partial | parametric | `1/(x**(13/2)*(a + b/x)**3)` | $\frac{1}{x^{\frac{13}{2}} \left(a + \frac{b}{x}\right)^{3}}$ |
| partial | parametric | `x**3*sqrt(a + b/x)` | $x^{3} \sqrt{a + \frac{b}{x}}$ |
| partial | parametric | `x**2*sqrt(a + b/x)` | $x^{2} \sqrt{a + \frac{b}{x}}$ |
| partial | parametric | `x*sqrt(a + b/x)` | $x \sqrt{a + \frac{b}{x}}$ |
| partial | parametric | `sqrt(a + b/x)` | $\sqrt{a + \frac{b}{x}}$ |
| partial | parametric | `sqrt(a + b/x)/x` | $\frac{\sqrt{a + \frac{b}{x}}}{x}$ |
| SOLVED-both | parametric | `sqrt(a + b/x)/x**2` | $\frac{\sqrt{a + \frac{b}{x}}}{x^{2}}$ |
| SOLVED-both | parametric | `sqrt(a + b/x)/x**3` | $\frac{\sqrt{a + \frac{b}{x}}}{x^{3}}$ |
| SOLVED-both | parametric | `sqrt(a + b/x)/x**4` | $\frac{\sqrt{a + \frac{b}{x}}}{x^{4}}$ |
| SOLVED-both | parametric | `sqrt(a + b/x)/x**5` | $\frac{\sqrt{a + \frac{b}{x}}}{x^{5}}$ |
| SOLVED-both | parametric | `sqrt(a + b/x)/x**6` | $\frac{\sqrt{a + \frac{b}{x}}}{x^{6}}$ |
| partial | parametric | `x**3*(a + b/x)**(3/2)` | $x^{3} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(a + b/x)**(3/2)` | $x^{2} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a + b/x)**(3/2)` | $x \left(a + \frac{b}{x}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x)**(3/2)` | $\left(a + \frac{b}{x}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x)**(3/2)/x` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{x}$ |
| SOLVED-both | parametric | `(a + b/x)**(3/2)/x**2` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b/x)**(3/2)/x**3` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b/x)**(3/2)/x**4` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b/x)**(3/2)/x**5` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{x^{5}}$ |
| SOLVED-both | parametric | `(a + b/x)**(3/2)/x**6` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b/x)**(3/2)/x**7` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `x**3*(a + b/x)**(5/2)` | $x^{3} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**2*(a + b/x)**(5/2)` | $x^{2} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x*(a + b/x)**(5/2)` | $x \left(a + \frac{b}{x}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b/x)**(5/2)` | $\left(a + \frac{b}{x}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b/x)**(5/2)/x` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}{x}$ |
| SOLVED-both | parametric | `(a + b/x)**(5/2)/x**2` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b/x)**(5/2)/x**3` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b/x)**(5/2)/x**4` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b/x)**(5/2)/x**5` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}{x^{5}}$ |
| SOLVED-both | parametric | `(a + b/x)**(5/2)/x**6` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}{x^{6}}$ |
| partial | parametric | `x**3/sqrt(a + b/x)` | $\frac{x^{3}}{\sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `x**2/sqrt(a + b/x)` | $\frac{x^{2}}{\sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `x/sqrt(a + b/x)` | $\frac{x}{\sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `1/sqrt(a + b/x)` | $\frac{1}{\sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `1/(x*sqrt(a + b/x))` | $\frac{1}{x \sqrt{a + \frac{b}{x}}}$ |
| SOLVED-both | parametric | `1/(x**2*sqrt(a + b/x))` | $\frac{1}{x^{2} \sqrt{a + \frac{b}{x}}}$ |
| SOLVED-both | parametric | `1/(x**3*sqrt(a + b/x))` | $\frac{1}{x^{3} \sqrt{a + \frac{b}{x}}}$ |
| SOLVED-both | parametric | `1/(x**4*sqrt(a + b/x))` | $\frac{1}{x^{4} \sqrt{a + \frac{b}{x}}}$ |
| SOLVED-both | parametric | `1/(x**5*sqrt(a + b/x))` | $\frac{1}{x^{5} \sqrt{a + \frac{b}{x}}}$ |
| SOLVED-both | parametric | `1/(x**6*sqrt(a + b/x))` | $\frac{1}{x^{6} \sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `x**2/(a + b/x)**(3/2)` | $\frac{x^{2}}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a + b/x)**(3/2)` | $\frac{x}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x)**(-3/2)` | $\frac{1}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b/x)**(3/2))` | $\frac{1}{x \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**2*(a + b/x)**(3/2))` | $\frac{1}{x^{2} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**3*(a + b/x)**(3/2))` | $\frac{1}{x^{3} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**4*(a + b/x)**(3/2))` | $\frac{1}{x^{4} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**5*(a + b/x)**(3/2))` | $\frac{1}{x^{5} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**6*(a + b/x)**(3/2))` | $\frac{1}{x^{6} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**7*(a + b/x)**(3/2))` | $\frac{1}{x^{7} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a + b/x)**(5/2)` | $\frac{x^{2}}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x/(a + b/x)**(5/2)` | $\frac{x}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b/x)**(-5/2)` | $\frac{1}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*(a + b/x)**(5/2))` | $\frac{1}{x \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**2*(a + b/x)**(5/2))` | $\frac{1}{x^{2} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**3*(a + b/x)**(5/2))` | $\frac{1}{x^{3} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**4*(a + b/x)**(5/2))` | $\frac{1}{x^{4} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**5*(a + b/x)**(5/2))` | $\frac{1}{x^{5} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**6*(a + b/x)**(5/2))` | $\frac{1}{x^{6} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**7*(a + b/x)**(5/2))` | $\frac{1}{x^{7} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(7/2)*sqrt(a + b/x)` | $x^{\frac{7}{2}} \sqrt{a + \frac{b}{x}}$ |
| partial | parametric | `x**(5/2)*sqrt(a + b/x)` | $x^{\frac{5}{2}} \sqrt{a + \frac{b}{x}}$ |
| SOLVED-both | parametric | `x**(3/2)*sqrt(a + b/x)` | $x^{\frac{3}{2}} \sqrt{a + \frac{b}{x}}$ |
| SOLVED-both | parametric | `sqrt(x)*sqrt(a + b/x)` | $\sqrt{x} \sqrt{a + \frac{b}{x}}$ |
| partial | parametric | `sqrt(a + b/x)/sqrt(x)` | $\frac{\sqrt{a + \frac{b}{x}}}{\sqrt{x}}$ |
| partial | parametric | `sqrt(a + b/x)/x**(3/2)` | $\frac{\sqrt{a + \frac{b}{x}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b/x)/x**(5/2)` | $\frac{\sqrt{a + \frac{b}{x}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(a + b/x)/x**(7/2)` | $\frac{\sqrt{a + \frac{b}{x}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `x**(9/2)*(a + b/x)**(3/2)` | $x^{\frac{9}{2}} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(7/2)*(a + b/x)**(3/2)` | $x^{\frac{7}{2}} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b/x)**(3/2)` | $x^{\frac{5}{2}} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b/x)**(3/2)` | $x^{\frac{3}{2}} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(x)*(a + b/x)**(3/2)` | $\sqrt{x} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x)**(3/2)/sqrt(x)` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(a + b/x)**(3/2)/x**(3/2)` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x)**(3/2)/x**(5/2)` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `x**(11/2)*(a + b/x)**(5/2)` | $x^{\frac{11}{2}} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**(9/2)*(a + b/x)**(5/2)` | $x^{\frac{9}{2}} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**(7/2)*(a + b/x)**(5/2)` | $x^{\frac{7}{2}} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b/x)**(5/2)` | $x^{\frac{5}{2}} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**(3/2)*(a + b/x)**(5/2)` | $x^{\frac{3}{2}} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(x)*(a + b/x)**(5/2)` | $\sqrt{x} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b/x)**(5/2)/sqrt(x)` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(a + b/x)**(5/2)/x**(3/2)` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x)**(5/2)/x**(5/2)` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `x**(7/2)/sqrt(a + b/x)` | $\frac{x^{\frac{7}{2}}}{\sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `x**(5/2)/sqrt(a + b/x)` | $\frac{x^{\frac{5}{2}}}{\sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `x**(3/2)/sqrt(a + b/x)` | $\frac{x^{\frac{3}{2}}}{\sqrt{a + \frac{b}{x}}}$ |
| SOLVED-both | parametric | `sqrt(x)/sqrt(a + b/x)` | $\frac{\sqrt{x}}{\sqrt{a + \frac{b}{x}}}$ |
| SOLVED-both | parametric | `1/(sqrt(x)*sqrt(a + b/x))` | $\frac{1}{\sqrt{x} \sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `1/(x**(3/2)*sqrt(a + b/x))` | $\frac{1}{x^{\frac{3}{2}} \sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `1/(x**(5/2)*sqrt(a + b/x))` | $\frac{1}{x^{\frac{5}{2}} \sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `1/(x**(7/2)*sqrt(a + b/x))` | $\frac{1}{x^{\frac{7}{2}} \sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `1/(x**(9/2)*sqrt(a + b/x))` | $\frac{1}{x^{\frac{9}{2}} \sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `x**(5/2)/(a + b/x)**(3/2)` | $\frac{x^{\frac{5}{2}}}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(3/2)/(a + b/x)**(3/2)` | $\frac{x^{\frac{3}{2}}}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)/(a + b/x)**(3/2)` | $\frac{\sqrt{x}}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(sqrt(x)*(a + b/x)**(3/2))` | $\frac{1}{\sqrt{x} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*(a + b/x)**(3/2))` | $\frac{1}{x^{\frac{3}{2}} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**(5/2)*(a + b/x)**(3/2))` | $\frac{1}{x^{\frac{5}{2}} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**(7/2)*(a + b/x)**(3/2))` | $\frac{1}{x^{\frac{7}{2}} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**(9/2)*(a + b/x)**(3/2))` | $\frac{1}{x^{\frac{9}{2}} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**(11/2)*(a + b/x)**(3/2))` | $\frac{1}{x^{\frac{11}{2}} \left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(5/2)/(a + b/x)**(5/2)` | $\frac{x^{\frac{5}{2}}}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(3/2)/(a + b/x)**(5/2)` | $\frac{x^{\frac{3}{2}}}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(x)/(a + b/x)**(5/2)` | $\frac{\sqrt{x}}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(x)*(a + b/x)**(5/2))` | $\frac{1}{\sqrt{x} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(3/2)*(a + b/x)**(5/2))` | $\frac{1}{x^{\frac{3}{2}} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**(5/2)*(a + b/x)**(5/2))` | $\frac{1}{x^{\frac{5}{2}} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**(7/2)*(a + b/x)**(5/2))` | $\frac{1}{x^{\frac{7}{2}} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**(9/2)*(a + b/x)**(5/2))` | $\frac{1}{x^{\frac{9}{2}} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**(11/2)*(a + b/x)**(5/2))` | $\frac{1}{x^{\frac{11}{2}} \left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3*sqrt(a + b/x**2)` | $x^{3} \sqrt{a + \frac{b}{x^{2}}}$ |
| SOLVED-both | parametric | `x**2*sqrt(a + b/x**2)` | $x^{2} \sqrt{a + \frac{b}{x^{2}}}$ |
| partial | parametric | `x*sqrt(a + b/x**2)` | $x \sqrt{a + \frac{b}{x^{2}}}$ |
| partial | parametric | `sqrt(a + b/x**2)` | $\sqrt{a + \frac{b}{x^{2}}}$ |
| partial | parametric | `sqrt(a + b/x**2)/x` | $\frac{\sqrt{a + \frac{b}{x^{2}}}}{x}$ |
| partial | parametric | `sqrt(a + b/x**2)/x**2` | $\frac{\sqrt{a + \frac{b}{x^{2}}}}{x^{2}}$ |
| SOLVED-both | parametric | `sqrt(a + b/x**2)/x**3` | $\frac{\sqrt{a + \frac{b}{x^{2}}}}{x^{3}}$ |
| partial | parametric | `sqrt(a + b/x**2)/x**4` | $\frac{\sqrt{a + \frac{b}{x^{2}}}}{x^{4}}$ |
| partial | parametric | `x**3*(a + b/x**2)**(3/2)` | $x^{3} \left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(a + b/x**2)**(3/2)` | $x^{2} \left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a + b/x**2)**(3/2)` | $x \left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x**2)**(3/2)` | $\left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x**2)**(3/2)/x` | $\frac{\left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a + b/x**2)**(3/2)/x**2` | $\frac{\left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b/x**2)**(3/2)/x**3` | $\frac{\left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b/x**2)**(3/2)/x**4` | $\frac{\left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `x**3*(a + b/x**2)**(5/2)` | $x^{3} \left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**2*(a + b/x**2)**(5/2)` | $x^{2} \left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x*(a + b/x**2)**(5/2)` | $x \left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b/x**2)**(5/2)` | $\left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b/x**2)**(5/2)/x` | $\frac{\left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(a + b/x**2)**(5/2)/x**2` | $\frac{\left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b/x**2)**(5/2)/x**3` | $\frac{\left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b/x**2)**(5/2)/x**4` | $\frac{\left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `x**3/sqrt(a + b/x**2)` | $\frac{x^{3}}{\sqrt{a + \frac{b}{x^{2}}}}$ |
| partial | parametric | `x/sqrt(a + b/x**2)` | $\frac{x}{\sqrt{a + \frac{b}{x^{2}}}}$ |
| partial | parametric | `1/(x*sqrt(a + b/x**2))` | $\frac{1}{x \sqrt{a + \frac{b}{x^{2}}}}$ |
| SOLVED-both | parametric | `1/(x**3*sqrt(a + b/x**2))` | $\frac{1}{x^{3} \sqrt{a + \frac{b}{x^{2}}}}$ |
| SOLVED-both | parametric | `1/(x**5*sqrt(a + b/x**2))` | $\frac{1}{x^{5} \sqrt{a + \frac{b}{x^{2}}}}$ |
| SOLVED-both | parametric | `1/(x**7*sqrt(a + b/x**2))` | $\frac{1}{x^{7} \sqrt{a + \frac{b}{x^{2}}}}$ |
| SOLVED-both | parametric | `1/(x**9*sqrt(a + b/x**2))` | $\frac{1}{x^{9} \sqrt{a + \frac{b}{x^{2}}}}$ |
| SOLVED-both | parametric | `x**4/sqrt(a + b/x**2)` | $\frac{x^{4}}{\sqrt{a + \frac{b}{x^{2}}}}$ |
| SOLVED-both | parametric | `x**2/sqrt(a + b/x**2)` | $\frac{x^{2}}{\sqrt{a + \frac{b}{x^{2}}}}$ |
| SOLVED-both | parametric | `1/sqrt(a + b/x**2)` | $\frac{1}{\sqrt{a + \frac{b}{x^{2}}}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b/x**2))` | $\frac{1}{x^{2} \sqrt{a + \frac{b}{x^{2}}}}$ |
| partial | parametric | `1/(x**4*sqrt(a + b/x**2))` | $\frac{1}{x^{4} \sqrt{a + \frac{b}{x^{2}}}}$ |
| partial | parametric | `1/(x*sqrt(-a + b/x**2))` | $\frac{1}{x \sqrt{- a + \frac{b}{x^{2}}}}$ |
| partial | parametric | `1/(x**2*sqrt(b/x**2 + 2))` | $\frac{1}{x^{2} \sqrt{\frac{b}{x^{2}} + 2}}$ |
| partial | parametric | `1/(x**2*sqrt(-b/x**2 + 2))` | $\frac{1}{x^{2} \sqrt{- \frac{b}{x^{2}} + 2}}$ |
| partial | parametric | `x**3/(a + b/x**2)**(3/2)` | $\frac{x^{3}}{\left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a + b/x**2)**(3/2)` | $\frac{x}{\left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b/x**2)**(3/2))` | $\frac{1}{x \left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**3*(a + b/x**2)**(3/2))` | $\frac{1}{x^{3} \left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**5*(a + b/x**2)**(3/2))` | $\frac{1}{x^{5} \left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**7*(a + b/x**2)**(3/2))` | $\frac{1}{x^{7} \left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**9*(a + b/x**2)**(3/2))` | $\frac{1}{x^{9} \left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/(a + b/x**2)**(3/2)` | $\frac{x^{4}}{\left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a + b/x**2)**(3/2)` | $\frac{x^{2}}{\left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x**2)**(-3/2)` | $\frac{1}{\left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b/x**2)**(3/2))` | $\frac{1}{x^{2} \left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b/x**2)**(3/2))` | $\frac{1}{x^{4} \left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**6*(a + b/x**2)**(3/2))` | $\frac{1}{x^{6} \left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**8*(a + b/x**2)**(3/2))` | $\frac{1}{x^{8} \left(a + \frac{b}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/(a + b/x**2)**(5/2)` | $\frac{x^{3}}{\left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x/(a + b/x**2)**(5/2)` | $\frac{x}{\left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*(a + b/x**2)**(5/2))` | $\frac{1}{x \left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**3*(a + b/x**2)**(5/2))` | $\frac{1}{x^{3} \left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**5*(a + b/x**2)**(5/2))` | $\frac{1}{x^{5} \left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**7*(a + b/x**2)**(5/2))` | $\frac{1}{x^{7} \left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(x**9*(a + b/x**2)**(5/2))` | $\frac{1}{x^{9} \left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2/(a + b/x**2)**(5/2)` | $\frac{x^{2}}{\left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b/x**2)**(-5/2)` | $\frac{1}{\left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b/x**2)**(5/2))` | $\frac{1}{x^{2} \left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b/x**2)**(5/2))` | $\frac{1}{x^{4} \left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**6*(a + b/x**2)**(5/2))` | $\frac{1}{x^{6} \left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**8*(a + b/x**2)**(5/2))` | $\frac{1}{x^{8} \left(a + \frac{b}{x^{2}}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(1 + x**(-2))**(1/3)/x**3` | $\frac{\sqrt[3]{1 + \frac{1}{x^{2}}}}{x^{3}}$ |
| SOLVED-both | concrete | `(1 + x**(-2))**(5/3)/x**3` | $\frac{\left(1 + \frac{1}{x^{2}}\right)^{\frac{5}{3}}}{x^{3}}$ |
| partial | parametric | `x**5*sqrt(a + b/x**3)` | $x^{5} \sqrt{a + \frac{b}{x^{3}}}$ |
| partial | parametric | `x**2*sqrt(a + b/x**3)` | $x^{2} \sqrt{a + \frac{b}{x^{3}}}$ |
| partial | parametric | `sqrt(a + b/x**3)/x` | $\frac{\sqrt{a + \frac{b}{x^{3}}}}{x}$ |
| SOLVED-both | parametric | `sqrt(a + b/x**3)/x**4` | $\frac{\sqrt{a + \frac{b}{x^{3}}}}{x^{4}}$ |
| SOLVED-both | parametric | `sqrt(a + b/x**3)/x**7` | $\frac{\sqrt{a + \frac{b}{x^{3}}}}{x^{7}}$ |
| SOLVED-both | parametric | `sqrt(a + b/x**3)/x**10` | $\frac{\sqrt{a + \frac{b}{x^{3}}}}{x^{10}}$ |
| SOLVED-both | parametric | `sqrt(a + b/x**3)/x**13` | $\frac{\sqrt{a + \frac{b}{x^{3}}}}{x^{13}}$ |
| partial | parametric | `x**7*sqrt(a + b/x**3)` | $x^{7} \sqrt{a + \frac{b}{x^{3}}}$ |
| partial | parametric | `x**4*sqrt(a + b/x**3)` | $x^{4} \sqrt{a + \frac{b}{x^{3}}}$ |
| partial | parametric | `x*sqrt(a + b/x**3)` | $x \sqrt{a + \frac{b}{x^{3}}}$ |
| partial | parametric | `sqrt(a + b/x**3)/x**2` | $\frac{\sqrt{a + \frac{b}{x^{3}}}}{x^{2}}$ |
| partial | parametric | `sqrt(a + b/x**3)/x**5` | $\frac{\sqrt{a + \frac{b}{x^{3}}}}{x^{5}}$ |
| partial | parametric | `sqrt(a + b/x**3)/x**8` | $\frac{\sqrt{a + \frac{b}{x^{3}}}}{x^{8}}$ |
| partial | parametric | `x**6*sqrt(a + b/x**3)` | $x^{6} \sqrt{a + \frac{b}{x^{3}}}$ |
| partial | parametric | `x**3*sqrt(a + b/x**3)` | $x^{3} \sqrt{a + \frac{b}{x^{3}}}$ |
| partial | parametric | `sqrt(a + b/x**3)` | $\sqrt{a + \frac{b}{x^{3}}}$ |
| partial | parametric | `sqrt(a + b/x**3)/x**3` | $\frac{\sqrt{a + \frac{b}{x^{3}}}}{x^{3}}$ |
| partial | parametric | `sqrt(a + b/x**3)/x**6` | $\frac{\sqrt{a + \frac{b}{x^{3}}}}{x^{6}}$ |
| partial | parametric | `sqrt(a + b/x**3)/x**9` | $\frac{\sqrt{a + \frac{b}{x^{3}}}}{x^{9}}$ |
| partial | parametric | `x**5*(a + b/x**3)**(3/2)` | $x^{5} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(a + b/x**3)**(3/2)` | $x^{2} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x**3)**(3/2)/x` | $\frac{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}{x}$ |
| SOLVED-both | parametric | `(a + b/x**3)**(3/2)/x**4` | $\frac{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b/x**3)**(3/2)/x**7` | $\frac{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}{x^{7}}$ |
| SOLVED-both | parametric | `(a + b/x**3)**(3/2)/x**10` | $\frac{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}{x^{10}}$ |
| SOLVED-both | parametric | `(a + b/x**3)**(3/2)/x**13` | $\frac{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}{x^{13}}$ |
| partial | parametric | `x**5/sqrt(a + b/x**3)` | $\frac{x^{5}}{\sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `x**2/sqrt(a + b/x**3)` | $\frac{x^{2}}{\sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `1/(x*sqrt(a + b/x**3))` | $\frac{1}{x \sqrt{a + \frac{b}{x^{3}}}}$ |
| SOLVED-both | parametric | `1/(x**4*sqrt(a + b/x**3))` | $\frac{1}{x^{4} \sqrt{a + \frac{b}{x^{3}}}}$ |
| SOLVED-both | parametric | `1/(x**7*sqrt(a + b/x**3))` | $\frac{1}{x^{7} \sqrt{a + \frac{b}{x^{3}}}}$ |
| SOLVED-both | parametric | `1/(x**10*sqrt(a + b/x**3))` | $\frac{1}{x^{10} \sqrt{a + \frac{b}{x^{3}}}}$ |
| SOLVED-both | parametric | `1/(x**13*sqrt(a + b/x**3))` | $\frac{1}{x^{13} \sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `x**7/sqrt(a + b/x**3)` | $\frac{x^{7}}{\sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `x**4/sqrt(a + b/x**3)` | $\frac{x^{4}}{\sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `x/sqrt(a + b/x**3)` | $\frac{x}{\sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b/x**3))` | $\frac{1}{x^{2} \sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `1/(x**5*sqrt(a + b/x**3))` | $\frac{1}{x^{5} \sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `1/(x**8*sqrt(a + b/x**3))` | $\frac{1}{x^{8} \sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `x**6/sqrt(a + b/x**3)` | $\frac{x^{6}}{\sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `x**3/sqrt(a + b/x**3)` | $\frac{x^{3}}{\sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `1/sqrt(a + b/x**3)` | $\frac{1}{\sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `1/(x**3*sqrt(a + b/x**3))` | $\frac{1}{x^{3} \sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `1/(x**6*sqrt(a + b/x**3))` | $\frac{1}{x^{6} \sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `1/(x**9*sqrt(a + b/x**3))` | $\frac{1}{x^{9} \sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `1/(x**12*sqrt(a + b/x**3))` | $\frac{1}{x^{12} \sqrt{a + \frac{b}{x^{3}}}}$ |
| partial | parametric | `x**5/(a + b/x**3)**(3/2)` | $\frac{x^{5}}{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a + b/x**3)**(3/2)` | $\frac{x^{2}}{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b/x**3)**(3/2))` | $\frac{1}{x \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**4*(a + b/x**3)**(3/2))` | $\frac{1}{x^{4} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**7*(a + b/x**3)**(3/2))` | $\frac{1}{x^{7} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**10*(a + b/x**3)**(3/2))` | $\frac{1}{x^{10} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/(x**13*(a + b/x**3)**(3/2))` | $\frac{1}{x^{13} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**7/(a + b/x**3)**(3/2)` | $\frac{x^{7}}{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/(a + b/x**3)**(3/2)` | $\frac{x^{4}}{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a + b/x**3)**(3/2)` | $\frac{x}{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b/x**3)**(3/2))` | $\frac{1}{x^{2} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**5*(a + b/x**3)**(3/2))` | $\frac{1}{x^{5} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**8*(a + b/x**3)**(3/2))` | $\frac{1}{x^{8} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**6/(a + b/x**3)**(3/2)` | $\frac{x^{6}}{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/(a + b/x**3)**(3/2)` | $\frac{x^{3}}{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x**3)**(-3/2)` | $\frac{1}{\left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b/x**3)**(3/2))` | $\frac{1}{x^{3} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**6*(a + b/x**3)**(3/2))` | $\frac{1}{x^{6} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**9*(a + b/x**3)**(3/2))` | $\frac{1}{x^{9} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**12*(a + b/x**3)**(3/2))` | $\frac{1}{x^{12} \left(a + \frac{b}{x^{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*sqrt(a + b/x**4)` | $x^{3} \sqrt{a + \frac{b}{x^{4}}}$ |
| partial | parametric | `x*sqrt(a + b/x**4)` | $x \sqrt{a + \frac{b}{x^{4}}}$ |
| partial | parametric | `sqrt(a + b/x**4)/x` | $\frac{\sqrt{a + \frac{b}{x^{4}}}}{x}$ |
| partial | parametric | `sqrt(a + b/x**4)/x**3` | $\frac{\sqrt{a + \frac{b}{x^{4}}}}{x^{3}}$ |
| partial | parametric | `x**2*sqrt(a + b/x**4)` | $x^{2} \sqrt{a + \frac{b}{x^{4}}}$ |
| partial | parametric | `sqrt(a + b/x**4)` | $\sqrt{a + \frac{b}{x^{4}}}$ |
| partial | parametric | `sqrt(a + b/x**4)/x**2` | $\frac{\sqrt{a + \frac{b}{x^{4}}}}{x^{2}}$ |
| partial | parametric | `sqrt(a + b/x**4)/x**4` | $\frac{\sqrt{a + \frac{b}{x^{4}}}}{x^{4}}$ |
| partial | parametric | `x**3*(a + b/x**4)**(3/2)` | $x^{3} \left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a + b/x**4)**(3/2)` | $x \left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x**4)**(3/2)/x` | $\frac{\left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a + b/x**4)**(3/2)/x**3` | $\frac{\left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `x**2*(a + b/x**4)**(3/2)` | $x^{2} \left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x**4)**(3/2)` | $\left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x**4)**(3/2)/x**2` | $\frac{\left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b/x**4)**(3/2)/x**4` | $\frac{\left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `x**3*(a + b/x**4)**(5/2)` | $x^{3} \left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x*(a + b/x**4)**(5/2)` | $x \left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b/x**4)**(5/2)/x` | $\frac{\left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(a + b/x**4)**(5/2)/x**3` | $\frac{\left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `x**2*(a + b/x**4)**(5/2)` | $x^{2} \left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b/x**4)**(5/2)` | $\left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b/x**4)**(5/2)/x**2` | $\frac{\left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b/x**4)**(5/2)/x**4` | $\frac{\left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `x**3/sqrt(a + b/x**4)` | $\frac{x^{3}}{\sqrt{a + \frac{b}{x^{4}}}}$ |
| partial | parametric | `x/sqrt(a + b/x**4)` | $\frac{x}{\sqrt{a + \frac{b}{x^{4}}}}$ |
| partial | parametric | `1/(x*sqrt(a + b/x**4))` | $\frac{1}{x \sqrt{a + \frac{b}{x^{4}}}}$ |
| partial | parametric | `1/(x**3*sqrt(a + b/x**4))` | $\frac{1}{x^{3} \sqrt{a + \frac{b}{x^{4}}}}$ |
| partial | parametric | `x**2/sqrt(a + b/x**4)` | $\frac{x^{2}}{\sqrt{a + \frac{b}{x^{4}}}}$ |
| partial | parametric | `1/sqrt(a + b/x**4)` | $\frac{1}{\sqrt{a + \frac{b}{x^{4}}}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b/x**4))` | $\frac{1}{x^{2} \sqrt{a + \frac{b}{x^{4}}}}$ |
| partial | parametric | `1/(x**4*sqrt(a + b/x**4))` | $\frac{1}{x^{4} \sqrt{a + \frac{b}{x^{4}}}}$ |
| partial | parametric | `x**3/(a + b/x**4)**(3/2)` | $\frac{x^{3}}{\left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a + b/x**4)**(3/2)` | $\frac{x}{\left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b/x**4)**(3/2))` | $\frac{1}{x \left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b/x**4)**(3/2))` | $\frac{1}{x^{3} \left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a + b/x**4)**(3/2)` | $\frac{x^{2}}{\left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x**4)**(-3/2)` | $\frac{1}{\left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b/x**4)**(3/2))` | $\frac{1}{x^{2} \left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b/x**4)**(3/2))` | $\frac{1}{x^{4} \left(a + \frac{b}{x^{4}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/(a + b/x**4)**(5/2)` | $\frac{x^{3}}{\left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x/(a + b/x**4)**(5/2)` | $\frac{x}{\left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*(a + b/x**4)**(5/2))` | $\frac{1}{x \left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b/x**4)**(5/2))` | $\frac{1}{x^{3} \left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2/(a + b/x**4)**(5/2)` | $\frac{x^{2}}{\left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b/x**4)**(-5/2)` | $\frac{1}{\left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b/x**4)**(5/2))` | $\frac{1}{x^{2} \left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b/x**4)**(5/2))` | $\frac{1}{x^{4} \left(a + \frac{b}{x^{4}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*sqrt(a + b/x**5))` | $\frac{1}{x \sqrt{a + \frac{b}{x^{5}}}}$ |
| partial | parametric | `1/(x*sqrt(-a + b/x**5))` | $\frac{1}{x \sqrt{- a + \frac{b}{x^{5}}}}$ |
| SOLVED-both | parametric | `x**4*(a + b*sqrt(x))` | $x^{4} \left(a + b \sqrt{x}\right)$ |
| SOLVED-both | parametric | `x**3*(a + b*sqrt(x))` | $x^{3} \left(a + b \sqrt{x}\right)$ |
| SOLVED-both | parametric | `x**2*(a + b*sqrt(x))` | $x^{2} \left(a + b \sqrt{x}\right)$ |
| SOLVED-both | parametric | `x*(a + b*sqrt(x))` | $x \left(a + b \sqrt{x}\right)$ |
| SOLVED-both | parametric | `a + b*sqrt(x)` | $a + b \sqrt{x}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))/x` | $\frac{a + b \sqrt{x}}{x}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))/x**2` | $\frac{a + b \sqrt{x}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))/x**3` | $\frac{a + b \sqrt{x}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))/x**4` | $\frac{a + b \sqrt{x}}{x^{4}}$ |
| SOLVED-both | parametric | `x**4*(a + b*sqrt(x))**2` | $x^{4} \left(a + b \sqrt{x}\right)^{2}$ |
| SOLVED-both | parametric | `x**3*(a + b*sqrt(x))**2` | $x^{3} \left(a + b \sqrt{x}\right)^{2}$ |
| SOLVED-both | parametric | `x**2*(a + b*sqrt(x))**2` | $x^{2} \left(a + b \sqrt{x}\right)^{2}$ |
| SOLVED-both | parametric | `x*(a + b*sqrt(x))**2` | $x \left(a + b \sqrt{x}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**2` | $\left(a + b \sqrt{x}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**2/x` | $\frac{\left(a + b \sqrt{x}\right)^{2}}{x}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**2/x**2` | $\frac{\left(a + b \sqrt{x}\right)^{2}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**2/x**3` | $\frac{\left(a + b \sqrt{x}\right)^{2}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**2/x**4` | $\frac{\left(a + b \sqrt{x}\right)^{2}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**2/x**5` | $\frac{\left(a + b \sqrt{x}\right)^{2}}{x^{5}}$ |
| SOLVED-both | parametric | `x**4*(a + b*sqrt(x))**3` | $x^{4} \left(a + b \sqrt{x}\right)^{3}$ |
| SOLVED-both | parametric | `x**3*(a + b*sqrt(x))**3` | $x^{3} \left(a + b \sqrt{x}\right)^{3}$ |
| SOLVED-both | parametric | `x**2*(a + b*sqrt(x))**3` | $x^{2} \left(a + b \sqrt{x}\right)^{3}$ |
| SOLVED-both | parametric | `x*(a + b*sqrt(x))**3` | $x \left(a + b \sqrt{x}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**3` | $\left(a + b \sqrt{x}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**3/x` | $\frac{\left(a + b \sqrt{x}\right)^{3}}{x}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**3/x**2` | $\frac{\left(a + b \sqrt{x}\right)^{3}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**3/x**3` | $\frac{\left(a + b \sqrt{x}\right)^{3}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**3/x**4` | $\frac{\left(a + b \sqrt{x}\right)^{3}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**3/x**5` | $\frac{\left(a + b \sqrt{x}\right)^{3}}{x^{5}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**3/x**6` | $\frac{\left(a + b \sqrt{x}\right)^{3}}{x^{6}}$ |
| SOLVED-both | parametric | `x**4*(a + b*sqrt(x))**5` | $x^{4} \left(a + b \sqrt{x}\right)^{5}$ |
| SOLVED-both | parametric | `x**3*(a + b*sqrt(x))**5` | $x^{3} \left(a + b \sqrt{x}\right)^{5}$ |
| SOLVED-both | parametric | `x**2*(a + b*sqrt(x))**5` | $x^{2} \left(a + b \sqrt{x}\right)^{5}$ |
| SOLVED-both | parametric | `x*(a + b*sqrt(x))**5` | $x \left(a + b \sqrt{x}\right)^{5}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**5` | $\left(a + b \sqrt{x}\right)^{5}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**5/x` | $\frac{\left(a + b \sqrt{x}\right)^{5}}{x}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**5/x**2` | $\frac{\left(a + b \sqrt{x}\right)^{5}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**5/x**3` | $\frac{\left(a + b \sqrt{x}\right)^{5}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**5/x**4` | $\frac{\left(a + b \sqrt{x}\right)^{5}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**5/x**5` | $\frac{\left(a + b \sqrt{x}\right)^{5}}{x^{5}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**5/x**6` | $\frac{\left(a + b \sqrt{x}\right)^{5}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**5/x**7` | $\frac{\left(a + b \sqrt{x}\right)^{5}}{x^{7}}$ |
| SOLVED-both | parametric | `x**4*(a + b*sqrt(x))**10` | $x^{4} \left(a + b \sqrt{x}\right)^{10}$ |
| SOLVED-both | parametric | `x**3*(a + b*sqrt(x))**10` | $x^{3} \left(a + b \sqrt{x}\right)^{10}$ |
| SOLVED-both | parametric | `x**2*(a + b*sqrt(x))**10` | $x^{2} \left(a + b \sqrt{x}\right)^{10}$ |
| SOLVED-both | parametric | `x*(a + b*sqrt(x))**10` | $x \left(a + b \sqrt{x}\right)^{10}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**10` | $\left(a + b \sqrt{x}\right)^{10}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**10/x` | $\frac{\left(a + b \sqrt{x}\right)^{10}}{x}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**10/x**2` | $\frac{\left(a + b \sqrt{x}\right)^{10}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**10/x**3` | $\frac{\left(a + b \sqrt{x}\right)^{10}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**10/x**4` | $\frac{\left(a + b \sqrt{x}\right)^{10}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**10/x**5` | $\frac{\left(a + b \sqrt{x}\right)^{10}}{x^{5}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**10/x**6` | $\frac{\left(a + b \sqrt{x}\right)^{10}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**10/x**7` | $\frac{\left(a + b \sqrt{x}\right)^{10}}{x^{7}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**10/x**8` | $\frac{\left(a + b \sqrt{x}\right)^{10}}{x^{8}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**10/x**9` | $\frac{\left(a + b \sqrt{x}\right)^{10}}{x^{9}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**10/x**10` | $\frac{\left(a + b \sqrt{x}\right)^{10}}{x^{10}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**10/x**11` | $\frac{\left(a + b \sqrt{x}\right)^{10}}{x^{11}}$ |
| SOLVED-both | parametric | `x**5*(a + b*sqrt(x))**15` | $x^{5} \left(a + b \sqrt{x}\right)^{15}$ |
| SOLVED-both | parametric | `x**4*(a + b*sqrt(x))**15` | $x^{4} \left(a + b \sqrt{x}\right)^{15}$ |
| SOLVED-both | parametric | `x**3*(a + b*sqrt(x))**15` | $x^{3} \left(a + b \sqrt{x}\right)^{15}$ |
| SOLVED-both | parametric | `x**2*(a + b*sqrt(x))**15` | $x^{2} \left(a + b \sqrt{x}\right)^{15}$ |
| SOLVED-both | parametric | `x*(a + b*sqrt(x))**15` | $x \left(a + b \sqrt{x}\right)^{15}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15` | $\left(a + b \sqrt{x}\right)^{15}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**2` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**3` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**4` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**6` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**7` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{7}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**8` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{8}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**9` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{9}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**10` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{10}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**11` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{11}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**12` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{12}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**13` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{13}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**14` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{14}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**15` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{15}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**16` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{16}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**15/x**17` | $\frac{\left(a + b \sqrt{x}\right)^{15}}{x^{17}}$ |
| partial | parametric | `x**3/(a + b*sqrt(x))` | $\frac{x^{3}}{a + b \sqrt{x}}$ |
| partial | parametric | `x**2/(a + b*sqrt(x))` | $\frac{x^{2}}{a + b \sqrt{x}}$ |
| partial | parametric | `x/(a + b*sqrt(x))` | $\frac{x}{a + b \sqrt{x}}$ |
| partial | parametric | `1/(a + b*sqrt(x))` | $\frac{1}{a + b \sqrt{x}}$ |
| SOLVED-both | parametric | `1/(x*(a + b*sqrt(x)))` | $\frac{1}{x \left(a + b \sqrt{x}\right)}$ |
| partial | parametric | `1/(x**2*(a + b*sqrt(x)))` | $\frac{1}{x^{2} \left(a + b \sqrt{x}\right)}$ |
| partial | parametric | `1/(x**3*(a + b*sqrt(x)))` | $\frac{1}{x^{3} \left(a + b \sqrt{x}\right)}$ |
| partial | parametric | `1/(x**4*(a + b*sqrt(x)))` | $\frac{1}{x^{4} \left(a + b \sqrt{x}\right)}$ |
| partial | parametric | `x**3/(a + b*sqrt(x))**2` | $\frac{x^{3}}{\left(a + b \sqrt{x}\right)^{2}}$ |
| partial | parametric | `x**2/(a + b*sqrt(x))**2` | $\frac{x^{2}}{\left(a + b \sqrt{x}\right)^{2}}$ |
| partial | parametric | `x/(a + b*sqrt(x))**2` | $\frac{x}{\left(a + b \sqrt{x}\right)^{2}}$ |
| partial | parametric | `(a + b*sqrt(x))**(-2)` | $\frac{1}{\left(a + b \sqrt{x}\right)^{2}}$ |
| SOLVED-both | parametric | `1/(x*(a + b*sqrt(x))**2)` | $\frac{1}{x \left(a + b \sqrt{x}\right)^{2}}$ |
| partial | parametric | `1/(x**2*(a + b*sqrt(x))**2)` | $\frac{1}{x^{2} \left(a + b \sqrt{x}\right)^{2}}$ |
| partial | parametric | `1/(x**3*(a + b*sqrt(x))**2)` | $\frac{1}{x^{3} \left(a + b \sqrt{x}\right)^{2}}$ |
| partial | parametric | `1/(x**4*(a + b*sqrt(x))**2)` | $\frac{1}{x^{4} \left(a + b \sqrt{x}\right)^{2}}$ |
| partial | parametric | `x**3/(a + b*sqrt(x))**3` | $\frac{x^{3}}{\left(a + b \sqrt{x}\right)^{3}}$ |
| partial | parametric | `x**2/(a + b*sqrt(x))**3` | $\frac{x^{2}}{\left(a + b \sqrt{x}\right)^{3}}$ |
| partial | parametric | `x/(a + b*sqrt(x))**3` | $\frac{x}{\left(a + b \sqrt{x}\right)^{3}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**(-3)` | $\frac{1}{\left(a + b \sqrt{x}\right)^{3}}$ |
| SOLVED-both | parametric | `1/(x*(a + b*sqrt(x))**3)` | $\frac{1}{x \left(a + b \sqrt{x}\right)^{3}}$ |
| partial | parametric | `1/(x**2*(a + b*sqrt(x))**3)` | $\frac{1}{x^{2} \left(a + b \sqrt{x}\right)^{3}}$ |
| partial | parametric | `1/(x**3*(a + b*sqrt(x))**3)` | $\frac{1}{x^{3} \left(a + b \sqrt{x}\right)^{3}}$ |
| partial | parametric | `1/(x**4*(a + b*sqrt(x))**3)` | $\frac{1}{x^{4} \left(a + b \sqrt{x}\right)^{3}}$ |
| partial | parametric | `x**4/(a + b*sqrt(x))**5` | $\frac{x^{4}}{\left(a + b \sqrt{x}\right)^{5}}$ |
| partial | parametric | `x**3/(a + b*sqrt(x))**5` | $\frac{x^{3}}{\left(a + b \sqrt{x}\right)^{5}}$ |
| partial | parametric | `x**2/(a + b*sqrt(x))**5` | $\frac{x^{2}}{\left(a + b \sqrt{x}\right)^{5}}$ |
| SOLVED-both | parametric | `x/(a + b*sqrt(x))**5` | $\frac{x}{\left(a + b \sqrt{x}\right)^{5}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**(-5)` | $\frac{1}{\left(a + b \sqrt{x}\right)^{5}}$ |
| SOLVED-both | parametric | `1/(x*(a + b*sqrt(x))**5)` | $\frac{1}{x \left(a + b \sqrt{x}\right)^{5}}$ |
| partial | parametric | `1/(x**2*(a + b*sqrt(x))**5)` | $\frac{1}{x^{2} \left(a + b \sqrt{x}\right)^{5}}$ |
| partial | parametric | `1/(x**3*(a + b*sqrt(x))**5)` | $\frac{1}{x^{3} \left(a + b \sqrt{x}\right)^{5}}$ |
| partial | parametric | `x**5/(a + b*sqrt(x))**8` | $\frac{x^{5}}{\left(a + b \sqrt{x}\right)^{8}}$ |
| partial | parametric | `x**4/(a + b*sqrt(x))**8` | $\frac{x^{4}}{\left(a + b \sqrt{x}\right)^{8}}$ |
| partial | parametric | `x**3/(a + b*sqrt(x))**8` | $\frac{x^{3}}{\left(a + b \sqrt{x}\right)^{8}}$ |
| SOLVED-both | parametric | `x**2/(a + b*sqrt(x))**8` | $\frac{x^{2}}{\left(a + b \sqrt{x}\right)^{8}}$ |
| SOLVED-both | parametric | `x/(a + b*sqrt(x))**8` | $\frac{x}{\left(a + b \sqrt{x}\right)^{8}}$ |
| SOLVED-both | parametric | `(a + b*sqrt(x))**(-8)` | $\frac{1}{\left(a + b \sqrt{x}\right)^{8}}$ |
| SOLVED-both | parametric | `1/(x*(a + b*sqrt(x))**8)` | $\frac{1}{x \left(a + b \sqrt{x}\right)^{8}}$ |
| partial | parametric | `1/(x**2*(a + b*sqrt(x))**8)` | $\frac{1}{x^{2} \left(a + b \sqrt{x}\right)^{8}}$ |
| partial | parametric | `1/(x**3*(a + b*sqrt(x))**8)` | $\frac{1}{x^{3} \left(a + b \sqrt{x}\right)^{8}}$ |
| SOLVED-both | parametric | `1/(x*(b*sqrt(x) + 2))` | $\frac{1}{x \left(b \sqrt{x} + 2\right)}$ |
| partial | parametric | `x**2*sqrt(a + b*sqrt(x))` | $x^{2} \sqrt{a + b \sqrt{x}}$ |
| partial | parametric | `x*sqrt(a + b*sqrt(x))` | $x \sqrt{a + b \sqrt{x}}$ |
| partial | parametric | `sqrt(a + b*sqrt(x))` | $\sqrt{a + b \sqrt{x}}$ |
| partial | parametric | `sqrt(a + b*sqrt(x))/x` | $\frac{\sqrt{a + b \sqrt{x}}}{x}$ |
| partial | parametric | `sqrt(a + b*sqrt(x))/x**2` | $\frac{\sqrt{a + b \sqrt{x}}}{x^{2}}$ |
| partial | parametric | `sqrt(a + b*sqrt(x))/x**3` | $\frac{\sqrt{a + b \sqrt{x}}}{x^{3}}$ |
| partial | parametric | `x**2/sqrt(a + b*sqrt(x))` | $\frac{x^{2}}{\sqrt{a + b \sqrt{x}}}$ |
| partial | parametric | `x/sqrt(a + b*sqrt(x))` | $\frac{x}{\sqrt{a + b \sqrt{x}}}$ |
| partial | parametric | `1/sqrt(a + b*sqrt(x))` | $\frac{1}{\sqrt{a + b \sqrt{x}}}$ |
| partial | parametric | `1/(x*sqrt(a + b*sqrt(x)))` | $\frac{1}{x \sqrt{a + b \sqrt{x}}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b*sqrt(x)))` | $\frac{1}{x^{2} \sqrt{a + b \sqrt{x}}}$ |
| partial | parametric | `1/(x**3*sqrt(a + b*sqrt(x)))` | $\frac{1}{x^{3} \sqrt{a + b \sqrt{x}}}$ |
| partial | concrete | `(sqrt(x) + 1)/sqrt(x)` | $\frac{\sqrt{x} + 1}{\sqrt{x}}$ |
| partial | concrete | `(sqrt(x) + 1)**2/sqrt(x)` | $\frac{\left(\sqrt{x} + 1\right)^{2}}{\sqrt{x}}$ |
| partial | concrete | `(sqrt(x) + 1)**3/sqrt(x)` | $\frac{\left(\sqrt{x} + 1\right)^{3}}{\sqrt{x}}$ |
| partial | concrete | `sqrt(x)/(sqrt(x) + 1)` | $\frac{\sqrt{x}}{\sqrt{x} + 1}$ |
| partial | concrete | `1/(sqrt(x)*(sqrt(x) + 1))` | $\frac{1}{\sqrt{x} \left(\sqrt{x} + 1\right)}$ |
| partial | concrete | `1/(sqrt(x)*(sqrt(x) + 1)**2)` | $\frac{1}{\sqrt{x} \left(\sqrt{x} + 1\right)^{2}}$ |
| partial | concrete | `1/(sqrt(x)*(sqrt(x) + 1)**3)` | $\frac{1}{\sqrt{x} \left(\sqrt{x} + 1\right)^{3}}$ |
| partial | concrete | `sqrt(x)*sqrt(sqrt(x) + 1)` | $\sqrt{x} \sqrt{\sqrt{x} + 1}$ |
| partial | concrete | `sqrt(sqrt(x) + 1)/sqrt(x)` | $\frac{\sqrt{\sqrt{x} + 1}}{\sqrt{x}}$ |
| partial | concrete | `x**(1/3)/(sqrt(x) + 1)` | $\frac{\sqrt[3]{x}}{\sqrt{x} + 1}$ |
| partial | parametric | `x**3/(a + b*x**(3/2))**(2/3)` | $\frac{x^{3}}{\left(a + b x^{\frac{3}{2}}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `x**2/(a + b*x**(3/2))**(2/3)` | $\frac{x^{2}}{\left(a + b x^{\frac{3}{2}}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a + b*x**(3/2))**(-2/3)` | $\frac{1}{\left(a + b x^{\frac{3}{2}}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x*(a + b*x**(3/2))**(2/3))` | $\frac{1}{x \left(a + b x^{\frac{3}{2}}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**(3/2))**(2/3))` | $\frac{1}{x^{3} \left(a + b x^{\frac{3}{2}}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**(3/2))**(2/3))` | $\frac{1}{x^{4} \left(a + b x^{\frac{3}{2}}\right)^{\frac{2}{3}}}$ |
| partial | concrete | `sqrt(x)/(x**(3/2) + 1)` | $\frac{\sqrt{x}}{x^{\frac{3}{2}} + 1}$ |
| SOLVED-both | parametric | `x**4*(a + b*x**(1/3))` | $x^{4} \left(a + b \sqrt[3]{x}\right)$ |
| SOLVED-both | parametric | `x**3*(a + b*x**(1/3))` | $x^{3} \left(a + b \sqrt[3]{x}\right)$ |
| SOLVED-both | parametric | `x**2*(a + b*x**(1/3))` | $x^{2} \left(a + b \sqrt[3]{x}\right)$ |
| SOLVED-both | parametric | `x*(a + b*x**(1/3))` | $x \left(a + b \sqrt[3]{x}\right)$ |
| SOLVED-both | parametric | `a + b*x**(1/3)` | $a + b \sqrt[3]{x}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))/x` | $\frac{a + b \sqrt[3]{x}}{x}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))/x**2` | $\frac{a + b \sqrt[3]{x}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))/x**3` | $\frac{a + b \sqrt[3]{x}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))/x**4` | $\frac{a + b \sqrt[3]{x}}{x^{4}}$ |
| SOLVED-both | parametric | `x**4*(a + b*x**(1/3))**2` | $x^{4} \left(a + b \sqrt[3]{x}\right)^{2}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**(1/3))**2` | $x^{3} \left(a + b \sqrt[3]{x}\right)^{2}$ |
| SOLVED-both | parametric | `x**2*(a + b*x**(1/3))**2` | $x^{2} \left(a + b \sqrt[3]{x}\right)^{2}$ |
| SOLVED-both | parametric | `x*(a + b*x**(1/3))**2` | $x \left(a + b \sqrt[3]{x}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**2` | $\left(a + b \sqrt[3]{x}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**2/x` | $\frac{\left(a + b \sqrt[3]{x}\right)^{2}}{x}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**2/x**2` | $\frac{\left(a + b \sqrt[3]{x}\right)^{2}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**2/x**3` | $\frac{\left(a + b \sqrt[3]{x}\right)^{2}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**2/x**4` | $\frac{\left(a + b \sqrt[3]{x}\right)^{2}}{x^{4}}$ |
| SOLVED-both | parametric | `x**4*(a + b*x**(1/3))**3` | $x^{4} \left(a + b \sqrt[3]{x}\right)^{3}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**(1/3))**3` | $x^{3} \left(a + b \sqrt[3]{x}\right)^{3}$ |
| SOLVED-both | parametric | `x**2*(a + b*x**(1/3))**3` | $x^{2} \left(a + b \sqrt[3]{x}\right)^{3}$ |
| SOLVED-both | parametric | `x*(a + b*x**(1/3))**3` | $x \left(a + b \sqrt[3]{x}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**3` | $\left(a + b \sqrt[3]{x}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**3/x` | $\frac{\left(a + b \sqrt[3]{x}\right)^{3}}{x}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**3/x**2` | $\frac{\left(a + b \sqrt[3]{x}\right)^{3}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**3/x**3` | $\frac{\left(a + b \sqrt[3]{x}\right)^{3}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**3/x**4` | $\frac{\left(a + b \sqrt[3]{x}\right)^{3}}{x^{4}}$ |
| SOLVED-both | parametric | `x**4*(a + b*x**(1/3))**5` | $x^{4} \left(a + b \sqrt[3]{x}\right)^{5}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**(1/3))**5` | $x^{3} \left(a + b \sqrt[3]{x}\right)^{5}$ |
| SOLVED-both | parametric | `x**2*(a + b*x**(1/3))**5` | $x^{2} \left(a + b \sqrt[3]{x}\right)^{5}$ |
| SOLVED-both | parametric | `x*(a + b*x**(1/3))**5` | $x \left(a + b \sqrt[3]{x}\right)^{5}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**5` | $\left(a + b \sqrt[3]{x}\right)^{5}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**5/x` | $\frac{\left(a + b \sqrt[3]{x}\right)^{5}}{x}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**5/x**2` | $\frac{\left(a + b \sqrt[3]{x}\right)^{5}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**5/x**3` | $\frac{\left(a + b \sqrt[3]{x}\right)^{5}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**5/x**4` | $\frac{\left(a + b \sqrt[3]{x}\right)^{5}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**5/x**5` | $\frac{\left(a + b \sqrt[3]{x}\right)^{5}}{x^{5}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**5/x**6` | $\frac{\left(a + b \sqrt[3]{x}\right)^{5}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**5/x**7` | $\frac{\left(a + b \sqrt[3]{x}\right)^{5}}{x^{7}}$ |
| SOLVED-both | parametric | `x**4*(a + b*x**(1/3))**10` | $x^{4} \left(a + b \sqrt[3]{x}\right)^{10}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**(1/3))**10` | $x^{3} \left(a + b \sqrt[3]{x}\right)^{10}$ |
| SOLVED-both | parametric | `x**2*(a + b*x**(1/3))**10` | $x^{2} \left(a + b \sqrt[3]{x}\right)^{10}$ |
| SOLVED-both | parametric | `x*(a + b*x**(1/3))**10` | $x \left(a + b \sqrt[3]{x}\right)^{10}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**10` | $\left(a + b \sqrt[3]{x}\right)^{10}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**10/x` | $\frac{\left(a + b \sqrt[3]{x}\right)^{10}}{x}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**10/x**2` | $\frac{\left(a + b \sqrt[3]{x}\right)^{10}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**10/x**3` | $\frac{\left(a + b \sqrt[3]{x}\right)^{10}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**10/x**4` | $\frac{\left(a + b \sqrt[3]{x}\right)^{10}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**10/x**5` | $\frac{\left(a + b \sqrt[3]{x}\right)^{10}}{x^{5}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**10/x**6` | $\frac{\left(a + b \sqrt[3]{x}\right)^{10}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**10/x**7` | $\frac{\left(a + b \sqrt[3]{x}\right)^{10}}{x^{7}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**10/x**8` | $\frac{\left(a + b \sqrt[3]{x}\right)^{10}}{x^{8}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**10/x**9` | $\frac{\left(a + b \sqrt[3]{x}\right)^{10}}{x^{9}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**10/x**10` | $\frac{\left(a + b \sqrt[3]{x}\right)^{10}}{x^{10}}$ |
| SOLVED-both | parametric | `x**5*(a + b*x**(1/3))**15` | $x^{5} \left(a + b \sqrt[3]{x}\right)^{15}$ |
| SOLVED-both | parametric | `x**4*(a + b*x**(1/3))**15` | $x^{4} \left(a + b \sqrt[3]{x}\right)^{15}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**(1/3))**15` | $x^{3} \left(a + b \sqrt[3]{x}\right)^{15}$ |
| SOLVED-both | parametric | `x**2*(a + b*x**(1/3))**15` | $x^{2} \left(a + b \sqrt[3]{x}\right)^{15}$ |
| SOLVED-both | parametric | `x*(a + b*x**(1/3))**15` | $x \left(a + b \sqrt[3]{x}\right)^{15}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**15` | $\left(a + b \sqrt[3]{x}\right)^{15}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**15/x` | $\frac{\left(a + b \sqrt[3]{x}\right)^{15}}{x}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**15/x**2` | $\frac{\left(a + b \sqrt[3]{x}\right)^{15}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**15/x**3` | $\frac{\left(a + b \sqrt[3]{x}\right)^{15}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**15/x**4` | $\frac{\left(a + b \sqrt[3]{x}\right)^{15}}{x^{4}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**15/x**6` | $\frac{\left(a + b \sqrt[3]{x}\right)^{15}}{x^{6}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**15/x**7` | $\frac{\left(a + b \sqrt[3]{x}\right)^{15}}{x^{7}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**15/x**8` | $\frac{\left(a + b \sqrt[3]{x}\right)^{15}}{x^{8}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**15/x**9` | $\frac{\left(a + b \sqrt[3]{x}\right)^{15}}{x^{9}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**15/x**10` | $\frac{\left(a + b \sqrt[3]{x}\right)^{15}}{x^{10}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**15/x**11` | $\frac{\left(a + b \sqrt[3]{x}\right)^{15}}{x^{11}}$ |
| SOLVED-both | parametric | `(a + b*x**(1/3))**15/x**12` | $\frac{\left(a + b \sqrt[3]{x}\right)^{15}}{x^{12}}$ |
| partial | parametric | `x**3/(a + b*x**(1/3))` | $\frac{x^{3}}{a + b \sqrt[3]{x}}$ |
| partial | parametric | `x**2/(a + b*x**(1/3))` | $\frac{x^{2}}{a + b \sqrt[3]{x}}$ |
| partial | parametric | `x/(a + b*x**(1/3))` | $\frac{x}{a + b \sqrt[3]{x}}$ |
| partial | parametric | `1/(a + b*x**(1/3))` | $\frac{1}{a + b \sqrt[3]{x}}$ |
| SOLVED-both | parametric | `1/(x*(a + b*x**(1/3)))` | $\frac{1}{x \left(a + b \sqrt[3]{x}\right)}$ |
| partial | parametric | `1/(x**2*(a + b*x**(1/3)))` | $\frac{1}{x^{2} \left(a + b \sqrt[3]{x}\right)}$ |
| partial | parametric | `1/(x**3*(a + b*x**(1/3)))` | $\frac{1}{x^{3} \left(a + b \sqrt[3]{x}\right)}$ |
| partial | parametric | `1/(x**4*(a + b*x**(1/3)))` | $\frac{1}{x^{4} \left(a + b \sqrt[3]{x}\right)}$ |
| SOLVED-both | parametric | `1/(x*(b*x**(1/3) + 2))` | $\frac{1}{x \left(b \sqrt[3]{x} + 2\right)}$ |
| partial | parametric | `x**3/(a + b*x**(1/3))**2` | $\frac{x^{3}}{\left(a + b \sqrt[3]{x}\right)^{2}}$ |
| partial | parametric | `x**2/(a + b*x**(1/3))**2` | $\frac{x^{2}}{\left(a + b \sqrt[3]{x}\right)^{2}}$ |
| partial | parametric | `x/(a + b*x**(1/3))**2` | $\frac{x}{\left(a + b \sqrt[3]{x}\right)^{2}}$ |
| partial | parametric | `(a + b*x**(1/3))**(-2)` | $\frac{1}{\left(a + b \sqrt[3]{x}\right)^{2}}$ |
| SOLVED-both | parametric | `1/(x*(a + b*x**(1/3))**2)` | $\frac{1}{x \left(a + b \sqrt[3]{x}\right)^{2}}$ |
| partial | parametric | `1/(x**2*(a + b*x**(1/3))**2)` | $\frac{1}{x^{2} \left(a + b \sqrt[3]{x}\right)^{2}}$ |
| partial | parametric | `1/(x**3*(a + b*x**(1/3))**2)` | $\frac{1}{x^{3} \left(a + b \sqrt[3]{x}\right)^{2}}$ |
| partial | parametric | `1/(x**4*(a + b*x**(1/3))**2)` | $\frac{1}{x^{4} \left(a + b \sqrt[3]{x}\right)^{2}}$ |
| partial | parametric | `x**3/(a + b*x**(1/3))**3` | $\frac{x^{3}}{\left(a + b \sqrt[3]{x}\right)^{3}}$ |
| partial | parametric | `x**2/(a + b*x**(1/3))**3` | $\frac{x^{2}}{\left(a + b \sqrt[3]{x}\right)^{3}}$ |
| partial | parametric | `x/(a + b*x**(1/3))**3` | $\frac{x}{\left(a + b \sqrt[3]{x}\right)^{3}}$ |
| partial | parametric | `(a + b*x**(1/3))**(-3)` | $\frac{1}{\left(a + b \sqrt[3]{x}\right)^{3}}$ |
| SOLVED-both | parametric | `1/(x*(a + b*x**(1/3))**3)` | $\frac{1}{x \left(a + b \sqrt[3]{x}\right)^{3}}$ |
| partial | parametric | `1/(x**2*(a + b*x**(1/3))**3)` | $\frac{1}{x^{2} \left(a + b \sqrt[3]{x}\right)^{3}}$ |
| partial | parametric | `1/(x**3*(a + b*x**(1/3))**3)` | $\frac{1}{x^{3} \left(a + b \sqrt[3]{x}\right)^{3}}$ |
| partial | parametric | `1/(x**4*(a + b*x**(1/3))**3)` | $\frac{1}{x^{4} \left(a + b \sqrt[3]{x}\right)^{3}}$ |
| partial | concrete | `1/sqrt(x**(1/3) + 1)` | $\frac{1}{\sqrt{\sqrt[3]{x} + 1}}$ |
| partial | concrete | `1/(x**(3/2)*(x**(1/3) + 1))` | $\frac{1}{x^{\frac{3}{2}} \left(\sqrt[3]{x} + 1\right)}$ |
| partial | concrete | `x**(2/3)/(x**(1/3) + 1)` | $\frac{x^{\frac{2}{3}}}{\sqrt[3]{x} + 1}$ |
| partial | concrete | `1/(x**(2/3) + 1)` | $\frac{1}{x^{\frac{2}{3}} + 1}$ |
| partial | concrete | `1/(x**(1/3)*(x**(2/3) + 1))` | $\frac{1}{\sqrt[3]{x} \left(x^{\frac{2}{3}} + 1\right)}$ |
| partial | concrete | `1/(x**(2/3)*(x**(2/3) + 1))` | $\frac{1}{x^{\frac{2}{3}} \left(x^{\frac{2}{3}} + 1\right)}$ |
| partial | concrete | `sqrt(x**(2/3) - 1)/x**(1/3)` | $\frac{\sqrt{x^{\frac{2}{3}} - 1}}{\sqrt[3]{x}}$ |
| partial | concrete | `(x**(2/3) + 1)**(3/2)/x**(1/3)` | $\frac{\left(x^{\frac{2}{3}} + 1\right)^{\frac{3}{2}}}{\sqrt[3]{x}}$ |
| partial | concrete | `sqrt(x)/(x**(2/3) + 1)` | $\frac{\sqrt{x}}{x^{\frac{2}{3}} + 1}$ |
| partial | concrete | `sqrt(3 - 1/sqrt(x))` | $\sqrt{3 - \frac{1}{\sqrt{x}}}$ |
| partial | concrete | `1/sqrt(1 + 1/sqrt(x))` | $\frac{1}{\sqrt{1 + \frac{1}{\sqrt{x}}}}$ |
| partial | parametric | `(a + b/x**(3/2))**(2/3)` | $\left(a + \frac{b}{x^{\frac{3}{2}}}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `x**4*(a + b/x**(1/3))` | $x^{4} \left(a + \frac{b}{\sqrt[3]{x}}\right)$ |
| SOLVED-both | parametric | `x**3*(a + b/x**(1/3))` | $x^{3} \left(a + \frac{b}{\sqrt[3]{x}}\right)$ |
| SOLVED-both | parametric | `x**2*(a + b/x**(1/3))` | $x^{2} \left(a + \frac{b}{\sqrt[3]{x}}\right)$ |
| SOLVED-both | parametric | `x*(a + b/x**(1/3))` | $x \left(a + \frac{b}{\sqrt[3]{x}}\right)$ |
| SOLVED-both | parametric | `a + b/x**(1/3)` | $a + \frac{b}{\sqrt[3]{x}}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))/x` | $\frac{a + \frac{b}{\sqrt[3]{x}}}{x}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))/x**2` | $\frac{a + \frac{b}{\sqrt[3]{x}}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))/x**3` | $\frac{a + \frac{b}{\sqrt[3]{x}}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))/x**4` | $\frac{a + \frac{b}{\sqrt[3]{x}}}{x^{4}}$ |
| SOLVED-both | parametric | `x**4*(a + b/x**(1/3))**2` | $x^{4} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}$ |
| SOLVED-both | parametric | `x**3*(a + b/x**(1/3))**2` | $x^{3} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}$ |
| SOLVED-both | parametric | `x**2*(a + b/x**(1/3))**2` | $x^{2} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}$ |
| SOLVED-both | parametric | `x*(a + b/x**(1/3))**2` | $x \left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))**2` | $\left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))**2/x` | $\frac{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}}{x}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))**2/x**2` | $\frac{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))**2/x**3` | $\frac{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))**2/x**4` | $\frac{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}}{x^{4}}$ |
| SOLVED-both | parametric | `x**4*(a + b/x**(1/3))**3` | $x^{4} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}$ |
| SOLVED-both | parametric | `x**3*(a + b/x**(1/3))**3` | $x^{3} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}$ |
| SOLVED-both | parametric | `x**2*(a + b/x**(1/3))**3` | $x^{2} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}$ |
| SOLVED-both | parametric | `x*(a + b/x**(1/3))**3` | $x \left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))**3` | $\left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))**3/x` | $\frac{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}}{x}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))**3/x**2` | $\frac{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}}{x^{2}}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))**3/x**3` | $\frac{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b/x**(1/3))**3/x**4` | $\frac{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}}{x^{4}}$ |
| partial | parametric | `x**2/(a + b/x**(1/3))` | $\frac{x^{2}}{a + \frac{b}{\sqrt[3]{x}}}$ |
| partial | parametric | `x/(a + b/x**(1/3))` | $\frac{x}{a + \frac{b}{\sqrt[3]{x}}}$ |
| partial | parametric | `1/(a + b/x**(1/3))` | $\frac{1}{a + \frac{b}{\sqrt[3]{x}}}$ |
| SOLVED-both | parametric | `1/(x*(a + b/x**(1/3)))` | $\frac{1}{x \left(a + \frac{b}{\sqrt[3]{x}}\right)}$ |
| partial | parametric | `1/(x**2*(a + b/x**(1/3)))` | $\frac{1}{x^{2} \left(a + \frac{b}{\sqrt[3]{x}}\right)}$ |
| partial | parametric | `1/(x**3*(a + b/x**(1/3)))` | $\frac{1}{x^{3} \left(a + \frac{b}{\sqrt[3]{x}}\right)}$ |
| partial | parametric | `1/(x**4*(a + b/x**(1/3)))` | $\frac{1}{x^{4} \left(a + \frac{b}{\sqrt[3]{x}}\right)}$ |
| partial | parametric | `1/(x**5*(a + b/x**(1/3)))` | $\frac{1}{x^{5} \left(a + \frac{b}{\sqrt[3]{x}}\right)}$ |
| partial | parametric | `x**2/(a + b/x**(1/3))**2` | $\frac{x^{2}}{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}}$ |
| partial | parametric | `x/(a + b/x**(1/3))**2` | $\frac{x}{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}}$ |
| partial | parametric | `(a + b/x**(1/3))**(-2)` | $\frac{1}{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}}$ |
| SOLVED-both | parametric | `1/(x*(a + b/x**(1/3))**2)` | $\frac{1}{x \left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}}$ |
| partial | parametric | `1/(x**2*(a + b/x**(1/3))**2)` | $\frac{1}{x^{2} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}}$ |
| partial | parametric | `1/(x**3*(a + b/x**(1/3))**2)` | $\frac{1}{x^{3} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}}$ |
| partial | parametric | `1/(x**4*(a + b/x**(1/3))**2)` | $\frac{1}{x^{4} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}}$ |
| partial | parametric | `1/(x**5*(a + b/x**(1/3))**2)` | $\frac{1}{x^{5} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{2}}$ |
| partial | parametric | `x**2/(a + b/x**(1/3))**3` | $\frac{x^{2}}{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}}$ |
| partial | parametric | `x/(a + b/x**(1/3))**3` | $\frac{x}{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}}$ |
| partial | parametric | `(a + b/x**(1/3))**(-3)` | $\frac{1}{\left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}}$ |
| SOLVED-both | parametric | `1/(x*(a + b/x**(1/3))**3)` | $\frac{1}{x \left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}}$ |
| partial | parametric | `1/(x**2*(a + b/x**(1/3))**3)` | $\frac{1}{x^{2} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}}$ |
| partial | parametric | `1/(x**3*(a + b/x**(1/3))**3)` | $\frac{1}{x^{3} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}}$ |
| partial | parametric | `1/(x**4*(a + b/x**(1/3))**3)` | $\frac{1}{x^{4} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}}$ |
| partial | parametric | `1/(x**5*(a + b/x**(1/3))**3)` | $\frac{1}{x^{5} \left(a + \frac{b}{\sqrt[3]{x}}\right)^{3}}$ |
| partial | parametric | `1/(b/x**(1/3) + 1)` | $\frac{1}{\frac{b}{\sqrt[3]{x}} + 1}$ |
| partial | concrete | `x**(2/3)*(x**(5/3) + 1)**(2/3)` | $x^{\frac{2}{3}} \left(x^{\frac{5}{3}} + 1\right)^{\frac{2}{3}}$ |
| partial | parametric | `x**(7/3)*(a**(10/3) - x**(10/3))**(19/7)` | $x^{\frac{7}{3}} \left(a^{\frac{10}{3}} - x^{\frac{10}{3}}\right)^{\frac{19}{7}}$ |
| partial | concrete | `1/(x**(1/5) + 1)` | $\frac{1}{\sqrt[5]{x} + 1}$ |
| partial | concrete | `1/(x**(1/5)*sqrt(x**(4/5) + 1))` | $\frac{1}{\sqrt[5]{x} \sqrt{x^{\frac{4}{5}} + 1}}$ |
| partial | parametric | `(a + b/x**(3/5))**(2/3)` | $\left(a + \frac{b}{x^{\frac{3}{5}}}\right)^{\frac{2}{3}}$ |
| SOLVED-both | parametric | `(c*(a + b*x)**2)**(5/2)` | $\left(c \left(a + b x\right)^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(c*(a + b*x)**2)**(3/2)` | $\left(c \left(a + b x\right)^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `sqrt(c*(a + b*x)**2)` | $\sqrt{c \left(a + b x\right)^{2}}$ |
| SOLVED-both | parametric | `1/sqrt(c*(a + b*x)**2)` | $\frac{1}{\sqrt{c \left(a + b x\right)^{2}}}$ |
| SOLVED-both | parametric | `(c*(a + b*x)**2)**(-3/2)` | $\frac{1}{\left(c \left(a + b x\right)^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(c*(a + b*x)**2)**(-5/2)` | $\frac{1}{\left(c \left(a + b x\right)^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `sqrt((5*x + 3)**2)` | $\sqrt{\left(5 x + 3\right)^{2}}$ |
| SOLVED-both | concrete | `sqrt((10*x + 6)**2)` | $\sqrt{\left(10 x + 6\right)^{2}}$ |
| SOLVED-both | concrete | `1/sqrt((5*x + 3)**2)` | $\frac{1}{\sqrt{\left(5 x + 3\right)^{2}}}$ |
| SOLVED-both | concrete | `1/sqrt(-(3*x + 2)**2)` | $\frac{1}{\sqrt{- \left(3 x + 2\right)^{2}}}$ |
| **SOLVED-NEW** | parametric | `(c*(a + b*x)**3)**(5/2)` | $\left(c \left(a + b x\right)^{3}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `(c*(a + b*x)**3)**(3/2)` | $\left(c \left(a + b x\right)^{3}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `sqrt(c*(a + b*x)**3)` | $\sqrt{c \left(a + b x\right)^{3}}$ |
| SOLVED-both | parametric | `1/sqrt(c*(a + b*x)**3)` | $\frac{1}{\sqrt{c \left(a + b x\right)^{3}}}$ |
| SOLVED-both | parametric | `(c*(a + b*x)**3)**(-3/2)` | $\frac{1}{\left(c \left(a + b x\right)^{3}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(c*(a + b*x)**3)**(-5/2)` | $\frac{1}{\left(c \left(a + b x\right)^{3}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(c/(a + b*x))**(5/2)` | $\left(\frac{c}{a + b x}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(c/(a + b*x))**(3/2)` | $\left(\frac{c}{a + b x}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `sqrt(c/(a + b*x))` | $\sqrt{\frac{c}{a + b x}}$ |
| SOLVED-both | parametric | `1/sqrt(c/(a + b*x))` | $\frac{1}{\sqrt{\frac{c}{a + b x}}}$ |
| SOLVED-both | parametric | `(c/(a + b*x))**(-3/2)` | $\frac{1}{\left(\frac{c}{a + b x}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(c/(a + b*x))**(-5/2)` | $\frac{1}{\left(\frac{c}{a + b x}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(c/(a + b*x)**2)**(5/2)` | $\left(\frac{c}{\left(a + b x\right)^{2}}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(c/(a + b*x)**2)**(3/2)` | $\left(\frac{c}{\left(a + b x\right)^{2}}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `sqrt(c/(a + b*x)**2)` | $\sqrt{\frac{c}{\left(a + b x\right)^{2}}}$ |
| SOLVED-both | parametric | `1/sqrt(c/(a + b*x)**2)` | $\frac{1}{\sqrt{\frac{c}{\left(a + b x\right)^{2}}}}$ |
| SOLVED-both | parametric | `(c/(a + b*x)**2)**(-3/2)` | $\frac{1}{\left(\frac{c}{\left(a + b x\right)^{2}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(c/(a + b*x)**2)**(-5/2)` | $\frac{1}{\left(\frac{c}{\left(a + b x\right)^{2}}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(c/(a + b*x)**3)**(5/2)` | $\left(\frac{c}{\left(a + b x\right)^{3}}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(c/(a + b*x)**3)**(3/2)` | $\left(\frac{c}{\left(a + b x\right)^{3}}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `sqrt(c/(a + b*x)**3)` | $\sqrt{\frac{c}{\left(a + b x\right)^{3}}}$ |
| SOLVED-both | parametric | `1/sqrt(c/(a + b*x)**3)` | $\frac{1}{\sqrt{\frac{c}{\left(a + b x\right)^{3}}}}$ |
| SOLVED-both | parametric | `(c/(a + b*x)**3)**(-3/2)` | $\frac{1}{\left(\frac{c}{\left(a + b x\right)^{3}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(c/(a + b*x)**3)**(-5/2)` | $\frac{1}{\left(\frac{c}{\left(a + b x\right)^{3}}\right)^{\frac{5}{2}}}$ |
| NIE | parametric | `(c*(a + b*x)**(3/2))**(2/3)` | $\left(c \left(a + b x\right)^{\frac{3}{2}}\right)^{\frac{2}{3}}$ |
| NIE | parametric | `(c*(a + b*x)**(2/3))**(3/2)` | $\left(c \left(a + b x\right)^{\frac{2}{3}}\right)^{\frac{3}{2}}$ |
| NIE | parametric | `(c/(a + b*x)**(3/2))**(-2/3)` | $\frac{1}{\left(\frac{c}{\left(a + b x\right)^{\frac{3}{2}}}\right)^{\frac{2}{3}}}$ |
| NIE | parametric | `(c/(a + b*x)**(2/3))**(-3/2)` | $\frac{1}{\left(\frac{c}{\left(a + b x\right)^{\frac{2}{3}}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/sqrt(a + b*(c + d*x)**4)` | $\frac{1}{\sqrt{a + b \left(c + d x\right)^{4}}}$ |
| partial | parametric | `x/sqrt(a + b*(c + d*x)**4)` | $\frac{x}{\sqrt{a + b \left(c + d x\right)^{4}}}$ |
| partial | concrete | `1/((x**2)**(3/2) + 1)` | $\frac{1}{\left(x^{2}\right)^{\frac{3}{2}} + 1}$ |
| partial | parametric | `x**5*sqrt(a + b*sqrt(c*x**2))` | $x^{5} \sqrt{a + b \sqrt{c x^{2}}}$ |
| partial | parametric | `x**3*sqrt(a + b*sqrt(c*x**2))` | $x^{3} \sqrt{a + b \sqrt{c x^{2}}}$ |
| partial | parametric | `x*sqrt(a + b*sqrt(c*x**2))` | $x \sqrt{a + b \sqrt{c x^{2}}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**2))/x` | $\frac{\sqrt{a + b \sqrt{c x^{2}}}}{x}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**2))/x**3` | $\frac{\sqrt{a + b \sqrt{c x^{2}}}}{x^{3}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**2))/x**5` | $\frac{\sqrt{a + b \sqrt{c x^{2}}}}{x^{5}}$ |
| partial | parametric | `x**4*sqrt(a + b*sqrt(c*x**2))` | $x^{4} \sqrt{a + b \sqrt{c x^{2}}}$ |
| partial | parametric | `x**2*sqrt(a + b*sqrt(c*x**2))` | $x^{2} \sqrt{a + b \sqrt{c x^{2}}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**2))` | $\sqrt{a + b \sqrt{c x^{2}}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**2))/x**2` | $\frac{\sqrt{a + b \sqrt{c x^{2}}}}{x^{2}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**2))/x**4` | $\frac{\sqrt{a + b \sqrt{c x^{2}}}}{x^{4}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**2))/x**6` | $\frac{\sqrt{a + b \sqrt{c x^{2}}}}{x^{6}}$ |
| partial | parametric | `x**8*sqrt(a + b*(c*x**2)**(3/2))` | $x^{8} \sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5*sqrt(a + b*(c*x**2)**(3/2))` | $x^{5} \sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*sqrt(a + b*(c*x**2)**(3/2))` | $x^{2} \sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*(c*x**2)**(3/2))/x` | $\frac{\sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}}{x}$ |
| partial | parametric | `sqrt(a + b*(c*x**2)**(3/2))/x**4` | $\frac{\sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}}{x^{4}}$ |
| partial | parametric | `x**3*sqrt(a + b*(c*x**2)**(3/2))` | $x^{3} \sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*(c*x**2)**(3/2))` | $\sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*(c*x**2)**(3/2))/x**3` | $\frac{\sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}}{x^{3}}$ |
| partial | parametric | `sqrt(a + b*(c*x**2)**(3/2))/x**6` | $\frac{\sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}}{x^{6}}$ |
| partial | parametric | `x**4*sqrt(a + b*(c*x**2)**(3/2))` | $x^{4} \sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*sqrt(a + b*(c*x**2)**(3/2))` | $x \sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*(c*x**2)**(3/2))/x**2` | $\frac{\sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}}{x^{2}}$ |
| partial | parametric | `sqrt(a + b*(c*x**2)**(3/2))/x**5` | $\frac{\sqrt{a + b \left(c x^{2}\right)^{\frac{3}{2}}}}{x^{5}}$ |
| partial | concrete | `1/((x**3)**(2/3) + 1)` | $\frac{1}{\left(x^{3}\right)^{\frac{2}{3}} + 1}$ |
| partial | parametric | `x**5*sqrt(a + b*sqrt(c*x**3))` | $x^{5} \sqrt{a + b \sqrt{c x^{3}}}$ |
| partial | parametric | `x**2*sqrt(a + b*sqrt(c*x**3))` | $x^{2} \sqrt{a + b \sqrt{c x^{3}}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**3))/x` | $\frac{\sqrt{a + b \sqrt{c x^{3}}}}{x}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**3))/x**4` | $\frac{\sqrt{a + b \sqrt{c x^{3}}}}{x^{4}}$ |
| partial | parametric | `x*sqrt(a + b*sqrt(c*x**3))` | $x \sqrt{a + b \sqrt{c x^{3}}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**3))/x**2` | $\frac{\sqrt{a + b \sqrt{c x^{3}}}}{x^{2}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**3))/x**5` | $\frac{\sqrt{a + b \sqrt{c x^{3}}}}{x^{5}}$ |
| partial | parametric | `x**3*sqrt(a + b*sqrt(c*x**3))` | $x^{3} \sqrt{a + b \sqrt{c x^{3}}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**3))` | $\sqrt{a + b \sqrt{c x^{3}}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c*x**3))/x**3` | $\frac{\sqrt{a + b \sqrt{c x^{3}}}}{x^{3}}$ |
| partial | parametric | `x**17*sqrt(a + b*(c*x**3)**(3/2))` | $x^{17} \sqrt{a + b \left(c x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**8*sqrt(a + b*(c*x**3)**(3/2))` | $x^{8} \sqrt{a + b \left(c x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*(c*x**3)**(3/2))/x` | $\frac{\sqrt{a + b \left(c x^{3}\right)^{\frac{3}{2}}}}{x}$ |
| partial | parametric | `x**2*sqrt(a + b*(c*x**3)**(3/2))` | $x^{2} \sqrt{a + b \left(c x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**9*sqrt(a + b*(c*x**3)**(3/2))` | $x^{9} \sqrt{a + b \left(c x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*(c*x**3)**(3/2))` | $\sqrt{a + b \left(c x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c/x))` | $\sqrt{a + b \sqrt{\frac{c}{x}}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c/x))/x` | $\frac{\sqrt{a + b \sqrt{\frac{c}{x}}}}{x}$ |
| partial | parametric | `sqrt(a + b*sqrt(c/x))/x**2` | $\frac{\sqrt{a + b \sqrt{\frac{c}{x}}}}{x^{2}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c/x))/x**3` | $\frac{\sqrt{a + b \sqrt{\frac{c}{x}}}}{x^{3}}$ |
| partial | parametric | `sqrt(a + b*sqrt(c/x))/x**4` | $\frac{\sqrt{a + b \sqrt{\frac{c}{x}}}}{x^{4}}$ |
| partial | parametric | `1/sqrt(a + b*sqrt(c/x))` | $\frac{1}{\sqrt{a + b \sqrt{\frac{c}{x}}}}$ |
| partial | parametric | `1/(x*sqrt(a + b*sqrt(c/x)))` | $\frac{1}{x \sqrt{a + b \sqrt{\frac{c}{x}}}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b*sqrt(c/x)))` | $\frac{1}{x^{2} \sqrt{a + b \sqrt{\frac{c}{x}}}}$ |
| partial | parametric | `1/(x**3*sqrt(a + b*sqrt(c/x)))` | $\frac{1}{x^{3} \sqrt{a + b \sqrt{\frac{c}{x}}}}$ |
| partial | parametric | `1/(x**4*sqrt(a + b*sqrt(c/x)))` | $\frac{1}{x^{4} \sqrt{a + b \sqrt{\frac{c}{x}}}}$ |
| partial | concrete | `1/sqrt(sqrt(1/x) + 1)` | $\frac{1}{\sqrt{\sqrt{\frac{1}{x}} + 1}}$ |
| partial | concrete | `1/(4*sqrt(x**4) + 1)` | $\frac{1}{4 \sqrt{x^{4}} + 1}$ |
| partial | concrete | `1/(1 - 4*sqrt(x**4))` | $\frac{1}{1 - 4 \sqrt{x^{4}}}$ |
| partial | concrete | `1/(4*(x**6)**(1/3) + 1)` | $\frac{1}{4 \sqrt[3]{x^{6}} + 1}$ |
| partial | concrete | `1/(1 - 4*(x**6)**(1/3))` | $\frac{1}{1 - 4 \sqrt[3]{x^{6}}}$ |
| NIE | parametric | `x**2*sqrt(a + b*sqrt(d/x) + c/x)` | $x^{2} \sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}$ |
| NIE | parametric | `x*sqrt(a + b*sqrt(d/x) + c/x)` | $x \sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}$ |
| NIE | parametric | `sqrt(a + b*sqrt(d/x) + c/x)` | $\sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}$ |
| NIE | parametric | `sqrt(a + b*sqrt(d/x) + c/x)/x` | $\frac{\sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}}{x}$ |
| NIE | parametric | `sqrt(a + b*sqrt(d/x) + c/x)/x**2` | $\frac{\sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}}{x^{2}}$ |
| NIE | parametric | `sqrt(a + b*sqrt(d/x) + c/x)/x**3` | $\frac{\sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}}{x^{3}}$ |
| NIE | parametric | `sqrt(a + b*sqrt(d/x) + c/x)/x**4` | $\frac{\sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}}{x^{4}}$ |
| NIE | parametric | `x**2/sqrt(a + b*sqrt(d/x) + c/x)` | $\frac{x^{2}}{\sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}}$ |
| NIE | parametric | `x/sqrt(a + b*sqrt(d/x) + c/x)` | $\frac{x}{\sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}}$ |
| NIE | parametric | `1/sqrt(a + b*sqrt(d/x) + c/x)` | $\frac{1}{\sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}}$ |
| NIE | parametric | `1/(x*sqrt(a + b*sqrt(d/x) + c/x))` | $\frac{1}{x \sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}}$ |
| NIE | parametric | `1/(x**2*sqrt(a + b*sqrt(d/x) + c/x))` | $\frac{1}{x^{2} \sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}}$ |
| NIE | parametric | `1/(x**3*sqrt(a + b*sqrt(d/x) + c/x))` | $\frac{1}{x^{3} \sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}}$ |
| NIE | parametric | `1/(x**4*sqrt(a + b*sqrt(d/x) + c/x))` | $\frac{1}{x^{4} \sqrt{a + b \sqrt{\frac{d}{x}} + \frac{c}{x}}}$ |
| **SOLVED-NEW** | concrete | `sqrt(sqrt(1/x) + 1/x)` | $\sqrt{\sqrt{\frac{1}{x}} + \frac{1}{x}}$ |
| NIE | concrete | `sqrt(sqrt(1/x) + 2 + 1/x)` | $\sqrt{\sqrt{\frac{1}{x}} + 2 + \frac{1}{x}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**3)**3/(c + d*x**3)**(13/3)` | $\frac{\left(a + b x^{3}\right)^{3}}{\left(c + d x^{3}\right)^{\frac{13}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**3)**2/(c + d*x**3)**(10/3)` | $\frac{\left(a + b x^{3}\right)^{2}}{\left(c + d x^{3}\right)^{\frac{10}{3}}}$ |
| SOLVED-both | parametric | `(a + b*x**3)/(c + d*x**3)**(7/3)` | $\frac{a + b x^{3}}{\left(c + d x^{3}\right)^{\frac{7}{3}}}$ |
| SOLVED-both | parametric | `(c + d*x**3)**(-4/3)` | $\frac{1}{\left(c + d x^{3}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `1/((a + b*x**3)*(c + d*x**3)**(1/3))` | $\frac{1}{\left(a + b x^{3}\right) \sqrt[3]{c + d x^{3}}}$ |
| partial | parametric | `(c + d*x**3)**(2/3)/(a + b*x**3)**2` | $\frac{\left(c + d x^{3}\right)^{\frac{2}{3}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `(c + d*x**3)**(5/3)/(a + b*x**3)**3` | $\frac{\left(c + d x^{3}\right)^{\frac{5}{3}}}{\left(a + b x^{3}\right)^{3}}$ |
| partial | parametric | `(a - b*x**4)**(5/2)/(c - d*x**4)` | $\frac{\left(a - b x^{4}\right)^{\frac{5}{2}}}{c - d x^{4}}$ |
| partial | parametric | `(a - b*x**4)**(3/2)/(c - d*x**4)` | $\frac{\left(a - b x^{4}\right)^{\frac{3}{2}}}{c - d x^{4}}$ |
| partial | parametric | `sqrt(a - b*x**4)/(c - d*x**4)` | $\frac{\sqrt{a - b x^{4}}}{c - d x^{4}}$ |
| partial | parametric | `1/(sqrt(a - b*x**4)*(c - d*x**4))` | $\frac{1}{\sqrt{a - b x^{4}} \left(c - d x^{4}\right)}$ |
| partial | parametric | `1/((a - b*x**4)**(3/2)*(c - d*x**4))` | $\frac{1}{\left(a - b x^{4}\right)^{\frac{3}{2}} \left(c - d x^{4}\right)}$ |
| partial | parametric | `1/((a - b*x**4)**(5/2)*(c - d*x**4))` | $\frac{1}{\left(a - b x^{4}\right)^{\frac{5}{2}} \left(c - d x^{4}\right)}$ |
| partial | parametric | `(a + b*x**4)**(3/2)/(c + d*x**4)` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}}}{c + d x^{4}}$ |
| partial | parametric | `sqrt(a + b*x**4)/(c + d*x**4)` | $\frac{\sqrt{a + b x^{4}}}{c + d x^{4}}$ |
| partial | parametric | `1/(sqrt(a + b*x**4)*(c + d*x**4))` | $\frac{1}{\sqrt{a + b x^{4}} \left(c + d x^{4}\right)}$ |
| partial | parametric | `1/((a + b*x**4)**(3/2)*(c + d*x**4))` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x^{4}\right)}$ |
| partial | parametric | `1/((a + b*x**4)**(5/2)*(c + d*x**4))` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{5}{2}} \left(c + d x^{4}\right)}$ |
| partial | parametric | `(a - b*x**4)**(7/2)/(c - d*x**4)**2` | $\frac{\left(a - b x^{4}\right)^{\frac{7}{2}}}{\left(c - d x^{4}\right)^{2}}$ |
| partial | parametric | `(a - b*x**4)**(5/2)/(c - d*x**4)**2` | $\frac{\left(a - b x^{4}\right)^{\frac{5}{2}}}{\left(c - d x^{4}\right)^{2}}$ |
| partial | parametric | `(a - b*x**4)**(3/2)/(c - d*x**4)**2` | $\frac{\left(a - b x^{4}\right)^{\frac{3}{2}}}{\left(c - d x^{4}\right)^{2}}$ |
| partial | parametric | `sqrt(a - b*x**4)/(c - d*x**4)**2` | $\frac{\sqrt{a - b x^{4}}}{\left(c - d x^{4}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(a - b*x**4)*(c - d*x**4)**2)` | $\frac{1}{\sqrt{a - b x^{4}} \left(c - d x^{4}\right)^{2}}$ |
| partial | parametric | `1/((a - b*x**4)**(3/2)*(c - d*x**4)**2)` | $\frac{1}{\left(a - b x^{4}\right)^{\frac{3}{2}} \left(c - d x^{4}\right)^{2}}$ |
| partial | parametric | `1/((a - b*x**4)**(5/2)*(c - d*x**4)**2)` | $\frac{1}{\left(a - b x^{4}\right)^{\frac{5}{2}} \left(c - d x^{4}\right)^{2}}$ |
| partial | parametric | `sqrt(a + b*x**4)/(a*c - b*c*x**4)` | $\frac{\sqrt{a + b x^{4}}}{a c - b c x^{4}}$ |
| partial | parametric | `sqrt(a - b*x**4)/(a*c + b*c*x**4)` | $\frac{\sqrt{a - b x^{4}}}{a c + b c x^{4}}$ |
| partial | parametric | `(a + b*x**4)**(7/4)/(c + d*x**4)` | $\frac{\left(a + b x^{4}\right)^{\frac{7}{4}}}{c + d x^{4}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/(c + d*x**4)` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{c + d x^{4}}$ |
| partial | parametric | `1/((a + b*x**4)**(1/4)*(c + d*x**4))` | $\frac{1}{\sqrt[4]{a + b x^{4}} \left(c + d x^{4}\right)}$ |
| partial | parametric | `1/((a + b*x**4)**(5/4)*(c + d*x**4))` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{5}{4}} \left(c + d x^{4}\right)}$ |
| partial | parametric | `1/((a + b*x**4)**(9/4)*(c + d*x**4))` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{9}{4}} \left(c + d x^{4}\right)}$ |
| partial | parametric | `1/((a + b*x**4)**(13/4)*(c + d*x**4))` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{13}{4}} \left(c + d x^{4}\right)}$ |
| partial | parametric | `(a + b*x**4)**(9/4)/(c + d*x**4)` | $\frac{\left(a + b x^{4}\right)^{\frac{9}{4}}}{c + d x^{4}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/(c + d*x**4)` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{c + d x^{4}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/(c + d*x**4)` | $\frac{\sqrt[4]{a + b x^{4}}}{c + d x^{4}}$ |
| partial | parametric | `1/((a + b*x**4)**(3/4)*(c + d*x**4))` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{3}{4}} \left(c + d x^{4}\right)}$ |
| partial | parametric | `1/((a + b*x**4)**(7/4)*(c + d*x**4))` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{7}{4}} \left(c + d x^{4}\right)}$ |
| partial | parametric | `1/((a + b*x**4)**(11/4)*(c + d*x**4))` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{11}{4}} \left(c + d x^{4}\right)}$ |
| partial | parametric | `(a + b*x**4)**(11/4)/(c + d*x**4)**2` | $\frac{\left(a + b x^{4}\right)^{\frac{11}{4}}}{\left(c + d x^{4}\right)^{2}}$ |
| partial | parametric | `(a + b*x**4)**(7/4)/(c + d*x**4)**2` | $\frac{\left(a + b x^{4}\right)^{\frac{7}{4}}}{\left(c + d x^{4}\right)^{2}}$ |
| partial | parametric | `(a + b*x**4)**(3/4)/(c + d*x**4)**2` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{4}}}{\left(c + d x^{4}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**4)**(1/4)*(c + d*x**4)**2)` | $\frac{1}{\sqrt[4]{a + b x^{4}} \left(c + d x^{4}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**4)**(5/4)*(c + d*x**4)**2)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{5}{4}} \left(c + d x^{4}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**4)**(9/4)*(c + d*x**4)**2)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{9}{4}} \left(c + d x^{4}\right)^{2}}$ |
| partial | parametric | `(a + b*x**4)**(9/4)/(c + d*x**4)**2` | $\frac{\left(a + b x^{4}\right)^{\frac{9}{4}}}{\left(c + d x^{4}\right)^{2}}$ |
| partial | parametric | `(a + b*x**4)**(5/4)/(c + d*x**4)**2` | $\frac{\left(a + b x^{4}\right)^{\frac{5}{4}}}{\left(c + d x^{4}\right)^{2}}$ |
| partial | parametric | `(a + b*x**4)**(1/4)/(c + d*x**4)**2` | $\frac{\sqrt[4]{a + b x^{4}}}{\left(c + d x^{4}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**4)**(3/4)*(c + d*x**4)**2)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{3}{4}} \left(c + d x^{4}\right)^{2}}$ |
| partial | parametric | `1/((a + b*x**4)**(7/4)*(c + d*x**4)**2)` | $\frac{1}{\left(a + b x^{4}\right)^{\frac{7}{4}} \left(c + d x^{4}\right)^{2}}$ |
| partial | concrete | `1/((x**4 + 1)**(1/4)*(x**4 + 2))` | $\frac{1}{\sqrt[4]{x^{4} + 1} \left(x^{4} + 2\right)}$ |
| partial | parametric | `1/((a + b*x**4)**(1/4)*(a - x**4*(a - b)))` | $\frac{1}{\sqrt[4]{a + b x^{4}} \left(a - x^{4} \left(a - b\right)\right)}$ |
| partial | parametric | `1/((a + b*x**5)**(1/5)*(c + d*x**5))` | $\frac{1}{\sqrt[5]{a + b x^{5}} \left(c + d x^{5}\right)}$ |
| partial | parametric | `sqrt(a + b/x)*(c + d/x)**3` | $\sqrt{a + \frac{b}{x}} \left(c + \frac{d}{x}\right)^{3}$ |
| partial | parametric | `sqrt(a + b/x)*(c + d/x)**2` | $\sqrt{a + \frac{b}{x}} \left(c + \frac{d}{x}\right)^{2}$ |
| partial | parametric | `sqrt(a + b/x)*(c + d/x)` | $\sqrt{a + \frac{b}{x}} \left(c + \frac{d}{x}\right)$ |
| partial | parametric | `sqrt(a + b/x)` | $\sqrt{a + \frac{b}{x}}$ |
| partial | parametric | `sqrt(a + b/x)/(c + d/x)` | $\frac{\sqrt{a + \frac{b}{x}}}{c + \frac{d}{x}}$ |
| partial | parametric | `sqrt(a + b/x)/(c + d/x)**2` | $\frac{\sqrt{a + \frac{b}{x}}}{\left(c + \frac{d}{x}\right)^{2}}$ |
| partial | parametric | `sqrt(a + b/x)/(c + d/x)**3` | $\frac{\sqrt{a + \frac{b}{x}}}{\left(c + \frac{d}{x}\right)^{3}}$ |
| partial | parametric | `(a + b/x)**(3/2)*(c + d/x)**3` | $\left(a + \frac{b}{x}\right)^{\frac{3}{2}} \left(c + \frac{d}{x}\right)^{3}$ |
| partial | parametric | `(a + b/x)**(3/2)*(c + d/x)**2` | $\left(a + \frac{b}{x}\right)^{\frac{3}{2}} \left(c + \frac{d}{x}\right)^{2}$ |
| partial | parametric | `(a + b/x)**(3/2)*(c + d/x)` | $\left(a + \frac{b}{x}\right)^{\frac{3}{2}} \left(c + \frac{d}{x}\right)$ |
| partial | parametric | `(a + b/x)**(3/2)` | $\left(a + \frac{b}{x}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x)**(3/2)/(c + d/x)` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{c + \frac{d}{x}}$ |
| partial | parametric | `(a + b/x)**(3/2)/(c + d/x)**2` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{\left(c + \frac{d}{x}\right)^{2}}$ |
| partial | parametric | `(a + b/x)**(3/2)/(c + d/x)**3` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}{\left(c + \frac{d}{x}\right)^{3}}$ |
| partial | parametric | `(a + b/x)**(5/2)*(c + d/x)**3` | $\left(a + \frac{b}{x}\right)^{\frac{5}{2}} \left(c + \frac{d}{x}\right)^{3}$ |
| partial | parametric | `(a + b/x)**(5/2)*(c + d/x)**2` | $\left(a + \frac{b}{x}\right)^{\frac{5}{2}} \left(c + \frac{d}{x}\right)^{2}$ |
| partial | parametric | `(a + b/x)**(5/2)*(c + d/x)` | $\left(a + \frac{b}{x}\right)^{\frac{5}{2}} \left(c + \frac{d}{x}\right)$ |
| partial | parametric | `(a + b/x)**(5/2)` | $\left(a + \frac{b}{x}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b/x)**(5/2)/(c + d/x)` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}{c + \frac{d}{x}}$ |
| partial | parametric | `(a + b/x)**(5/2)/(c + d/x)**2` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}{\left(c + \frac{d}{x}\right)^{2}}$ |
| partial | parametric | `(a + b/x)**(5/2)/(c + d/x)**3` | $\frac{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}{\left(c + \frac{d}{x}\right)^{3}}$ |
| partial | parametric | `(c + d/x)**3/sqrt(a + b/x)` | $\frac{\left(c + \frac{d}{x}\right)^{3}}{\sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `(c + d/x)**2/sqrt(a + b/x)` | $\frac{\left(c + \frac{d}{x}\right)^{2}}{\sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `(c + d/x)/sqrt(a + b/x)` | $\frac{c + \frac{d}{x}}{\sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `1/sqrt(a + b/x)` | $\frac{1}{\sqrt{a + \frac{b}{x}}}$ |
| partial | parametric | `1/(sqrt(a + b/x)*(c + d/x))` | $\frac{1}{\sqrt{a + \frac{b}{x}} \left(c + \frac{d}{x}\right)}$ |
| partial | parametric | `1/(sqrt(a + b/x)*(c + d/x)**2)` | $\frac{1}{\sqrt{a + \frac{b}{x}} \left(c + \frac{d}{x}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(a + b/x)*(c + d/x)**3)` | $\frac{1}{\sqrt{a + \frac{b}{x}} \left(c + \frac{d}{x}\right)^{3}}$ |
| partial | parametric | `(c + d/x)**3/(a + b/x)**(3/2)` | $\frac{\left(c + \frac{d}{x}\right)^{3}}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d/x)**2/(a + b/x)**(3/2)` | $\frac{\left(c + \frac{d}{x}\right)^{2}}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d/x)/(a + b/x)**(3/2)` | $\frac{c + \frac{d}{x}}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x)**(-3/2)` | $\frac{1}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b/x)**(3/2)*(c + d/x))` | $\frac{1}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}} \left(c + \frac{d}{x}\right)}$ |
| partial | parametric | `1/((a + b/x)**(3/2)*(c + d/x)**2)` | $\frac{1}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}} \left(c + \frac{d}{x}\right)^{2}}$ |
| partial | parametric | `1/((a + b/x)**(3/2)*(c + d/x)**3)` | $\frac{1}{\left(a + \frac{b}{x}\right)^{\frac{3}{2}} \left(c + \frac{d}{x}\right)^{3}}$ |
| partial | parametric | `(c + d/x)**3/(a + b/x)**(5/2)` | $\frac{\left(c + \frac{d}{x}\right)^{3}}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d/x)**2/(a + b/x)**(5/2)` | $\frac{\left(c + \frac{d}{x}\right)^{2}}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d/x)/(a + b/x)**(5/2)` | $\frac{c + \frac{d}{x}}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b/x)**(-5/2)` | $\frac{1}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((a + b/x)**(5/2)*(c + d/x))` | $\frac{1}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}} \left(c + \frac{d}{x}\right)}$ |
| partial | parametric | `1/((a + b/x)**(5/2)*(c + d/x)**2)` | $\frac{1}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}} \left(c + \frac{d}{x}\right)^{2}}$ |
| partial | parametric | `1/((a + b/x)**(5/2)*(c + d/x)**3)` | $\frac{1}{\left(a + \frac{b}{x}\right)^{\frac{5}{2}} \left(c + \frac{d}{x}\right)^{3}}$ |
| partial | parametric | `sqrt(a + b/x)*sqrt(c + d/x)` | $\sqrt{a + \frac{b}{x}} \sqrt{c + \frac{d}{x}}$ |
| partial | parametric | `sqrt(a + b/x)/sqrt(c + d/x)` | $\frac{\sqrt{a + \frac{b}{x}}}{\sqrt{c + \frac{d}{x}}}$ |
| timeout | parametric | `sqrt(a + b/x)/(c + d/x)**(3/2)` | $\frac{\sqrt{a + \frac{b}{x}}}{\left(c + \frac{d}{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b/x**2)*sqrt(c + d/x**2)` | $\sqrt{a + \frac{b}{x^{2}}} \sqrt{c + \frac{d}{x^{2}}}$ |
| partial | parametric | `sqrt(a + b/x**2)/sqrt(c + d/x**2)` | $\frac{\sqrt{a + \frac{b}{x^{2}}}}{\sqrt{c + \frac{d}{x^{2}}}}$ |
| partial | parametric | `sqrt(a + b/x**2)/(c + d/x**2)**(3/2)` | $\frac{\sqrt{a + \frac{b}{x^{2}}}}{\left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*sqrt(x))/(c + d*sqrt(x))` | $\frac{a + b \sqrt{x}}{c + d \sqrt{x}}$ |
| partial | concrete | `(x**(1/3) - 1)/(x**(1/3) + 1)` | $\frac{\sqrt[3]{x} - 1}{\sqrt[3]{x} + 1}$ |
| partial | concrete | `(x**(2/3) + 1)/(x**(2/3) - 1)` | $\frac{x^{\frac{2}{3}} + 1}{x^{\frac{2}{3}} - 1}$ |
| partial | concrete | `(x**(3/4) - 16)/(x**(3/4) + 16)` | $\frac{x^{\frac{3}{4}} - 16}{x^{\frac{3}{4}} + 16}$ |
| partial | concrete | `(1 + x**(-1/3))/(-1 + x**(-1/3))` | $\frac{1 + \frac{1}{\sqrt[3]{x}}}{-1 + \frac{1}{\sqrt[3]{x}}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(-c + d*x)*sqrt(c + d*x)/x` | $\frac{\left(a + b x^{2}\right) \sqrt{- c + d x} \sqrt{c + d x}}{x}$ |
| timeout | parametric | `x**4*(a + b*x**2)*sqrt(-c + d*x)*sqrt(c + d*x)` | $x^{4} \left(a + b x^{2}\right) \sqrt{- c + d x} \sqrt{c + d x}$ |
| partial | parametric | `x**2*(a + b*x**2)*sqrt(-c + d*x)*sqrt(c + d*x)` | $x^{2} \left(a + b x^{2}\right) \sqrt{- c + d x} \sqrt{c + d x}$ |
| partial | parametric | `(a + b*x**2)*sqrt(-c + d*x)*sqrt(c + d*x)` | $\left(a + b x^{2}\right) \sqrt{- c + d x} \sqrt{c + d x}$ |
| partial | parametric | `(a + b*x**2)*sqrt(-c + d*x)*sqrt(c + d*x)/x**2` | $\frac{\left(a + b x^{2}\right) \sqrt{- c + d x} \sqrt{c + d x}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2)*sqrt(-c + d*x)*sqrt(c + d*x)/x**4` | $\frac{\left(a + b x^{2}\right) \sqrt{- c + d x} \sqrt{c + d x}}{x^{4}}$ |
| partial | parametric | `x**4*(a + b*x**2)/(sqrt(c*x - 1)*sqrt(c*x + 1))` | $\frac{x^{4} \left(a + b x^{2}\right)}{\sqrt{c x - 1} \sqrt{c x + 1}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)/(sqrt(c*x - 1)*sqrt(c*x + 1))` | $\frac{x^{3} \left(a + b x^{2}\right)}{\sqrt{c x - 1} \sqrt{c x + 1}}$ |
| partial | parametric | `x**2*(a + b*x**2)/(sqrt(c*x - 1)*sqrt(c*x + 1))` | $\frac{x^{2} \left(a + b x^{2}\right)}{\sqrt{c x - 1} \sqrt{c x + 1}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)/(sqrt(c*x - 1)*sqrt(c*x + 1))` | $\frac{x \left(a + b x^{2}\right)}{\sqrt{c x - 1} \sqrt{c x + 1}}$ |
| partial | parametric | `(a + b*x**2)/(sqrt(c*x - 1)*sqrt(c*x + 1))` | $\frac{a + b x^{2}}{\sqrt{c x - 1} \sqrt{c x + 1}}$ |
| partial | parametric | `(a + b*x**2)/(x*sqrt(c*x - 1)*sqrt(c*x + 1))` | $\frac{a + b x^{2}}{x \sqrt{c x - 1} \sqrt{c x + 1}}$ |
| partial | parametric | `(a + b*x**2)/(x**2*sqrt(c*x - 1)*sqrt(c*x + 1))` | $\frac{a + b x^{2}}{x^{2} \sqrt{c x - 1} \sqrt{c x + 1}}$ |
| partial | parametric | `(a + b*x**2)/(x**3*sqrt(c*x - 1)*sqrt(c*x + 1))` | $\frac{a + b x^{2}}{x^{3} \sqrt{c x - 1} \sqrt{c x + 1}}$ |
| SOLVED-both | parametric | `(a + b*x**2)/(x**4*sqrt(c*x - 1)*sqrt(c*x + 1))` | $\frac{a + b x^{2}}{x^{4} \sqrt{c x - 1} \sqrt{c x + 1}}$ |
| partial | parametric | `(a + b*x**2)/(x**5*sqrt(c*x - 1)*sqrt(c*x + 1))` | $\frac{a + b x^{2}}{x^{5} \sqrt{c x - 1} \sqrt{c x + 1}}$ |
| timeout | parametric | `x**4*(a + b*x**2)/(sqrt(-c + d*x)*sqrt(c + d*x))` | $\frac{x^{4} \left(a + b x^{2}\right)}{\sqrt{- c + d x} \sqrt{c + d x}}$ |
| SOLVED-both | parametric | `x**3*(a + b*x**2)/(sqrt(-c + d*x)*sqrt(c + d*x))` | $\frac{x^{3} \left(a + b x^{2}\right)}{\sqrt{- c + d x} \sqrt{c + d x}}$ |
| partial | parametric | `x**2*(a + b*x**2)/(sqrt(-c + d*x)*sqrt(c + d*x))` | $\frac{x^{2} \left(a + b x^{2}\right)}{\sqrt{- c + d x} \sqrt{c + d x}}$ |
| SOLVED-both | parametric | `x*(a + b*x**2)/(sqrt(-c + d*x)*sqrt(c + d*x))` | $\frac{x \left(a + b x^{2}\right)}{\sqrt{- c + d x} \sqrt{c + d x}}$ |
| partial | parametric | `(a + b*x**2)/(sqrt(-c + d*x)*sqrt(c + d*x))` | $\frac{a + b x^{2}}{\sqrt{- c + d x} \sqrt{c + d x}}$ |
| partial | parametric | `(a + b*x**2)/(x*sqrt(-c + d*x)*sqrt(c + d*x))` | $\frac{a + b x^{2}}{x \sqrt{- c + d x} \sqrt{c + d x}}$ |
| partial | parametric | `(a + b*x**2)/(x**2*sqrt(-c + d*x)*sqrt(c + d*x))` | $\frac{a + b x^{2}}{x^{2} \sqrt{- c + d x} \sqrt{c + d x}}$ |
| partial | parametric | `(a + b*x**2)/(x**3*sqrt(-c + d*x)*sqrt(c + d*x))` | $\frac{a + b x^{2}}{x^{3} \sqrt{- c + d x} \sqrt{c + d x}}$ |
| SOLVED-both | parametric | `(a + b*x**2)/(x**4*sqrt(-c + d*x)*sqrt(c + d*x))` | $\frac{a + b x^{2}}{x^{4} \sqrt{- c + d x} \sqrt{c + d x}}$ |
| partial | parametric | `(a + b*x**2)/(x**5*sqrt(-c + d*x)*sqrt(c + d*x))` | $\frac{a + b x^{2}}{x^{5} \sqrt{- c + d x} \sqrt{c + d x}}$ |
| timeout | parametric | `x**4*(a + b*x**2)/((-c + d*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{x^{4} \left(a + b x^{2}\right)}{\left(- c + d x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**3*(a + b*x**2)/((-c + d*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{x^{3} \left(a + b x^{2}\right)}{\left(- c + d x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(a + b*x**2)/((-c + d*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{x^{2} \left(a + b x^{2}\right)}{\left(- c + d x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x*(a + b*x**2)/((-c + d*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{x \left(a + b x^{2}\right)}{\left(- c + d x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)/((-c + d*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{a + b x^{2}}{\left(- c + d x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)/(x*(-c + d*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{a + b x^{2}}{x \left(- c + d x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)/(x**2*(-c + d*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{a + b x^{2}}{x^{2} \left(- c + d x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)/(x**3*(-c + d*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{a + b x^{2}}{x^{3} \left(- c + d x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2)/(x**4*(-c + d*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{a + b x^{2}}{x^{4} \left(- c + d x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2)/(x**5*(-c + d*x)**(3/2)*(c + d*x)**(3/2))` | $\frac{a + b x^{2}}{x^{5} \left(- c + d x\right)^{\frac{3}{2}} \left(c + d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c**2*x**2 + 1)/(x*sqrt(c*x - 1)*sqrt(c*x + 1))` | $\frac{c^{2} x^{2} + 1}{x \sqrt{c x - 1} \sqrt{c x + 1}}$ |
| NIE | concrete | `1/(sqrt(-sqrt(x) - 1)*sqrt(sqrt(x) - 1)*sqrt(x + 1))` | $\frac{1}{\sqrt{- \sqrt{x} - 1} \sqrt{\sqrt{x} - 1} \sqrt{x + 1}}$ |
| NIE | parametric | `1/(sqrt(a - b*sqrt(x))*sqrt(a + b*sqrt(x))*sqrt(a**2 + b**2*x))` | $\frac{1}{\sqrt{a - b \sqrt{x}} \sqrt{a + b \sqrt{x}} \sqrt{a^{2} + b^{2} x}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x**3)*(a + b*x**3)` | $x^{\frac{7}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x**3)*(a + b*x**3)` | $x^{\frac{5}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x**3)*(a + b*x**3)` | $x^{\frac{3}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x**3)*(a + b*x**3)` | $\sqrt{x} \left(A + B x^{3}\right) \left(a + b x^{3}\right)$ |
| SOLVED-both | parametric | `(A + B*x**3)*(a + b*x**3)/sqrt(x)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x**3)*(a + b*x**3)/x**(3/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**3)*(a + b*x**3)/x**(5/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**3)*(a + b*x**3)/x**(7/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x**3)*(a + b*x**3)**2` | $x^{\frac{7}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{2}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x**3)*(a + b*x**3)**2` | $x^{\frac{5}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x**3)*(a + b*x**3)**2` | $x^{\frac{3}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x**3)*(a + b*x**3)**2` | $\sqrt{x} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x**3)*(a + b*x**3)**2/sqrt(x)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x**3)*(a + b*x**3)**2/x**(3/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**3)*(a + b*x**3)**2/x**(5/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**3)*(a + b*x**3)**2/x**(7/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x**3)*(a + b*x**3)**3` | $x^{\frac{7}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{3}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x**3)*(a + b*x**3)**3` | $x^{\frac{5}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x**3)*(a + b*x**3)**3` | $x^{\frac{3}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x**3)*(a + b*x**3)**3` | $\sqrt{x} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{3}$ |
| SOLVED-both | parametric | `(A + B*x**3)*(a + b*x**3)**3/sqrt(x)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x**3)*(a + b*x**3)**3/x**(3/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**3)*(a + b*x**3)**3/x**(5/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**3)*(a + b*x**3)**3/x**(7/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{3}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x**3)/(a + b*x**3)` | $\frac{x^{\frac{7}{2}} \left(A + B x^{3}\right)}{a + b x^{3}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**3)/(a + b*x**3)` | $\frac{x^{\frac{5}{2}} \left(A + B x^{3}\right)}{a + b x^{3}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**3)/(a + b*x**3)` | $\frac{x^{\frac{3}{2}} \left(A + B x^{3}\right)}{a + b x^{3}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**3)/(a + b*x**3)` | $\frac{\sqrt{x} \left(A + B x^{3}\right)}{a + b x^{3}}$ |
| partial | parametric | `(A + B*x**3)/(sqrt(x)*(a + b*x**3))` | $\frac{A + B x^{3}}{\sqrt{x} \left(a + b x^{3}\right)}$ |
| partial | parametric | `(A + B*x**3)/(x**(3/2)*(a + b*x**3))` | $\frac{A + B x^{3}}{x^{\frac{3}{2}} \left(a + b x^{3}\right)}$ |
| partial | parametric | `(A + B*x**3)/(x**(5/2)*(a + b*x**3))` | $\frac{A + B x^{3}}{x^{\frac{5}{2}} \left(a + b x^{3}\right)}$ |
| partial | parametric | `(A + B*x**3)/(x**(7/2)*(a + b*x**3))` | $\frac{A + B x^{3}}{x^{\frac{7}{2}} \left(a + b x^{3}\right)}$ |
| partial | parametric | `x**(7/2)*(A + B*x**3)/(a + b*x**3)**2` | $\frac{x^{\frac{7}{2}} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**3)/(a + b*x**3)**2` | $\frac{x^{\frac{5}{2}} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**3)/(a + b*x**3)**2` | $\frac{x^{\frac{3}{2}} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**3)/(a + b*x**3)**2` | $\frac{\sqrt{x} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `(A + B*x**3)/(sqrt(x)*(a + b*x**3)**2)` | $\frac{A + B x^{3}}{\sqrt{x} \left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `(A + B*x**3)/(x**(3/2)*(a + b*x**3)**2)` | $\frac{A + B x^{3}}{x^{\frac{3}{2}} \left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `(A + B*x**3)/(x**(5/2)*(a + b*x**3)**2)` | $\frac{A + B x^{3}}{x^{\frac{5}{2}} \left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `(A + B*x**3)/(x**(7/2)*(a + b*x**3)**2)` | $\frac{A + B x^{3}}{x^{\frac{7}{2}} \left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x**(7/2)*(A + B*x**3)/(a + b*x**3)**3` | $\frac{x^{\frac{7}{2}} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{3}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**3)/(a + b*x**3)**3` | $\frac{x^{\frac{5}{2}} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{3}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**3)/(a + b*x**3)**3` | $\frac{x^{\frac{3}{2}} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{3}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**3)/(a + b*x**3)**3` | $\frac{\sqrt{x} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{3}}$ |
| partial | parametric | `(A + B*x**3)/(sqrt(x)*(a + b*x**3)**3)` | $\frac{A + B x^{3}}{\sqrt{x} \left(a + b x^{3}\right)^{3}}$ |
| partial | parametric | `(A + B*x**3)/(x**(3/2)*(a + b*x**3)**3)` | $\frac{A + B x^{3}}{x^{\frac{3}{2}} \left(a + b x^{3}\right)^{3}}$ |
| partial | parametric | `(A + B*x**3)/(x**(5/2)*(a + b*x**3)**3)` | $\frac{A + B x^{3}}{x^{\frac{5}{2}} \left(a + b x^{3}\right)^{3}}$ |
| partial | parametric | `(A + B*x**3)/(x**(7/2)*(a + b*x**3)**3)` | $\frac{A + B x^{3}}{x^{\frac{7}{2}} \left(a + b x^{3}\right)^{3}}$ |
| SOLVED-both | parametric | `x**8*(A + B*x**3)*sqrt(a + b*x**3)` | $x^{8} \left(A + B x^{3}\right) \sqrt{a + b x^{3}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x**3)*sqrt(a + b*x**3)` | $x^{5} \left(A + B x^{3}\right) \sqrt{a + b x^{3}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x**3)*sqrt(a + b*x**3)` | $x^{2} \left(A + B x^{3}\right) \sqrt{a + b x^{3}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x**4` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x^{4}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x**7` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x^{7}}$ |
| partial | parametric | `x**3*(A + B*x**3)*sqrt(a + b*x**3)` | $x^{3} \left(A + B x^{3}\right) \sqrt{a + b x^{3}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)` | $\left(A + B x^{3}\right) \sqrt{a + b x^{3}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x**3` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x^{3}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x**6` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x^{6}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x**9` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x^{9}}$ |
| partial | parametric | `x**4*(A + B*x**3)*sqrt(a + b*x**3)` | $x^{4} \left(A + B x^{3}\right) \sqrt{a + b x^{3}}$ |
| partial | parametric | `x*(A + B*x**3)*sqrt(a + b*x**3)` | $x \left(A + B x^{3}\right) \sqrt{a + b x^{3}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x**2` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x^{2}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x**5` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x^{5}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x**8` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x^{8}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x**11` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x^{11}}$ |
| SOLVED-both | parametric | `x**8*(A + B*x**3)*(a + b*x**3)**(3/2)` | $x^{8} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x**3)*(a + b*x**3)**(3/2)` | $x^{5} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x**3)*(a + b*x**3)**(3/2)` | $x^{2} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/x` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/x**4` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/x**7` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `x**3*(A + B*x**3)*(a + b*x**3)**(3/2)` | $x^{3} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)` | $\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/x**3` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/x**6` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/x**9` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{9}}$ |
| partial | parametric | `x**4*(A + B*x**3)*(a + b*x**3)**(3/2)` | $x^{4} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(A + B*x**3)*(a + b*x**3)**(3/2)` | $x \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/x**2` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/x**5` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/x**8` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{8}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/x**11` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{x^{11}}$ |
| SOLVED-both | parametric | `x**8*(A + B*x**3)/sqrt(a + b*x**3)` | $\frac{x^{8} \left(A + B x^{3}\right)}{\sqrt{a + b x^{3}}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x**3)/sqrt(a + b*x**3)` | $\frac{x^{5} \left(A + B x^{3}\right)}{\sqrt{a + b x^{3}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x**3)/sqrt(a + b*x**3)` | $\frac{x^{2} \left(A + B x^{3}\right)}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/(x*sqrt(a + b*x**3))` | $\frac{A + B x^{3}}{x \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/(x**4*sqrt(a + b*x**3))` | $\frac{A + B x^{3}}{x^{4} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/(x**7*sqrt(a + b*x**3))` | $\frac{A + B x^{3}}{x^{7} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `x**3*(A + B*x**3)/sqrt(a + b*x**3)` | $\frac{x^{3} \left(A + B x^{3}\right)}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/sqrt(a + b*x**3)` | $\frac{A + B x^{3}}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/(x**3*sqrt(a + b*x**3))` | $\frac{A + B x^{3}}{x^{3} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/(x**6*sqrt(a + b*x**3))` | $\frac{A + B x^{3}}{x^{6} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `x**4*(A + B*x**3)/sqrt(a + b*x**3)` | $\frac{x^{4} \left(A + B x^{3}\right)}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `x*(A + B*x**3)/sqrt(a + b*x**3)` | $\frac{x \left(A + B x^{3}\right)}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/(x**2*sqrt(a + b*x**3))` | $\frac{A + B x^{3}}{x^{2} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/(x**5*sqrt(a + b*x**3))` | $\frac{A + B x^{3}}{x^{5} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/(x**8*sqrt(a + b*x**3))` | $\frac{A + B x^{3}}{x^{8} \sqrt{a + b x^{3}}}$ |
| SOLVED-both | parametric | `x**8*(A + B*x**3)/(a + b*x**3)**(3/2)` | $\frac{x^{8} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x**3)/(a + b*x**3)**(3/2)` | $\frac{x^{5} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x**3)/(a + b*x**3)**(3/2)` | $\frac{x^{2} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x*(a + b*x**3)**(3/2))` | $\frac{A + B x^{3}}{x \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x**4*(a + b*x**3)**(3/2))` | $\frac{A + B x^{3}}{x^{4} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x**7*(a + b*x**3)**(3/2))` | $\frac{A + B x^{3}}{x^{7} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**6*(A + B*x**3)/(a + b*x**3)**(3/2)` | $\frac{x^{6} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*(A + B*x**3)/(a + b*x**3)**(3/2)` | $\frac{x^{3} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(a + b*x**3)**(3/2)` | $\frac{A + B x^{3}}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x**3*(a + b*x**3)**(3/2))` | $\frac{A + B x^{3}}{x^{3} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x**6*(a + b*x**3)**(3/2))` | $\frac{A + B x^{3}}{x^{6} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4*(A + B*x**3)/(a + b*x**3)**(3/2)` | $\frac{x^{4} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(A + B*x**3)/(a + b*x**3)**(3/2)` | $\frac{x \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x**2*(a + b*x**3)**(3/2))` | $\frac{A + B x^{3}}{x^{2} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x**5*(a + b*x**3)**(3/2))` | $\frac{A + B x^{3}}{x^{5} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x**8*(a + b*x**3)**(3/2))` | $\frac{A + B x^{3}}{x^{8} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**8*(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{x^{8} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{x^{5} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{x^{2} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x*(a + b*x**3)**(5/2))` | $\frac{A + B x^{3}}{x \left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x**4*(a + b*x**3)**(5/2))` | $\frac{A + B x^{3}}{x^{4} \left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**6*(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{x^{6} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3*(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{x^{3} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{A + B x^{3}}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x**3*(a + b*x**3)**(5/2))` | $\frac{A + B x^{3}}{x^{3} \left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x**6*(a + b*x**3)**(5/2))` | $\frac{A + B x^{3}}{x^{6} \left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**7*(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{x^{7} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4*(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{x^{4} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x*(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{x \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x**2*(a + b*x**3)**(5/2))` | $\frac{A + B x^{3}}{x^{2} \left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(x**5*(a + b*x**3)**(5/2))` | $\frac{A + B x^{3}}{x^{5} \left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**8*sqrt(c + d*x**3)/(4*c + d*x**3)` | $\frac{x^{8} \sqrt{c + d x^{3}}}{4 c + d x^{3}}$ |
| partial | parametric | `x**5*sqrt(c + d*x**3)/(4*c + d*x**3)` | $\frac{x^{5} \sqrt{c + d x^{3}}}{4 c + d x^{3}}$ |
| partial | parametric | `x**2*sqrt(c + d*x**3)/(4*c + d*x**3)` | $\frac{x^{2} \sqrt{c + d x^{3}}}{4 c + d x^{3}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x*(4*c + d*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**4*(4*c + d*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x^{4} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `x**4*sqrt(c + d*x**3)/(4*c + d*x**3)` | $\frac{x^{4} \sqrt{c + d x^{3}}}{4 c + d x^{3}}$ |
| partial | parametric | `x*sqrt(c + d*x**3)/(4*c + d*x**3)` | $\frac{x \sqrt{c + d x^{3}}}{4 c + d x^{3}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**2*(4*c + d*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x^{2} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `x**3*sqrt(c + d*x**3)/(4*c + d*x**3)` | $\frac{x^{3} \sqrt{c + d x^{3}}}{4 c + d x^{3}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(4*c + d*x**3)` | $\frac{\sqrt{c + d x^{3}}}{4 c + d x^{3}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**3*(4*c + d*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x^{3} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `x**8/(sqrt(c + d*x**3)*(4*c + d*x**3))` | $\frac{x^{8}}{\sqrt{c + d x^{3}} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `x**5/(sqrt(c + d*x**3)*(4*c + d*x**3))` | $\frac{x^{5}}{\sqrt{c + d x^{3}} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `x**2/(sqrt(c + d*x**3)*(4*c + d*x**3))` | $\frac{x^{2}}{\sqrt{c + d x^{3}} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `1/(x*sqrt(c + d*x**3)*(4*c + d*x**3))` | $\frac{1}{x \sqrt{c + d x^{3}} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `1/(x**4*sqrt(c + d*x**3)*(4*c + d*x**3))` | $\frac{1}{x^{4} \sqrt{c + d x^{3}} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `x**4/(sqrt(c + d*x**3)*(4*c + d*x**3))` | $\frac{x^{4}}{\sqrt{c + d x^{3}} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `x/(sqrt(c + d*x**3)*(4*c + d*x**3))` | $\frac{x}{\sqrt{c + d x^{3}} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `1/(x**2*sqrt(c + d*x**3)*(4*c + d*x**3))` | $\frac{1}{x^{2} \sqrt{c + d x^{3}} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `x**3/(sqrt(c + d*x**3)*(4*c + d*x**3))` | $\frac{x^{3}}{\sqrt{c + d x^{3}} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `1/(sqrt(c + d*x**3)*(4*c + d*x**3))` | $\frac{1}{\sqrt{c + d x^{3}} \left(4 c + d x^{3}\right)}$ |
| partial | parametric | `1/(x**3*sqrt(c + d*x**3)*(4*c + d*x**3))` | $\frac{1}{x^{3} \sqrt{c + d x^{3}} \left(4 c + d x^{3}\right)}$ |
| partial | concrete | `x/(sqrt(1 - x**3)*(4 - x**3))` | $\frac{x}{\sqrt{1 - x^{3}} \left(4 - x^{3}\right)}$ |
| partial | parametric | `x**11*sqrt(c + d*x**3)/(8*c - d*x**3)` | $\frac{x^{11} \sqrt{c + d x^{3}}}{8 c - d x^{3}}$ |
| partial | parametric | `x**8*sqrt(c + d*x**3)/(8*c - d*x**3)` | $\frac{x^{8} \sqrt{c + d x^{3}}}{8 c - d x^{3}}$ |
| partial | parametric | `x**5*sqrt(c + d*x**3)/(8*c - d*x**3)` | $\frac{x^{5} \sqrt{c + d x^{3}}}{8 c - d x^{3}}$ |
| partial | parametric | `x**2*sqrt(c + d*x**3)/(8*c - d*x**3)` | $\frac{x^{2} \sqrt{c + d x^{3}}}{8 c - d x^{3}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x*(8*c - d*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**4*(8*c - d*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x^{4} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**7*(8*c - d*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x^{7} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**7*sqrt(c + d*x**3)/(8*c - d*x**3)` | $\frac{x^{7} \sqrt{c + d x^{3}}}{8 c - d x^{3}}$ |
| partial | parametric | `x**4*sqrt(c + d*x**3)/(8*c - d*x**3)` | $\frac{x^{4} \sqrt{c + d x^{3}}}{8 c - d x^{3}}$ |
| partial | parametric | `x*sqrt(c + d*x**3)/(8*c - d*x**3)` | $\frac{x \sqrt{c + d x^{3}}}{8 c - d x^{3}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**2*(8*c - d*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x^{2} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**5*(8*c - d*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x^{5} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**8*(8*c - d*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x^{8} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**11*(c + d*x**3)**(3/2)/(8*c - d*x**3)` | $\frac{x^{11} \left(c + d x^{3}\right)^{\frac{3}{2}}}{8 c - d x^{3}}$ |
| partial | parametric | `x**8*(c + d*x**3)**(3/2)/(8*c - d*x**3)` | $\frac{x^{8} \left(c + d x^{3}\right)^{\frac{3}{2}}}{8 c - d x^{3}}$ |
| partial | parametric | `x**5*(c + d*x**3)**(3/2)/(8*c - d*x**3)` | $\frac{x^{5} \left(c + d x^{3}\right)^{\frac{3}{2}}}{8 c - d x^{3}}$ |
| partial | parametric | `x**2*(c + d*x**3)**(3/2)/(8*c - d*x**3)` | $\frac{x^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}{8 c - d x^{3}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x*(8*c - d*x**3))` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**4*(8*c - d*x**3))` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{4} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**7*(8*c - d*x**3))` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{7} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**7*(c + d*x**3)**(3/2)/(8*c - d*x**3)` | $\frac{x^{7} \left(c + d x^{3}\right)^{\frac{3}{2}}}{8 c - d x^{3}}$ |
| partial | parametric | `x**4*(c + d*x**3)**(3/2)/(8*c - d*x**3)` | $\frac{x^{4} \left(c + d x^{3}\right)^{\frac{3}{2}}}{8 c - d x^{3}}$ |
| partial | parametric | `x*(c + d*x**3)**(3/2)/(8*c - d*x**3)` | $\frac{x \left(c + d x^{3}\right)^{\frac{3}{2}}}{8 c - d x^{3}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**2*(8*c - d*x**3))` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{2} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**5*(8*c - d*x**3))` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{5} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**8*(8*c - d*x**3))` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{8} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**11/(sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{x^{11}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**8/(sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{x^{8}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**5/(sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{x^{5}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**2/(sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{x^{2}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x*sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{1}{x \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**4*sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{1}{x^{4} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**7*sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{1}{x^{7} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**7/(sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{x^{7}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**4/(sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{x^{4}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x/(sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{x}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**2*sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{1}{x^{2} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**5*sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{1}{x^{5} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**8*sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{1}{x^{8} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**3/(sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{x^{3}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{1}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**3*sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{1}{x^{3} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**6*sqrt(c + d*x**3)*(8*c - d*x**3))` | $\frac{1}{x^{6} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**11/((c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{x^{11}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**8/((c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{x^{8}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**5/((c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{x^{5}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**2/((c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{x^{2}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x*(c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{1}{x \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**4*(c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{1}{x^{4} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**7*(c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{1}{x^{7} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**7/((c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{x^{7}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**4/((c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{x^{4}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x/((c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{x}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**2*(c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{1}{x^{2} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**5*(c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{1}{x^{5} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**8*(c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{1}{x^{8} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x**3/((c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{x^{3}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/((c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{1}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**3*(c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{1}{x^{3} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `1/(x**6*(c + d*x**3)**(3/2)*(8*c - d*x**3))` | $\frac{1}{x^{6} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)}$ |
| partial | parametric | `x*sqrt(a + b*x**3)/(a*(10 + 6*sqrt(3)) + b*x**3)` | $\frac{x \sqrt{a + b x^{3}}}{a \left(10 + 6 \sqrt{3}\right) + b x^{3}}$ |
| partial | parametric | `x*sqrt(a - b*x**3)/(a*(10 + 6*sqrt(3)) - b*x**3)` | $\frac{x \sqrt{a - b x^{3}}}{a \left(10 + 6 \sqrt{3}\right) - b x^{3}}$ |
| partial | parametric | `x*sqrt(-a + b*x**3)/(a*(-6*sqrt(3) - 10) + b*x**3)` | $\frac{x \sqrt{- a + b x^{3}}}{a \left(- 6 \sqrt{3} - 10\right) + b x^{3}}$ |
| partial | parametric | `x*sqrt(-a - b*x**3)/(a*(-6*sqrt(3) - 10) - b*x**3)` | $\frac{x \sqrt{- a - b x^{3}}}{a \left(- 6 \sqrt{3} - 10\right) - b x^{3}}$ |
| partial | parametric | `x*sqrt(a + b*x**3)/(a*(10 - 6*sqrt(3)) + b*x**3)` | $\frac{x \sqrt{a + b x^{3}}}{a \left(10 - 6 \sqrt{3}\right) + b x^{3}}$ |
| partial | parametric | `x*sqrt(a - b*x**3)/(a*(10 - 6*sqrt(3)) - b*x**3)` | $\frac{x \sqrt{a - b x^{3}}}{a \left(10 - 6 \sqrt{3}\right) - b x^{3}}$ |
| partial | parametric | `x*sqrt(-a + b*x**3)/(a*(10 - 6*sqrt(3)) - b*x**3)` | $\frac{x \sqrt{- a + b x^{3}}}{a \left(10 - 6 \sqrt{3}\right) - b x^{3}}$ |
| partial | parametric | `x*sqrt(-a - b*x**3)/(a*(10 - 6*sqrt(3)) + b*x**3)` | $\frac{x \sqrt{- a - b x^{3}}}{a \left(10 - 6 \sqrt{3}\right) + b x^{3}}$ |
| partial | parametric | `x/(sqrt(a + b*x**3)*(a*(10 + 6*sqrt(3)) + b*x**3))` | $\frac{x}{\sqrt{a + b x^{3}} \left(a \left(10 + 6 \sqrt{3}\right) + b x^{3}\right)}$ |
| partial | parametric | `x/(sqrt(a - b*x**3)*(a*(10 + 6*sqrt(3)) - b*x**3))` | $\frac{x}{\sqrt{a - b x^{3}} \left(a \left(10 + 6 \sqrt{3}\right) - b x^{3}\right)}$ |
| partial | parametric | `x/(sqrt(-a + b*x**3)*(a*(-6*sqrt(3) - 10) + b*x**3))` | $\frac{x}{\sqrt{- a + b x^{3}} \left(a \left(- 6 \sqrt{3} - 10\right) + b x^{3}\right)}$ |
| partial | parametric | `x/(sqrt(-a - b*x**3)*(a*(-6*sqrt(3) - 10) - b*x**3))` | $\frac{x}{\sqrt{- a - b x^{3}} \left(a \left(- 6 \sqrt{3} - 10\right) - b x^{3}\right)}$ |
| partial | parametric | `x/(sqrt(a + b*x**3)*(a*(10 - 6*sqrt(3)) + b*x**3))` | $\frac{x}{\sqrt{a + b x^{3}} \left(a \left(10 - 6 \sqrt{3}\right) + b x^{3}\right)}$ |
| partial | parametric | `x/(sqrt(a - b*x**3)*(a*(10 - 6*sqrt(3)) - b*x**3))` | $\frac{x}{\sqrt{a - b x^{3}} \left(a \left(10 - 6 \sqrt{3}\right) - b x^{3}\right)}$ |
| partial | parametric | `x/(sqrt(-a + b*x**3)*(a*(10 - 6*sqrt(3)) - b*x**3))` | $\frac{x}{\sqrt{- a + b x^{3}} \left(a \left(10 - 6 \sqrt{3}\right) - b x^{3}\right)}$ |
| partial | parametric | `x/(sqrt(-a - b*x**3)*(a*(10 - 6*sqrt(3)) + b*x**3))` | $\frac{x}{\sqrt{- a - b x^{3}} \left(a \left(10 - 6 \sqrt{3}\right) + b x^{3}\right)}$ |
| partial | parametric | `x**8*sqrt(c + d*x**3)/(a + b*x**3)` | $\frac{x^{8} \sqrt{c + d x^{3}}}{a + b x^{3}}$ |
| partial | parametric | `x**5*sqrt(c + d*x**3)/(a + b*x**3)` | $\frac{x^{5} \sqrt{c + d x^{3}}}{a + b x^{3}}$ |
| partial | parametric | `x**2*sqrt(c + d*x**3)/(a + b*x**3)` | $\frac{x^{2} \sqrt{c + d x^{3}}}{a + b x^{3}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x*(a + b*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x \left(a + b x^{3}\right)}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**4*(a + b*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x^{4} \left(a + b x^{3}\right)}$ |
| partial | parametric | `x**3*sqrt(c + d*x**3)/(a + b*x**3)` | $\frac{x^{3} \sqrt{c + d x^{3}}}{a + b x^{3}}$ |
| partial | parametric | `x*sqrt(c + d*x**3)/(a + b*x**3)` | $\frac{x \sqrt{c + d x^{3}}}{a + b x^{3}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(a + b*x**3)` | $\frac{\sqrt{c + d x^{3}}}{a + b x^{3}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**2*(a + b*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x^{2} \left(a + b x^{3}\right)}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**3*(a + b*x**3))` | $\frac{\sqrt{c + d x^{3}}}{x^{3} \left(a + b x^{3}\right)}$ |
| partial | parametric | `x**8*(c + d*x**3)**(3/2)/(a + b*x**3)` | $\frac{x^{8} \left(c + d x^{3}\right)^{\frac{3}{2}}}{a + b x^{3}}$ |
| partial | parametric | `x**5*(c + d*x**3)**(3/2)/(a + b*x**3)` | $\frac{x^{5} \left(c + d x^{3}\right)^{\frac{3}{2}}}{a + b x^{3}}$ |
| partial | parametric | `x**2*(c + d*x**3)**(3/2)/(a + b*x**3)` | $\frac{x^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}{a + b x^{3}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x*(a + b*x**3))` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x \left(a + b x^{3}\right)}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**4*(a + b*x**3))` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{4} \left(a + b x^{3}\right)}$ |
| partial | parametric | `x**3*(c + d*x**3)**(3/2)/(a + b*x**3)` | $\frac{x^{3} \left(c + d x^{3}\right)^{\frac{3}{2}}}{a + b x^{3}}$ |
| partial | parametric | `x*(c + d*x**3)**(3/2)/(a + b*x**3)` | $\frac{x \left(c + d x^{3}\right)^{\frac{3}{2}}}{a + b x^{3}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(a + b*x**3)` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{a + b x^{3}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**2*(a + b*x**3))` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{2} \left(a + b x^{3}\right)}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**3*(a + b*x**3))` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{3} \left(a + b x^{3}\right)}$ |
| partial | parametric | `x**8/((a + b*x**3)*sqrt(c + d*x**3))` | $\frac{x^{8}}{\left(a + b x^{3}\right) \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x**5/((a + b*x**3)*sqrt(c + d*x**3))` | $\frac{x^{5}}{\left(a + b x^{3}\right) \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x**2/((a + b*x**3)*sqrt(c + d*x**3))` | $\frac{x^{2}}{\left(a + b x^{3}\right) \sqrt{c + d x^{3}}}$ |
| partial | parametric | `1/(x*(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{1}{x \left(a + b x^{3}\right) \sqrt{c + d x^{3}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{1}{x^{4} \left(a + b x^{3}\right) \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x**3/((a + b*x**3)*sqrt(c + d*x**3))` | $\frac{x^{3}}{\left(a + b x^{3}\right) \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x/((a + b*x**3)*sqrt(c + d*x**3))` | $\frac{x}{\left(a + b x^{3}\right) \sqrt{c + d x^{3}}}$ |
| partial | parametric | `1/((a + b*x**3)*sqrt(c + d*x**3))` | $\frac{1}{\left(a + b x^{3}\right) \sqrt{c + d x^{3}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{1}{x^{2} \left(a + b x^{3}\right) \sqrt{c + d x^{3}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{1}{x^{3} \left(a + b x^{3}\right) \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x**8/((a + b*x**3)*(c + d*x**3)**(3/2))` | $\frac{x^{8}}{\left(a + b x^{3}\right) \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5/((a + b*x**3)*(c + d*x**3)**(3/2))` | $\frac{x^{5}}{\left(a + b x^{3}\right) \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/((a + b*x**3)*(c + d*x**3)**(3/2))` | $\frac{x^{2}}{\left(a + b x^{3}\right) \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**3)*(c + d*x**3)**(3/2))` | $\frac{1}{x \left(a + b x^{3}\right) \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**3)*(c + d*x**3)**(3/2))` | $\frac{1}{x^{4} \left(a + b x^{3}\right) \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/((a + b*x**3)*(c + d*x**3)**(3/2))` | $\frac{x^{3}}{\left(a + b x^{3}\right) \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/((a + b*x**3)*(c + d*x**3)**(3/2))` | $\frac{x}{\left(a + b x^{3}\right) \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x**3)*(c + d*x**3)**(3/2))` | $\frac{1}{\left(a + b x^{3}\right) \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**3)*(c + d*x**3)**(3/2))` | $\frac{1}{x^{2} \left(a + b x^{3}\right) \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**3)*(c + d*x**3)**(3/2))` | $\frac{1}{x^{3} \left(a + b x^{3}\right) \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**11*sqrt(c + d*x**3)/(8*c - d*x**3)**2` | $\frac{x^{11} \sqrt{c + d x^{3}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**8*sqrt(c + d*x**3)/(8*c - d*x**3)**2` | $\frac{x^{8} \sqrt{c + d x^{3}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**5*sqrt(c + d*x**3)/(8*c - d*x**3)**2` | $\frac{x^{5} \sqrt{c + d x^{3}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**2*sqrt(c + d*x**3)/(8*c - d*x**3)**2` | $\frac{x^{2} \sqrt{c + d x^{3}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x*(8*c - d*x**3)**2)` | $\frac{\sqrt{c + d x^{3}}}{x \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**4*(8*c - d*x**3)**2)` | $\frac{\sqrt{c + d x^{3}}}{x^{4} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**7*(8*c - d*x**3)**2)` | $\frac{\sqrt{c + d x^{3}}}{x^{7} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**7*sqrt(c + d*x**3)/(8*c - d*x**3)**2` | $\frac{x^{7} \sqrt{c + d x^{3}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**4*sqrt(c + d*x**3)/(8*c - d*x**3)**2` | $\frac{x^{4} \sqrt{c + d x^{3}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x*sqrt(c + d*x**3)/(8*c - d*x**3)**2` | $\frac{x \sqrt{c + d x^{3}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**2*(8*c - d*x**3)**2)` | $\frac{\sqrt{c + d x^{3}}}{x^{2} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**5*(8*c - d*x**3)**2)` | $\frac{\sqrt{c + d x^{3}}}{x^{5} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**8*(8*c - d*x**3)**2)` | $\frac{\sqrt{c + d x^{3}}}{x^{8} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**11*(c + d*x**3)**(3/2)/(8*c - d*x**3)**2` | $\frac{x^{11} \left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**8*(c + d*x**3)**(3/2)/(8*c - d*x**3)**2` | $\frac{x^{8} \left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**5*(c + d*x**3)**(3/2)/(8*c - d*x**3)**2` | $\frac{x^{5} \left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**2*(c + d*x**3)**(3/2)/(8*c - d*x**3)**2` | $\frac{x^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x*(8*c - d*x**3)**2)` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**4*(8*c - d*x**3)**2)` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{4} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**7*(8*c - d*x**3)**2)` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{7} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**7*(c + d*x**3)**(3/2)/(8*c - d*x**3)**2` | $\frac{x^{7} \left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**4*(c + d*x**3)**(3/2)/(8*c - d*x**3)**2` | $\frac{x^{4} \left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x*(c + d*x**3)**(3/2)/(8*c - d*x**3)**2` | $\frac{x \left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**2*(8*c - d*x**3)**2)` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{2} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**5*(8*c - d*x**3)**2)` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{5} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**8*(8*c - d*x**3)**2)` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{8} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**11/(sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{x^{11}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**8/(sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{x^{8}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**5/(sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{x^{5}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**2/(sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{x^{2}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x*sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{1}{x \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**4*sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{1}{x^{4} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**7*sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{1}{x^{7} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**7/(sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{x^{7}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**4/(sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{x^{4}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x/(sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{x}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**2*sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{1}{x^{2} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**5*sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{1}{x^{5} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**8*sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{1}{x^{8} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**6/(sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{x^{6}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**3/(sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{x^{3}}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{1}{\sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**3*sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{1}{x^{3} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**6*sqrt(c + d*x**3)*(8*c - d*x**3)**2)` | $\frac{1}{x^{6} \sqrt{c + d x^{3}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**11/((c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{x^{11}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**8/((c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{x^{8}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**5/((c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{x^{5}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**2/((c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{x^{2}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x*(c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{1}{x \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**4*(c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{1}{x^{4} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**7*(c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{1}{x^{7} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**7/((c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{x^{7}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**4/((c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{x^{4}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x/((c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{x}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**2*(c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{1}{x^{2} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**5*(c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{1}{x^{5} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**8*(c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{1}{x^{8} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**6/((c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{x^{6}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**3/((c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{x^{3}}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/((c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{1}{\left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**3*(c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{1}{x^{3} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `1/(x**6*(c + d*x**3)**(3/2)*(8*c - d*x**3)**2)` | $\frac{1}{x^{6} \left(c + d x^{3}\right)^{\frac{3}{2}} \left(8 c - d x^{3}\right)^{2}}$ |
| partial | parametric | `x**8*sqrt(c + d*x**3)/(a + b*x**3)**2` | $\frac{x^{8} \sqrt{c + d x^{3}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x**5*sqrt(c + d*x**3)/(a + b*x**3)**2` | $\frac{x^{5} \sqrt{c + d x^{3}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x**2*sqrt(c + d*x**3)/(a + b*x**3)**2` | $\frac{x^{2} \sqrt{c + d x^{3}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x*(a + b*x**3)**2)` | $\frac{\sqrt{c + d x^{3}}}{x \left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**4*(a + b*x**3)**2)` | $\frac{\sqrt{c + d x^{3}}}{x^{4} \left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x**3*sqrt(c + d*x**3)/(a + b*x**3)**2` | $\frac{x^{3} \sqrt{c + d x^{3}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x*sqrt(c + d*x**3)/(a + b*x**3)**2` | $\frac{x \sqrt{c + d x^{3}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(a + b*x**3)**2` | $\frac{\sqrt{c + d x^{3}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**2*(a + b*x**3)**2)` | $\frac{\sqrt{c + d x^{3}}}{x^{2} \left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(x**3*(a + b*x**3)**2)` | $\frac{\sqrt{c + d x^{3}}}{x^{3} \left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x**8*(c + d*x**3)**(3/2)/(a + b*x**3)**2` | $\frac{x^{8} \left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x**5*(c + d*x**3)**(3/2)/(a + b*x**3)**2` | $\frac{x^{5} \left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x**2*(c + d*x**3)**(3/2)/(a + b*x**3)**2` | $\frac{x^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x*(a + b*x**3)**2)` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x \left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**4*(a + b*x**3)**2)` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{4} \left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x**3*(c + d*x**3)**(3/2)/(a + b*x**3)**2` | $\frac{x^{3} \left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x*(c + d*x**3)**(3/2)/(a + b*x**3)**2` | $\frac{x \left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(a + b*x**3)**2` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{\left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**2*(a + b*x**3)**2)` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{2} \left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `(c + d*x**3)**(3/2)/(x**3*(a + b*x**3)**2)` | $\frac{\left(c + d x^{3}\right)^{\frac{3}{2}}}{x^{3} \left(a + b x^{3}\right)^{2}}$ |
| partial | parametric | `x**8/((a + b*x**3)**2*sqrt(c + d*x**3))` | $\frac{x^{8}}{\left(a + b x^{3}\right)^{2} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x**5/((a + b*x**3)**2*sqrt(c + d*x**3))` | $\frac{x^{5}}{\left(a + b x^{3}\right)^{2} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x**2/((a + b*x**3)**2*sqrt(c + d*x**3))` | $\frac{x^{2}}{\left(a + b x^{3}\right)^{2} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `1/(x*(a + b*x**3)**2*sqrt(c + d*x**3))` | $\frac{1}{x \left(a + b x^{3}\right)^{2} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**3)**2*sqrt(c + d*x**3))` | $\frac{1}{x^{4} \left(a + b x^{3}\right)^{2} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x**3/((a + b*x**3)**2*sqrt(c + d*x**3))` | $\frac{x^{3}}{\left(a + b x^{3}\right)^{2} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x/((a + b*x**3)**2*sqrt(c + d*x**3))` | $\frac{x}{\left(a + b x^{3}\right)^{2} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `1/((a + b*x**3)**2*sqrt(c + d*x**3))` | $\frac{1}{\left(a + b x^{3}\right)^{2} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**3)**2*sqrt(c + d*x**3))` | $\frac{1}{x^{2} \left(a + b x^{3}\right)^{2} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**3)**2*sqrt(c + d*x**3))` | $\frac{1}{x^{3} \left(a + b x^{3}\right)^{2} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x**8/((a + b*x**3)**2*(c + d*x**3)**(3/2))` | $\frac{x^{8}}{\left(a + b x^{3}\right)^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5/((a + b*x**3)**2*(c + d*x**3)**(3/2))` | $\frac{x^{5}}{\left(a + b x^{3}\right)^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/((a + b*x**3)**2*(c + d*x**3)**(3/2))` | $\frac{x^{2}}{\left(a + b x^{3}\right)^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**3)**2*(c + d*x**3)**(3/2))` | $\frac{1}{x \left(a + b x^{3}\right)^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**3)**2*(c + d*x**3)**(3/2))` | $\frac{1}{x^{4} \left(a + b x^{3}\right)^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/((a + b*x**3)**2*(c + d*x**3)**(3/2))` | $\frac{x^{3}}{\left(a + b x^{3}\right)^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/((a + b*x**3)**2*(c + d*x**3)**(3/2))` | $\frac{x}{\left(a + b x^{3}\right)^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x**3)**2*(c + d*x**3)**(3/2))` | $\frac{1}{\left(a + b x^{3}\right)^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**3)**2*(c + d*x**3)**(3/2))` | $\frac{1}{x^{2} \left(a + b x^{3}\right)^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**3)**2*(c + d*x**3)**(3/2))` | $\frac{1}{x^{3} \left(a + b x^{3}\right)^{2} \left(c + d x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5/(sqrt(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{x^{5}}{\sqrt{a + b x^{3}} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x**2/(sqrt(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{x^{2}}{\sqrt{a + b x^{3}} \sqrt{c + d x^{3}}}$ |
| timeout | parametric | `1/(x*sqrt(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{1}{x \sqrt{a + b x^{3}} \sqrt{c + d x^{3}}}$ |
| timeout | parametric | `1/(x**4*sqrt(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{1}{x^{4} \sqrt{a + b x^{3}} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x**4/(sqrt(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{x^{4}}{\sqrt{a + b x^{3}} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x**3/(sqrt(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{x^{3}}{\sqrt{a + b x^{3}} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `x/(sqrt(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{x}{\sqrt{a + b x^{3}} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `1/(sqrt(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{1}{\sqrt{a + b x^{3}} \sqrt{c + d x^{3}}}$ |
| timeout | parametric | `1/(x**2*sqrt(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{1}{x^{2} \sqrt{a + b x^{3}} \sqrt{c + d x^{3}}}$ |
| timeout | parametric | `1/(x**3*sqrt(a + b*x**3)*sqrt(c + d*x**3))` | $\frac{1}{x^{3} \sqrt{a + b x^{3}} \sqrt{c + d x^{3}}}$ |
| partial | parametric | `(e*x)**(7/2)*(A + B*x**3)*sqrt(a + b*x**3)` | $\left(e x\right)^{\frac{7}{2}} \left(A + B x^{3}\right) \sqrt{a + b x^{3}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x**3)*sqrt(a + b*x**3)` | $\left(e x\right)^{\frac{5}{2}} \left(A + B x^{3}\right) \sqrt{a + b x^{3}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x**3)*sqrt(a + b*x**3)` | $\left(e x\right)^{\frac{3}{2}} \left(A + B x^{3}\right) \sqrt{a + b x^{3}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x**3)*sqrt(a + b*x**3)` | $\sqrt{e x} \left(A + B x^{3}\right) \sqrt{a + b x^{3}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/sqrt(e*x)` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{\sqrt{e x}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/(e*x)**(3/2)` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{\left(e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/(e*x)**(5/2)` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{\left(e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/(e*x)**(7/2)` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{\left(e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x**(9/2)` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x**(11/2)` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `(A + B*x**3)*sqrt(a + b*x**3)/x**(13/2)` | $\frac{\left(A + B x^{3}\right) \sqrt{a + b x^{3}}}{x^{\frac{13}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*(A + B*x**3)*(a + b*x**3)**(3/2)` | $\left(e x\right)^{\frac{7}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x**3)*(a + b*x**3)**(3/2)` | $\left(e x\right)^{\frac{5}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x**3)*(a + b*x**3)**(3/2)` | $\left(e x\right)^{\frac{3}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x**3)*(a + b*x**3)**(3/2)` | $\sqrt{e x} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/sqrt(e*x)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{\sqrt{e x}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/(e*x)**(3/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/(e*x)**(5/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(3/2)/(e*x)**(7/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*(A + B*x**3)*(a + b*x**3)**(5/2)` | $\left(e x\right)^{\frac{7}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x**3)*(a + b*x**3)**(5/2)` | $\left(e x\right)^{\frac{5}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x**3)*(a + b*x**3)**(5/2)` | $\left(e x\right)^{\frac{3}{2}} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x**3)*(a + b*x**3)**(5/2)` | $\sqrt{e x} \left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(5/2)/sqrt(e*x)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{5}{2}}}{\sqrt{e x}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(5/2)/(e*x)**(3/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{5}{2}}}{\left(e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(5/2)/(e*x)**(5/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{5}{2}}}{\left(e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)*(a + b*x**3)**(5/2)/(e*x)**(7/2)` | $\frac{\left(A + B x^{3}\right) \left(a + b x^{3}\right)^{\frac{5}{2}}}{\left(e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*(A + B*x**3)/sqrt(a + b*x**3)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(A + B x^{3}\right)}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x**3)/sqrt(a + b*x**3)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(A + B x^{3}\right)}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x**3)/sqrt(a + b*x**3)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(A + B x^{3}\right)}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x**3)/sqrt(a + b*x**3)` | $\frac{\sqrt{e x} \left(A + B x^{3}\right)}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/(sqrt(e*x)*sqrt(a + b*x**3))` | $\frac{A + B x^{3}}{\sqrt{e x} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/((e*x)**(3/2)*sqrt(a + b*x**3))` | $\frac{A + B x^{3}}{\left(e x\right)^{\frac{3}{2}} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/((e*x)**(5/2)*sqrt(a + b*x**3))` | $\frac{A + B x^{3}}{\left(e x\right)^{\frac{5}{2}} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(A + B*x**3)/((e*x)**(7/2)*sqrt(a + b*x**3))` | $\frac{A + B x^{3}}{\left(e x\right)^{\frac{7}{2}} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(e*x)**(7/2)*(A + B*x**3)/(a + b*x**3)**(3/2)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x**3)/(a + b*x**3)**(3/2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x**3)/(a + b*x**3)**(3/2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x**3)/(a + b*x**3)**(3/2)` | $\frac{\sqrt{e x} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(sqrt(e*x)*(a + b*x**3)**(3/2))` | $\frac{A + B x^{3}}{\sqrt{e x} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)/((e*x)**(3/2)*(a + b*x**3)**(3/2))` | $\frac{A + B x^{3}}{\left(e x\right)^{\frac{3}{2}} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**3)/((e*x)**(5/2)*(a + b*x**3)**(3/2))` | $\frac{A + B x^{3}}{\left(e x\right)^{\frac{5}{2}} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**3)/((e*x)**(7/2)*(a + b*x**3)**(3/2))` | $\frac{A + B x^{3}}{\left(e x\right)^{\frac{7}{2}} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(e*x)*(A + B*x**3)/(a + b*x**3)**(5/2)` | $\frac{\sqrt{e x} \left(A + B x^{3}\right)}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)/(sqrt(e*x)*(a + b*x**3)**(5/2))` | $\frac{A + B x^{3}}{\sqrt{e x} \left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)/((e*x)**(3/2)*(a + b*x**3)**(5/2))` | $\frac{A + B x^{3}}{\left(e x\right)^{\frac{3}{2}} \left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**3)/((e*x)**(5/2)*(a + b*x**3)**(5/2))` | $\frac{A + B x^{3}}{\left(e x\right)^{\frac{5}{2}} \left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**3)/((e*x)**(7/2)*(a + b*x**3)**(5/2))` | $\frac{A + B x^{3}}{\left(e x\right)^{\frac{7}{2}} \left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x**14/((1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{x^{14}}{\sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**11/((1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{x^{11}}{\sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**8/((1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{x^{8}}{\sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**5/((1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{x^{5}}{\sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**2/((1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{x^{2}}{\sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/(x*(1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{1}{x \sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/(x**4*(1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{1}{x^{4} \sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**6/((1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{x^{6}}{\sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**3/((1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{x^{3}}{\sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/((1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{1}{\sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/(x**3*(1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{1}{x^{3} \sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/(x**6*(1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{1}{x^{6} \sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/(x**9*(1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{1}{x^{9} \sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**7/((1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{x^{7}}{\sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**4/((1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{x^{4}}{\sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x/((1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{x}{\sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/(x**2*(1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{1}{x^{2} \sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/(x**5*(1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{1}{x^{5} \sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**11/((1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{x^{11}}{\left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**8/((1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{x^{8}}{\left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**5/((1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{x^{5}}{\left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**2/((1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{x^{2}}{\left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/(x*(1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{1}{x \left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/(x**4*(1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{1}{x^{4} \left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**4/((1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{x^{4}}{\left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x/((1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{x}{\left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/(x**2*(1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{1}{x^{2} \left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/(x**5*(1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{1}{x^{5} \left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**6/((1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{x^{6}}{\left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `x**3/((1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{x^{3}}{\left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/((1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{1}{\left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | concrete | `1/(x**3*(1 - x**3)**(2/3)*(x**3 + 1))` | $\frac{1}{x^{3} \left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{3} + 1\right)}$ |
| partial | parametric | `x**7*sqrt(c + d*x**4)/(a + b*x**4)` | $\frac{x^{7} \sqrt{c + d x^{4}}}{a + b x^{4}}$ |
| partial | parametric | `x**5*sqrt(c + d*x**4)/(a + b*x**4)` | $\frac{x^{5} \sqrt{c + d x^{4}}}{a + b x^{4}}$ |
| partial | parametric | `x**3*sqrt(c + d*x**4)/(a + b*x**4)` | $\frac{x^{3} \sqrt{c + d x^{4}}}{a + b x^{4}}$ |
| partial | parametric | `x*sqrt(c + d*x**4)/(a + b*x**4)` | $\frac{x \sqrt{c + d x^{4}}}{a + b x^{4}}$ |
| partial | parametric | `sqrt(c + d*x**4)/(x*(a + b*x**4))` | $\frac{\sqrt{c + d x^{4}}}{x \left(a + b x^{4}\right)}$ |
| partial | parametric | `sqrt(c + d*x**4)/(x**3*(a + b*x**4))` | $\frac{\sqrt{c + d x^{4}}}{x^{3} \left(a + b x^{4}\right)}$ |
| partial | parametric | `sqrt(c + d*x**4)/(x**5*(a + b*x**4))` | $\frac{\sqrt{c + d x^{4}}}{x^{5} \left(a + b x^{4}\right)}$ |
| partial | parametric | `sqrt(c + d*x**4)/(x**7*(a + b*x**4))` | $\frac{\sqrt{c + d x^{4}}}{x^{7} \left(a + b x^{4}\right)}$ |
| timeout | parametric | `(e*x)**(3/2)*sqrt(c + d*x**4)/(a + b*x**4)` | $\frac{\left(e x\right)^{\frac{3}{2}} \sqrt{c + d x^{4}}}{a + b x^{4}}$ |
| timeout | parametric | `sqrt(e*x)*sqrt(c + d*x**4)/(a + b*x**4)` | $\frac{\sqrt{e x} \sqrt{c + d x^{4}}}{a + b x^{4}}$ |
| timeout | parametric | `sqrt(c + d*x**4)/(sqrt(e*x)*(a + b*x**4))` | $\frac{\sqrt{c + d x^{4}}}{\sqrt{e x} \left(a + b x^{4}\right)}$ |
| timeout | parametric | `sqrt(c + d*x**4)/((e*x)**(3/2)*(a + b*x**4))` | $\frac{\sqrt{c + d x^{4}}}{\left(e x\right)^{\frac{3}{2}} \left(a + b x^{4}\right)}$ |
| partial | parametric | `x**11/((a + b*x**4)*sqrt(c + d*x**4))` | $\frac{x^{11}}{\left(a + b x^{4}\right) \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**7/((a + b*x**4)*sqrt(c + d*x**4))` | $\frac{x^{7}}{\left(a + b x^{4}\right) \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**3/((a + b*x**4)*sqrt(c + d*x**4))` | $\frac{x^{3}}{\left(a + b x^{4}\right) \sqrt{c + d x^{4}}}$ |
| partial | parametric | `1/(x*(a + b*x**4)*sqrt(c + d*x**4))` | $\frac{1}{x \left(a + b x^{4}\right) \sqrt{c + d x^{4}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**4)*sqrt(c + d*x**4))` | $\frac{1}{x^{5} \left(a + b x^{4}\right) \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**9/((a + b*x**4)*sqrt(c + d*x**4))` | $\frac{x^{9}}{\left(a + b x^{4}\right) \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**5/((a + b*x**4)*sqrt(c + d*x**4))` | $\frac{x^{5}}{\left(a + b x^{4}\right) \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x/((a + b*x**4)*sqrt(c + d*x**4))` | $\frac{x}{\left(a + b x^{4}\right) \sqrt{c + d x^{4}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**4)*sqrt(c + d*x**4))` | $\frac{1}{x^{3} \left(a + b x^{4}\right) \sqrt{c + d x^{4}}}$ |
| partial | parametric | `1/(x**7*(a + b*x**4)*sqrt(c + d*x**4))` | $\frac{1}{x^{7} \left(a + b x^{4}\right) \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**8/((a + b*x**4)*sqrt(c + d*x**4))` | $\frac{x^{8}}{\left(a + b x^{4}\right) \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**15/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{x^{15}}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**11/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{x^{11}}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**7/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{x^{7}}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**3/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{x^{3}}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `1/(x*(a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{1}{x \left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{1}{x^{5} \left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**13/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{x^{13}}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**9/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{x^{9}}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**5/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{x^{5}}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{x}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{1}{x^{3} \left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `1/(x**7*(a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{1}{x^{7} \left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**8/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{x^{8}}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**4/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{x^{4}}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `1/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{1}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{1}{x^{4} \left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**6/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{x^{6}}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**2/((a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{x^{2}}{\left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**4)**2*sqrt(c + d*x**4))` | $\frac{1}{x^{2} \left(a + b x^{4}\right)^{2} \sqrt{c + d x^{4}}}$ |
| partial | parametric | `x**17/((a + b*x**6)*sqrt(c + d*x**6))` | $\frac{x^{17}}{\left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `x**11/((a + b*x**6)*sqrt(c + d*x**6))` | $\frac{x^{11}}{\left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `x**5/((a + b*x**6)*sqrt(c + d*x**6))` | $\frac{x^{5}}{\left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `1/(x*(a + b*x**6)*sqrt(c + d*x**6))` | $\frac{1}{x \left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `1/(x**7*(a + b*x**6)*sqrt(c + d*x**6))` | $\frac{1}{x^{7} \left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `x**14/((a + b*x**6)*sqrt(c + d*x**6))` | $\frac{x^{14}}{\left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `x**8/((a + b*x**6)*sqrt(c + d*x**6))` | $\frac{x^{8}}{\left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `x**2/((a + b*x**6)*sqrt(c + d*x**6))` | $\frac{x^{2}}{\left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**6)*sqrt(c + d*x**6))` | $\frac{1}{x^{4} \left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `1/(x**10*(a + b*x**6)*sqrt(c + d*x**6))` | $\frac{1}{x^{10} \left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `x**4/((a + b*x**6)*sqrt(c + d*x**6))` | $\frac{x^{4}}{\left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `x**3/((a + b*x**6)*sqrt(c + d*x**6))` | $\frac{x^{3}}{\left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `x/((a + b*x**6)*sqrt(c + d*x**6))` | $\frac{x}{\left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `1/((a + b*x**6)*sqrt(c + d*x**6))` | $\frac{1}{\left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**6)*sqrt(c + d*x**6))` | $\frac{1}{x^{2} \left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**6)*sqrt(c + d*x**6))` | $\frac{1}{x^{3} \left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**6)*sqrt(c + d*x**6))` | $\frac{1}{x^{5} \left(a + b x^{6}\right) \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `x**17/((a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{x^{17}}{\left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `x**11/((a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{x^{11}}{\left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `x**5/((a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{x^{5}}{\left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| partial | parametric | `1/(x*(a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{1}{x \left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `1/(x**7*(a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{1}{x^{7} \left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `x**14/((a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{x^{14}}{\left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `x**8/((a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{x^{8}}{\left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `x**2/((a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{x^{2}}{\left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `1/(x**4*(a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{1}{x^{4} \left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `1/(x**10*(a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{1}{x^{10} \left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `x**4/((a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{x^{4}}{\left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `x**3/((a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{x^{3}}{\left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `x/((a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{x}{\left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `1/((a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{1}{\left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `1/(x**2*(a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{1}{x^{2} \left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `1/(x**3*(a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{1}{x^{3} \left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| timeout | parametric | `1/(x**5*(a + b*x**6)**2*sqrt(c + d*x**6))` | $\frac{1}{x^{5} \left(a + b x^{6}\right)^{2} \sqrt{c + d x^{6}}}$ |
| partial | parametric | `x**23/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{x^{23}}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `x**15/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{x^{15}}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `x**7/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{x^{7}}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `1/(x*(a + b*x**8)*sqrt(c + d*x**8))` | $\frac{1}{x \left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `1/(x**9*(a + b*x**8)*sqrt(c + d*x**8))` | $\frac{1}{x^{9} \left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `x**19/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{x^{19}}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `x**11/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{x^{11}}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `x**3/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{x^{3}}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**8)*sqrt(c + d*x**8))` | $\frac{1}{x^{5} \left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `1/(x**13*(a + b*x**8)*sqrt(c + d*x**8))` | $\frac{1}{x^{13} \left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `x**9/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{x^{9}}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `x/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{x}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `1/(x**7*(a + b*x**8)*sqrt(c + d*x**8))` | $\frac{1}{x^{7} \left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `x**13/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{x^{13}}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `x**5/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{x^{5}}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**8)*sqrt(c + d*x**8))` | $\frac{1}{x^{3} \left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `x**4/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{x^{4}}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `x**2/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{x^{2}}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `1/((a + b*x**8)*sqrt(c + d*x**8))` | $\frac{1}{\left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**8)*sqrt(c + d*x**8))` | $\frac{1}{x^{2} \left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**8)*sqrt(c + d*x**8))` | $\frac{1}{x^{4} \left(a + b x^{8}\right) \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `x**23/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{x^{23}}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `x**15/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{x^{15}}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `x**7/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{x^{7}}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| partial | parametric | `1/(x*(a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{1}{x \left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `1/(x**9*(a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{1}{x^{9} \left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `x**19/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{x^{19}}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `x**11/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{x^{11}}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `x**3/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{x^{3}}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `1/(x**5*(a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{1}{x^{5} \left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `1/(x**13*(a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{1}{x^{13} \left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `x**9/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{x^{9}}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `x/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{x}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `1/(x**7*(a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{1}{x^{7} \left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `x**13/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{x^{13}}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `x**5/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{x^{5}}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `1/(x**3*(a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{1}{x^{3} \left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `x**4/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{x^{4}}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `x**2/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{x^{2}}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `1/((a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{1}{\left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `1/(x**2*(a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{1}{x^{2} \left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| timeout | parametric | `1/(x**4*(a + b*x**8)**2*sqrt(c + d*x**8))` | $\frac{1}{x^{4} \left(a + b x^{8}\right)^{2} \sqrt{c + d x^{8}}}$ |
| partial | parametric | `x**5*(a + b/x**2)*sqrt(c + d/x**2)` | $x^{5} \left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}$ |
| partial | parametric | `x**3*(a + b/x**2)*sqrt(c + d/x**2)` | $x^{3} \left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}$ |
| partial | parametric | `x*(a + b/x**2)*sqrt(c + d/x**2)` | $x \left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}$ |
| partial | parametric | `(a + b/x**2)*sqrt(c + d/x**2)/x` | $\frac{\left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}}{x}$ |
| SOLVED-both | parametric | `(a + b/x**2)*sqrt(c + d/x**2)/x**3` | $\frac{\left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b/x**2)*sqrt(c + d/x**2)/x**5` | $\frac{\left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}}{x^{5}}$ |
| SOLVED-both | parametric | `(a + b/x**2)*sqrt(c + d/x**2)/x**7` | $\frac{\left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}}{x^{7}}$ |
| SOLVED-both | parametric | `(a + b/x**2)*sqrt(c + d/x**2)/x**9` | $\frac{\left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}}{x^{9}}$ |
| SOLVED-both | parametric | `x**10*(a + b/x**2)*sqrt(c + d/x**2)` | $x^{10} \left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}$ |
| SOLVED-both | parametric | `x**8*(a + b/x**2)*sqrt(c + d/x**2)` | $x^{8} \left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}$ |
| SOLVED-both | parametric | `x**6*(a + b/x**2)*sqrt(c + d/x**2)` | $x^{6} \left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}$ |
| SOLVED-both | parametric | `x**4*(a + b/x**2)*sqrt(c + d/x**2)` | $x^{4} \left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}$ |
| partial | parametric | `x**2*(a + b/x**2)*sqrt(c + d/x**2)` | $x^{2} \left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}$ |
| partial | parametric | `(a + b/x**2)*sqrt(c + d/x**2)` | $\left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}$ |
| partial | parametric | `(a + b/x**2)*sqrt(c + d/x**2)/x**2` | $\frac{\left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}}{x^{2}}$ |
| partial | parametric | `(a + b/x**2)*sqrt(c + d/x**2)/x**4` | $\frac{\left(a + \frac{b}{x^{2}}\right) \sqrt{c + \frac{d}{x^{2}}}}{x^{4}}$ |
| partial | parametric | `x**5*(a + b/x**2)*(c + d/x**2)**(3/2)` | $x^{5} \left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**3*(a + b/x**2)*(c + d/x**2)**(3/2)` | $x^{3} \left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a + b/x**2)*(c + d/x**2)**(3/2)` | $x \left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x**2)*(c + d/x**2)**(3/2)/x` | $\frac{\left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}{x}$ |
| SOLVED-both | parametric | `(a + b/x**2)*(c + d/x**2)**(3/2)/x**3` | $\frac{\left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}{x^{3}}$ |
| SOLVED-both | parametric | `(a + b/x**2)*(c + d/x**2)**(3/2)/x**5` | $\frac{\left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}{x^{5}}$ |
| SOLVED-both | parametric | `(a + b/x**2)*(c + d/x**2)**(3/2)/x**7` | $\frac{\left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}{x^{7}}$ |
| SOLVED-both | parametric | `(a + b/x**2)*(c + d/x**2)**(3/2)/x**9` | $\frac{\left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}{x^{9}}$ |
| SOLVED-both | parametric | `x**12*(a + b/x**2)*(c + d/x**2)**(3/2)` | $x^{12} \left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**10*(a + b/x**2)*(c + d/x**2)**(3/2)` | $x^{10} \left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**8*(a + b/x**2)*(c + d/x**2)**(3/2)` | $x^{8} \left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**6*(a + b/x**2)*(c + d/x**2)**(3/2)` | $x^{6} \left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**4*(a + b/x**2)*(c + d/x**2)**(3/2)` | $x^{4} \left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(a + b/x**2)*(c + d/x**2)**(3/2)` | $x^{2} \left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x**2)*(c + d/x**2)**(3/2)` | $\left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b/x**2)*(c + d/x**2)**(3/2)/x**2` | $\frac{\left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b/x**2)*(c + d/x**2)**(3/2)/x**4` | $\frac{\left(a + \frac{b}{x^{2}}\right) \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `x**3*(a + b/x**2)/sqrt(c + d/x**2)` | $\frac{x^{3} \left(a + \frac{b}{x^{2}}\right)}{\sqrt{c + \frac{d}{x^{2}}}}$ |
| partial | parametric | `x*(a + b/x**2)/sqrt(c + d/x**2)` | $\frac{x \left(a + \frac{b}{x^{2}}\right)}{\sqrt{c + \frac{d}{x^{2}}}}$ |
| partial | parametric | `(a + b/x**2)/(x*sqrt(c + d/x**2))` | $\frac{a + \frac{b}{x^{2}}}{x \sqrt{c + \frac{d}{x^{2}}}}$ |
| SOLVED-both | parametric | `(a + b/x**2)/(x**3*sqrt(c + d/x**2))` | $\frac{a + \frac{b}{x^{2}}}{x^{3} \sqrt{c + \frac{d}{x^{2}}}}$ |
| SOLVED-both | parametric | `(a + b/x**2)/(x**5*sqrt(c + d/x**2))` | $\frac{a + \frac{b}{x^{2}}}{x^{5} \sqrt{c + \frac{d}{x^{2}}}}$ |
| SOLVED-both | parametric | `(a + b/x**2)/(x**7*sqrt(c + d/x**2))` | $\frac{a + \frac{b}{x^{2}}}{x^{7} \sqrt{c + \frac{d}{x^{2}}}}$ |
| SOLVED-both | parametric | `x**4*(a + b/x**2)/sqrt(c + d/x**2)` | $\frac{x^{4} \left(a + \frac{b}{x^{2}}\right)}{\sqrt{c + \frac{d}{x^{2}}}}$ |
| SOLVED-both | parametric | `x**2*(a + b/x**2)/sqrt(c + d/x**2)` | $\frac{x^{2} \left(a + \frac{b}{x^{2}}\right)}{\sqrt{c + \frac{d}{x^{2}}}}$ |
| partial | parametric | `(a + b/x**2)/sqrt(c + d/x**2)` | $\frac{a + \frac{b}{x^{2}}}{\sqrt{c + \frac{d}{x^{2}}}}$ |
| partial | parametric | `(a + b/x**2)/(x**2*sqrt(c + d/x**2))` | $\frac{a + \frac{b}{x^{2}}}{x^{2} \sqrt{c + \frac{d}{x^{2}}}}$ |
| partial | parametric | `(a + b/x**2)/(x**4*sqrt(c + d/x**2))` | $\frac{a + \frac{b}{x^{2}}}{x^{4} \sqrt{c + \frac{d}{x^{2}}}}$ |
| partial | parametric | `x**3*(a + b/x**2)/(c + d/x**2)**(3/2)` | $\frac{x^{3} \left(a + \frac{b}{x^{2}}\right)}{\left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(a + b/x**2)/(c + d/x**2)**(3/2)` | $\frac{x \left(a + \frac{b}{x^{2}}\right)}{\left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x**2)/(x*(c + d/x**2)**(3/2))` | $\frac{a + \frac{b}{x^{2}}}{x \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b/x**2)/(x**3*(c + d/x**2)**(3/2))` | $\frac{a + \frac{b}{x^{2}}}{x^{3} \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b/x**2)/(x**5*(c + d/x**2)**(3/2))` | $\frac{a + \frac{b}{x^{2}}}{x^{5} \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b/x**2)/(x**7*(c + d/x**2)**(3/2))` | $\frac{a + \frac{b}{x^{2}}}{x^{7} \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b/x**2)/(x**9*(c + d/x**2)**(3/2))` | $\frac{a + \frac{b}{x^{2}}}{x^{9} \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4*(a + b/x**2)/(c + d/x**2)**(3/2)` | $\frac{x^{4} \left(a + \frac{b}{x^{2}}\right)}{\left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(a + b/x**2)/(c + d/x**2)**(3/2)` | $\frac{x^{2} \left(a + \frac{b}{x^{2}}\right)}{\left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x**2)/(c + d/x**2)**(3/2)` | $\frac{a + \frac{b}{x^{2}}}{\left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x**2)/(x**2*(c + d/x**2)**(3/2))` | $\frac{a + \frac{b}{x^{2}}}{x^{2} \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x**2)/(x**4*(c + d/x**2)**(3/2))` | $\frac{a + \frac{b}{x^{2}}}{x^{4} \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x**2)/(x**6*(c + d/x**2)**(3/2))` | $\frac{a + \frac{b}{x^{2}}}{x^{6} \left(c + \frac{d}{x^{2}}\right)^{\frac{3}{2}}}$ |
| timeout | concrete | `x**(5/2)*sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1)` | $x^{\frac{5}{2}} \sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}$ |
| partial | concrete | `x**(3/2)*sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1)` | $x^{\frac{3}{2}} \sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}$ |
| partial | concrete | `sqrt(x)*sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1)` | $\sqrt{x} \sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}$ |
| partial | concrete | `sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1)/sqrt(x)` | $\frac{\sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}{\sqrt{x}}$ |
| partial | concrete | `sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1)/x**(3/2)` | $\frac{\sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}{x^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | concrete | `sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1)/x**(5/2)` | $\frac{\sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}{x^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | concrete | `sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1)/x**(7/2)` | $\frac{\sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}{x^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | concrete | `sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1)/x**(9/2)` | $\frac{\sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}{x^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | concrete | `sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1)/x**(11/2)` | $\frac{\sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}{x^{\frac{11}{2}}}$ |
| timeout | concrete | `x**(5/2)/(sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1))` | $\frac{x^{\frac{5}{2}}}{\sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}$ |
| partial | concrete | `x**(3/2)/(sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1))` | $\frac{x^{\frac{3}{2}}}{\sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}$ |
| partial | concrete | `sqrt(x)/(sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1))` | $\frac{\sqrt{x}}{\sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}$ |
| partial | concrete | `1/(sqrt(x)*sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1))` | $\frac{1}{\sqrt{x} \sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}$ |
| **SOLVED-NEW** | concrete | `1/(x**(3/2)*sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1))` | $\frac{1}{x^{\frac{3}{2}} \sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}$ |
| **SOLVED-NEW** | concrete | `1/(x**(5/2)*sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1))` | $\frac{1}{x^{\frac{5}{2}} \sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}$ |
| **SOLVED-NEW** | concrete | `1/(x**(7/2)*sqrt(sqrt(x) - 1)*sqrt(sqrt(x) + 1))` | $\frac{1}{x^{\frac{7}{2}} \sqrt{\sqrt{x} - 1} \sqrt{\sqrt{x} + 1}}$ |
| partial | concrete | `x**31*sqrt(x**16 + 1)/(1 - x**16)` | $\frac{x^{31} \sqrt{x^{16} + 1}}{1 - x^{16}}$ |
| partial | parametric | `sqrt(c + d/x)/(x*sqrt(a + b/x))` | $\frac{\sqrt{c + \frac{d}{x}}}{x \sqrt{a + \frac{b}{x}}}$ |
| SOLVED-both | parametric | `(c + d*x + e*x**2)/sqrt(a + b*x)` | $\frac{c + d x + e x^{2}}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `(c + d*x + e*x**2)**2/sqrt(a + b*x)` | $\frac{\left(c + d x + e x^{2}\right)^{2}}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `(c + d*x + e*x**2)**3/sqrt(a + b*x)` | $\frac{\left(c + d x + e x^{2}\right)^{3}}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `(c + d*x + e*x**2 + f*x**3)/sqrt(a + b*x)` | $\frac{c + d x + e x^{2} + f x^{3}}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `(c + d*x + e*x**2 + f*x**3)**2/sqrt(a + b*x)` | $\frac{\left(c + d x + e x^{2} + f x^{3}\right)^{2}}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `(c + d*x + e*x**2 + f*x**3)**3/sqrt(a + b*x)` | $\frac{\left(c + d x + e x^{2} + f x^{3}\right)^{3}}{\sqrt{a + b x}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)*(a*c + a*d*x + b*c*x**3 + b*d*x**4)` | $\left(a + b x^{3}\right)^{\frac{3}{2}} \left(a c + a d x + b c x^{3} + b d x^{4}\right)$ |
| partial | parametric | `sqrt(a + b*x**3)*(a*c + a*d*x + b*c*x**3 + b*d*x**4)` | $\sqrt{a + b x^{3}} \left(a c + a d x + b c x^{3} + b d x^{4}\right)$ |
| partial | parametric | `(a*c + a*d*x + b*c*x**3 + b*d*x**4)/sqrt(a + b*x**3)` | $\frac{a c + a d x + b c x^{3} + b d x^{4}}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(a*c + a*d*x + b*c*x**3 + b*d*x**4)/(a + b*x**3)**(3/2)` | $\frac{a c + a d x + b c x^{3} + b d x^{4}}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*c + a*d*x + b*c*x**3 + b*d*x**4)/(a + b*x**3)**(5/2)` | $\frac{a c + a d x + b c x^{3} + b d x^{4}}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a*c + a*d*x + b*c*x**3 + b*d*x**4)/(a + b*x**3)**(7/2)` | $\frac{a c + a d x + b c x^{3} + b d x^{4}}{\left(a + b x^{3}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a*c + a*d*x + b*c*x**3 + b*d*x**4)/(a + b*x**3)**(9/2)` | $\frac{a c + a d x + b c x^{3} + b d x^{4}}{\left(a + b x^{3}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3 + g*x**4)/sqrt(a + b*x**3)` | $\frac{c + d x + e x^{2} + f x^{3} + g x^{4}}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3 + g*x**4)/(a + b*x**3)**(3/2)` | $\frac{c + d x + e x^{2} + f x^{3} + g x^{4}}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3 + g*x**4)/(a + b*x**3)**(5/2)` | $\frac{c + d x + e x^{2} + f x^{3} + g x^{4}}{\left(a + b x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3 + g*x**4)/(a + b*x**3)**(7/2)` | $\frac{c + d x + e x^{2} + f x^{3} + g x^{4}}{\left(a + b x^{3}\right)^{\frac{7}{2}}}$ |
| partial | concrete | `(x + 1 + sqrt(3))/sqrt(x**3 + 1)` | $\frac{x + 1 + \sqrt{3}}{\sqrt{x^{3} + 1}}$ |
| partial | concrete | `(-x + 1 + sqrt(3))/sqrt(1 - x**3)` | $\frac{- x + 1 + \sqrt{3}}{\sqrt{1 - x^{3}}}$ |
| partial | concrete | `(-x + 1 + sqrt(3))/sqrt(x**3 - 1)` | $\frac{- x + 1 + \sqrt{3}}{\sqrt{x^{3} - 1}}$ |
| partial | concrete | `(x + 1 + sqrt(3))/sqrt(-x**3 - 1)` | $\frac{x + 1 + \sqrt{3}}{\sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(a**(1/3)*(1 + sqrt(3)) + b**(1/3)*x)/sqrt(a + b*x**3)` | $\frac{\sqrt[3]{a} \left(1 + \sqrt{3}\right) + \sqrt[3]{b} x}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(a**(1/3)*(1 + sqrt(3)) - b**(1/3)*x)/sqrt(a - b*x**3)` | $\frac{\sqrt[3]{a} \left(1 + \sqrt{3}\right) - \sqrt[3]{b} x}{\sqrt{a - b x^{3}}}$ |
| partial | parametric | `(a**(1/3)*(1 + sqrt(3)) - b**(1/3)*x)/sqrt(-a + b*x**3)` | $\frac{\sqrt[3]{a} \left(1 + \sqrt{3}\right) - \sqrt[3]{b} x}{\sqrt{- a + b x^{3}}}$ |
| partial | parametric | `(a**(1/3)*(1 + sqrt(3)) + b**(1/3)*x)/sqrt(-a - b*x**3)` | $\frac{\sqrt[3]{a} \left(1 + \sqrt{3}\right) + \sqrt[3]{b} x}{\sqrt{- a - b x^{3}}}$ |
| partial | parametric | `(x*(b/a)**(1/3) + 1 + sqrt(3))/sqrt(a + b*x**3)` | $\frac{x \sqrt[3]{\frac{b}{a}} + 1 + \sqrt{3}}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(-x*(b/a)**(1/3) + 1 + sqrt(3))/sqrt(a - b*x**3)` | $\frac{- x \sqrt[3]{\frac{b}{a}} + 1 + \sqrt{3}}{\sqrt{a - b x^{3}}}$ |
| partial | parametric | `(-x*(b/a)**(1/3) + 1 + sqrt(3))/sqrt(-a + b*x**3)` | $\frac{- x \sqrt[3]{\frac{b}{a}} + 1 + \sqrt{3}}{\sqrt{- a + b x^{3}}}$ |
| partial | parametric | `(x*(b/a)**(1/3) + 1 + sqrt(3))/sqrt(-a - b*x**3)` | $\frac{x \sqrt[3]{\frac{b}{a}} + 1 + \sqrt{3}}{\sqrt{- a - b x^{3}}}$ |
| partial | concrete | `(x - sqrt(3) + 1)/sqrt(x**3 + 1)` | $\frac{x - \sqrt{3} + 1}{\sqrt{x^{3} + 1}}$ |
| partial | concrete | `(-x - sqrt(3) + 1)/sqrt(1 - x**3)` | $\frac{- x - \sqrt{3} + 1}{\sqrt{1 - x^{3}}}$ |
| partial | concrete | `(-x - sqrt(3) + 1)/sqrt(x**3 - 1)` | $\frac{- x - \sqrt{3} + 1}{\sqrt{x^{3} - 1}}$ |
| partial | concrete | `(x - sqrt(3) + 1)/sqrt(-x**3 - 1)` | $\frac{x - \sqrt{3} + 1}{\sqrt{- x^{3} - 1}}$ |
| partial | concrete | `(-x - 1 + sqrt(3))/sqrt(x**3 + 1)` | $\frac{- x - 1 + \sqrt{3}}{\sqrt{x^{3} + 1}}$ |
| partial | concrete | `(x - 1 + sqrt(3))/sqrt(1 - x**3)` | $\frac{x - 1 + \sqrt{3}}{\sqrt{1 - x^{3}}}$ |
| partial | concrete | `(x - 1 + sqrt(3))/sqrt(x**3 - 1)` | $\frac{x - 1 + \sqrt{3}}{\sqrt{x^{3} - 1}}$ |
| partial | concrete | `(-x - 1 + sqrt(3))/sqrt(-x**3 - 1)` | $\frac{- x - 1 + \sqrt{3}}{\sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(a**(1/3)*(1 - sqrt(3)) + b**(1/3)*x)/sqrt(a + b*x**3)` | $\frac{\sqrt[3]{a} \left(1 - \sqrt{3}\right) + \sqrt[3]{b} x}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(a**(1/3)*(1 - sqrt(3)) - b**(1/3)*x)/sqrt(a - b*x**3)` | $\frac{\sqrt[3]{a} \left(1 - \sqrt{3}\right) - \sqrt[3]{b} x}{\sqrt{a - b x^{3}}}$ |
| partial | parametric | `(a**(1/3)*(1 - sqrt(3)) - b**(1/3)*x)/sqrt(-a + b*x**3)` | $\frac{\sqrt[3]{a} \left(1 - \sqrt{3}\right) - \sqrt[3]{b} x}{\sqrt{- a + b x^{3}}}$ |
| partial | parametric | `(a**(1/3)*(1 - sqrt(3)) + b**(1/3)*x)/sqrt(-a - b*x**3)` | $\frac{\sqrt[3]{a} \left(1 - \sqrt{3}\right) + \sqrt[3]{b} x}{\sqrt{- a - b x^{3}}}$ |
| partial | parametric | `(x*(b/a)**(1/3) - sqrt(3) + 1)/sqrt(a + b*x**3)` | $\frac{x \sqrt[3]{\frac{b}{a}} - \sqrt{3} + 1}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(-x*(b/a)**(1/3) - sqrt(3) + 1)/sqrt(a - b*x**3)` | $\frac{- x \sqrt[3]{\frac{b}{a}} - \sqrt{3} + 1}{\sqrt{a - b x^{3}}}$ |
| partial | parametric | `(-x*(b/a)**(1/3) - sqrt(3) + 1)/sqrt(-a + b*x**3)` | $\frac{- x \sqrt[3]{\frac{b}{a}} - \sqrt{3} + 1}{\sqrt{- a + b x^{3}}}$ |
| partial | parametric | `(x*(b/a)**(1/3) - sqrt(3) + 1)/sqrt(-a - b*x**3)` | $\frac{x \sqrt[3]{\frac{b}{a}} - \sqrt{3} + 1}{\sqrt{- a - b x^{3}}}$ |
| partial | parametric | `(c + d*x)/sqrt(a + b*x**3)` | $\frac{c + d x}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(c + d*x)/sqrt(a - b*x**3)` | $\frac{c + d x}{\sqrt{a - b x^{3}}}$ |
| partial | parametric | `(c + d*x)/sqrt(-a + b*x**3)` | $\frac{c + d x}{\sqrt{- a + b x^{3}}}$ |
| partial | parametric | `(c + d*x)/sqrt(-a - b*x**3)` | $\frac{c + d x}{\sqrt{- a - b x^{3}}}$ |
| partial | parametric | `(c + d*x)/sqrt(x**3 + 1)` | $\frac{c + d x}{\sqrt{x^{3} + 1}}$ |
| partial | parametric | `(c + d*x)/sqrt(1 - x**3)` | $\frac{c + d x}{\sqrt{1 - x^{3}}}$ |
| partial | parametric | `(c + d*x)/sqrt(x**3 - 1)` | $\frac{c + d x}{\sqrt{x^{3} - 1}}$ |
| partial | parametric | `(c + d*x)/sqrt(-x**3 - 1)` | $\frac{c + d x}{\sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(c + d*x)/sqrt(a + b*x**4)` | $\frac{c + d x}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `(c + d*x)/sqrt(a - b*x**4)` | $\frac{c + d x}{\sqrt{a - b x^{4}}}$ |
| partial | parametric | `(c + d*x)/sqrt(-a + b*x**4)` | $\frac{c + d x}{\sqrt{- a + b x^{4}}}$ |
| partial | parametric | `(c + d*x)/sqrt(-a - b*x**4)` | $\frac{c + d x}{\sqrt{- a - b x^{4}}}$ |
| partial | parametric | `(c + d*x + e*x**2)/sqrt(a + b*x**4)` | $\frac{c + d x + e x^{2}}{\sqrt{a + b x^{4}}}$ |
| SOLVED-both | parametric | `(a*g - b*g*x**4)/(a + b*x**4)**(3/2)` | $\frac{a g - b g x^{4}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a*g - b*g*x**4 + e*x)/(a + b*x**4)**(3/2)` | $\frac{a g - b g x^{4} + e x}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a*g - b*g*x**4 + f*x**3)/(a + b*x**4)**(3/2)` | $\frac{a g - b g x^{4} + f x^{3}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a*g - b*g*x**4 + e*x + f*x**3)/(a + b*x**4)**(3/2)` | $\frac{a g - b g x^{4} + e x + f x^{3}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(x**4 - 1)/(x**4 + 1)**(3/2)` | $\frac{x^{4} - 1}{\left(x^{4} + 1\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3 + g*x**4 + h*x**5 + i*x**6)/sqrt(a + b*x**4)` | $\frac{c + d x + e x^{2} + f x^{3} + g x^{4} + h x^{5} + i x^{6}}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `x**3*(c + d*x + e*x**2)/sqrt(a + b*x**3)` | $\frac{x^{3} \left(c + d x + e x^{2}\right)}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `x**2*(c + d*x + e*x**2)/sqrt(a + b*x**3)` | $\frac{x^{2} \left(c + d x + e x^{2}\right)}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `x*(c + d*x + e*x**2)/sqrt(a + b*x**3)` | $\frac{x \left(c + d x + e x^{2}\right)}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(c + d*x + e*x**2)/sqrt(a + b*x**3)` | $\frac{c + d x + e x^{2}}{\sqrt{a + b x^{3}}}$ |
| partial | parametric | `(c + d*x + e*x**2)/(x*sqrt(a + b*x**3))` | $\frac{c + d x + e x^{2}}{x \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(c + d*x + e*x**2)/(x**2*sqrt(a + b*x**3))` | $\frac{c + d x + e x^{2}}{x^{2} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(c + d*x + e*x**2)/(x**3*sqrt(a + b*x**3))` | $\frac{c + d x + e x^{2}}{x^{3} \sqrt{a + b x^{3}}}$ |
| partial | parametric | `x**5*(c + d*x + e*x**2)/(a + b*x**3)**(3/2)` | $\frac{x^{5} \left(c + d x + e x^{2}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4*(c + d*x + e*x**2)/(a + b*x**3)**(3/2)` | $\frac{x^{4} \left(c + d x + e x^{2}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*(c + d*x + e*x**2)/(a + b*x**3)**(3/2)` | $\frac{x^{3} \left(c + d x + e x^{2}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(c + d*x + e*x**2)/(a + b*x**3)**(3/2)` | $\frac{x^{2} \left(c + d x + e x^{2}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(c + d*x + e*x**2)/(a + b*x**3)**(3/2)` | $\frac{x \left(c + d x + e x^{2}\right)}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x + e*x**2)/(a + b*x**3)**(3/2)` | $\frac{c + d x + e x^{2}}{\left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x + e*x**2)/(x*(a + b*x**3)**(3/2))` | $\frac{c + d x + e x^{2}}{x \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x + e*x**2)/(x**2*(a + b*x**3)**(3/2))` | $\frac{c + d x + e x^{2}}{x^{2} \left(a + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)` | $x^{3} \sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)$ |
| partial | parametric | `x**2*sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)` | $x^{2} \sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)$ |
| partial | parametric | `x*sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)` | $x \sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)$ |
| partial | parametric | `sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)` | $\sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)$ |
| partial | parametric | `sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x` | $\frac{\sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x}$ |
| partial | parametric | `sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**2` | $\frac{\sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**3` | $\frac{\sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{3}}$ |
| partial | parametric | `sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**4` | $\frac{\sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{4}}$ |
| partial | parametric | `sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**5` | $\frac{\sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{5}}$ |
| partial | parametric | `sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**6` | $\frac{\sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{6}}$ |
| partial | parametric | `sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**7` | $\frac{\sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{7}}$ |
| partial | parametric | `sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**8` | $\frac{\sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{8}}$ |
| partial | parametric | `sqrt(a + b*x**3)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**9` | $\frac{\sqrt{a + b x^{3}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{9}}$ |
| partial | parametric | `x**3*(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)` | $x^{3} \left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)$ |
| partial | parametric | `x**2*(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)` | $x^{2} \left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)$ |
| partial | parametric | `x*(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)` | $x \left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)$ |
| partial | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)` | $\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)$ |
| partial | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x}$ |
| partial | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**2` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{2}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**3` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{3}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**4` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{4}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**5` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{5}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**6` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{6}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**7` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{7}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**8` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{8}}$ |
| partial | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**9` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{9}}$ |
| timeout | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**10` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{10}}$ |
| timeout | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**11` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{11}}$ |
| timeout | parametric | `(a + b*x**3)**(3/2)*(c + d*x + e*x**2 + f*x**3 + g*x**4)/x**12` | $\frac{\left(a + b x^{3}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3} + g x^{4}\right)}{x^{12}}$ |
| partial | parametric | `x**4*sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)` | $x^{4} \sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)$ |
| partial | parametric | `x**3*sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)` | $x^{3} \sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)$ |
| partial | parametric | `x**2*sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)` | $x^{2} \sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)$ |
| partial | parametric | `x*sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)` | $x \sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)$ |
| partial | parametric | `sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)` | $\sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)$ |
| partial | parametric | `sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)/x` | $\frac{\sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)}{x}$ |
| partial | parametric | `sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)/x**2` | $\frac{\sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)/x**3` | $\frac{\sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{3}}$ |
| partial | parametric | `sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)/x**4` | $\frac{\sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{4}}$ |
| partial | parametric | `sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)/x**5` | $\frac{\sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{5}}$ |
| partial | parametric | `sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)/x**6` | $\frac{\sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{6}}$ |
| partial | parametric | `sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)/x**7` | $\frac{\sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{7}}$ |
| partial | parametric | `sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)/x**8` | $\frac{\sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{8}}$ |
| partial | parametric | `sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)/x**9` | $\frac{\sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{9}}$ |
| partial | parametric | `sqrt(a + b*x**4)*(c + d*x + e*x**2 + f*x**3)/x**10` | $\frac{\sqrt{a + b x^{4}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{10}}$ |
| partial | parametric | `x**4*(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)` | $x^{4} \left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)$ |
| partial | parametric | `x**3*(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)` | $x^{3} \left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)$ |
| partial | parametric | `x**2*(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)` | $x^{2} \left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)$ |
| partial | parametric | `x*(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)` | $x \left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)` | $\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**2` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{2}}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**3` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{3}}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**4` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{4}}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**5` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{5}}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**6` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{6}}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**7` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{7}}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**8` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{8}}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**9` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{9}}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**10` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{10}}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**11` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{11}}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**12` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{12}}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**13` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{13}}$ |
| partial | parametric | `(a + b*x**4)**(3/2)*(c + d*x + e*x**2 + f*x**3)/x**14` | $\frac{\left(a + b x^{4}\right)^{\frac{3}{2}} \left(c + d x + e x^{2} + f x^{3}\right)}{x^{14}}$ |
| partial | parametric | `x**4*(c + d*x + e*x**2 + f*x**3)/sqrt(a + b*x**4)` | $\frac{x^{4} \left(c + d x + e x^{2} + f x^{3}\right)}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `x**3*(c + d*x + e*x**2 + f*x**3)/sqrt(a + b*x**4)` | $\frac{x^{3} \left(c + d x + e x^{2} + f x^{3}\right)}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `x**2*(c + d*x + e*x**2 + f*x**3)/sqrt(a + b*x**4)` | $\frac{x^{2} \left(c + d x + e x^{2} + f x^{3}\right)}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `x*(c + d*x + e*x**2 + f*x**3)/sqrt(a + b*x**4)` | $\frac{x \left(c + d x + e x^{2} + f x^{3}\right)}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3)/sqrt(a + b*x**4)` | $\frac{c + d x + e x^{2} + f x^{3}}{\sqrt{a + b x^{4}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3)/(x*sqrt(a + b*x**4))` | $\frac{c + d x + e x^{2} + f x^{3}}{x \sqrt{a + b x^{4}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3)/(x**2*sqrt(a + b*x**4))` | $\frac{c + d x + e x^{2} + f x^{3}}{x^{2} \sqrt{a + b x^{4}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3)/(x**3*sqrt(a + b*x**4))` | $\frac{c + d x + e x^{2} + f x^{3}}{x^{3} \sqrt{a + b x^{4}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3)/(x**4*sqrt(a + b*x**4))` | $\frac{c + d x + e x^{2} + f x^{3}}{x^{4} \sqrt{a + b x^{4}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3)/(x**5*sqrt(a + b*x**4))` | $\frac{c + d x + e x^{2} + f x^{3}}{x^{5} \sqrt{a + b x^{4}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3)/(x**6*sqrt(a + b*x**4))` | $\frac{c + d x + e x^{2} + f x^{3}}{x^{6} \sqrt{a + b x^{4}}}$ |
| partial | parametric | `x**6*(c + d*x + e*x**2 + f*x**3)/(a + b*x**4)**(3/2)` | $\frac{x^{6} \left(c + d x + e x^{2} + f x^{3}\right)}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5*(c + d*x + e*x**2 + f*x**3)/(a + b*x**4)**(3/2)` | $\frac{x^{5} \left(c + d x + e x^{2} + f x^{3}\right)}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4*(c + d*x + e*x**2 + f*x**3)/(a + b*x**4)**(3/2)` | $\frac{x^{4} \left(c + d x + e x^{2} + f x^{3}\right)}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*(c + d*x + e*x**2 + f*x**3)/(a + b*x**4)**(3/2)` | $\frac{x^{3} \left(c + d x + e x^{2} + f x^{3}\right)}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(c + d*x + e*x**2 + f*x**3)/(a + b*x**4)**(3/2)` | $\frac{x^{2} \left(c + d x + e x^{2} + f x^{3}\right)}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(c + d*x + e*x**2 + f*x**3)/(a + b*x**4)**(3/2)` | $\frac{x \left(c + d x + e x^{2} + f x^{3}\right)}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3)/(a + b*x**4)**(3/2)` | $\frac{c + d x + e x^{2} + f x^{3}}{\left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3)/(x*(a + b*x**4)**(3/2))` | $\frac{c + d x + e x^{2} + f x^{3}}{x \left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3)/(x**2*(a + b*x**4)**(3/2))` | $\frac{c + d x + e x^{2} + f x^{3}}{x^{2} \left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3)/(x**3*(a + b*x**4)**(3/2))` | $\frac{c + d x + e x^{2} + f x^{3}}{x^{3} \left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c + d*x + e*x**2 + f*x**3)/(x**4*(a + b*x**4)**(3/2))` | $\frac{c + d x + e x^{2} + f x^{3}}{x^{4} \left(a + b x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a*c + 3*b*d*x**4 + x**2*(2*a*d + 2*b*c))/(sqrt(a + b*x**2)*sqrt(c + d*x**2))` | $\frac{a c + 3 b d x^{4} + x^{2} \left(2 a d + 2 b c\right)}{\sqrt{a + b x^{2}} \sqrt{c + d x^{2}}}$ |
| partial | concrete | `(x**3 + 1)/((1 - x**4)*(x**4 + 1)**(1/4))` | $\frac{x^{3} + 1}{\left(1 - x^{4}\right) \sqrt[4]{x^{4} + 1}}$ |
| partial | parametric | `x**3*sqrt(a*x + b*x**3)` | $x^{3} \sqrt{a x + b x^{3}}$ |
| partial | parametric | `x**2*sqrt(a*x + b*x**3)` | $x^{2} \sqrt{a x + b x^{3}}$ |
| partial | parametric | `x*sqrt(a*x + b*x**3)` | $x \sqrt{a x + b x^{3}}$ |
| partial | parametric | `sqrt(a*x + b*x**3)` | $\sqrt{a x + b x^{3}}$ |
| partial | parametric | `sqrt(a*x + b*x**3)/x` | $\frac{\sqrt{a x + b x^{3}}}{x}$ |
| partial | parametric | `sqrt(a*x + b*x**3)/x**2` | $\frac{\sqrt{a x + b x^{3}}}{x^{2}}$ |
| partial | parametric | `sqrt(a*x + b*x**3)/x**3` | $\frac{\sqrt{a x + b x^{3}}}{x^{3}}$ |
| partial | parametric | `sqrt(a*x + b*x**3)/x**4` | $\frac{\sqrt{a x + b x^{3}}}{x^{4}}$ |
| partial | parametric | `x**2*(a*x + b*x**3)**(3/2)` | $x^{2} \left(a x + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a*x + b*x**3)**(3/2)` | $x \left(a x + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*x + b*x**3)**(3/2)` | $\left(a x + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*x + b*x**3)**(3/2)/x` | $\frac{\left(a x + b x^{3}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a*x + b*x**3)**(3/2)/x**2` | $\frac{\left(a x + b x^{3}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a*x + b*x**3)**(3/2)/x**3` | $\frac{\left(a x + b x^{3}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a*x + b*x**3)**(3/2)/x**4` | $\frac{\left(a x + b x^{3}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(a*x + b*x**3)**(3/2)/x**5` | $\frac{\left(a x + b x^{3}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(a*x + b*x**3)**(3/2)/x**6` | $\frac{\left(a x + b x^{3}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(a*x + b*x**3)**(3/2)/x**7` | $\frac{\left(a x + b x^{3}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `(a*x + b*x**3)**(3/2)/x**8` | $\frac{\left(a x + b x^{3}\right)^{\frac{3}{2}}}{x^{8}}$ |
| partial | parametric | `x**4/sqrt(a*x + b*x**3)` | $\frac{x^{4}}{\sqrt{a x + b x^{3}}}$ |
| partial | parametric | `x**3/sqrt(a*x + b*x**3)` | $\frac{x^{3}}{\sqrt{a x + b x^{3}}}$ |
| partial | parametric | `x**2/sqrt(a*x + b*x**3)` | $\frac{x^{2}}{\sqrt{a x + b x^{3}}}$ |
| partial | parametric | `x/sqrt(a*x + b*x**3)` | $\frac{x}{\sqrt{a x + b x^{3}}}$ |
| partial | parametric | `1/sqrt(a*x + b*x**3)` | $\frac{1}{\sqrt{a x + b x^{3}}}$ |
| partial | parametric | `1/(x*sqrt(a*x + b*x**3))` | $\frac{1}{x \sqrt{a x + b x^{3}}}$ |
| partial | parametric | `1/(x**2*sqrt(a*x + b*x**3))` | $\frac{1}{x^{2} \sqrt{a x + b x^{3}}}$ |
| partial | parametric | `1/(x**3*sqrt(a*x + b*x**3))` | $\frac{1}{x^{3} \sqrt{a x + b x^{3}}}$ |
| partial | parametric | `x**7/(a*x + b*x**3)**(3/2)` | $\frac{x^{7}}{\left(a x + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**6/(a*x + b*x**3)**(3/2)` | $\frac{x^{6}}{\left(a x + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5/(a*x + b*x**3)**(3/2)` | $\frac{x^{5}}{\left(a x + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/(a*x + b*x**3)**(3/2)` | $\frac{x^{4}}{\left(a x + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/(a*x + b*x**3)**(3/2)` | $\frac{x^{3}}{\left(a x + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a*x + b*x**3)**(3/2)` | $\frac{x^{2}}{\left(a x + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a*x + b*x**3)**(3/2)` | $\frac{x}{\left(a x + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*x + b*x**3)**(-3/2)` | $\frac{1}{\left(a x + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a*x + b*x**3)**(3/2))` | $\frac{1}{x \left(a x + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a*x + b*x**3)**(3/2))` | $\frac{1}{x^{2} \left(a x + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(29/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{29}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `x**(27/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{27}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `x**(25/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{25}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `x**(23/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{23}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(21/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{21}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `x**(19/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{19}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(17/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{17}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `x**(15/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{15}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(13/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{13}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(11/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{11}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(9/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{9}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `x**(7/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{7}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(5/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{5}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `x**(3/2)/(a*x + b*x**3)**(9/2)` | $\frac{x^{\frac{3}{2}}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(x)/(a*x + b*x**3)**(9/2)` | $\frac{\sqrt{x}}{\left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `1/(sqrt(x)*(a*x + b*x**3)**(9/2))` | $\frac{1}{\sqrt{x} \left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**(3/2)*(a*x + b*x**3)**(9/2))` | $\frac{1}{x^{\frac{3}{2}} \left(a x + b x^{3}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `x**4/sqrt(a*x + b*x**4)` | $\frac{x^{4}}{\sqrt{a x + b x^{4}}}$ |
| partial | parametric | `x/sqrt(a*x + b*x**4)` | $\frac{x}{\sqrt{a x + b x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**2*sqrt(a*x + b*x**4))` | $\frac{1}{x^{2} \sqrt{a x + b x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**5*sqrt(a*x + b*x**4))` | $\frac{1}{x^{5} \sqrt{a x + b x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**8*sqrt(a*x + b*x**4))` | $\frac{1}{x^{8} \sqrt{a x + b x^{4}}}$ |
| partial | parametric | `x**3/sqrt(a*x + b*x**4)` | $\frac{x^{3}}{\sqrt{a x + b x^{4}}}$ |
| partial | parametric | `1/sqrt(a*x + b*x**4)` | $\frac{1}{\sqrt{a x + b x^{4}}}$ |
| partial | parametric | `1/(x**3*sqrt(a*x + b*x**4))` | $\frac{1}{x^{3} \sqrt{a x + b x^{4}}}$ |
| partial | parametric | `x**5/sqrt(a*x + b*x**4)` | $\frac{x^{5}}{\sqrt{a x + b x^{4}}}$ |
| partial | parametric | `x**2/sqrt(a*x + b*x**4)` | $\frac{x^{2}}{\sqrt{a x + b x^{4}}}$ |
| partial | parametric | `1/(x*sqrt(a*x + b*x**4))` | $\frac{1}{x \sqrt{a x + b x^{4}}}$ |
| partial | parametric | `x**2/sqrt(a*x + b*sqrt(x))` | $\frac{x^{2}}{\sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `x/sqrt(a*x + b*sqrt(x))` | $\frac{x}{\sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `1/sqrt(a*x + b*sqrt(x))` | $\frac{1}{\sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `1/(x*sqrt(a*x + b*sqrt(x)))` | $\frac{1}{x \sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `1/(x**2*sqrt(a*x + b*sqrt(x)))` | $\frac{1}{x^{2} \sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `1/(x**3*sqrt(a*x + b*sqrt(x)))` | $\frac{1}{x^{3} \sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `1/(x**4*sqrt(a*x + b*sqrt(x)))` | $\frac{1}{x^{4} \sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `x**3/(a*x + b*sqrt(x))**(3/2)` | $\frac{x^{3}}{\left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a*x + b*sqrt(x))**(3/2)` | $\frac{x^{2}}{\left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a*x + b*sqrt(x))**(3/2)` | $\frac{x}{\left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*x + b*sqrt(x))**(-3/2)` | $\frac{1}{\left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a*x + b*sqrt(x))**(3/2))` | $\frac{1}{x \left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a*x + b*sqrt(x))**(3/2))` | $\frac{1}{x^{2} \left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a*x + b*sqrt(x))**(3/2))` | $\frac{1}{x^{3} \left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(5/2)/sqrt(a*x + b*sqrt(x))` | $\frac{x^{\frac{5}{2}}}{\sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `x**(3/2)/sqrt(a*x + b*sqrt(x))` | $\frac{x^{\frac{3}{2}}}{\sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `sqrt(x)/sqrt(a*x + b*sqrt(x))` | $\frac{\sqrt{x}}{\sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(a*x + b*sqrt(x)))` | $\frac{1}{\sqrt{x} \sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `1/(x**(3/2)*sqrt(a*x + b*sqrt(x)))` | $\frac{1}{x^{\frac{3}{2}} \sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `1/(x**(5/2)*sqrt(a*x + b*sqrt(x)))` | $\frac{1}{x^{\frac{5}{2}} \sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `1/(x**(7/2)*sqrt(a*x + b*sqrt(x)))` | $\frac{1}{x^{\frac{7}{2}} \sqrt{a x + b \sqrt{x}}}$ |
| partial | parametric | `x**(5/2)/(a*x + b*sqrt(x))**(3/2)` | $\frac{x^{\frac{5}{2}}}{\left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(3/2)/(a*x + b*sqrt(x))**(3/2)` | $\frac{x^{\frac{3}{2}}}{\left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)/(a*x + b*sqrt(x))**(3/2)` | $\frac{\sqrt{x}}{\left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(x)*(a*x + b*sqrt(x))**(3/2))` | $\frac{1}{\sqrt{x} \left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**(3/2)*(a*x + b*sqrt(x))**(3/2))` | $\frac{1}{x^{\frac{3}{2}} \left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**(5/2)*(a*x + b*sqrt(x))**(3/2))` | $\frac{1}{x^{\frac{5}{2}} \left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**(7/2)*(a*x + b*sqrt(x))**(3/2))` | $\frac{1}{x^{\frac{7}{2}} \left(a x + b \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*sqrt(a*x + b*x**(1/3))` | $x^{3} \sqrt{a x + b \sqrt[3]{x}}$ |
| partial | parametric | `x**2*sqrt(a*x + b*x**(1/3))` | $x^{2} \sqrt{a x + b \sqrt[3]{x}}$ |
| partial | parametric | `x*sqrt(a*x + b*x**(1/3))` | $x \sqrt{a x + b \sqrt[3]{x}}$ |
| partial | parametric | `sqrt(a*x + b*x**(1/3))` | $\sqrt{a x + b \sqrt[3]{x}}$ |
| partial | parametric | `sqrt(a*x + b*x**(1/3))/x` | $\frac{\sqrt{a x + b \sqrt[3]{x}}}{x}$ |
| partial | parametric | `sqrt(a*x + b*x**(1/3))/x**2` | $\frac{\sqrt{a x + b \sqrt[3]{x}}}{x^{2}}$ |
| partial | parametric | `sqrt(a*x + b*x**(1/3))/x**3` | $\frac{\sqrt{a x + b \sqrt[3]{x}}}{x^{3}}$ |
| partial | parametric | `sqrt(a*x + b*x**(1/3))/x**4` | $\frac{\sqrt{a x + b \sqrt[3]{x}}}{x^{4}}$ |
| partial | parametric | `sqrt(a*x + b*x**(1/3))/x**5` | $\frac{\sqrt{a x + b \sqrt[3]{x}}}{x^{5}}$ |
| partial | parametric | `x**2*(a*x + b*x**(1/3))**(3/2)` | $x^{2} \left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a*x + b*x**(1/3))**(3/2)` | $x \left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*x + b*x**(1/3))**(3/2)` | $\left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*x + b*x**(1/3))**(3/2)/x` | $\frac{\left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a*x + b*x**(1/3))**(3/2)/x**2` | $\frac{\left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a*x + b*x**(1/3))**(3/2)/x**3` | $\frac{\left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a*x + b*x**(1/3))**(3/2)/x**4` | $\frac{\left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(a*x + b*x**(1/3))**(3/2)/x**5` | $\frac{\left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(a*x + b*x**(1/3))**(3/2)/x**6` | $\frac{\left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `x**4/sqrt(a*x + b*x**(1/3))` | $\frac{x^{4}}{\sqrt{a x + b \sqrt[3]{x}}}$ |
| partial | parametric | `x**3/sqrt(a*x + b*x**(1/3))` | $\frac{x^{3}}{\sqrt{a x + b \sqrt[3]{x}}}$ |
| partial | parametric | `x**2/sqrt(a*x + b*x**(1/3))` | $\frac{x^{2}}{\sqrt{a x + b \sqrt[3]{x}}}$ |
| partial | parametric | `x/sqrt(a*x + b*x**(1/3))` | $\frac{x}{\sqrt{a x + b \sqrt[3]{x}}}$ |
| partial | parametric | `1/sqrt(a*x + b*x**(1/3))` | $\frac{1}{\sqrt{a x + b \sqrt[3]{x}}}$ |
| partial | parametric | `1/(x*sqrt(a*x + b*x**(1/3)))` | $\frac{1}{x \sqrt{a x + b \sqrt[3]{x}}}$ |
| partial | parametric | `1/(x**2*sqrt(a*x + b*x**(1/3)))` | $\frac{1}{x^{2} \sqrt{a x + b \sqrt[3]{x}}}$ |
| partial | parametric | `1/(x**3*sqrt(a*x + b*x**(1/3)))` | $\frac{1}{x^{3} \sqrt{a x + b \sqrt[3]{x}}}$ |
| partial | parametric | `1/(x**4*sqrt(a*x + b*x**(1/3)))` | $\frac{1}{x^{4} \sqrt{a x + b \sqrt[3]{x}}}$ |
| partial | parametric | `x**4/(a*x + b*x**(1/3))**(3/2)` | $\frac{x^{4}}{\left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/(a*x + b*x**(1/3))**(3/2)` | $\frac{x^{3}}{\left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a*x + b*x**(1/3))**(3/2)` | $\frac{x^{2}}{\left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a*x + b*x**(1/3))**(3/2)` | $\frac{x}{\left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*x + b*x**(1/3))**(-3/2)` | $\frac{1}{\left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a*x + b*x**(1/3))**(3/2))` | $\frac{1}{x \left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a*x + b*x**(1/3))**(3/2))` | $\frac{1}{x^{2} \left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a*x + b*x**(1/3))**(3/2))` | $\frac{1}{x^{3} \left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a*x + b*x**(1/3))**(3/2))` | $\frac{1}{x^{4} \left(a x + b \sqrt[3]{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*sqrt(a*x + b*x**(2/3))` | $x^{3} \sqrt{a x + b x^{\frac{2}{3}}}$ |
| partial | parametric | `x**2*sqrt(a*x + b*x**(2/3))` | $x^{2} \sqrt{a x + b x^{\frac{2}{3}}}$ |
| partial | parametric | `x*sqrt(a*x + b*x**(2/3))` | $x \sqrt{a x + b x^{\frac{2}{3}}}$ |
| partial | parametric | `sqrt(a*x + b*x**(2/3))` | $\sqrt{a x + b x^{\frac{2}{3}}}$ |
| partial | parametric | `sqrt(a*x + b*x**(2/3))/x` | $\frac{\sqrt{a x + b x^{\frac{2}{3}}}}{x}$ |
| partial | parametric | `sqrt(a*x + b*x**(2/3))/x**2` | $\frac{\sqrt{a x + b x^{\frac{2}{3}}}}{x^{2}}$ |
| partial | parametric | `sqrt(a*x + b*x**(2/3))/x**3` | $\frac{\sqrt{a x + b x^{\frac{2}{3}}}}{x^{3}}$ |
| partial | parametric | `sqrt(a*x + b*x**(2/3))/x**4` | $\frac{\sqrt{a x + b x^{\frac{2}{3}}}}{x^{4}}$ |
| partial | parametric | `sqrt(a*x + b*x**(2/3))/x**5` | $\frac{\sqrt{a x + b x^{\frac{2}{3}}}}{x^{5}}$ |
| partial | parametric | `x**2*(a*x + b*x**(2/3))**(3/2)` | $x^{2} \left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a*x + b*x**(2/3))**(3/2)` | $x \left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*x + b*x**(2/3))**(3/2)` | $\left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*x + b*x**(2/3))**(3/2)/x` | $\frac{\left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a*x + b*x**(2/3))**(3/2)/x**2` | $\frac{\left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a*x + b*x**(2/3))**(3/2)/x**3` | $\frac{\left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a*x + b*x**(2/3))**(3/2)/x**4` | $\frac{\left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(a*x + b*x**(2/3))**(3/2)/x**5` | $\frac{\left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(a*x + b*x**(2/3))**(3/2)/x**6` | $\frac{\left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `x**4/sqrt(a*x + b*x**(2/3))` | $\frac{x^{4}}{\sqrt{a x + b x^{\frac{2}{3}}}}$ |
| partial | parametric | `x**3/sqrt(a*x + b*x**(2/3))` | $\frac{x^{3}}{\sqrt{a x + b x^{\frac{2}{3}}}}$ |
| partial | parametric | `x**2/sqrt(a*x + b*x**(2/3))` | $\frac{x^{2}}{\sqrt{a x + b x^{\frac{2}{3}}}}$ |
| partial | parametric | `x/sqrt(a*x + b*x**(2/3))` | $\frac{x}{\sqrt{a x + b x^{\frac{2}{3}}}}$ |
| partial | parametric | `1/sqrt(a*x + b*x**(2/3))` | $\frac{1}{\sqrt{a x + b x^{\frac{2}{3}}}}$ |
| partial | parametric | `1/(x*sqrt(a*x + b*x**(2/3)))` | $\frac{1}{x \sqrt{a x + b x^{\frac{2}{3}}}}$ |
| partial | parametric | `1/(x**2*sqrt(a*x + b*x**(2/3)))` | $\frac{1}{x^{2} \sqrt{a x + b x^{\frac{2}{3}}}}$ |
| partial | parametric | `1/(x**3*sqrt(a*x + b*x**(2/3)))` | $\frac{1}{x^{3} \sqrt{a x + b x^{\frac{2}{3}}}}$ |
| partial | parametric | `1/(x**4*sqrt(a*x + b*x**(2/3)))` | $\frac{1}{x^{4} \sqrt{a x + b x^{\frac{2}{3}}}}$ |
| partial | parametric | `x**4/(a*x + b*x**(2/3))**(3/2)` | $\frac{x^{4}}{\left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/(a*x + b*x**(2/3))**(3/2)` | $\frac{x^{3}}{\left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a*x + b*x**(2/3))**(3/2)` | $\frac{x^{2}}{\left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a*x + b*x**(2/3))**(3/2)` | $\frac{x}{\left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*x + b*x**(2/3))**(-3/2)` | $\frac{1}{\left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a*x + b*x**(2/3))**(3/2))` | $\frac{1}{x \left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a*x + b*x**(2/3))**(3/2))` | $\frac{1}{x^{2} \left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a*x + b*x**(2/3))**(3/2))` | $\frac{1}{x^{3} \left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a*x + b*x**(2/3))**(3/2))` | $\frac{1}{x^{4} \left(a x + b x^{\frac{2}{3}}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2*sqrt(a*x**2 + b*x**3)` | $x^{2} \sqrt{a x^{2} + b x^{3}}$ |
| **SOLVED-NEW** | parametric | `x*sqrt(a*x**2 + b*x**3)` | $x \sqrt{a x^{2} + b x^{3}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a*x**2 + b*x**3)` | $\sqrt{a x^{2} + b x^{3}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a*x**2 + b*x**3)/x` | $\frac{\sqrt{a x^{2} + b x^{3}}}{x}$ |
| partial | parametric | `sqrt(a*x**2 + b*x**3)/x**2` | $\frac{\sqrt{a x^{2} + b x^{3}}}{x^{2}}$ |
| partial | parametric | `sqrt(a*x**2 + b*x**3)/x**3` | $\frac{\sqrt{a x^{2} + b x^{3}}}{x^{3}}$ |
| partial | parametric | `sqrt(a*x**2 + b*x**3)/x**4` | $\frac{\sqrt{a x^{2} + b x^{3}}}{x^{4}}$ |
| partial | parametric | `sqrt(a*x**2 + b*x**3)/x**5` | $\frac{\sqrt{a x^{2} + b x^{3}}}{x^{5}}$ |
| partial | parametric | `x**2*(a*x**2 + b*x**3)**(3/2)` | $x^{2} \left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a*x**2 + b*x**3)**(3/2)` | $x \left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*x**2 + b*x**3)**(3/2)` | $\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*x**2 + b*x**3)**(3/2)/x` | $\frac{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a*x**2 + b*x**3)**(3/2)/x**2` | $\frac{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a*x**2 + b*x**3)**(3/2)/x**3` | $\frac{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a*x**2 + b*x**3)**(3/2)/x**4` | $\frac{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(a*x**2 + b*x**3)**(3/2)/x**5` | $\frac{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(a*x**2 + b*x**3)**(3/2)/x**6` | $\frac{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(a*x**2 + b*x**3)**(3/2)/x**7` | $\frac{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `(a*x**2 + b*x**3)**(3/2)/x**8` | $\frac{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}{x^{8}}$ |
| partial | parametric | `(a*x**2 + b*x**3)**(3/2)/x**9` | $\frac{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `x**4/sqrt(a*x**2 + b*x**3)` | $\frac{x^{4}}{\sqrt{a x^{2} + b x^{3}}}$ |
| **SOLVED-NEW** | parametric | `x**3/sqrt(a*x**2 + b*x**3)` | $\frac{x^{3}}{\sqrt{a x^{2} + b x^{3}}}$ |
| **SOLVED-NEW** | parametric | `x**2/sqrt(a*x**2 + b*x**3)` | $\frac{x^{2}}{\sqrt{a x^{2} + b x^{3}}}$ |
| **SOLVED-NEW** | parametric | `x/sqrt(a*x**2 + b*x**3)` | $\frac{x}{\sqrt{a x^{2} + b x^{3}}}$ |
| partial | parametric | `1/sqrt(a*x**2 + b*x**3)` | $\frac{1}{\sqrt{a x^{2} + b x^{3}}}$ |
| partial | parametric | `1/(x*sqrt(a*x**2 + b*x**3))` | $\frac{1}{x \sqrt{a x^{2} + b x^{3}}}$ |
| partial | parametric | `1/(x**2*sqrt(a*x**2 + b*x**3))` | $\frac{1}{x^{2} \sqrt{a x^{2} + b x^{3}}}$ |
| partial | parametric | `1/(x**3*sqrt(a*x**2 + b*x**3))` | $\frac{1}{x^{3} \sqrt{a x^{2} + b x^{3}}}$ |
| **SOLVED-NEW** | parametric | `x**6/(a*x**2 + b*x**3)**(3/2)` | $\frac{x^{6}}{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**5/(a*x**2 + b*x**3)**(3/2)` | $\frac{x^{5}}{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**4/(a*x**2 + b*x**3)**(3/2)` | $\frac{x^{4}}{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**3/(a*x**2 + b*x**3)**(3/2)` | $\frac{x^{3}}{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a*x**2 + b*x**3)**(3/2)` | $\frac{x^{2}}{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a*x**2 + b*x**3)**(3/2)` | $\frac{x}{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*x**2 + b*x**3)**(-3/2)` | $\frac{1}{\left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a*x**2 + b*x**3)**(3/2))` | $\frac{1}{x \left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a*x**2 + b*x**3)**(3/2))` | $\frac{1}{x^{2} \left(a x^{2} + b x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(7/2)/sqrt(a*x**2 + b*x**3)` | $\frac{x^{\frac{7}{2}}}{\sqrt{a x^{2} + b x^{3}}}$ |
| partial | parametric | `x**(5/2)/sqrt(a*x**2 + b*x**3)` | $\frac{x^{\frac{5}{2}}}{\sqrt{a x^{2} + b x^{3}}}$ |
| partial | parametric | `x**(3/2)/sqrt(a*x**2 + b*x**3)` | $\frac{x^{\frac{3}{2}}}{\sqrt{a x^{2} + b x^{3}}}$ |
| partial | parametric | `sqrt(x)/sqrt(a*x**2 + b*x**3)` | $\frac{\sqrt{x}}{\sqrt{a x^{2} + b x^{3}}}$ |
| **SOLVED-NEW** | parametric | `1/(sqrt(x)*sqrt(a*x**2 + b*x**3))` | $\frac{1}{\sqrt{x} \sqrt{a x^{2} + b x^{3}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**(3/2)*sqrt(a*x**2 + b*x**3))` | $\frac{1}{x^{\frac{3}{2}} \sqrt{a x^{2} + b x^{3}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**(5/2)*sqrt(a*x**2 + b*x**3))` | $\frac{1}{x^{\frac{5}{2}} \sqrt{a x^{2} + b x^{3}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**(7/2)*sqrt(a*x**2 + b*x**3))` | $\frac{1}{x^{\frac{7}{2}} \sqrt{a x^{2} + b x^{3}}}$ |
| **SOLVED-NEW** | parametric | `x**9/sqrt(a*x**2 + b*x**5)` | $\frac{x^{9}}{\sqrt{a x^{2} + b x^{5}}}$ |
| **SOLVED-NEW** | parametric | `x**6/sqrt(a*x**2 + b*x**5)` | $\frac{x^{6}}{\sqrt{a x^{2} + b x^{5}}}$ |
| **SOLVED-NEW** | parametric | `x**3/sqrt(a*x**2 + b*x**5)` | $\frac{x^{3}}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `1/sqrt(a*x**2 + b*x**5)` | $\frac{1}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `1/(x**3*sqrt(a*x**2 + b*x**5))` | $\frac{1}{x^{3} \sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `x**4/sqrt(a*x**2 + b*x**5)` | $\frac{x^{4}}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `x/sqrt(a*x**2 + b*x**5)` | $\frac{x}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `1/(x**2*sqrt(a*x**2 + b*x**5))` | $\frac{1}{x^{2} \sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `x**5/sqrt(a*x**2 + b*x**5)` | $\frac{x^{5}}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `x**2/sqrt(a*x**2 + b*x**5)` | $\frac{x^{2}}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `1/(x*sqrt(a*x**2 + b*x**5))` | $\frac{1}{x \sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `x**(13/2)/sqrt(a*x**2 + b*x**5)` | $\frac{x^{\frac{13}{2}}}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `x**(11/2)/sqrt(a*x**2 + b*x**5)` | $\frac{x^{\frac{11}{2}}}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `x**(9/2)/sqrt(a*x**2 + b*x**5)` | $\frac{x^{\frac{9}{2}}}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `x**(7/2)/sqrt(a*x**2 + b*x**5)` | $\frac{x^{\frac{7}{2}}}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `x**(5/2)/sqrt(a*x**2 + b*x**5)` | $\frac{x^{\frac{5}{2}}}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `x**(3/2)/sqrt(a*x**2 + b*x**5)` | $\frac{x^{\frac{3}{2}}}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `sqrt(x)/sqrt(a*x**2 + b*x**5)` | $\frac{\sqrt{x}}{\sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(a*x**2 + b*x**5))` | $\frac{1}{\sqrt{x} \sqrt{a x^{2} + b x^{5}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**(3/2)*sqrt(a*x**2 + b*x**5))` | $\frac{1}{x^{\frac{3}{2}} \sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `1/(x**(5/2)*sqrt(a*x**2 + b*x**5))` | $\frac{1}{x^{\frac{5}{2}} \sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `1/(x**(7/2)*sqrt(a*x**2 + b*x**5))` | $\frac{1}{x^{\frac{7}{2}} \sqrt{a x^{2} + b x^{5}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**(9/2)*sqrt(a*x**2 + b*x**5))` | $\frac{1}{x^{\frac{9}{2}} \sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `1/(x**(11/2)*sqrt(a*x**2 + b*x**5))` | $\frac{1}{x^{\frac{11}{2}} \sqrt{a x^{2} + b x^{5}}}$ |
| partial | parametric | `x**4/sqrt(a*x**3 + b*x**4)` | $\frac{x^{4}}{\sqrt{a x^{3} + b x^{4}}}$ |
| partial | parametric | `x**3/sqrt(a*x**3 + b*x**4)` | $\frac{x^{3}}{\sqrt{a x^{3} + b x^{4}}}$ |
| partial | parametric | `x**2/sqrt(a*x**3 + b*x**4)` | $\frac{x^{2}}{\sqrt{a x^{3} + b x^{4}}}$ |
| partial | parametric | `x/sqrt(a*x**3 + b*x**4)` | $\frac{x}{\sqrt{a x^{3} + b x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/sqrt(a*x**3 + b*x**4)` | $\frac{1}{\sqrt{a x^{3} + b x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x*sqrt(a*x**3 + b*x**4))` | $\frac{1}{x \sqrt{a x^{3} + b x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**2*sqrt(a*x**3 + b*x**4))` | $\frac{1}{x^{2} \sqrt{a x^{3} + b x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**3*sqrt(a*x**3 + b*x**4))` | $\frac{1}{x^{3} \sqrt{a x^{3} + b x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**4*sqrt(a*x**3 + b*x**4))` | $\frac{1}{x^{4} \sqrt{a x^{3} + b x^{4}}}$ |
| SOLVED-both | concrete | `1/(-sqrt(x) + x)` | $\frac{1}{- \sqrt{x} + x}$ |
| SOLVED-both | concrete | `1/(-x**(3/5) + x)` | $\frac{1}{- x^{\frac{3}{5}} + x}$ |
| SOLVED-both | concrete | `1/(x + x**(-1/3))` | $\frac{1}{x + \frac{1}{\sqrt[3]{x}}}$ |
| partial | parametric | `sqrt((a + b*x)/x**2)` | $\sqrt{\frac{a + b x}{x^{2}}}$ |
| partial | parametric | `sqrt((a + b*x**2)/x**2)` | $\sqrt{\frac{a + b x^{2}}{x^{2}}}$ |
| partial | parametric | `sqrt((a + b*x**3)/x**2)` | $\sqrt{\frac{a + b x^{3}}{x^{2}}}$ |
| partial | parametric | `sqrt((-a + b*x)/x**2)` | $\sqrt{\frac{- a + b x}{x^{2}}}$ |
| partial | parametric | `sqrt((-a + b*x**2)/x**2)` | $\sqrt{\frac{- a + b x^{2}}{x^{2}}}$ |
| partial | parametric | `sqrt((-a + b*x**3)/x**2)` | $\sqrt{\frac{- a + b x^{3}}{x^{2}}}$ |
| partial | parametric | `1/sqrt((a + b*x**3)/x)` | $\frac{1}{\sqrt{\frac{a + b x^{3}}{x}}}$ |
| partial | parametric | `1/sqrt((a + b*x**4)/x**2)` | $\frac{1}{\sqrt{\frac{a + b x^{4}}{x^{2}}}}$ |
| partial | parametric | `1/sqrt((a + b*x**5)/x**3)` | $\frac{1}{\sqrt{\frac{a + b x^{5}}{x^{3}}}}$ |
| partial | parametric | `1/sqrt((a - b*x**3)/x)` | $\frac{1}{\sqrt{\frac{a - b x^{3}}{x}}}$ |
| partial | parametric | `1/sqrt((a - b*x**4)/x**2)` | $\frac{1}{\sqrt{\frac{a - b x^{4}}{x^{2}}}}$ |
| partial | parametric | `1/sqrt((a - b*x**5)/x**3)` | $\frac{1}{\sqrt{\frac{a - b x^{5}}{x^{3}}}}$ |
| **SOLVED-NEW** | concrete | `sqrt((x + 1)/x**5)` | $\sqrt{\frac{x + 1}{x^{5}}}$ |
| partial | concrete | `sqrt(x**(5/2) + x)` | $\sqrt{x^{\frac{5}{2}} + x}$ |
| partial | concrete | `1/(x**(3/2) + sqrt(x))` | $\frac{1}{x^{\frac{3}{2}} + \sqrt{x}}$ |
| **SOLVED-NEW** | parametric | `x*sqrt(x**2*(a + b*x**3))` | $x \sqrt{x^{2} \left(a + b x^{3}\right)}$ |
| **SOLVED-NEW** | parametric | `x*sqrt(a*x**2 + b*x**5)` | $x \sqrt{a x^{2} + b x^{5}}$ |
| partial | parametric | `sqrt(x**4*(a + b*x**3))` | $\sqrt{x^{4} \left(a + b x^{3}\right)}$ |
| partial | parametric | `(a*x**(1/3) + b*x**(2/3))**(-1/3)` | $\frac{1}{\sqrt[3]{a \sqrt[3]{x} + b x^{\frac{2}{3}}}}$ |
| partial | parametric | `(a*x**(1/3) + b*x**(2/3))**(-2/3)` | $\frac{1}{\left(a \sqrt[3]{x} + b x^{\frac{2}{3}}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `x**7*(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | $x^{7} \left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**5*(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | $x^{5} \left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**3*(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | $x^{3} \left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `x*(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | $x \left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**3` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{3}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**5` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**7` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**9` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**11` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**13` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{13}}$ |
| **SOLVED-NEW** | parametric | `x**4*(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | $x^{4} \left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}$ |
| **SOLVED-NEW** | parametric | `x**2*(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | $x^{2} \left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | $\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**2` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{2}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**4` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{4}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**6` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{6}}$ |
| partial | parametric | `x**5*(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | $x^{5} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**3*(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | $x^{3} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | $x \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**3` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**5` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**7` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**9` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**11` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**13` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{13}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**15` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{15}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**17` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{17}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**19` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{19}}$ |
| partial | parametric | `x**4*(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | $x^{4} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | $x^{2} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | $\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**2` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**4` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**6` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**8` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{8}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**10` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{10}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**12` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{12}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**14` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{14}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**16` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{16}}$ |
| partial | parametric | `x**7*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{7} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**5*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{5} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**3*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{3} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x \sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)/(x**3*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{3} \sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)/(x**5*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{5} \sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)/(x**7*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{7} \sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)/(x**9*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{9} \sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `x**6*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{6} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `x**4*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{4} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `x**2*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{2} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{A + B x^{2}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x**2*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{2} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x**4*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{4} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**9*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{9} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**7*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{7} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{5} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{3} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)/(x*(b*x**2 + c*x**4)**(3/2))` | $\frac{A + B x^{2}}{x \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)/(x**3*(b*x**2 + c*x**4)**(3/2))` | $\frac{A + B x^{2}}{x^{3} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x**2)/(x**5*(b*x**2 + c*x**4)**(3/2))` | $\frac{A + B x^{2}}{x^{5} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**8*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{8} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**6*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{6} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**4*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{4} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{2} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{A + B x^{2}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x**2*(b*x**2 + c*x**4)**(3/2))` | $\frac{A + B x^{2}}{x^{2} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x**2)*(b*x**2 + c*x**4)` | $x^{\frac{7}{2}} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x**2)*(b*x**2 + c*x**4)` | $x^{\frac{5}{2}} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x**2)*(b*x**2 + c*x**4)` | $x^{\frac{3}{2}} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x**2)*(b*x**2 + c*x**4)` | $\sqrt{x} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)$ |
| SOLVED-both | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)/sqrt(x)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)/x**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)/x**(5/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)/x**(7/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x**2)*(b*x**2 + c*x**4)**2` | $x^{\frac{7}{2}} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x**2)*(b*x**2 + c*x**4)**2` | $x^{\frac{5}{2}} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x**2)*(b*x**2 + c*x**4)**2` | $x^{\frac{3}{2}} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x**2)*(b*x**2 + c*x**4)**2` | $\sqrt{x} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**2/sqrt(x)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**2/x**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**2/x**(5/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**2/x**(7/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x**2)*(b*x**2 + c*x**4)**3` | $x^{\frac{7}{2}} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x**2)*(b*x**2 + c*x**4)**3` | $x^{\frac{5}{2}} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x**2)*(b*x**2 + c*x**4)**3` | $x^{\frac{3}{2}} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x**2)*(b*x**2 + c*x**4)**3` | $\sqrt{x} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**3/sqrt(x)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**3/x**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**3/x**(5/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**3/x**(7/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{3}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `x**(13/2)*(A + B*x**2)/(b*x**2 + c*x**4)` | $\frac{x^{\frac{13}{2}} \left(A + B x^{2}\right)}{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(11/2)*(A + B*x**2)/(b*x**2 + c*x**4)` | $\frac{x^{\frac{11}{2}} \left(A + B x^{2}\right)}{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(9/2)*(A + B*x**2)/(b*x**2 + c*x**4)` | $\frac{x^{\frac{9}{2}} \left(A + B x^{2}\right)}{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(7/2)*(A + B*x**2)/(b*x**2 + c*x**4)` | $\frac{x^{\frac{7}{2}} \left(A + B x^{2}\right)}{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**2)/(b*x**2 + c*x**4)` | $\frac{x^{\frac{5}{2}} \left(A + B x^{2}\right)}{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**2)/(b*x**2 + c*x**4)` | $\frac{x^{\frac{3}{2}} \left(A + B x^{2}\right)}{b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**2)/(b*x**2 + c*x**4)` | $\frac{\sqrt{x} \left(A + B x^{2}\right)}{b x^{2} + c x^{4}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(x)*(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{\sqrt{x} \left(b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `(A + B*x**2)/(x**(3/2)*(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{\frac{3}{2}} \left(b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `(A + B*x**2)/(x**(5/2)*(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{\frac{5}{2}} \left(b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `(A + B*x**2)/(x**(7/2)*(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{\frac{7}{2}} \left(b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `(A + B*x**2)/(x**(9/2)*(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{\frac{9}{2}} \left(b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**(19/2)*(A + B*x**2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{19}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(17/2)*(A + B*x**2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{17}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(15/2)*(A + B*x**2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{15}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(13/2)*(A + B*x**2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{13}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(11/2)*(A + B*x**2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{11}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(9/2)*(A + B*x**2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{9}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(7/2)*(A + B*x**2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{7}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{5}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{3}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**2)/(b*x**2 + c*x**4)**2` | $\frac{\sqrt{x} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(x)*(b*x**2 + c*x**4)**2)` | $\frac{A + B x^{2}}{\sqrt{x} \left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `(A + B*x**2)/(x**(3/2)*(b*x**2 + c*x**4)**2)` | $\frac{A + B x^{2}}{x^{\frac{3}{2}} \left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(23/2)*(A + B*x**2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{23}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(21/2)*(A + B*x**2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{21}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(19/2)*(A + B*x**2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{19}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(17/2)*(A + B*x**2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{17}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(15/2)*(A + B*x**2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{15}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(13/2)*(A + B*x**2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{13}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(11/2)*(A + B*x**2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{11}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(9/2)*(A + B*x**2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{9}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(7/2)*(A + B*x**2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{7}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{5}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{3}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**2)/(b*x**2 + c*x**4)**3` | $\frac{\sqrt{x} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(x)*(b*x**2 + c*x**4)**3)` | $\frac{A + B x^{2}}{\sqrt{x} \left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | $x^{\frac{5}{2}} \left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | $x^{\frac{3}{2}} \left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | $\sqrt{x} \left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/sqrt(x)` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{\sqrt{x}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**(3/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**(5/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**(7/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**(9/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**(11/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**(13/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{\frac{13}{2}}}$ |
| partial | parametric | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**(15/2)` | $\frac{\left(A + B x^{2}\right) \sqrt{b x^{2} + c x^{4}}}{x^{\frac{15}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | $x^{\frac{7}{2}} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | $x^{\frac{5}{2}} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | $x^{\frac{3}{2}} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | $\sqrt{x} \left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/sqrt(x)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**(5/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**(7/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**(9/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**(11/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**(13/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{13}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**(15/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{15}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**(17/2)` | $\frac{\left(A + B x^{2}\right) \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{17}{2}}}$ |
| partial | parametric | `x**(13/2)*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{\frac{13}{2}} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**(11/2)*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{\frac{11}{2}} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**(9/2)*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{\frac{9}{2}} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{\frac{7}{2}} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{\frac{5}{2}} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{\frac{3}{2}} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | $\frac{\sqrt{x} \left(A + B x^{2}\right)}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(x)*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{\sqrt{x} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x**(3/2)*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{\frac{3}{2}} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x**(5/2)*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{\frac{5}{2}} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x**(7/2)*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{\frac{7}{2}} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x**(9/2)*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{\frac{9}{2}} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x**(11/2)*sqrt(b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{\frac{11}{2}} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**(17/2)*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{17}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(15/2)*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{15}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(13/2)*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{13}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(11/2)*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{11}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(9/2)*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{9}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{7}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{5}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(3/2)*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{3}{2}} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{\sqrt{x} \left(A + B x^{2}\right)}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(x)*(b*x**2 + c*x**4)**(3/2))` | $\frac{A + B x^{2}}{\sqrt{x} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x**(3/2)*(b*x**2 + c*x**4)**(3/2))` | $\frac{A + B x^{2}}{x^{\frac{3}{2}} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(x**(5/2)*(b*x**2 + c*x**4)**(3/2))` | $\frac{A + B x^{2}}{x^{\frac{5}{2}} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
