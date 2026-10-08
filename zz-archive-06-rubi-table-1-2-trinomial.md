# 1.2 Trinomial products

All attempted radical cases from this part of the Rubi corpus, run through `risch_integrate(f, x, algebraic=True)` (sympy branch `risch-algebraic`).  **SOLVED-NEW** means solved here but not by sympy's non-risch `integrate()`; SOLVED-both means both solve it.  6148 cases: partial 4451 (72%), SOLVED-both 874 (14%), SOLVED-NEW 617 (10%), timeout 203 (3%), NIE 3 (0%).

| Status | Kind | SymPy expression | Math |
|---|---|---|---|
| partial | parametric | `(b*x + c*x**2)**(7/2)` | $\left(b x + c x^{2}\right)^{\frac{7}{2}}$ |
| partial | concrete | `(4*x**2 + 3*I*x)**(7/2)` | $\left(4 x^{2} + 3 i x\right)^{\frac{7}{2}}$ |
| partial | concrete | `(4*x**2 + 3*I*x)**(5/2)` | $\left(4 x^{2} + 3 i x\right)^{\frac{5}{2}}$ |
| partial | concrete | `(4*x**2 + 3*I*x)**(3/2)` | $\left(4 x^{2} + 3 i x\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(4*x**2 + 3*I*x)` | $\sqrt{4 x^{2} + 3 i x}$ |
| partial | concrete | `(-4*x**2 + 3*x)**(7/2)` | $\left(- 4 x^{2} + 3 x\right)^{\frac{7}{2}}$ |
| partial | concrete | `(-4*x**2 + 3*x)**(5/2)` | $\left(- 4 x^{2} + 3 x\right)^{\frac{5}{2}}$ |
| partial | concrete | `(-4*x**2 + 3*x)**(3/2)` | $\left(- 4 x^{2} + 3 x\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(-4*x**2 + 3*x)` | $\sqrt{- 4 x^{2} + 3 x}$ |
| partial | concrete | `sqrt(-x**2 + 6*x)` | $\sqrt{- x^{2} + 6 x}$ |
| partial | concrete | `sqrt(-9*x**2 + 5*x)` | $\sqrt{- 9 x^{2} + 5 x}$ |
| partial | concrete | `(-x**2 + x)**(3/2)` | $\left(- x^{2} + x\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(x**2 + 4*x)` | $\sqrt{x^{2} + 4 x}$ |
| partial | concrete | `sqrt(x**2 - 8*x)` | $\sqrt{x^{2} - 8 x}$ |
| partial | concrete | `sqrt(x**2 - x)` | $\sqrt{x^{2} - x}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)**(-7/2)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| partial | concrete | `1/sqrt(4*x**2 + 3*I*x)` | $\frac{1}{\sqrt{4 x^{2} + 3 i x}}$ |
| partial | concrete | `(4*x**2 + 3*I*x)**(-3/2)` | $\frac{1}{\left(4 x^{2} + 3 i x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*I*x)**(-5/2)` | $\frac{1}{\left(4 x^{2} + 3 i x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*I*x)**(-7/2)` | $\frac{1}{\left(4 x^{2} + 3 i x\right)^{\frac{7}{2}}}$ |
| partial | concrete | `1/sqrt(-4*x**2 + 3*x)` | $\frac{1}{\sqrt{- 4 x^{2} + 3 x}}$ |
| SOLVED-both | concrete | `(-4*x**2 + 3*x)**(-3/2)` | $\frac{1}{\left(- 4 x^{2} + 3 x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(-4*x**2 + 3*x)**(-5/2)` | $\frac{1}{\left(- 4 x^{2} + 3 x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(-4*x**2 + 3*x)**(-7/2)` | $\frac{1}{\left(- 4 x^{2} + 3 x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `1/sqrt(-b**2*x**2 + b*x)` | $\frac{1}{\sqrt{- b^{2} x^{2} + b x}}$ |
| partial | parametric | `1/sqrt(b**2*x**2 + b*x)` | $\frac{1}{\sqrt{b^{2} x^{2} + b x}}$ |
| partial | concrete | `1/sqrt(-x**2 + 6*x)` | $\frac{1}{\sqrt{- x^{2} + 6 x}}$ |
| partial | concrete | `1/sqrt(x**2 + 4*x)` | $\frac{1}{\sqrt{x^{2} + 4 x}}$ |
| partial | concrete | `1/sqrt(x**2 - 2*x)` | $\frac{1}{\sqrt{x^{2} - 2 x}}$ |
| partial | parametric | `(b*x + c*x**2)**(4/3)` | $\left(b x + c x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(b*x + c*x**2)**(1/3)` | $\sqrt[3]{b x + c x^{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(-2/3)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(b*x + c*x**2)**(-5/3)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{5}{3}}}$ |
| partial | parametric | `(b*x + c*x**2)**(-8/3)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{8}{3}}}$ |
| partial | parametric | `(b*x + c*x**2)**(5/3)` | $\left(b x + c x^{2}\right)^{\frac{5}{3}}$ |
| partial | parametric | `(b*x + c*x**2)**(2/3)` | $\left(b x + c x^{2}\right)^{\frac{2}{3}}$ |
| partial | parametric | `(b*x + c*x**2)**(-1/3)` | $\frac{1}{\sqrt[3]{b x + c x^{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(-4/3)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(b*x + c*x**2)**(-7/3)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{7}{3}}}$ |
| partial | parametric | `(b*x + c*x**2)**(5/4)` | $\left(b x + c x^{2}\right)^{\frac{5}{4}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/4)` | $\left(b x + c x^{2}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(b*x + c*x**2)**(1/4)` | $\sqrt[4]{b x + c x^{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(-1/4)` | $\frac{1}{\sqrt[4]{b x + c x^{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(-3/4)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(b*x + c*x**2)**(-5/4)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(b*x + c*x**2)**(-9/4)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{9}{4}}}$ |
| partial | parametric | `(b*x + c*x**2)**(-13/4)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{13}{4}}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)` | $\left(a + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)` | $\left(a + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(a + c*x**2)` | $\sqrt{a + c x^{2}}$ |
| partial | parametric | `1/sqrt(a + c*x**2)` | $\frac{1}{\sqrt{a + c x^{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**(-3/2)` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**(-5/2)` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**(-7/2)` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**(-9/2)` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | concrete | `(9*x**2 + 12*x + 4)**(3/2)` | $\left(9 x^{2} + 12 x + 4\right)^{\frac{3}{2}}$ |
| SOLVED-both | concrete | `sqrt(9*x**2 + 12*x + 4)` | $\sqrt{9 x^{2} + 12 x + 4}$ |
| SOLVED-both | concrete | `1/sqrt(9*x**2 + 12*x + 4)` | $\frac{1}{\sqrt{9 x^{2} + 12 x + 4}}$ |
| SOLVED-both | concrete | `(9*x**2 + 12*x + 4)**(-3/2)` | $\frac{1}{\left(9 x^{2} + 12 x + 4\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `sqrt(9*x**2 - 12*x + 4)` | $\sqrt{9 x^{2} - 12 x + 4}$ |
| SOLVED-both | concrete | `1/sqrt(9*x**2 - 12*x + 4)` | $\frac{1}{\sqrt{9 x^{2} - 12 x + 4}}$ |
| SOLVED-both | concrete | `sqrt(-9*x**2 + 12*x - 4)` | $\sqrt{- 9 x^{2} + 12 x - 4}$ |
| SOLVED-both | concrete | `1/sqrt(-9*x**2 + 12*x - 4)` | $\frac{1}{\sqrt{- 9 x^{2} + 12 x - 4}}$ |
| SOLVED-both | concrete | `sqrt(-9*x**2 - 12*x - 4)` | $\sqrt{- 9 x^{2} - 12 x - 4}$ |
| SOLVED-both | concrete | `1/sqrt(-9*x**2 - 12*x - 4)` | $\frac{1}{\sqrt{- 9 x^{2} - 12 x - 4}}$ |
| partial | concrete | `sqrt(9*x**2 - 6*x + 5)` | $\sqrt{9 x^{2} - 6 x + 5}$ |
| partial | concrete | `sqrt(-4*x**2 - 4*x + 3)` | $\sqrt{- 4 x^{2} - 4 x + 3}$ |
| partial | concrete | `sqrt(9*x**2 + 6*x - 8)` | $\sqrt{9 x^{2} + 6 x - 8}$ |
| partial | concrete | `sqrt(3*x**2 + 4*x + 2)` | $\sqrt{3 x^{2} + 4 x + 2}$ |
| partial | concrete | `sqrt(-3*x**2 + 4*x + 2)` | $\sqrt{- 3 x^{2} + 4 x + 2}$ |
| partial | concrete | `sqrt(3*x**2 + 5*x + 2)` | $\sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `sqrt(-3*x**2 + 5*x + 2)` | $\sqrt{- 3 x^{2} + 5 x + 2}$ |
| partial | concrete | `sqrt(3*x**2 + 4*x - 2)` | $\sqrt{3 x^{2} + 4 x - 2}$ |
| partial | concrete | `sqrt(-3*x**2 + 4*x - 2)` | $\sqrt{- 3 x^{2} + 4 x - 2}$ |
| partial | concrete | `sqrt(3*x**2 + 5*x - 2)` | $\sqrt{3 x^{2} + 5 x - 2}$ |
| partial | concrete | `sqrt(-3*x**2 + 5*x - 2)` | $\sqrt{- 3 x^{2} + 5 x - 2}$ |
| partial | concrete | `1/sqrt(9*x**2 - 6*x + 5)` | $\frac{1}{\sqrt{9 x^{2} - 6 x + 5}}$ |
| partial | concrete | `1/sqrt(-4*x**2 - 4*x + 3)` | $\frac{1}{\sqrt{- 4 x^{2} - 4 x + 3}}$ |
| partial | concrete | `1/sqrt(9*x**2 + 6*x - 8)` | $\frac{1}{\sqrt{9 x^{2} + 6 x - 8}}$ |
| partial | concrete | `1/sqrt(3*x**2 + 4*x + 2)` | $\frac{1}{\sqrt{3 x^{2} + 4 x + 2}}$ |
| partial | concrete | `1/sqrt(-3*x**2 + 4*x + 2)` | $\frac{1}{\sqrt{- 3 x^{2} + 4 x + 2}}$ |
| partial | concrete | `1/sqrt(3*x**2 + 5*x + 2)` | $\frac{1}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `1/sqrt(-3*x**2 + 5*x + 2)` | $\frac{1}{\sqrt{- 3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `1/sqrt(3*x**2 + 4*x - 2)` | $\frac{1}{\sqrt{3 x^{2} + 4 x - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**2 + 4*x - 2)` | $\frac{1}{\sqrt{- 3 x^{2} + 4 x - 2}}$ |
| partial | concrete | `1/sqrt(3*x**2 + 5*x - 2)` | $\frac{1}{\sqrt{3 x^{2} + 5 x - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**2 + 5*x - 2)` | $\frac{1}{\sqrt{- 3 x^{2} + 5 x - 2}}$ |
| partial | parametric | `1/sqrt(b*x + c*x**2 + (b**2 + 4*c)/(4*c))` | $\frac{1}{\sqrt{b x + c x^{2} + \frac{b^{2} + 4 c}{4 c}}}$ |
| partial | parametric | `1/sqrt(b*x - c*x**2 + (-b**2 + 4*c)/(4*c))` | $\frac{1}{\sqrt{b x - c x^{2} + \frac{- b^{2} + 4 c}{4 c}}}$ |
| partial | parametric | `1/sqrt(b*x - c*x**2 + (-b**2 + c)/(4*c))` | $\frac{1}{\sqrt{b x - c x^{2} + \frac{- b^{2} + c}{4 c}}}$ |
| SOLVED-both | concrete | `(x**2 + 3*x + 2)**(-3/2)` | $\frac{1}{\left(x^{2} + 3 x + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(4*x**2 - 24*x + 27)**(-3/2)` | $\frac{1}{\left(4 x^{2} - 24 x + 27\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x/(-x**2 - 4*x + 5)**(3/2)` | $\frac{x}{\left(- x^{2} - 4 x + 5\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(-x**2 - 4*x + 5)**(-5/2)` | $\frac{1}{\left(- x^{2} - 4 x + 5\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3*sqrt(b*x + c*x**2)` | $x^{3} \sqrt{b x + c x^{2}}$ |
| partial | parametric | `x**2*sqrt(b*x + c*x**2)` | $x^{2} \sqrt{b x + c x^{2}}$ |
| partial | parametric | `x*sqrt(b*x + c*x**2)` | $x \sqrt{b x + c x^{2}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)` | $\sqrt{b x + c x^{2}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/x` | $\frac{\sqrt{b x + c x^{2}}}{x}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/x**2` | $\frac{\sqrt{b x + c x^{2}}}{x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(b*x + c*x**2)/x**3` | $\frac{\sqrt{b x + c x^{2}}}{x^{3}}$ |
| **SOLVED-NEW** | parametric | `sqrt(b*x + c*x**2)/x**4` | $\frac{\sqrt{b x + c x^{2}}}{x^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(b*x + c*x**2)/x**5` | $\frac{\sqrt{b x + c x^{2}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `sqrt(b*x + c*x**2)/x**6` | $\frac{\sqrt{b x + c x^{2}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `sqrt(b*x + c*x**2)/x**7` | $\frac{\sqrt{b x + c x^{2}}}{x^{7}}$ |
| partial | parametric | `x**2*(b*x + c*x**2)**(3/2)` | $x^{2} \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(b*x + c*x**2)**(3/2)` | $x \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)` | $\left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/x` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/x**2` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/x**3` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/x**4` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{4}}$ |
| **SOLVED-NEW** | parametric | `(b*x + c*x**2)**(3/2)/x**5` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `(b*x + c*x**2)**(3/2)/x**6` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `(b*x + c*x**2)**(3/2)/x**7` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(b*x + c*x**2)**(3/2)/x**8` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `(b*x + c*x**2)**(3/2)/x**9` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{9}}$ |
| partial | parametric | `x**2*(a*x + b*x**2)**(5/2)` | $x^{2} \left(a x + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x*(a*x + b*x**2)**(5/2)` | $x \left(a x + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a*x + b*x**2)**(5/2)` | $\left(a x + b x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a*x + b*x**2)**(5/2)/x` | $\frac{\left(a x + b x^{2}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(a*x + b*x**2)**(5/2)/x**2` | $\frac{\left(a x + b x^{2}\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(a*x + b*x**2)**(5/2)/x**3` | $\frac{\left(a x + b x^{2}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(a*x + b*x**2)**(5/2)/x**4` | $\frac{\left(a x + b x^{2}\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(a*x + b*x**2)**(5/2)/x**5` | $\frac{\left(a x + b x^{2}\right)^{\frac{5}{2}}}{x^{5}}$ |
| partial | parametric | `(a*x + b*x**2)**(5/2)/x**6` | $\frac{\left(a x + b x^{2}\right)^{\frac{5}{2}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `(a*x + b*x**2)**(5/2)/x**7` | $\frac{\left(a x + b x^{2}\right)^{\frac{5}{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(a*x + b*x**2)**(5/2)/x**8` | $\frac{\left(a x + b x^{2}\right)^{\frac{5}{2}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `(a*x + b*x**2)**(5/2)/x**9` | $\frac{\left(a x + b x^{2}\right)^{\frac{5}{2}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `(a*x + b*x**2)**(5/2)/x**10` | $\frac{\left(a x + b x^{2}\right)^{\frac{5}{2}}}{x^{10}}$ |
| **SOLVED-NEW** | parametric | `(a*x + b*x**2)**(5/2)/x**11` | $\frac{\left(a x + b x^{2}\right)^{\frac{5}{2}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `(a*x + b*x**2)**(5/2)/x**12` | $\frac{\left(a x + b x^{2}\right)^{\frac{5}{2}}}{x^{12}}$ |
| partial | concrete | `x*sqrt(-x**2 + 2*x)` | $x \sqrt{- x^{2} + 2 x}$ |
| partial | concrete | `x*sqrt(-4*x**2 + 3*x)` | $x \sqrt{- 4 x^{2} + 3 x}$ |
| partial | concrete | `x*sqrt(x**2 + x)` | $x \sqrt{x^{2} + x}$ |
| partial | parametric | `x**4/sqrt(b*x + c*x**2)` | $\frac{x^{4}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `x**3/sqrt(b*x + c*x**2)` | $\frac{x^{3}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `x**2/sqrt(b*x + c*x**2)` | $\frac{x^{2}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `x/sqrt(b*x + c*x**2)` | $\frac{x}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/sqrt(b*x + c*x**2)` | $\frac{1}{\sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x*sqrt(b*x + c*x**2))` | $\frac{1}{x \sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**2*sqrt(b*x + c*x**2))` | $\frac{1}{x^{2} \sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**3*sqrt(b*x + c*x**2))` | $\frac{1}{x^{3} \sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**4*sqrt(b*x + c*x**2))` | $\frac{1}{x^{4} \sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**5*sqrt(b*x + c*x**2))` | $\frac{1}{x^{5} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `x**4/(b*x + c*x**2)**(3/2)` | $\frac{x^{4}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/(b*x + c*x**2)**(3/2)` | $\frac{x^{3}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(b*x + c*x**2)**(3/2)` | $\frac{x^{2}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x/(b*x + c*x**2)**(3/2)` | $\frac{x}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)**(-3/2)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x*(b*x + c*x**2)**(3/2))` | $\frac{1}{x \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**2*(b*x + c*x**2)**(3/2))` | $\frac{1}{x^{2} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**3*(b*x + c*x**2)**(3/2))` | $\frac{1}{x^{3} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**6/(a*x + b*x**2)**(5/2)` | $\frac{x^{6}}{\left(a x + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**5/(a*x + b*x**2)**(5/2)` | $\frac{x^{5}}{\left(a x + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4/(a*x + b*x**2)**(5/2)` | $\frac{x^{4}}{\left(a x + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**3/(a*x + b*x**2)**(5/2)` | $\frac{x^{3}}{\left(a x + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2/(a*x + b*x**2)**(5/2)` | $\frac{x^{2}}{\left(a x + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x/(a*x + b*x**2)**(5/2)` | $\frac{x}{\left(a x + b x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a*x + b*x**2)**(-5/2)` | $\frac{1}{\left(a x + b x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x*(a*x + b*x**2)**(5/2))` | $\frac{1}{x \left(a x + b x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**2*(a*x + b*x**2)**(5/2))` | $\frac{1}{x^{2} \left(a x + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x/sqrt(-x**2 + 4*x)` | $\frac{x}{\sqrt{- x^{2} + 4 x}}$ |
| partial | concrete | `x/sqrt(x**2 - 4*x)` | $\frac{x}{\sqrt{x^{2} - 4 x}}$ |
| partial | concrete | `x**2/sqrt(-x**2 + 2*x)` | $\frac{x^{2}}{\sqrt{- x^{2} + 2 x}}$ |
| partial | parametric | `x**(7/2)*sqrt(b*x + c*x**2)` | $x^{\frac{7}{2}} \sqrt{b x + c x^{2}}$ |
| partial | parametric | `x**(5/2)*sqrt(b*x + c*x**2)` | $x^{\frac{5}{2}} \sqrt{b x + c x^{2}}$ |
| partial | parametric | `x**(3/2)*sqrt(b*x + c*x**2)` | $x^{\frac{3}{2}} \sqrt{b x + c x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(x)*sqrt(b*x + c*x**2)` | $\sqrt{x} \sqrt{b x + c x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(b*x + c*x**2)/sqrt(x)` | $\frac{\sqrt{b x + c x^{2}}}{\sqrt{x}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/x**(3/2)` | $\frac{\sqrt{b x + c x^{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/x**(5/2)` | $\frac{\sqrt{b x + c x^{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/x**(7/2)` | $\frac{\sqrt{b x + c x^{2}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/x**(9/2)` | $\frac{\sqrt{b x + c x^{2}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/x**(11/2)` | $\frac{\sqrt{b x + c x^{2}}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `x**(7/2)*(b*x + c*x**2)**(3/2)` | $x^{\frac{7}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(5/2)*(b*x + c*x**2)**(3/2)` | $x^{\frac{5}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(3/2)*(b*x + c*x**2)**(3/2)` | $x^{\frac{3}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(x)*(b*x + c*x**2)**(3/2)` | $\sqrt{x} \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `(b*x + c*x**2)**(3/2)/sqrt(x)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| **SOLVED-NEW** | parametric | `(b*x + c*x**2)**(3/2)/x**(3/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/x**(5/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/x**(7/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/x**(9/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/x**(11/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/x**(13/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{13}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/x**(15/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{15}{2}}}$ |
| partial | parametric | `x**(7/2)/sqrt(b*x + c*x**2)` | $\frac{x^{\frac{7}{2}}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `x**(5/2)/sqrt(b*x + c*x**2)` | $\frac{x^{\frac{5}{2}}}{\sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(3/2)/sqrt(b*x + c*x**2)` | $\frac{x^{\frac{3}{2}}}{\sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(x)/sqrt(b*x + c*x**2)` | $\frac{\sqrt{x}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(b*x + c*x**2))` | $\frac{1}{\sqrt{x} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/(x**(3/2)*sqrt(b*x + c*x**2))` | $\frac{1}{x^{\frac{3}{2}} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/(x**(5/2)*sqrt(b*x + c*x**2))` | $\frac{1}{x^{\frac{5}{2}} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/(x**(7/2)*sqrt(b*x + c*x**2))` | $\frac{1}{x^{\frac{7}{2}} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `x**(13/2)/(b*x + c*x**2)**(3/2)` | $\frac{x^{\frac{13}{2}}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(11/2)/(b*x + c*x**2)**(3/2)` | $\frac{x^{\frac{11}{2}}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(9/2)/(b*x + c*x**2)**(3/2)` | $\frac{x^{\frac{9}{2}}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(7/2)/(b*x + c*x**2)**(3/2)` | $\frac{x^{\frac{7}{2}}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(5/2)/(b*x + c*x**2)**(3/2)` | $\frac{x^{\frac{5}{2}}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(3/2)/(b*x + c*x**2)**(3/2)` | $\frac{x^{\frac{3}{2}}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)/(b*x + c*x**2)**(3/2)` | $\frac{\sqrt{x}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(x)*(b*x + c*x**2)**(3/2))` | $\frac{1}{\sqrt{x} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**(3/2)*(b*x + c*x**2)**(3/2))` | $\frac{1}{x^{\frac{3}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**(5/2)*(b*x + c*x**2)**(3/2))` | $\frac{1}{x^{\frac{5}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**4*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x^{4} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `x**3*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x^{3} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `x**2*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x^{2} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `x*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/x` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**2` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**3` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{3}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**4` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**5` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**6` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{6}}$ |
| SOLVED-both | parametric | `x**5*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $x^{5} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**4*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $x^{4} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $x^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $x \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**2` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**3` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**4` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{4}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**5` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**6` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**7` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**8` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**9` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{9}}$ |
| SOLVED-both | parametric | `x**5*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x^{5} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**4*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x^{4} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**2` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**3` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**4` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**5` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{5}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**6` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**7` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**8` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**9` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**10` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{10}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**11` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**12` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{12}}$ |
| SOLVED-both | parametric | `x**4/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x^{4}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `x**3/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x^{3}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `x**2/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x^{2}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `x/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `1/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{1}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/(x*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{x \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/(x**2*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{x^{2} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/(x**3*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{x^{3} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/(x**4*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{x^{4} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `x**4/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{x^{4}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**3/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{x^{3}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**2/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{x^{2}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{x}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(-3/2)` | $\frac{1}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{1}{x \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{1}{x^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{1}{x^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**6/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{6}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**5/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{5}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**4/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{4}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**3/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{3}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{2}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(-5/2)` | $\frac{1}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{1}{x \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{1}{x^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{1}{x^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `x*(4*x**2 + 12*x + 9)**(5/2)` | $x \left(4 x^{2} + 12 x + 9\right)^{\frac{5}{2}}$ |
| SOLVED-both | concrete | `x*(4*x**2 + 12*x + 9)**(3/2)` | $x \left(4 x^{2} + 12 x + 9\right)^{\frac{3}{2}}$ |
| SOLVED-both | concrete | `x*sqrt(4*x**2 + 12*x + 9)` | $x \sqrt{4 x^{2} + 12 x + 9}$ |
| SOLVED-both | concrete | `x/sqrt(4*x**2 + 12*x + 9)` | $\frac{x}{\sqrt{4 x^{2} + 12 x + 9}}$ |
| SOLVED-both | concrete | `x/(4*x**2 + 12*x + 9)**(3/2)` | $\frac{x}{\left(4 x^{2} + 12 x + 9\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x/(4*x**2 + 12*x + 9)**(5/2)` | $\frac{x}{\left(4 x^{2} + 12 x + 9\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `x/(4*x**2 + 12*x + 9)**(7/2)` | $\frac{x}{\left(4 x^{2} + 12 x + 9\right)^{\frac{7}{2}}}$ |
| SOLVED-both | concrete | `x/sqrt(9*x**2 + 12*x + 4)` | $\frac{x}{\sqrt{9 x^{2} + 12 x + 4}}$ |
| SOLVED-both | concrete | `x/sqrt(9*x**2 - 12*x + 4)` | $\frac{x}{\sqrt{9 x^{2} - 12 x + 4}}$ |
| SOLVED-both | concrete | `x/sqrt(-9*x**2 + 12*x - 4)` | $\frac{x}{\sqrt{- 9 x^{2} + 12 x - 4}}$ |
| SOLVED-both | concrete | `x/sqrt(-9*x**2 - 12*x - 4)` | $\frac{x}{\sqrt{- 9 x^{2} - 12 x - 4}}$ |
| partial | parametric | `(d + e*x)**3*sqrt(b*x + c*x**2)` | $\left(d + e x\right)^{3} \sqrt{b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)**2*sqrt(b*x + c*x**2)` | $\left(d + e x\right)^{2} \sqrt{b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)*sqrt(b*x + c*x**2)` | $\left(d + e x\right) \sqrt{b x + c x^{2}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)` | $\sqrt{b x + c x^{2}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/(d + e*x)` | $\frac{\sqrt{b x + c x^{2}}}{d + e x}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/(d + e*x)**2` | $\frac{\sqrt{b x + c x^{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/(d + e*x)**3` | $\frac{\sqrt{b x + c x^{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/(d + e*x)**4` | $\frac{\sqrt{b x + c x^{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/(d + e*x)**5` | $\frac{\sqrt{b x + c x^{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/(d + e*x)**6` | $\frac{\sqrt{b x + c x^{2}}}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(d + e*x)**3*(b*x + c*x**2)**(3/2)` | $\left(d + e x\right)^{3} \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)**2*(b*x + c*x**2)**(3/2)` | $\left(d + e x\right)^{2} \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)*(b*x + c*x**2)**(3/2)` | $\left(d + e x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)` | $\left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/(d + e*x)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/(d + e*x)**2` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/(d + e*x)**3` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(d + e*x)**3*(b*x + c*x**2)**(5/2)` | $\left(d + e x\right)^{3} \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)**2*(b*x + c*x**2)**(5/2)` | $\left(d + e x\right)^{2} \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)*(b*x + c*x**2)**(5/2)` | $\left(d + e x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(5/2)` | $\left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(5/2)/(d + e*x)` | $\frac{\left(b x + c x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(b*x + c*x**2)**(5/2)/(d + e*x)**2` | $\frac{\left(b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(5/2)/(d + e*x)**3` | $\frac{\left(b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | concrete | `sqrt(x**2 + 2*x)/(x + 1)` | $\frac{\sqrt{x^{2} + 2 x}}{x + 1}$ |
| partial | concrete | `(-x**2 + 2*x)**(3/2)/(2 - 2*x)` | $\frac{\left(- x^{2} + 2 x\right)^{\frac{3}{2}}}{2 - 2 x}$ |
| partial | concrete | `sqrt(-x**2 + 2*x)/(2 - 2*x)` | $\frac{\sqrt{- x^{2} + 2 x}}{2 - 2 x}$ |
| partial | concrete | `1/((2 - 2*x)*sqrt(-x**2 + 2*x))` | $\frac{1}{\left(2 - 2 x\right) \sqrt{- x^{2} + 2 x}}$ |
| partial | concrete | `1/((2 - 2*x)*(-x**2 + 2*x)**(3/2))` | $\frac{1}{\left(2 - 2 x\right) \left(- x^{2} + 2 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((2 - 2*x)*(-x**2 + 2*x)**(5/2))` | $\frac{1}{\left(2 - 2 x\right) \left(- x^{2} + 2 x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**3/sqrt(b*x + c*x**2)` | $\frac{\left(d + e x\right)^{3}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**2/sqrt(b*x + c*x**2)` | $\frac{\left(d + e x\right)^{2}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)/sqrt(b*x + c*x**2)` | $\frac{d + e x}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/sqrt(b*x + c*x**2)` | $\frac{1}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)*sqrt(b*x + c*x**2))` | $\frac{1}{\left(d + e x\right) \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**2*sqrt(b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{2} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**3*sqrt(b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{3} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**3/(b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{3}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**2/(b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{2}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(b*x + c*x**2)**(3/2)` | $\frac{d + e x}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)**(-3/2)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)*(b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**2*(b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**3*(b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{3} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**4/(b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{4}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/(b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{3}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/(b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{2}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(b*x + c*x**2)**(5/2)` | $\frac{d + e x}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)**(-5/2)` | $\frac{1}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)*(b*x + c*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**2*(b*x + c*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | concrete | `1/((x + 2)*sqrt(x**2 + 2*x))` | $\frac{1}{\left(x + 2\right) \sqrt{x^{2} + 2 x}}$ |
| SOLVED-both | parametric | `(d + e*x)**(7/2)*(b*x + c*x**2)` | $\left(d + e x\right)^{\frac{7}{2}} \left(b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(d + e*x)**(5/2)*(b*x + c*x**2)` | $\left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(d + e*x)**(3/2)*(b*x + c*x**2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `sqrt(d + e*x)*(b*x + c*x**2)` | $\sqrt{d + e x} \left(b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(b*x + c*x**2)/sqrt(d + e*x)` | $\frac{b x + c x^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)/(d + e*x)**(3/2)` | $\frac{b x + c x^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)/(d + e*x)**(5/2)` | $\frac{b x + c x^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)/(d + e*x)**(7/2)` | $\frac{b x + c x^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**(7/2)*(b*x + c*x**2)**2` | $\left(d + e x\right)^{\frac{7}{2}} \left(b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(d + e*x)**(5/2)*(b*x + c*x**2)**2` | $\left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(d + e*x)**(3/2)*(b*x + c*x**2)**2` | $\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(d + e*x)*(b*x + c*x**2)**2` | $\sqrt{d + e x} \left(b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)**2/sqrt(d + e*x)` | $\frac{\left(b x + c x^{2}\right)^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)**2/(d + e*x)**(3/2)` | $\frac{\left(b x + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)**2/(d + e*x)**(5/2)` | $\frac{\left(b x + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)**2/(d + e*x)**(7/2)` | $\frac{\left(b x + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**(7/2)*(b*x + c*x**2)**3` | $\left(d + e x\right)^{\frac{7}{2}} \left(b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(d + e*x)**(5/2)*(b*x + c*x**2)**3` | $\left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(d + e*x)**(3/2)*(b*x + c*x**2)**3` | $\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(d + e*x)*(b*x + c*x**2)**3` | $\sqrt{d + e x} \left(b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)**3/sqrt(d + e*x)` | $\frac{\left(b x + c x^{2}\right)^{3}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)**3/(d + e*x)**(3/2)` | $\frac{\left(b x + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)**3/(d + e*x)**(5/2)` | $\frac{\left(b x + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b*x + c*x**2)**3/(d + e*x)**(7/2)` | $\frac{\left(b x + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{b x + c x^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(b*x + c*x**2)` | $\frac{\sqrt{d + e x}}{b x + c x^{2}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(b*x + c*x**2))` | $\frac{1}{\sqrt{d + e x} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*(b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `(d + e*x)**(9/2)/(b*x + c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(b*x + c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(b*x + c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(b*x + c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(b*x + c*x**2)**2` | $\frac{\sqrt{d + e x}}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(b*x + c*x**2)**2)` | $\frac{1}{\sqrt{d + e x} \left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(b*x + c*x**2)**2)` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(b*x + c*x**2)**2)` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*(b*x + c*x**2)**2)` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(9/2)/(b*x + c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(b*x + c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(b*x + c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(b*x + c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(d + e*x)/(b*x + c*x**2)**3` | $\frac{\sqrt{d + e x}}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(b*x + c*x**2)**3)` | $\frac{1}{\sqrt{d + e x} \left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(b*x + c*x**2)**3)` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(b*x + c*x**2)**3)` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(3/2)*sqrt(b*x + c*x**2)` | $\left(d + e x\right)^{\frac{3}{2}} \sqrt{b x + c x^{2}}$ |
| partial | parametric | `sqrt(d + e*x)*sqrt(b*x + c*x**2)` | $\sqrt{d + e x} \sqrt{b x + c x^{2}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/sqrt(d + e*x)` | $\frac{\sqrt{b x + c x^{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/(d + e*x)**(3/2)` | $\frac{\sqrt{b x + c x^{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/(d + e*x)**(5/2)` | $\frac{\sqrt{b x + c x^{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(b*x + c*x**2)/(d + e*x)**(7/2)` | $\frac{\sqrt{b x + c x^{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(b*x + c*x**2)**(3/2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(d + e*x)*(b*x + c*x**2)**(3/2)` | $\sqrt{d + e x} \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/sqrt(d + e*x)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(3/2)/(d + e*x)**(9/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)*(b*x + c*x**2)**(5/2)` | $\sqrt{d + e x} \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(b*x + c*x**2)**(5/2)/sqrt(d + e*x)` | $\frac{\left(b x + c x^{2}\right)^{\frac{5}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(b*x + c*x**2)**(5/2)/(d + e*x)**(3/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(5/2)/(d + e*x)**(7/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(5/2)/(d + e*x)**(9/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(b*x + c*x**2)**(5/2)/(d + e*x)**(11/2)` | $\frac{\left(b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/sqrt(b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/sqrt(b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/sqrt(b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/sqrt(b*x + c*x**2)` | $\frac{\sqrt{d + e x}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*sqrt(b*x + c*x**2))` | $\frac{1}{\sqrt{d + e x} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*sqrt(b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*sqrt(b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*sqrt(b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/(b*x + c*x**2)**(3/2)` | $\frac{\sqrt{d + e x}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(b*x + c*x**2)**(3/2))` | $\frac{1}{\sqrt{d + e x} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(9/2)/(b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/(b*x + c*x**2)**(5/2)` | $\frac{\sqrt{d + e x}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(b*x + c*x**2)**(5/2))` | $\frac{1}{\sqrt{d + e x} \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(b*x + c*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/sqrt(-3*x**2 + 2*x)` | $\frac{\sqrt{d + e x}}{\sqrt{- 3 x^{2} + 2 x}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*sqrt(-3*x**2 + 2*x))` | $\frac{1}{\sqrt{d + e x} \sqrt{- 3 x^{2} + 2 x}}$ |
| partial | parametric | `sqrt(d + e*x)/sqrt(-3*x**2 - 2*x)` | $\frac{\sqrt{d + e x}}{\sqrt{- 3 x^{2} - 2 x}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*sqrt(-3*x**2 - 2*x))` | $\frac{1}{\sqrt{d + e x} \sqrt{- 3 x^{2} - 2 x}}$ |
| partial | concrete | `sqrt(1 - x)/(sqrt(-x)*sqrt(x + 1))` | $\frac{\sqrt{1 - x}}{\sqrt{- x} \sqrt{x + 1}}$ |
| partial | concrete | `sqrt(1 - x)/sqrt(-x**2 - x)` | $\frac{\sqrt{1 - x}}{\sqrt{- x^{2} - x}}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x)**4` | $\sqrt{a + c x^{2}} \left(d + e x\right)^{4}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x)**3` | $\sqrt{a + c x^{2}} \left(d + e x\right)^{3}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x)**2` | $\sqrt{a + c x^{2}} \left(d + e x\right)^{2}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x)` | $\sqrt{a + c x^{2}} \left(d + e x\right)$ |
| partial | parametric | `sqrt(a + c*x**2)/(d + e*x)` | $\frac{\sqrt{a + c x^{2}}}{d + e x}$ |
| partial | parametric | `sqrt(a + c*x**2)/(d + e*x)**2` | $\frac{\sqrt{a + c x^{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `sqrt(a + c*x**2)/(d + e*x)**3` | $\frac{\sqrt{a + c x^{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `sqrt(a + c*x**2)/(d + e*x)**4` | $\frac{\sqrt{a + c x^{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `sqrt(a + c*x**2)/(d + e*x)**5` | $\frac{\sqrt{a + c x^{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x)**4` | $\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)^{4}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x)**3` | $\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)^{3}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x)**2` | $\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)^{2}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x)` | $\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(d + e*x)` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(d + e*x)**2` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(d + e*x)**3` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(d + e*x)**4` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(d + e*x)**5` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(d + e*x)**6` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(d + e*x)**7` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{7}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)*(d + e*x)**4` | $\left(a + c x^{2}\right)^{\frac{5}{2}} \left(d + e x\right)^{4}$ |
| partial | parametric | `(a + c*x**2)**(5/2)*(d + e*x)**3` | $\left(a + c x^{2}\right)^{\frac{5}{2}} \left(d + e x\right)^{3}$ |
| partial | parametric | `(a + c*x**2)**(5/2)*(d + e*x)**2` | $\left(a + c x^{2}\right)^{\frac{5}{2}} \left(d + e x\right)^{2}$ |
| partial | parametric | `(a + c*x**2)**(5/2)*(d + e*x)` | $\left(a + c x^{2}\right)^{\frac{5}{2}} \left(d + e x\right)$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**2` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**3` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**4` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**5` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**6` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**7` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{7}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**8` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{8}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**9` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{9}}$ |
| partial | concrete | `sqrt(x**2 + 2)/(4*x + 1)` | $\frac{\sqrt{x^{2} + 2}}{4 x + 1}$ |
| partial | concrete | `sqrt(4*x**2 + 2)/(4*x + 5)` | $\frac{\sqrt{4 x^{2} + 2}}{4 x + 5}$ |
| partial | concrete | `(3*x + 2)*sqrt(7*x**2 - 5)` | $\left(3 x + 2\right) \sqrt{7 x^{2} - 5}$ |
| partial | parametric | `(d + e*x)**4/sqrt(a + c*x**2)` | $\frac{\left(d + e x\right)^{4}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**3/sqrt(a + c*x**2)` | $\frac{\left(d + e x\right)^{3}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**2/sqrt(a + c*x**2)` | $\frac{\left(d + e x\right)^{2}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(d + e*x)/sqrt(a + c*x**2)` | $\frac{d + e x}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `1/(sqrt(a + c*x**2)*(d + e*x))` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right)}$ |
| partial | parametric | `1/(sqrt(a + c*x**2)*(d + e*x)**2)` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `1/(sqrt(a + c*x**2)*(d + e*x)**3)` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right)^{3}}$ |
| partial | parametric | `1/(sqrt(a + c*x**2)*(d + e*x)**4)` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right)^{4}}$ |
| partial | parametric | `(d + e*x)**4/(a + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{4}}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**3/(a + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{3}}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**2/(a + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{2}}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(a + c*x**2)**(3/2)` | $\frac{d + e x}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + c*x**2)**(3/2)*(d + e*x))` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)}$ |
| partial | parametric | `1/((a + c*x**2)**(3/2)*(d + e*x)**2)` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `1/((a + c*x**2)**(3/2)*(d + e*x)**3)` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)^{3}}$ |
| partial | parametric | `1/((a + c*x**2)**(3/2)*(d + e*x)**4)` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)^{4}}$ |
| partial | parametric | `(d + e*x)**5/(a + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{5}}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**4/(a + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{4}}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/(a + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{3}}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/(a + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{2}}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(a + c*x**2)**(5/2)` | $\frac{d + e x}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((a + c*x**2)**(5/2)*(d + e*x))` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{5}{2}} \left(d + e x\right)}$ |
| partial | parametric | `1/((a + c*x**2)**(5/2)*(d + e*x)**2)` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{5}{2}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `1/((a + c*x**2)**(5/2)*(d + e*x)**3)` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{5}{2}} \left(d + e x\right)^{3}}$ |
| partial | concrete | `(x + 3)/sqrt(1 - x**2)` | $\frac{x + 3}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `(x + 1)/sqrt(4 - x**2)` | $\frac{x + 1}{\sqrt{4 - x^{2}}}$ |
| partial | concrete | `(x + 2)/sqrt(x**2 + 9)` | $\frac{x + 2}{\sqrt{x^{2} + 9}}$ |
| partial | parametric | `(a + b*x)**2/sqrt(1 - x**2)` | $\frac{\left(a + b x\right)^{2}}{\sqrt{1 - x^{2}}}$ |
| partial | parametric | `(a + b*x)**2/sqrt(x**2 + 1)` | $\frac{\left(a + b x\right)^{2}}{\sqrt{x^{2} + 1}}$ |
| SOLVED-both | concrete | `(3*x + 2)/(x**2 + 4)**(3/2)` | $\frac{3 x + 2}{\left(x^{2} + 4\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)*(d + e*x)**(5/2)` | $\left(a + c x^{2}\right) \left(d + e x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + c*x**2)*(d + e*x)**(3/2)` | $\left(a + c x^{2}\right) \left(d + e x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + c*x**2)*sqrt(d + e*x)` | $\left(a + c x^{2}\right) \sqrt{d + e x}$ |
| SOLVED-both | parametric | `(a + c*x**2)/sqrt(d + e*x)` | $\frac{a + c x^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a + c*x**2)/(d + e*x)**(3/2)` | $\frac{a + c x^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)/(d + e*x)**(5/2)` | $\frac{a + c x^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)/(d + e*x)**(7/2)` | $\frac{a + c x^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**2*(d + e*x)**(5/2)` | $\left(a + c x^{2}\right)^{2} \left(d + e x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**2*(d + e*x)**(3/2)` | $\left(a + c x^{2}\right)^{2} \left(d + e x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**2*sqrt(d + e*x)` | $\left(a + c x^{2}\right)^{2} \sqrt{d + e x}$ |
| SOLVED-both | parametric | `(a + c*x**2)**2/sqrt(d + e*x)` | $\frac{\left(a + c x^{2}\right)^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**2/(d + e*x)**(3/2)` | $\frac{\left(a + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**2/(d + e*x)**(5/2)` | $\frac{\left(a + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**2/(d + e*x)**(7/2)` | $\frac{\left(a + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**3*(d + e*x)**(5/2)` | $\left(a + c x^{2}\right)^{3} \left(d + e x\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**3*(d + e*x)**(3/2)` | $\left(a + c x^{2}\right)^{3} \left(d + e x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**3*sqrt(d + e*x)` | $\left(a + c x^{2}\right)^{3} \sqrt{d + e x}$ |
| SOLVED-both | parametric | `(a + c*x**2)**3/sqrt(d + e*x)` | $\frac{\left(a + c x^{2}\right)^{3}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**3/(d + e*x)**(3/2)` | $\frac{\left(a + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**3/(d + e*x)**(5/2)` | $\frac{\left(a + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)**3/(d + e*x)**(7/2)` | $\frac{\left(a + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a - c*x**2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{a - c x^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a - c*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{a - c x^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(a - c*x**2)` | $\frac{\sqrt{d + e x}}{a - c x^{2}}$ |
| partial | parametric | `1/((a - c*x**2)*sqrt(d + e*x))` | $\frac{1}{\left(a - c x^{2}\right) \sqrt{d + e x}}$ |
| partial | parametric | `1/((a - c*x**2)*(d + e*x)**(3/2))` | $\frac{1}{\left(a - c x^{2}\right) \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a - c*x**2)*(d + e*x)**(5/2))` | $\frac{1}{\left(a - c x^{2}\right) \left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{a + c x^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{a + c x^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(a + c*x**2)` | $\frac{\sqrt{d + e x}}{a + c x^{2}}$ |
| partial | parametric | `1/((a + c*x**2)*sqrt(d + e*x))` | $\frac{1}{\left(a + c x^{2}\right) \sqrt{d + e x}}$ |
| partial | parametric | `1/((a + c*x**2)*(d + e*x)**(3/2))` | $\frac{1}{\left(a + c x^{2}\right) \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + c*x**2)*(d + e*x)**(5/2))` | $\frac{1}{\left(a + c x^{2}\right) \left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a - c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a - c x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a - c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a - c x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a - c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a - c x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(a - c*x**2)**2` | $\frac{\sqrt{d + e x}}{\left(a - c x^{2}\right)^{2}}$ |
| partial | parametric | `1/((a - c*x**2)**2*sqrt(d + e*x))` | $\frac{1}{\left(a - c x^{2}\right)^{2} \sqrt{d + e x}}$ |
| partial | parametric | `1/((a - c*x**2)**2*(d + e*x)**(3/2))` | $\frac{1}{\left(a - c x^{2}\right)^{2} \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a - c*x**2)**2*(d + e*x)**(5/2))` | $\frac{1}{\left(a - c x^{2}\right)^{2} \left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a + c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a + c x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a + c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a + c x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a + c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a + c x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(a + c*x**2)**2` | $\frac{\sqrt{d + e x}}{\left(a + c x^{2}\right)^{2}}$ |
| partial | parametric | `1/((a + c*x**2)**2*sqrt(d + e*x))` | $\frac{1}{\left(a + c x^{2}\right)^{2} \sqrt{d + e x}}$ |
| partial | parametric | `1/((a + c*x**2)**2*(d + e*x)**(3/2))` | $\frac{1}{\left(a + c x^{2}\right)^{2} \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + c*x**2)**2*(d + e*x)**(5/2))` | $\frac{1}{\left(a + c x^{2}\right)^{2} \left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a - c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a - c x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a - c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a - c x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a - c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a - c x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(d + e*x)/(a - c*x**2)**3` | $\frac{\sqrt{d + e x}}{\left(a - c x^{2}\right)^{3}}$ |
| partial | parametric | `1/((a - c*x**2)**3*sqrt(d + e*x))` | $\frac{1}{\left(a - c x^{2}\right)^{3} \sqrt{d + e x}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a + c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a + c x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a + c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a + c x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a + c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a + c x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(d + e*x)/(a + c*x**2)**3` | $\frac{\sqrt{d + e x}}{\left(a + c x^{2}\right)^{3}}$ |
| partial | parametric | `1/((a + c*x**2)**3*sqrt(d + e*x))` | $\frac{1}{\left(a + c x^{2}\right)^{3} \sqrt{d + e x}}$ |
| partial | concrete | `sqrt(3*x + 2)/(x**2 + 1)` | $\frac{\sqrt{3 x + 2}}{x^{2} + 1}$ |
| partial | parametric | `sqrt(c + d*x)/(x**2 + 1)` | $\frac{\sqrt{c + d x}}{x^{2} + 1}$ |
| partial | concrete | `sqrt(3*x + 2)/(1 - x**2)` | $\frac{\sqrt{3 x + 2}}{1 - x^{2}}$ |
| partial | parametric | `sqrt(c + d*x)/(1 - x**2)` | $\frac{\sqrt{c + d x}}{1 - x^{2}}$ |
| partial | parametric | `sqrt(3*x + 2)/(a + b*x**2)` | $\frac{\sqrt{3 x + 2}}{a + b x^{2}}$ |
| partial | parametric | `sqrt(3*x + 2)/(a - b*x**2)` | $\frac{\sqrt{3 x + 2}}{a - b x^{2}}$ |
| partial | concrete | `sqrt(x + 1)/(x**2 + 1)` | $\frac{\sqrt{x + 1}}{x^{2} + 1}$ |
| partial | concrete | `1/(sqrt(x + 1)*(x**2 + 1))` | $\frac{1}{\sqrt{x + 1} \left(x^{2} + 1\right)}$ |
| partial | concrete | `sqrt(x - 1)/(x**2 + 1)**3` | $\frac{\sqrt{x - 1}}{\left(x^{2} + 1\right)^{3}}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x)**(3/2)` | $\sqrt{a + c x^{2}} \left(d + e x\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(a + c*x**2)*sqrt(d + e*x)` | $\sqrt{a + c x^{2}} \sqrt{d + e x}$ |
| partial | parametric | `sqrt(a + c*x**2)/sqrt(d + e*x)` | $\frac{\sqrt{a + c x^{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `sqrt(a + c*x**2)/(d + e*x)**(3/2)` | $\frac{\sqrt{a + c x^{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + c*x**2)/(d + e*x)**(5/2)` | $\frac{\sqrt{a + c x^{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(a + c*x**2)/(d + e*x)**(7/2)` | $\frac{\sqrt{a + c x^{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x)**(3/2)` | $\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*sqrt(d + e*x)` | $\left(a + c x^{2}\right)^{\frac{3}{2}} \sqrt{d + e x}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/sqrt(d + e*x)` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(d + e*x)**(9/2)` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)*sqrt(d + e*x)` | $\left(a + c x^{2}\right)^{\frac{5}{2}} \sqrt{d + e x}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/sqrt(d + e*x)` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**(3/2)` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**(7/2)` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**(9/2)` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)/(d + e*x)**(11/2)` | $\frac{\left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/sqrt(a + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/sqrt(a + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/sqrt(a + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/sqrt(a + c*x**2)` | $\frac{\sqrt{d + e x}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `1/(sqrt(a + c*x**2)*sqrt(d + e*x))` | $\frac{1}{\sqrt{a + c x^{2}} \sqrt{d + e x}}$ |
| partial | parametric | `1/(sqrt(a + c*x**2)*(d + e*x)**(3/2))` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(a + c*x**2)*(d + e*x)**(5/2))` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(a + c*x**2)*(d + e*x)**(7/2))` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/(a + c*x**2)**(3/2)` | $\frac{\sqrt{d + e x}}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + c*x**2)**(3/2)*sqrt(d + e*x))` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{3}{2}} \sqrt{d + e x}}$ |
| partial | parametric | `1/((a + c*x**2)**(3/2)*(d + e*x)**(3/2))` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + c*x**2)**(3/2)*(d + e*x)**(5/2))` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(9/2)/(a + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/(a + c*x**2)**(5/2)` | $\frac{\sqrt{d + e x}}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((a + c*x**2)**(5/2)*sqrt(d + e*x))` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{5}{2}} \sqrt{d + e x}}$ |
| partial | parametric | `1/((a + c*x**2)**(5/2)*(d + e*x)**(3/2))` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{5}{2}} \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)*(d**2 + 3*e**2*x**2)**(1/3))` | $\frac{1}{\left(d + e x\right) \sqrt[3]{d^{2} + 3 e^{2} x^{2}}}$ |
| partial | concrete | `(3*x + 2)**3/(27*x**2 + 4)**(1/3)` | $\frac{\left(3 x + 2\right)^{3}}{\sqrt[3]{27 x^{2} + 4}}$ |
| partial | concrete | `(3*x + 2)**2/(27*x**2 + 4)**(1/3)` | $\frac{\left(3 x + 2\right)^{2}}{\sqrt[3]{27 x^{2} + 4}}$ |
| partial | concrete | `(3*x + 2)/(27*x**2 + 4)**(1/3)` | $\frac{3 x + 2}{\sqrt[3]{27 x^{2} + 4}}$ |
| partial | concrete | `1/((3*x + 2)*(27*x**2 + 4)**(1/3))` | $\frac{1}{\left(3 x + 2\right) \sqrt[3]{27 x^{2} + 4}}$ |
| partial | concrete | `1/((3*x + 2)**2*(27*x**2 + 4)**(1/3))` | $\frac{1}{\left(3 x + 2\right)^{2} \sqrt[3]{27 x^{2} + 4}}$ |
| partial | concrete | `1/((3*x + 2)**3*(27*x**2 + 4)**(1/3))` | $\frac{1}{\left(3 x + 2\right)^{3} \sqrt[3]{27 x^{2} + 4}}$ |
| partial | concrete | `(3*I*x + 2)**3/(4 - 27*x**2)**(1/3)` | $\frac{\left(3 i x + 2\right)^{3}}{\sqrt[3]{4 - 27 x^{2}}}$ |
| partial | concrete | `(3*I*x + 2)**2/(4 - 27*x**2)**(1/3)` | $\frac{\left(3 i x + 2\right)^{2}}{\sqrt[3]{4 - 27 x^{2}}}$ |
| partial | concrete | `(3*I*x + 2)/(4 - 27*x**2)**(1/3)` | $\frac{3 i x + 2}{\sqrt[3]{4 - 27 x^{2}}}$ |
| partial | concrete | `1/((4 - 27*x**2)**(1/3)*(3*I*x + 2))` | $\frac{1}{\sqrt[3]{4 - 27 x^{2}} \left(3 i x + 2\right)}$ |
| partial | concrete | `1/((4 - 27*x**2)**(1/3)*(3*I*x + 2)**2)` | $\frac{1}{\sqrt[3]{4 - 27 x^{2}} \left(3 i x + 2\right)^{2}}$ |
| partial | concrete | `1/((4 - 27*x**2)**(1/3)*(3*I*x + 2)**3)` | $\frac{1}{\sqrt[3]{4 - 27 x^{2}} \left(3 i x + 2\right)^{3}}$ |
| partial | concrete | `1/((x + sqrt(3))*(x**2 + 1)**(1/3))` | $\frac{1}{\left(x + \sqrt{3}\right) \sqrt[3]{x^{2} + 1}}$ |
| partial | concrete | `1/((-x + sqrt(3))*(x**2 + 1)**(1/3))` | $\frac{1}{\left(- x + \sqrt{3}\right) \sqrt[3]{x^{2} + 1}}$ |
| partial | concrete | `1/((1 - x**2)**(1/3)*(3 - x))` | $\frac{1}{\sqrt[3]{1 - x^{2}} \left(3 - x\right)}$ |
| partial | concrete | `1/((1 - x**2)**(1/3)*(x + 3))` | $\frac{1}{\sqrt[3]{1 - x^{2}} \left(x + 3\right)}$ |
| partial | parametric | `1/((d + e*x)*(d**2 - 9*e**2*x**2)**(1/3))` | $\frac{1}{\left(d + e x\right) \sqrt[3]{d^{2} - 9 e^{2} x^{2}}}$ |
| partial | parametric | `1/((a + b*x)*(c + d*x**2)**(1/4))` | $\frac{1}{\left(a + b x\right) \sqrt[4]{c + d x^{2}}}$ |
| partial | parametric | `1/((a + b*x)*(c + d*x**2)**(3/4))` | $\frac{1}{\left(a + b x\right) \left(c + d x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((a + c*x**2)**(1/4)*(d + e*x)**(3/2))` | $\frac{1}{\sqrt[4]{a + c x^{2}} \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((x + 1)*(x**2 + 1)**(1/6))` | $\frac{1}{\left(x + 1\right) \sqrt[6]{x^{2} + 1}}$ |
| partial | parametric | `(a + b*x)**4*sqrt(a**2 - b**2*x**2)` | $\left(a + b x\right)^{4} \sqrt{a^{2} - b^{2} x^{2}}$ |
| partial | parametric | `(a + b*x)**3*sqrt(a**2 - b**2*x**2)` | $\left(a + b x\right)^{3} \sqrt{a^{2} - b^{2} x^{2}}$ |
| partial | parametric | `(a + b*x)**2*sqrt(a**2 - b**2*x**2)` | $\left(a + b x\right)^{2} \sqrt{a^{2} - b^{2} x^{2}}$ |
| partial | parametric | `(a + b*x)*sqrt(a**2 - b**2*x**2)` | $\left(a + b x\right) \sqrt{a^{2} - b^{2} x^{2}}$ |
| partial | parametric | `sqrt(a**2 - b**2*x**2)/(a + b*x)` | $\frac{\sqrt{a^{2} - b^{2} x^{2}}}{a + b x}$ |
| partial | parametric | `sqrt(a**2 - b**2*x**2)/(a + b*x)**2` | $\frac{\sqrt{a^{2} - b^{2} x^{2}}}{\left(a + b x\right)^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 - b**2*x**2)/(a + b*x)**3` | $\frac{\sqrt{a^{2} - b^{2} x^{2}}}{\left(a + b x\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 - b**2*x**2)/(a + b*x)**4` | $\frac{\sqrt{a^{2} - b^{2} x^{2}}}{\left(a + b x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 - b**2*x**2)/(a + b*x)**5` | $\frac{\sqrt{a^{2} - b^{2} x^{2}}}{\left(a + b x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 - b**2*x**2)/(a + b*x)**6` | $\frac{\sqrt{a^{2} - b^{2} x^{2}}}{\left(a + b x\right)^{6}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 - b**2*x**2)/(a + b*x)**7` | $\frac{\sqrt{a^{2} - b^{2} x^{2}}}{\left(a + b x\right)^{7}}$ |
| partial | parametric | `(a + b*x)**3*(a**2 - b**2*x**2)**(3/2)` | $\left(a + b x\right)^{3} \left(a^{2} - b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)**2*(a**2 - b**2*x**2)**(3/2)` | $\left(a + b x\right)^{2} \left(a^{2} - b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)*(a**2 - b**2*x**2)**(3/2)` | $\left(a + b x\right) \left(a^{2} - b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)` | $\frac{\left(a^{2} - b^{2} x^{2}\right)^{\frac{3}{2}}}{a + b x}$ |
| partial | parametric | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**2` | $\frac{\left(a^{2} - b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(a + b x\right)^{2}}$ |
| partial | parametric | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**3` | $\frac{\left(a^{2} - b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(a + b x\right)^{3}}$ |
| partial | parametric | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**4` | $\frac{\left(a^{2} - b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(a + b x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**5` | $\frac{\left(a^{2} - b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(a + b x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**6` | $\frac{\left(a^{2} - b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(a + b x\right)^{6}}$ |
| **SOLVED-NEW** | parametric | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**7` | $\frac{\left(a^{2} - b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(a + b x\right)^{7}}$ |
| **SOLVED-NEW** | parametric | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**8` | $\frac{\left(a^{2} - b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(a + b x\right)^{8}}$ |
| **SOLVED-NEW** | parametric | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**9` | $\frac{\left(a^{2} - b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(a + b x\right)^{9}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(7/2)` | $\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}$ |
| partial | parametric | `(d + e*x)**2*(d**2 - e**2*x**2)**(7/2)` | $\left(d + e x\right)^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}$ |
| partial | parametric | `(d + e*x)*(d**2 - e**2*x**2)**(7/2)` | $\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{d + e x}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**2` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**3` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**4` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**5` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**6` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**7` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{\left(d + e x\right)^{7}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**8` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{\left(d + e x\right)^{8}}$ |
| **SOLVED-NEW** | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**9` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{\left(d + e x\right)^{9}}$ |
| **SOLVED-NEW** | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**10` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{\left(d + e x\right)^{10}}$ |
| **SOLVED-NEW** | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**11` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{\left(d + e x\right)^{11}}$ |
| **SOLVED-NEW** | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**12` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{\left(d + e x\right)^{12}}$ |
| **SOLVED-NEW** | parametric | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**13` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}{\left(d + e x\right)^{13}}$ |
| partial | parametric | `sqrt(a**2 - b**2*x**2)/(a - b*x)` | $\frac{\sqrt{a^{2} - b^{2} x^{2}}}{a - b x}$ |
| partial | parametric | `(a + b*x)**2*sqrt(-a**2*c/b**2 + c*x**2)` | $\left(a + b x\right)^{2} \sqrt{- \frac{a^{2} c}{b^{2}} + c x^{2}}$ |
| partial | parametric | `(a + b*x)**3*sqrt(-a**2*c/b**2 + c*x**2)` | $\left(a + b x\right)^{3} \sqrt{- \frac{a^{2} c}{b^{2}} + c x^{2}}$ |
| partial | concrete | `(x + 1)*sqrt(x**2 - 1)` | $\left(x + 1\right) \sqrt{x^{2} - 1}$ |
| partial | concrete | `sqrt(1 - x**2)*(x + 1)` | $\sqrt{1 - x^{2}} \left(x + 1\right)$ |
| partial | concrete | `sqrt(1 - x**2)/(x + 1)` | $\frac{\sqrt{1 - x^{2}}}{x + 1}$ |
| partial | concrete | `(1 - x)*sqrt(1 - x**2)` | $\left(1 - x\right) \sqrt{1 - x^{2}}$ |
| partial | concrete | `sqrt(1 - x**2)/(1 - x)` | $\frac{\sqrt{1 - x^{2}}}{1 - x}$ |
| partial | concrete | `sqrt(1 - x**2)/(1 - x)**2` | $\frac{\sqrt{1 - x^{2}}}{\left(1 - x\right)^{2}}$ |
| **SOLVED-NEW** | concrete | `sqrt(1 - x**2)/(1 - x)**3` | $\frac{\sqrt{1 - x^{2}}}{\left(1 - x\right)^{3}}$ |
| partial | parametric | `(d + e*x)**5/sqrt(d**2 - e**2*x**2)` | $\frac{\left(d + e x\right)^{5}}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**4/sqrt(d**2 - e**2*x**2)` | $\frac{\left(d + e x\right)^{4}}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**3/sqrt(d**2 - e**2*x**2)` | $\frac{\left(d + e x\right)^{3}}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)/sqrt(d**2 - e**2*x**2)` | $\frac{d + e x}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)*sqrt(d**2 - e**2*x**2))` | $\frac{1}{\left(d + e x\right) \sqrt{d^{2} - e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**2*sqrt(d**2 - e**2*x**2))` | $\frac{1}{\left(d + e x\right)^{2} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | $\frac{1}{\left(d + e x\right)^{3} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**4*sqrt(d**2 - e**2*x**2))` | $\frac{1}{\left(d + e x\right)^{4} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**5*sqrt(d**2 - e**2*x**2))` | $\frac{1}{\left(d + e x\right)^{5} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**6/(d**2 - e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{6}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**5/(d**2 - e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{5}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**4/(d**2 - e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{4}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/(d**2 - e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/(d**2 - e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{2}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(d**2 - e**2*x**2)**(5/2)` | $\frac{d + e x}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**2*(d**2 - e**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**3*(d**2 - e**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**4*(d**2 - e**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{4} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**9/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{9}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**8/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{8}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**7/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{7}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**6/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{6}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**5/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{5}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**4/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{4}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{2}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | $\frac{d + e x}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)*(d**2 - e**2*x**2)**(7/2))` | $\frac{1}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**2*(d**2 - e**2*x**2)**(7/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**3*(d**2 - e**2*x**2)**(7/2))` | $\frac{1}{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**4*(d**2 - e**2*x**2)**(7/2))` | $\frac{1}{\left(d + e x\right)^{4} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**5*(d**2 - e**2*x**2)**(7/2))` | $\frac{1}{\left(d + e x\right)^{5} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | concrete | `(x + 1)/sqrt(1 - x**2)` | $\frac{x + 1}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `(1 - x)/sqrt(1 - x**2)` | $\frac{1 - x}{\sqrt{1 - x^{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)*sqrt(c*d**2 - c*e**2*x**2)` | $\left(d + e x\right)^{\frac{5}{2}} \sqrt{c d^{2} - c e^{2} x^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)*sqrt(c*d**2 - c*e**2*x**2)` | $\left(d + e x\right)^{\frac{3}{2}} \sqrt{c d^{2} - c e^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d + e*x)*sqrt(c*d**2 - c*e**2*x**2)` | $\sqrt{d + e x} \sqrt{c d^{2} - c e^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(c*d**2 - c*e**2*x**2)/sqrt(d + e*x)` | $\frac{\sqrt{c d^{2} - c e^{2} x^{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `sqrt(c*d**2 - c*e**2*x**2)/(d + e*x)**(3/2)` | $\frac{\sqrt{c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(c*d**2 - c*e**2*x**2)/(d + e*x)**(5/2)` | $\frac{\sqrt{c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(c*d**2 - c*e**2*x**2)/(d + e*x)**(7/2)` | $\frac{\sqrt{c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)*(c*d**2 - c*e**2*x**2)**(3/2)` | $\left(d + e x\right)^{\frac{5}{2}} \left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(c*d**2 - c*e**2*x**2)**(3/2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(d + e*x)*(c*d**2 - c*e**2*x**2)**(3/2)` | $\sqrt{d + e x} \left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `(c*d**2 - c*e**2*x**2)**(3/2)/sqrt(d + e*x)` | $\frac{\left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(9/2)` | $\frac{\left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(11/2)` | $\frac{\left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(13/2)` | $\frac{\left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/sqrt(c*d**2 - c*e**2*x**2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\sqrt{c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/sqrt(c*d**2 - c*e**2*x**2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\sqrt{c d^{2} - c e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)/sqrt(c*d**2 - c*e**2*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\sqrt{c d^{2} - c e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d + e*x)/sqrt(c*d**2 - c*e**2*x**2)` | $\frac{\sqrt{d + e x}}{\sqrt{c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*sqrt(c*d**2 - c*e**2*x**2))` | $\frac{1}{\sqrt{d + e x} \sqrt{c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*sqrt(c*d**2 - c*e**2*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*sqrt(c*d**2 - c*e**2*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**(9/2)/(c*d**2 - c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{\left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(c*d**2 - c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(5/2)/(c*d**2 - c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)/(c*d**2 - c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/(c*d**2 - c*e**2*x**2)**(3/2)` | $\frac{\sqrt{d + e x}}{\left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(c*d**2 - c*e**2*x**2)**(3/2))` | $\frac{1}{\sqrt{d + e x} \left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(c*d**2 - c*e**2*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(x - 1))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{x - 1}}$ |
| partial | parametric | `(e*x + 2)**(5/2)*sqrt(-3*e**2*x**2 + 12)` | $\left(e x + 2\right)^{\frac{5}{2}} \sqrt{- 3 e^{2} x^{2} + 12}$ |
| partial | parametric | `(e*x + 2)**(3/2)*sqrt(-3*e**2*x**2 + 12)` | $\left(e x + 2\right)^{\frac{3}{2}} \sqrt{- 3 e^{2} x^{2} + 12}$ |
| **SOLVED-NEW** | parametric | `sqrt(e*x + 2)*sqrt(-3*e**2*x**2 + 12)` | $\sqrt{e x + 2} \sqrt{- 3 e^{2} x^{2} + 12}$ |
| **SOLVED-NEW** | parametric | `sqrt(-3*e**2*x**2 + 12)/sqrt(e*x + 2)` | $\frac{\sqrt{- 3 e^{2} x^{2} + 12}}{\sqrt{e x + 2}}$ |
| partial | parametric | `sqrt(-3*e**2*x**2 + 12)/(e*x + 2)**(3/2)` | $\frac{\sqrt{- 3 e^{2} x^{2} + 12}}{\left(e x + 2\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(-3*e**2*x**2 + 12)/(e*x + 2)**(5/2)` | $\frac{\sqrt{- 3 e^{2} x^{2} + 12}}{\left(e x + 2\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(-3*e**2*x**2 + 12)/(e*x + 2)**(7/2)` | $\frac{\sqrt{- 3 e^{2} x^{2} + 12}}{\left(e x + 2\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(e*x + 2)**(5/2)*(-3*e**2*x**2 + 12)**(3/2)` | $\left(e x + 2\right)^{\frac{5}{2}} \left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}$ |
| partial | parametric | `(e*x + 2)**(3/2)*(-3*e**2*x**2 + 12)**(3/2)` | $\left(e x + 2\right)^{\frac{3}{2}} \left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(e*x + 2)*(-3*e**2*x**2 + 12)**(3/2)` | $\sqrt{e x + 2} \left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `(-3*e**2*x**2 + 12)**(3/2)/sqrt(e*x + 2)` | $\frac{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}{\sqrt{e x + 2}}$ |
| **SOLVED-NEW** | parametric | `(-3*e**2*x**2 + 12)**(3/2)/(e*x + 2)**(3/2)` | $\frac{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}{\left(e x + 2\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(-3*e**2*x**2 + 12)**(3/2)/(e*x + 2)**(5/2)` | $\frac{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}{\left(e x + 2\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(-3*e**2*x**2 + 12)**(3/2)/(e*x + 2)**(7/2)` | $\frac{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}{\left(e x + 2\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(-3*e**2*x**2 + 12)**(3/2)/(e*x + 2)**(9/2)` | $\frac{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}{\left(e x + 2\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(-3*e**2*x**2 + 12)**(3/2)/(e*x + 2)**(11/2)` | $\frac{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}{\left(e x + 2\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(-3*e**2*x**2 + 12)**(3/2)/(e*x + 2)**(13/2)` | $\frac{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}{\left(e x + 2\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(e*x + 2)**(7/2)/sqrt(-3*e**2*x**2 + 12)` | $\frac{\left(e x + 2\right)^{\frac{7}{2}}}{\sqrt{- 3 e^{2} x^{2} + 12}}$ |
| partial | parametric | `(e*x + 2)**(5/2)/sqrt(-3*e**2*x**2 + 12)` | $\frac{\left(e x + 2\right)^{\frac{5}{2}}}{\sqrt{- 3 e^{2} x^{2} + 12}}$ |
| **SOLVED-NEW** | parametric | `(e*x + 2)**(3/2)/sqrt(-3*e**2*x**2 + 12)` | $\frac{\left(e x + 2\right)^{\frac{3}{2}}}{\sqrt{- 3 e^{2} x^{2} + 12}}$ |
| **SOLVED-NEW** | parametric | `sqrt(e*x + 2)/sqrt(-3*e**2*x**2 + 12)` | $\frac{\sqrt{e x + 2}}{\sqrt{- 3 e^{2} x^{2} + 12}}$ |
| partial | parametric | `1/(sqrt(e*x + 2)*sqrt(-3*e**2*x**2 + 12))` | $\frac{1}{\sqrt{e x + 2} \sqrt{- 3 e^{2} x^{2} + 12}}$ |
| partial | parametric | `1/((e*x + 2)**(3/2)*sqrt(-3*e**2*x**2 + 12))` | $\frac{1}{\left(e x + 2\right)^{\frac{3}{2}} \sqrt{- 3 e^{2} x^{2} + 12}}$ |
| partial | parametric | `1/((e*x + 2)**(5/2)*sqrt(-3*e**2*x**2 + 12))` | $\frac{1}{\left(e x + 2\right)^{\frac{5}{2}} \sqrt{- 3 e^{2} x^{2} + 12}}$ |
| partial | parametric | `(e*x + 2)**(11/2)/(-3*e**2*x**2 + 12)**(3/2)` | $\frac{\left(e x + 2\right)^{\frac{11}{2}}}{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x + 2)**(9/2)/(-3*e**2*x**2 + 12)**(3/2)` | $\frac{\left(e x + 2\right)^{\frac{9}{2}}}{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x + 2)**(7/2)/(-3*e**2*x**2 + 12)**(3/2)` | $\frac{\left(e x + 2\right)^{\frac{7}{2}}}{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(e*x + 2)**(5/2)/(-3*e**2*x**2 + 12)**(3/2)` | $\frac{\left(e x + 2\right)^{\frac{5}{2}}}{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(e*x + 2)**(3/2)/(-3*e**2*x**2 + 12)**(3/2)` | $\frac{\left(e x + 2\right)^{\frac{3}{2}}}{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(e*x + 2)/(-3*e**2*x**2 + 12)**(3/2)` | $\frac{\sqrt{e x + 2}}{\left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(e*x + 2)*(-3*e**2*x**2 + 12)**(3/2))` | $\frac{1}{\sqrt{e x + 2} \left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((e*x + 2)**(3/2)*(-3*e**2*x**2 + 12)**(3/2))` | $\frac{1}{\left(e x + 2\right)^{\frac{3}{2}} \left(- 3 e^{2} x^{2} + 12\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(sqrt(1 - x)*(x + 1))` | $\frac{1}{\sqrt{1 - x} \left(x + 1\right)}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*sqrt(x + 1))` | $\frac{1}{\sqrt{1 - x^{2}} \sqrt{x + 1}}$ |
| partial | parametric | `1/(sqrt(-a*x + 1)*(a*x + 1))` | $\frac{1}{\sqrt{- a x + 1} \left(a x + 1\right)}$ |
| partial | parametric | `1/(sqrt(a*x + 1)*sqrt(-a**2*x**2 + 1))` | $\frac{1}{\sqrt{a x + 1} \sqrt{- a^{2} x^{2} + 1}}$ |
| partial | parametric | `sqrt(e*x + 2)*(-3*e**2*x**2 + 12)**(1/4)` | $\sqrt{e x + 2} \sqrt[4]{- 3 e^{2} x^{2} + 12}$ |
| partial | parametric | `(-3*e**2*x**2 + 12)**(1/4)/sqrt(e*x + 2)` | $\frac{\sqrt[4]{- 3 e^{2} x^{2} + 12}}{\sqrt{e x + 2}}$ |
| partial | parametric | `(-3*e**2*x**2 + 12)**(1/4)/(e*x + 2)**(3/2)` | $\frac{\sqrt[4]{- 3 e^{2} x^{2} + 12}}{\left(e x + 2\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(-3*e**2*x**2 + 12)**(1/4)/(e*x + 2)**(5/2)` | $\frac{\sqrt[4]{- 3 e^{2} x^{2} + 12}}{\left(e x + 2\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(-3*e**2*x**2 + 12)**(1/4)/(e*x + 2)**(7/2)` | $\frac{\sqrt[4]{- 3 e^{2} x^{2} + 12}}{\left(e x + 2\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `(-3*e**2*x**2 + 12)**(1/4)/(e*x + 2)**(9/2)` | $\frac{\sqrt[4]{- 3 e^{2} x^{2} + 12}}{\left(e x + 2\right)^{\frac{9}{2}}}$ |
| **SOLVED-NEW** | parametric | `(-3*e**2*x**2 + 12)**(1/4)/(e*x + 2)**(11/2)` | $\frac{\sqrt[4]{- 3 e^{2} x^{2} + 12}}{\left(e x + 2\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(e*x + 2)**(5/2)/(-3*e**2*x**2 + 12)**(1/4)` | $\frac{\left(e x + 2\right)^{\frac{5}{2}}}{\sqrt[4]{- 3 e^{2} x^{2} + 12}}$ |
| partial | parametric | `(e*x + 2)**(3/2)/(-3*e**2*x**2 + 12)**(1/4)` | $\frac{\left(e x + 2\right)^{\frac{3}{2}}}{\sqrt[4]{- 3 e^{2} x^{2} + 12}}$ |
| partial | parametric | `sqrt(e*x + 2)/(-3*e**2*x**2 + 12)**(1/4)` | $\frac{\sqrt{e x + 2}}{\sqrt[4]{- 3 e^{2} x^{2} + 12}}$ |
| partial | parametric | `1/(sqrt(e*x + 2)*(-3*e**2*x**2 + 12)**(1/4))` | $\frac{1}{\sqrt{e x + 2} \sqrt[4]{- 3 e^{2} x^{2} + 12}}$ |
| **SOLVED-NEW** | parametric | `1/((e*x + 2)**(3/2)*(-3*e**2*x**2 + 12)**(1/4))` | $\frac{1}{\left(e x + 2\right)^{\frac{3}{2}} \sqrt[4]{- 3 e^{2} x^{2} + 12}}$ |
| **SOLVED-NEW** | parametric | `1/((e*x + 2)**(5/2)*(-3*e**2*x**2 + 12)**(1/4))` | $\frac{1}{\left(e x + 2\right)^{\frac{5}{2}} \sqrt[4]{- 3 e^{2} x^{2} + 12}}$ |
| **SOLVED-NEW** | parametric | `1/((e*x + 2)**(7/2)*(-3*e**2*x**2 + 12)**(1/4))` | $\frac{1}{\left(e x + 2\right)^{\frac{7}{2}} \sqrt[4]{- 3 e^{2} x^{2} + 12}}$ |
| **SOLVED-NEW** | parametric | `1/((e*x + 2)**(9/2)*(-3*e**2*x**2 + 12)**(1/4))` | $\frac{1}{\left(e x + 2\right)^{\frac{9}{2}} \sqrt[4]{- 3 e^{2} x^{2} + 12}}$ |
| SOLVED-both | parametric | `(d + e*x)**3*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | $\left(d + e x\right)^{3} \sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}$ |
| SOLVED-both | parametric | `(d + e*x)**2*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | $\left(d + e x\right)^{2} \sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}$ |
| SOLVED-both | parametric | `(d + e*x)*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | $\left(d + e x\right) \sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}$ |
| SOLVED-both | parametric | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | $\sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}$ |
| SOLVED-both | parametric | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)/(d + e*x)` | $\frac{\sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}{d + e x}$ |
| **SOLVED-NEW** | parametric | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)/(d + e*x)**2` | $\frac{\sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}{\left(d + e x\right)^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)/(d + e*x)**3` | $\frac{\sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}{\left(d + e x\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)/(d + e*x)**4` | $\frac{\sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}{\left(d + e x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)/(d + e*x)**5` | $\frac{\sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}{\left(d + e x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)/(d + e*x)**6` | $\frac{\sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}{\left(d + e x\right)^{6}}$ |
| SOLVED-both | parametric | `(d + e*x)**3*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | $\left(d + e x\right)^{3} \left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)**2*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | $\left(d + e x\right)^{2} \left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | $\left(d + e x\right) \left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | $\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| SOLVED-both | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)**2` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{2}}$ |
| SOLVED-both | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)**3` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)**4` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)**5` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)**6` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{6}}$ |
| **SOLVED-NEW** | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)**7` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{7}}$ |
| SOLVED-both | parametric | `(d + e*x)**3*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | $\left(d + e x\right)^{3} \left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)**2*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | $\left(d + e x\right)^{2} \left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | $\left(d + e x\right) \left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | $\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| SOLVED-both | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**2` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| SOLVED-both | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**3` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{3}}$ |
| SOLVED-both | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**4` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| SOLVED-both | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**5` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**6` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{6}}$ |
| **SOLVED-NEW** | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**7` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{7}}$ |
| **SOLVED-NEW** | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**8` | $\frac{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{8}}$ |
| SOLVED-both | parametric | `(d + e*x)**4/sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | $\frac{\left(d + e x\right)^{4}}{\sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | $\frac{\left(d + e x\right)^{3}}{\sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | $\frac{\left(d + e x\right)^{2}}{\sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | $\frac{d + e x}{\sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}$ |
| SOLVED-both | parametric | `1/sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | $\frac{1}{\sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}$ |
| SOLVED-both | parametric | `1/((d + e*x)*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2))` | $\frac{1}{\left(d + e x\right) \sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**2*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2))` | $\frac{1}{\left(d + e x\right)^{2} \sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**3*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2))` | $\frac{1}{\left(d + e x\right)^{3} \sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**4*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2))` | $\frac{1}{\left(d + e x\right)^{4} \sqrt{c d^{2} + 2 c d e x + c e^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**4/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{4}}{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{3}}{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{2}}{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | $\frac{d + e x}{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(-3/2)` | $\frac{1}{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `1/((d + e*x)*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right) \left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**2*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**3*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{3} \left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**6/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{6}}{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**5/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{5}}{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**4/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{4}}{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{3}}{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{2}}{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | $\frac{d + e x}{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(-5/2)` | $\frac{1}{\left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/((d + e*x)*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right) \left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**2*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**3*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{3} \left(c d^{2} + 2 c d e x + c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**4*sqrt(a + b*x + c*x**2)` | $\left(b d + 2 c d x\right)^{4} \sqrt{a + b x + c x^{2}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**3*sqrt(a + b*x + c*x**2)` | $\left(b d + 2 c d x\right)^{3} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**2*sqrt(a + b*x + c*x**2)` | $\left(b d + 2 c d x\right)^{2} \sqrt{a + b x + c x^{2}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)*sqrt(a + b*x + c*x**2)` | $\left(b d + 2 c d x\right) \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(b*d + 2*c*d*x)` | $\frac{\sqrt{a + b x + c x^{2}}}{b d + 2 c d x}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(b*d + 2*c*d*x)**2` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(b d + 2 c d x\right)^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(b*d + 2*c*d*x)**3` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(b d + 2 c d x\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a + b*x + c*x**2)/(b*d + 2*c*d*x)**4` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(b d + 2 c d x\right)^{4}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(b*d + 2*c*d*x)**5` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(b d + 2 c d x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a + b*x + c*x**2)/(b*d + 2*c*d*x)**6` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(b d + 2 c d x\right)^{6}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(b*d + 2*c*d*x)**7` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(b d + 2 c d x\right)^{7}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**5*(a + b*x + c*x**2)**(3/2)` | $\left(b d + 2 c d x\right)^{5} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**4*(a + b*x + c*x**2)**(3/2)` | $\left(b d + 2 c d x\right)^{4} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**3*(a + b*x + c*x**2)**(3/2)` | $\left(b d + 2 c d x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**2*(a + b*x + c*x**2)**(3/2)` | $\left(b d + 2 c d x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)*(a + b*x + c*x**2)**(3/2)` | $\left(b d + 2 c d x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{b d + 2 c d x}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**2` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**3` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{3}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**4` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{4}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**5` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**6` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{6}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**7` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{7}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**8` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{8}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**9` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{9}}$ |
| timeout | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**10` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{10}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**5*(a + b*x + c*x**2)**(5/2)` | $\left(b d + 2 c d x\right)^{5} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**4*(a + b*x + c*x**2)**(5/2)` | $\left(b d + 2 c d x\right)^{4} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**3*(a + b*x + c*x**2)**(5/2)` | $\left(b d + 2 c d x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**2*(a + b*x + c*x**2)**(5/2)` | $\left(b d + 2 c d x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)*(a + b*x + c*x**2)**(5/2)` | $\left(b d + 2 c d x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{b d + 2 c d x}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**2` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**3` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{3}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**4` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{4}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**5` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{5}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**6` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{6}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**7` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{7}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**8` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{8}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**9` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{9}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**10` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{10}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**11` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{11}}$ |
| timeout | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**12` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{12}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**4/sqrt(a + b*x + c*x**2)` | $\frac{\left(b d + 2 c d x\right)^{4}}{\sqrt{a + b x + c x^{2}}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**3/sqrt(a + b*x + c*x**2)` | $\frac{\left(b d + 2 c d x\right)^{3}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**2/sqrt(a + b*x + c*x**2)` | $\frac{\left(b d + 2 c d x\right)^{2}}{\sqrt{a + b x + c x^{2}}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)/sqrt(a + b*x + c*x**2)` | $\frac{b d + 2 c d x}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(b d + 2 c d x\right) \sqrt{a + b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((b*d + 2*c*d*x)**2*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(b d + 2 c d x\right)^{2} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**3*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(b d + 2 c d x\right)^{3} \sqrt{a + b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((b*d + 2*c*d*x)**4*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(b d + 2 c d x\right)^{4} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**4/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b d + 2 c d x\right)^{4}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**3/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b d + 2 c d x\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**2/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b d + 2 c d x\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{b d + 2 c d x}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(b d + 2 c d x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((b*d + 2*c*d*x)**2*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(b d + 2 c d x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**3*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(b d + 2 c d x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((b*d + 2*c*d*x)**4*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(b d + 2 c d x\right)^{4} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**6/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b d + 2 c d x\right)^{6}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**5/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b d + 2 c d x\right)^{5}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**4/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b d + 2 c d x\right)^{4}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**3/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b d + 2 c d x\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**2/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b d + 2 c d x\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{b d + 2 c d x}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)*(a + b*x + c*x**2)**(5/2))` | $\frac{1}{\left(b d + 2 c d x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((b*d + 2*c*d*x)**2*(a + b*x + c*x**2)**(5/2))` | $\frac{1}{\left(b d + 2 c d x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**3*(a + b*x + c*x**2)**(5/2))` | $\frac{1}{\left(b d + 2 c d x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((b*d + 2*c*d*x)**4*(a + b*x + c*x**2)**(5/2))` | $\frac{1}{\left(b d + 2 c d x\right)^{4} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2 + 1))` | $\frac{1}{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2} + 1}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**(5/2)*(a + b*x + c*x**2)` | $\left(b d + 2 c d x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**(3/2)*(a + b*x + c*x**2)` | $\left(b d + 2 c d x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2)` | $\sqrt{b d + 2 c d x} \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)/sqrt(b*d + 2*c*d*x)` | $\frac{a + b x + c x^{2}}{\sqrt{b d + 2 c d x}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)/(b*d + 2*c*d*x)**(3/2)` | $\frac{a + b x + c x^{2}}{\left(b d + 2 c d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)/(b*d + 2*c*d*x)**(5/2)` | $\frac{a + b x + c x^{2}}{\left(b d + 2 c d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)/(b*d + 2*c*d*x)**(7/2)` | $\frac{a + b x + c x^{2}}{\left(b d + 2 c d x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)/(b*d + 2*c*d*x)**(9/2)` | $\frac{a + b x + c x^{2}}{\left(b d + 2 c d x\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(b*d + 2*c*d*x)**(3/2)*(a + b*x + c*x**2)**2` | $\left(b d + 2 c d x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2)**2` | $\sqrt{b d + 2 c d x} \left(a + b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**2/sqrt(b*d + 2*c*d*x)` | $\frac{\left(a + b x + c x^{2}\right)^{2}}{\sqrt{b d + 2 c d x}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**2/(b*d + 2*c*d*x)**(3/2)` | $\frac{\left(a + b x + c x^{2}\right)^{2}}{\left(b d + 2 c d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**2/(b*d + 2*c*d*x)**(5/2)` | $\frac{\left(a + b x + c x^{2}\right)^{2}}{\left(b d + 2 c d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**2/(b*d + 2*c*d*x)**(7/2)` | $\frac{\left(a + b x + c x^{2}\right)^{2}}{\left(b d + 2 c d x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**2/(b*d + 2*c*d*x)**(9/2)` | $\frac{\left(a + b x + c x^{2}\right)^{2}}{\left(b d + 2 c d x\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**2/(b*d + 2*c*d*x)**(11/2)` | $\frac{\left(a + b x + c x^{2}\right)^{2}}{\left(b d + 2 c d x\right)^{\frac{11}{2}}}$ |
| SOLVED-both | parametric | `sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2)**3` | $\sqrt{b d + 2 c d x} \left(a + b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**3/sqrt(b*d + 2*c*d*x)` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\sqrt{b d + 2 c d x}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**3/(b*d + 2*c*d*x)**(3/2)` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\left(b d + 2 c d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**3/(b*d + 2*c*d*x)**(5/2)` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\left(b d + 2 c d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**3/(b*d + 2*c*d*x)**(7/2)` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\left(b d + 2 c d x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**3/(b*d + 2*c*d*x)**(9/2)` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\left(b d + 2 c d x\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**3/(b*d + 2*c*d*x)**(11/2)` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\left(b d + 2 c d x\right)^{\frac{11}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**3/(b*d + 2*c*d*x)**(13/2)` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\left(b d + 2 c d x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(11/2)/(a + b*x + c*x**2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{11}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(9/2)/(a + b*x + c*x**2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{9}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(7/2)/(a + b*x + c*x**2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{7}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(5/2)/(a + b*x + c*x**2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{5}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(3/2)/(a + b*x + c*x**2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{3}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(b*d + 2*c*d*x)/(a + b*x + c*x**2)` | $\frac{\sqrt{b d + 2 c d x}}{a + b x + c x^{2}}$ |
| partial | parametric | `1/(sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2))` | $\frac{1}{\sqrt{b d + 2 c d x} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(3/2)*(a + b*x + c*x**2))` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(5/2)*(a + b*x + c*x**2))` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(7/2)*(a + b*x + c*x**2))` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{7}{2}} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(15/2)/(a + b*x + c*x**2)**2` | $\frac{\left(b d + 2 c d x\right)^{\frac{15}{2}}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(13/2)/(a + b*x + c*x**2)**2` | $\frac{\left(b d + 2 c d x\right)^{\frac{13}{2}}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(11/2)/(a + b*x + c*x**2)**2` | $\frac{\left(b d + 2 c d x\right)^{\frac{11}{2}}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(9/2)/(a + b*x + c*x**2)**2` | $\frac{\left(b d + 2 c d x\right)^{\frac{9}{2}}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(7/2)/(a + b*x + c*x**2)**2` | $\frac{\left(b d + 2 c d x\right)^{\frac{7}{2}}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(5/2)/(a + b*x + c*x**2)**2` | $\frac{\left(b d + 2 c d x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(3/2)/(a + b*x + c*x**2)**2` | $\frac{\left(b d + 2 c d x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(b*d + 2*c*d*x)/(a + b*x + c*x**2)**2` | $\frac{\sqrt{b d + 2 c d x}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2)**2)` | $\frac{1}{\sqrt{b d + 2 c d x} \left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(3/2)*(a + b*x + c*x**2)**2)` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(5/2)*(a + b*x + c*x**2)**2)` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(7/2)*(a + b*x + c*x**2)**2)` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{7}{2}} \left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(17/2)/(a + b*x + c*x**2)**3` | $\frac{\left(b d + 2 c d x\right)^{\frac{17}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(15/2)/(a + b*x + c*x**2)**3` | $\frac{\left(b d + 2 c d x\right)^{\frac{15}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(13/2)/(a + b*x + c*x**2)**3` | $\frac{\left(b d + 2 c d x\right)^{\frac{13}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(11/2)/(a + b*x + c*x**2)**3` | $\frac{\left(b d + 2 c d x\right)^{\frac{11}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(9/2)/(a + b*x + c*x**2)**3` | $\frac{\left(b d + 2 c d x\right)^{\frac{9}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(7/2)/(a + b*x + c*x**2)**3` | $\frac{\left(b d + 2 c d x\right)^{\frac{7}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(5/2)/(a + b*x + c*x**2)**3` | $\frac{\left(b d + 2 c d x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(3/2)/(a + b*x + c*x**2)**3` | $\frac{\left(b d + 2 c d x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(b*d + 2*c*d*x)/(a + b*x + c*x**2)**3` | $\frac{\sqrt{b d + 2 c d x}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `1/(sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2)**3)` | $\frac{1}{\sqrt{b d + 2 c d x} \left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(3/2)*(a + b*x + c*x**2)**3)` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(5/2)*(a + b*x + c*x**2)**3)` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(7/2)*(a + b*x + c*x**2)**3)` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{7}{2}} \left(a + b x + c x^{2}\right)^{3}}$ |
| partial | concrete | `(2*x + 1)**(7/2)/(x**2 + x + 1)` | $\frac{\left(2 x + 1\right)^{\frac{7}{2}}}{x^{2} + x + 1}$ |
| partial | concrete | `(2*x + 1)**(5/2)/(x**2 + x + 1)` | $\frac{\left(2 x + 1\right)^{\frac{5}{2}}}{x^{2} + x + 1}$ |
| partial | concrete | `(2*x + 1)**(3/2)/(x**2 + x + 1)` | $\frac{\left(2 x + 1\right)^{\frac{3}{2}}}{x^{2} + x + 1}$ |
| partial | concrete | `sqrt(2*x + 1)/(x**2 + x + 1)` | $\frac{\sqrt{2 x + 1}}{x^{2} + x + 1}$ |
| partial | concrete | `1/(sqrt(2*x + 1)*(x**2 + x + 1))` | $\frac{1}{\sqrt{2 x + 1} \left(x^{2} + x + 1\right)}$ |
| partial | concrete | `1/((2*x + 1)**(3/2)*(x**2 + x + 1))` | $\frac{1}{\left(2 x + 1\right)^{\frac{3}{2}} \left(x^{2} + x + 1\right)}$ |
| partial | concrete | `1/((2*x + 1)**(5/2)*(x**2 + x + 1))` | $\frac{1}{\left(2 x + 1\right)^{\frac{5}{2}} \left(x^{2} + x + 1\right)}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(7/2)*sqrt(a + b*x + c*x**2)` | $\left(b d + 2 c d x\right)^{\frac{7}{2}} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(3/2)*sqrt(a + b*x + c*x**2)` | $\left(b d + 2 c d x\right)^{\frac{3}{2}} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/sqrt(b*d + 2*c*d*x)` | $\frac{\sqrt{a + b x + c x^{2}}}{\sqrt{b d + 2 c d x}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(b*d + 2*c*d*x)**(5/2)` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(b d + 2 c d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(b*d + 2*c*d*x)**(9/2)` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(b d + 2 c d x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(b*d + 2*c*d*x)**(13/2)` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(b d + 2 c d x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(5/2)*sqrt(a + b*x + c*x**2)` | $\left(b d + 2 c d x\right)^{\frac{5}{2}} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(b*d + 2*c*d*x)*sqrt(a + b*x + c*x**2)` | $\sqrt{b d + 2 c d x} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(b*d + 2*c*d*x)**(3/2)` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(b d + 2 c d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(b*d + 2*c*d*x)**(7/2)` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(b d + 2 c d x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(7/2)*(a + b*x + c*x**2)**(3/2)` | $\left(b d + 2 c d x\right)^{\frac{7}{2}} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(3/2)*(a + b*x + c*x**2)**(3/2)` | $\left(b d + 2 c d x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/sqrt(b*d + 2*c*d*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\sqrt{b d + 2 c d x}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**(5/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**(9/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**(13/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**(17/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{\frac{17}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(5/2)*(a + b*x + c*x**2)**(3/2)` | $\left(b d + 2 c d x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2)**(3/2)` | $\sqrt{b d + 2 c d x} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**(3/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**(7/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(b*d + 2*c*d*x)**(11/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(b d + 2 c d x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(7/2)*(a + b*x + c*x**2)**(5/2)` | $\left(b d + 2 c d x\right)^{\frac{7}{2}} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(3/2)*(a + b*x + c*x**2)**(5/2)` | $\left(b d + 2 c d x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/sqrt(b*d + 2*c*d*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\sqrt{b d + 2 c d x}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**(5/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**(9/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**(13/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**(17/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{\frac{17}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**(21/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{\frac{21}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(5/2)*(a + b*x + c*x**2)**(5/2)` | $\left(b d + 2 c d x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2)**(5/2)` | $\sqrt{b d + 2 c d x} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**(3/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**(7/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**(11/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(b*d + 2*c*d*x)**(15/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(b d + 2 c d x\right)^{\frac{15}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(7/2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{7}{2}}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(3/2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{3}{2}}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/(sqrt(b*d + 2*c*d*x)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\sqrt{b d + 2 c d x} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(5/2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{5}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(9/2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{9}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(9/2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{9}{2}}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(5/2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{5}{2}}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `sqrt(b*d + 2*c*d*x)/sqrt(a + b*x + c*x**2)` | $\frac{\sqrt{b d + 2 c d x}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(3/2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{3}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(7/2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{7}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | concrete | `(3 - 2*x)**(3/2)/sqrt(x**2 - 3*x + 1)` | $\frac{\left(3 - 2 x\right)^{\frac{3}{2}}}{\sqrt{x^{2} - 3 x + 1}}$ |
| partial | concrete | `1/(sqrt(3 - 2*x)*sqrt(x**2 - 3*x + 1))` | $\frac{1}{\sqrt{3 - 2 x} \sqrt{x^{2} - 3 x + 1}}$ |
| partial | concrete | `1/((3 - 2*x)**(5/2)*sqrt(x**2 - 3*x + 1))` | $\frac{1}{\left(3 - 2 x\right)^{\frac{5}{2}} \sqrt{x^{2} - 3 x + 1}}$ |
| partial | concrete | `(3 - 2*x)**(5/2)/sqrt(x**2 - 3*x + 1)` | $\frac{\left(3 - 2 x\right)^{\frac{5}{2}}}{\sqrt{x^{2} - 3 x + 1}}$ |
| partial | concrete | `sqrt(3 - 2*x)/sqrt(x**2 - 3*x + 1)` | $\frac{\sqrt{3 - 2 x}}{\sqrt{x^{2} - 3 x + 1}}$ |
| partial | concrete | `1/((3 - 2*x)**(3/2)*sqrt(x**2 - 3*x + 1))` | $\frac{1}{\left(3 - 2 x\right)^{\frac{3}{2}} \sqrt{x^{2} - 3 x + 1}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(11/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{11}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(7/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{7}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(3/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\sqrt{b d + 2 c d x} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(5/2)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(9/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{9}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(5/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(b*d + 2*c*d*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{\sqrt{b d + 2 c d x}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(3/2)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(7/2)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{7}{2}} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(15/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{15}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(11/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{11}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(7/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{7}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(3/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2)**(5/2))` | $\frac{1}{\sqrt{b d + 2 c d x} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(5/2)*(a + b*x + c*x**2)**(5/2))` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(13/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{13}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(9/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{9}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b*d + 2*c*d*x)**(5/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b d + 2 c d x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(b*d + 2*c*d*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{\sqrt{b d + 2 c d x}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((b*d + 2*c*d*x)**(3/2)*(a + b*x + c*x**2)**(5/2))` | $\frac{1}{\left(b d + 2 c d x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(c*e + d*e*x)**(11/2)/sqrt(-c**2 - 2*c*d*x - d**2*x**2 + 1)` | $\frac{\left(c e + d e x\right)^{\frac{11}{2}}}{\sqrt{- c^{2} - 2 c d x - d^{2} x^{2} + 1}}$ |
| partial | parametric | `(c*e + d*e*x)**(7/2)/sqrt(-c**2 - 2*c*d*x - d**2*x**2 + 1)` | $\frac{\left(c e + d e x\right)^{\frac{7}{2}}}{\sqrt{- c^{2} - 2 c d x - d^{2} x^{2} + 1}}$ |
| partial | parametric | `(c*e + d*e*x)**(3/2)/sqrt(-c**2 - 2*c*d*x - d**2*x**2 + 1)` | $\frac{\left(c e + d e x\right)^{\frac{3}{2}}}{\sqrt{- c^{2} - 2 c d x - d^{2} x^{2} + 1}}$ |
| partial | parametric | `1/(sqrt(c*e + d*e*x)*sqrt(-c**2 - 2*c*d*x - d**2*x**2 + 1))` | $\frac{1}{\sqrt{c e + d e x} \sqrt{- c^{2} - 2 c d x - d^{2} x^{2} + 1}}$ |
| partial | parametric | `1/((c*e + d*e*x)**(5/2)*sqrt(-c**2 - 2*c*d*x - d**2*x**2 + 1))` | $\frac{1}{\left(c e + d e x\right)^{\frac{5}{2}} \sqrt{- c^{2} - 2 c d x - d^{2} x^{2} + 1}}$ |
| partial | parametric | `1/((c*e + d*e*x)**(9/2)*sqrt(-c**2 - 2*c*d*x - d**2*x**2 + 1))` | $\frac{1}{\left(c e + d e x\right)^{\frac{9}{2}} \sqrt{- c^{2} - 2 c d x - d^{2} x^{2} + 1}}$ |
| partial | parametric | `1/((c*e + d*e*x)**(13/2)*sqrt(-c**2 - 2*c*d*x - d**2*x**2 + 1))` | $\frac{1}{\left(c e + d e x\right)^{\frac{13}{2}} \sqrt{- c^{2} - 2 c d x - d^{2} x^{2} + 1}}$ |
| partial | parametric | `(c*e + d*e*x)**(9/2)/sqrt(-c**2 - 2*c*d*x - d**2*x**2 + 1)` | $\frac{\left(c e + d e x\right)^{\frac{9}{2}}}{\sqrt{- c^{2} - 2 c d x - d^{2} x^{2} + 1}}$ |
| partial | parametric | `(c*e + d*e*x)**(5/2)/sqrt(-c**2 - 2*c*d*x - d**2*x**2 + 1)` | $\frac{\left(c e + d e x\right)^{\frac{5}{2}}}{\sqrt{- c^{2} - 2 c d x - d^{2} x^{2} + 1}}$ |
| partial | parametric | `sqrt(c*e + d*e*x)/sqrt(-c**2 - 2*c*d*x - d**2*x**2 + 1)` | $\frac{\sqrt{c e + d e x}}{\sqrt{- c^{2} - 2 c d x - d^{2} x^{2} + 1}}$ |
| partial | parametric | `1/((c*e + d*e*x)**(3/2)*sqrt(-c**2 - 2*c*d*x - d**2*x**2 + 1))` | $\frac{1}{\left(c e + d e x\right)^{\frac{3}{2}} \sqrt{- c^{2} - 2 c d x - d^{2} x^{2} + 1}}$ |
| partial | parametric | `1/((c*e + d*e*x)**(7/2)*sqrt(-c**2 - 2*c*d*x - d**2*x**2 + 1))` | $\frac{1}{\left(c e + d e x\right)^{\frac{7}{2}} \sqrt{- c^{2} - 2 c d x - d^{2} x^{2} + 1}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(11/3)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(b d + 2 c d x\right)^{\frac{11}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(17/3)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(b d + 2 c d x\right)^{\frac{17}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(23/3)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(b d + 2 c d x\right)^{\frac{23}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(29/3)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(b d + 2 c d x\right)^{\frac{29}{3}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(2/3)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(b d + 2 c d x\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(8/3)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(b d + 2 c d x\right)^{\frac{8}{3}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(14/3)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(b d + 2 c d x\right)^{\frac{14}{3}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(20/3)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(b d + 2 c d x\right)^{\frac{20}{3}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(4/3)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(b d + 2 c d x\right)^{\frac{4}{3}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(10/3)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(b d + 2 c d x\right)^{\frac{10}{3}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(16/3)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(b d + 2 c d x\right)^{\frac{16}{3}}}$ |
| SOLVED-both | concrete | `(x + 1)/(x**2 + 2*x - 3)**(2/3)` | $\frac{x + 1}{\left(x^{2} + 2 x - 3\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `(b + c*x)/(a + 2*b*x + c*x**2)**(3/7)` | $\frac{b + c x}{\left(a + 2 b x + c x^{2}\right)^{\frac{3}{7}}}$ |
| SOLVED-both | parametric | `(d + e*x)**4*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(d + e x\right)^{4} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(d + e*x)**3*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(d + e x\right)^{3} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(d + e*x)**2*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(d + e x\right)^{2} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(d + e x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{d + e x}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**2` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**3` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**4` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**5` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**6` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{6}}$ |
| SOLVED-both | parametric | `(d + e*x)**5*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(d + e x\right)^{5} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)**4*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(d + e x\right)^{4} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(d + e x\right)^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(d + e x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**2` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**3` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**4` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**5` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**6` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{6}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**8` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{8}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**9` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{9}}$ |
| SOLVED-both | parametric | `(d + e*x)**5*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(d + e x\right)^{5} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)**4*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(d + e x\right)^{4} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(d + e x\right)^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(d + e x\right)^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(d + e x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**2` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**3` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**4` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**5` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**6` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{6}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**7` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{7}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**8` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{8}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**9` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{9}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**10` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{10}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**11` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{11}}$ |
| timeout | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**12` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{12}}$ |
| SOLVED-both | parametric | `(d + e*x)**4/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(d + e x\right)^{4}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(d + e x\right)^{3}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(d + e x\right)^{2}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{d + e x}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `1/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{1}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/((d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{\left(d + e x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**2*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{\left(d + e x\right)^{2} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**3*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{\left(d + e x\right)^{3} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**4*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{\left(d + e x\right)^{4} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**4/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{4}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{3}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{2}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{d + e x}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(-3/2)` | $\frac{1}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**6/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{6}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**5/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{5}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**4/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{4}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{3}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{2}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{d + e x}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(-5/2)` | $\frac{1}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)*(4*x**2 + 12*x + 9)**(5/2)` | $\left(d + e x\right) \left(4 x^{2} + 12 x + 9\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)*(4*x**2 + 12*x + 9)**(3/2)` | $\left(d + e x\right) \left(4 x^{2} + 12 x + 9\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(d + e*x)*sqrt(4*x**2 + 12*x + 9)` | $\left(d + e x\right) \sqrt{4 x^{2} + 12 x + 9}$ |
| SOLVED-both | parametric | `(d + e*x)/sqrt(4*x**2 + 12*x + 9)` | $\frac{d + e x}{\sqrt{4 x^{2} + 12 x + 9}}$ |
| SOLVED-both | parametric | `(d + e*x)/(4*x**2 + 12*x + 9)**(3/2)` | $\frac{d + e x}{\left(4 x^{2} + 12 x + 9\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(4*x**2 + 12*x + 9)**(5/2)` | $\frac{d + e x}{\left(4 x^{2} + 12 x + 9\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(4*x**2 + 12*x + 9)**(7/2)` | $\frac{d + e x}{\left(4 x^{2} + 12 x + 9\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)` | $\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)` | $\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)` | $\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)/sqrt(d + e*x)` | $\frac{a^{2} + 2 a b x + b^{2} x^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(3/2)` | $\frac{a^{2} + 2 a b x + b^{2} x^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(5/2)` | $\frac{a^{2} + 2 a b x + b^{2} x^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(7/2)` | $\frac{a^{2} + 2 a b x + b^{2} x^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**2/sqrt(d + e*x)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**2/(d + e*x)**(3/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**2/(d + e*x)**(5/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**2/(d + e*x)**(7/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**3/sqrt(d + e*x)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**3/(d + e*x)**(3/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**3/(d + e*x)**(5/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**3/(d + e*x)**(7/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**(9/2)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\sqrt{d + e x}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(d + e*x)**(11/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{11}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(9/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\sqrt{d + e x}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{1}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(15/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{15}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(13/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{13}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(11/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{11}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(9/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\sqrt{d + e x}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{1}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(5/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(d + e x\right)^{\frac{5}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(d + e x\right)^{\frac{3}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\sqrt{d + e x} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/sqrt(d + e*x)` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(3/2)` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(5/2)` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(7/2)` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/sqrt(d + e*x)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(9/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(11/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/sqrt(d + e*x)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(3/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(7/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(9/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(11/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(13/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(15/2)` | $\frac{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{15}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\sqrt{d + e x}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{\sqrt{d + e x} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**(9/2)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\sqrt{d + e x}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{1}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(13/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{13}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(11/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{11}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(9/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\sqrt{d + e x}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{1}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**4*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\left(d + e x\right)^{4} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| partial | parametric | `(d + e*x)**3*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\left(d + e x\right)^{3} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| partial | parametric | `(d + e*x)**2*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\left(d + e x\right)^{2} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| partial | parametric | `(d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\left(d + e x\right) \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{d + e x}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**2` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\left(d + e x\right)^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**3` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\left(d + e x\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**4` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\left(d + e x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**5` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\left(d + e x\right)^{5}}$ |
| timeout | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**6` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(d + e*x)**4*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\left(d + e x\right)^{4} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\left(d + e x\right)^{3} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\left(d + e x\right)^{2} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**2` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**3` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**4` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**5` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**6` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{6}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**7` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{7}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**8` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{8}}$ |
| partial | parametric | `(d + e*x)**4*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\left(d + e x\right)^{4} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\left(d + e x\right)^{3} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\left(d + e x\right)^{2} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**2` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**3` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**4` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**5` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**6` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{6}}$ |
| **SOLVED-NEW** | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**7` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{7}}$ |
| **SOLVED-NEW** | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**8` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{8}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**9` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{9}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**10` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{10}}$ |
| partial | parametric | `(d + e*x)**3/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{3}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `(d + e*x)**2/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{2}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `(d + e*x)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{d + e x}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `1/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{1}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\left(d + e x\right) \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**2*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\left(d + e x\right)^{2} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**3*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\left(d + e x\right)^{3} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| timeout | parametric | `1/((d + e*x)**4*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\left(d + e x\right)^{4} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `(d + e*x)**5/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{5}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**4/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{4}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**3/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{3}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**2/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{2}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{d + e x}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(-3/2)` | $\frac{1}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{\left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/((d + e*x)**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{\left(d + e x\right)^{3} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/((d + e*x)**4*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{\left(d + e x\right)^{4} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**6/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{6}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**5/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{5}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**4/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{4}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{3}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{2}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{d + e x}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(-5/2)` | $\frac{1}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{1}{\left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `1/((d + e*x)**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `1/((d + e*x)**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{1}{\left(d + e x\right)^{3} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(1/3)` | $\frac{d + e x}{\sqrt[3]{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(-1/3)` | $\frac{1}{\sqrt[3]{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| SOLVED-both | parametric | `(d + e*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\left(d + e x\right)^{\frac{3}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)$ |
| SOLVED-both | parametric | `sqrt(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\sqrt{d + e x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | $\frac{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**(3/2)` | $\frac{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**(5/2)` | $\frac{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**(7/2)` | $\frac{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**(9/2)` | $\frac{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**(11/2)` | $\frac{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| SOLVED-both | parametric | `sqrt(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2` | $\sqrt{d + e x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2/sqrt(d + e*x)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2/(d + e*x)**(3/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2/(d + e*x)**(5/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2/(d + e*x)**(7/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2/(d + e*x)**(9/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2/(d + e*x)**(11/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2/(d + e*x)**(13/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| SOLVED-both | parametric | `sqrt(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3` | $\sqrt{d + e x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3/sqrt(d + e*x)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3/(d + e*x)**(3/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3/(d + e*x)**(5/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3/(d + e*x)**(7/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3/(d + e*x)**(9/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3/(d + e*x)**(11/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| SOLVED-both | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3/(d + e*x)**(13/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(d + e*x)**(9/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| partial | parametric | `sqrt(d + e*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\sqrt{d + e x}}{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\sqrt{d + e x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)}$ |
| partial | parametric | `(d + e*x)**(13/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2` | $\frac{\left(d + e x\right)^{\frac{13}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(11/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2` | $\frac{\left(d + e x\right)^{\frac{11}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(9/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2` | $\frac{\sqrt{d + e x}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2)` | $\frac{1}{\sqrt{d + e x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**2)` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(15/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3` | $\frac{\left(d + e x\right)^{\frac{15}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(13/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3` | $\frac{\left(d + e x\right)^{\frac{13}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(11/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3` | $\frac{\left(d + e x\right)^{\frac{11}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(9/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3` | $\frac{\left(d + e x\right)^{\frac{9}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}$ |
| partial | parametric | `sqrt(d + e*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3` | $\frac{\sqrt{d + e x}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**3)` | $\frac{1}{\sqrt{d + e x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(7/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\left(d + e x\right)^{\frac{7}{2}} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| partial | parametric | `(d + e*x)**(5/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\left(d + e x\right)^{\frac{5}{2}} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| partial | parametric | `(d + e*x)**(3/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\left(d + e x\right)^{\frac{3}{2}} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| **SOLVED-NEW** | parametric | `sqrt(d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\sqrt{d + e x} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}$ |
| **SOLVED-NEW** | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x}}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**(3/2)` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**(5/2)` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**(7/2)` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**(9/2)` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\left(d + e x\right)^{\frac{5}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\sqrt{d + e x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/sqrt(d + e*x)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(9/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(11/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(13/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\sqrt{d + e x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/sqrt(d + e*x)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(3/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(7/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(9/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(11/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(13/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(15/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{15}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(17/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{17}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `(d + e*x)**(5/2)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d + e*x)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\sqrt{d + e x}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\sqrt{d + e x} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(5/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\sqrt{d + e x}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{\sqrt{d + e x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(7/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(5/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\sqrt{d + e x}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{1}{\sqrt{d + e x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*sqrt(d**2 - e**2*x**2))` | $\frac{1}{\sqrt{d + e x} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `1/(sqrt(-d + e*x)*sqrt(d**2 - e**2*x**2))` | $\frac{1}{\sqrt{- d + e x} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**(2/3)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{2}{3}}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| SOLVED-both | parametric | `(d + e*x)**(5/2)*(a + b*x + c*x**2)` | $\left(d + e x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(d + e*x)**(3/2)*(a + b*x + c*x**2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `sqrt(d + e*x)*(a + b*x + c*x**2)` | $\sqrt{d + e x} \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)/sqrt(d + e*x)` | $\frac{a + b x + c x^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)/(d + e*x)**(3/2)` | $\frac{a + b x + c x^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)/(d + e*x)**(5/2)` | $\frac{a + b x + c x^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)/(d + e*x)**(7/2)` | $\frac{a + b x + c x^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**(5/2)*(a + b*x + c*x**2)**2` | $\left(d + e x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(d + e*x)**(3/2)*(a + b*x + c*x**2)**2` | $\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(d + e*x)*(a + b*x + c*x**2)**2` | $\sqrt{d + e x} \left(a + b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**2/sqrt(d + e*x)` | $\frac{\left(a + b x + c x^{2}\right)^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**2/(d + e*x)**(3/2)` | $\frac{\left(a + b x + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**2/(d + e*x)**(5/2)` | $\frac{\left(a + b x + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**2/(d + e*x)**(7/2)` | $\frac{\left(a + b x + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**(5/2)*(a + b*x + c*x**2)**3` | $\left(d + e x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(d + e*x)**(3/2)*(a + b*x + c*x**2)**3` | $\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(d + e*x)*(a + b*x + c*x**2)**3` | $\sqrt{d + e x} \left(a + b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**3/sqrt(d + e*x)` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**3/(d + e*x)**(3/2)` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**3/(d + e*x)**(5/2)` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**3/(d + e*x)**(7/2)` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a + b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a + b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(a + b*x + c*x**2)` | $\frac{\sqrt{d + e x}}{a + b x + c x^{2}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a + b*x + c*x**2))` | $\frac{1}{\sqrt{d + e x} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a + b*x + c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a + b*x + c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a + b*x + c*x**2)**2` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(a + b*x + c*x**2)**2` | $\frac{\sqrt{d + e x}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a + b*x + c*x**2)**2)` | $\frac{1}{\sqrt{d + e x} \left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a + b*x + c*x**2)**2)` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `1/(x**(5/2)*(a + b*x + c*x**2)**2)` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a + b*x + c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a + b*x + c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a + b*x + c*x**2)**3` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(d + e*x)/(a + b*x + c*x**2)**3` | $\frac{\sqrt{d + e x}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a + b*x + c*x**2)**3)` | $\frac{1}{\sqrt{d + e x} \left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(d + e*x)/(a + I*b*x + c*x**2)` | $\frac{\sqrt{d + e x}}{a + i b x + c x^{2}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a + I*b*x + c*x**2))` | $\frac{1}{\sqrt{d + e x} \left(a + i b x + c x^{2}\right)}$ |
| partial | concrete | `(2*x + 1)**(7/2)/(5*x**2 + 3*x + 2)` | $\frac{\left(2 x + 1\right)^{\frac{7}{2}}}{5 x^{2} + 3 x + 2}$ |
| partial | concrete | `(2*x + 1)**(5/2)/(5*x**2 + 3*x + 2)` | $\frac{\left(2 x + 1\right)^{\frac{5}{2}}}{5 x^{2} + 3 x + 2}$ |
| partial | concrete | `(2*x + 1)**(3/2)/(5*x**2 + 3*x + 2)` | $\frac{\left(2 x + 1\right)^{\frac{3}{2}}}{5 x^{2} + 3 x + 2}$ |
| partial | concrete | `sqrt(2*x + 1)/(5*x**2 + 3*x + 2)` | $\frac{\sqrt{2 x + 1}}{5 x^{2} + 3 x + 2}$ |
| partial | concrete | `1/(sqrt(2*x + 1)*(5*x**2 + 3*x + 2))` | $\frac{1}{\sqrt{2 x + 1} \left(5 x^{2} + 3 x + 2\right)}$ |
| partial | concrete | `1/((2*x + 1)**(3/2)*(5*x**2 + 3*x + 2))` | $\frac{1}{\left(2 x + 1\right)^{\frac{3}{2}} \left(5 x^{2} + 3 x + 2\right)}$ |
| partial | concrete | `1/((2*x + 1)**(5/2)*(5*x**2 + 3*x + 2))` | $\frac{1}{\left(2 x + 1\right)^{\frac{5}{2}} \left(5 x^{2} + 3 x + 2\right)}$ |
| partial | concrete | `(2*x + 1)**(7/2)/(5*x**2 + 3*x + 2)**2` | $\frac{\left(2 x + 1\right)^{\frac{7}{2}}}{\left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `(2*x + 1)**(5/2)/(5*x**2 + 3*x + 2)**2` | $\frac{\left(2 x + 1\right)^{\frac{5}{2}}}{\left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `(2*x + 1)**(3/2)/(5*x**2 + 3*x + 2)**2` | $\frac{\left(2 x + 1\right)^{\frac{3}{2}}}{\left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `sqrt(2*x + 1)/(5*x**2 + 3*x + 2)**2` | $\frac{\sqrt{2 x + 1}}{\left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `1/(sqrt(2*x + 1)*(5*x**2 + 3*x + 2)**2)` | $\frac{1}{\sqrt{2 x + 1} \left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `1/((2*x + 1)**(3/2)*(5*x**2 + 3*x + 2)**2)` | $\frac{1}{\left(2 x + 1\right)^{\frac{3}{2}} \left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `1/((2*x + 1)**(5/2)*(5*x**2 + 3*x + 2)**2)` | $\frac{1}{\left(2 x + 1\right)^{\frac{5}{2}} \left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `(2*x + 1)**(9/2)/(5*x**2 + 3*x + 2)**3` | $\frac{\left(2 x + 1\right)^{\frac{9}{2}}}{\left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | concrete | `(2*x + 1)**(7/2)/(5*x**2 + 3*x + 2)**3` | $\frac{\left(2 x + 1\right)^{\frac{7}{2}}}{\left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | concrete | `(2*x + 1)**(5/2)/(5*x**2 + 3*x + 2)**3` | $\frac{\left(2 x + 1\right)^{\frac{5}{2}}}{\left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | concrete | `(2*x + 1)**(3/2)/(5*x**2 + 3*x + 2)**3` | $\frac{\left(2 x + 1\right)^{\frac{3}{2}}}{\left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | concrete | `sqrt(2*x + 1)/(5*x**2 + 3*x + 2)**3` | $\frac{\sqrt{2 x + 1}}{\left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | concrete | `1/(sqrt(2*x + 1)*(5*x**2 + 3*x + 2)**3)` | $\frac{1}{\sqrt{2 x + 1} \left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | concrete | `1/((2*x + 1)**(3/2)*(5*x**2 + 3*x + 2)**3)` | $\frac{1}{\left(2 x + 1\right)^{\frac{3}{2}} \left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | parametric | `x**(9/2)/(a + b*x + c*x**2)**3` | $\frac{x^{\frac{9}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `1/(x**(3/2)*(a + b*x + c*x**2)**3)` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{3}}$ |
| SOLVED-both | concrete | `(x**2 - x + 3)/x**(1/3)` | $\frac{x^{2} - x + 3}{\sqrt[3]{x}}$ |
| partial | parametric | `(d + e*x)**3*sqrt(a + b*x + c*x**2)` | $\left(d + e x\right)^{3} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)**2*sqrt(a + b*x + c*x**2)` | $\left(d + e x\right)^{2} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)*sqrt(a + b*x + c*x**2)` | $\left(d + e x\right) \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)` | $\sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x)` | $\frac{\sqrt{a + b x + c x^{2}}}{d + e x}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x)**2` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x)**3` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x)**4` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x)**5` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x)**6` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(d + e*x)**3*(a + b*x + c*x**2)**(3/2)` | $\left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)**2*(a + b*x + c*x**2)**(3/2)` | $\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)*(a + b*x + c*x**2)**(3/2)` | $\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)` | $\left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)**2` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)**3` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)**4` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)**5` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)**6` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)**7` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{7}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)**8` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{8}}$ |
| partial | parametric | `(d + e*x)**3*(a + b*x + c*x**2)**(5/2)` | $\left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)**2*(a + b*x + c*x**2)**(5/2)` | $\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)*(a + b*x + c*x**2)**(5/2)` | $\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)` | $\left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(d + e*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(d + e*x)**2` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(d + e*x)**3` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(d + e*x)**4` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(d + e*x)**5` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{5}}$ |
| partial | concrete | `sqrt(5*x**2 - 3*x - 2)/x` | $\frac{\sqrt{5 x^{2} - 3 x - 2}}{x}$ |
| partial | concrete | `sqrt(-x**2 - x + 2)/x**2` | $\frac{\sqrt{- x^{2} - x + 2}}{x^{2}}$ |
| SOLVED-both | concrete | `(x + 1)**3*sqrt(x**2 + 2*x + 2)` | $\left(x + 1\right)^{3} \sqrt{x^{2} + 2 x + 2}$ |
| partial | concrete | `(3*x - 2)*sqrt(9*x**2 + 12*x + 8)` | $\left(3 x - 2\right) \sqrt{9 x^{2} + 12 x + 8}$ |
| partial | concrete | `(7 - 2*x)*sqrt(-4*x**2 + 16*x + 9)` | $\left(7 - 2 x\right) \sqrt{- 4 x^{2} + 16 x + 9}$ |
| partial | concrete | `sqrt(x**2 - x - 1)/(x + 1)` | $\frac{\sqrt{x^{2} - x - 1}}{x + 1}$ |
| partial | concrete | `sqrt(x**2 - x - 1)/(1 - x)` | $\frac{\sqrt{x^{2} - x - 1}}{1 - x}$ |
| partial | parametric | `x**6/sqrt(a + b*x + c*x**2)` | $\frac{x^{6}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `x**5/sqrt(a + b*x + c*x**2)` | $\frac{x^{5}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**4/sqrt(a + b*x + c*x**2)` | $\frac{\left(d + e x\right)^{4}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**3/sqrt(a + b*x + c*x**2)` | $\frac{\left(d + e x\right)^{3}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**2/sqrt(a + b*x + c*x**2)` | $\frac{\left(d + e x\right)^{2}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)/sqrt(a + b*x + c*x**2)` | $\frac{d + e x}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/sqrt(a + b*x + c*x**2)` | $\frac{1}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**2*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{2} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**3*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{3} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**4*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{4} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**4/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{4}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**3/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**2/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{d + e x}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**(-3/2)` | $\frac{1}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**2*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**3*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/((d + e*x)**4*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{4} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**5/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{5}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**4/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{4}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{d + e x}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)**(-5/2)` | $\frac{1}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)*(a + b*x + c*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**2*(a + b*x + c*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**3*(a + b*x + c*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(x + 3)/sqrt(-x**2 - 4*x + 5)` | $\frac{x + 3}{\sqrt{- x^{2} - 4 x + 5}}$ |
| partial | concrete | `(5 - 4*x)/sqrt(-4*x**2 + 12*x - 8)` | $\frac{5 - 4 x}{\sqrt{- 4 x^{2} + 12 x - 8}}$ |
| partial | concrete | `(2*x + 3)/sqrt(x**2 + 2*x + 5)` | $\frac{2 x + 3}{\sqrt{x^{2} + 2 x + 5}}$ |
| partial | concrete | `(x - 1)/sqrt(x**2 - 4*x + 3)` | $\frac{x - 1}{\sqrt{x^{2} - 4 x + 3}}$ |
| partial | concrete | `1/((1 - x)*sqrt(x**2 + 2*x - 4))` | $\frac{1}{\left(1 - x\right) \sqrt{x^{2} + 2 x - 4}}$ |
| partial | concrete | `1/((x - 2)*sqrt(x**2 - 4*x + 3))` | $\frac{1}{\left(x - 2\right) \sqrt{x^{2} - 4 x + 3}}$ |
| SOLVED-both | concrete | `(x + 1)/(x**2 + 3*x + 2)**(3/2)` | $\frac{x + 1}{\left(x^{2} + 3 x + 2\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)*sqrt(b**2/(4*c) + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right) \sqrt{\frac{b^{2}}{4 c} + b x + c x^{2}}}$ |
| partial | parametric | `1/((b*e/(2*c) + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(\frac{b e}{2 c} + e x\right) \sqrt{a + b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)*sqrt(b*x + c*x**2 + (b*d*e - c*d**2)/e**2))` | $\frac{1}{\left(d + e x\right) \sqrt{b x + c x^{2} + \frac{b d e - c d^{2}}{e^{2}}}}$ |
| SOLVED-both | parametric | `1/((b*e/(2*c) + e*x)*sqrt(b**2/(4*c) + b*x + c*x**2))` | $\frac{1}{\left(\frac{b e}{2 c} + e x\right) \sqrt{\frac{b^{2}}{4 c} + b x + c x^{2}}}$ |
| partial | concrete | `x/sqrt(3*x**2 + 4*x + 2)` | $\frac{x}{\sqrt{3 x^{2} + 4 x + 2}}$ |
| partial | concrete | `x/sqrt(-3*x**2 + 4*x + 2)` | $\frac{x}{\sqrt{- 3 x^{2} + 4 x + 2}}$ |
| partial | concrete | `x/sqrt(3*x**2 + 5*x + 2)` | $\frac{x}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `x/sqrt(-3*x**2 + 5*x + 2)` | $\frac{x}{\sqrt{- 3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `x/sqrt(3*x**2 + 4*x - 2)` | $\frac{x}{\sqrt{3 x^{2} + 4 x - 2}}$ |
| partial | concrete | `x/sqrt(-3*x**2 + 4*x - 2)` | $\frac{x}{\sqrt{- 3 x^{2} + 4 x - 2}}$ |
| partial | concrete | `x/sqrt(3*x**2 + 5*x - 2)` | $\frac{x}{\sqrt{3 x^{2} + 5 x - 2}}$ |
| partial | concrete | `x/sqrt(-3*x**2 + 5*x - 2)` | $\frac{x}{\sqrt{- 3 x^{2} + 5 x - 2}}$ |
| partial | parametric | `1/(x*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{1}{x \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/(x*sqrt(a**2 - 2*a*b*x + b**2*x**2))` | $\frac{1}{x \sqrt{a^{2} - 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `1/(x*sqrt(-a**2 + 2*a*b*x - b**2*x**2))` | $\frac{1}{x \sqrt{- a^{2} + 2 a b x - b^{2} x^{2}}}$ |
| partial | parametric | `1/(x*sqrt(-a**2 - 2*a*b*x - b**2*x**2))` | $\frac{1}{x \sqrt{- a^{2} - 2 a b x - b^{2} x^{2}}}$ |
| partial | concrete | `x*sqrt(-x**2 - 2*x + 3)` | $x \sqrt{- x^{2} - 2 x + 3}$ |
| partial | concrete | `x*sqrt(-x**2 + 2*x + 8)` | $x \sqrt{- x^{2} + 2 x + 8}$ |
| partial | concrete | `x*sqrt(x**2 + 2*x + 4)` | $x \sqrt{x^{2} + 2 x + 4}$ |
| partial | concrete | `1/(x*sqrt(3*x**2 + 4*x + 2))` | $\frac{1}{x \sqrt{3 x^{2} + 4 x + 2}}$ |
| partial | concrete | `1/(x*sqrt(-3*x**2 + 4*x + 2))` | $\frac{1}{x \sqrt{- 3 x^{2} + 4 x + 2}}$ |
| partial | concrete | `1/(x*sqrt(3*x**2 + 5*x + 2))` | $\frac{1}{x \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `1/(x*sqrt(-3*x**2 + 5*x + 2))` | $\frac{1}{x \sqrt{- 3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `1/(x*sqrt(3*x**2 + 4*x - 2))` | $\frac{1}{x \sqrt{3 x^{2} + 4 x - 2}}$ |
| partial | concrete | `1/(x*sqrt(-3*x**2 + 4*x - 2))` | $\frac{1}{x \sqrt{- 3 x^{2} + 4 x - 2}}$ |
| partial | concrete | `1/(x*sqrt(3*x**2 + 5*x - 2))` | $\frac{1}{x \sqrt{3 x^{2} + 5 x - 2}}$ |
| partial | concrete | `1/(x*sqrt(-3*x**2 + 5*x - 2))` | $\frac{1}{x \sqrt{- 3 x^{2} + 5 x - 2}}$ |
| partial | concrete | `1/(x**3*sqrt(x**2 + x + 1))` | $\frac{1}{x^{3} \sqrt{x^{2} + x + 1}}$ |
| partial | parametric | `(d*x)**(5/2)*sqrt(a + b*x + c*x**2)` | $\left(d x\right)^{\frac{5}{2}} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)*sqrt(a + b*x + c*x**2)` | $\left(d + e x\right)^{\frac{3}{2}} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(d + e*x)*sqrt(a + b*x + c*x**2)` | $\sqrt{d + e x} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/sqrt(d + e*x)` | $\frac{\sqrt{a + b x + c x^{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x)**(3/2)` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x)**(5/2)` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x)**(7/2)` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(a + b*x + c*x**2)**(3/2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(d + e*x)*(a + b*x + c*x**2)**(3/2)` | $\sqrt{d + e x} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/sqrt(d + e*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)**(9/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `sqrt(d*x)*(a + b*x + c*x**2)**(5/2)` | $\sqrt{d x} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/sqrt(d + e*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(d + e*x)**(3/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(d + e*x)**(7/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(d + e*x)**(9/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/(d + e*x)**(11/2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/sqrt(a + b*x + c*x**2)` | $\frac{\sqrt{d + e x}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\sqrt{d + e x} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**(7/2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{7}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{\sqrt{d + e x}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\sqrt{d + e x} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(5/2)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{\sqrt{d + e x}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(d + e*x)*(a + b*x + c*x**2)**(5/2))` | $\frac{1}{\sqrt{d + e x} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a + b*x + c*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(5*x + 3)/sqrt(-12*x**2 + 5*x + 2)` | $\frac{\sqrt{5 x + 3}}{\sqrt{- 12 x^{2} + 5 x + 2}}$ |
| partial | parametric | `(d + e*x)**2*(a + b*x + c*x**2)**(4/3)` | $\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(d + e*x)*(a + b*x + c*x**2)**(4/3)` | $\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(4/3)` | $\left(a + b x + c x^{2}\right)^{\frac{4}{3}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(4/3)/(d + e*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{d + e x}$ |
| partial | parametric | `(a + b*x + c*x**2)**(4/3)/(d + e*x)**2` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(4/3)/(d + e*x)**3` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{4}{3}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(d + e*x)**3/(a + b*x + c*x**2)**(7/3)` | $\frac{\left(d + e x\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{7}{3}}}$ |
| partial | parametric | `(d + e*x)**2/(a + b*x + c*x**2)**(7/3)` | $\frac{\left(d + e x\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{7}{3}}}$ |
| partial | parametric | `(d + e*x)/(a + b*x + c*x**2)**(7/3)` | $\frac{d + e x}{\left(a + b x + c x^{2}\right)^{\frac{7}{3}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(-7/3)` | $\frac{1}{\left(a + b x + c x^{2}\right)^{\frac{7}{3}}}$ |
| partial | parametric | `1/((d + e*x)*(a + b*x + c*x**2)**(7/3))` | $\frac{1}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{7}{3}}}$ |
| partial | parametric | `1/((d + e*x)**2*(a + b*x + c*x**2)**(7/3))` | $\frac{1}{\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{7}{3}}}$ |
| partial | parametric | `1/((d + e*x)**3*(a + b*x + c*x**2)**(7/3))` | $\frac{1}{\left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{7}{3}}}$ |
| partial | parametric | `1/((d + e*x)*(b**2*e**2 - b*c*d*e + 3*b*c*e**2*x + c**2*d**2 + 3*c**2*e**2*x**2)**(1/3))` | $\frac{1}{\left(d + e x\right) \sqrt[3]{b^{2} e^{2} - b c d e + 3 b c e^{2} x + c^{2} d^{2} + 3 c^{2} e^{2} x^{2}}}$ |
| partial | concrete | `(3*x + 2)**3/(27*x**2 - 54*x + 52)**(1/3)` | $\frac{\left(3 x + 2\right)^{3}}{\sqrt[3]{27 x^{2} - 54 x + 52}}$ |
| partial | concrete | `(3*x + 2)**2/(27*x**2 - 54*x + 52)**(1/3)` | $\frac{\left(3 x + 2\right)^{2}}{\sqrt[3]{27 x^{2} - 54 x + 52}}$ |
| partial | concrete | `(3*x + 2)/(27*x**2 - 54*x + 52)**(1/3)` | $\frac{3 x + 2}{\sqrt[3]{27 x^{2} - 54 x + 52}}$ |
| partial | concrete | `1/((3*x + 2)*(27*x**2 - 54*x + 52)**(1/3))` | $\frac{1}{\left(3 x + 2\right) \sqrt[3]{27 x^{2} - 54 x + 52}}$ |
| partial | concrete | `1/((3*x + 2)**2*(27*x**2 - 54*x + 52)**(1/3))` | $\frac{1}{\left(3 x + 2\right)^{2} \sqrt[3]{27 x^{2} - 54 x + 52}}$ |
| partial | concrete | `1/((3*x + 2)**3*(27*x**2 - 54*x + 52)**(1/3))` | $\frac{1}{\left(3 x + 2\right)^{3} \sqrt[3]{27 x^{2} - 54 x + 52}}$ |
| partial | concrete | `(3*x + 2)**3/(27*x**2 + 54*x + 28)**(1/3)` | $\frac{\left(3 x + 2\right)^{3}}{\sqrt[3]{27 x^{2} + 54 x + 28}}$ |
| partial | concrete | `(3*x + 2)**2/(27*x**2 + 54*x + 28)**(1/3)` | $\frac{\left(3 x + 2\right)^{2}}{\sqrt[3]{27 x^{2} + 54 x + 28}}$ |
| partial | concrete | `(3*x + 2)/(27*x**2 + 54*x + 28)**(1/3)` | $\frac{3 x + 2}{\sqrt[3]{27 x^{2} + 54 x + 28}}$ |
| partial | concrete | `1/((3*x + 2)*(27*x**2 + 54*x + 28)**(1/3))` | $\frac{1}{\left(3 x + 2\right) \sqrt[3]{27 x^{2} + 54 x + 28}}$ |
| partial | concrete | `1/((3*x + 2)**2*(27*x**2 + 54*x + 28)**(1/3))` | $\frac{1}{\left(3 x + 2\right)^{2} \sqrt[3]{27 x^{2} + 54 x + 28}}$ |
| partial | concrete | `1/((3*x + 2)**3*(27*x**2 + 54*x + 28)**(1/3))` | $\frac{1}{\left(3 x + 2\right)^{3} \sqrt[3]{27 x^{2} + 54 x + 28}}$ |
| partial | parametric | `1/((d + e*x)*(2*b**2*e**2 + b*c*d*e + 9*b*c*e**2*x - c**2*d**2 + 9*c**2*e**2*x**2)**(1/3))` | $\frac{1}{\left(d + e x\right) \sqrt[3]{2 b^{2} e^{2} + b c d e + 9 b c e^{2} x - c^{2} d^{2} + 9 c^{2} e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**3*(a + b*x + c*x**2)**(1/4)` | $\left(d + e x\right)^{3} \sqrt[4]{a + b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)**2*(a + b*x + c*x**2)**(1/4)` | $\left(d + e x\right)^{2} \sqrt[4]{a + b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)*(a + b*x + c*x**2)**(1/4)` | $\left(d + e x\right) \sqrt[4]{a + b x + c x^{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(1/4)` | $\sqrt[4]{a + b x + c x^{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(1/4)/(d + e*x)` | $\frac{\sqrt[4]{a + b x + c x^{2}}}{d + e x}$ |
| partial | parametric | `(a + b*x + c*x**2)**(1/4)/(d + e*x)**2` | $\frac{\sqrt[4]{a + b x + c x^{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(d + e*x)**3*(a + b*x + c*x**2)**(3/4)` | $\left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(d + e*x)**2*(a + b*x + c*x**2)**(3/4)` | $\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(d + e*x)*(a + b*x + c*x**2)**(3/4)` | $\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/4)` | $\left(a + b x + c x^{2}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/4)/(d + e*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{4}}}{d + e x}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/4)/(d + e*x)**2` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{4}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(d + e*x)**3*(a + b*x + c*x**2)**(5/4)` | $\left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{5}{4}}$ |
| partial | parametric | `(d + e*x)**2*(a + b*x + c*x**2)**(5/4)` | $\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{5}{4}}$ |
| partial | parametric | `(d + e*x)*(a + b*x + c*x**2)**(5/4)` | $\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{4}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/4)` | $\left(a + b x + c x^{2}\right)^{\frac{5}{4}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/4)/(d + e*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{4}}}{d + e x}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/4)/(d + e*x)**2` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{4}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(d + e*x)**3/(a + b*x + c*x**2)**(1/4)` | $\frac{\left(d + e x\right)^{3}}{\sqrt[4]{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**2/(a + b*x + c*x**2)**(1/4)` | $\frac{\left(d + e x\right)^{2}}{\sqrt[4]{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)/(a + b*x + c*x**2)**(1/4)` | $\frac{d + e x}{\sqrt[4]{a + b x + c x^{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(-1/4)` | $\frac{1}{\sqrt[4]{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)*(a + b*x + c*x**2)**(1/4))` | $\frac{1}{\left(d + e x\right) \sqrt[4]{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**2*(a + b*x + c*x**2)**(1/4))` | $\frac{1}{\left(d + e x\right)^{2} \sqrt[4]{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)**3*(a + b*x + c*x**2)**(1/4))` | $\frac{1}{\left(d + e x\right)^{3} \sqrt[4]{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**3/(a + b*x + c*x**2)**(3/4)` | $\frac{\left(d + e x\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(d + e*x)**2/(a + b*x + c*x**2)**(3/4)` | $\frac{\left(d + e x\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(d + e*x)/(a + b*x + c*x**2)**(3/4)` | $\frac{d + e x}{\left(a + b x + c x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(-3/4)` | $\frac{1}{\left(a + b x + c x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((d + e*x)*(a + b*x + c*x**2)**(3/4))` | $\frac{1}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((d + e*x)**2*(a + b*x + c*x**2)**(3/4))` | $\frac{1}{\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `1/((d + e*x)**3*(a + b*x + c*x**2)**(3/4))` | $\frac{1}{\left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{4}}}$ |
| partial | parametric | `(d + e*x)**3/(a + b*x + c*x**2)**(5/4)` | $\frac{\left(d + e x\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(d + e*x)**2/(a + b*x + c*x**2)**(5/4)` | $\frac{\left(d + e x\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(d + e*x)/(a + b*x + c*x**2)**(5/4)` | $\frac{d + e x}{\left(a + b x + c x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(-5/4)` | $\frac{1}{\left(a + b x + c x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((d + e*x)*(a + b*x + c*x**2)**(5/4))` | $\frac{1}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((d + e*x)**2*(a + b*x + c*x**2)**(5/4))` | $\frac{1}{\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{5}{4}}}$ |
| partial | parametric | `1/((d + e*x)**(3/2)*(a + b*x + c*x**2)**(1/4))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \sqrt[4]{a + b x + c x^{2}}}$ |
| partial | concrete | `1/((x + 1)**(1/3)*(x**2 - x + 1)**(1/3))` | $\frac{1}{\sqrt[3]{x + 1} \sqrt[3]{x^{2} - x + 1}}$ |
| partial | concrete | `1/((x + 1)**(2/3)*(x**2 - x + 1)**(2/3))` | $\frac{1}{\left(x + 1\right)^{\frac{2}{3}} \left(x^{2} - x + 1\right)^{\frac{2}{3}}}$ |
| partial | concrete | `1/((1 - x)**(1/3)*(x**2 + x + 1)**(1/3))` | $\frac{1}{\sqrt[3]{1 - x} \sqrt[3]{x^{2} + x + 1}}$ |
| partial | concrete | `1/((1 - x)**(2/3)*(x**2 + x + 1)**(2/3))` | $\frac{1}{\left(1 - x\right)^{\frac{2}{3}} \left(x^{2} + x + 1\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/((b*e - c*e*x)**(1/3)*(b**2 + b*c*x + c**2*x**2)**(1/3))` | $\frac{1}{\sqrt[3]{b e - c e x} \sqrt[3]{b^{2} + b c x + c^{2} x^{2}}}$ |
| partial | parametric | `1/((b*e - c*e*x)**(2/3)*(b**2 + b*c*x + c**2*x**2)**(2/3))` | $\frac{1}{\left(b e - c e x\right)^{\frac{2}{3}} \left(b^{2} + b c x + c^{2} x^{2}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `x**3*(A + B*x)*sqrt(b*x + c*x**2)` | $x^{3} \left(A + B x\right) \sqrt{b x + c x^{2}}$ |
| partial | parametric | `x**2*(A + B*x)*sqrt(b*x + c*x**2)` | $x^{2} \left(A + B x\right) \sqrt{b x + c x^{2}}$ |
| partial | parametric | `x*(A + B*x)*sqrt(b*x + c*x**2)` | $x \left(A + B x\right) \sqrt{b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)` | $\left(A + B x\right) \sqrt{b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/x` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{x}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/x**2` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/x**3` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{x^{3}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/x**4` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{x^{4}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/x**5` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/x**6` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/x**7` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/x**8` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{x^{8}}$ |
| partial | parametric | `x**3*(A + B*x)*(b*x + c*x**2)**(3/2)` | $x^{3} \left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(A + B*x)*(b*x + c*x**2)**(3/2)` | $x^{2} \left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(A + B*x)*(b*x + c*x**2)**(3/2)` | $x \left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)` | $\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**2` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**3` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**4` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**5` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**6` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**7` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**8` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**9` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**10` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{10}}$ |
| partial | parametric | `x**3*(A + B*x)*(b*x + c*x**2)**(5/2)` | $x^{3} \left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**2*(A + B*x)*(b*x + c*x**2)**(5/2)` | $x^{2} \left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x*(A + B*x)*(b*x + c*x**2)**(5/2)` | $x \left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)` | $\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**2` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**3` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**4` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**5` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**6` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**7` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**8` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**9` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**10` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{10}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**11` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**12` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{12}}$ |
| partial | parametric | `x**4*(A + B*x)/sqrt(b*x + c*x**2)` | $\frac{x^{4} \left(A + B x\right)}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `x**3*(A + B*x)/sqrt(b*x + c*x**2)` | $\frac{x^{3} \left(A + B x\right)}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `x**2*(A + B*x)/sqrt(b*x + c*x**2)` | $\frac{x^{2} \left(A + B x\right)}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `x*(A + B*x)/sqrt(b*x + c*x**2)` | $\frac{x \left(A + B x\right)}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/sqrt(b*x + c*x**2)` | $\frac{A + B x}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x*sqrt(b*x + c*x**2))` | $\frac{A + B x}{x \sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(x**2*sqrt(b*x + c*x**2))` | $\frac{A + B x}{x^{2} \sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(x**3*sqrt(b*x + c*x**2))` | $\frac{A + B x}{x^{3} \sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(x**4*sqrt(b*x + c*x**2))` | $\frac{A + B x}{x^{4} \sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(x**5*sqrt(b*x + c*x**2))` | $\frac{A + B x}{x^{5} \sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(x**6*sqrt(b*x + c*x**2))` | $\frac{A + B x}{x^{6} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `x**4*(A + B*x)/(b*x + c*x**2)**(3/2)` | $\frac{x^{4} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*(A + B*x)/(b*x + c*x**2)**(3/2)` | $\frac{x^{3} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(A + B*x)/(b*x + c*x**2)**(3/2)` | $\frac{x^{2} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(A + B*x)/(b*x + c*x**2)**(3/2)` | $\frac{x \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(b*x + c*x**2)**(3/2)` | $\frac{A + B x}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(x*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{x \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(x**2*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{x^{2} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(x**3*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{x^{3} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(x**4*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{x^{4} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5*(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{x^{5} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4*(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{x^{4} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3*(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{x^{3} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{x^{2} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{x \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{A + B x}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(x*(b*x + c*x**2)**(5/2))` | $\frac{A + B x}{x \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(x**2*(b*x + c*x**2)**(5/2))` | $\frac{A + B x}{x^{2} \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)/(x**3*(b*x + c*x**2)**(5/2))` | $\frac{A + B x}{x^{3} \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(b*x + c*x**2)**(7/2)` | $\frac{d + e x}{\left(b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(b*x + c*x**2)**(9/2)` | $\frac{d + e x}{\left(b x + c x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(b*x + c*x**2)` | $x^{\frac{7}{2}} \left(A + B x\right) \left(b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(b*x + c*x**2)` | $x^{\frac{5}{2}} \left(A + B x\right) \left(b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(b*x + c*x**2)` | $x^{\frac{3}{2}} \left(A + B x\right) \left(b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(b*x + c*x**2)` | $\sqrt{x} \left(A + B x\right) \left(b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)/sqrt(x)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)/x**(3/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)/x**(5/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)/x**(7/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)/x**(9/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(b*x + c*x**2)**2` | $x^{\frac{7}{2}} \left(A + B x\right) \left(b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(b*x + c*x**2)**2` | $x^{\frac{5}{2}} \left(A + B x\right) \left(b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(b*x + c*x**2)**2` | $x^{\frac{3}{2}} \left(A + B x\right) \left(b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(b*x + c*x**2)**2` | $\sqrt{x} \left(A + B x\right) \left(b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**2/sqrt(x)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**2/x**(3/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**2/x**(5/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**2/x**(7/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**2/x**(9/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{2}}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(b*x + c*x**2)**3` | $x^{\frac{7}{2}} \left(A + B x\right) \left(b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(b*x + c*x**2)**3` | $x^{\frac{5}{2}} \left(A + B x\right) \left(b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(b*x + c*x**2)**3` | $x^{\frac{3}{2}} \left(A + B x\right) \left(b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(b*x + c*x**2)**3` | $\sqrt{x} \left(A + B x\right) \left(b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**3/sqrt(x)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**3/x**(3/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**3/x**(5/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**3/x**(7/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{3}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**3/x**(9/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{3}}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**3/x**(11/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{3}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(b*x + c*x**2)` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{b x + c x^{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(b*x + c*x**2)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{b x + c x^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(b*x + c*x**2)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{b x + c x^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(b*x + c*x**2)` | $\frac{\sqrt{x} \left(A + B x\right)}{b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(b*x + c*x**2))` | $\frac{A + B x}{\sqrt{x} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(b*x + c*x**2))` | $\frac{A + B x}{x^{\frac{3}{2}} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(b*x + c*x**2))` | $\frac{A + B x}{x^{\frac{5}{2}} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(7/2)*(b*x + c*x**2))` | $\frac{A + B x}{x^{\frac{7}{2}} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(9/2)*(b*x + c*x**2))` | $\frac{A + B x}{x^{\frac{9}{2}} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `x**(9/2)*(A + B*x)/(b*x + c*x**2)**2` | $\frac{x^{\frac{9}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(b*x + c*x**2)**2` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(b*x + c*x**2)**2` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(b*x + c*x**2)**2` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(b*x + c*x**2)**2` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(b*x + c*x**2)**2)` | $\frac{A + B x}{\sqrt{x} \left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(b*x + c*x**2)**2)` | $\frac{A + B x}{x^{\frac{3}{2}} \left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(b*x + c*x**2)**2)` | $\frac{A + B x}{x^{\frac{5}{2}} \left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `x**(13/2)*(A + B*x)/(b*x + c*x**2)**3` | $\frac{x^{\frac{13}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `x**(11/2)*(A + B*x)/(b*x + c*x**2)**3` | $\frac{x^{\frac{11}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `x**(9/2)*(A + B*x)/(b*x + c*x**2)**3` | $\frac{x^{\frac{9}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(b*x + c*x**2)**3` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(b*x + c*x**2)**3` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(b*x + c*x**2)**3` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(b*x + c*x**2)**3` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(b*x + c*x**2)**3)` | $\frac{A + B x}{\sqrt{x} \left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(b*x + c*x**2)**3)` | $\frac{A + B x}{x^{\frac{3}{2}} \left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)*sqrt(b*x + c*x**2)` | $x^{\frac{7}{2}} \left(A + B x\right) \sqrt{b x + c x^{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)*sqrt(b*x + c*x**2)` | $x^{\frac{5}{2}} \left(A + B x\right) \sqrt{b x + c x^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)*sqrt(b*x + c*x**2)` | $x^{\frac{3}{2}} \left(A + B x\right) \sqrt{b x + c x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(x)*(A + B*x)*sqrt(b*x + c*x**2)` | $\sqrt{x} \left(A + B x\right) \sqrt{b x + c x^{2}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/sqrt(x)` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{\sqrt{x}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/x**(3/2)` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/x**(5/2)` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/x**(7/2)` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/x**(9/2)` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)*(b*x + c*x**2)**(3/2)` | $x^{\frac{5}{2}} \left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)*(b*x + c*x**2)**(3/2)` | $x^{\frac{3}{2}} \left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)*(b*x + c*x**2)**(3/2)` | $\sqrt{x} \left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/sqrt(x)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**(3/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**(5/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**(7/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**(9/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**(11/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**(13/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{13}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**(15/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{x^{\frac{15}{2}}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)*(b*x + c*x**2)**(5/2)` | $x^{\frac{3}{2}} \left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)*(b*x + c*x**2)**(5/2)` | $\sqrt{x} \left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/sqrt(x)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{\sqrt{x}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**(3/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**(5/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**(7/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**(9/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**(11/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**(13/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{\frac{13}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**(15/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{\frac{15}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**(17/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{x^{\frac{17}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/sqrt(b*x + c*x**2)` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/sqrt(b*x + c*x**2)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(3/2)*(A + B*x)/sqrt(b*x + c*x**2)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\sqrt{b x + c x^{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(x)*(A + B*x)/sqrt(b*x + c*x**2)` | $\frac{\sqrt{x} \left(A + B x\right)}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(e*x)*sqrt(b*x + c*x**2))` | $\frac{A + B x}{\sqrt{e x} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*sqrt(b*x + c*x**2))` | $\frac{A + B x}{x^{\frac{3}{2}} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*sqrt(b*x + c*x**2))` | $\frac{A + B x}{x^{\frac{5}{2}} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(7/2)*sqrt(b*x + c*x**2))` | $\frac{A + B x}{x^{\frac{7}{2}} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `x**(9/2)*(A + B*x)/(b*x + c*x**2)**(3/2)` | $\frac{x^{\frac{9}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(b*x + c*x**2)**(3/2)` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(5/2)*(A + B*x)/(b*x + c*x**2)**(3/2)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(3/2)*(A + B*x)/(b*x + c*x**2)**(3/2)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(b*x + c*x**2)**(3/2)` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\sqrt{x} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{x^{\frac{3}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{x^{\frac{5}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(7/2)*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{x^{\frac{7}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(11/2)*(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{x^{\frac{11}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(9/2)*(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{x^{\frac{9}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(7/2)*(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**(5/2)*(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(b*x + c*x**2)**(5/2))` | $\frac{A + B x}{\sqrt{x} \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(b*x + c*x**2)**(5/2))` | $\frac{A + B x}{x^{\frac{3}{2}} \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4*(A + B*x)*sqrt(a + c*x**2)` | $x^{4} \left(A + B x\right) \sqrt{a + c x^{2}}$ |
| partial | parametric | `x**3*(A + B*x)*sqrt(a + c*x**2)` | $x^{3} \left(A + B x\right) \sqrt{a + c x^{2}}$ |
| partial | parametric | `x**2*(A + B*x)*sqrt(a + c*x**2)` | $x^{2} \left(A + B x\right) \sqrt{a + c x^{2}}$ |
| partial | parametric | `x*(A + B*x)*sqrt(a + c*x**2)` | $x \left(A + B x\right) \sqrt{a + c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)` | $\left(A + B x\right) \sqrt{a + c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/x` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{x}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/x**2` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/x**3` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/x**4` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/x**5` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/x**6` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/x**7` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{x^{7}}$ |
| partial | parametric | `x**4*(A + B*x)*(a + c*x**2)**(3/2)` | $x^{4} \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**3*(A + B*x)*(a + c*x**2)**(3/2)` | $x^{3} \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(A + B*x)*(a + c*x**2)**(3/2)` | $x^{2} \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(A + B*x)*(a + c*x**2)**(3/2)` | $x \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)` | $\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/x` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/x**2` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/x**3` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/x**4` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/x**5` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/x**6` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/x**7` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/x**8` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{x^{8}}$ |
| partial | parametric | `x**4*(A + B*x)*(a + c*x**2)**(5/2)` | $x^{4} \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**3*(A + B*x)*(a + c*x**2)**(5/2)` | $x^{3} \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**2*(A + B*x)*(a + c*x**2)**(5/2)` | $x^{2} \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x*(A + B*x)*(a + c*x**2)**(5/2)` | $x \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)` | $\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/x` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/x**2` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/x**3` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/x**4` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/x**5` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/x**6` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/x**7` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{x^{7}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/x**8` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{x^{8}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/x**9` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{x^{9}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/x**10` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{x^{10}}$ |
| partial | parametric | `x**4*(A + B*x)/sqrt(a + c*x**2)` | $\frac{x^{4} \left(A + B x\right)}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `x**3*(A + B*x)/sqrt(a + c*x**2)` | $\frac{x^{3} \left(A + B x\right)}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `x**2*(A + B*x)/sqrt(a + c*x**2)` | $\frac{x^{2} \left(A + B x\right)}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `x*(A + B*x)/sqrt(a + c*x**2)` | $\frac{x \left(A + B x\right)}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/sqrt(a + c*x**2)` | $\frac{A + B x}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x*sqrt(a + c*x**2))` | $\frac{A + B x}{x \sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*sqrt(a + c*x**2))` | $\frac{A + B x}{x^{2} \sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*sqrt(a + c*x**2))` | $\frac{A + B x}{x^{3} \sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**4*sqrt(a + c*x**2))` | $\frac{A + B x}{x^{4} \sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**5*sqrt(a + c*x**2))` | $\frac{A + B x}{x^{5} \sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**6*sqrt(a + c*x**2))` | $\frac{A + B x}{x^{6} \sqrt{a + c x^{2}}}$ |
| partial | parametric | `x**4*(A + B*x)/(a + c*x**2)**(3/2)` | $\frac{x^{4} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*(A + B*x)/(a + c*x**2)**(3/2)` | $\frac{x^{3} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(A + B*x)/(a + c*x**2)**(3/2)` | $\frac{x^{2} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(A + B*x)/(a + c*x**2)**(3/2)` | $\frac{x \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a + c*x**2)**(3/2)` | $\frac{A + B x}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x*(a + c*x**2)**(3/2))` | $\frac{A + B x}{x \left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*(a + c*x**2)**(3/2))` | $\frac{A + B x}{x^{2} \left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*(a + c*x**2)**(3/2))` | $\frac{A + B x}{x^{3} \left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**4*(a + c*x**2)**(3/2))` | $\frac{A + B x}{x^{4} \left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4*(A + B*x)/(a + c*x**2)**(5/2)` | $\frac{x^{4} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3*(A + B*x)/(a + c*x**2)**(5/2)` | $\frac{x^{3} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)/(a + c*x**2)**(5/2)` | $\frac{x^{2} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x)/(a + c*x**2)**(5/2)` | $\frac{x \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a + c*x**2)**(5/2)` | $\frac{A + B x}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x*(a + c*x**2)**(5/2))` | $\frac{A + B x}{x \left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*(a + c*x**2)**(5/2))` | $\frac{A + B x}{x^{2} \left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*(a + c*x**2)**(5/2))` | $\frac{A + B x}{x^{3} \left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(a + c*x**2)**(7/2)` | $\frac{d + e x}{\left(a + c x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(a + c*x**2)**(9/2)` | $\frac{d + e x}{\left(a + c x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(a + c*x**2)` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a + c x^{2}\right)$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(a + c*x**2)` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a + c x^{2}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(a + c*x**2)` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a + c x^{2}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(a + c*x**2)` | $\sqrt{x} \left(A + B x\right) \left(a + c x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)/sqrt(x)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)/x**(3/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)/x**(5/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)/x**(7/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)/x**(9/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(a + c*x**2)**2` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(a + c*x**2)**2` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(a + c*x**2)**2` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(a + c*x**2)**2` | $\sqrt{x} \left(A + B x\right) \left(a + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**2/sqrt(x)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**2/x**(3/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**2/x**(5/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**2/x**(7/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**2/x**(9/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{2}}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(a + c*x**2)**3` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(a + c*x**2)**3` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(a + c*x**2)**3` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(a + c*x**2)**3` | $\sqrt{x} \left(A + B x\right) \left(a + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**3/sqrt(x)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**3/x**(3/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**3/x**(5/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**3/x**(7/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{3}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**3/x**(9/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{3}}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**3/x**(11/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{3}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a + c*x**2)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{a + c x^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a + c*x**2)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{a + c x^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a + c*x**2)` | $\frac{\sqrt{x} \left(A + B x\right)}{a + c x^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a + c*x**2))` | $\frac{A + B x}{\sqrt{x} \left(a + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a + c*x**2))` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(a + c*x**2))` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(7/2)*(a + c*x**2))` | $\frac{A + B x}{x^{\frac{7}{2}} \left(a + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(9/2)*(a + c*x**2))` | $\frac{A + B x}{x^{\frac{9}{2}} \left(a + c x^{2}\right)}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a + c*x**2)**2` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a + c*x**2)**2` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a + c*x**2)**2` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(a + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a + c*x**2)**2)` | $\frac{A + B x}{\sqrt{x} \left(a + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a + c*x**2)**2)` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(a + c*x**2)**2)` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a + c x^{2}\right)^{2}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(a + c*x**2)**3` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{3}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a + c*x**2)**3` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{3}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a + c*x**2)**3` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a + c*x**2)**3` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(a + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a + c*x**2)**3)` | $\frac{A + B x}{\sqrt{x} \left(a + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a + c*x**2)**3)` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a + c x^{2}\right)^{3}}$ |
| partial | concrete | `(1 - x)/(sqrt(x)*(x**2 + 1))` | $\frac{1 - x}{\sqrt{x} \left(x^{2} + 1\right)}$ |
| partial | parametric | `(e*x)**(7/2)*(A + B*x)*sqrt(a + c*x**2)` | $\left(e x\right)^{\frac{7}{2}} \left(A + B x\right) \sqrt{a + c x^{2}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x)*sqrt(a + c*x**2)` | $\left(e x\right)^{\frac{5}{2}} \left(A + B x\right) \sqrt{a + c x^{2}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x)*sqrt(a + c*x**2)` | $\left(e x\right)^{\frac{3}{2}} \left(A + B x\right) \sqrt{a + c x^{2}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x)*sqrt(a + c*x**2)` | $\sqrt{e x} \left(A + B x\right) \sqrt{a + c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/sqrt(e*x)` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{\sqrt{e x}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/(e*x)**(3/2)` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{\left(e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/(e*x)**(5/2)` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{\left(e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/(e*x)**(7/2)` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{\left(e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/(e*x)**(9/2)` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{\left(e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x)*(a + c*x**2)**(3/2)` | $\left(e x\right)^{\frac{5}{2}} \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x)*(a + c*x**2)**(3/2)` | $\left(e x\right)^{\frac{3}{2}} \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x)*(a + c*x**2)**(3/2)` | $\sqrt{e x} \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/sqrt(e*x)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{\sqrt{e x}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/(e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/(e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/(e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/(e*x)**(9/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x)*(a + c*x**2)**(5/2)` | $\left(e x\right)^{\frac{3}{2}} \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x)*(a + c*x**2)**(5/2)` | $\sqrt{e x} \left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/sqrt(e*x)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{\sqrt{e x}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/(e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/(e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/(e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/(e*x)**(9/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(5/2)/(e*x)**(11/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{5}{2}}}{\left(e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*(A + B*x)/sqrt(a + c*x**2)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(A + B x\right)}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x)/sqrt(a + c*x**2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(A + B x\right)}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x)/sqrt(a + c*x**2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(A + B x\right)}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x)/sqrt(a + c*x**2)` | $\frac{\sqrt{e x} \left(A + B x\right)}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(e*x)*sqrt(a + c*x**2))` | $\frac{A + B x}{\sqrt{e x} \sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((e*x)**(3/2)*sqrt(a + c*x**2))` | $\frac{A + B x}{\left(e x\right)^{\frac{3}{2}} \sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((e*x)**(5/2)*sqrt(a + c*x**2))` | $\frac{A + B x}{\left(e x\right)^{\frac{5}{2}} \sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((e*x)**(7/2)*sqrt(a + c*x**2))` | $\frac{A + B x}{\left(e x\right)^{\frac{7}{2}} \sqrt{a + c x^{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*(A + B*x)/(a + c*x**2)**(3/2)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x)/(a + c*x**2)**(3/2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x)/(a + c*x**2)**(3/2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x)/(a + c*x**2)**(3/2)` | $\frac{\sqrt{e x} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(e*x)*(a + c*x**2)**(3/2))` | $\frac{A + B x}{\sqrt{e x} \left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((e*x)**(3/2)*(a + c*x**2)**(3/2))` | $\frac{A + B x}{\left(e x\right)^{\frac{3}{2}} \left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((e*x)**(5/2)*(a + c*x**2)**(3/2))` | $\frac{A + B x}{\left(e x\right)^{\frac{5}{2}} \left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((e*x)**(7/2)*(a + c*x**2)**(3/2))` | $\frac{A + B x}{\left(e x\right)^{\frac{7}{2}} \left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(e*x)**(13/2)*(A + B*x)/(a + c*x**2)**(5/2)` | $\frac{\left(e x\right)^{\frac{13}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(11/2)*(A + B*x)/(a + c*x**2)**(5/2)` | $\frac{\left(e x\right)^{\frac{11}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(9/2)*(A + B*x)/(a + c*x**2)**(5/2)` | $\frac{\left(e x\right)^{\frac{9}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(7/2)*(A + B*x)/(a + c*x**2)**(5/2)` | $\frac{\left(e x\right)^{\frac{7}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(5/2)*(A + B*x)/(a + c*x**2)**(5/2)` | $\frac{\left(e x\right)^{\frac{5}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(e*x)**(3/2)*(A + B*x)/(a + c*x**2)**(5/2)` | $\frac{\left(e x\right)^{\frac{3}{2}} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(e*x)*(A + B*x)/(a + c*x**2)**(5/2)` | $\frac{\sqrt{e x} \left(A + B x\right)}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(e*x)*(a + c*x**2)**(5/2))` | $\frac{A + B x}{\sqrt{e x} \left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((e*x)**(3/2)*(a + c*x**2)**(5/2))` | $\frac{A + B x}{\left(e x\right)^{\frac{3}{2}} \left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((e*x)**(5/2)*(a + c*x**2)**(5/2))` | $\frac{A + B x}{\left(e x\right)^{\frac{5}{2}} \left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((e*x)**(7/2)*(a + c*x**2)**(5/2))` | $\frac{A + B x}{\left(e x\right)^{\frac{7}{2}} \left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x^{4} \left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x^{3} \left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x^{2} \left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `x*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x \left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x}$ |
| partial | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**2` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**3` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{3}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**4` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{4}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**5` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**6` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**7` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{7}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $x^{5} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $x^{4} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $x^{3} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $x^{2} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $x \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**2` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**3` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**4` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**5` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**6` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**7` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**8` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**9` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**10` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{10}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**11` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**12` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{12}}$ |
| SOLVED-both | parametric | `x**6*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x^{6} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**5*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x^{5} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x^{4} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x^{3} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x^{2} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `x*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**2` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**3` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**4` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**5` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**6` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**7` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**8` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**9` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**10` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{10}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**11` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**12` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{12}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**13` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{13}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**14` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{14}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x^{4} \left(A + B x\right)}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x^{3} \left(A + B x\right)}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x^{2} \left(A + B x\right)}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x \left(A + B x\right)}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{A + B x}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x^{2} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x^{3} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**4*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x^{4} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**5*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x^{5} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{x^{4} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{x^{3} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{x^{2} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{x \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{A + B x}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{x \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{x^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{x^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**4*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{4} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**3*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{3} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{2} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{A + B x}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{x \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{x^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)` | $\sqrt{x} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)/sqrt(x)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)/x**(3/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)/x**(5/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)/x**(7/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)/x**(9/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\sqrt{x} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/sqrt(x)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/x**(3/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/x**(5/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/x**(7/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/x**(9/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\sqrt{x} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/sqrt(x)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/x**(3/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/x**(5/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/x**(7/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/x**(9/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/x**(11/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\sqrt{x} \left(A + B x\right)}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\sqrt{x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(7/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(9/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x^{\frac{9}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{A + B x}{\sqrt{x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `x**(11/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{x^{\frac{11}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `x**(9/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{x^{\frac{9}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{A + B x}{\sqrt{x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `x**(7/2)*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x^{\frac{7}{2}} \left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `x**(5/2)*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x^{\frac{5}{2}} \left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `x**(3/2)*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x^{\frac{3}{2}} \left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(x)*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\sqrt{x} \left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/sqrt(x)` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\sqrt{x}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**(3/2)` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**(5/2)` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**(7/2)` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**(9/2)` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\sqrt{x} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/sqrt(x)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**(3/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**(5/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**(7/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**(9/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\sqrt{x} \left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/sqrt(x)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**(3/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**(5/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**(7/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**(9/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\sqrt{x} \left(A + B x\right)}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\sqrt{x} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x^{\frac{3}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x^{\frac{5}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(7/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x^{\frac{7}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(9/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{x^{\frac{9}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{\sqrt{x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{x^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(11/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{\frac{11}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(9/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{\frac{9}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{\sqrt{x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{x^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4*(A + B*x)*sqrt(a + b*x + c*x**2)` | $x^{4} \left(A + B x\right) \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `x**3*(A + B*x)*sqrt(a + b*x + c*x**2)` | $x^{3} \left(A + B x\right) \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `x**2*(A + B*x)*sqrt(a + b*x + c*x**2)` | $x^{2} \left(A + B x\right) \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `x*(A + B*x)*sqrt(a + b*x + c*x**2)` | $x \left(A + B x\right) \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)` | $\left(A + B x\right) \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/x` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{x}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/x**2` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/x**3` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/x**4` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/x**5` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/x**6` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/x**7` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{x^{7}}$ |
| partial | parametric | `x**4*(A + B*x)*(a + b*x + c*x**2)**(3/2)` | $x^{4} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**3*(A + B*x)*(a + b*x + c*x**2)**(3/2)` | $x^{3} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(A + B*x)*(a + b*x + c*x**2)**(3/2)` | $x^{2} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(A + B*x)*(a + b*x + c*x**2)**(3/2)` | $x \left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(3/2)` | $\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(3/2)/x` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(3/2)/x**2` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(3/2)/x**3` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(3/2)/x**4` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(3/2)/x**5` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(3/2)/x**6` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(3/2)/x**7` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(3/2)/x**8` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{x^{8}}$ |
| partial | parametric | `x**4*(A + B*x)*(a + b*x + c*x**2)**(5/2)` | $x^{4} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**3*(A + B*x)*(a + b*x + c*x**2)**(5/2)` | $x^{3} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**2*(A + B*x)*(a + b*x + c*x**2)**(5/2)` | $x^{2} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x*(A + B*x)*(a + b*x + c*x**2)**(5/2)` | $x \left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(5/2)` | $\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(5/2)/x` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(5/2)/x**2` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(5/2)/x**3` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(5/2)/x**4` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(5/2)/x**5` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{x^{5}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(5/2)/x**6` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{x^{6}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(5/2)/x**7` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{x^{7}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(5/2)/x**8` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{x^{8}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(5/2)/x**9` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{x^{9}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(5/2)/x**10` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{x^{10}}$ |
| partial | parametric | `x**4*(A + B*x)/sqrt(a + b*x + c*x**2)` | $\frac{x^{4} \left(A + B x\right)}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `x**3*(A + B*x)/sqrt(a + b*x + c*x**2)` | $\frac{x^{3} \left(A + B x\right)}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `x**2*(A + B*x)/sqrt(a + b*x + c*x**2)` | $\frac{x^{2} \left(A + B x\right)}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `x*(A + B*x)/sqrt(a + b*x + c*x**2)` | $\frac{x \left(A + B x\right)}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/sqrt(a + b*x + c*x**2)` | $\frac{A + B x}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{x \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{x^{2} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{x^{3} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**4*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{x^{4} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**5*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{x^{5} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(x**6*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{x^{6} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `x**4*(A + B*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{x^{4} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3*(A + B*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{x^{3} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(A + B*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{x^{2} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(A + B*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{x \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{A + B x}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x*(a + b*x + c*x**2)**(3/2))` | $\frac{A + B x}{x \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*(a + b*x + c*x**2)**(3/2))` | $\frac{A + B x}{x^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*(a + b*x + c*x**2)**(3/2))` | $\frac{A + B x}{x^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**4*(a + b*x + c*x**2)**(3/2))` | $\frac{A + B x}{x^{4} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4*(A + B*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{x^{4} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3*(A + B*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{x^{3} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x**2*(A + B*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{x^{2} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `x*(A + B*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{x \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{A + B x}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x*(a + b*x + c*x**2)**(5/2))` | $\frac{A + B x}{x \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**2*(a + b*x + c*x**2)**(5/2))` | $\frac{A + B x}{x^{2} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(x**3*(a + b*x + c*x**2)**(5/2))` | $\frac{A + B x}{x^{3} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(a + b*x + c*x**2)**(7/2)` | $\frac{d + e x}{\left(a + b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(a + b*x + c*x**2)**(9/2)` | $\frac{d + e x}{\left(a + b x + c x^{2}\right)^{\frac{9}{2}}}$ |
| partial | concrete | `(1 - x)/(x*sqrt(x**2 + 3*x + 1))` | $\frac{1 - x}{x \sqrt{x^{2} + 3 x + 1}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(a + b*x + c*x**2)` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(a + b*x + c*x**2)` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(a + b*x + c*x**2)` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(a + b*x + c*x**2)` | $\sqrt{x} \left(A + B x\right) \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)/sqrt(x)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)/x**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)/x**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)/x**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)/x**(9/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(a + b*x + c*x**2)**2` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(a + b*x + c*x**2)**2` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(a + b*x + c*x**2)**2` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(a + b*x + c*x**2)**2` | $\sqrt{x} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)**2/sqrt(x)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)**2/x**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)**2/x**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)**2/x**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)**2/x**(9/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{2}}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(A + B*x)*(a + b*x + c*x**2)**3` | $x^{\frac{7}{2}} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(5/2)*(A + B*x)*(a + b*x + c*x**2)**3` | $x^{\frac{5}{2}} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(A + B*x)*(a + b*x + c*x**2)**3` | $x^{\frac{3}{2}} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(A + B*x)*(a + b*x + c*x**2)**3` | $\sqrt{x} \left(A + B x\right) \left(a + b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)**3/sqrt(x)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)**3/x**(3/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)**3/x**(5/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)**3/x**(7/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{3}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)**3/x**(9/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{3}}{x^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + b*x + c*x**2)**3/x**(11/2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{3}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a + b*x + c*x**2)` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{a + b x + c x^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a + b*x + c*x**2)` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a + b*x + c*x**2)` | $\frac{\sqrt{x} \left(A + B x\right)}{a + b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a + b*x + c*x**2))` | $\frac{A + B x}{\sqrt{x} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a + b*x + c*x**2))` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(a + b*x + c*x**2))` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(7/2)*(a + b*x + c*x**2))` | $\frac{A + B x}{x^{\frac{7}{2}} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/(x**(9/2)*(a + b*x + c*x**2))` | $\frac{A + B x}{x^{\frac{9}{2}} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a + b*x + c*x**2)**2` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a + b*x + c*x**2)**2` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a + b*x + c*x**2)**2` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a + b*x + c*x**2)**2)` | $\frac{A + B x}{\sqrt{x} \left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a + b*x + c*x**2)**2)` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(x**(5/2)*(a + b*x + c*x**2)**2)` | $\frac{A + B x}{x^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `x**(7/2)*(A + B*x)/(a + b*x + c*x**2)**3` | $\frac{x^{\frac{7}{2}} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `x**(5/2)*(A + B*x)/(a + b*x + c*x**2)**3` | $\frac{x^{\frac{5}{2}} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `x**(3/2)*(A + B*x)/(a + b*x + c*x**2)**3` | $\frac{x^{\frac{3}{2}} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)/(a + b*x + c*x**2)**3` | $\frac{\sqrt{x} \left(A + B x\right)}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(sqrt(x)*(a + b*x + c*x**2)**3)` | $\frac{A + B x}{\sqrt{x} \left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(x**(3/2)*(a + b*x + c*x**2)**3)` | $\frac{A + B x}{x^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `sqrt(x)*(A + B*x)*sqrt(a + b*x + c*x**2)` | $\sqrt{x} \left(A + B x\right) \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/sqrt(x)` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{\sqrt{x}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/x**(3/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/x**(5/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/x**(7/2)` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{x^{\frac{7}{2}}}$ |
| partial | concrete | `x**(7/2)*(2 - 5*x)*sqrt(3*x**2 + 5*x + 2)` | $x^{\frac{7}{2}} \left(2 - 5 x\right) \sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `x**(5/2)*(2 - 5*x)*sqrt(3*x**2 + 5*x + 2)` | $x^{\frac{5}{2}} \left(2 - 5 x\right) \sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `x**(3/2)*(2 - 5*x)*sqrt(3*x**2 + 5*x + 2)` | $x^{\frac{3}{2}} \left(2 - 5 x\right) \sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `sqrt(x)*(2 - 5*x)*sqrt(3*x**2 + 5*x + 2)` | $\sqrt{x} \left(2 - 5 x\right) \sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(2 - 5*x)*sqrt(3*x**2 + 5*x + 2)/sqrt(x)` | $\frac{\left(2 - 5 x\right) \sqrt{3 x^{2} + 5 x + 2}}{\sqrt{x}}$ |
| partial | concrete | `(2 - 5*x)*sqrt(3*x**2 + 5*x + 2)/x**(3/2)` | $\frac{\left(2 - 5 x\right) \sqrt{3 x^{2} + 5 x + 2}}{x^{\frac{3}{2}}}$ |
| partial | concrete | `(2 - 5*x)*sqrt(3*x**2 + 5*x + 2)/x**(5/2)` | $\frac{\left(2 - 5 x\right) \sqrt{3 x^{2} + 5 x + 2}}{x^{\frac{5}{2}}}$ |
| partial | concrete | `(2 - 5*x)*sqrt(3*x**2 + 5*x + 2)/x**(7/2)` | $\frac{\left(2 - 5 x\right) \sqrt{3 x^{2} + 5 x + 2}}{x^{\frac{7}{2}}}$ |
| partial | concrete | `(2 - 5*x)*sqrt(3*x**2 + 5*x + 2)/x**(9/2)` | $\frac{\left(2 - 5 x\right) \sqrt{3 x^{2} + 5 x + 2}}{x^{\frac{9}{2}}}$ |
| partial | concrete | `(2 - 5*x)*sqrt(3*x**2 + 5*x + 2)/x**(11/2)` | $\frac{\left(2 - 5 x\right) \sqrt{3 x^{2} + 5 x + 2}}{x^{\frac{11}{2}}}$ |
| partial | concrete | `x**(5/2)*(2 - 5*x)*(3*x**2 + 5*x + 2)**(3/2)` | $x^{\frac{5}{2}} \left(2 - 5 x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `x**(3/2)*(2 - 5*x)*(3*x**2 + 5*x + 2)**(3/2)` | $x^{\frac{3}{2}} \left(2 - 5 x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(x)*(2 - 5*x)*(3*x**2 + 5*x + 2)**(3/2)` | $\sqrt{x} \left(2 - 5 x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(2 - 5*x)*(3*x**2 + 5*x + 2)**(3/2)/sqrt(x)` | $\frac{\left(2 - 5 x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| partial | concrete | `(2 - 5*x)*(3*x**2 + 5*x + 2)**(3/2)/x**(3/2)` | $\frac{\left(2 - 5 x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | concrete | `(2 - 5*x)*(3*x**2 + 5*x + 2)**(3/2)/x**(5/2)` | $\frac{\left(2 - 5 x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{x^{\frac{5}{2}}}$ |
| partial | concrete | `(2 - 5*x)*(3*x**2 + 5*x + 2)**(3/2)/x**(7/2)` | $\frac{\left(2 - 5 x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{x^{\frac{7}{2}}}$ |
| partial | concrete | `(2 - 5*x)*(3*x**2 + 5*x + 2)**(3/2)/x**(9/2)` | $\frac{\left(2 - 5 x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{x^{\frac{9}{2}}}$ |
| partial | concrete | `(2 - 5*x)*(3*x**2 + 5*x + 2)**(3/2)/x**(11/2)` | $\frac{\left(2 - 5 x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{x^{\frac{11}{2}}}$ |
| partial | concrete | `(2 - 5*x)*(3*x**2 + 5*x + 2)**(3/2)/x**(13/2)` | $\frac{\left(2 - 5 x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{x^{\frac{13}{2}}}$ |
| partial | concrete | `(2 - 5*x)*(3*x**2 + 5*x + 2)**(3/2)/x**(15/2)` | $\frac{\left(2 - 5 x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{x^{\frac{15}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(e*x)*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{\sqrt{e x} \sqrt{a + b x + c x^{2}}}$ |
| partial | concrete | `x**(7/2)*(2 - 5*x)/sqrt(3*x**2 + 5*x + 2)` | $\frac{x^{\frac{7}{2}} \left(2 - 5 x\right)}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `x**(5/2)*(2 - 5*x)/sqrt(3*x**2 + 5*x + 2)` | $\frac{x^{\frac{5}{2}} \left(2 - 5 x\right)}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `x**(3/2)*(2 - 5*x)/sqrt(3*x**2 + 5*x + 2)` | $\frac{x^{\frac{3}{2}} \left(2 - 5 x\right)}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `sqrt(x)*(2 - 5*x)/sqrt(3*x**2 + 5*x + 2)` | $\frac{\sqrt{x} \left(2 - 5 x\right)}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(2 - 5*x)/(sqrt(x)*sqrt(3*x**2 + 5*x + 2))` | $\frac{2 - 5 x}{\sqrt{x} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(2 - 5*x)/(x**(3/2)*sqrt(3*x**2 + 5*x + 2))` | $\frac{2 - 5 x}{x^{\frac{3}{2}} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(2 - 5*x)/(x**(5/2)*sqrt(3*x**2 + 5*x + 2))` | $\frac{2 - 5 x}{x^{\frac{5}{2}} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(2 - 5*x)/(x**(7/2)*sqrt(3*x**2 + 5*x + 2))` | $\frac{2 - 5 x}{x^{\frac{7}{2}} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `x**(7/2)*(2 - 5*x)/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{x^{\frac{7}{2}} \left(2 - 5 x\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**(5/2)*(2 - 5*x)/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{x^{\frac{5}{2}} \left(2 - 5 x\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**(3/2)*(2 - 5*x)/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{x^{\frac{3}{2}} \left(2 - 5 x\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(x)*(2 - 5*x)/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{\sqrt{x} \left(2 - 5 x\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2 - 5*x)/(sqrt(x)*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{2 - 5 x}{\sqrt{x} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2 - 5*x)/(x**(3/2)*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{2 - 5 x}{x^{\frac{3}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2 - 5*x)/(x**(5/2)*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{2 - 5 x}{x^{\frac{5}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2 - 5*x)/(x**(7/2)*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{2 - 5 x}{x^{\frac{7}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**(13/2)*(2 - 5*x)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{x^{\frac{13}{2}} \left(2 - 5 x\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x**(11/2)*(2 - 5*x)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{x^{\frac{11}{2}} \left(2 - 5 x\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x**(9/2)*(2 - 5*x)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{x^{\frac{9}{2}} \left(2 - 5 x\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x**(7/2)*(2 - 5*x)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{x^{\frac{7}{2}} \left(2 - 5 x\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x**(5/2)*(2 - 5*x)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{x^{\frac{5}{2}} \left(2 - 5 x\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x**(3/2)*(2 - 5*x)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{x^{\frac{3}{2}} \left(2 - 5 x\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(x)*(2 - 5*x)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{\sqrt{x} \left(2 - 5 x\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(2 - 5*x)/(sqrt(x)*(3*x**2 + 5*x + 2)**(5/2))` | $\frac{2 - 5 x}{\sqrt{x} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(2 - 5*x)/(x**(3/2)*(3*x**2 + 5*x + 2)**(5/2))` | $\frac{2 - 5 x}{x^{\frac{3}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(2 - 5*x)/(x**(5/2)*(3*x**2 + 5*x + 2)**(5/2))` | $\frac{2 - 5 x}{x^{\frac{5}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(2 - 5*x)/(x**(7/2)*(3*x**2 + 5*x + 2)**(5/2))` | $\frac{2 - 5 x}{x^{\frac{7}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**3*sqrt(b*x + c*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{3} \sqrt{b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**2*sqrt(b*x + c*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{2} \sqrt{b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)*sqrt(b*x + c*x**2)` | $\left(A + B x\right) \left(d + e x\right) \sqrt{b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)` | $\left(A + B x\right) \sqrt{b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/(d + e*x)` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{d + e x}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/(d + e*x)**2` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/(d + e*x)**3` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/(d + e*x)**4` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/(d + e*x)**5` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/(d + e*x)**6` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**2*(b*x + c*x**2)**(3/2)` | $\left(A + B x\right) \left(d + e x\right)^{2} \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)*(b*x + c*x**2)**(3/2)` | $\left(A + B x\right) \left(d + e x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)` | $\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/(d + e*x)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/(d + e*x)**2` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/(d + e*x)**3` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/(d + e*x)**4` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/(d + e*x)**5` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/(d + e*x)**6` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/(d + e*x)**7` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{7}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/(d + e*x)**8` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{8}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**2*(b*x + c*x**2)**(5/2)` | $\left(A + B x\right) \left(d + e x\right)^{2} \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)*(b*x + c*x**2)**(5/2)` | $\left(A + B x\right) \left(d + e x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)` | $\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/(d + e*x)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/(d + e*x)**2` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/(d + e*x)**3` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/(d + e*x)**4` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(5/2)/(d + e*x)**5` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**3/sqrt(b*x + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{3}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**2/sqrt(b*x + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{2}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)/sqrt(b*x + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/sqrt(b*x + c*x**2)` | $\frac{A + B x}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)*sqrt(b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right) \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**2*sqrt(b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{2} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**3*sqrt(b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{3} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**4*sqrt(b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{4} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**3/(b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{3}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**2/(b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{2}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)/(b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(b*x + c*x**2)**(3/2)` | $\frac{A + B x}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**2*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right)^{2} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**3*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right)^{3} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**4/(b*x + c*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{4}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**3/(b*x + c*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{3}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**2/(b*x + c*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{2}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)/(b*x + c*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(b*x + c*x**2)**(5/2)` | $\frac{A + B x}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)*(b*x + c*x**2)**(5/2))` | $\frac{A + B x}{\left(d + e x\right) \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**2*(b*x + c*x**2)**(5/2))` | $\frac{A + B x}{\left(d + e x\right)^{2} \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(7/2)*(b*x + c*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}} \left(b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(5/2)*(b*x + c*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(3/2)*(b*x + c*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(d + e*x)*(b*x + c*x**2)` | $\left(A + B x\right) \sqrt{d + e x} \left(b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(7/2)*(b*x + c*x**2)**2` | $\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}} \left(b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(5/2)*(b*x + c*x**2)**2` | $\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(3/2)*(b*x + c*x**2)**2` | $\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(d + e*x)*(b*x + c*x**2)**2` | $\left(A + B x\right) \sqrt{d + e x} \left(b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**2/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**2/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**2/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(b*x + c*x**2)**2/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(b*x + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(b*x + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(b*x + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(b*x + c*x**2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(b*x + c*x**2))` | $\frac{A + B x}{\sqrt{d + e x} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*(b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(5/2)*(b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(7/2)*(b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{7}{2}} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(9/2)*(b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{9}{2}} \left(b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(9/2)/(b*x + c*x**2)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{9}{2}}}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(b*x + c*x**2)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(b*x + c*x**2)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(b*x + c*x**2)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(b*x + c*x**2)**2` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(b*x + c*x**2)**2)` | $\frac{A + B x}{\sqrt{d + e x} \left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*(b*x + c*x**2)**2)` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(5/2)*(b*x + c*x**2)**2)` | $\frac{A + B x}{\left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(7/2)*(b*x + c*x**2)**2)` | $\frac{A + B x}{\left(d + e x\right)^{\frac{7}{2}} \left(b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(9/2)/(b*x + c*x**2)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{9}{2}}}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(b*x + c*x**2)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(b*x + c*x**2)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(b*x + c*x**2)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(b*x + c*x**2)**3` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(b*x + c*x**2)**3)` | $\frac{A + B x}{\sqrt{d + e x} \left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*(b*x + c*x**2)**3)` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(5/2)*(b*x + c*x**2)**3)` | $\frac{A + B x}{\left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)*sqrt(b*x + c*x**2)` | $\left(A + B x\right) \sqrt{d + e x} \sqrt{b x + c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(b*x + c*x**2)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \sqrt{b x + c x^{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(b*x + c*x**2)**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/sqrt(b*x + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/sqrt(b*x + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/sqrt(b*x + c*x**2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*sqrt(b*x + c*x**2))` | $\frac{A + B x}{\sqrt{d + e x} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*sqrt(b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(5/2)*sqrt(b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(7/2)*sqrt(b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{7}{2}} \sqrt{b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\sqrt{d + e x} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(5/2)*(b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{5}{2}} \left(b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(b*x + c*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(b*x + c*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(b*x + c*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(b*x + c*x**2)**(5/2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(b*x + c*x**2)**(5/2))` | $\frac{A + B x}{\sqrt{d + e x} \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*(b*x + c*x**2)**(5/2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \left(b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4*sqrt(3*x**2 + 2)` | $\left(5 - x\right) \left(2 x + 3\right)^{4} \sqrt{3 x^{2} + 2}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3*sqrt(3*x**2 + 2)` | $\left(5 - x\right) \left(2 x + 3\right)^{3} \sqrt{3 x^{2} + 2}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**2*sqrt(3*x**2 + 2)` | $\left(5 - x\right) \left(2 x + 3\right)^{2} \sqrt{3 x^{2} + 2}$ |
| partial | concrete | `(5 - x)*(2*x + 3)*sqrt(3*x**2 + 2)` | $\left(5 - x\right) \left(2 x + 3\right) \sqrt{3 x^{2} + 2}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 2)` | $\left(5 - x\right) \sqrt{3 x^{2} + 2}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 2)/(2*x + 3)` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 2}}{2 x + 3}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 2)/(2*x + 3)**2` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 2}}{\left(2 x + 3\right)^{2}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 2)/(2*x + 3)**3` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 2}}{\left(2 x + 3\right)^{3}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 2)/(2*x + 3)**4` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 2}}{\left(2 x + 3\right)^{4}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 2)/(2*x + 3)**5` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 2}}{\left(2 x + 3\right)^{5}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 2)/(2*x + 3)**6` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 2}}{\left(2 x + 3\right)^{6}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 2)/(2*x + 3)**7` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 2}}{\left(2 x + 3\right)^{7}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4*(3*x**2 + 2)**(3/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{4} \left(3 x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3*(3*x**2 + 2)**(3/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{3} \left(3 x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**2*(3*x**2 + 2)**(3/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{2} \left(3 x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)*(3*x**2 + 2)**(3/2)` | $\left(5 - x\right) \left(2 x + 3\right) \left(3 x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(3/2)` | $\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(3/2)/(2*x + 3)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{3}{2}}}{2 x + 3}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(3/2)/(2*x + 3)**2` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(3/2)/(2*x + 3)**3` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{3}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(3/2)/(2*x + 3)**4` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{4}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(3/2)/(2*x + 3)**5` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{5}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(3/2)/(2*x + 3)**6` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{6}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(3/2)/(2*x + 3)**7` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{7}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(3/2)/(2*x + 3)**8` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{8}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4*(3*x**2 + 2)**(5/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{4} \left(3 x^{2} + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3*(3*x**2 + 2)**(5/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{3} \left(3 x^{2} + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**2*(3*x**2 + 2)**(5/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{2} \left(3 x^{2} + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)*(3*x**2 + 2)**(5/2)` | $\left(5 - x\right) \left(2 x + 3\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(5/2)` | $\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(5/2)/(2*x + 3)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}{2 x + 3}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(5/2)/(2*x + 3)**2` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(5/2)/(2*x + 3)**3` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{3}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(5/2)/(2*x + 3)**4` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{4}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(5/2)/(2*x + 3)**5` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{5}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(5/2)/(2*x + 3)**6` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{6}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(5/2)/(2*x + 3)**7` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{7}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(5/2)/(2*x + 3)**8` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{8}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(5/2)/(2*x + 3)**9` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{9}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(5/2)/(2*x + 3)**10` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{10}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 2)**(5/2)/(2*x + 3)**11` | $\frac{\left(5 - x\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{11}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4/sqrt(3*x**2 + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{4}}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3/sqrt(3*x**2 + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{3}}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**2/sqrt(3*x**2 + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{2}}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)/sqrt(3*x**2 + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(5 - x)/sqrt(3*x**2 + 2)` | $\frac{5 - x}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)*sqrt(3*x**2 + 2))` | $\frac{5 - x}{\left(2 x + 3\right) \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**2*sqrt(3*x**2 + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{2} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**3*sqrt(3*x**2 + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{3} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**4*sqrt(3*x**2 + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{4} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**5*sqrt(3*x**2 + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{5} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**6*sqrt(3*x**2 + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{6} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4/(3*x**2 + 2)**(3/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{4}}{\left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3/(3*x**2 + 2)**(3/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{3}}{\left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**2/(3*x**2 + 2)**(3/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{2}}{\left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)/(3*x**2 + 2)**(3/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)}{\left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)/(3*x**2 + 2)**(3/2)` | $\frac{5 - x}{\left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)*(3*x**2 + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right) \left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**2*(3*x**2 + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{2} \left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**3*(3*x**2 + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{3} \left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**4*(3*x**2 + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{4} \left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**5*(3*x**2 + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{5} \left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**6/(3*x**2 + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{6}}{\left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**5/(3*x**2 + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{5}}{\left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4/(3*x**2 + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{4}}{\left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3/(3*x**2 + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{3}}{\left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)**2/(3*x**2 + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{2}}{\left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)/(3*x**2 + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)}{\left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)/(3*x**2 + 2)**(5/2)` | $\frac{5 - x}{\left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)*(3*x**2 + 2)**(5/2))` | $\frac{5 - x}{\left(2 x + 3\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**2*(3*x**2 + 2)**(5/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{2} \left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**3*(3*x**2 + 2)**(5/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{3} \left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**4*(3*x**2 + 2)**(5/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{4} \left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)*(d + e*x)**(3/2)` | $\left(A + B x\right) \left(a + c x^{2}\right) \left(d + e x\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)*sqrt(d + e*x)` | $\left(A + B x\right) \left(a + c x^{2}\right) \sqrt{d + e x}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**2*sqrt(d + e*x)` | $\left(A + B x\right) \left(a + c x^{2}\right)^{2} \sqrt{d + e x}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**2/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**2/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**2/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**2/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**2/(d + e*x)**(9/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**3/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{3}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**3/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**3/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**3/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**3/(d + e*x)**(9/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a + c*x**2)**3/(d + e*x)**(11/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a - c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{a - c x^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a - c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{a - c x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a - c*x**2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{a - c x^{2}}$ |
| partial | parametric | `(A + B*x)/((a - c*x**2)*sqrt(d + e*x))` | $\frac{A + B x}{\left(a - c x^{2}\right) \sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)/((a - c*x**2)*(d + e*x)**(3/2))` | $\frac{A + B x}{\left(a - c x^{2}\right) \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((a - c*x**2)*(d + e*x)**(5/2))` | $\frac{A + B x}{\left(a - c x^{2}\right) \left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a - c*x**2)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a - c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a - c*x**2)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a - c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a - c*x**2)**2` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(a - c x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/((a - c*x**2)**2*sqrt(d + e*x))` | $\frac{A + B x}{\left(a - c x^{2}\right)^{2} \sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)/((a - c*x**2)**2*(d + e*x)**(3/2))` | $\frac{A + B x}{\left(a - c x^{2}\right)^{2} \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(a - c*x**2)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a - c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a - c*x**2)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a - c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a - c*x**2)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a - c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a - c*x**2)**3` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(a - c x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/((a - c*x**2)**3*sqrt(d + e*x))` | $\frac{A + B x}{\left(a - c x^{2}\right)^{3} \sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(-A**2*e + 2*A*B*d - B**2*e*x**2))` | $\frac{A + B x}{\sqrt{d + e x} \left(- A^{2} e + 2 A B d - B^{2} e x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/((x**2 + 1)*sqrt(e*x + (A**2*e - B**2*e)/(2*A*B)))` | $\frac{A + B x}{\left(x^{2} + 1\right) \sqrt{e x + \frac{A^{2} e - B^{2} e}{2 A B}}}$ |
| partial | parametric | `(A + B*x)/((1 - x**2)*sqrt(d + e*x))` | $\frac{A + B x}{\left(1 - x^{2}\right) \sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(x**2 + 1))` | $\frac{A + B x}{\sqrt{d + e x} \left(x^{2} + 1\right)}$ |
| partial | concrete | `(1 - x)*sqrt(x + 1)/(x**2 + 1)` | $\frac{\left(1 - x\right) \sqrt{x + 1}}{x^{2} + 1}$ |
| partial | concrete | `(x + 3)/(sqrt(3*x + 4)*(x**2 + 1))` | $\frac{x + 3}{\sqrt{3 x + 4} \left(x^{2} + 1\right)}$ |
| partial | concrete | `(1 - 3*x)/(sqrt(3*x + 4)*(x**2 + 1))` | $\frac{1 - 3 x}{\sqrt{3 x + 4} \left(x^{2} + 1\right)}$ |
| partial | concrete | `(x + 2)/(sqrt(4*x + 3)*(x**2 + 1))` | $\frac{x + 2}{\sqrt{4 x + 3} \left(x^{2} + 1\right)}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)*sqrt(d + e*x)` | $\left(A + B x\right) \sqrt{a + c x^{2}} \sqrt{d + e x}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + c*x**2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \sqrt{a + c x^{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(a + c*x**2)**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/sqrt(a + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/sqrt(a + c*x**2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(a + c*x**2)*sqrt(d + e*x))` | $\frac{A + B x}{\sqrt{a + c x^{2}} \sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)/(sqrt(a + c*x**2)*(d + e*x)**(3/2))` | $\frac{A + B x}{\sqrt{a + c x^{2}} \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((a + c*x**2)**(3/2)*sqrt(d + e*x))` | $\frac{A + B x}{\left(a + c x^{2}\right)^{\frac{3}{2}} \sqrt{d + e x}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**4*sqrt(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \left(d + e x\right)^{4} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**3*sqrt(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \left(d + e x\right)^{3} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**2*sqrt(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \left(d + e x\right)^{2} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)*sqrt(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \left(d + e x\right) \sqrt{a + b x + c x^{2}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*sqrt(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(a + b*x + c*x**2)/(d + e*x)` | $\frac{\left(b + 2 c x\right) \sqrt{a + b x + c x^{2}}}{d + e x}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(a + b*x + c*x**2)/(d + e*x)**2` | $\frac{\left(b + 2 c x\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(a + b*x + c*x**2)/(d + e*x)**3` | $\frac{\left(b + 2 c x\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(a + b*x + c*x**2)/(d + e*x)**4` | $\frac{\left(b + 2 c x\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(a + b*x + c*x**2)/(d + e*x)**5` | $\frac{\left(b + 2 c x\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(a + b*x + c*x**2)/(d + e*x)**6` | $\frac{\left(b + 2 c x\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**3*(a + b*x + c*x**2)**(3/2)` | $\left(b + 2 c x\right) \left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**2*(a + b*x + c*x**2)**(3/2)` | $\left(b + 2 c x\right) \left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)*(a + b*x + c*x**2)**(3/2)` | $\left(b + 2 c x\right) \left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(3/2)` | $\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(3/2)/(d + e*x)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(3/2)/(d + e*x)**2` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(3/2)/(d + e*x)**3` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(3/2)/(d + e*x)**4` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**3*(a + b*x + c*x**2)**(5/2)` | $\left(b + 2 c x\right) \left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**2*(a + b*x + c*x**2)**(5/2)` | $\left(b + 2 c x\right) \left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)*(a + b*x + c*x**2)**(5/2)` | $\left(b + 2 c x\right) \left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(5/2)` | $\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(5/2)/(d + e*x)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(5/2)/(d + e*x)**2` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(5/2)/(d + e*x)**3` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(5/2)/(d + e*x)**4` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**3/sqrt(a + b*x + c*x**2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{3}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**2/sqrt(a + b*x + c*x**2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{2}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)/sqrt(a + b*x + c*x**2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)}{\sqrt{a + b x + c x^{2}}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)/sqrt(a + b*x + c*x**2)` | $\frac{b + 2 c x}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{b + 2 c x}{\left(d + e x\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)**2*sqrt(a + b*x + c*x**2))` | $\frac{b + 2 c x}{\left(d + e x\right)^{2} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)**3*sqrt(a + b*x + c*x**2))` | $\frac{b + 2 c x}{\left(d + e x\right)^{3} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)**4*sqrt(a + b*x + c*x**2))` | $\frac{b + 2 c x}{\left(d + e x\right)^{4} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**4/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{4}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**3/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**2/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{b + 2 c x}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{b + 2 c x}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)**2*(a + b*x + c*x**2)**(3/2))` | $\frac{b + 2 c x}{\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**4/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{4}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**3/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(d + e*x)**2/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(d + e*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{b + 2 c x}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)*(a + b*x + c*x**2)**(5/2))` | $\frac{b + 2 c x}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)**2*(a + b*x + c*x**2)**(5/2))` | $\frac{b + 2 c x}{\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(d + e*x)**(5/2)*(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(d + e*x)**(3/2)*(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(b + 2*c*x)*sqrt(d + e*x)*(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \sqrt{d + e x} \left(a + b x + c x^{2}\right)$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)/sqrt(d + e*x)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)/(d + e*x)**(3/2)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)/(d + e*x)**(5/2)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(d + e*x)**(5/2)*(a + b*x + c*x**2)**2` | $\left(b + 2 c x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(d + e*x)**(3/2)*(a + b*x + c*x**2)**2` | $\left(b + 2 c x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*sqrt(d + e*x)*(a + b*x + c*x**2)**2` | $\left(b + 2 c x\right) \sqrt{d + e x} \left(a + b x + c x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**2/sqrt(d + e*x)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**2/(d + e*x)**(3/2)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**2/(d + e*x)**(5/2)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(d + e*x)**(5/2)*(a + b*x + c*x**2)**3` | $\left(b + 2 c x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(d + e*x)**(3/2)*(a + b*x + c*x**2)**3` | $\left(b + 2 c x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*sqrt(d + e*x)*(a + b*x + c*x**2)**3` | $\left(b + 2 c x\right) \sqrt{d + e x} \left(a + b x + c x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**3/sqrt(d + e*x)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{3}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**3/(d + e*x)**(3/2)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**3/(d + e*x)**(5/2)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(3/2)/(a + b*x + c*x**2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{3}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(d + e*x)/(a + b*x + c*x**2)` | $\frac{\left(b + 2 c x\right) \sqrt{d + e x}}{a + b x + c x^{2}}$ |
| partial | parametric | `(b + 2*c*x)/(sqrt(d + e*x)*(a + b*x + c*x**2))` | $\frac{b + 2 c x}{\sqrt{d + e x} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)**(3/2)*(a + b*x + c*x**2))` | $\frac{b + 2 c x}{\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)**(5/2)*(a + b*x + c*x**2))` | $\frac{b + 2 c x}{\left(d + e x\right)^{\frac{5}{2}} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(5/2)/(a + b*x + c*x**2)**2` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(3/2)/(a + b*x + c*x**2)**2` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(d + e*x)/(a + b*x + c*x**2)**2` | $\frac{\left(b + 2 c x\right) \sqrt{d + e x}}{\left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(b + 2*c*x)/(sqrt(d + e*x)*(a + b*x + c*x**2)**2)` | $\frac{b + 2 c x}{\sqrt{d + e x} \left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)**(3/2)*(a + b*x + c*x**2)**2)` | $\frac{b + 2 c x}{\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{2}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(7/2)/(a + b*x + c*x**2)**3` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(5/2)/(a + b*x + c*x**2)**3` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(3/2)/(a + b*x + c*x**2)**3` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(d + e*x)/(a + b*x + c*x**2)**3` | $\frac{\left(b + 2 c x\right) \sqrt{d + e x}}{\left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(b + 2*c*x)/(sqrt(d + e*x)*(a + b*x + c*x**2)**3)` | $\frac{b + 2 c x}{\sqrt{d + e x} \left(a + b x + c x^{2}\right)^{3}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(d + e*x)*sqrt(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \sqrt{d + e x} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(a + b*x + c*x**2)/sqrt(d + e*x)` | $\frac{\left(b + 2 c x\right) \sqrt{a + b x + c x^{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(a + b*x + c*x**2)/(d + e*x)**(3/2)` | $\frac{\left(b + 2 c x\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(a + b*x + c*x**2)/(d + e*x)**(5/2)` | $\frac{\left(b + 2 c x\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(a + b*x + c*x**2)/(d + e*x)**(7/2)` | $\frac{\left(b + 2 c x\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(3/2)/sqrt(d + e*x)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(5/2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{5}{2}}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(3/2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{3}{2}}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(d + e*x)/sqrt(a + b*x + c*x**2)` | $\frac{\left(b + 2 c x\right) \sqrt{d + e x}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)/(sqrt(d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{b + 2 c x}{\sqrt{d + e x} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)**(3/2)*sqrt(a + b*x + c*x**2))` | $\frac{b + 2 c x}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)**(5/2)*sqrt(a + b*x + c*x**2))` | $\frac{b + 2 c x}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(7/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(5/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(3/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(d + e*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b + 2 c x\right) \sqrt{d + e x}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)/(sqrt(d + e*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{b + 2 c x}{\sqrt{d + e x} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)/((d + e*x)**(3/2)*(a + b*x + c*x**2)**(3/2))` | $\frac{b + 2 c x}{\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(7/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(5/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*(d + e*x)**(3/2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b + 2 c x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b + 2*c*x)*sqrt(d + e*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b + 2 c x\right) \sqrt{d + e x}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(b + 2*c*x)/(sqrt(d + e*x)*(a + b*x + c*x**2)**(5/2))` | $\frac{b + 2 c x}{\sqrt{d + e x} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**4*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{4} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**3*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{3} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**2*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{2} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \left(d + e x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{d + e x}$ |
| partial | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**2` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**3` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**4` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**5` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**6` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{6}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**7` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{7}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**5*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(A + B x\right) \left(d + e x\right)^{5} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**4*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(A + B x\right) \left(d + e x\right)^{4} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(A + B x\right) \left(d + e x\right)^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(A + B x\right) \left(d + e x\right)^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(A + B x\right) \left(d + e x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**2` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**3` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**4` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**5` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**6` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{6}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**7` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{7}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**8` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{8}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**9` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{9}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**10` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{10}}$ |
| timeout | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**11` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{11}}$ |
| timeout | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**12` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{12}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**6*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(A + B x\right) \left(d + e x\right)^{6} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**5*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(A + B x\right) \left(d + e x\right)^{5} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**4*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(A + B x\right) \left(d + e x\right)^{4} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(A + B x\right) \left(d + e x\right)^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(A + B x\right) \left(d + e x\right)^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(A + B x\right) \left(d + e x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**2` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**3` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**4` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**5` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**6` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**7` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{7}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**8` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{8}}$ |
| timeout | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**9` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{9}}$ |
| timeout | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**10` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{10}}$ |
| timeout | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**11` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{11}}$ |
| timeout | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**12` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{12}}$ |
| timeout | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**13` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{13}}$ |
| timeout | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**14` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{14}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**3/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{3}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**2/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{2}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{A + B x}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\left(d + e x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**2*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{2} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**3*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{3} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**4*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{4} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**4/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{4}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**3/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{3}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**2/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{2}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{A + B x}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right)^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right)^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(A + B*x)*(d + e*x)**5/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{5}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**4/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{4}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**3/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{3}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**2/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{2}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{A + B x}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{\left(d + e x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{\left(d + e x\right)^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{\left(d + e x\right)^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\left(A + B x\right) \sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(A + B*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\left(A + B x\right) \sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(9/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{A + B x}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{A + B x}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{A + B x}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(11/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{11}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(9/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{A + B x}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{A + B x}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{A + B x}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(d + e*x)**(7/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(d + e*x)**(5/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*(d + e*x)**(3/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(A + B x\right) \sqrt{d + e x} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(A + B x\right) \sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(A + B x\right) \sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/sqrt(d + e*x)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(7/2)` | $\frac{\left(A + B x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\sqrt{d + e x} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(5/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(7/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{7}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(11/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{11}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(9/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**5*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \left(d + e x\right)^{5} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**4*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \left(d + e x\right)^{4} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**3*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \left(d + e x\right)^{3} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**2*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \left(d + e x\right)^{2} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \left(d + e x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)` | $\frac{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{d + e x}$ |
| partial | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**2` | $\frac{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**3` | $\frac{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**4` | $\frac{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**5` | $\frac{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**6` | $\frac{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{6}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**7` | $\frac{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{7}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**8` | $\frac{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{8}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**7*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a + b x\right) \left(d + e x\right)^{7} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**6*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a + b x\right) \left(d + e x\right)^{6} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**5*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a + b x\right) \left(d + e x\right)^{5} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**4*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a + b x\right) \left(d + e x\right)^{4} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a + b x\right) \left(d + e x\right)^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a + b x\right) \left(d + e x\right)^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a + b x\right) \left(d + e x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**2` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**3` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**4` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**5` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**6` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{6}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**7` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{7}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**8` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{8}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**9` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{9}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**10` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{10}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**11` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{11}}$ |
| timeout | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**12` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{12}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**9*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \left(d + e x\right)^{9} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**8*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \left(d + e x\right)^{8} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**7*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \left(d + e x\right)^{7} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**6*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \left(d + e x\right)^{6} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**5*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \left(d + e x\right)^{5} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**4*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \left(d + e x\right)^{4} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \left(d + e x\right)^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \left(d + e x\right)^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \left(d + e x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**2` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**3` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**4` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**5` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**6` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**7` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{7}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**8` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{8}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**9` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{9}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**10` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{10}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**11` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{11}}$ |
| timeout | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**12` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{12}}$ |
| timeout | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**13` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{13}}$ |
| timeout | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**14` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{14}}$ |
| timeout | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**15` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{15}}$ |
| timeout | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**16` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{16}}$ |
| timeout | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**17` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{17}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**4/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{4}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**3/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{3}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**2/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{2}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(a + b x\right) \left(d + e x\right)}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{a + b x}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\left(d + e x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)/((d + e*x)**2*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\left(d + e x\right)^{2} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)/((d + e*x)**3*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\left(d + e x\right)^{3} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)/((d + e*x)**4*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\left(d + e x\right)^{4} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)/((d + e*x)**5*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\left(d + e x\right)^{5} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**4/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{4}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**3/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{3}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**2/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{2}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{a + b x}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{a + b x}{\left(d + e x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{a + b x}{\left(d + e x\right)^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{a + b x}{\left(d + e x\right)^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**5/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{5}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**4/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{4}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**3/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{3}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**2/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{2}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{a + b x}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{a + b x}{\left(d + e x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{a + b x}{\left(d + e x\right)^{2} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{a + b x}{\left(d + e x\right)^{3} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `(a + b*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)/sqrt(d + e*x)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(3/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(5/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(7/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\left(a + b x\right) \left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**2` | $\left(a + b x\right) \sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/sqrt(d + e*x)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/(d + e*x)**(3/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/(d + e*x)**(5/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**2/(d + e*x)**(7/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\left(a + b x\right) \left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**3` | $\left(a + b x\right) \sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/sqrt(d + e*x)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\sqrt{d + e x}}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/(d + e*x)**(3/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/(d + e*x)**(5/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**3/(d + e*x)**(7/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{7}{2}}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(a + b*x)*sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(a + b x\right) \sqrt{d + e x}}{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `(a + b*x)/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(9/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x)*sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**2` | $\frac{\left(a + b x\right) \sqrt{d + e x}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x)/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{a + b x}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{a + b x}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{a + b x}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**2)` | $\frac{a + b x}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(11/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{11}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(9/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x)*sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**3` | $\frac{\left(a + b x\right) \sqrt{d + e x}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x)/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{a + b x}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{a + b x}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**3)` | $\frac{a + b x}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(d + e*x)**(7/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \left(d + e x\right)^{\frac{7}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(d + e*x)**(5/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(d + e*x)**(3/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*sqrt(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\left(a + b x\right) \sqrt{d + e x} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/sqrt(d + e*x)` | $\frac{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(3/2)` | $\frac{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(5/2)` | $\frac{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(7/2)` | $\frac{\left(a + b x\right) \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\left(a + b x\right) \sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/sqrt(d + e*x)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(9/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(11/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(13/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\left(a + b x\right) \sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/sqrt(d + e*x)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(3/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(7/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(9/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(11/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(13/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(15/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{15}{2}}}$ |
| partial | parametric | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(17/2)` | $\frac{\left(a + b x\right) \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{17}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(d + e*x)**(7/2)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{7}{2}}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(d + e*x)**(5/2)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*(d + e*x)**(3/2)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)*sqrt(d + e*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\frac{\left(a + b x\right) \sqrt{d + e x}}{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)/(sqrt(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\sqrt{d + e x} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)/((d + e*x)**(3/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)/((d + e*x)**(5/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x)/((d + e*x)**(7/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | $\frac{a + b x}{\left(d + e x\right)^{\frac{7}{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)*sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | $\frac{\left(a + b x\right) \sqrt{d + e x}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{a + b x}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{a + b x}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{a + b x}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | $\frac{a + b x}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(7/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(5/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)*(d + e*x)**(3/2)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)*sqrt(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | $\frac{\left(a + b x\right) \sqrt{d + e x}}{\left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)/(sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{a + b x}{\sqrt{d + e x} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{a + b x}{\left(d + e x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{a + b x}{\left(d + e x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)/((d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | $\frac{a + b x}{\left(d + e x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x + b^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**3*(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | $\left(d + e x\right)^{3} \left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}$ |
| partial | parametric | `(d + e*x)**2*(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | $\left(d + e x\right)^{2} \left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}$ |
| partial | parametric | `(d + e*x)*(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | $\left(d + e x\right) \left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}$ |
| partial | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{d + e x}$ |
| partial | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**2` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**3` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**4` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**5` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{5}}$ |
| timeout | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**6` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{6}}$ |
| timeout | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**7` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{7}}$ |
| timeout | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**8` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{8}}$ |
| partial | parametric | `(d + e*x)**3*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\left(d + e x\right)^{3} \left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)**2*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\left(d + e x\right)^{2} \left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\left(d + e x\right) \left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**2` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**3` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**4` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**5` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**6` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{6}}$ |
| timeout | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**7` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{7}}$ |
| timeout | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**8` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{8}}$ |
| timeout | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**9` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{9}}$ |
| partial | parametric | `(d + e*x)**3*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\left(d + e x\right)^{3} \left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)**2*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\left(d + e x\right)^{2} \left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\left(d + e x\right) \left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**2` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**3` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**4` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**5` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{5}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**6` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{6}}$ |
| timeout | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**7` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{7}}$ |
| timeout | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**8` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{8}}$ |
| timeout | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**9` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{9}}$ |
| timeout | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**10` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{10}}$ |
| timeout | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**11` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{11}}$ |
| partial | parametric | `(d + e*x)**3*(f + g*x)/sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | $\frac{\left(d + e x\right)^{3} \left(f + g x\right)}{\sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**2*(f + g*x)/sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | $\frac{\left(d + e x\right)^{2} \left(f + g x\right)}{\sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)*(f + g*x)/sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | $\frac{\left(d + e x\right) \left(f + g x\right)}{\sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `(f + g*x)/((d + e*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2))` | $\frac{f + g x}{\left(d + e x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)/((d + e*x)**2*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2))` | $\frac{f + g x}{\left(d + e x\right)^{2} \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)/((d + e*x)**3*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2))` | $\frac{f + g x}{\left(d + e x\right)^{3} \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| timeout | parametric | `(f + g*x)/((d + e*x)**4*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2))` | $\frac{f + g x}{\left(d + e x\right)^{4} \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| timeout | parametric | `(f + g*x)/((d + e*x)**5*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2))` | $\frac{f + g x}{\left(d + e x\right)^{5} \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**3*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{3} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**2*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{2} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)/((d + e*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2))` | $\frac{f + g x}{\left(d + e x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)/((d + e*x)**2*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2))` | $\frac{f + g x}{\left(d + e x\right)^{2} \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)/((d + e*x)**3*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2))` | $\frac{f + g x}{\left(d + e x\right)^{3} \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**5*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{5} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**4*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{4} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**3*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{3} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{2} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right) \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)/((d + e*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2))` | $\frac{f + g x}{\left(d + e x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(f + g*x)/((d + e*x)**2*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2))` | $\frac{f + g x}{\left(d + e x\right)^{2} \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(f + g*x)/((d + e*x)**3*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2))` | $\frac{f + g x}{\left(d + e x\right)^{3} \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)*(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | $\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d + e*x)*(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | $\sqrt{d + e x} \left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/sqrt(d + e*x)` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**(3/2)` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**(5/2)` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**(7/2)` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**(9/2)` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**(11/2)` | $\frac{\left(f + g x\right) \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(d + e*x)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\sqrt{d + e x} \left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/sqrt(d + e*x)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(5/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(7/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(9/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(11/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(13/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(d + e*x)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\sqrt{d + e x} \left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/sqrt(d + e*x)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**(3/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**(7/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**(9/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**(11/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**(13/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{13}{2}}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**(15/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{15}{2}}}$ |
| partial | parametric | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**(17/2)` | $\frac{\left(f + g x\right) \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{17}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)*(f + g*x)/sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)}{\sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)*(f + g*x)/sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)}{\sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d + e*x)*(f + g*x)/sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | $\frac{\sqrt{d + e x} \left(f + g x\right)}{\sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `(f + g*x)/(sqrt(d + e*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2))` | $\frac{f + g x}{\sqrt{d + e x} \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `(f + g*x)/((d + e*x)**(3/2)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2))` | $\frac{f + g x}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `(f + g*x)/((d + e*x)**(5/2)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2))` | $\frac{f + g x}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**(9/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{9}{2}} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(7/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(5/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | $\frac{\sqrt{d + e x} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(f + g*x)/(sqrt(d + e*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2))` | $\frac{f + g x}{\sqrt{d + e x} \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(f + g*x)/((d + e*x)**(3/2)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2))` | $\frac{f + g x}{\left(d + e x\right)^{\frac{3}{2}} \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(f + g*x)/((d + e*x)**(5/2)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2))` | $\frac{f + g x}{\left(d + e x\right)^{\frac{5}{2}} \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(13/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{13}{2}} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(11/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{11}{2}} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(9/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{9}{2}} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(7/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{7}{2}} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(5/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | $\frac{\sqrt{d + e x} \left(f + g x\right)}{\left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(f + g*x)/(sqrt(d + e*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2))` | $\frac{f + g x}{\sqrt{d + e x} \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(f + g*x)/((d + e*x)**(3/2)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2))` | $\frac{f + g x}{\left(d + e x\right)^{\frac{3}{2}} \left(- b d e - b e^{2} x + c d^{2} - c e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x)*(x + 1)**(3/2)*(x**2 - x + 1)**(3/2)` | $\left(a + b x\right) \left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x)*sqrt(x + 1)*sqrt(x**2 - x + 1)` | $\left(a + b x\right) \sqrt{x + 1} \sqrt{x^{2} - x + 1}$ |
| partial | parametric | `(a + b*x)/(sqrt(x + 1)*sqrt(x**2 - x + 1))` | $\frac{a + b x}{\sqrt{x + 1} \sqrt{x^{2} - x + 1}}$ |
| partial | parametric | `(a + b*x)/((x + 1)**(3/2)*(x**2 - x + 1)**(3/2))` | $\frac{a + b x}{\left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x)/((x + 1)**(5/2)*(x**2 - x + 1)**(5/2))` | $\frac{a + b x}{\left(x + 1\right)^{\frac{5}{2}} \left(x^{2} - x + 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4*sqrt(3*x**2 + 5*x + 2)` | $\left(5 - x\right) \left(2 x + 3\right)^{4} \sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3*sqrt(3*x**2 + 5*x + 2)` | $\left(5 - x\right) \left(2 x + 3\right)^{3} \sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**2*sqrt(3*x**2 + 5*x + 2)` | $\left(5 - x\right) \left(2 x + 3\right)^{2} \sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(5 - x)*(2*x + 3)*sqrt(3*x**2 + 5*x + 2)` | $\left(5 - x\right) \left(2 x + 3\right) \sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)` | $\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)/(2*x + 3)` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}}{2 x + 3}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)/(2*x + 3)**2` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}}{\left(2 x + 3\right)^{2}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)/(2*x + 3)**3` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}}{\left(2 x + 3\right)^{3}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)/(2*x + 3)**4` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}}{\left(2 x + 3\right)^{4}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)/(2*x + 3)**5` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}}{\left(2 x + 3\right)^{5}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)/(2*x + 3)**6` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}}{\left(2 x + 3\right)^{6}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)/(2*x + 3)**7` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}}{\left(2 x + 3\right)^{7}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4*(3*x**2 + 5*x + 2)**(3/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{4} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3*(3*x**2 + 5*x + 2)**(3/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{3} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**2*(3*x**2 + 5*x + 2)**(3/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{2} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)*(3*x**2 + 5*x + 2)**(3/2)` | $\left(5 - x\right) \left(2 x + 3\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)` | $\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{2 x + 3}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**2` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**3` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{3}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**4` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{4}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**5` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{5}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**6` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{6}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**7` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{7}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**8` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{8}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**9` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{9}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4*(3*x**2 + 5*x + 2)**(5/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{4} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3*(3*x**2 + 5*x + 2)**(5/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{3} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**2*(3*x**2 + 5*x + 2)**(5/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{2} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)*(3*x**2 + 5*x + 2)**(5/2)` | $\left(5 - x\right) \left(2 x + 3\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)` | $\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{2 x + 3}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**2` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**3` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{3}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**4` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{4}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**5` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{5}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**6` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{6}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**7` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{7}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**8` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{8}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**9` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{9}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**10` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{10}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4*(3*x**2 + 5*x + 2)**(7/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{4} \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3*(3*x**2 + 5*x + 2)**(7/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{3} \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**2*(3*x**2 + 5*x + 2)**(7/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{2} \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)*(3*x**2 + 5*x + 2)**(7/2)` | $\left(5 - x\right) \left(2 x + 3\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)` | $\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{2 x + 3}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)**2` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{\left(2 x + 3\right)^{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)**3` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{\left(2 x + 3\right)^{3}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)**4` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{\left(2 x + 3\right)^{4}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)**5` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{\left(2 x + 3\right)^{5}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)**6` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{\left(2 x + 3\right)^{6}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)**7` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{\left(2 x + 3\right)^{7}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)**8` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{\left(2 x + 3\right)^{8}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)**9` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{\left(2 x + 3\right)^{9}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)**10` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{\left(2 x + 3\right)^{10}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)**11` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{\left(2 x + 3\right)^{11}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)**12` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{\left(2 x + 3\right)^{12}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(7/2)/(2*x + 3)**13` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{7}{2}}}{\left(2 x + 3\right)^{13}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**3/sqrt(a + b*x + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{3}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**2/sqrt(a + b*x + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{2}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)/sqrt(a + b*x + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/sqrt(a + b*x + c*x**2)` | $\frac{A + B x}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**2*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{2} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**3*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{3} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**4*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{4} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**3/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**2/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{A + B x}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**2*(a + b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**3*(a + b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**4/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{4}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**3/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**2/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a + b*x + c*x**2)**(5/2)` | $\frac{A + B x}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)*(a + b*x + c*x**2)**(5/2))` | $\frac{A + B x}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**2*(a + b*x + c*x**2)**(5/2))` | $\frac{A + B x}{\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**6/(a + b*x + c*x**2)**(7/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{6}}{\left(a + b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**5/(a + b*x + c*x**2)**(7/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{5}}{\left(a + b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**4/(a + b*x + c*x**2)**(7/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{4}}{\left(a + b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**3/(a + b*x + c*x**2)**(7/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)**2/(a + b*x + c*x**2)**(7/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)*(d + e*x)/(a + b*x + c*x**2)**(7/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)}{\left(a + b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x)/(a + b*x + c*x**2)**(7/2)` | $\frac{A + B x}{\left(a + b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)*(a + b*x + c*x**2)**(7/2))` | $\frac{A + B x}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4/sqrt(3*x**2 + 5*x + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{4}}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3/sqrt(3*x**2 + 5*x + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{3}}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**2/sqrt(3*x**2 + 5*x + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{2}}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)/sqrt(3*x**2 + 5*x + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)/sqrt(3*x**2 + 5*x + 2)` | $\frac{5 - x}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)*sqrt(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\left(2 x + 3\right) \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**2*sqrt(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{2} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**3*sqrt(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{3} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**4*sqrt(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{4} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**5*sqrt(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{5} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**6*sqrt(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{6} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{4}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{3}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**2/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{2}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{5 - x}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**2*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{2} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**3*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{3} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**4*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{4} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**5*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{5} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**4/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{4}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**3/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{3}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)**2/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{2}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{5 - x}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)*(3*x**2 + 5*x + 2)**(5/2))` | $\frac{5 - x}{\left(2 x + 3\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**2*(3*x**2 + 5*x + 2)**(5/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{2} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**3*(3*x**2 + 5*x + 2)**(5/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{3} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**4*(3*x**2 + 5*x + 2)**(5/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{4} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(x - 1)/((x + 1)*sqrt(x**2 + x + 1))` | $\frac{x - 1}{\left(x + 1\right) \sqrt{x^{2} + x + 1}}$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)**(7/2)*(3*x**2 + 5*x + 2)` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{7}{2}} \left(3 x^{2} + 5 x + 2\right)$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)**(5/2)*(3*x**2 + 5*x + 2)` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{5}{2}} \left(3 x^{2} + 5 x + 2\right)$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)**(3/2)*(3*x**2 + 5*x + 2)` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{3}{2}} \left(3 x^{2} + 5 x + 2\right)$ |
| SOLVED-both | concrete | `(5 - x)*sqrt(2*x + 3)*(3*x**2 + 5*x + 2)` | $\left(5 - x\right) \sqrt{2 x + 3} \left(3 x^{2} + 5 x + 2\right)$ |
| SOLVED-both | concrete | `(5 - x)*(3*x**2 + 5*x + 2)/sqrt(2*x + 3)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)}{\sqrt{2 x + 3}}$ |
| SOLVED-both | concrete | `(5 - x)*(3*x**2 + 5*x + 2)/(2*x + 3)**(3/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)}{\left(2 x + 3\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)*(3*x**2 + 5*x + 2)/(2*x + 3)**(5/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)}{\left(2 x + 3\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)*(3*x**2 + 5*x + 2)/(2*x + 3)**(7/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)}{\left(2 x + 3\right)^{\frac{7}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)**(7/2)*(3*x**2 + 5*x + 2)**2` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{7}{2}} \left(3 x^{2} + 5 x + 2\right)^{2}$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)**(5/2)*(3*x**2 + 5*x + 2)**2` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{5}{2}} \left(3 x^{2} + 5 x + 2\right)^{2}$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)**(3/2)*(3*x**2 + 5*x + 2)**2` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{3}{2}} \left(3 x^{2} + 5 x + 2\right)^{2}$ |
| SOLVED-both | concrete | `(5 - x)*sqrt(2*x + 3)*(3*x**2 + 5*x + 2)**2` | $\left(5 - x\right) \sqrt{2 x + 3} \left(3 x^{2} + 5 x + 2\right)^{2}$ |
| SOLVED-both | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**2/sqrt(2*x + 3)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{2}}{\sqrt{2 x + 3}}$ |
| SOLVED-both | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**2/(2*x + 3)**(3/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{2}}{\left(2 x + 3\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**2/(2*x + 3)**(5/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{2}}{\left(2 x + 3\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**2/(2*x + 3)**(7/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{2}}{\left(2 x + 3\right)^{\frac{7}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)**(7/2)*(3*x**2 + 5*x + 2)**3` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{7}{2}} \left(3 x^{2} + 5 x + 2\right)^{3}$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)**(5/2)*(3*x**2 + 5*x + 2)**3` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{5}{2}} \left(3 x^{2} + 5 x + 2\right)^{3}$ |
| SOLVED-both | concrete | `(5 - x)*(2*x + 3)**(3/2)*(3*x**2 + 5*x + 2)**3` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{3}{2}} \left(3 x^{2} + 5 x + 2\right)^{3}$ |
| SOLVED-both | concrete | `(5 - x)*sqrt(2*x + 3)*(3*x**2 + 5*x + 2)**3` | $\left(5 - x\right) \sqrt{2 x + 3} \left(3 x^{2} + 5 x + 2\right)^{3}$ |
| SOLVED-both | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**3/sqrt(2*x + 3)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{3}}{\sqrt{2 x + 3}}$ |
| SOLVED-both | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**3/(2*x + 3)**(3/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{3}}{\left(2 x + 3\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**3/(2*x + 3)**(5/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{3}}{\left(2 x + 3\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**3/(2*x + 3)**(7/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{3}}{\left(2 x + 3\right)^{\frac{7}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(7/2)/(3*x**2 + 5*x + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{7}{2}}}{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(5/2)/(3*x**2 + 5*x + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{5}{2}}}{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(3/2)/(3*x**2 + 5*x + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{3}{2}}}{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(5 - x)*sqrt(2*x + 3)/(3*x**2 + 5*x + 2)` | $\frac{\left(5 - x\right) \sqrt{2 x + 3}}{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(5 - x)/(sqrt(2*x + 3)*(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\sqrt{2 x + 3} \left(3 x^{2} + 5 x + 2\right)}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(3/2)*(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{3}{2}} \left(3 x^{2} + 5 x + 2\right)}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(5/2)*(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{5}{2}} \left(3 x^{2} + 5 x + 2\right)}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(7/2)*(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{7}{2}} \left(3 x^{2} + 5 x + 2\right)}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(7/2)/(3*x**2 + 5*x + 2)**2` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{7}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(5/2)/(3*x**2 + 5*x + 2)**2` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{5}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(3/2)/(3*x**2 + 5*x + 2)**2` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{3}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{2}}$ |
| partial | concrete | `(5 - x)*sqrt(2*x + 3)/(3*x**2 + 5*x + 2)**2` | $\frac{\left(5 - x\right) \sqrt{2 x + 3}}{\left(3 x^{2} + 5 x + 2\right)^{2}}$ |
| partial | concrete | `(5 - x)/(sqrt(2*x + 3)*(3*x**2 + 5*x + 2)**2)` | $\frac{5 - x}{\sqrt{2 x + 3} \left(3 x^{2} + 5 x + 2\right)^{2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(3/2)*(3*x**2 + 5*x + 2)**2)` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{3}{2}} \left(3 x^{2} + 5 x + 2\right)^{2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(5/2)*(3*x**2 + 5*x + 2)**2)` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{5}{2}} \left(3 x^{2} + 5 x + 2\right)^{2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(7/2)*(3*x**2 + 5*x + 2)**2)` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{7}{2}} \left(3 x^{2} + 5 x + 2\right)^{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(9/2)/(3*x**2 + 5*x + 2)**3` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{9}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{3}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(7/2)/(3*x**2 + 5*x + 2)**3` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{7}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{3}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(5/2)/(3*x**2 + 5*x + 2)**3` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{5}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{3}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(3/2)/(3*x**2 + 5*x + 2)**3` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{3}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{3}}$ |
| partial | concrete | `(5 - x)*sqrt(2*x + 3)/(3*x**2 + 5*x + 2)**3` | $\frac{\left(5 - x\right) \sqrt{2 x + 3}}{\left(3 x^{2} + 5 x + 2\right)^{3}}$ |
| partial | concrete | `(5 - x)/(sqrt(2*x + 3)*(3*x**2 + 5*x + 2)**3)` | $\frac{5 - x}{\sqrt{2 x + 3} \left(3 x^{2} + 5 x + 2\right)^{3}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(3/2)*(3*x**2 + 5*x + 2)**3)` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{3}{2}} \left(3 x^{2} + 5 x + 2\right)^{3}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(5/2)*(3*x**2 + 5*x + 2)**3)` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{5}{2}} \left(3 x^{2} + 5 x + 2\right)^{3}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(7/2)*(3*x**2 + 5*x + 2)**3)` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{7}{2}} \left(3 x^{2} + 5 x + 2\right)^{3}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(5/2)*sqrt(3*x**2 + 5*x + 2)` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{5}{2}} \sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(3/2)*sqrt(3*x**2 + 5*x + 2)` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{3}{2}} \sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(5 - x)*sqrt(2*x + 3)*sqrt(3*x**2 + 5*x + 2)` | $\left(5 - x\right) \sqrt{2 x + 3} \sqrt{3 x^{2} + 5 x + 2}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)/sqrt(2*x + 3)` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}}{\sqrt{2 x + 3}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)/(2*x + 3)**(3/2)` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}}{\left(2 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)/(2*x + 3)**(5/2)` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}}{\left(2 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)/(2*x + 3)**(7/2)` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}}{\left(2 x + 3\right)^{\frac{7}{2}}}$ |
| partial | concrete | `(5 - x)*sqrt(3*x**2 + 5*x + 2)/(2*x + 3)**(9/2)` | $\frac{\left(5 - x\right) \sqrt{3 x^{2} + 5 x + 2}}{\left(2 x + 3\right)^{\frac{9}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(5/2)*(3*x**2 + 5*x + 2)**(3/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{5}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(3/2)*(3*x**2 + 5*x + 2)**(3/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{3}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*sqrt(2*x + 3)*(3*x**2 + 5*x + 2)**(3/2)` | $\left(5 - x\right) \sqrt{2 x + 3} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/sqrt(2*x + 3)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\sqrt{2 x + 3}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**(3/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**(5/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**(7/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{\frac{7}{2}}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**(9/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{\frac{9}{2}}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**(11/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{\frac{11}{2}}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(3/2)/(2*x + 3)**(13/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}{\left(2 x + 3\right)^{\frac{13}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(5/2)*(3*x**2 + 5*x + 2)**(5/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{5}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(3/2)*(3*x**2 + 5*x + 2)**(5/2)` | $\left(5 - x\right) \left(2 x + 3\right)^{\frac{3}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*sqrt(2*x + 3)*(3*x**2 + 5*x + 2)**(5/2)` | $\left(5 - x\right) \sqrt{2 x + 3} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/sqrt(2*x + 3)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\sqrt{2 x + 3}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**(3/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**(5/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**(7/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{\frac{7}{2}}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**(9/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{\frac{9}{2}}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**(11/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{\frac{11}{2}}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**(13/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{\frac{13}{2}}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**(15/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{\frac{15}{2}}}$ |
| partial | concrete | `(5 - x)*(3*x**2 + 5*x + 2)**(5/2)/(2*x + 3)**(17/2)` | $\frac{\left(5 - x\right) \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}{\left(2 x + 3\right)^{\frac{17}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(5/2)/sqrt(3*x**2 + 5*x + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{5}{2}}}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(3/2)/sqrt(3*x**2 + 5*x + 2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{3}{2}}}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)*sqrt(2*x + 3)/sqrt(3*x**2 + 5*x + 2)` | $\frac{\left(5 - x\right) \sqrt{2 x + 3}}{\sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)/(sqrt(2*x + 3)*sqrt(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\sqrt{2 x + 3} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(3/2)*sqrt(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{3}{2}} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(5/2)*sqrt(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{5}{2}} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(7/2)*sqrt(3*x**2 + 5*x + 2))` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{7}{2}} \sqrt{3 x^{2} + 5 x + 2}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(7/2)/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{7}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(5/2)/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{5}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(3/2)/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{3}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*sqrt(2*x + 3)/(3*x**2 + 5*x + 2)**(3/2)` | $\frac{\left(5 - x\right) \sqrt{2 x + 3}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/(sqrt(2*x + 3)*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{5 - x}{\sqrt{2 x + 3} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(3/2)*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{3}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(5/2)*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{5}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(7/2)*(3*x**2 + 5*x + 2)**(3/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{7}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(9/2)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{9}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(7/2)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{7}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(5/2)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{5}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*(2*x + 3)**(3/2)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{\left(5 - x\right) \left(2 x + 3\right)^{\frac{3}{2}}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)*sqrt(2*x + 3)/(3*x**2 + 5*x + 2)**(5/2)` | $\frac{\left(5 - x\right) \sqrt{2 x + 3}}{\left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)/(sqrt(2*x + 3)*(3*x**2 + 5*x + 2)**(5/2))` | $\frac{5 - x}{\sqrt{2 x + 3} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(3/2)*(3*x**2 + 5*x + 2)**(5/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{3}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(5/2)*(3*x**2 + 5*x + 2)**(5/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{5}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5 - x)/((2*x + 3)**(7/2)*(3*x**2 + 5*x + 2)**(5/2))` | $\frac{5 - x}{\left(2 x + 3\right)^{\frac{7}{2}} \left(3 x^{2} + 5 x + 2\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/sqrt(a + b*x + c*x**2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{\sqrt{d + e x} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(5/2)*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(5/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{5}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*(d + e*x)**(3/2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \left(d + e x\right)^{\frac{3}{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(d + e*x)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(A + B x\right) \sqrt{d + e x}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\sqrt{d + e x} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d + e*x)**(3/2)*(a + b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(d + e*x)*sqrt(d**2 - e**2*x**2)` | $x^{2} \left(d + e x\right) \sqrt{d^{2} - e^{2} x^{2}}$ |
| partial | parametric | `x**4*(d + e*x)*(d**2 - e**2*x**2)**(3/2)` | $x^{4} \left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**3*(d + e*x)*(d**2 - e**2*x**2)**(3/2)` | $x^{3} \left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(d + e*x)*(d**2 - e**2*x**2)**(3/2)` | $x^{2} \left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(d + e*x)*(d**2 - e**2*x**2)**(3/2)` | $x \left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(d + e*x)*(d**2 - e**2*x**2)**(3/2)` | $x \left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x)*(d**2 - e**2*x**2)**(3/2)/x` | $\frac{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(d + e*x)*(d**2 - e**2*x**2)**(3/2)/x**2` | $\frac{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(d + e*x)*(d**2 - e**2*x**2)**(3/2)/x**3` | $\frac{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(d + e*x)*(d**2 - e**2*x**2)**(3/2)/x**4` | $\frac{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(d + e*x)*(d**2 - e**2*x**2)**(3/2)/x**5` | $\frac{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(d + e*x)*(d**2 - e**2*x**2)**(3/2)/x**6` | $\frac{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(d + e*x)*(d**2 - e**2*x**2)**(3/2)/x**7` | $\frac{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `(d + e*x)*(d**2 - e**2*x**2)**(3/2)/x**8` | $\frac{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}{x^{8}}$ |
| partial | parametric | `(d + e*x)*(d**2 - e**2*x**2)**(3/2)/x**9` | $\frac{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}{x^{9}}$ |
| partial | parametric | `x**2*(d + e*x)/sqrt(d**2 - e**2*x**2)` | $\frac{x^{2} \left(d + e x\right)}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `x**2*(d + e*x)/(d**2 - e**2*x**2)**(3/2)` | $\frac{x^{2} \left(d + e x\right)}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `x**2*(d + e*x)/(d**2 - e**2*x**2)**(5/2)` | $\frac{x^{2} \left(d + e x\right)}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**7*(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{7} \left(d + e x\right)}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `x**6*(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{6} \left(d + e x\right)}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `x**5*(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{5} \left(d + e x\right)}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**4*(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{4} \left(d + e x\right)}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**3*(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{3} \left(d + e x\right)}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**2*(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{2} \left(d + e x\right)}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x*(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | $\frac{x \left(d + e x\right)}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | $\frac{d + e x}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)/(x*(d**2 - e**2*x**2)**(7/2))` | $\frac{d + e x}{x \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)/(x**2*(d**2 - e**2*x**2)**(7/2))` | $\frac{d + e x}{x^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)/(x**3*(d**2 - e**2*x**2)**(7/2))` | $\frac{d + e x}{x^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**2*(d + e*x)/(d**2 - e**2*x**2)**(9/2)` | $\frac{x^{2} \left(d + e x\right)}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `x**2*(d + e*x)/(d**2 - e**2*x**2)**(11/2)` | $\frac{x^{2} \left(d + e x\right)}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{11}{2}}}$ |
| partial | parametric | `x**2*(-a*x + 1)/(-a**2*x**2 + 1)**(3/2)` | $\frac{x^{2} \left(- a x + 1\right)}{\left(- a^{2} x^{2} + 1\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4*(d + e*x)**2/sqrt(d**2 - e**2*x**2)` | $\frac{x^{4} \left(d + e x\right)^{2}}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `x**3*(d + e*x)**2/sqrt(d**2 - e**2*x**2)` | $\frac{x^{3} \left(d + e x\right)^{2}}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `x**2*(d + e*x)**2/sqrt(d**2 - e**2*x**2)` | $\frac{x^{2} \left(d + e x\right)^{2}}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `x*(d + e*x)**2/sqrt(d**2 - e**2*x**2)` | $\frac{x \left(d + e x\right)^{2}}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**2/sqrt(d**2 - e**2*x**2)` | $\frac{\left(d + e x\right)^{2}}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**2/(x*sqrt(d**2 - e**2*x**2))` | $\frac{\left(d + e x\right)^{2}}{x \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**2/(x**2*sqrt(d**2 - e**2*x**2))` | $\frac{\left(d + e x\right)^{2}}{x^{2} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**2/(x**3*sqrt(d**2 - e**2*x**2))` | $\frac{\left(d + e x\right)^{2}}{x^{3} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**2/(x**4*sqrt(d**2 - e**2*x**2))` | $\frac{\left(d + e x\right)^{2}}{x^{4} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**2/(x**5*sqrt(d**2 - e**2*x**2))` | $\frac{\left(d + e x\right)^{2}}{x^{5} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**2/(x**6*sqrt(d**2 - e**2*x**2))` | $\frac{\left(d + e x\right)^{2}}{x^{6} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `x**5*(d + e*x)**2/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{5} \left(d + e x\right)^{2}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `x**4*(d + e*x)**2/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{4} \left(d + e x\right)^{2}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**3*(d + e*x)**2/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{3} \left(d + e x\right)^{2}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**2*(d + e*x)**2/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{2} \left(d + e x\right)^{2}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x*(d + e*x)**2/(d**2 - e**2*x**2)**(7/2)` | $\frac{x \left(d + e x\right)^{2}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{2}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**2/(x*(d**2 - e**2*x**2)**(7/2))` | $\frac{\left(d + e x\right)^{2}}{x \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**2/(x**2*(d**2 - e**2*x**2)**(7/2))` | $\frac{\left(d + e x\right)^{2}}{x^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**2/(x**3*(d**2 - e**2*x**2)**(7/2))` | $\frac{\left(d + e x\right)^{2}}{x^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**2/(x**4*(d**2 - e**2*x**2)**(7/2))` | $\frac{\left(d + e x\right)^{2}}{x^{4} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | concrete | `x**3*(x + 1)**2/sqrt(1 - x**2)` | $\frac{x^{3} \left(x + 1\right)^{2}}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `x**2*(x + 1)**2/sqrt(1 - x**2)` | $\frac{x^{2} \left(x + 1\right)^{2}}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `x*(x + 1)**2/sqrt(1 - x**2)` | $\frac{x \left(x + 1\right)^{2}}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `(x + 1)**2/sqrt(1 - x**2)` | $\frac{\left(x + 1\right)^{2}}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `(x + 1)**2/(x*sqrt(1 - x**2))` | $\frac{\left(x + 1\right)^{2}}{x \sqrt{1 - x^{2}}}$ |
| partial | concrete | `(x + 1)**2/(x**2*sqrt(1 - x**2))` | $\frac{\left(x + 1\right)^{2}}{x^{2} \sqrt{1 - x^{2}}}$ |
| partial | concrete | `(x + 1)**2/(x**3*sqrt(1 - x**2))` | $\frac{\left(x + 1\right)^{2}}{x^{3} \sqrt{1 - x^{2}}}$ |
| partial | concrete | `(x + 1)**2/(x**4*sqrt(1 - x**2))` | $\frac{\left(x + 1\right)^{2}}{x^{4} \sqrt{1 - x^{2}}}$ |
| partial | concrete | `(x + 1)**2/(x**5*sqrt(1 - x**2))` | $\frac{\left(x + 1\right)^{2}}{x^{5} \sqrt{1 - x^{2}}}$ |
| partial | concrete | `(x + 1)**2/(x**6*sqrt(1 - x**2))` | $\frac{\left(x + 1\right)^{2}}{x^{6} \sqrt{1 - x^{2}}}$ |
| partial | parametric | `(d + e*x)**3*sqrt(d**2 - e**2*x**2)/x**5` | $\frac{\left(d + e x\right)^{3} \sqrt{d^{2} - e^{2} x^{2}}}{x^{5}}$ |
| partial | parametric | `x**5*(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)` | $x^{5} \left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**4*(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)` | $x^{4} \left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**3*(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)` | $x^{3} \left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x**2*(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)` | $x^{2} \left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `x*(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)` | $x \left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)` | $\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)/x` | $\frac{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)/x**2` | $\frac{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{2}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)/x**3` | $\frac{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)/x**4` | $\frac{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{4}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)/x**5` | $\frac{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{5}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)/x**6` | $\frac{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{6}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)/x**7` | $\frac{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{7}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)/x**8` | $\frac{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{8}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)/x**9` | $\frac{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{9}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)/x**10` | $\frac{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{10}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)/x**11` | $\frac{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{11}}$ |
| partial | parametric | `(d + e*x)**3*(d**2 - e**2*x**2)**(5/2)/x**12` | $\frac{\left(d + e x\right)^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{12}}$ |
| partial | parametric | `x**5*(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{5} \left(d + e x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `x**4*(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{4} \left(d + e x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `x**3*(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{3} \left(d + e x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**2*(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | $\frac{x^{2} \left(d + e x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x*(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | $\frac{x \left(d + e x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**3/(x*(d**2 - e**2*x**2)**(7/2))` | $\frac{\left(d + e x\right)^{3}}{x \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**3/(x**2*(d**2 - e**2*x**2)**(7/2))` | $\frac{\left(d + e x\right)^{3}}{x^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**3/(x**3*(d**2 - e**2*x**2)**(7/2))` | $\frac{\left(d + e x\right)^{3}}{x^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `x**4*sqrt(d**2 - e**2*x**2)/(d + e*x)` | $\frac{x^{4} \sqrt{d^{2} - e^{2} x^{2}}}{d + e x}$ |
| partial | parametric | `x**3*sqrt(d**2 - e**2*x**2)/(d + e*x)` | $\frac{x^{3} \sqrt{d^{2} - e^{2} x^{2}}}{d + e x}$ |
| partial | parametric | `x**2*sqrt(d**2 - e**2*x**2)/(d + e*x)` | $\frac{x^{2} \sqrt{d^{2} - e^{2} x^{2}}}{d + e x}$ |
| partial | parametric | `x*sqrt(d**2 - e**2*x**2)/(d + e*x)` | $\frac{x \sqrt{d^{2} - e^{2} x^{2}}}{d + e x}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)/(d + e*x)` | $\frac{\sqrt{d^{2} - e^{2} x^{2}}}{d + e x}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)/(x*(d + e*x))` | $\frac{\sqrt{d^{2} - e^{2} x^{2}}}{x \left(d + e x\right)}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)/(x**2*(d + e*x))` | $\frac{\sqrt{d^{2} - e^{2} x^{2}}}{x^{2} \left(d + e x\right)}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)/(x**3*(d + e*x))` | $\frac{\sqrt{d^{2} - e^{2} x^{2}}}{x^{3} \left(d + e x\right)}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)/(x**4*(d + e*x))` | $\frac{\sqrt{d^{2} - e^{2} x^{2}}}{x^{4} \left(d + e x\right)}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)/(x**5*(d + e*x))` | $\frac{\sqrt{d^{2} - e^{2} x^{2}}}{x^{5} \left(d + e x\right)}$ |
| partial | parametric | `x**2*(d**2 - e**2*x**2)**(3/2)/(d + e*x)` | $\frac{x^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `x**4*(d**2 - e**2*x**2)**(5/2)/(d + e*x)` | $\frac{x^{4} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `x**3*(d**2 - e**2*x**2)**(5/2)/(d + e*x)` | $\frac{x^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `x**2*(d**2 - e**2*x**2)**(5/2)/(d + e*x)` | $\frac{x^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `x*(d**2 - e**2*x**2)**(5/2)/(d + e*x)` | $\frac{x \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(d + e*x)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x*(d + e*x))` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x \left(d + e x\right)}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**2*(d + e*x))` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{2} \left(d + e x\right)}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**3*(d + e*x))` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{3} \left(d + e x\right)}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**4*(d + e*x))` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{4} \left(d + e x\right)}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**5*(d + e*x))` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{5} \left(d + e x\right)}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**6*(d + e*x))` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{6} \left(d + e x\right)}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**7*(d + e*x))` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{7} \left(d + e x\right)}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**8*(d + e*x))` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{8} \left(d + e x\right)}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**9*(d + e*x))` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{9} \left(d + e x\right)}$ |
| partial | concrete | `x*sqrt(1 - x**2)/(x + 1)` | $\frac{x \sqrt{1 - x^{2}}}{x + 1}$ |
| partial | parametric | `(-a**2*x**2 + 1)**(3/2)/(x**2*(-a*x + 1))` | $\frac{\left(- a^{2} x^{2} + 1\right)^{\frac{3}{2}}}{x^{2} \left(- a x + 1\right)}$ |
| partial | parametric | `x**4/((d + e*x)*sqrt(d**2 - e**2*x**2))` | $\frac{x^{4}}{\left(d + e x\right) \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `x**3/((d + e*x)*sqrt(d**2 - e**2*x**2))` | $\frac{x^{3}}{\left(d + e x\right) \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `x**2/((d + e*x)*sqrt(d**2 - e**2*x**2))` | $\frac{x^{2}}{\left(d + e x\right) \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `x/((d + e*x)*sqrt(d**2 - e**2*x**2))` | $\frac{x}{\left(d + e x\right) \sqrt{d^{2} - e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)*sqrt(d**2 - e**2*x**2))` | $\frac{1}{\left(d + e x\right) \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `1/(x*(d + e*x)*sqrt(d**2 - e**2*x**2))` | $\frac{1}{x \left(d + e x\right) \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `1/(x**2*(d + e*x)*sqrt(d**2 - e**2*x**2))` | $\frac{1}{x^{2} \left(d + e x\right) \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `1/(x**3*(d + e*x)*sqrt(d**2 - e**2*x**2))` | $\frac{1}{x^{3} \left(d + e x\right) \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `x**5/((d + e*x)*(d**2 - e**2*x**2)**(3/2))` | $\frac{x^{5}}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/((d + e*x)*(d**2 - e**2*x**2)**(3/2))` | $\frac{x^{4}}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/((d + e*x)*(d**2 - e**2*x**2)**(3/2))` | $\frac{x^{3}}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2/((d + e*x)*(d**2 - e**2*x**2)**(3/2))` | $\frac{x^{2}}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/((d + e*x)*(d**2 - e**2*x**2)**(3/2))` | $\frac{x}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)*(d**2 - e**2*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(d + e*x)*(d**2 - e**2*x**2)**(3/2))` | $\frac{1}{x \left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(d + e*x)*(d**2 - e**2*x**2)**(3/2))` | $\frac{1}{x^{2} \left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(d + e*x)*(d**2 - e**2*x**2)**(3/2))` | $\frac{1}{x^{3} \left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**7/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{x^{7}}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**6/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{x^{6}}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**5/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{x^{5}}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**4/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{x^{4}}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**3/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{x^{3}}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{x^{2}}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{x}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{1}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*(d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{1}{x \left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**2*(d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{1}{x^{2} \left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**3*(d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{1}{x^{3} \left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**4*(d + e*x)*(d**2 - e**2*x**2)**(5/2))` | $\frac{1}{x^{4} \left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**3/((d + e*x)*(d**2 - e**2*x**2)**(7/2))` | $\frac{x^{3}}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2/((d + e*x)*(d**2 - e**2*x**2)**(7/2))` | $\frac{x^{2}}{\left(d + e x\right) \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `x**3/((a*x + 1)*sqrt(-a**2*x**2 + 1))` | $\frac{x^{3}}{\left(a x + 1\right) \sqrt{- a^{2} x^{2} + 1}}$ |
| partial | parametric | `x**2/((a*x + 1)*sqrt(-a**2*x**2 + 1))` | $\frac{x^{2}}{\left(a x + 1\right) \sqrt{- a^{2} x^{2} + 1}}$ |
| partial | parametric | `x/((a*x + 1)*sqrt(-a**2*x**2 + 1))` | $\frac{x}{\left(a x + 1\right) \sqrt{- a^{2} x^{2} + 1}}$ |
| **SOLVED-NEW** | parametric | `1/((a*x + 1)*sqrt(-a**2*x**2 + 1))` | $\frac{1}{\left(a x + 1\right) \sqrt{- a^{2} x^{2} + 1}}$ |
| partial | parametric | `1/(x*(-a*x + 1)*sqrt(-a**2*x**2 + 1))` | $\frac{1}{x \left(- a x + 1\right) \sqrt{- a^{2} x^{2} + 1}}$ |
| partial | parametric | `1/(x**2*(-a*x + 1)*sqrt(-a**2*x**2 + 1))` | $\frac{1}{x^{2} \left(- a x + 1\right) \sqrt{- a^{2} x^{2} + 1}}$ |
| partial | parametric | `1/(x**3*(-a*x + 1)*sqrt(-a**2*x**2 + 1))` | $\frac{1}{x^{3} \left(- a x + 1\right) \sqrt{- a^{2} x^{2} + 1}}$ |
| partial | parametric | `x**5*(d**2 - e**2*x**2)**(5/2)/(d + e*x)**2` | $\frac{x^{5} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `x**4*(d**2 - e**2*x**2)**(5/2)/(d + e*x)**2` | $\frac{x^{4} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `x**3*(d**2 - e**2*x**2)**(5/2)/(d + e*x)**2` | $\frac{x^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `x**2*(d**2 - e**2*x**2)**(5/2)/(d + e*x)**2` | $\frac{x^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `x*(d**2 - e**2*x**2)**(5/2)/(d + e*x)**2` | $\frac{x \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(d + e*x)**2` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x*(d + e*x)**2)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x \left(d + e x\right)^{2}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**2*(d + e*x)**2)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{2} \left(d + e x\right)^{2}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**3*(d + e*x)**2)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{3} \left(d + e x\right)^{2}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**4*(d + e*x)**2)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{4} \left(d + e x\right)^{2}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**5*(d + e*x)**2)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{5} \left(d + e x\right)^{2}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**6*(d + e*x)**2)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{6} \left(d + e x\right)^{2}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**7*(d + e*x)**2)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{7} \left(d + e x\right)^{2}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**8*(d + e*x)**2)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{8} \left(d + e x\right)^{2}}$ |
| partial | parametric | `x**4/((d + e*x)**2*(d**2 - e**2*x**2)**(3/2))` | $\frac{x^{4}}{\left(d + e x\right)^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**3/((d + e*x)**2*(d**2 - e**2*x**2)**(3/2))` | $\frac{x^{3}}{\left(d + e x\right)^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/((d + e*x)**2*(d**2 - e**2*x**2)**(3/2))` | $\frac{x}{\left(d + e x\right)^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**2*(d**2 - e**2*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right)^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(d + e*x)**2*(d**2 - e**2*x**2)**(3/2))` | $\frac{1}{x \left(d + e x\right)^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(d + e*x)**2*(d**2 - e**2*x**2)**(3/2))` | $\frac{1}{x^{2} \left(d + e x\right)^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(d + e*x)**2*(d**2 - e**2*x**2)**(3/2))` | $\frac{1}{x^{3} \left(d + e x\right)^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | $\frac{x^{5}}{\left(d + e x\right)^{3} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `x**4/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | $\frac{x^{4}}{\left(d + e x\right)^{3} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `x**3/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | $\frac{x^{3}}{\left(d + e x\right)^{3} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | $\frac{x^{2}}{\left(d + e x\right)^{3} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `x/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | $\frac{x}{\left(d + e x\right)^{3} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | $\frac{1}{\left(d + e x\right)^{3} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `1/(x*(d + e*x)**3*sqrt(d**2 - e**2*x**2))` | $\frac{1}{x \left(d + e x\right)^{3} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `1/(x**2*(d + e*x)**3*sqrt(d**2 - e**2*x**2))` | $\frac{1}{x^{2} \left(d + e x\right)^{3} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `1/(x**3*(d + e*x)**3*sqrt(d**2 - e**2*x**2))` | $\frac{1}{x^{3} \left(d + e x\right)^{3} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `x**5*sqrt(d**2 - e**2*x**2)/(d + e*x)**4` | $\frac{x^{5} \sqrt{d^{2} - e^{2} x^{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `x**4*sqrt(d**2 - e**2*x**2)/(d + e*x)**4` | $\frac{x^{4} \sqrt{d^{2} - e^{2} x^{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `x**3*sqrt(d**2 - e**2*x**2)/(d + e*x)**4` | $\frac{x^{3} \sqrt{d^{2} - e^{2} x^{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `x**2*sqrt(d**2 - e**2*x**2)/(d + e*x)**4` | $\frac{x^{2} \sqrt{d^{2} - e^{2} x^{2}}}{\left(d + e x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `x*sqrt(d**2 - e**2*x**2)/(d + e*x)**4` | $\frac{x \sqrt{d^{2} - e^{2} x^{2}}}{\left(d + e x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d**2 - e**2*x**2)/(d + e*x)**4` | $\frac{\sqrt{d^{2} - e^{2} x^{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)/(x*(d + e*x)**4)` | $\frac{\sqrt{d^{2} - e^{2} x^{2}}}{x \left(d + e x\right)^{4}}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)/(x**2*(d + e*x)**4)` | $\frac{\sqrt{d^{2} - e^{2} x^{2}}}{x^{2} \left(d + e x\right)^{4}}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)/(x**3*(d + e*x)**4)` | $\frac{\sqrt{d^{2} - e^{2} x^{2}}}{x^{3} \left(d + e x\right)^{4}}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)/(x**4*(d + e*x)**4)` | $\frac{\sqrt{d^{2} - e^{2} x^{2}}}{x^{4} \left(d + e x\right)^{4}}$ |
| partial | parametric | `x**5*(d**2 - e**2*x**2)**(5/2)/(d + e*x)**4` | $\frac{x^{5} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `x**4*(d**2 - e**2*x**2)**(5/2)/(d + e*x)**4` | $\frac{x^{4} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `x**3*(d**2 - e**2*x**2)**(5/2)/(d + e*x)**4` | $\frac{x^{3} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `x**2*(d**2 - e**2*x**2)**(5/2)/(d + e*x)**4` | $\frac{x^{2} \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `x*(d**2 - e**2*x**2)**(5/2)/(d + e*x)**4` | $\frac{x \left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(d + e*x)**4` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right)^{4}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x*(d + e*x)**4)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x \left(d + e x\right)^{4}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**2*(d + e*x)**4)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{2} \left(d + e x\right)^{4}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**3*(d + e*x)**4)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{3} \left(d + e x\right)^{4}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**4*(d + e*x)**4)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{4} \left(d + e x\right)^{4}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**5*(d + e*x)**4)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{5} \left(d + e x\right)^{4}}$ |
| partial | parametric | `(d**2 - e**2*x**2)**(5/2)/(x**6*(d + e*x)**4)` | $\frac{\left(d^{2} - e^{2} x^{2}\right)^{\frac{5}{2}}}{x^{6} \left(d + e x\right)^{4}}$ |
| partial | parametric | `x**2*sqrt(-a**2*x**2 + 1)/(-a*x + 1)**4` | $\frac{x^{2} \sqrt{- a^{2} x^{2} + 1}}{\left(- a x + 1\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `x**2*sqrt(-a**2*x**2 + 1)/(-a*x + 1)**5` | $\frac{x^{2} \sqrt{- a^{2} x^{2} + 1}}{\left(- a x + 1\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `x**3/((d + e*x)**4*(d**2 - e**2*x**2)**(7/2))` | $\frac{x^{3}}{\left(d + e x\right)^{4} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2/((d + e*x)**4*(d**2 - e**2*x**2)**(7/2))` | $\frac{x^{2}}{\left(d + e x\right)^{4} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/((d + e*x)**4*(d**2 - e**2*x**2)**(7/2))` | $\frac{x}{\left(d + e x\right)^{4} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)**4*(d**2 - e**2*x**2)**(7/2))` | $\frac{1}{\left(d + e x\right)^{4} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `1/(x*(d + e*x)**4*(d**2 - e**2*x**2)**(7/2))` | $\frac{1}{x \left(d + e x\right)^{4} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `1/(x**2*(d + e*x)**4*(d**2 - e**2*x**2)**(7/2))` | $\frac{1}{x^{2} \left(d + e x\right)^{4} \left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `sqrt(-a**2*x**2 + 1)*sqrt(-a*c*x + c)/x**2` | $\frac{\sqrt{- a^{2} x^{2} + 1} \sqrt{- a c x + c}}{x^{2}}$ |
| partial | parametric | `sqrt(-a*c*x + c)/(x*sqrt(-a**2*x**2 + 1))` | $\frac{\sqrt{- a c x + c}}{x \sqrt{- a^{2} x^{2} + 1}}$ |
| partial | parametric | `sqrt(-a*x + 1)/sqrt(x)` | $\frac{\sqrt{- a x + 1}}{\sqrt{x}}$ |
| partial | parametric | `sqrt(-a**2*x**2 + 1)/(sqrt(x)*sqrt(a*x + 1))` | $\frac{\sqrt{- a^{2} x^{2} + 1}}{\sqrt{x} \sqrt{a x + 1}}$ |
| partial | parametric | `sqrt(a*x + 1)/sqrt(x)` | $\frac{\sqrt{a x + 1}}{\sqrt{x}}$ |
| partial | parametric | `sqrt(-a**2*x**2 + 1)/(sqrt(x)*sqrt(-a*x + 1))` | $\frac{\sqrt{- a^{2} x^{2} + 1}}{\sqrt{x} \sqrt{- a x + 1}}$ |
| partial | parametric | `sqrt(x)*sqrt(-a*x + 1)` | $\sqrt{x} \sqrt{- a x + 1}$ |
| partial | parametric | `sqrt(x)*sqrt(-a**2*x**2 + 1)/sqrt(a*x + 1)` | $\frac{\sqrt{x} \sqrt{- a^{2} x^{2} + 1}}{\sqrt{a x + 1}}$ |
| partial | concrete | `x*sqrt(x + 1)/(x**2 + 1)` | $\frac{x \sqrt{x + 1}}{x^{2} + 1}$ |
| partial | parametric | `x**4*sqrt(a + c*x**2)/(d + e*x)` | $\frac{x^{4} \sqrt{a + c x^{2}}}{d + e x}$ |
| partial | parametric | `x**3*sqrt(a + c*x**2)/(d + e*x)` | $\frac{x^{3} \sqrt{a + c x^{2}}}{d + e x}$ |
| partial | parametric | `x**2*sqrt(a + c*x**2)/(d + e*x)` | $\frac{x^{2} \sqrt{a + c x^{2}}}{d + e x}$ |
| partial | parametric | `x*sqrt(a + c*x**2)/(d + e*x)` | $\frac{x \sqrt{a + c x^{2}}}{d + e x}$ |
| partial | parametric | `sqrt(a + c*x**2)/(d + e*x)` | $\frac{\sqrt{a + c x^{2}}}{d + e x}$ |
| partial | parametric | `sqrt(a + c*x**2)/(x*(d + e*x))` | $\frac{\sqrt{a + c x^{2}}}{x \left(d + e x\right)}$ |
| partial | parametric | `sqrt(a + c*x**2)/(x**2*(d + e*x))` | $\frac{\sqrt{a + c x^{2}}}{x^{2} \left(d + e x\right)}$ |
| partial | parametric | `sqrt(a + c*x**2)/(x**3*(d + e*x))` | $\frac{\sqrt{a + c x^{2}}}{x^{3} \left(d + e x\right)}$ |
| partial | parametric | `sqrt(a + c*x**2)/(x**4*(d + e*x))` | $\frac{\sqrt{a + c x^{2}}}{x^{4} \left(d + e x\right)}$ |
| partial | parametric | `sqrt(a + c*x**2)/(x**5*(d + e*x))` | $\frac{\sqrt{a + c x^{2}}}{x^{5} \left(d + e x\right)}$ |
| partial | parametric | `x**4/(sqrt(a + c*x**2)*(d + e*x))` | $\frac{x^{4}}{\sqrt{a + c x^{2}} \left(d + e x\right)}$ |
| partial | parametric | `x**3/(sqrt(a + c*x**2)*(d + e*x))` | $\frac{x^{3}}{\sqrt{a + c x^{2}} \left(d + e x\right)}$ |
| partial | parametric | `x**2/(sqrt(a + c*x**2)*(d + e*x))` | $\frac{x^{2}}{\sqrt{a + c x^{2}} \left(d + e x\right)}$ |
| partial | parametric | `x/(sqrt(a + c*x**2)*(d + e*x))` | $\frac{x}{\sqrt{a + c x^{2}} \left(d + e x\right)}$ |
| partial | parametric | `1/(sqrt(a + c*x**2)*(d + e*x))` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right)}$ |
| partial | parametric | `1/(x*sqrt(a + c*x**2)*(d + e*x))` | $\frac{1}{x \sqrt{a + c x^{2}} \left(d + e x\right)}$ |
| partial | parametric | `1/(x**2*sqrt(a + c*x**2)*(d + e*x))` | $\frac{1}{x^{2} \sqrt{a + c x^{2}} \left(d + e x\right)}$ |
| partial | parametric | `1/(x**3*sqrt(a + c*x**2)*(d + e*x))` | $\frac{1}{x^{3} \sqrt{a + c x^{2}} \left(d + e x\right)}$ |
| partial | parametric | `x**4/((a + c*x**2)**(3/2)*(d + e*x))` | $\frac{x^{4}}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)}$ |
| partial | parametric | `x**3/((a + c*x**2)**(3/2)*(d + e*x))` | $\frac{x^{3}}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)}$ |
| partial | parametric | `x**2/((a + c*x**2)**(3/2)*(d + e*x))` | $\frac{x^{2}}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)}$ |
| partial | parametric | `x/((a + c*x**2)**(3/2)*(d + e*x))` | $\frac{x}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)}$ |
| partial | parametric | `1/((a + c*x**2)**(3/2)*(d + e*x))` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)}$ |
| partial | parametric | `1/(x*(a + c*x**2)**(3/2)*(d + e*x))` | $\frac{1}{x \left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)}$ |
| partial | parametric | `1/(x**2*(a + c*x**2)**(3/2)*(d + e*x))` | $\frac{1}{x^{2} \left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)}$ |
| partial | parametric | `1/(x**3*(a + c*x**2)**(3/2)*(d + e*x))` | $\frac{1}{x^{3} \left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x\right)}$ |
| partial | parametric | `x**5/(sqrt(a + c*x**2)*(d + e*x)**2)` | $\frac{x^{5}}{\sqrt{a + c x^{2}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `x**4/(sqrt(a + c*x**2)*(d + e*x)**2)` | $\frac{x^{4}}{\sqrt{a + c x^{2}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `x**3/(sqrt(a + c*x**2)*(d + e*x)**2)` | $\frac{x^{3}}{\sqrt{a + c x^{2}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `x**2/(sqrt(a + c*x**2)*(d + e*x)**2)` | $\frac{x^{2}}{\sqrt{a + c x^{2}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `x/(sqrt(a + c*x**2)*(d + e*x)**2)` | $\frac{x}{\sqrt{a + c x^{2}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `1/(sqrt(a + c*x**2)*(d + e*x)**2)` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `1/(x*sqrt(a + c*x**2)*(d + e*x)**2)` | $\frac{1}{x \sqrt{a + c x^{2}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `1/(x**2*sqrt(a + c*x**2)*(d + e*x)**2)` | $\frac{1}{x^{2} \sqrt{a + c x^{2}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `1/(x**3*sqrt(a + c*x**2)*(d + e*x)**2)` | $\frac{1}{x^{3} \sqrt{a + c x^{2}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `x**3*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)` | $\frac{x^{3} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{d + e x}$ |
| partial | parametric | `x**2*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)` | $\frac{x^{2} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{d + e x}$ |
| partial | parametric | `x*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)` | $\frac{x \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{d + e x}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{d + e x}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(x*(d + e*x))` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{x \left(d + e x\right)}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(x**2*(d + e*x))` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{x^{2} \left(d + e x\right)}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(x**3*(d + e*x))` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{x^{3} \left(d + e x\right)}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(x**4*(d + e*x))` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{x^{4} \left(d + e x\right)}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(x**5*(d + e*x))` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{x^{5} \left(d + e x\right)}$ |
| partial | parametric | `x**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)` | $\frac{x^{3} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `x**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)` | $\frac{x^{2} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `x*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)` | $\frac{x \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(x*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{x \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(x**2*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{x^{2} \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(x**3*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{x^{3} \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(x**4*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{x^{4} \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(x**5*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{x^{5} \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(x**6*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{x^{6} \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(x**7*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{x^{7} \left(d + e x\right)}$ |
| partial | parametric | `x**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)` | $\frac{x^{3} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `x**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)` | $\frac{x^{2} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `x*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)` | $\frac{x \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{d + e x}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(x*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{x \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(x**2*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{x^{2} \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(x**3*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{x^{3} \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(x**4*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{x^{4} \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(x**5*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{x^{5} \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(x**6*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{x^{6} \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(x**7*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{x^{7} \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(x**8*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{x^{8} \left(d + e x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(x**9*(d + e*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{x^{9} \left(d + e x\right)}$ |
| partial | parametric | `x**2/((d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{x^{2}}{\left(d + e x\right) \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `x/((d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{x}{\left(d + e x\right) \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{\left(d + e x\right) \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `1/(x*(d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{x \left(d + e x\right) \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `1/(x**2*(d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{x^{2} \left(d + e x\right) \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `1/(x**3*(d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{1}{x^{3} \left(d + e x\right) \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `x**5/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{x^{5}}{\left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{x^{4}}{\left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{x^{3}}{\left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{x^{2}}{\left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{x}{\left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{\left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{x \left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{x^{2} \left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{x^{3} \left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{1}{x^{4} \left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{x^{2}}{\left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `x**2/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(7/2))` | $\frac{x^{2}}{\left(d + e x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{7}{2}}}$ |
| partial | concrete | `x**3*sqrt(x + 1)*sqrt(x**2 - x + 1)` | $x^{3} \sqrt{x + 1} \sqrt{x^{2} - x + 1}$ |
| **SOLVED-NEW** | concrete | `x**2*sqrt(x + 1)*sqrt(x**2 - x + 1)` | $x^{2} \sqrt{x + 1} \sqrt{x^{2} - x + 1}$ |
| partial | concrete | `x*sqrt(x + 1)*sqrt(x**2 - x + 1)` | $x \sqrt{x + 1} \sqrt{x^{2} - x + 1}$ |
| partial | concrete | `sqrt(x + 1)*sqrt(x**2 - x + 1)` | $\sqrt{x + 1} \sqrt{x^{2} - x + 1}$ |
| partial | concrete | `sqrt(x + 1)*sqrt(x**2 - x + 1)/x` | $\frac{\sqrt{x + 1} \sqrt{x^{2} - x + 1}}{x}$ |
| partial | concrete | `sqrt(x + 1)*sqrt(x**2 - x + 1)/x**2` | $\frac{\sqrt{x + 1} \sqrt{x^{2} - x + 1}}{x^{2}}$ |
| partial | concrete | `sqrt(x + 1)*sqrt(x**2 - x + 1)/x**3` | $\frac{\sqrt{x + 1} \sqrt{x^{2} - x + 1}}{x^{3}}$ |
| partial | concrete | `x**3*(x + 1)**(3/2)*(x**2 - x + 1)**(3/2)` | $x^{3} \left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | concrete | `x**2*(x + 1)**(3/2)*(x**2 - x + 1)**(3/2)` | $x^{2} \left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}$ |
| partial | concrete | `x*(x + 1)**(3/2)*(x**2 - x + 1)**(3/2)` | $x \left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}$ |
| partial | concrete | `(x + 1)**(3/2)*(x**2 - x + 1)**(3/2)` | $\left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}$ |
| partial | concrete | `(x + 1)**(3/2)*(x**2 - x + 1)**(3/2)/x` | $\frac{\left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}}{x}$ |
| partial | concrete | `(x + 1)**(3/2)*(x**2 - x + 1)**(3/2)/x**2` | $\frac{\left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | concrete | `(x + 1)**(3/2)*(x**2 - x + 1)**(3/2)/x**3` | $\frac{\left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | concrete | `x**3/(sqrt(x + 1)*sqrt(x**2 - x + 1))` | $\frac{x^{3}}{\sqrt{x + 1} \sqrt{x^{2} - x + 1}}$ |
| **SOLVED-NEW** | concrete | `x**2/(sqrt(x + 1)*sqrt(x**2 - x + 1))` | $\frac{x^{2}}{\sqrt{x + 1} \sqrt{x^{2} - x + 1}}$ |
| partial | concrete | `x/(sqrt(x + 1)*sqrt(x**2 - x + 1))` | $\frac{x}{\sqrt{x + 1} \sqrt{x^{2} - x + 1}}$ |
| partial | concrete | `1/(sqrt(x + 1)*sqrt(x**2 - x + 1))` | $\frac{1}{\sqrt{x + 1} \sqrt{x^{2} - x + 1}}$ |
| partial | concrete | `1/(x*sqrt(x + 1)*sqrt(x**2 - x + 1))` | $\frac{1}{x \sqrt{x + 1} \sqrt{x^{2} - x + 1}}$ |
| partial | concrete | `1/(x**2*sqrt(x + 1)*sqrt(x**2 - x + 1))` | $\frac{1}{x^{2} \sqrt{x + 1} \sqrt{x^{2} - x + 1}}$ |
| partial | concrete | `1/(x**3*sqrt(x + 1)*sqrt(x**2 - x + 1))` | $\frac{1}{x^{3} \sqrt{x + 1} \sqrt{x^{2} - x + 1}}$ |
| partial | concrete | `x**3/((x + 1)**(3/2)*(x**2 - x + 1)**(3/2))` | $\frac{x^{3}}{\left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | concrete | `x**2/((x + 1)**(3/2)*(x**2 - x + 1)**(3/2))` | $\frac{x^{2}}{\left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x/((x + 1)**(3/2)*(x**2 - x + 1)**(3/2))` | $\frac{x}{\left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((x + 1)**(3/2)*(x**2 - x + 1)**(3/2))` | $\frac{1}{\left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x*(x + 1)**(3/2)*(x**2 - x + 1)**(3/2))` | $\frac{1}{x \left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**2*(x + 1)**(3/2)*(x**2 - x + 1)**(3/2))` | $\frac{1}{x^{2} \left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**3*(x + 1)**(3/2)*(x**2 - x + 1)**(3/2))` | $\frac{1}{x^{3} \left(x + 1\right)^{\frac{3}{2}} \left(x^{2} - x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**3/((x + 1)**(5/2)*(x**2 - x + 1)**(5/2))` | $\frac{x^{3}}{\left(x + 1\right)^{\frac{5}{2}} \left(x^{2} - x + 1\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | concrete | `x**2/((x + 1)**(5/2)*(x**2 - x + 1)**(5/2))` | $\frac{x^{2}}{\left(x + 1\right)^{\frac{5}{2}} \left(x^{2} - x + 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x/((x + 1)**(5/2)*(x**2 - x + 1)**(5/2))` | $\frac{x}{\left(x + 1\right)^{\frac{5}{2}} \left(x^{2} - x + 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((x + 1)**(5/2)*(x**2 - x + 1)**(5/2))` | $\frac{1}{\left(x + 1\right)^{\frac{5}{2}} \left(x^{2} - x + 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(x*(x + 1)**(5/2)*(x**2 - x + 1)**(5/2))` | $\frac{1}{x \left(x + 1\right)^{\frac{5}{2}} \left(x^{2} - x + 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(x**2*(x + 1)**(5/2)*(x**2 - x + 1)**(5/2))` | $\frac{1}{x^{2} \left(x + 1\right)^{\frac{5}{2}} \left(x^{2} - x + 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(x**3*(x + 1)**(5/2)*(x**2 - x + 1)**(5/2))` | $\frac{1}{x^{3} \left(x + 1\right)^{\frac{5}{2}} \left(x^{2} - x + 1\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4*sqrt(d + e*x)/(a + b*x + c*x**2)` | $\frac{x^{4} \sqrt{d + e x}}{a + b x + c x^{2}}$ |
| partial | parametric | `x**2*sqrt(d + e*x)/(a + b*x + c*x**2)` | $\frac{x^{2} \sqrt{d + e x}}{a + b x + c x^{2}}$ |
| partial | parametric | `x*sqrt(d + e*x)/(a + b*x + c*x**2)` | $\frac{x \sqrt{d + e x}}{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(a + b*x + c*x**2)` | $\frac{\sqrt{d + e x}}{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(d + e*x)/(x*(a + b*x + c*x**2))` | $\frac{\sqrt{d + e x}}{x \left(a + b x + c x^{2}\right)}$ |
| timeout | parametric | `sqrt(d + e*x)/(x**2*(a + b*x + c*x**2))` | $\frac{\sqrt{d + e x}}{x^{2} \left(a + b x + c x^{2}\right)}$ |
| timeout | parametric | `sqrt(d + e*x)/(x**3*(a + b*x + c*x**2))` | $\frac{\sqrt{d + e x}}{x^{3} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `x**4*(d + e*x)**(3/2)/(a + b*x + c*x**2)` | $\frac{x^{4} \left(d + e x\right)^{\frac{3}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `x**3*(d + e*x)**(3/2)/(a + b*x + c*x**2)` | $\frac{x^{3} \left(d + e x\right)^{\frac{3}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `x**2*(d + e*x)**(3/2)/(a + b*x + c*x**2)` | $\frac{x^{2} \left(d + e x\right)^{\frac{3}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `x*(d + e*x)**(3/2)/(a + b*x + c*x**2)` | $\frac{x \left(d + e x\right)^{\frac{3}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(a + b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{a + b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(x*(a + b*x + c*x**2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{x \left(a + b x + c x^{2}\right)}$ |
| timeout | parametric | `(d + e*x)**(3/2)/(x**2*(a + b*x + c*x**2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{x^{2} \left(a + b x + c x^{2}\right)}$ |
| timeout | parametric | `(d + e*x)**(3/2)/(x**3*(a + b*x + c*x**2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{x^{3} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `(d + e*x)**3*(f + g*x)**5/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{3} \left(f + g x\right)^{5}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**3*(f + g*x)**4/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{3} \left(f + g x\right)^{4}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**3*(f + g*x)**3/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{3} \left(f + g x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3*(f + g*x)**2/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{3} \left(f + g x\right)^{2}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3*(f + g*x)/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{3} \left(f + g x\right)}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | $\frac{\left(d + e x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**3/((d**2 - e**2*x**2)**(7/2)*(f + g*x))` | $\frac{\left(d + e x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}} \left(f + g x\right)}$ |
| partial | parametric | `(d + e*x)**3/((d**2 - e**2*x**2)**(7/2)*(f + g*x)**2)` | $\frac{\left(d + e x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}} \left(f + g x\right)^{2}}$ |
| partial | parametric | `(d + e*x)**3/((d**2 - e**2*x**2)**(7/2)*(f + g*x)**3)` | $\frac{\left(d + e x\right)^{3}}{\left(d^{2} - e^{2} x^{2}\right)^{\frac{7}{2}} \left(f + g x\right)^{3}}$ |
| partial | parametric | `(a + c*x**2)/((d + e*x)**(3/2)*(f + g*x))` | $\frac{a + c x^{2}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)}$ |
| SOLVED-both | parametric | `(a + c*x**2)*(d + e*x)**3/sqrt(f + g*x)` | $\frac{\left(a + c x^{2}\right) \left(d + e x\right)^{3}}{\sqrt{f + g x}}$ |
| SOLVED-both | parametric | `(a + c*x**2)*(d + e*x)**2/sqrt(f + g*x)` | $\frac{\left(a + c x^{2}\right) \left(d + e x\right)^{2}}{\sqrt{f + g x}}$ |
| SOLVED-both | parametric | `(a + c*x**2)*(d + e*x)/sqrt(f + g*x)` | $\frac{\left(a + c x^{2}\right) \left(d + e x\right)}{\sqrt{f + g x}}$ |
| SOLVED-both | parametric | `(a + c*x**2)/sqrt(f + g*x)` | $\frac{a + c x^{2}}{\sqrt{f + g x}}$ |
| partial | parametric | `(a + c*x**2)/((d + e*x)*sqrt(f + g*x))` | $\frac{a + c x^{2}}{\left(d + e x\right) \sqrt{f + g x}}$ |
| partial | parametric | `(a + c*x**2)/((d + e*x)**2*sqrt(f + g*x))` | $\frac{a + c x^{2}}{\left(d + e x\right)^{2} \sqrt{f + g x}}$ |
| partial | parametric | `(a + c*x**2)/((d + e*x)**3*sqrt(f + g*x))` | $\frac{a + c x^{2}}{\left(d + e x\right)^{3} \sqrt{f + g x}}$ |
| SOLVED-both | parametric | `(a + c*x**2)*(d + e*x)**3/(f + g*x)**(3/2)` | $\frac{\left(a + c x^{2}\right) \left(d + e x\right)^{3}}{\left(f + g x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)*(d + e*x)**2/(f + g*x)**(3/2)` | $\frac{\left(a + c x^{2}\right) \left(d + e x\right)^{2}}{\left(f + g x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)*(d + e*x)/(f + g*x)**(3/2)` | $\frac{\left(a + c x^{2}\right) \left(d + e x\right)}{\left(f + g x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + c*x**2)/(f + g*x)**(3/2)` | $\frac{a + c x^{2}}{\left(f + g x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + c*x**2)/((d + e*x)*(f + g*x)**(3/2))` | $\frac{a + c x^{2}}{\left(d + e x\right) \left(f + g x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + c*x**2)/((d + e*x)**2*(f + g*x)**(3/2))` | $\frac{a + c x^{2}}{\left(d + e x\right)^{2} \left(f + g x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + c*x**2)/((d + e*x)**3*(f + g*x)**(3/2))` | $\frac{a + c x^{2}}{\left(d + e x\right)^{3} \left(f + g x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + c*x**2)/(sqrt(d + e*x)*sqrt(f + g*x))` | $\frac{a + c x^{2}}{\sqrt{d + e x} \sqrt{f + g x}}$ |
| SOLVED-both | concrete | `(2*x**2 - 1)/(sqrt(x - 1)*sqrt(x + 1))` | $\frac{2 x^{2} - 1}{\sqrt{x - 1} \sqrt{x + 1}}$ |
| timeout | parametric | `(d + e*x)**(3/2)*sqrt(f + g*x)/(a + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \sqrt{f + g x}}{a + c x^{2}}$ |
| timeout | parametric | `sqrt(d + e*x)*sqrt(f + g*x)/(a + c*x**2)` | $\frac{\sqrt{d + e x} \sqrt{f + g x}}{a + c x^{2}}$ |
| timeout | parametric | `sqrt(f + g*x)/((a + c*x**2)*sqrt(d + e*x))` | $\frac{\sqrt{f + g x}}{\left(a + c x^{2}\right) \sqrt{d + e x}}$ |
| timeout | parametric | `sqrt(f + g*x)/((a + c*x**2)*(d + e*x)**(3/2))` | $\frac{\sqrt{f + g x}}{\left(a + c x^{2}\right) \left(d + e x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(f + g*x)/((a + c*x**2)*(d + e*x)**(5/2))` | $\frac{\sqrt{f + g x}}{\left(a + c x^{2}\right) \left(d + e x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(d + e*x)**(3/2)/((a + c*x**2)*sqrt(f + g*x))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a + c x^{2}\right) \sqrt{f + g x}}$ |
| timeout | parametric | `sqrt(d + e*x)/((a + c*x**2)*sqrt(f + g*x))` | $\frac{\sqrt{d + e x}}{\left(a + c x^{2}\right) \sqrt{f + g x}}$ |
| timeout | parametric | `1/((a + c*x**2)*sqrt(d + e*x)*sqrt(f + g*x))` | $\frac{1}{\left(a + c x^{2}\right) \sqrt{d + e x} \sqrt{f + g x}}$ |
| timeout | parametric | `1/((a + c*x**2)*(d + e*x)**(3/2)*sqrt(f + g*x))` | $\frac{1}{\left(a + c x^{2}\right) \left(d + e x\right)^{\frac{3}{2}} \sqrt{f + g x}}$ |
| timeout | parametric | `(d + e*x)**(3/2)/((a + c*x**2)*(f + g*x)**(3/2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a + c x^{2}\right) \left(f + g x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `sqrt(d + e*x)/((a + c*x**2)*(f + g*x)**(3/2))` | $\frac{\sqrt{d + e x}}{\left(a + c x^{2}\right) \left(f + g x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/((a + c*x**2)*sqrt(d + e*x)*(f + g*x)**(3/2))` | $\frac{1}{\left(a + c x^{2}\right) \sqrt{d + e x} \left(f + g x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/((a + c*x**2)*(d + e*x)**(3/2)*(f + g*x)**(3/2))` | $\frac{1}{\left(a + c x^{2}\right) \left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(x)/(sqrt(x + 1)*(x**2 + 1))` | $\frac{\sqrt{x}}{\sqrt{x + 1} \left(x^{2} + 1\right)}$ |
| partial | parametric | `sqrt(1 - x**2)*(f + g*x)**2/(1 - x)**4` | $\frac{\sqrt{1 - x^{2}} \left(f + g x\right)^{2}}{\left(1 - x\right)^{4}}$ |
| partial | parametric | `(-a**2*x**2 + 1)**(3/2)/((c + d*x)*(-a*x + 1)**2)` | $\frac{\left(- a^{2} x^{2} + 1\right)^{\frac{3}{2}}}{\left(c + d x\right) \left(- a x + 1\right)^{2}}$ |
| partial | parametric | `(a*x + 1)**2/((c + d*x)*sqrt(-a**2*x**2 + 1))` | $\frac{\left(a x + 1\right)^{2}}{\left(c + d x\right) \sqrt{- a^{2} x^{2} + 1}}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x)**3*sqrt(f + g*x)` | $\sqrt{a + c x^{2}} \left(d + e x\right)^{3} \sqrt{f + g x}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x)**2*sqrt(f + g*x)` | $\sqrt{a + c x^{2}} \left(d + e x\right)^{2} \sqrt{f + g x}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x)*sqrt(f + g*x)` | $\sqrt{a + c x^{2}} \left(d + e x\right) \sqrt{f + g x}$ |
| partial | parametric | `sqrt(a + c*x**2)*sqrt(f + g*x)` | $\sqrt{a + c x^{2}} \sqrt{f + g x}$ |
| timeout | parametric | `sqrt(a + c*x**2)*sqrt(f + g*x)/(d + e*x)` | $\frac{\sqrt{a + c x^{2}} \sqrt{f + g x}}{d + e x}$ |
| timeout | parametric | `sqrt(a + c*x**2)*sqrt(f + g*x)/(d + e*x)**2` | $\frac{\sqrt{a + c x^{2}} \sqrt{f + g x}}{\left(d + e x\right)^{2}}$ |
| timeout | parametric | `sqrt(a + c*x**2)*sqrt(f + g*x)/(d + e*x)**3` | $\frac{\sqrt{a + c x^{2}} \sqrt{f + g x}}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x)**3/sqrt(f + g*x)` | $\frac{\sqrt{a + c x^{2}} \left(d + e x\right)^{3}}{\sqrt{f + g x}}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x)**2/sqrt(f + g*x)` | $\frac{\sqrt{a + c x^{2}} \left(d + e x\right)^{2}}{\sqrt{f + g x}}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x)/sqrt(f + g*x)` | $\frac{\sqrt{a + c x^{2}} \left(d + e x\right)}{\sqrt{f + g x}}$ |
| partial | parametric | `sqrt(a + c*x**2)/sqrt(f + g*x)` | $\frac{\sqrt{a + c x^{2}}}{\sqrt{f + g x}}$ |
| timeout | parametric | `sqrt(a + c*x**2)/((d + e*x)*sqrt(f + g*x))` | $\frac{\sqrt{a + c x^{2}}}{\left(d + e x\right) \sqrt{f + g x}}$ |
| timeout | parametric | `sqrt(a + c*x**2)/((d + e*x)**2*sqrt(f + g*x))` | $\frac{\sqrt{a + c x^{2}}}{\left(d + e x\right)^{2} \sqrt{f + g x}}$ |
| timeout | parametric | `sqrt(a + c*x**2)/((d + e*x)**3*sqrt(f + g*x))` | $\frac{\sqrt{a + c x^{2}}}{\left(d + e x\right)^{3} \sqrt{f + g x}}$ |
| partial | parametric | `(d + e*x)**3*sqrt(f + g*x)/sqrt(a + c*x**2)` | $\frac{\left(d + e x\right)^{3} \sqrt{f + g x}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**2*sqrt(f + g*x)/sqrt(a + c*x**2)` | $\frac{\left(d + e x\right)^{2} \sqrt{f + g x}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(d + e*x)*sqrt(f + g*x)/sqrt(a + c*x**2)` | $\frac{\left(d + e x\right) \sqrt{f + g x}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `sqrt(f + g*x)/sqrt(a + c*x**2)` | $\frac{\sqrt{f + g x}}{\sqrt{a + c x^{2}}}$ |
| timeout | parametric | `sqrt(f + g*x)/(sqrt(a + c*x**2)*(d + e*x))` | $\frac{\sqrt{f + g x}}{\sqrt{a + c x^{2}} \left(d + e x\right)}$ |
| timeout | parametric | `sqrt(f + g*x)/(sqrt(a + c*x**2)*(d + e*x)**2)` | $\frac{\sqrt{f + g x}}{\sqrt{a + c x^{2}} \left(d + e x\right)^{2}}$ |
| timeout | parametric | `sqrt(f + g*x)/(sqrt(a + c*x**2)*(d + e*x)**3)` | $\frac{\sqrt{f + g x}}{\sqrt{a + c x^{2}} \left(d + e x\right)^{3}}$ |
| timeout | parametric | `(f + g*x)**(3/2)/(sqrt(a + c*x**2)*(d + e*x))` | $\frac{\left(f + g x\right)^{\frac{3}{2}}}{\sqrt{a + c x^{2}} \left(d + e x\right)}$ |
| partial | parametric | `(d + e*x)**3/(sqrt(a + c*x**2)*sqrt(f + g*x))` | $\frac{\left(d + e x\right)^{3}}{\sqrt{a + c x^{2}} \sqrt{f + g x}}$ |
| partial | parametric | `(d + e*x)**2/(sqrt(a + c*x**2)*sqrt(f + g*x))` | $\frac{\left(d + e x\right)^{2}}{\sqrt{a + c x^{2}} \sqrt{f + g x}}$ |
| partial | parametric | `(d + e*x)/(sqrt(a + c*x**2)*sqrt(f + g*x))` | $\frac{d + e x}{\sqrt{a + c x^{2}} \sqrt{f + g x}}$ |
| partial | parametric | `1/(sqrt(a + c*x**2)*sqrt(f + g*x))` | $\frac{1}{\sqrt{a + c x^{2}} \sqrt{f + g x}}$ |
| timeout | parametric | `1/(sqrt(a + c*x**2)*(d + e*x)*sqrt(f + g*x))` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right) \sqrt{f + g x}}$ |
| timeout | parametric | `1/(sqrt(a + c*x**2)*(d + e*x)**2*sqrt(f + g*x))` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right)^{2} \sqrt{f + g x}}$ |
| timeout | parametric | `1/(sqrt(a + c*x**2)*(d + e*x)**3*sqrt(f + g*x))` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right)^{3} \sqrt{f + g x}}$ |
| timeout | parametric | `1/(sqrt(a + c*x**2)*(d + e*x)*(f + g*x)**(3/2))` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right) \left(f + g x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/(sqrt(a + c*x**2)*(d + e*x)*(f + g*x)**(5/2))` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x\right) \left(f + g x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `1/((d + e*x)*sqrt(f + g*x)*sqrt(c*x**2 + 1))` | $\frac{1}{\left(d + e x\right) \sqrt{f + g x} \sqrt{c x^{2} + 1}}$ |
| timeout | parametric | `1/(sqrt(a + c*x**2)*sqrt(d + e*x)*sqrt(f + g*x))` | $\frac{1}{\sqrt{a + c x^{2}} \sqrt{d + e x} \sqrt{f + g x}}$ |
| partial | concrete | `1/(sqrt(x - 1)*sqrt(x + 1)*sqrt(2*x**2 - 1))` | $\frac{1}{\sqrt{x - 1} \sqrt{x + 1} \sqrt{2 x^{2} - 1}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d + e*x)*(f + g*x)**3/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\sqrt{d + e x} \left(f + g x\right)^{3}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d + e*x)*(f + g*x)**2/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\sqrt{d + e x} \left(f + g x\right)^{2}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d + e*x)*(f + g*x)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\sqrt{d + e x} \left(f + g x\right)}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d + e*x)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\sqrt{d + e x}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `sqrt(d + e*x)/((f + g*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\sqrt{d + e x}}{\left(f + g x\right) \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `sqrt(d + e*x)/((f + g*x)**2*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\sqrt{d + e x}}{\left(f + g x\right)^{2} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `sqrt(d + e*x)/((f + g*x)**3*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\sqrt{d + e x}}{\left(f + g x\right)^{3} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `sqrt(d + e*x)/((f + g*x)**4*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\sqrt{d + e x}}{\left(f + g x\right)^{4} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)*(f + g*x)**3/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{3}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)*(f + g*x)**2/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{2}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)*(f + g*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/((f + g*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(f + g x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/((f + g*x)**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(f + g x\right)^{2} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/((f + g*x)**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(f + g x\right)^{3} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(5/2)*(f + g*x)**3/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{3}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(5/2)*(f + g*x)**2/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{2}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(5/2)*(f + g*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(5/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/((f + g*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(f + g x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/((f + g*x)**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(f + g x\right)^{2} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/((f + g*x)**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(f + g x\right)^{3} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)**4*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | $\frac{\left(f + g x\right)^{4} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)**3*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | $\frac{\left(f + g x\right)^{3} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)**2*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | $\frac{\left(f + g x\right)^{2} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | $\frac{\left(f + g x\right) \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x}}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x))` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x} \left(f + g x\right)}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x)**2)` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x} \left(f + g x\right)^{2}}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x)**3)` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x} \left(f + g x\right)^{3}}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x)**4)` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x} \left(f + g x\right)^{4}}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x)**5)` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x} \left(f + g x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)**4*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(f + g x\right)^{4} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(f + g x\right)^{3} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(f + g x\right)^{2} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(f + g x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{2}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**3)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{3}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**4)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{4}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**5)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{5}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**6)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{6}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)**4*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(f + g x\right)^{4} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(f + g x\right)^{3} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(f + g x\right)^{2} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(f + g*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(f + g x\right) \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**2)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{2}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**3)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{3}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**4)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{4}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**5)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{5}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**6)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{6}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**7)` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{7}}$ |
| partial | parametric | `sqrt(d + e*x)*(f + g*x)**(5/2)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\sqrt{d + e x} \left(f + g x\right)^{\frac{5}{2}}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `sqrt(d + e*x)*(f + g*x)**(3/2)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\sqrt{d + e x} \left(f + g x\right)^{\frac{3}{2}}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `sqrt(d + e*x)*sqrt(f + g*x)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\sqrt{d + e x} \sqrt{f + g x}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `sqrt(d + e*x)/(sqrt(f + g*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\sqrt{d + e x}}{\sqrt{f + g x} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `sqrt(d + e*x)/((f + g*x)**(3/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\sqrt{d + e x}}{\left(f + g x\right)^{\frac{3}{2}} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `sqrt(d + e*x)/((f + g*x)**(5/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\sqrt{d + e x}}{\left(f + g x\right)^{\frac{5}{2}} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| partial | parametric | `sqrt(d + e*x)/((f + g*x)**(7/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\sqrt{d + e x}}{\left(f + g x\right)^{\frac{7}{2}} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| timeout | parametric | `sqrt(d + e*x)/((f + g*x)**(9/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\sqrt{d + e x}}{\left(f + g x\right)^{\frac{9}{2}} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| timeout | parametric | `(d + e*x)**(3/2)*(f + g*x)**(5/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{\frac{5}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(f + g*x)**(3/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{\frac{3}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)*sqrt(f + g*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \sqrt{f + g x}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/(sqrt(f + g*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\sqrt{f + g x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)/((f + g*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(f + g x\right)^{\frac{3}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(d + e*x)**(3/2)/((f + g*x)**(5/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(f + g x\right)^{\frac{5}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(d + e*x)**(3/2)/((f + g*x)**(7/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(f + g x\right)^{\frac{7}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(d + e*x)**(5/2)*(f + g*x)**(5/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{\frac{5}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(d + e*x)**(5/2)*(f + g*x)**(3/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{\frac{3}{2}}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)*sqrt(f + g*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | $\frac{\left(d + e x\right)^{\frac{5}{2}} \sqrt{f + g x}}{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x)**(5/2)/(sqrt(f + g*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\sqrt{f + g x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(d + e*x)**(5/2)/((f + g*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(f + g x\right)^{\frac{3}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(d + e*x)**(5/2)/((f + g*x)**(5/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | $\frac{\left(d + e x\right)^{\frac{5}{2}}}{\left(f + g x\right)^{\frac{5}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(f + g*x)**(5/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | $\frac{\left(f + g x\right)^{\frac{5}{2}} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x}}$ |
| partial | parametric | `(f + g*x)**(3/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | $\frac{\left(f + g x\right)^{\frac{3}{2}} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x}}$ |
| partial | parametric | `sqrt(f + g*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | $\frac{\sqrt{f + g x} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x}}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*sqrt(f + g*x))` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x} \sqrt{f + g x}}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x)**(3/2))` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x} \left(f + g x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x)**(5/2))` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x} \left(f + g x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x)**(7/2))` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x} \left(f + g x\right)^{\frac{7}{2}}}$ |
| timeout | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x)**(9/2))` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x} \left(f + g x\right)^{\frac{9}{2}}}$ |
| timeout | parametric | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x)**(11/2))` | $\frac{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}{\sqrt{d + e x} \left(f + g x\right)^{\frac{11}{2}}}$ |
| timeout | parametric | `(f + g*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | $\frac{\left(f + g x\right)^{\frac{3}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(f + g*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | $\frac{\sqrt{f + g x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*sqrt(f + g*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{f + g x}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**(3/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**(5/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**(7/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{\frac{7}{2}}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**(9/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{\frac{9}{2}}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**(11/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{\frac{11}{2}}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**(13/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{3}{2}}}{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{\frac{13}{2}}}$ |
| timeout | parametric | `(f + g*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | $\frac{\left(f + g x\right)^{\frac{3}{2}} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(f + g*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | $\frac{\sqrt{f + g x} \left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*sqrt(f + g*x))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{f + g x}}$ |
| partial | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**(3/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**(5/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**(7/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{\frac{7}{2}}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**(9/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{\frac{9}{2}}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**(11/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{\frac{11}{2}}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**(13/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{\frac{13}{2}}}$ |
| timeout | parametric | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**(15/2))` | $\frac{\left(a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)\right)^{\frac{5}{2}}}{\left(d + e x\right)^{\frac{5}{2}} \left(f + g x\right)^{\frac{15}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)*(f + g*x)**4/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{4}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)*(f + g*x)**3/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{3}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)*(f + g*x)**2/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)^{2}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)*(f + g*x)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(f + g x\right)}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x)**(3/2)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| timeout | parametric | `(d + e*x)**(3/2)/((f + g*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(f + g x\right) \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| timeout | parametric | `(d + e*x)**(3/2)/((f + g*x)**2*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(f + g x\right)^{2} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| timeout | parametric | `(d + e*x)**(3/2)/((f + g*x)**3*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(f + g x\right)^{3} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| timeout | parametric | `(d + e*x)**(3/2)/((f + g*x)**4*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\left(f + g x\right)^{4} \sqrt{a d e + c d e x^{2} + x \left(a e^{2} + c d^{2}\right)}}$ |
| timeout | parametric | `(a + b*x + c*x**2)**3/(sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(a + b*x + c*x**2)**2/(sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{\left(a + b x + c x^{2}\right)^{2}}{\sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `(a + b*x + c*x**2)/(sqrt(-d*x + 1)*sqrt(d*x + 1))` | $\frac{a + b x + c x^{2}}{\sqrt{- d x + 1} \sqrt{d x + 1}}$ |
| partial | parametric | `1/(sqrt(-d*x + 1)*sqrt(d*x + 1)*(a + b*x + c*x**2))` | $\frac{1}{\sqrt{- d x + 1} \sqrt{d x + 1} \left(a + b x + c x^{2}\right)}$ |
| timeout | parametric | `1/(sqrt(-d*x + 1)*sqrt(d*x + 1)*(a + b*x + c*x**2)**2)` | $\frac{1}{\sqrt{- d x + 1} \sqrt{d x + 1} \left(a + b x + c x^{2}\right)^{2}}$ |
| timeout | parametric | `(a + b*x + c*x**2)**3/((-d*x + 1)**(3/2)*(d*x + 1)**(3/2))` | $\frac{\left(a + b x + c x^{2}\right)^{3}}{\left(- d x + 1\right)^{\frac{3}{2}} \left(d x + 1\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)**2/((-d*x + 1)**(3/2)*(d*x + 1)**(3/2))` | $\frac{\left(a + b x + c x^{2}\right)^{2}}{\left(- d x + 1\right)^{\frac{3}{2}} \left(d x + 1\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)/((-d*x + 1)**(3/2)*(d*x + 1)**(3/2))` | $\frac{a + b x + c x^{2}}{\left(- d x + 1\right)^{\frac{3}{2}} \left(d x + 1\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `1/((-d*x + 1)**(3/2)*(d*x + 1)**(3/2)*(a + b*x + c*x**2))` | $\frac{1}{\left(- d x + 1\right)^{\frac{3}{2}} \left(d x + 1\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)}$ |
| timeout | parametric | `1/((-d*x + 1)**(3/2)*(d*x + 1)**(3/2)*(a + b*x + c*x**2)**2)` | $\frac{1}{\left(- d x + 1\right)^{\frac{3}{2}} \left(d x + 1\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)^{2}}$ |
| SOLVED-both | parametric | `(d + e*x)**3*(a + b*x + c*x**2)/sqrt(f + g*x)` | $\frac{\left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)}{\sqrt{f + g x}}$ |
| SOLVED-both | parametric | `(d + e*x)**2*(a + b*x + c*x**2)/sqrt(f + g*x)` | $\frac{\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)}{\sqrt{f + g x}}$ |
| SOLVED-both | parametric | `(d + e*x)*(a + b*x + c*x**2)/sqrt(f + g*x)` | $\frac{\left(d + e x\right) \left(a + b x + c x^{2}\right)}{\sqrt{f + g x}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)/sqrt(f + g*x)` | $\frac{a + b x + c x^{2}}{\sqrt{f + g x}}$ |
| partial | parametric | `(a + b*x + c*x**2)/((d + e*x)*sqrt(f + g*x))` | $\frac{a + b x + c x^{2}}{\left(d + e x\right) \sqrt{f + g x}}$ |
| partial | parametric | `(a + b*x + c*x**2)/((d + e*x)**2*sqrt(f + g*x))` | $\frac{a + b x + c x^{2}}{\left(d + e x\right)^{2} \sqrt{f + g x}}$ |
| partial | parametric | `(a + b*x + c*x**2)/((d + e*x)**3*sqrt(f + g*x))` | $\frac{a + b x + c x^{2}}{\left(d + e x\right)^{3} \sqrt{f + g x}}$ |
| SOLVED-both | parametric | `(d + e*x)**3*(a + b*x + c*x**2)/(f + g*x)**(3/2)` | $\frac{\left(d + e x\right)^{3} \left(a + b x + c x^{2}\right)}{\left(f + g x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)**2*(a + b*x + c*x**2)/(f + g*x)**(3/2)` | $\frac{\left(d + e x\right)^{2} \left(a + b x + c x^{2}\right)}{\left(f + g x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x)*(a + b*x + c*x**2)/(f + g*x)**(3/2)` | $\frac{\left(d + e x\right) \left(a + b x + c x^{2}\right)}{\left(f + g x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x + c*x**2)/(f + g*x)**(3/2)` | $\frac{a + b x + c x^{2}}{\left(f + g x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)/((d + e*x)*(f + g*x)**(3/2))` | $\frac{a + b x + c x^{2}}{\left(d + e x\right) \left(f + g x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)/((d + e*x)**2*(f + g*x)**(3/2))` | $\frac{a + b x + c x^{2}}{\left(d + e x\right)^{2} \left(f + g x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x + c*x**2)/((d + e*x)**3*(f + g*x)**(3/2))` | $\frac{a + b x + c x^{2}}{\left(d + e x\right)^{3} \left(f + g x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(x - 1)*sqrt(x + 1)/(-x**2 + x + 1)` | $\frac{\sqrt{x - 1} \sqrt{x + 1}}{- x^{2} + x + 1}$ |
| partial | parametric | `(a + b*x + c*x**2)/(sqrt(d + e*x)*sqrt(f + g*x))` | $\frac{a + b x + c x^{2}}{\sqrt{d + e x} \sqrt{f + g x}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(a + b*x + c*x**2)/sqrt(f + g*x)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(a + b x + c x^{2}\right)}{\sqrt{f + g x}}$ |
| partial | parametric | `sqrt(d + e*x)*(a + b*x + c*x**2)/sqrt(f + g*x)` | $\frac{\sqrt{d + e x} \left(a + b x + c x^{2}\right)}{\sqrt{f + g x}}$ |
| partial | parametric | `(a + b*x + c*x**2)/(sqrt(d + e*x)*sqrt(f + g*x))` | $\frac{a + b x + c x^{2}}{\sqrt{d + e x} \sqrt{f + g x}}$ |
| partial | parametric | `(a + b*x + c*x**2)/((d + e*x)**(3/2)*sqrt(f + g*x))` | $\frac{a + b x + c x^{2}}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{f + g x}}$ |
| partial | parametric | `(a + b*x + c*x**2)/((d + e*x)**(5/2)*sqrt(f + g*x))` | $\frac{a + b x + c x^{2}}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{f + g x}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x + c*x**2)/((d + e*x)**(7/2)*sqrt(f + g*x))` | $\frac{a + b x + c x^{2}}{\left(d + e x\right)^{\frac{7}{2}} \sqrt{f + g x}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x + c*x**2)/((d + e*x)**(9/2)*sqrt(f + g*x))` | $\frac{a + b x + c x^{2}}{\left(d + e x\right)^{\frac{9}{2}} \sqrt{f + g x}}$ |
| partial | parametric | `sqrt(d + e*x)*(a + b*x + c*x**2)/(e + f*x)**(3/2)` | $\frac{\sqrt{d + e x} \left(a + b x + c x^{2}\right)}{\left(e + f x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(15*d**2 + 20*d*e*x + 8*e**2*x**2)/sqrt(a + b*x)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(15 d^{2} + 20 d e x + 8 e^{2} x^{2}\right)}{\sqrt{a + b x}}$ |
| partial | parametric | `sqrt(d + e*x)*(15*d**2 + 20*d*e*x + 8*e**2*x**2)/sqrt(a + b*x)` | $\frac{\sqrt{d + e x} \left(15 d^{2} + 20 d e x + 8 e^{2} x^{2}\right)}{\sqrt{a + b x}}$ |
| partial | parametric | `(15*d**2 + 20*d*e*x + 8*e**2*x**2)/(sqrt(a + b*x)*sqrt(d + e*x))` | $\frac{15 d^{2} + 20 d e x + 8 e^{2} x^{2}}{\sqrt{a + b x} \sqrt{d + e x}}$ |
| partial | parametric | `(15*d**2 + 20*d*e*x + 8*e**2*x**2)/(sqrt(a + b*x)*(d + e*x)**(3/2))` | $\frac{15 d^{2} + 20 d e x + 8 e^{2} x^{2}}{\sqrt{a + b x} \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(15*d**2 + 20*d*e*x + 8*e**2*x**2)/(sqrt(a + b*x)*(d + e*x)**(5/2))` | $\frac{15 d^{2} + 20 d e x + 8 e^{2} x^{2}}{\sqrt{a + b x} \left(d + e x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(15*d**2 + 20*d*e*x + 8*e**2*x**2)/(sqrt(a + b*x)*(d + e*x)**(7/2))` | $\frac{15 d^{2} + 20 d e x + 8 e^{2} x^{2}}{\sqrt{a + b x} \left(d + e x\right)^{\frac{7}{2}}}$ |
| **SOLVED-NEW** | parametric | `(15*d**2 + 20*d*e*x + 8*e**2*x**2)/(sqrt(a + b*x)*(d + e*x)**(9/2))` | $\frac{15 d^{2} + 20 d e x + 8 e^{2} x^{2}}{\sqrt{a + b x} \left(d + e x\right)^{\frac{9}{2}}}$ |
| timeout | parametric | `(d + e*x)**(3/2)/(sqrt(f + g*x)*(a + b*x + c*x**2))` | $\frac{\left(d + e x\right)^{\frac{3}{2}}}{\sqrt{f + g x} \left(a + b x + c x^{2}\right)}$ |
| timeout | parametric | `sqrt(d + e*x)/(sqrt(f + g*x)*(a + b*x + c*x**2))` | $\frac{\sqrt{d + e x}}{\sqrt{f + g x} \left(a + b x + c x^{2}\right)}$ |
| timeout | parametric | `1/(sqrt(d + e*x)*sqrt(f + g*x)*(a + b*x + c*x**2))` | $\frac{1}{\sqrt{d + e x} \sqrt{f + g x} \left(a + b x + c x^{2}\right)}$ |
| timeout | parametric | `1/((d + e*x)**(3/2)*sqrt(f + g*x)*(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{f + g x} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `(f + g*x)**3*sqrt(a + b*x + c*x**2)/(d + e*x)` | $\frac{\left(f + g x\right)^{3} \sqrt{a + b x + c x^{2}}}{d + e x}$ |
| partial | parametric | `(f + g*x)**2*sqrt(a + b*x + c*x**2)/(d + e*x)` | $\frac{\left(f + g x\right)^{2} \sqrt{a + b x + c x^{2}}}{d + e x}$ |
| partial | parametric | `(f + g*x)*sqrt(a + b*x + c*x**2)/(d + e*x)` | $\frac{\left(f + g x\right) \sqrt{a + b x + c x^{2}}}{d + e x}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x)` | $\frac{\sqrt{a + b x + c x^{2}}}{d + e x}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/((d + e*x)*(f + g*x))` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right) \left(f + g x\right)}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/((d + e*x)*(f + g*x)**2)` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right) \left(f + g x\right)^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/((d + e*x)*(f + g*x)**3)` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right) \left(f + g x\right)^{3}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/((d + e*x)*(f + g*x)**4)` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right) \left(f + g x\right)^{4}}$ |
| partial | parametric | `(f + g*x)**3*(a + b*x + c*x**2)**(3/2)/(d + e*x)` | $\frac{\left(f + g x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(f + g*x)**2*(a + b*x + c*x**2)**(3/2)/(d + e*x)` | $\frac{\left(f + g x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(f + g*x)*(a + b*x + c*x**2)**(3/2)/(d + e*x)` | $\frac{\left(f + g x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{d + e x}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/((d + e*x)*(f + g*x))` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right) \left(f + g x\right)}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/((d + e*x)*(f + g*x)**2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right) \left(f + g x\right)^{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/((d + e*x)*(f + g*x)**3)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x\right) \left(f + g x\right)^{3}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(5/2)/((d + e*x)*(f + g*x))` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}{\left(d + e x\right) \left(f + g x\right)}$ |
| partial | parametric | `(f + g*x)**4/((d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{\left(f + g x\right)^{4}}{\left(d + e x\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(f + g*x)**3/((d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{\left(f + g x\right)^{3}}{\left(d + e x\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(f + g*x)**2/((d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{\left(f + g x\right)^{2}}{\left(d + e x\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(f + g*x)/((d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{f + g x}{\left(d + e x\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)*(f + g*x)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right) \left(f + g x\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)*(f + g*x)**2*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right) \left(f + g x\right)^{2} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d + e*x)*(f + g*x)**3*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right) \left(f + g x\right)^{3} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(f + g*x)**4/((d + e*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{\left(f + g x\right)^{4}}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(f + g*x)**3/((d + e*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{\left(f + g x\right)^{3}}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(f + g*x)**2/((d + e*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{\left(f + g x\right)^{2}}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(f + g*x)/((d + e*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{f + g x}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)*(f + g*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right) \left(f + g x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)*(f + g*x)**2*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right) \left(f + g x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d + e*x)*(f + g*x)**3*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d + e x\right) \left(f + g x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**3*sqrt(f + g*x)*sqrt(a + b*x + c*x**2)` | $\left(d + e x\right)^{3} \sqrt{f + g x} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)**2*sqrt(f + g*x)*sqrt(a + b*x + c*x**2)` | $\left(d + e x\right)^{2} \sqrt{f + g x} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)*sqrt(f + g*x)*sqrt(a + b*x + c*x**2)` | $\left(d + e x\right) \sqrt{f + g x} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `sqrt(f + g*x)*sqrt(a + b*x + c*x**2)` | $\sqrt{f + g x} \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(d + e*x)**3*sqrt(a + b*x + c*x**2)/sqrt(f + g*x)` | $\frac{\left(d + e x\right)^{3} \sqrt{a + b x + c x^{2}}}{\sqrt{f + g x}}$ |
| partial | parametric | `(d + e*x)**2*sqrt(a + b*x + c*x**2)/sqrt(f + g*x)` | $\frac{\left(d + e x\right)^{2} \sqrt{a + b x + c x^{2}}}{\sqrt{f + g x}}$ |
| partial | parametric | `(d + e*x)*sqrt(a + b*x + c*x**2)/sqrt(f + g*x)` | $\frac{\left(d + e x\right) \sqrt{a + b x + c x^{2}}}{\sqrt{f + g x}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/sqrt(f + g*x)` | $\frac{\sqrt{a + b x + c x^{2}}}{\sqrt{f + g x}}$ |
| timeout | parametric | `sqrt(a + b*x + c*x**2)/((d + e*x)*sqrt(f + g*x))` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x\right) \sqrt{f + g x}}$ |
| partial | parametric | `(d + e*x)**3*sqrt(f + g*x)/sqrt(a + b*x + c*x**2)` | $\frac{\left(d + e x\right)^{3} \sqrt{f + g x}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**2*sqrt(f + g*x)/sqrt(a + b*x + c*x**2)` | $\frac{\left(d + e x\right)^{2} \sqrt{f + g x}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)*sqrt(f + g*x)/sqrt(a + b*x + c*x**2)` | $\frac{\left(d + e x\right) \sqrt{f + g x}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `sqrt(f + g*x)/sqrt(a + b*x + c*x**2)` | $\frac{\sqrt{f + g x}}{\sqrt{a + b x + c x^{2}}}$ |
| timeout | parametric | `sqrt(f + g*x)/((d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{\sqrt{f + g x}}{\left(d + e x\right) \sqrt{a + b x + c x^{2}}}$ |
| timeout | parametric | `sqrt(f + g*x)/((d + e*x)**2*sqrt(a + b*x + c*x**2))` | $\frac{\sqrt{f + g x}}{\left(d + e x\right)^{2} \sqrt{a + b x + c x^{2}}}$ |
| timeout | parametric | `sqrt(f + g*x)/((d + e*x)**3*sqrt(a + b*x + c*x**2))` | $\frac{\sqrt{f + g x}}{\left(d + e x\right)^{3} \sqrt{a + b x + c x^{2}}}$ |
| timeout | parametric | `(f + g*x)**(3/2)/((d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{\left(f + g x\right)^{\frac{3}{2}}}{\left(d + e x\right) \sqrt{a + b x + c x^{2}}}$ |
| timeout | parametric | `(f + g*x)**(5/2)/((d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{\left(f + g x\right)^{\frac{5}{2}}}{\left(d + e x\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**3/(sqrt(f + g*x)*sqrt(a + b*x + c*x**2))` | $\frac{\left(d + e x\right)^{3}}{\sqrt{f + g x} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)**2/(sqrt(f + g*x)*sqrt(a + b*x + c*x**2))` | $\frac{\left(d + e x\right)^{2}}{\sqrt{f + g x} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x)/(sqrt(f + g*x)*sqrt(a + b*x + c*x**2))` | $\frac{d + e x}{\sqrt{f + g x} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/(sqrt(f + g*x)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\sqrt{f + g x} \sqrt{a + b x + c x^{2}}}$ |
| timeout | parametric | `1/((d + e*x)*sqrt(f + g*x)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right) \sqrt{f + g x} \sqrt{a + b x + c x^{2}}}$ |
| timeout | parametric | `1/((d + e*x)**2*sqrt(f + g*x)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right)^{2} \sqrt{f + g x} \sqrt{a + b x + c x^{2}}}$ |
| timeout | parametric | `1/((d + e*x)*(f + g*x)**(3/2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right) \left(f + g x\right)^{\frac{3}{2}} \sqrt{a + b x + c x^{2}}}$ |
| timeout | parametric | `1/((d + e*x)*(f + g*x)**(5/2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d + e x\right) \left(f + g x\right)^{\frac{5}{2}} \sqrt{a + b x + c x^{2}}}$ |
| timeout | parametric | `sqrt(d + e*x)/(sqrt(f + g*x)*sqrt(a + b*x + c*x**2))` | $\frac{\sqrt{d + e x}}{\sqrt{f + g x} \sqrt{a + b x + c x^{2}}}$ |
| timeout | parametric | `1/(sqrt(d + e*x)*sqrt(f + g*x)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\sqrt{d + e x} \sqrt{f + g x} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/(x**2*sqrt(1 - 1/(c**2*x**2))*sqrt(d + e*x))` | $\frac{1}{x^{2} \sqrt{1 - \frac{1}{c^{2} x^{2}}} \sqrt{d + e x}}$ |
| partial | parametric | `(a + b*x + b*f*x**2/e)/sqrt(d + e*x + f*x**2)` | $\frac{a + b x + \frac{b f x^{2}}{e}}{\sqrt{d + e x + f x^{2}}}$ |
| partial | parametric | `1/((a + b*x + b*f*x**2/e)*sqrt(d + e*x + f*x**2))` | $\frac{1}{\left(a + b x + \frac{b f x^{2}}{e}\right) \sqrt{d + e x + f x^{2}}}$ |
| partial | parametric | `1/(sqrt(a + b*x + c*x**2)*(b*x + c*x**2 + d))` | $\frac{1}{\sqrt{a + b x + c x^{2}} \left(b x + c x^{2} + d\right)}$ |
| partial | parametric | `1/(sqrt(a + b*x + c*x**2)*(b*x + c*x**2 + d)**2)` | $\frac{1}{\sqrt{a + b x + c x^{2}} \left(b x + c x^{2} + d\right)^{2}}$ |
| partial | parametric | `1/(sqrt(a + b*x + c*x**2)*(b*x + c*x**2 + d)**3)` | $\frac{1}{\sqrt{a + b x + c x^{2}} \left(b x + c x^{2} + d\right)^{3}}$ |
| partial | parametric | `1/(sqrt(a + b*x + c*x**2)*(b*x + c*x**2 + d)**4)` | $\frac{1}{\sqrt{a + b x + c x^{2}} \left(b x + c x^{2} + d\right)^{4}}$ |
| partial | parametric | `1/(sqrt(d + e*x + f*x**2)*(a*e + b*e*x + b*f*x**2)**2)` | $\frac{1}{\sqrt{d + e x + f x^{2}} \left(a e + b e x + b f x^{2}\right)^{2}}$ |
| partial | concrete | `1/((x**2 + 2*x + 4)*sqrt(x**2 + 2*x + 5))` | $\frac{1}{\left(x^{2} + 2 x + 4\right) \sqrt{x^{2} + 2 x + 5}}$ |
| partial | concrete | `sqrt(x**2 + 2*x + 1)/sqrt(x**2 + 1)` | $\frac{\sqrt{x^{2} + 2 x + 1}}{\sqrt{x^{2} + 1}}$ |
| partial | concrete | `1/((x**2 - 1)**2*sqrt(x**2 + x - 1))` | $\frac{1}{\left(x^{2} - 1\right)^{2} \sqrt{x^{2} + x - 1}}$ |
| timeout | parametric | `1/(sqrt(d + f*x**2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\sqrt{d + f x^{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | concrete | `sqrt(-x**2 - 4*x - 3)/(2*x**2 + 4*x + 3)` | $\frac{\sqrt{- x^{2} - 4 x - 3}}{2 x^{2} + 4 x + 3}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**2 + 3*x + 2)**4` | $\sqrt{2 x^{2} - x + 3} \left(5 x^{2} + 3 x + 2\right)^{4}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**2 + 3*x + 2)**3` | $\sqrt{2 x^{2} - x + 3} \left(5 x^{2} + 3 x + 2\right)^{3}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**2 + 3*x + 2)**2` | $\sqrt{2 x^{2} - x + 3} \left(5 x^{2} + 3 x + 2\right)^{2}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**2 + 3*x + 2)` | $\sqrt{2 x^{2} - x + 3} \left(5 x^{2} + 3 x + 2\right)$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)/(5*x**2 + 3*x + 2)` | $\frac{\sqrt{2 x^{2} - x + 3}}{5 x^{2} + 3 x + 2}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)/(5*x**2 + 3*x + 2)**2` | $\frac{\sqrt{2 x^{2} - x + 3}}{\left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)/(5*x**2 + 3*x + 2)**3` | $\frac{\sqrt{2 x^{2} - x + 3}}{\left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**2 + 3*x + 2)**4` | $\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{2} + 3 x + 2\right)^{4}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**2 + 3*x + 2)**3` | $\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{2} + 3 x + 2\right)^{3}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**2 + 3*x + 2)**2` | $\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{2} + 3 x + 2\right)^{2}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**2 + 3*x + 2)` | $\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{2} + 3 x + 2\right)$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)/(5*x**2 + 3*x + 2)` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}{5 x^{2} + 3 x + 2}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)/(5*x**2 + 3*x + 2)**2` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}{\left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)/(5*x**2 + 3*x + 2)**3` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}{\left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | concrete | `(2*x**2 - x + 3)**(5/2)*(5*x**2 + 3*x + 2)**4` | $\left(2 x^{2} - x + 3\right)^{\frac{5}{2}} \left(5 x^{2} + 3 x + 2\right)^{4}$ |
| partial | concrete | `(2*x**2 - x + 3)**(5/2)*(5*x**2 + 3*x + 2)**3` | $\left(2 x^{2} - x + 3\right)^{\frac{5}{2}} \left(5 x^{2} + 3 x + 2\right)^{3}$ |
| partial | concrete | `(2*x**2 - x + 3)**(5/2)*(5*x**2 + 3*x + 2)**2` | $\left(2 x^{2} - x + 3\right)^{\frac{5}{2}} \left(5 x^{2} + 3 x + 2\right)^{2}$ |
| partial | concrete | `(2*x**2 - x + 3)**(5/2)*(5*x**2 + 3*x + 2)` | $\left(2 x^{2} - x + 3\right)^{\frac{5}{2}} \left(5 x^{2} + 3 x + 2\right)$ |
| partial | concrete | `(2*x**2 - x + 3)**(5/2)/(5*x**2 + 3*x + 2)` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}{5 x^{2} + 3 x + 2}$ |
| partial | concrete | `(2*x**2 - x + 3)**(5/2)/(5*x**2 + 3*x + 2)**2` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}{\left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `(2*x**2 - x + 3)**(5/2)/(5*x**2 + 3*x + 2)**3` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}{\left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x**2 + 3*x + 2)**4/sqrt(2*x**2 - x + 3)` | $\frac{\left(5 x^{2} + 3 x + 2\right)^{4}}{\sqrt{2 x^{2} - x + 3}}$ |
| partial | concrete | `(5*x**2 + 3*x + 2)**3/sqrt(2*x**2 - x + 3)` | $\frac{\left(5 x^{2} + 3 x + 2\right)^{3}}{\sqrt{2 x^{2} - x + 3}}$ |
| partial | concrete | `(5*x**2 + 3*x + 2)**2/sqrt(2*x**2 - x + 3)` | $\frac{\left(5 x^{2} + 3 x + 2\right)^{2}}{\sqrt{2 x^{2} - x + 3}}$ |
| partial | concrete | `(5*x**2 + 3*x + 2)/sqrt(2*x**2 - x + 3)` | $\frac{5 x^{2} + 3 x + 2}{\sqrt{2 x^{2} - x + 3}}$ |
| partial | concrete | `1/(sqrt(2*x**2 - x + 3)*(5*x**2 + 3*x + 2))` | $\frac{1}{\sqrt{2 x^{2} - x + 3} \left(5 x^{2} + 3 x + 2\right)}$ |
| partial | concrete | `1/(sqrt(2*x**2 - x + 3)*(5*x**2 + 3*x + 2)**2)` | $\frac{1}{\sqrt{2 x^{2} - x + 3} \left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `1/(sqrt(2*x**2 - x + 3)*(5*x**2 + 3*x + 2)**3)` | $\frac{1}{\sqrt{2 x^{2} - x + 3} \left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x**2 + 3*x + 2)**4/(2*x**2 - x + 3)**(3/2)` | $\frac{\left(5 x^{2} + 3 x + 2\right)^{4}}{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 3*x + 2)**3/(2*x**2 - x + 3)**(3/2)` | $\frac{\left(5 x^{2} + 3 x + 2\right)^{3}}{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 3*x + 2)**2/(2*x**2 - x + 3)**(3/2)` | $\frac{\left(5 x^{2} + 3 x + 2\right)^{2}}{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 3*x + 2)/(2*x**2 - x + 3)**(3/2)` | $\frac{5 x^{2} + 3 x + 2}{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((2*x**2 - x + 3)**(3/2)*(5*x**2 + 3*x + 2))` | $\frac{1}{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{2} + 3 x + 2\right)}$ |
| partial | concrete | `1/((2*x**2 - x + 3)**(3/2)*(5*x**2 + 3*x + 2)**2)` | $\frac{1}{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `1/((2*x**2 - x + 3)**(3/2)*(5*x**2 + 3*x + 2)**3)` | $\frac{1}{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | concrete | `(5*x**2 + 3*x + 2)**4/(2*x**2 - x + 3)**(5/2)` | $\frac{\left(5 x^{2} + 3 x + 2\right)^{4}}{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x**2 + 3*x + 2)**3/(2*x**2 - x + 3)**(5/2)` | $\frac{\left(5 x^{2} + 3 x + 2\right)^{3}}{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x**2 + 3*x + 2)**2/(2*x**2 - x + 3)**(5/2)` | $\frac{\left(5 x^{2} + 3 x + 2\right)^{2}}{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(5*x**2 + 3*x + 2)/(2*x**2 - x + 3)**(5/2)` | $\frac{5 x^{2} + 3 x + 2}{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/((2*x**2 - x + 3)**(5/2)*(5*x**2 + 3*x + 2))` | $\frac{1}{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}} \left(5 x^{2} + 3 x + 2\right)}$ |
| partial | concrete | `1/((2*x**2 - x + 3)**(5/2)*(5*x**2 + 3*x + 2)**2)` | $\frac{1}{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}} \left(5 x^{2} + 3 x + 2\right)^{2}}$ |
| partial | concrete | `1/((2*x**2 - x + 3)**(5/2)*(5*x**2 + 3*x + 2)**3)` | $\frac{1}{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}} \left(5 x^{2} + 3 x + 2\right)^{3}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)**2` | $\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)^{2}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)` | $\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x + f*x**2)` | $\frac{\sqrt{a + b x + c x^{2}}}{d + e x + f x^{2}}$ |
| timeout | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x + f*x**2)**2` | $\frac{\sqrt{a + b x + c x^{2}}}{\left(d + e x + f x^{2}\right)^{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)**2` | $\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)^{2}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)` | $\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x + f*x**2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{d + e x + f x^{2}}$ |
| timeout | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x + f*x**2)**2` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x + f x^{2}\right)^{2}}$ |
| timeout | parametric | `(a + b*x + c*x**2)**(3/2)/(d + e*x + f*x**2)**3` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{\left(d + e x + f x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x + f*x**2)**3/sqrt(a + b*x + c*x**2)` | $\frac{\left(d + e x + f x^{2}\right)^{3}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)**2/sqrt(a + b*x + c*x**2)` | $\frac{\left(d + e x + f x^{2}\right)^{2}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/sqrt(a + b*x + c*x**2)` | $\frac{d + e x + f x^{2}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/(sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2))` | $\frac{1}{\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| timeout | parametric | `1/(sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)**2)` | $\frac{1}{\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)^{2}}$ |
| partial | parametric | `(d + e*x + f*x**2)**3/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x + f x^{2}\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)**2/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(d + e x + f x^{2}\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/(a + b*x + c*x**2)**(3/2)` | $\frac{d + e x + f x^{2}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2))` | $\frac{1}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `(d + e*x + f*x**2)**3/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x + f x^{2}\right)^{3}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)**2/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(d + e x + f x^{2}\right)^{2}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(d + e*x + f*x**2)/(a + b*x + c*x**2)**(5/2)` | $\frac{d + e x + f x^{2}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(sqrt(5*x**2 + 2*x - 7)*(5*x**2 + 12*x + 8))` | $\frac{1}{\sqrt{5 x^{2} + 2 x - 7} \left(5 x^{2} + 12 x + 8\right)}$ |
| timeout | parametric | `1/(sqrt(a + b*x + c*x**2)*sqrt(d + e*x + f*x**2))` | $\frac{1}{\sqrt{a + b x + c x^{2}} \sqrt{d + e x + f x^{2}}}$ |
| partial | concrete | `1/(sqrt(2*x**2 - x + 3)*sqrt(5*x**2 + 3*x + 2))` | $\frac{1}{\sqrt{2 x^{2} - x + 3} \sqrt{5 x^{2} + 3 x + 2}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/(d - f*x**2)` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{d - f x^{2}}$ |
| partial | parametric | `(A + B*x)/((d - f*x**2)*sqrt(a + b*x + c*x**2))` | $\frac{A + B x}{\left(d - f x^{2}\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)/((d - f*x**2)*(a + b*x + c*x**2)**(3/2))` | $\frac{A + B x}{\left(d - f x^{2}\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x)/((d - f*x**2)*(a + b*x + c*x**2)**(5/2))` | $\frac{A + B x}{\left(d - f x^{2}\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(2*x + 1)/((x**2 - 1)*sqrt(x**2 + x - 1))` | $\frac{2 x + 1}{\left(x^{2} - 1\right) \sqrt{x^{2} + x - 1}}$ |
| partial | concrete | `(2*x + 1)/((x**2 + 1)*sqrt(x**2 + x - 1))` | $\frac{2 x + 1}{\left(x^{2} + 1\right) \sqrt{x^{2} + x - 1}}$ |
| partial | parametric | `(a + b*x - c)/((x**2 + 1)*sqrt(a + b*x + c*x**2))` | $\frac{a + b x - c}{\left(x^{2} + 1\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x)*sqrt(a + b*x + c*x**2)/(d + e*x + f*x**2)` | $\frac{\left(A + B x\right) \sqrt{a + b x + c x^{2}}}{d + e x + f x^{2}}$ |
| partial | parametric | `(A + B*x)*(a + b*x + c*x**2)**(3/2)/(d + e*x + f*x**2)` | $\frac{\left(A + B x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{d + e x + f x^{2}}$ |
| partial | parametric | `(A + B*x)/((a + b*x + c*x**2)*sqrt(d + e*x + f*x**2))` | $\frac{A + B x}{\left(a + b x + c x^{2}\right) \sqrt{d + e x + f x^{2}}}$ |
| partial | parametric | `(A + B*x)/((a + c*x**2)*sqrt(d + e*x + f*x**2))` | $\frac{A + B x}{\left(a + c x^{2}\right) \sqrt{d + e x + f x^{2}}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + f*x**2)*(a + b*x + c*x**2))` | $\frac{A + B x}{\sqrt{d + f x^{2}} \left(a + b x + c x^{2}\right)}$ |
| partial | parametric | `(A + B*x)/((a + c*x**2)*sqrt(d + f*x**2))` | $\frac{A + B x}{\left(a + c x^{2}\right) \sqrt{d + f x^{2}}}$ |
| partial | concrete | `(x + 2)/((-3*x**2 + 4*x + 2)*sqrt(-2*x**2 + 3*x + 1))` | $\frac{x + 2}{\left(- 3 x^{2} + 4 x + 2\right) \sqrt{- 2 x^{2} + 3 x + 1}}$ |
| partial | concrete | `(x + 2)/((-3*x**2 + 4*x + 2)*(-2*x**2 + 3*x + 1)**(3/2))` | $\frac{x + 2}{\left(- 3 x^{2} + 4 x + 2\right) \left(- 2 x^{2} + 3 x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x + 2)/((-3*x**2 + 4*x + 2)*(-2*x**2 + 3*x + 1)**(5/2))` | $\frac{x + 2}{\left(- 3 x^{2} + 4 x + 2\right) \left(- 2 x^{2} + 3 x + 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(x + 2)/((-3*x**2 + 4*x + 2)*sqrt(2*x**2 + 3*x + 1))` | $\frac{x + 2}{\left(- 3 x^{2} + 4 x + 2\right) \sqrt{2 x^{2} + 3 x + 1}}$ |
| partial | concrete | `(x + 2)/((-3*x**2 + 4*x + 2)*(2*x**2 + 3*x + 1)**(3/2))` | $\frac{x + 2}{\left(- 3 x^{2} + 4 x + 2\right) \left(2 x^{2} + 3 x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x + 2)/((-3*x**2 + 4*x + 2)*(2*x**2 + 3*x + 1)**(5/2))` | $\frac{x + 2}{\left(- 3 x^{2} + 4 x + 2\right) \left(2 x^{2} + 3 x + 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(x + 1)/((x**2 + 2*x + 4)*sqrt(x**2 + 2*x + 5))` | $\frac{x + 1}{\left(x^{2} + 2 x + 4\right) \sqrt{x^{2} + 2 x + 5}}$ |
| partial | concrete | `(x + 4)/((x**2 + 2*x + 4)*sqrt(x**2 + 2*x + 5))` | $\frac{x + 4}{\left(x^{2} + 2 x + 4\right) \sqrt{x^{2} + 2 x + 5}}$ |
| partial | concrete | `(2*x + 1)/((x**2 + x + 3)*sqrt(x**2 + x + 5))` | $\frac{2 x + 1}{\left(x^{2} + x + 3\right) \sqrt{x^{2} + x + 5}}$ |
| partial | concrete | `x/((x**2 + x + 3)*sqrt(x**2 + x + 5))` | $\frac{x}{\left(x^{2} + x + 3\right) \sqrt{x^{2} + x + 5}}$ |
| partial | parametric | `(A + B*x)/(sqrt(d + e*x + f*x**2)*(a*e + b*e*x + b*f*x**2)**2)` | $\frac{A + B x}{\sqrt{d + e x + f x^{2}} \left(a e + b e x + b f x^{2}\right)^{2}}$ |
| **SOLVED-NEW** | parametric | `(g + h*x)*sqrt(a + b*x + c*x**2)/(a*d + b*d*x + c*d*x**2)**2` | $\frac{\left(g + h x\right) \sqrt{a + b x + c x^{2}}}{\left(a d + b d x + c d x^{2}\right)^{2}}$ |
| partial | concrete | `(2*x + 3)/(sqrt(-x**2 - 4*x - 3)*(2*x**2 + 4*x + 3))` | $\frac{2 x + 3}{\sqrt{- x^{2} - 4 x - 3} \left(2 x^{2} + 4 x + 3\right)}$ |
| partial | concrete | `(4*x + 3)/(sqrt(-x**2 - 4*x - 3)*(2*x**2 + 4*x + 3))` | $\frac{4 x + 3}{\sqrt{- x^{2} - 4 x - 3} \left(2 x^{2} + 4 x + 3\right)}$ |
| partial | parametric | `(g + h*x)*sqrt(a + b*x + c*x**2)/(a*d + b*d*x + c*d*x**2)**(3/2)` | $\frac{\left(g + h x\right) \sqrt{a + b x + c x^{2}}}{\left(a d + b d x + c d x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x^{2} \sqrt{c + d x^{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `x*sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $x \sqrt{c + d x^{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | $\sqrt{c + d x^{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}$ |
| partial | parametric | `sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x` | $\frac{\sqrt{c + d x^{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x}$ |
| partial | parametric | `sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**2` | $\frac{\sqrt{c + d x^{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{2}}$ |
| partial | parametric | `sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**3` | $\frac{\sqrt{c + d x^{2}} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}}}{x^{3}}$ |
| partial | parametric | `x**2*sqrt(a**2 + 2*a*b*x + b**2*x**2)*sqrt(c + d*x**2 + e*x)` | $x^{2} \sqrt{a^{2} + 2 a b x + b^{2} x^{2}} \sqrt{c + d x^{2} + e x}$ |
| partial | parametric | `x*sqrt(a**2 + 2*a*b*x + b**2*x**2)*sqrt(c + d*x**2 + e*x)` | $x \sqrt{a^{2} + 2 a b x + b^{2} x^{2}} \sqrt{c + d x^{2} + e x}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)*sqrt(c + d*x**2 + e*x)` | $\sqrt{a^{2} + 2 a b x + b^{2} x^{2}} \sqrt{c + d x^{2} + e x}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)*sqrt(c + d*x**2 + e*x)/x` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}} \sqrt{c + d x^{2} + e x}}{x}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)*sqrt(c + d*x**2 + e*x)/x**2` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}} \sqrt{c + d x^{2} + e x}}{x^{2}}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b*x + b**2*x**2)*sqrt(c + d*x**2 + e*x)/x**3` | $\frac{\sqrt{a^{2} + 2 a b x + b^{2} x^{2}} \sqrt{c + d x^{2} + e x}}{x^{3}}$ |
| partial | parametric | `x**2*sqrt(a + c*x**2)/(d + e*x + f*x**2)` | $\frac{x^{2} \sqrt{a + c x^{2}}}{d + e x + f x^{2}}$ |
| partial | parametric | `x*sqrt(a + c*x**2)/(d + e*x + f*x**2)` | $\frac{x \sqrt{a + c x^{2}}}{d + e x + f x^{2}}$ |
| partial | parametric | `sqrt(a + c*x**2)/(d + e*x + f*x**2)` | $\frac{\sqrt{a + c x^{2}}}{d + e x + f x^{2}}$ |
| partial | parametric | `sqrt(a + c*x**2)/(x*(d + e*x + f*x**2))` | $\frac{\sqrt{a + c x^{2}}}{x \left(d + e x + f x^{2}\right)}$ |
| timeout | parametric | `sqrt(a + c*x**2)/(x**2*(d + e*x + f*x**2))` | $\frac{\sqrt{a + c x^{2}}}{x^{2} \left(d + e x + f x^{2}\right)}$ |
| timeout | parametric | `sqrt(a + c*x**2)/(x**3*(d + e*x + f*x**2))` | $\frac{\sqrt{a + c x^{2}}}{x^{3} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x**2*(a + c*x**2)**(3/2)/(d + e*x + f*x**2)` | $\frac{x^{2} \left(a + c x^{2}\right)^{\frac{3}{2}}}{d + e x + f x^{2}}$ |
| partial | parametric | `x*(a + c*x**2)**(3/2)/(d + e*x + f*x**2)` | $\frac{x \left(a + c x^{2}\right)^{\frac{3}{2}}}{d + e x + f x^{2}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(d + e*x + f*x**2)` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{d + e x + f x^{2}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)/(x*(d + e*x + f*x**2))` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{x \left(d + e x + f x^{2}\right)}$ |
| timeout | parametric | `(a + c*x**2)**(3/2)/(x**2*(d + e*x + f*x**2))` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{x^{2} \left(d + e x + f x^{2}\right)}$ |
| timeout | parametric | `(a + c*x**2)**(3/2)/(x**3*(d + e*x + f*x**2))` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}}}{x^{3} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x**3/(sqrt(a + c*x**2)*(d + e*x + f*x**2))` | $\frac{x^{3}}{\sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x**2/(sqrt(a + c*x**2)*(d + e*x + f*x**2))` | $\frac{x^{2}}{\sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x/(sqrt(a + c*x**2)*(d + e*x + f*x**2))` | $\frac{x}{\sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `1/(sqrt(a + c*x**2)*(d + e*x + f*x**2))` | $\frac{1}{\sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `1/(x*sqrt(a + c*x**2)*(d + e*x + f*x**2))` | $\frac{1}{x \sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| timeout | parametric | `1/(x**2*sqrt(a + c*x**2)*(d + e*x + f*x**2))` | $\frac{1}{x^{2} \sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| timeout | parametric | `1/(x**3*sqrt(a + c*x**2)*(d + e*x + f*x**2))` | $\frac{1}{x^{3} \sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x**3/((a + c*x**2)**(3/2)*(d + e*x + f*x**2))` | $\frac{x^{3}}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x**2/((a + c*x**2)**(3/2)*(d + e*x + f*x**2))` | $\frac{x^{2}}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x/((a + c*x**2)**(3/2)*(d + e*x + f*x**2))` | $\frac{x}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `1/((a + c*x**2)**(3/2)*(d + e*x + f*x**2))` | $\frac{1}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `1/(x*(a + c*x**2)**(3/2)*(d + e*x + f*x**2))` | $\frac{1}{x \left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}$ |
| timeout | parametric | `1/(x**2*(a + c*x**2)**(3/2)*(d + e*x + f*x**2))` | $\frac{1}{x^{2} \left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x**3*sqrt(a + b*x + c*x**2)/(d - f*x**2)` | $\frac{x^{3} \sqrt{a + b x + c x^{2}}}{d - f x^{2}}$ |
| partial | parametric | `x**2*sqrt(a + b*x + c*x**2)/(d - f*x**2)` | $\frac{x^{2} \sqrt{a + b x + c x^{2}}}{d - f x^{2}}$ |
| partial | parametric | `x*sqrt(a + b*x + c*x**2)/(d - f*x**2)` | $\frac{x \sqrt{a + b x + c x^{2}}}{d - f x^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d - f*x**2)` | $\frac{\sqrt{a + b x + c x^{2}}}{d - f x^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(x*(d - f*x**2))` | $\frac{\sqrt{a + b x + c x^{2}}}{x \left(d - f x^{2}\right)}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(x**2*(d - f*x**2))` | $\frac{\sqrt{a + b x + c x^{2}}}{x^{2} \left(d - f x^{2}\right)}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(x**3*(d - f*x**2))` | $\frac{\sqrt{a + b x + c x^{2}}}{x^{3} \left(d - f x^{2}\right)}$ |
| partial | parametric | `x**3*(a + b*x + c*x**2)**(3/2)/(d - f*x**2)` | $\frac{x^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{d - f x^{2}}$ |
| partial | parametric | `x**2*(a + b*x + c*x**2)**(3/2)/(d - f*x**2)` | $\frac{x^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{d - f x^{2}}$ |
| partial | parametric | `x*(a + b*x + c*x**2)**(3/2)/(d - f*x**2)` | $\frac{x \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{d - f x^{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(d - f*x**2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{d - f x^{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(x*(d - f*x**2))` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{x \left(d - f x^{2}\right)}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(x**2*(d - f*x**2))` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{x^{2} \left(d - f x^{2}\right)}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(x**3*(d - f*x**2))` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{x^{3} \left(d - f x^{2}\right)}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)/(1 - x**2)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}{1 - x^{2}}$ |
| partial | concrete | `sqrt(x**2 - x - 1)/(1 - x**2)` | $\frac{\sqrt{x^{2} - x - 1}}{1 - x^{2}}$ |
| partial | concrete | `(x**2 + x)**(3/2)/(x**2 + 1)` | $\frac{\left(x^{2} + x\right)^{\frac{3}{2}}}{x^{2} + 1}$ |
| partial | parametric | `x**4/((d - f*x**2)*sqrt(a + b*x + c*x**2))` | $\frac{x^{4}}{\left(d - f x^{2}\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `x**3/((d - f*x**2)*sqrt(a + b*x + c*x**2))` | $\frac{x^{3}}{\left(d - f x^{2}\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `x**2/((d - f*x**2)*sqrt(a + b*x + c*x**2))` | $\frac{x^{2}}{\left(d - f x^{2}\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `x/((d - f*x**2)*sqrt(a + b*x + c*x**2))` | $\frac{x}{\left(d - f x^{2}\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/((d - f*x**2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{\left(d - f x^{2}\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/(x*(d - f*x**2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{x \left(d - f x^{2}\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/(x**2*(d - f*x**2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{x^{2} \left(d - f x^{2}\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/(x**3*(d - f*x**2)*sqrt(a + b*x + c*x**2))` | $\frac{1}{x^{3} \left(d - f x^{2}\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `x**4/((d - f*x**2)*(a + b*x + c*x**2)**(3/2))` | $\frac{x^{4}}{\left(d - f x^{2}\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/((d - f*x**2)*(a + b*x + c*x**2)**(3/2))` | $\frac{x^{3}}{\left(d - f x^{2}\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/((d - f*x**2)*(a + b*x + c*x**2)**(3/2))` | $\frac{x^{2}}{\left(d - f x^{2}\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/((d - f*x**2)*(a + b*x + c*x**2)**(3/2))` | $\frac{x}{\left(d - f x^{2}\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d - f*x**2)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{\left(d - f x^{2}\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(d - f*x**2)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{x \left(d - f x^{2}\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(d - f*x**2)*(a + b*x + c*x**2)**(3/2))` | $\frac{1}{x^{2} \left(d - f x^{2}\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*sqrt(a + b*x + c*x**2)/(d + e*x + f*x**2)` | $\frac{x^{2} \sqrt{a + b x + c x^{2}}}{d + e x + f x^{2}}$ |
| partial | parametric | `x*sqrt(a + b*x + c*x**2)/(d + e*x + f*x**2)` | $\frac{x \sqrt{a + b x + c x^{2}}}{d + e x + f x^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(d + e*x + f*x**2)` | $\frac{\sqrt{a + b x + c x^{2}}}{d + e x + f x^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)/(x*(d + e*x + f*x**2))` | $\frac{\sqrt{a + b x + c x^{2}}}{x \left(d + e x + f x^{2}\right)}$ |
| timeout | parametric | `sqrt(a + b*x + c*x**2)/(x**2*(d + e*x + f*x**2))` | $\frac{\sqrt{a + b x + c x^{2}}}{x^{2} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x**3/(sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2))` | $\frac{x^{3}}{\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x**2/(sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2))` | $\frac{x^{2}}{\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x/(sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2))` | $\frac{x}{\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `1/(sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2))` | $\frac{1}{\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `1/(x*sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2))` | $\frac{1}{x \sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| timeout | parametric | `1/(x**2*sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2))` | $\frac{1}{x^{2} \sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| timeout | parametric | `1/(x**3*sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2))` | $\frac{1}{x^{3} \sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x**3/((a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2))` | $\frac{x^{3}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x**2/((a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2))` | $\frac{x^{2}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `x/((a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2))` | $\frac{x}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `1/((a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2))` | $\frac{1}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | parametric | `1/(x*(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2))` | $\frac{1}{x \left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}$ |
| partial | concrete | `x**4/(sqrt(-x**2 - 4*x - 3)*(2*x**2 + 4*x + 3))` | $\frac{x^{4}}{\sqrt{- x^{2} - 4 x - 3} \left(2 x^{2} + 4 x + 3\right)}$ |
| partial | concrete | `x**3/(sqrt(-x**2 - 4*x - 3)*(2*x**2 + 4*x + 3))` | $\frac{x^{3}}{\sqrt{- x^{2} - 4 x - 3} \left(2 x^{2} + 4 x + 3\right)}$ |
| partial | concrete | `x**2/(sqrt(-x**2 - 4*x - 3)*(2*x**2 + 4*x + 3))` | $\frac{x^{2}}{\sqrt{- x^{2} - 4 x - 3} \left(2 x^{2} + 4 x + 3\right)}$ |
| partial | concrete | `1/(sqrt(-x**2 - 4*x - 3)*(2*x**2 + 4*x + 3))` | $\frac{1}{\sqrt{- x^{2} - 4 x - 3} \left(2 x^{2} + 4 x + 3\right)}$ |
| partial | concrete | `1/(x*sqrt(-x**2 - 4*x - 3)*(2*x**2 + 4*x + 3))` | $\frac{1}{x \sqrt{- x^{2} - 4 x - 3} \left(2 x^{2} + 4 x + 3\right)}$ |
| partial | concrete | `1/(x**2*sqrt(-x**2 - 4*x - 3)*(2*x**2 + 4*x + 3))` | $\frac{1}{x^{2} \sqrt{- x^{2} - 4 x - 3} \left(2 x^{2} + 4 x + 3\right)}$ |
| partial | concrete | `(3*x + 2)**2*(-12*x**2 + 31*x + 30)**2*sqrt(12*x**2 + 17*x + 6)` | $\left(3 x + 2\right)^{2} \left(- 12 x^{2} + 31 x + 30\right)^{2} \sqrt{12 x^{2} + 17 x + 6}$ |
| partial | concrete | `(3*x + 2)*(-12*x**2 + 31*x + 30)*sqrt(12*x**2 + 17*x + 6)` | $\left(3 x + 2\right) \left(- 12 x^{2} + 31 x + 30\right) \sqrt{12 x^{2} + 17 x + 6}$ |
| partial | concrete | `sqrt(12*x**2 + 17*x + 6)/((3*x + 2)*(-12*x**2 + 31*x + 30))` | $\frac{\sqrt{12 x^{2} + 17 x + 6}}{\left(3 x + 2\right) \left(- 12 x^{2} + 31 x + 30\right)}$ |
| partial | concrete | `sqrt(12*x**2 + 17*x + 6)/((3*x + 2)**2*(-12*x**2 + 31*x + 30)**2)` | $\frac{\sqrt{12 x^{2} + 17 x + 6}}{\left(3 x + 2\right)^{2} \left(- 12 x^{2} + 31 x + 30\right)^{2}}$ |
| partial | concrete | `sqrt(12*x**2 + 17*x + 6)/((3*x + 2)**3*(-12*x**2 + 31*x + 30)**3)` | $\frac{\sqrt{12 x^{2} + 17 x + 6}}{\left(3 x + 2\right)^{3} \left(- 12 x^{2} + 31 x + 30\right)^{3}}$ |
| SOLVED-both | concrete | `(2*x - 3)*(x**2 - 3*x)**(2/3)` | $\left(2 x - 3\right) \left(x^{2} - 3 x\right)^{\frac{2}{3}}$ |
| SOLVED-both | concrete | `(x*(x - 3))**(2/3)*(2*x - 3)` | $\left(x \left(x - 3\right)\right)^{\frac{2}{3}} \left(2 x - 3\right)$ |
| **SOLVED-NEW** | concrete | `x*(2*x**2 - 9*x + 9)/(x**2 - 3*x)**(1/3)` | $\frac{x \left(2 x^{2} - 9 x + 9\right)}{\sqrt[3]{x^{2} - 3 x}}$ |
| **SOLVED-NEW** | concrete | `x*(2*x**2 - 9*x + 9)/(x*(x - 3))**(1/3)` | $\frac{x \left(2 x^{2} - 9 x + 9\right)}{\sqrt[3]{x \left(x - 3\right)}}$ |
| partial | parametric | `(g + h*x)/((g**2 + 3*h**2*x**2)*(-c*g**2/h**2 + 9*c*x**2)**(1/3))` | $\frac{g + h x}{\left(g^{2} + 3 h^{2} x^{2}\right) \sqrt[3]{- \frac{c g^{2}}{h^{2}} + 9 c x^{2}}}$ |
| partial | parametric | `(g + h*x)/((b*x + c*x**2 + (2*b**2*h**2 + b*c*g*h - c**2*g**2)/(9*c*h**2))**(1/3)*(b*f*x/c + f*x**2 + f*(b**2 - (2*b**2*h**2 + b*c*g*h - c**2*g**2)/(3*h**2))/c**2))` | $\frac{g + h x}{\sqrt[3]{b x + c x^{2} + \frac{2 b^{2} h^{2} + b c g h - c^{2} g^{2}}{9 c h^{2}}} \left(\frac{b f x}{c} + f x^{2} + \frac{f \left(b^{2} - \frac{2 b^{2} h^{2} + b c g h - c^{2} g^{2}}{3 h^{2}}\right)}{c^{2}}\right)}$ |
| partial | parametric | `(d + e*x)**2*sqrt(d**2 - e**2*x**2)*(A + B*x + C*x**2)` | $\left(d + e x\right)^{2} \sqrt{d^{2} - e^{2} x^{2}} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `(d + e*x)*sqrt(d**2 - e**2*x**2)*(A + B*x + C*x**2)` | $\left(d + e x\right) \sqrt{d^{2} - e^{2} x^{2}} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)*(A + B*x + C*x**2)` | $\sqrt{d^{2} - e^{2} x^{2}} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)*(A + B*x + C*x**2)/(d + e*x)` | $\frac{\sqrt{d^{2} - e^{2} x^{2}} \left(A + B x + C x^{2}\right)}{d + e x}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)*(A + B*x + C*x**2)/(d + e*x)**2` | $\frac{\sqrt{d^{2} - e^{2} x^{2}} \left(A + B x + C x^{2}\right)}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)*(A + B*x + C*x**2)/(d + e*x)**3` | $\frac{\sqrt{d^{2} - e^{2} x^{2}} \left(A + B x + C x^{2}\right)}{\left(d + e x\right)^{3}}$ |
| partial | parametric | `sqrt(d**2 - e**2*x**2)*(A + B*x + C*x**2)/(d + e*x)**4` | $\frac{\sqrt{d^{2} - e^{2} x^{2}} \left(A + B x + C x^{2}\right)}{\left(d + e x\right)^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d**2 - e**2*x**2)*(A + B*x + C*x**2)/(d + e*x)**5` | $\frac{\sqrt{d^{2} - e^{2} x^{2}} \left(A + B x + C x^{2}\right)}{\left(d + e x\right)^{5}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d**2 - e**2*x**2)*(A + B*x + C*x**2)/(d + e*x)**6` | $\frac{\sqrt{d^{2} - e^{2} x^{2}} \left(A + B x + C x^{2}\right)}{\left(d + e x\right)^{6}}$ |
| partial | parametric | `(d + e*x)**3*(A + B*x + C*x**2)/sqrt(d**2 - e**2*x**2)` | $\frac{\left(d + e x\right)^{3} \left(A + B x + C x^{2}\right)}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)**2*(A + B*x + C*x**2)/sqrt(d**2 - e**2*x**2)` | $\frac{\left(d + e x\right)^{2} \left(A + B x + C x^{2}\right)}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(d + e*x)*(A + B*x + C*x**2)/sqrt(d**2 - e**2*x**2)` | $\frac{\left(d + e x\right) \left(A + B x + C x^{2}\right)}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)/sqrt(d**2 - e**2*x**2)` | $\frac{A + B x + C x^{2}}{\sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)/((d + e*x)*sqrt(d**2 - e**2*x**2))` | $\frac{A + B x + C x^{2}}{\left(d + e x\right) \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)/((d + e*x)**2*sqrt(d**2 - e**2*x**2))` | $\frac{A + B x + C x^{2}}{\left(d + e x\right)^{2} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x + C*x**2)/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | $\frac{A + B x + C x^{2}}{\left(d + e x\right)^{3} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| **SOLVED-NEW** | parametric | `(A + B*x + C*x**2)/((d + e*x)**4*sqrt(d**2 - e**2*x**2))` | $\frac{A + B x + C x^{2}}{\left(d + e x\right)^{4} \sqrt{d^{2} - e^{2} x^{2}}}$ |
| partial | parametric | `sqrt(a + c*x**2)*(g + h*x)**3*(d + e*x + f*x**2)` | $\sqrt{a + c x^{2}} \left(g + h x\right)^{3} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `sqrt(a + c*x**2)*(g + h*x)**2*(d + e*x + f*x**2)` | $\sqrt{a + c x^{2}} \left(g + h x\right)^{2} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `sqrt(a + c*x**2)*(g + h*x)*(d + e*x + f*x**2)` | $\sqrt{a + c x^{2}} \left(g + h x\right) \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x + f*x**2)` | $\sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x + f*x**2)/(g + h*x)` | $\frac{\sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}{g + h x}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x + f*x**2)/(g + h*x)**2` | $\frac{\sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{2}}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x + f*x**2)/(g + h*x)**3` | $\frac{\sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{3}}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x + f*x**2)/(g + h*x)**4` | $\frac{\sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{4}}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x + f*x**2)/(g + h*x)**5` | $\frac{\sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{5}}$ |
| partial | parametric | `sqrt(a + c*x**2)*(d + e*x + f*x**2)/(g + h*x)**6` | $\frac{\sqrt{a + c x^{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{6}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(g + h*x)**3*(d + e*x + f*x**2)` | $\left(a + c x^{2}\right)^{\frac{3}{2}} \left(g + h x\right)^{3} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(g + h*x)**2*(d + e*x + f*x**2)` | $\left(a + c x^{2}\right)^{\frac{3}{2}} \left(g + h x\right)^{2} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(g + h*x)*(d + e*x + f*x**2)` | $\left(a + c x^{2}\right)^{\frac{3}{2}} \left(g + h x\right) \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x + f*x**2)` | $\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{g + h x}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**2` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{2}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**3` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{3}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**4` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{4}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**5` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{5}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**6` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{6}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**7` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{7}}$ |
| partial | parametric | `(a + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**8` | $\frac{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{8}}$ |
| partial | parametric | `(a + c*x**2)**(5/2)*(A + B*x + C*x**2)` | $\left(a + c x^{2}\right)^{\frac{5}{2}} \left(A + B x + C x^{2}\right)$ |
| partial | parametric | `(g + h*x)**3*(d + e*x + f*x**2)/sqrt(a + c*x**2)` | $\frac{\left(g + h x\right)^{3} \left(d + e x + f x^{2}\right)}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(g + h*x)**2*(d + e*x + f*x**2)/sqrt(a + c*x**2)` | $\frac{\left(g + h x\right)^{2} \left(d + e x + f x^{2}\right)}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(g + h*x)*(d + e*x + f*x**2)/sqrt(a + c*x**2)` | $\frac{\left(g + h x\right) \left(d + e x + f x^{2}\right)}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/sqrt(a + c*x**2)` | $\frac{d + e x + f x^{2}}{\sqrt{a + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/(sqrt(a + c*x**2)*(g + h*x))` | $\frac{d + e x + f x^{2}}{\sqrt{a + c x^{2}} \left(g + h x\right)}$ |
| partial | parametric | `(d + e*x + f*x**2)/(sqrt(a + c*x**2)*(g + h*x)**2)` | $\frac{d + e x + f x^{2}}{\sqrt{a + c x^{2}} \left(g + h x\right)^{2}}$ |
| partial | parametric | `(d + e*x + f*x**2)/(sqrt(a + c*x**2)*(g + h*x)**3)` | $\frac{d + e x + f x^{2}}{\sqrt{a + c x^{2}} \left(g + h x\right)^{3}}$ |
| partial | parametric | `(g + h*x)**3*(d + e*x + f*x**2)/(a + c*x**2)**(3/2)` | $\frac{\left(g + h x\right)^{3} \left(d + e x + f x^{2}\right)}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(g + h*x)**2*(d + e*x + f*x**2)/(a + c*x**2)**(3/2)` | $\frac{\left(g + h x\right)^{2} \left(d + e x + f x^{2}\right)}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(g + h*x)*(d + e*x + f*x**2)/(a + c*x**2)**(3/2)` | $\frac{\left(g + h x\right) \left(d + e x + f x^{2}\right)}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/(a + c*x**2)**(3/2)` | $\frac{d + e x + f x^{2}}{\left(a + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/((a + c*x**2)**(3/2)*(g + h*x))` | $\frac{d + e x + f x^{2}}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(g + h x\right)}$ |
| partial | parametric | `(d + e*x + f*x**2)/((a + c*x**2)**(3/2)*(g + h*x)**2)` | $\frac{d + e x + f x^{2}}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(g + h x\right)^{2}}$ |
| partial | parametric | `(d + e*x + f*x**2)/((a + c*x**2)**(3/2)*(g + h*x)**3)` | $\frac{d + e x + f x^{2}}{\left(a + c x^{2}\right)^{\frac{3}{2}} \left(g + h x\right)^{3}}$ |
| SOLVED-both | parametric | `(A + B*x + C*x**2)/(a + c*x**2)**(5/2)` | $\frac{A + B x + C x^{2}}{\left(a + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x + C*x**2)/(a + c*x**2)**(7/2)` | $\frac{A + B x + C x^{2}}{\left(a + c x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + B*x + C*x**2)/(a + c*x**2)**(9/2)` | $\frac{A + B x + C x^{2}}{\left(a + c x^{2}\right)^{\frac{9}{2}}}$ |
| partial | concrete | `(2*x + 1)**3*(4*x**2 + 3*x + 1)/sqrt(3*x**2 + 2)` | $\frac{\left(2 x + 1\right)^{3} \left(4 x^{2} + 3 x + 1\right)}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(2*x + 1)**2*(4*x**2 + 3*x + 1)/sqrt(3*x**2 + 2)` | $\frac{\left(2 x + 1\right)^{2} \left(4 x^{2} + 3 x + 1\right)}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(2*x + 1)*(4*x**2 + 3*x + 1)/sqrt(3*x**2 + 2)` | $\frac{\left(2 x + 1\right) \left(4 x^{2} + 3 x + 1\right)}{\sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)*sqrt(3*x**2 + 2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right) \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)**2*sqrt(3*x**2 + 2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right)^{2} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)**3*sqrt(3*x**2 + 2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right)^{3} \sqrt{3 x^{2} + 2}}$ |
| partial | concrete | `(2*x + 1)**3*(4*x**2 + 3*x + 1)/(3*x**2 + 2)**(3/2)` | $\frac{\left(2 x + 1\right)^{3} \left(4 x^{2} + 3 x + 1\right)}{\left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2*x + 1)**2*(4*x**2 + 3*x + 1)/(3*x**2 + 2)**(3/2)` | $\frac{\left(2 x + 1\right)^{2} \left(4 x^{2} + 3 x + 1\right)}{\left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2*x + 1)*(4*x**2 + 3*x + 1)/(3*x**2 + 2)**(3/2)` | $\frac{\left(2 x + 1\right) \left(4 x^{2} + 3 x + 1\right)}{\left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)*(3*x**2 + 2)**(3/2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right) \left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)**2*(3*x**2 + 2)**(3/2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right)^{2} \left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)**3*(3*x**2 + 2)**(3/2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right)^{3} \left(3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2*x + 1)**3*(4*x**2 + 3*x + 1)/(3*x**2 + 2)**(5/2)` | $\frac{\left(2 x + 1\right)^{3} \left(4 x^{2} + 3 x + 1\right)}{\left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(2*x + 1)**2*(4*x**2 + 3*x + 1)/(3*x**2 + 2)**(5/2)` | $\frac{\left(2 x + 1\right)^{2} \left(4 x^{2} + 3 x + 1\right)}{\left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(2*x + 1)*(4*x**2 + 3*x + 1)/(3*x**2 + 2)**(5/2)` | $\frac{\left(2 x + 1\right) \left(4 x^{2} + 3 x + 1\right)}{\left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)*(3*x**2 + 2)**(5/2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right) \left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)**2*(3*x**2 + 2)**(5/2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right)^{2} \left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)**3*(3*x**2 + 2)**(5/2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right)^{3} \left(3 x^{2} + 2\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + C*x**2)*(a + b*x + c*x**2)**(5/2)` | $\left(A + C x^{2}\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(A + C*x**2)*(a + b*x + c*x**2)**(3/2)` | $\left(A + C x^{2}\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(A + C*x**2)*sqrt(a + b*x + c*x**2)` | $\left(A + C x^{2}\right) \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(A + C*x**2)/sqrt(a + b*x + c*x**2)` | $\frac{A + C x^{2}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + C*x**2)/(a + b*x + c*x**2)**(3/2)` | $\frac{A + C x^{2}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(A + C*x**2)/(a + b*x + c*x**2)**(5/2)` | $\frac{A + C x^{2}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(A + C*x**2)/(a + b*x + c*x**2)**(7/2)` | $\frac{A + C x^{2}}{\left(a + b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(A + C*x**2)/(a + b*x + c*x**2)**(9/2)` | $\frac{A + C x^{2}}{\left(a + b x + c x^{2}\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(g + h*x)**3*sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)` | $\left(g + h x\right)^{3} \sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `(g + h*x)**2*sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)` | $\left(g + h x\right)^{2} \sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `(g + h*x)*sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)` | $\left(g + h x\right) \sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)` | $\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)/(g + h*x)` | $\frac{\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}{g + h x}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)/(g + h*x)**2` | $\frac{\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{2}}$ |
| partial | parametric | `sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)/(g + h*x)**3` | $\frac{\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{3}}$ |
| timeout | parametric | `sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)/(g + h*x)**4` | $\frac{\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{4}}$ |
| timeout | parametric | `sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)/(g + h*x)**5` | $\frac{\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{5}}$ |
| timeout | parametric | `sqrt(a + b*x + c*x**2)*(d + e*x + f*x**2)/(g + h*x)**6` | $\frac{\sqrt{a + b x + c x^{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{6}}$ |
| partial | parametric | `(g + h*x)**3*(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)` | $\left(g + h x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `(g + h*x)**2*(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)` | $\left(g + h x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `(g + h*x)*(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)` | $\left(g + h x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)` | $\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{g + h x}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**2` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{2}}$ |
| partial | parametric | `(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**3` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{3}}$ |
| timeout | parametric | `(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**4` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{4}}$ |
| timeout | parametric | `(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**5` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{5}}$ |
| timeout | parametric | `(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**6` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{6}}$ |
| timeout | parametric | `(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**7` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{7}}$ |
| timeout | parametric | `(a + b*x + c*x**2)**(3/2)*(d + e*x + f*x**2)/(g + h*x)**8` | $\frac{\left(a + b x + c x^{2}\right)^{\frac{3}{2}} \left(d + e x + f x^{2}\right)}{\left(g + h x\right)^{8}}$ |
| partial | concrete | `(2*x + 1)**3*sqrt(3*x**2 - x + 2)*(4*x**2 + 3*x + 1)` | $\left(2 x + 1\right)^{3} \sqrt{3 x^{2} - x + 2} \left(4 x^{2} + 3 x + 1\right)$ |
| partial | concrete | `(2*x + 1)**2*sqrt(3*x**2 - x + 2)*(4*x**2 + 3*x + 1)` | $\left(2 x + 1\right)^{2} \sqrt{3 x^{2} - x + 2} \left(4 x^{2} + 3 x + 1\right)$ |
| partial | concrete | `(2*x + 1)*sqrt(3*x**2 - x + 2)*(4*x**2 + 3*x + 1)` | $\left(2 x + 1\right) \sqrt{3 x^{2} - x + 2} \left(4 x^{2} + 3 x + 1\right)$ |
| partial | concrete | `sqrt(3*x**2 - x + 2)*(4*x**2 + 3*x + 1)/(2*x + 1)` | $\frac{\sqrt{3 x^{2} - x + 2} \left(4 x^{2} + 3 x + 1\right)}{2 x + 1}$ |
| partial | concrete | `sqrt(3*x**2 - x + 2)*(4*x**2 + 3*x + 1)/(2*x + 1)**2` | $\frac{\sqrt{3 x^{2} - x + 2} \left(4 x^{2} + 3 x + 1\right)}{\left(2 x + 1\right)^{2}}$ |
| partial | concrete | `sqrt(3*x**2 - x + 2)*(4*x**2 + 3*x + 1)/(2*x + 1)**3` | $\frac{\sqrt{3 x^{2} - x + 2} \left(4 x^{2} + 3 x + 1\right)}{\left(2 x + 1\right)^{3}}$ |
| partial | concrete | `(2*x + 1)**3*(3*x**2 - x + 2)**(3/2)*(4*x**2 + 3*x + 1)` | $\left(2 x + 1\right)^{3} \left(3 x^{2} - x + 2\right)^{\frac{3}{2}} \left(4 x^{2} + 3 x + 1\right)$ |
| partial | concrete | `(2*x + 1)**2*(3*x**2 - x + 2)**(3/2)*(4*x**2 + 3*x + 1)` | $\left(2 x + 1\right)^{2} \left(3 x^{2} - x + 2\right)^{\frac{3}{2}} \left(4 x^{2} + 3 x + 1\right)$ |
| partial | concrete | `(2*x + 1)*(3*x**2 - x + 2)**(3/2)*(4*x**2 + 3*x + 1)` | $\left(2 x + 1\right) \left(3 x^{2} - x + 2\right)^{\frac{3}{2}} \left(4 x^{2} + 3 x + 1\right)$ |
| partial | concrete | `(3*x**2 - x + 2)**(3/2)*(4*x**2 + 3*x + 1)/(2*x + 1)` | $\frac{\left(3 x^{2} - x + 2\right)^{\frac{3}{2}} \left(4 x^{2} + 3 x + 1\right)}{2 x + 1}$ |
| partial | concrete | `(3*x**2 - x + 2)**(3/2)*(4*x**2 + 3*x + 1)/(2*x + 1)**2` | $\frac{\left(3 x^{2} - x + 2\right)^{\frac{3}{2}} \left(4 x^{2} + 3 x + 1\right)}{\left(2 x + 1\right)^{2}}$ |
| partial | concrete | `(3*x**2 - x + 2)**(3/2)*(4*x**2 + 3*x + 1)/(2*x + 1)**3` | $\frac{\left(3 x^{2} - x + 2\right)^{\frac{3}{2}} \left(4 x^{2} + 3 x + 1\right)}{\left(2 x + 1\right)^{3}}$ |
| partial | concrete | `(2*x + 1)**3*(3*x**2 - x + 2)**(5/2)*(4*x**2 + 3*x + 1)` | $\left(2 x + 1\right)^{3} \left(3 x^{2} - x + 2\right)^{\frac{5}{2}} \left(4 x^{2} + 3 x + 1\right)$ |
| partial | concrete | `(2*x + 1)**2*(3*x**2 - x + 2)**(5/2)*(4*x**2 + 3*x + 1)` | $\left(2 x + 1\right)^{2} \left(3 x^{2} - x + 2\right)^{\frac{5}{2}} \left(4 x^{2} + 3 x + 1\right)$ |
| partial | concrete | `(2*x + 1)*(3*x**2 - x + 2)**(5/2)*(4*x**2 + 3*x + 1)` | $\left(2 x + 1\right) \left(3 x^{2} - x + 2\right)^{\frac{5}{2}} \left(4 x^{2} + 3 x + 1\right)$ |
| partial | concrete | `(3*x**2 - x + 2)**(5/2)*(4*x**2 + 3*x + 1)/(2*x + 1)` | $\frac{\left(3 x^{2} - x + 2\right)^{\frac{5}{2}} \left(4 x^{2} + 3 x + 1\right)}{2 x + 1}$ |
| partial | concrete | `(3*x**2 - x + 2)**(5/2)*(4*x**2 + 3*x + 1)/(2*x + 1)**2` | $\frac{\left(3 x^{2} - x + 2\right)^{\frac{5}{2}} \left(4 x^{2} + 3 x + 1\right)}{\left(2 x + 1\right)^{2}}$ |
| partial | concrete | `(3*x**2 - x + 2)**(5/2)*(4*x**2 + 3*x + 1)/(2*x + 1)**3` | $\frac{\left(3 x^{2} - x + 2\right)^{\frac{5}{2}} \left(4 x^{2} + 3 x + 1\right)}{\left(2 x + 1\right)^{3}}$ |
| partial | parametric | `(g + h*x)**3*(d + e*x + f*x**2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(g + h x\right)^{3} \left(d + e x + f x^{2}\right)}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(g + h*x)**2*(d + e*x + f*x**2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(g + h x\right)^{2} \left(d + e x + f x^{2}\right)}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(g + h*x)*(d + e*x + f*x**2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(g + h x\right) \left(d + e x + f x^{2}\right)}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/sqrt(a + b*x + c*x**2)` | $\frac{d + e x + f x^{2}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/((g + h*x)*sqrt(a + b*x + c*x**2))` | $\frac{d + e x + f x^{2}}{\left(g + h x\right) \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/((g + h*x)**2*sqrt(a + b*x + c*x**2))` | $\frac{d + e x + f x^{2}}{\left(g + h x\right)^{2} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/((g + h*x)**3*sqrt(a + b*x + c*x**2))` | $\frac{d + e x + f x^{2}}{\left(g + h x\right)^{3} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(g + h*x)**3*(d + e*x + f*x**2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(g + h x\right)^{3} \left(d + e x + f x^{2}\right)}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(g + h*x)**2*(d + e*x + f*x**2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(g + h x\right)^{2} \left(d + e x + f x^{2}\right)}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(g + h*x)*(d + e*x + f*x**2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(g + h x\right) \left(d + e x + f x^{2}\right)}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/(a + b*x + c*x**2)**(3/2)` | $\frac{d + e x + f x^{2}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/((g + h*x)*(a + b*x + c*x**2)**(3/2))` | $\frac{d + e x + f x^{2}}{\left(g + h x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/((g + h*x)**2*(a + b*x + c*x**2)**(3/2))` | $\frac{d + e x + f x^{2}}{\left(g + h x\right)^{2} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2)/((g + h*x)**3*(a + b*x + c*x**2)**(3/2))` | $\frac{d + e x + f x^{2}}{\left(g + h x\right)^{3} \left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2*x + 1)**3*(4*x**2 + 3*x + 1)/sqrt(3*x**2 - x + 2)` | $\frac{\left(2 x + 1\right)^{3} \left(4 x^{2} + 3 x + 1\right)}{\sqrt{3 x^{2} - x + 2}}$ |
| partial | concrete | `(2*x + 1)**2*(4*x**2 + 3*x + 1)/sqrt(3*x**2 - x + 2)` | $\frac{\left(2 x + 1\right)^{2} \left(4 x^{2} + 3 x + 1\right)}{\sqrt{3 x^{2} - x + 2}}$ |
| partial | concrete | `(2*x + 1)*(4*x**2 + 3*x + 1)/sqrt(3*x**2 - x + 2)` | $\frac{\left(2 x + 1\right) \left(4 x^{2} + 3 x + 1\right)}{\sqrt{3 x^{2} - x + 2}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)*sqrt(3*x**2 - x + 2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right) \sqrt{3 x^{2} - x + 2}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)**2*sqrt(3*x**2 - x + 2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right)^{2} \sqrt{3 x^{2} - x + 2}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)**3*sqrt(3*x**2 - x + 2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right)^{3} \sqrt{3 x^{2} - x + 2}}$ |
| partial | concrete | `(2*x + 1)**3*(4*x**2 + 3*x + 1)/(3*x**2 - x + 2)**(3/2)` | $\frac{\left(2 x + 1\right)^{3} \left(4 x^{2} + 3 x + 1\right)}{\left(3 x^{2} - x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2*x + 1)**2*(4*x**2 + 3*x + 1)/(3*x**2 - x + 2)**(3/2)` | $\frac{\left(2 x + 1\right)^{2} \left(4 x^{2} + 3 x + 1\right)}{\left(3 x^{2} - x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2*x + 1)*(4*x**2 + 3*x + 1)/(3*x**2 - x + 2)**(3/2)` | $\frac{\left(2 x + 1\right) \left(4 x^{2} + 3 x + 1\right)}{\left(3 x^{2} - x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)*(3*x**2 - x + 2)**(3/2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right) \left(3 x^{2} - x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)**2*(3*x**2 - x + 2)**(3/2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right)^{2} \left(3 x^{2} - x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)**3*(3*x**2 - x + 2)**(3/2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right)^{3} \left(3 x^{2} - x + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2*x + 1)**3*(4*x**2 + 3*x + 1)/(3*x**2 - x + 2)**(5/2)` | $\frac{\left(2 x + 1\right)^{3} \left(4 x^{2} + 3 x + 1\right)}{\left(3 x^{2} - x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(2*x + 1)**2*(4*x**2 + 3*x + 1)/(3*x**2 - x + 2)**(5/2)` | $\frac{\left(2 x + 1\right)^{2} \left(4 x^{2} + 3 x + 1\right)}{\left(3 x^{2} - x + 2\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(2*x + 1)*(4*x**2 + 3*x + 1)/(3*x**2 - x + 2)**(5/2)` | $\frac{\left(2 x + 1\right) \left(4 x^{2} + 3 x + 1\right)}{\left(3 x^{2} - x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)*(3*x**2 - x + 2)**(5/2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right) \left(3 x^{2} - x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)**2*(3*x**2 - x + 2)**(5/2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right)^{2} \left(3 x^{2} - x + 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(4*x**2 + 3*x + 1)/((2*x + 1)**3*(3*x**2 - x + 2)**(5/2))` | $\frac{4 x^{2} + 3 x + 1}{\left(2 x + 1\right)^{3} \left(3 x^{2} - x + 2\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(d + e*x + f*x**2)/((g + h*x)*(b*g*h + b*h**2*x - c*g**2 + c*h**2*x**2)**(3/2))` | $\frac{d + e x + f x^{2}}{\left(g + h x\right) \left(b g h + b h^{2} x - c g^{2} + c h^{2} x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(d + e*x)*(A + B*x + C*x**2)*sqrt(a + b*x + c*x**2)` | $\sqrt{d + e x} \left(A + B x + C x^{2}\right) \sqrt{a + b x + c x^{2}}$ |
| partial | parametric | `(A + B*x + C*x**2)*sqrt(a + b*x + c*x**2)/sqrt(d + e*x)` | $\frac{\left(A + B x + C x^{2}\right) \sqrt{a + b x + c x^{2}}}{\sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x + C*x**2)*sqrt(a + b*x + c*x**2)/(d + e*x)**(3/2)` | $\frac{\left(A + B x + C x^{2}\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)*sqrt(a + b*x + c*x**2)/(d + e*x)**(5/2)` | $\frac{\left(A + B x + C x^{2}\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)*sqrt(a + b*x + c*x**2)/(d + e*x)**(7/2)` | $\frac{\left(A + B x + C x^{2}\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)*sqrt(a + b*x + c*x**2)/(d + e*x)**(9/2)` | $\frac{\left(A + B x + C x^{2}\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{\frac{9}{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)*sqrt(a + b*x + c*x**2)/(d + e*x)**(11/2)` | $\frac{\left(A + B x + C x^{2}\right) \sqrt{a + b x + c x^{2}}}{\left(d + e x\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)*(A + B*x + C*x**2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \left(A + B x + C x^{2}\right)}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `sqrt(d + e*x)*(A + B*x + C*x**2)/sqrt(a + b*x + c*x**2)` | $\frac{\sqrt{d + e x} \left(A + B x + C x^{2}\right)}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)/(sqrt(d + e*x)*sqrt(a + b*x + c*x**2))` | $\frac{A + B x + C x^{2}}{\sqrt{d + e x} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)/((d + e*x)**(3/2)*sqrt(a + b*x + c*x**2))` | $\frac{A + B x + C x^{2}}{\left(d + e x\right)^{\frac{3}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)/((d + e*x)**(5/2)*sqrt(a + b*x + c*x**2))` | $\frac{A + B x + C x^{2}}{\left(d + e x\right)^{\frac{5}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(A + B*x + C*x**2)/((d + e*x)**(7/2)*sqrt(a + b*x + c*x**2))` | $\frac{A + B x + C x^{2}}{\left(d + e x\right)^{\frac{7}{2}} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `x**2*(d + e*x + f*x**2 + g*x**3)/sqrt(a + b*x + c*x**2)` | $\frac{x^{2} \left(d + e x + f x^{2} + g x^{3}\right)}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `x*(d + e*x + f*x**2 + g*x**3)/sqrt(a + b*x + c*x**2)` | $\frac{x \left(d + e x + f x^{2} + g x^{3}\right)}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2 + g*x**3)/sqrt(a + b*x + c*x**2)` | $\frac{d + e x + f x^{2} + g x^{3}}{\sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2 + g*x**3)/(x*sqrt(a + b*x + c*x**2))` | $\frac{d + e x + f x^{2} + g x^{3}}{x \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2 + g*x**3)/(x**2*sqrt(a + b*x + c*x**2))` | $\frac{d + e x + f x^{2} + g x^{3}}{x^{2} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2 + g*x**3)/(x**3*sqrt(a + b*x + c*x**2))` | $\frac{d + e x + f x^{2} + g x^{3}}{x^{3} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2 + g*x**3)/(x**4*sqrt(a + b*x + c*x**2))` | $\frac{d + e x + f x^{2} + g x^{3}}{x^{4} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2 + g*x**3)/(x**5*sqrt(a + b*x + c*x**2))` | $\frac{d + e x + f x^{2} + g x^{3}}{x^{5} \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2 + g*x**3)/(x**6*sqrt(a + b*x + c*x**2))` | $\frac{d + e x + f x^{2} + g x^{3}}{x^{6} \sqrt{a + b x + c x^{2}}}$ |
| partial | concrete | `(2*x + 5)*sqrt(2*x**2 - x + 3)*(5*x**4 - x**3 + 3*x**2 + x + 2)` | $\left(2 x + 5\right) \sqrt{2 x^{2} - x + 3} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**4 - x**3 + 3*x**2 + x + 2)` | $\sqrt{2 x^{2} - x + 3} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)` | $\frac{\sqrt{2 x^{2} - x + 3} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{2 x + 5}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**2` | $\frac{\sqrt{2 x^{2} - x + 3} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{2}}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**3` | $\frac{\sqrt{2 x^{2} - x + 3} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{3}}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**4` | $\frac{\sqrt{2 x^{2} - x + 3} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{4}}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**5` | $\frac{\sqrt{2 x^{2} - x + 3} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{5}}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**6` | $\frac{\sqrt{2 x^{2} - x + 3} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{6}}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**7` | $\frac{\sqrt{2 x^{2} - x + 3} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{7}}$ |
| partial | concrete | `sqrt(2*x**2 - x + 3)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**8` | $\frac{\sqrt{2 x^{2} - x + 3} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{8}}$ |
| partial | concrete | `(2*x + 5)*(2*x**2 - x + 3)**(3/2)*(5*x**4 - x**3 + 3*x**2 + x + 2)` | $\left(2 x + 5\right) \left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**4 - x**3 + 3*x**2 + x + 2)` | $\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{2 x + 5}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**2` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{2}}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**3` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{3}}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**4` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{4}}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**5` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{5}}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**6` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{6}}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**7` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{7}}$ |
| partial | concrete | `(2*x**2 - x + 3)**(3/2)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x + 5)**8` | $\frac{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x + 5\right)^{8}}$ |
| partial | concrete | `(2*x + 5)*(5*x**4 - x**3 + 3*x**2 + x + 2)/sqrt(2*x**2 - x + 3)` | $\frac{\left(2 x + 5\right) \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\sqrt{2 x^{2} - x + 3}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/sqrt(2*x**2 - x + 3)` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\sqrt{2 x^{2} - x + 3}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)*sqrt(2*x**2 - x + 3))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right) \sqrt{2 x^{2} - x + 3}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)**2*sqrt(2*x**2 - x + 3))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right)^{2} \sqrt{2 x^{2} - x + 3}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)**3*sqrt(2*x**2 - x + 3))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right)^{3} \sqrt{2 x^{2} - x + 3}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)**4*sqrt(2*x**2 - x + 3))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right)^{4} \sqrt{2 x^{2} - x + 3}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)**5*sqrt(2*x**2 - x + 3))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right)^{5} \sqrt{2 x^{2} - x + 3}}$ |
| partial | concrete | `(2*x + 5)**2*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x**2 - x + 3)**(3/2)` | $\frac{\left(2 x + 5\right)^{2} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2*x + 5)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x**2 - x + 3)**(3/2)` | $\frac{\left(2 x + 5\right) \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x**2 - x + 3)**(3/2)` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)*(2*x**2 - x + 3)**(3/2))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right) \left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)**2*(2*x**2 - x + 3)**(3/2))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right)^{2} \left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)**3*(2*x**2 - x + 3)**(3/2))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right)^{3} \left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)**4*(2*x**2 - x + 3)**(3/2))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right)^{4} \left(2 x^{2} - x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2*x + 5)**2*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x**2 - x + 3)**(5/2)` | $\frac{\left(2 x + 5\right)^{2} \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(2*x + 5)*(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x**2 - x + 3)**(5/2)` | $\frac{\left(2 x + 5\right) \left(5 x^{4} - x^{3} + 3 x^{2} + x + 2\right)}{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/(2*x**2 - x + 3)**(5/2)` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)*(2*x**2 - x + 3)**(5/2))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right) \left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)**2*(2*x**2 - x + 3)**(5/2))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right)^{2} \left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)**3*(2*x**2 - x + 3)**(5/2))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right)^{3} \left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(5*x**4 - x**3 + 3*x**2 + x + 2)/((2*x + 5)**4*(2*x**2 - x + 3)**(5/2))` | $\frac{5 x^{4} - x^{3} + 3 x^{2} + x + 2}{\left(2 x + 5\right)^{4} \left(2 x^{2} - x + 3\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(f + g*x + h*x**2 + i*x**3 + j*x**4)/(a + b*x + c*x**2)**(5/2)` | $\frac{f + g x + h x^{2} + i x^{3} + j x^{4}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(f + g*x + h*x**2 + i*x**3 + j*x**4)/(a + b*x - c*x**2)**(5/2)` | $\frac{f + g x + h x^{2} + i x^{3} + j x^{4}}{\left(a + b x - c x^{2}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(-7*x**2 + 4*x + 1)**3*(x**2 + 5*x + 2)*sqrt(5*x**2 + 2*x + 3)` | $\left(- 7 x^{2} + 4 x + 1\right)^{3} \left(x^{2} + 5 x + 2\right) \sqrt{5 x^{2} + 2 x + 3}$ |
| partial | concrete | `(-7*x**2 + 4*x + 1)**2*(x**2 + 5*x + 2)*sqrt(5*x**2 + 2*x + 3)` | $\left(- 7 x^{2} + 4 x + 1\right)^{2} \left(x^{2} + 5 x + 2\right) \sqrt{5 x^{2} + 2 x + 3}$ |
| partial | concrete | `(-7*x**2 + 4*x + 1)*(x**2 + 5*x + 2)*sqrt(5*x**2 + 2*x + 3)` | $\left(- 7 x^{2} + 4 x + 1\right) \left(x^{2} + 5 x + 2\right) \sqrt{5 x^{2} + 2 x + 3}$ |
| partial | concrete | `(x**2 + 5*x + 2)*sqrt(5*x**2 + 2*x + 3)/(-7*x**2 + 4*x + 1)` | $\frac{\left(x^{2} + 5 x + 2\right) \sqrt{5 x^{2} + 2 x + 3}}{- 7 x^{2} + 4 x + 1}$ |
| partial | concrete | `(x**2 + 5*x + 2)*sqrt(5*x**2 + 2*x + 3)/(-7*x**2 + 4*x + 1)**2` | $\frac{\left(x^{2} + 5 x + 2\right) \sqrt{5 x^{2} + 2 x + 3}}{\left(- 7 x^{2} + 4 x + 1\right)^{2}}$ |
| partial | concrete | `(x**2 + 5*x + 2)*sqrt(5*x**2 + 2*x + 3)/(-7*x**2 + 4*x + 1)**3` | $\frac{\left(x^{2} + 5 x + 2\right) \sqrt{5 x^{2} + 2 x + 3}}{\left(- 7 x^{2} + 4 x + 1\right)^{3}}$ |
| partial | concrete | `(-7*x**2 + 4*x + 1)**3*(x**2 + 5*x + 2)*(5*x**2 + 2*x + 3)**(3/2)` | $\left(- 7 x^{2} + 4 x + 1\right)^{3} \left(x^{2} + 5 x + 2\right) \left(5 x^{2} + 2 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(-7*x**2 + 4*x + 1)**2*(x**2 + 5*x + 2)*(5*x**2 + 2*x + 3)**(3/2)` | $\left(- 7 x^{2} + 4 x + 1\right)^{2} \left(x^{2} + 5 x + 2\right) \left(5 x^{2} + 2 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(-7*x**2 + 4*x + 1)*(x**2 + 5*x + 2)*(5*x**2 + 2*x + 3)**(3/2)` | $\left(- 7 x^{2} + 4 x + 1\right) \left(x^{2} + 5 x + 2\right) \left(5 x^{2} + 2 x + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(x**2 + 5*x + 2)*(5*x**2 + 2*x + 3)**(3/2)/(-7*x**2 + 4*x + 1)` | $\frac{\left(x^{2} + 5 x + 2\right) \left(5 x^{2} + 2 x + 3\right)^{\frac{3}{2}}}{- 7 x^{2} + 4 x + 1}$ |
| partial | concrete | `(x**2 + 5*x + 2)*(5*x**2 + 2*x + 3)**(3/2)/(-7*x**2 + 4*x + 1)**2` | $\frac{\left(x^{2} + 5 x + 2\right) \left(5 x^{2} + 2 x + 3\right)^{\frac{3}{2}}}{\left(- 7 x^{2} + 4 x + 1\right)^{2}}$ |
| partial | concrete | `(x**2 + 5*x + 2)*(5*x**2 + 2*x + 3)**(3/2)/(-7*x**2 + 4*x + 1)**3` | $\frac{\left(x^{2} + 5 x + 2\right) \left(5 x^{2} + 2 x + 3\right)^{\frac{3}{2}}}{\left(- 7 x^{2} + 4 x + 1\right)^{3}}$ |
| partial | concrete | `(-7*x**2 + 4*x + 1)**3*(x**2 + 5*x + 2)/sqrt(5*x**2 + 2*x + 3)` | $\frac{\left(- 7 x^{2} + 4 x + 1\right)^{3} \left(x^{2} + 5 x + 2\right)}{\sqrt{5 x^{2} + 2 x + 3}}$ |
| partial | concrete | `(-7*x**2 + 4*x + 1)**2*(x**2 + 5*x + 2)/sqrt(5*x**2 + 2*x + 3)` | $\frac{\left(- 7 x^{2} + 4 x + 1\right)^{2} \left(x^{2} + 5 x + 2\right)}{\sqrt{5 x^{2} + 2 x + 3}}$ |
| partial | concrete | `(-7*x**2 + 4*x + 1)*(x**2 + 5*x + 2)/sqrt(5*x**2 + 2*x + 3)` | $\frac{\left(- 7 x^{2} + 4 x + 1\right) \left(x^{2} + 5 x + 2\right)}{\sqrt{5 x^{2} + 2 x + 3}}$ |
| partial | concrete | `(x**2 + 5*x + 2)/((-7*x**2 + 4*x + 1)*sqrt(5*x**2 + 2*x + 3))` | $\frac{x^{2} + 5 x + 2}{\left(- 7 x^{2} + 4 x + 1\right) \sqrt{5 x^{2} + 2 x + 3}}$ |
| partial | concrete | `(x**2 + 5*x + 2)/((-7*x**2 + 4*x + 1)**2*sqrt(5*x**2 + 2*x + 3))` | $\frac{x^{2} + 5 x + 2}{\left(- 7 x^{2} + 4 x + 1\right)^{2} \sqrt{5 x^{2} + 2 x + 3}}$ |
| partial | concrete | `(x**2 + 5*x + 2)/((-7*x**2 + 4*x + 1)**3*sqrt(5*x**2 + 2*x + 3))` | $\frac{x^{2} + 5 x + 2}{\left(- 7 x^{2} + 4 x + 1\right)^{3} \sqrt{5 x^{2} + 2 x + 3}}$ |
| partial | concrete | `(-7*x**2 + 4*x + 1)**3*(x**2 + 5*x + 2)/(5*x**2 + 2*x + 3)**(3/2)` | $\frac{\left(- 7 x^{2} + 4 x + 1\right)^{3} \left(x^{2} + 5 x + 2\right)}{\left(5 x^{2} + 2 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(-7*x**2 + 4*x + 1)**2*(x**2 + 5*x + 2)/(5*x**2 + 2*x + 3)**(3/2)` | $\frac{\left(- 7 x^{2} + 4 x + 1\right)^{2} \left(x^{2} + 5 x + 2\right)}{\left(5 x^{2} + 2 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(-7*x**2 + 4*x + 1)*(x**2 + 5*x + 2)/(5*x**2 + 2*x + 3)**(3/2)` | $\frac{\left(- 7 x^{2} + 4 x + 1\right) \left(x^{2} + 5 x + 2\right)}{\left(5 x^{2} + 2 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x**2 + 5*x + 2)/((-7*x**2 + 4*x + 1)*(5*x**2 + 2*x + 3)**(3/2))` | $\frac{x^{2} + 5 x + 2}{\left(- 7 x^{2} + 4 x + 1\right) \left(5 x^{2} + 2 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x**2 + 5*x + 2)/((-7*x**2 + 4*x + 1)**2*(5*x**2 + 2*x + 3)**(3/2))` | $\frac{x^{2} + 5 x + 2}{\left(- 7 x^{2} + 4 x + 1\right)^{2} \left(5 x^{2} + 2 x + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x**2 + 5*x + 2)/((-7*x**2 + 4*x + 1)**3*(5*x**2 + 2*x + 3)**(3/2))` | $\frac{x^{2} + 5 x + 2}{\left(- 7 x^{2} + 4 x + 1\right)^{3} \left(5 x^{2} + 2 x + 3\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/4)` | $\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{4}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(1/4)` | $\sqrt[4]{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(-1/4)` | $\frac{1}{\sqrt[4]{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(-3/4)` | $\frac{1}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/sqrt(-3*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{- 3 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 + 4*x**2 + 2)` | $\frac{1}{\sqrt{- 3 x^{4} + 4 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 + 3*x**2 + 2)` | $\frac{1}{\sqrt{- 3 x^{4} + 3 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 + 2*x**2 + 2)` | $\frac{1}{\sqrt{- 3 x^{4} + 2 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 + x**2 + 2)` | $\frac{1}{\sqrt{- 3 x^{4} + x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(2 - 3*x**4)` | $\frac{1}{\sqrt{2 - 3 x^{4}}}$ |
| partial | concrete | `1/sqrt(-3*x**4 - x**2 + 2)` | $\frac{1}{\sqrt{- 3 x^{4} - x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 - 2*x**2 + 2)` | $\frac{1}{\sqrt{- 3 x^{4} - 2 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 - 3*x**2 + 2)` | $\frac{1}{\sqrt{- 3 x^{4} - 3 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 - 4*x**2 + 2)` | $\frac{1}{\sqrt{- 3 x^{4} - 4 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 - 5*x**2 + 2)` | $\frac{1}{\sqrt{- 3 x^{4} - 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 7*x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} + 7 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 6*x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} + 6 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 5*x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 4*x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} + 4 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 3*x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} + 3 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 2*x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} + 2 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} + x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(3 - 2*x**4)` | $\frac{1}{\sqrt{3 - 2 x^{4}}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} - x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - 2*x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} - 2 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - 3*x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} - 3 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - 4*x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} - 4 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - 5*x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} - 5 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - 6*x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} - 6 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - 7*x**2 + 3)` | $\frac{1}{\sqrt{- 2 x^{4} - 7 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(3*x**4 + 5*x**2 - 2)` | $\frac{1}{\sqrt{3 x^{4} + 5 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 + 4*x**2 - 2)` | $\frac{1}{\sqrt{3 x^{4} + 4 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 + 3*x**2 - 2)` | $\frac{1}{\sqrt{3 x^{4} + 3 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 + 2*x**2 - 2)` | $\frac{1}{\sqrt{3 x^{4} + 2 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 + x**2 - 2)` | $\frac{1}{\sqrt{3 x^{4} + x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 - 2)` | $\frac{1}{\sqrt{3 x^{4} - 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 - x**2 - 2)` | $\frac{1}{\sqrt{3 x^{4} - x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 - 2*x**2 - 2)` | $\frac{1}{\sqrt{3 x^{4} - 2 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 - 3*x**2 - 2)` | $\frac{1}{\sqrt{3 x^{4} - 3 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 - 4*x**2 - 2)` | $\frac{1}{\sqrt{3 x^{4} - 4 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 - 5*x**2 - 2)` | $\frac{1}{\sqrt{3 x^{4} - 5 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 7*x**2 - 3)` | $\frac{1}{\sqrt{2 x^{4} + 7 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 6*x**2 - 3)` | $\frac{1}{\sqrt{2 x^{4} + 6 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 5*x**2 - 3)` | $\frac{1}{\sqrt{2 x^{4} + 5 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 4*x**2 - 3)` | $\frac{1}{\sqrt{2 x^{4} + 4 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 3*x**2 - 3)` | $\frac{1}{\sqrt{2 x^{4} + 3 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 2*x**2 - 3)` | $\frac{1}{\sqrt{2 x^{4} + 2 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + x**2 - 3)` | $\frac{1}{\sqrt{2 x^{4} + x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - 3)` | $\frac{1}{\sqrt{2 x^{4} - 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - x**2 - 3)` | $\frac{1}{\sqrt{2 x^{4} - x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - 2*x**2 - 3)` | $\frac{1}{\sqrt{2 x^{4} - 2 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - 3*x**2 - 3)` | $\frac{1}{\sqrt{2 x^{4} - 3 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - 4*x**2 - 3)` | $\frac{1}{\sqrt{2 x^{4} - 4 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - 5*x**2 - 3)` | $\frac{1}{\sqrt{2 x^{4} - 5 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(3*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{3 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 + 4*x**2 + 2)` | $\frac{1}{\sqrt{3 x^{4} + 4 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 + 3*x**2 + 2)` | $\frac{1}{\sqrt{3 x^{4} + 3 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 + 2*x**2 + 2)` | $\frac{1}{\sqrt{3 x^{4} + 2 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 + x**2 + 2)` | $\frac{1}{\sqrt{3 x^{4} + x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 + 2)` | $\frac{1}{\sqrt{3 x^{4} + 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 - x**2 + 2)` | $\frac{1}{\sqrt{3 x^{4} - x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 - 2*x**2 + 2)` | $\frac{1}{\sqrt{3 x^{4} - 2 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 - 3*x**2 + 2)` | $\frac{1}{\sqrt{3 x^{4} - 3 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 - 4*x**2 + 2)` | $\frac{1}{\sqrt{3 x^{4} - 4 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 - 5*x**2 + 2)` | $\frac{1}{\sqrt{3 x^{4} - 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 - 6*x**2 + 2)` | $\frac{1}{\sqrt{3 x^{4} - 6 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 9*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} + 9 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 8*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} + 8 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 7*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} + 7 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 6*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} + 6 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 5*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 4*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} + 4 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 3*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} + 3 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 2*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} + 2 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} + x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 3)` | $\frac{1}{\sqrt{2 x^{4} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} - x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - 2*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} - 2 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - 3*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} - 3 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - 4*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} - 4 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - 5*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} - 5 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - 6*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} - 6 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(2*x**4 - 7*x**2 + 3)` | $\frac{1}{\sqrt{2 x^{4} - 7 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 7*x**2 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} + 7 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 6*x**2 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} + 6 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 5*x**2 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} + 5 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 4*x**2 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} + 4 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 3*x**2 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} + 3 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 2*x**2 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} + 2 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + x**2 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} + x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} - 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - x**2 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} - x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - 2*x**2 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} - 2 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - 3*x**2 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} - 3 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - 4*x**2 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} - 4 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(-2*x**4 - 5*x**2 - 3)` | $\frac{1}{\sqrt{- 2 x^{4} - 5 x^{2} - 3}}$ |
| partial | concrete | `1/sqrt(-3*x**4 + 6*x**2 - 2)` | $\frac{1}{\sqrt{- 3 x^{4} + 6 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 + 5*x**2 - 2)` | $\frac{1}{\sqrt{- 3 x^{4} + 5 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 + 4*x**2 - 2)` | $\frac{1}{\sqrt{- 3 x^{4} + 4 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 + 3*x**2 - 2)` | $\frac{1}{\sqrt{- 3 x^{4} + 3 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 + 2*x**2 - 2)` | $\frac{1}{\sqrt{- 3 x^{4} + 2 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 + x**2 - 2)` | $\frac{1}{\sqrt{- 3 x^{4} + x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 - 2)` | $\frac{1}{\sqrt{- 3 x^{4} - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 - x**2 - 2)` | $\frac{1}{\sqrt{- 3 x^{4} - x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 - 2*x**2 - 2)` | $\frac{1}{\sqrt{- 3 x^{4} - 2 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 - 3*x**2 - 2)` | $\frac{1}{\sqrt{- 3 x^{4} - 3 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 - 4*x**2 - 2)` | $\frac{1}{\sqrt{- 3 x^{4} - 4 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 - 5*x**2 - 2)` | $\frac{1}{\sqrt{- 3 x^{4} - 5 x^{2} - 2}}$ |
| partial | concrete | `1/sqrt(5*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{5 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(4*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{4 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(3*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{3 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(2*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{2 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{- x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-2*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{- 2 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-3*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{- 3 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-4*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{- 4 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-5*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{- 5 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-6*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{- 6 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-7*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{- 7 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-8*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{- 8 x^{4} + 5 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-9*x**4 + 5*x**2 + 2)` | $\frac{1}{\sqrt{- 9 x^{4} + 5 x^{2} + 2}}$ |
| partial | parametric | `x**5*sqrt(b*x**2 + c*x**4)` | $x^{5} \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**3*sqrt(b*x**2 + c*x**4)` | $x^{3} \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `x*sqrt(b*x**2 + c*x**4)` | $x \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x**3` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{3}}$ |
| **SOLVED-NEW** | parametric | `sqrt(b*x**2 + c*x**4)/x**5` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `sqrt(b*x**2 + c*x**4)/x**7` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `sqrt(b*x**2 + c*x**4)/x**9` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `sqrt(b*x**2 + c*x**4)/x**11` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `sqrt(b*x**2 + c*x**4)/x**13` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{13}}$ |
| **SOLVED-NEW** | parametric | `x**4*sqrt(b*x**2 + c*x**4)` | $x^{4} \sqrt{b x^{2} + c x^{4}}$ |
| **SOLVED-NEW** | parametric | `x**2*sqrt(b*x**2 + c*x**4)` | $x^{2} \sqrt{b x^{2} + c x^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(b*x**2 + c*x**4)` | $\sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x**2` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{2}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x**4` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{4}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x**6` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{6}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x**8` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{8}}$ |
| partial | parametric | `x**3*(b*x**2 + c*x**4)**(3/2)` | $x^{3} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(b*x**2 + c*x**4)**(3/2)` | $x \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**3` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**5` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**7` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(b*x**2 + c*x**4)**(3/2)/x**9` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `(b*x**2 + c*x**4)**(3/2)/x**11` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `(b*x**2 + c*x**4)**(3/2)/x**13` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{13}}$ |
| **SOLVED-NEW** | parametric | `(b*x**2 + c*x**4)**(3/2)/x**15` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{15}}$ |
| **SOLVED-NEW** | parametric | `(b*x**2 + c*x**4)**(3/2)/x**17` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{17}}$ |
| partial | parametric | `x**6*(b*x**2 + c*x**4)**(3/2)` | $x^{6} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**4*(b*x**2 + c*x**4)**(3/2)` | $x^{4} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(b*x**2 + c*x**4)**(3/2)` | $x^{2} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)` | $\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**2` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**4` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**6` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**8` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{8}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**10` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{10}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**12` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{12}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**14` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{14}}$ |
| partial | parametric | `x**7/sqrt(b*x**2 + c*x**4)` | $\frac{x^{7}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**5/sqrt(b*x**2 + c*x**4)` | $\frac{x^{5}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**3/sqrt(b*x**2 + c*x**4)` | $\frac{x^{3}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x/sqrt(b*x**2 + c*x**4)` | $\frac{x}{\sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x \sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**3*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{3} \sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**5*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{5} \sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**7*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{7} \sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `x**4/sqrt(b*x**2 + c*x**4)` | $\frac{x^{4}}{\sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `x**2/sqrt(b*x**2 + c*x**4)` | $\frac{x^{2}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/sqrt(b*x**2 + c*x**4)` | $\frac{1}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**2*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{2} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**4*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{4} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**9/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{9}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**7/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{7}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{5}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**3/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{3}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/(b*x**2 + c*x**4)**(3/2)` | $\frac{x}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x*(b*x**2 + c*x**4)**(3/2))` | $\frac{1}{x \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**3*(b*x**2 + c*x**4)**(3/2))` | $\frac{1}{x^{3} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**5*(b*x**2 + c*x**4)**(3/2))` | $\frac{1}{x^{5} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**6/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{6}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**4/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{4}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{2}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(-3/2)` | $\frac{1}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(b*x**2 + c*x**4)**(3/2))` | $\frac{1}{x^{2} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**3/sqrt(-4*x**4 + 3*x**2)` | $\frac{x^{3}}{\sqrt{- 4 x^{4} + 3 x^{2}}}$ |
| partial | concrete | `x**3/sqrt(-4*x**4 - 3*x**2)` | $\frac{x^{3}}{\sqrt{- 4 x^{4} - 3 x^{2}}}$ |
| partial | concrete | `x**3/sqrt(4*x**4 + 3*x**2)` | $\frac{x^{3}}{\sqrt{4 x^{4} + 3 x^{2}}}$ |
| partial | concrete | `x**3/sqrt(4*x**4 - 3*x**2)` | $\frac{x^{3}}{\sqrt{4 x^{4} - 3 x^{2}}}$ |
| partial | parametric | `x**3/sqrt(a*x**2 + b*x**4)` | $\frac{x^{3}}{\sqrt{a x^{2} + b x^{4}}}$ |
| partial | parametric | `x**3/sqrt(a*x**2 - b*x**4)` | $\frac{x^{3}}{\sqrt{a x^{2} - b x^{4}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(b*x**2 + c*x**4)` | $x^{\frac{7}{2}} \left(b x^{2} + c x^{4}\right)$ |
| SOLVED-both | parametric | `x**(5/2)*(b*x**2 + c*x**4)` | $x^{\frac{5}{2}} \left(b x^{2} + c x^{4}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(b*x**2 + c*x**4)` | $x^{\frac{3}{2}} \left(b x^{2} + c x^{4}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(b*x**2 + c*x**4)` | $\sqrt{x} \left(b x^{2} + c x^{4}\right)$ |
| SOLVED-both | parametric | `(b*x**2 + c*x**4)/sqrt(x)` | $\frac{b x^{2} + c x^{4}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(b*x**2 + c*x**4)/x**(3/2)` | $\frac{b x^{2} + c x^{4}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*x**2 + c*x**4)/x**(5/2)` | $\frac{b x^{2} + c x^{4}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b*x**2 + c*x**4)/x**(7/2)` | $\frac{b x^{2} + c x^{4}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(b*x**2 + c*x**4)**2` | $x^{\frac{7}{2}} \left(b x^{2} + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `x**(5/2)*(b*x**2 + c*x**4)**2` | $x^{\frac{5}{2}} \left(b x^{2} + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(b*x**2 + c*x**4)**2` | $x^{\frac{3}{2}} \left(b x^{2} + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(b*x**2 + c*x**4)**2` | $\sqrt{x} \left(b x^{2} + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `(b*x**2 + c*x**4)**2/sqrt(x)` | $\frac{\left(b x^{2} + c x^{4}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(b*x**2 + c*x**4)**2/x**(3/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*x**2 + c*x**4)**2/x**(5/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b*x**2 + c*x**4)**2/x**(7/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(7/2)*(b*x**2 + c*x**4)**3` | $x^{\frac{7}{2}} \left(b x^{2} + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `x**(5/2)*(b*x**2 + c*x**4)**3` | $x^{\frac{5}{2}} \left(b x^{2} + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(b*x**2 + c*x**4)**3` | $x^{\frac{3}{2}} \left(b x^{2} + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(b*x**2 + c*x**4)**3` | $\sqrt{x} \left(b x^{2} + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `(b*x**2 + c*x**4)**3/sqrt(x)` | $\frac{\left(b x^{2} + c x^{4}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(b*x**2 + c*x**4)**3/x**(3/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(b*x**2 + c*x**4)**3/x**(5/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(b*x**2 + c*x**4)**3/x**(7/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{3}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `x**(13/2)/(b*x**2 + c*x**4)` | $\frac{x^{\frac{13}{2}}}{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(11/2)/(b*x**2 + c*x**4)` | $\frac{x^{\frac{11}{2}}}{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(9/2)/(b*x**2 + c*x**4)` | $\frac{x^{\frac{9}{2}}}{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(7/2)/(b*x**2 + c*x**4)` | $\frac{x^{\frac{7}{2}}}{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(5/2)/(b*x**2 + c*x**4)` | $\frac{x^{\frac{5}{2}}}{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(3/2)/(b*x**2 + c*x**4)` | $\frac{x^{\frac{3}{2}}}{b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(x)/(b*x**2 + c*x**4)` | $\frac{\sqrt{x}}{b x^{2} + c x^{4}}$ |
| partial | parametric | `1/(sqrt(x)*(b*x**2 + c*x**4))` | $\frac{1}{\sqrt{x} \left(b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `1/(x**(3/2)*(b*x**2 + c*x**4))` | $\frac{1}{x^{\frac{3}{2}} \left(b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `1/(x**(5/2)*(b*x**2 + c*x**4))` | $\frac{1}{x^{\frac{5}{2}} \left(b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `1/(x**(7/2)*(b*x**2 + c*x**4))` | $\frac{1}{x^{\frac{7}{2}} \left(b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**(19/2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{19}{2}}}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(17/2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{17}{2}}}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(15/2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{15}{2}}}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(13/2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{13}{2}}}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(11/2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{11}{2}}}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(9/2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{9}{2}}}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(7/2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{7}{2}}}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(5/2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{5}{2}}}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(3/2)/(b*x**2 + c*x**4)**2` | $\frac{x^{\frac{3}{2}}}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `sqrt(x)/(b*x**2 + c*x**4)**2` | $\frac{\sqrt{x}}{\left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(x)*(b*x**2 + c*x**4)**2)` | $\frac{1}{\sqrt{x} \left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `1/(x**(3/2)*(b*x**2 + c*x**4)**2)` | $\frac{1}{x^{\frac{3}{2}} \left(b x^{2} + c x^{4}\right)^{2}}$ |
| partial | parametric | `x**(23/2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{23}{2}}}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(21/2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{21}{2}}}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(19/2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{19}{2}}}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(17/2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{17}{2}}}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(15/2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{15}{2}}}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(13/2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{13}{2}}}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(11/2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{11}{2}}}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(9/2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{9}{2}}}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(7/2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{7}{2}}}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(5/2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{5}{2}}}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(3/2)/(b*x**2 + c*x**4)**3` | $\frac{x^{\frac{3}{2}}}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `sqrt(x)/(b*x**2 + c*x**4)**3` | $\frac{\sqrt{x}}{\left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `1/(sqrt(x)*(b*x**2 + c*x**4)**3)` | $\frac{1}{\sqrt{x} \left(b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `x**(7/2)*sqrt(b*x**2 + c*x**4)` | $x^{\frac{7}{2}} \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(5/2)*sqrt(b*x**2 + c*x**4)` | $x^{\frac{5}{2}} \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(3/2)*sqrt(b*x**2 + c*x**4)` | $x^{\frac{3}{2}} \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(x)*sqrt(b*x**2 + c*x**4)` | $\sqrt{x} \sqrt{b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/sqrt(x)` | $\frac{\sqrt{b x^{2} + c x^{4}}}{\sqrt{x}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x**(3/2)` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x**(5/2)` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x**(7/2)` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x**(9/2)` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x**(11/2)` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x**(13/2)` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{\frac{13}{2}}}$ |
| partial | parametric | `sqrt(b*x**2 + c*x**4)/x**(15/2)` | $\frac{\sqrt{b x^{2} + c x^{4}}}{x^{\frac{15}{2}}}$ |
| partial | parametric | `x**(3/2)*(b*x**2 + c*x**4)**(3/2)` | $x^{\frac{3}{2}} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(x)*(b*x**2 + c*x**4)**(3/2)` | $\sqrt{x} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/sqrt(x)` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**(3/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**(5/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**(7/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**(9/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{9}{2}}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**(11/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{11}{2}}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**(13/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{13}{2}}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**(15/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{15}{2}}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**(17/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{17}{2}}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**(19/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{19}{2}}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**(21/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{21}{2}}}$ |
| partial | parametric | `(b*x**2 + c*x**4)**(3/2)/x**(23/2)` | $\frac{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{\frac{23}{2}}}$ |
| partial | parametric | `x**(13/2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{\frac{13}{2}}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**(11/2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{\frac{11}{2}}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**(9/2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{\frac{9}{2}}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**(7/2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{\frac{7}{2}}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**(5/2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{\frac{5}{2}}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**(3/2)/sqrt(b*x**2 + c*x**4)` | $\frac{x^{\frac{3}{2}}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `sqrt(x)/sqrt(b*x**2 + c*x**4)` | $\frac{\sqrt{x}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(b*x**2 + c*x**4))` | $\frac{1}{\sqrt{x} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**(3/2)*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{\frac{3}{2}} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**(5/2)*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{\frac{5}{2}} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**(7/2)*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{\frac{7}{2}} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**(9/2)*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{\frac{9}{2}} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**(11/2)*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{\frac{11}{2}} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**(17/2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{17}{2}}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(15/2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{15}{2}}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(13/2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{13}{2}}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(11/2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{11}{2}}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(9/2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{9}{2}}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(7/2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{7}{2}}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(5/2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{5}{2}}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**(3/2)/(b*x**2 + c*x**4)**(3/2)` | $\frac{x^{\frac{3}{2}}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)/(b*x**2 + c*x**4)**(3/2)` | $\frac{\sqrt{x}}{\left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(x)*(b*x**2 + c*x**4)**(3/2))` | $\frac{1}{\sqrt{x} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**(3/2)*(b*x**2 + c*x**4)**(3/2))` | $\frac{1}{x^{\frac{3}{2}} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**(5/2)*(b*x**2 + c*x**4)**(3/2))` | $\frac{1}{x^{\frac{5}{2}} \left(b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**5*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $x^{5} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| **SOLVED-NEW** | parametric | `x**3*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $x^{3} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| **SOLVED-NEW** | parametric | `x*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $x \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**3` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x^{3}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**5` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**7` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**9` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**11` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `x**4*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $x^{4} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| **SOLVED-NEW** | parametric | `x**2*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $x^{2} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**2` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**4` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**6` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**8` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**10` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x^{10}}$ |
| **SOLVED-NEW** | parametric | `x**9*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $x^{9} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x**7*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $x^{7} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x**3*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $x^{3} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $x \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**3` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**5` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**7` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**9` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**11` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**13` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{13}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**15` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{15}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**17` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{17}}$ |
| **SOLVED-NEW** | parametric | `x**8*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $x^{8} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x**6*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $x^{6} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x**4*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $x^{4} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x**2*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $x^{2} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**2` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{2}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**4` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{4}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**6` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**8` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**10` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{10}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**12` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{12}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**14` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{14}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**16` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{x^{16}}$ |
| **SOLVED-NEW** | parametric | `x**13*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x^{13} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**11*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x^{11} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**9*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x^{9} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**7*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x^{7} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**5*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x^{5} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**3*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x^{3} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**3` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**5` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{5}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**7` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{7}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**9` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{9}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**11` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**13` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{13}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**15` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{15}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**17` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{17}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**19` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{19}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**21` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{21}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**23` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{23}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**25` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{25}}$ |
| **SOLVED-NEW** | parametric | `x**12*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x^{12} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**10*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x^{10} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**8*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x^{8} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**6*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x^{6} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**4*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x^{4} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**2*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $x^{2} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**2` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{2}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**4` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{4}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**6` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**8` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**10` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{10}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**12` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{12}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**14` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{14}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**16` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{16}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**18` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{18}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**20` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{20}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**22` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{22}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**24` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{x^{24}}$ |
| **SOLVED-NEW** | parametric | `x**5/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{x^{5}}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| **SOLVED-NEW** | parametric | `x**3/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{x^{3}}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| **SOLVED-NEW** | parametric | `x/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{x}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `1/(x*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{1}{x \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `1/(x**3*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{1}{x^{3} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `x**4/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{x^{4}}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `x**2/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{x^{2}}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `1/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{1}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `1/(x**2*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{1}{x^{2} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `1/(x**4*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{1}{x^{4} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| **SOLVED-NEW** | parametric | `x**7/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{x^{7}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**5/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{x^{5}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{x}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | $\frac{1}{x \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | $\frac{1}{x^{3} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{x^{4}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{x^{2}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(-3/2)` | $\frac{1}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | $\frac{1}{x^{2} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | $\frac{1}{x^{4} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**11/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{x^{11}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**9/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{x^{9}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**7/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{x^{7}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**5/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{x^{5}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**3/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{x^{3}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{x}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2))` | $\frac{1}{x \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**3*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2))` | $\frac{1}{x^{3} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**6/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{x^{6}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{x^{4}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{x^{2}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(-5/2)` | $\frac{1}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**2*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2))` | $\frac{1}{x^{2} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**4*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2))` | $\frac{1}{x^{4} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2/(a**2 + 2*a*b*x**2 + b**2*x**4)**(1/3)` | $\frac{x^{2}}{\sqrt[3]{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(-1/3)` | $\frac{1}{\sqrt[3]{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `1/(x**2*(a**2 + 2*a*b*x**2 + b**2*x**4)**(1/3))` | $\frac{1}{x^{2} \sqrt[3]{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `x**2/(a**2 + 2*a*b*x**2 + b**2*x**4)**(2/3)` | $\frac{x^{2}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(-2/3)` | $\frac{1}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{2}{3}}}$ |
| partial | parametric | `1/(x**2*(a**2 + 2*a*b*x**2 + b**2*x**4)**(2/3))` | $\frac{1}{x^{2} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{2}{3}}}$ |
| SOLVED-both | parametric | `(d*x)**(5/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\left(d x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)$ |
| SOLVED-both | parametric | `(d*x)**(3/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\left(d x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)$ |
| SOLVED-both | parametric | `sqrt(d*x)*(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\sqrt{d x} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)/sqrt(d*x)` | $\frac{a^{2} + 2 a b x^{2} + b^{2} x^{4}}{\sqrt{d x}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)/(d*x)**(3/2)` | $\frac{a^{2} + 2 a b x^{2} + b^{2} x^{4}}{\left(d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)/(d*x)**(5/2)` | $\frac{a^{2} + 2 a b x^{2} + b^{2} x^{4}}{\left(d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)/(d*x)**(7/2)` | $\frac{a^{2} + 2 a b x^{2} + b^{2} x^{4}}{\left(d x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d*x)**(5/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\left(d x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `(d*x)**(3/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\left(d x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(d*x)*(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\sqrt{d x} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**2/sqrt(d*x)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}{\sqrt{d x}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**2/(d*x)**(3/2)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}{\left(d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**2/(d*x)**(5/2)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}{\left(d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**2/(d*x)**(7/2)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}{\left(d x\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(d*x)**(5/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\left(d x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `(d*x)**(3/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\left(d x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(d*x)*(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\sqrt{d x} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**3/sqrt(d*x)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}{\sqrt{d x}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**3/(d*x)**(3/2)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}{\left(d x\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**3/(d*x)**(5/2)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}{\left(d x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**3/(d*x)**(7/2)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}{\left(d x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d*x)**(11/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{\left(d x\right)^{\frac{11}{2}}}{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| partial | parametric | `(d*x)**(9/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{\left(d x\right)^{\frac{9}{2}}}{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| partial | parametric | `(d*x)**(7/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{\left(d x\right)^{\frac{7}{2}}}{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| partial | parametric | `(d*x)**(5/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{\left(d x\right)^{\frac{5}{2}}}{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| partial | parametric | `(d*x)**(3/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{\left(d x\right)^{\frac{3}{2}}}{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| partial | parametric | `sqrt(d*x)/(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{\sqrt{d x}}{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| partial | parametric | `1/(sqrt(d*x)*(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{1}{\sqrt{d x} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)}$ |
| partial | parametric | `1/((d*x)**(3/2)*(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{1}{\left(d x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)}$ |
| partial | parametric | `1/((d*x)**(5/2)*(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{1}{\left(d x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)}$ |
| partial | parametric | `1/((d*x)**(7/2)*(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{1}{\left(d x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)}$ |
| partial | parametric | `(d*x)**(19/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\frac{\left(d x\right)^{\frac{19}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `(d*x)**(17/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\frac{\left(d x\right)^{\frac{17}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `(d*x)**(15/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\frac{\left(d x\right)^{\frac{15}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `(d*x)**(13/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\frac{\left(d x\right)^{\frac{13}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `(d*x)**(11/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\frac{\left(d x\right)^{\frac{11}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `(d*x)**(9/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\frac{\left(d x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `(d*x)**(7/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\frac{\left(d x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `(d*x)**(5/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\frac{\left(d x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `(d*x)**(3/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\frac{\left(d x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `sqrt(d*x)/(a**2 + 2*a*b*x**2 + b**2*x**4)**2` | $\frac{\sqrt{d x}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(d*x)*(a**2 + 2*a*b*x**2 + b**2*x**4)**2)` | $\frac{1}{\sqrt{d x} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `1/((d*x)**(3/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**2)` | $\frac{1}{\left(d x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `1/((d*x)**(5/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**2)` | $\frac{1}{\left(d x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `1/((d*x)**(7/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**2)` | $\frac{1}{\left(d x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{2}}$ |
| partial | parametric | `(d*x)**(27/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{27}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(25/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{25}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(23/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{23}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(21/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{21}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(19/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{19}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(17/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{17}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(15/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{15}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(13/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{13}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(11/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{11}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(9/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(7/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(5/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(3/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\left(d x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `sqrt(d*x)/(a**2 + 2*a*b*x**2 + b**2*x**4)**3` | $\frac{\sqrt{d x}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `1/(sqrt(d*x)*(a**2 + 2*a*b*x**2 + b**2*x**4)**3)` | $\frac{1}{\sqrt{d x} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `1/((d*x)**(3/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**3)` | $\frac{1}{\left(d x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `1/((d*x)**(5/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**3)` | $\frac{1}{\left(d x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| partial | parametric | `1/((d*x)**(7/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**3)` | $\frac{1}{\left(d x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{3}}$ |
| **SOLVED-NEW** | parametric | `(d*x)**(5/2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\left(d x\right)^{\frac{5}{2}} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| **SOLVED-NEW** | parametric | `(d*x)**(3/2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\left(d x\right)^{\frac{3}{2}} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(d*x)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\sqrt{d x} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/sqrt(d*x)` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{\sqrt{d x}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/(d*x)**(3/2)` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{\left(d x\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/(d*x)**(5/2)` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{\left(d x\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/(d*x)**(7/2)` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{\left(d x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d*x)**(5/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\left(d x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d*x)**(3/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\left(d x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(d*x)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\sqrt{d x} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/sqrt(d*x)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{\sqrt{d x}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/(d*x)**(3/2)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{\left(d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/(d*x)**(5/2)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{\left(d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/(d*x)**(7/2)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}{\left(d x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d*x)**(5/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\left(d x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(d*x)**(3/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\left(d x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| partial | parametric | `sqrt(d*x)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\sqrt{d x} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/sqrt(d*x)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{\sqrt{d x}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/(d*x)**(3/2)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{\left(d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/(d*x)**(5/2)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{\left(d x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/(d*x)**(7/2)` | $\frac{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}{\left(d x\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(d*x)**(7/2)/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{\left(d x\right)^{\frac{7}{2}}}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `(d*x)**(5/2)/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{\left(d x\right)^{\frac{5}{2}}}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `(d*x)**(3/2)/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{\left(d x\right)^{\frac{3}{2}}}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `sqrt(d*x)/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{\sqrt{d x}}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `1/(sqrt(d*x)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{1}{\sqrt{d x} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `1/((d*x)**(3/2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{1}{\left(d x\right)^{\frac{3}{2}} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `1/((d*x)**(5/2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{1}{\left(d x\right)^{\frac{5}{2}} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `1/((d*x)**(7/2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{1}{\left(d x\right)^{\frac{7}{2}} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `(d*x)**(15/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{\left(d x\right)^{\frac{15}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d*x)**(13/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{\left(d x\right)^{\frac{13}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d*x)**(11/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{\left(d x\right)^{\frac{11}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d*x)**(9/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{\left(d x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d*x)**(7/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{\left(d x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d*x)**(5/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{\left(d x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d*x)**(3/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{\left(d x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(d*x)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{\sqrt{d x}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(d*x)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | $\frac{1}{\sqrt{d x} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d*x)**(3/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | $\frac{1}{\left(d x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d*x)**(5/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | $\frac{1}{\left(d x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d*x)**(7/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | $\frac{1}{\left(d x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d*x)**(23/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{\left(d x\right)^{\frac{23}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d*x)**(21/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{\left(d x\right)^{\frac{21}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d*x)**(19/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{\left(d x\right)^{\frac{19}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d*x)**(17/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{\left(d x\right)^{\frac{17}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d*x)**(15/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{\left(d x\right)^{\frac{15}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d*x)**(13/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{\left(d x\right)^{\frac{13}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d*x)**(11/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{\left(d x\right)^{\frac{11}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d*x)**(9/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{\left(d x\right)^{\frac{9}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d*x)**(7/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{\left(d x\right)^{\frac{7}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d*x)**(5/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{\left(d x\right)^{\frac{5}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(d*x)**(3/2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{\left(d x\right)^{\frac{3}{2}}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(d*x)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | $\frac{\sqrt{d x}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(sqrt(d*x)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2))` | $\frac{1}{\sqrt{d x} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d*x)**(3/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2))` | $\frac{1}{\left(d x\right)^{\frac{3}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d*x)**(5/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2))` | $\frac{1}{\left(d x\right)^{\frac{5}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/((d*x)**(7/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2))` | $\frac{1}{\left(d x\right)^{\frac{7}{2}} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**7*sqrt(a + b*x**2 + c*x**4)` | $x^{7} \sqrt{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x**5*sqrt(a + b*x**2 + c*x**4)` | $x^{5} \sqrt{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x**3*sqrt(a + b*x**2 + c*x**4)` | $x^{3} \sqrt{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x*sqrt(a + b*x**2 + c*x**4)` | $x \sqrt{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/x` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{x}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/x**3` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{x^{3}}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/x**5` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{x^{5}}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/x**7` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{x^{7}}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/x**9` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{x^{9}}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/x**11` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{x^{11}}$ |
| partial | parametric | `x**4*sqrt(a + b*x**2 + c*x**4)` | $x^{4} \sqrt{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x**2*sqrt(a + b*x**2 + c*x**4)` | $x^{2} \sqrt{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)` | $\sqrt{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/x**2` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/x**4` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{x^{4}}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/x**6` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{x^{6}}$ |
| partial | parametric | `x**7*(a + b*x**2 + c*x**4)**(3/2)` | $x^{7} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**5*(a + b*x**2 + c*x**4)**(3/2)` | $x^{5} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**3*(a + b*x**2 + c*x**4)**(3/2)` | $x^{3} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a + b*x**2 + c*x**4)**(3/2)` | $x \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/x` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/x**3` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/x**5` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/x**7` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/x**9` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{9}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/x**11` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{11}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/x**13` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{13}}$ |
| partial | parametric | `x**4*(a + b*x**2 + c*x**4)**(3/2)` | $x^{4} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(a + b*x**2 + c*x**4)**(3/2)` | $x^{2} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)` | $\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/x**2` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/x**4` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/x**6` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/x**8` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{8}}$ |
| partial | concrete | `sqrt(-x**4 - 2*x**2 + 3)` | $\sqrt{- x^{4} - 2 x^{2} + 3}$ |
| partial | parametric | `x**7/sqrt(a + b*x**2 + c*x**4)` | $\frac{x^{7}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**5/sqrt(a + b*x**2 + c*x**4)` | $\frac{x^{5}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**3/sqrt(a + b*x**2 + c*x**4)` | $\frac{x^{3}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x/sqrt(a + b*x**2 + c*x**4)` | $\frac{x}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{x \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**3*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{x^{3} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**5*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{x^{5} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**7*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{x^{7} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**4/sqrt(a + b*x**2 + c*x**4)` | $\frac{x^{4}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**2/sqrt(a + b*x**2 + c*x**4)` | $\frac{x^{2}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/sqrt(a + b*x**2 + c*x**4)` | $\frac{1}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{x^{2} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**4*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{x^{4} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**7/sqrt(a + b*x**2 - c*x**4)` | $\frac{x^{7}}{\sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `x**5/sqrt(a + b*x**2 - c*x**4)` | $\frac{x^{5}}{\sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `x**3/sqrt(a + b*x**2 - c*x**4)` | $\frac{x^{3}}{\sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `x/sqrt(a + b*x**2 - c*x**4)` | $\frac{x}{\sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `1/(x*sqrt(-a + b*x**2 + c*x**4))` | $\frac{1}{x \sqrt{- a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**3*sqrt(-a + b*x**2 + c*x**4))` | $\frac{1}{x^{3} \sqrt{- a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**5*sqrt(-a + b*x**2 + c*x**4))` | $\frac{1}{x^{5} \sqrt{- a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**7*sqrt(-a + b*x**2 + c*x**4))` | $\frac{1}{x^{7} \sqrt{- a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**4/sqrt(a + b*x**2 - c*x**4)` | $\frac{x^{4}}{\sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `x**2/sqrt(a + b*x**2 - c*x**4)` | $\frac{x^{2}}{\sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `1/sqrt(a + b*x**2 - c*x**4)` | $\frac{1}{\sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b*x**2 - c*x**4))` | $\frac{1}{x^{2} \sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `1/(x**4*sqrt(a + b*x**2 - c*x**4))` | $\frac{1}{x^{4} \sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `x**9/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{x^{9}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**7/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{x^{7}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{x^{5}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**3/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{x^{3}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{x}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{1}{x \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{1}{x^{3} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**5*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{1}{x^{5} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**6/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{x^{6}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**4/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{x^{4}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{x^{2}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(-3/2)` | $\frac{1}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{1}{x^{2} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**4/sqrt(b*x**2 + c*x**4)` | $\frac{x^{4}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**3/sqrt(b*x**2 + c*x**4)` | $\frac{x^{3}}{\sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `x**2/sqrt(b*x**2 + c*x**4)` | $\frac{x^{2}}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x/sqrt(b*x**2 + c*x**4)` | $\frac{x}{\sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/sqrt(b*x**2 + c*x**4)` | $\frac{1}{\sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**2*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{2} \sqrt{b x^{2} + c x^{4}}}$ |
| **SOLVED-NEW** | parametric | `1/(x**3*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{3} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**4*sqrt(b*x**2 + c*x**4))` | $\frac{1}{x^{4} \sqrt{b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**4/sqrt(a + c*x**4)` | $\frac{x^{4}}{\sqrt{a + c x^{4}}}$ |
| SOLVED-both | parametric | `x**3/sqrt(a + c*x**4)` | $\frac{x^{3}}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `x**2/sqrt(a + c*x**4)` | $\frac{x^{2}}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `x/sqrt(a + c*x**4)` | $\frac{x}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `1/sqrt(a + c*x**4)` | $\frac{1}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `1/(x*sqrt(a + c*x**4))` | $\frac{1}{x \sqrt{a + c x^{4}}}$ |
| partial | parametric | `1/(x**2*sqrt(a + c*x**4))` | $\frac{1}{x^{2} \sqrt{a + c x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**3*sqrt(a + c*x**4))` | $\frac{1}{x^{3} \sqrt{a + c x^{4}}}$ |
| partial | parametric | `1/(x**4*sqrt(a + c*x**4))` | $\frac{1}{x^{4} \sqrt{a + c x^{4}}}$ |
| partial | parametric | `x**4/sqrt(a + b*x**2)` | $\frac{x^{4}}{\sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x**3/sqrt(a + b*x**2)` | $\frac{x^{3}}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**2/sqrt(a + b*x**2)` | $\frac{x^{2}}{\sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x/sqrt(a + b*x**2)` | $\frac{x}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/sqrt(a + b*x**2)` | $\frac{1}{\sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x**2))` | $\frac{1}{x \sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `1/(x**2*sqrt(a + b*x**2))` | $\frac{1}{x^{2} \sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/(x**3*sqrt(a + b*x**2))` | $\frac{1}{x^{3} \sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `1/(x**4*sqrt(a + b*x**2))` | $\frac{1}{x^{4} \sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x**4/sqrt(c*x**4)` | $\frac{x^{4}}{\sqrt{c x^{4}}}$ |
| SOLVED-both | parametric | `x**3/sqrt(c*x**4)` | $\frac{x^{3}}{\sqrt{c x^{4}}}$ |
| SOLVED-both | parametric | `x**2/sqrt(c*x**4)` | $\frac{x^{2}}{\sqrt{c x^{4}}}$ |
| SOLVED-both | parametric | `x/sqrt(c*x**4)` | $\frac{x}{\sqrt{c x^{4}}}$ |
| SOLVED-both | parametric | `1/sqrt(c*x**4)` | $\frac{1}{\sqrt{c x^{4}}}$ |
| SOLVED-both | parametric | `1/(x*sqrt(c*x**4))` | $\frac{1}{x \sqrt{c x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**2*sqrt(c*x**4))` | $\frac{1}{x^{2} \sqrt{c x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**3*sqrt(c*x**4))` | $\frac{1}{x^{3} \sqrt{c x^{4}}}$ |
| SOLVED-both | parametric | `1/(x**4*sqrt(c*x**4))` | $\frac{1}{x^{4} \sqrt{c x^{4}}}$ |
| partial | concrete | `1/sqrt(-x**4 - 2*x**2 + 3)` | $\frac{1}{\sqrt{- x^{4} - 2 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(-x**4 + 5*x**2 - 1)` | $\frac{1}{\sqrt{- x^{4} + 5 x^{2} - 1}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b*x**2 + c*x**4)` | $x^{\frac{5}{2}} \left(a + b x^{2} + c x^{4}\right)$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b*x**2 + c*x**4)` | $x^{\frac{3}{2}} \left(a + b x^{2} + c x^{4}\right)$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b*x**2 + c*x**4)` | $\sqrt{x} \left(a + b x^{2} + c x^{4}\right)$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)/sqrt(x)` | $\frac{a + b x^{2} + c x^{4}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)/x**(3/2)` | $\frac{a + b x^{2} + c x^{4}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)/x**(5/2)` | $\frac{a + b x^{2} + c x^{4}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)/x**(7/2)` | $\frac{a + b x^{2} + c x^{4}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b*x**2 + c*x**4)**2` | $x^{\frac{5}{2}} \left(a + b x^{2} + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b*x**2 + c*x**4)**2` | $x^{\frac{3}{2}} \left(a + b x^{2} + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b*x**2 + c*x**4)**2` | $\sqrt{x} \left(a + b x^{2} + c x^{4}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)**2/sqrt(x)` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{2}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)**2/x**(3/2)` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{2}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)**2/x**(5/2)` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{2}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)**2/x**(7/2)` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{2}}{x^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x**(5/2)*(a + b*x**2 + c*x**4)**3` | $x^{\frac{5}{2}} \left(a + b x^{2} + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `x**(3/2)*(a + b*x**2 + c*x**4)**3` | $x^{\frac{3}{2}} \left(a + b x^{2} + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `sqrt(x)*(a + b*x**2 + c*x**4)**3` | $\sqrt{x} \left(a + b x^{2} + c x^{4}\right)^{3}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)**3/sqrt(x)` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{3}}{\sqrt{x}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)**3/x**(3/2)` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{3}}{x^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)**3/x**(5/2)` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{3}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)**3/x**(7/2)` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{3}}{x^{\frac{7}{2}}}$ |
| partial | parametric | `x**(9/2)/(a + b*x**2 + c*x**4)` | $\frac{x^{\frac{9}{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(7/2)/(a + b*x**2 + c*x**4)` | $\frac{x^{\frac{7}{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(5/2)/(a + b*x**2 + c*x**4)` | $\frac{x^{\frac{5}{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x**(3/2)/(a + b*x**2 + c*x**4)` | $\frac{x^{\frac{3}{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(x)/(a + b*x**2 + c*x**4)` | $\frac{\sqrt{x}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `1/(sqrt(x)*(a + b*x**2 + c*x**4))` | $\frac{1}{\sqrt{x} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `1/(x**(3/2)*(a + b*x**2 + c*x**4))` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `1/(x**(5/2)*(a + b*x**2 + c*x**4))` | $\frac{1}{x^{\frac{5}{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `1/(x**(7/2)*(a + b*x**2 + c*x**4))` | $\frac{1}{x^{\frac{7}{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| timeout | parametric | `x**(13/2)/(a + b*x**2 + c*x**4)**2` | $\frac{x^{\frac{13}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{2}}$ |
| timeout | parametric | `x**(11/2)/(a + b*x**2 + c*x**4)**2` | $\frac{x^{\frac{11}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{2}}$ |
| timeout | parametric | `x**(9/2)/(a + b*x**2 + c*x**4)**2` | $\frac{x^{\frac{9}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{2}}$ |
| timeout | parametric | `x**(7/2)/(a + b*x**2 + c*x**4)**2` | $\frac{x^{\frac{7}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{2}}$ |
| timeout | parametric | `x**(5/2)/(a + b*x**2 + c*x**4)**2` | $\frac{x^{\frac{5}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{2}}$ |
| timeout | parametric | `x**(3/2)/(a + b*x**2 + c*x**4)**2` | $\frac{x^{\frac{3}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{2}}$ |
| timeout | parametric | `sqrt(x)/(a + b*x**2 + c*x**4)**2` | $\frac{\sqrt{x}}{\left(a + b x^{2} + c x^{4}\right)^{2}}$ |
| timeout | parametric | `1/(sqrt(x)*(a + b*x**2 + c*x**4)**2)` | $\frac{1}{\sqrt{x} \left(a + b x^{2} + c x^{4}\right)^{2}}$ |
| timeout | parametric | `1/(x**(3/2)*(a + b*x**2 + c*x**4)**2)` | $\frac{1}{x^{\frac{3}{2}} \left(a + b x^{2} + c x^{4}\right)^{2}}$ |
| timeout | parametric | `x**(15/2)/(a + b*x**2 + c*x**4)**3` | $\frac{x^{\frac{15}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{3}}$ |
| timeout | parametric | `x**(13/2)/(a + b*x**2 + c*x**4)**3` | $\frac{x^{\frac{13}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{3}}$ |
| timeout | parametric | `x**(11/2)/(a + b*x**2 + c*x**4)**3` | $\frac{x^{\frac{11}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{3}}$ |
| timeout | parametric | `x**(9/2)/(a + b*x**2 + c*x**4)**3` | $\frac{x^{\frac{9}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{3}}$ |
| timeout | parametric | `x**(7/2)/(a + b*x**2 + c*x**4)**3` | $\frac{x^{\frac{7}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{3}}$ |
| timeout | parametric | `x**(5/2)/(a + b*x**2 + c*x**4)**3` | $\frac{x^{\frac{5}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{3}}$ |
| timeout | parametric | `x**(3/2)/(a + b*x**2 + c*x**4)**3` | $\frac{x^{\frac{3}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{3}}$ |
| timeout | parametric | `sqrt(x)/(a + b*x**2 + c*x**4)**3` | $\frac{\sqrt{x}}{\left(a + b x^{2} + c x^{4}\right)^{3}}$ |
| timeout | parametric | `1/(sqrt(x)*(a + b*x**2 + c*x**4)**3)` | $\frac{1}{\sqrt{x} \left(a + b x^{2} + c x^{4}\right)^{3}}$ |
| partial | parametric | `(d*x)**(3/2)*sqrt(a + b*x**2 + c*x**4)` | $\left(d x\right)^{\frac{3}{2}} \sqrt{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(d*x)*sqrt(a + b*x**2 + c*x**4)` | $\sqrt{d x} \sqrt{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/sqrt(d*x)` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{\sqrt{d x}}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/(d*x)**(3/2)` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{\left(d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d*x)**(3/2)*(a + b*x**2 + c*x**4)**(3/2)` | $\left(d x\right)^{\frac{3}{2}} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(d*x)*(a + b*x**2 + c*x**4)**(3/2)` | $\sqrt{d x} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/sqrt(d*x)` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{\sqrt{d x}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/(d*x)**(3/2)` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{\left(d x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d*x)**(3/2)/sqrt(a + b*x**2 + c*x**4)` | $\frac{\left(d x\right)^{\frac{3}{2}}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `sqrt(d*x)/sqrt(a + b*x**2 + c*x**4)` | $\frac{\sqrt{d x}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(sqrt(d*x)*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{\sqrt{d x} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/((d*x)**(3/2)*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{\left(d x\right)^{\frac{3}{2}} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(d*x)**(3/2)/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{\left(d x\right)^{\frac{3}{2}}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(d*x)/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{\sqrt{d x}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(d*x)*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{1}{\sqrt{d x} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((d*x)**(3/2)*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{1}{\left(d x\right)^{\frac{3}{2}} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(b*x**2 + 1)/sqrt(-b**2*x**4 + 1)` | $\frac{b x^{2} + 1}{\sqrt{- b^{2} x^{4} + 1}}$ |
| partial | parametric | `(-b*x**2 + 1)/sqrt(-b**2*x**4 + 1)` | $\frac{- b x^{2} + 1}{\sqrt{- b^{2} x^{4} + 1}}$ |
| partial | parametric | `(b*x**2 + 1)/sqrt(b**2*x**4 - 1)` | $\frac{b x^{2} + 1}{\sqrt{b^{2} x^{4} - 1}}$ |
| partial | parametric | `(-b*x**2 + 1)/sqrt(b**2*x**4 - 1)` | $\frac{- b x^{2} + 1}{\sqrt{b^{2} x^{4} - 1}}$ |
| partial | parametric | `(-b*x**2 + 1)/sqrt(b**2*x**4 + 1)` | $\frac{- b x^{2} + 1}{\sqrt{b^{2} x^{4} + 1}}$ |
| partial | parametric | `(b*x**2 + 1)/sqrt(b**2*x**4 + 1)` | $\frac{b x^{2} + 1}{\sqrt{b^{2} x^{4} + 1}}$ |
| partial | parametric | `(-b*x**2 + 1)/sqrt(-b**2*x**4 - 1)` | $\frac{- b x^{2} + 1}{\sqrt{- b^{2} x^{4} - 1}}$ |
| partial | parametric | `(b*x**2 + 1)/sqrt(-b**2*x**4 - 1)` | $\frac{b x^{2} + 1}{\sqrt{- b^{2} x^{4} - 1}}$ |
| partial | parametric | `sqrt(c**2*x**2 + 1)/sqrt(-c**2*x**2 + 1)` | $\frac{\sqrt{c^{2} x^{2} + 1}}{\sqrt{- c^{2} x^{2} + 1}}$ |
| partial | parametric | `(c**2*x**2 + 1)/sqrt(-c**4*x**4 + 1)` | $\frac{c^{2} x^{2} + 1}{\sqrt{- c^{4} x^{4} + 1}}$ |
| partial | parametric | `sqrt(-c**2*x**2 + 1)/sqrt(c**2*x**2 + 1)` | $\frac{\sqrt{- c^{2} x^{2} + 1}}{\sqrt{c^{2} x^{2} + 1}}$ |
| partial | parametric | `(-c**2*x**2 + 1)/sqrt(-c**4*x**4 + 1)` | $\frac{- c^{2} x^{2} + 1}{\sqrt{- c^{4} x^{4} + 1}}$ |
| partial | concrete | `(3 - x**2)/sqrt(-x**4 + x**2 + 3)` | $\frac{3 - x^{2}}{\sqrt{- x^{4} + x^{2} + 3}}$ |
| partial | concrete | `(3 - x**2)/sqrt(-x**4 + 2*x**2 + 3)` | $\frac{3 - x^{2}}{\sqrt{- x^{4} + 2 x^{2} + 3}}$ |
| partial | concrete | `(3 - x**2)/sqrt(-x**4 + 3*x**2 + 3)` | $\frac{3 - x^{2}}{\sqrt{- x^{4} + 3 x^{2} + 3}}$ |
| partial | concrete | `(3 - x**2)/sqrt(-x**4 - x**2 + 3)` | $\frac{3 - x^{2}}{\sqrt{- x^{4} - x^{2} + 3}}$ |
| partial | concrete | `(3 - x**2)/sqrt(-x**4 - 2*x**2 + 3)` | $\frac{3 - x^{2}}{\sqrt{- x^{4} - 2 x^{2} + 3}}$ |
| partial | concrete | `(3 - x**2)/sqrt(-x**4 - 3*x**2 + 3)` | $\frac{3 - x^{2}}{\sqrt{- x^{4} - 3 x^{2} + 3}}$ |
| partial | parametric | `(b + 2*c*x**2 - sqrt(-4*a*c + b**2))/sqrt(a + b*x**2 + c*x**4)` | $\frac{b + 2 c x^{2} - \sqrt{- 4 a c + b^{2}}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)**4/sqrt(a + c*x**4)` | $\frac{\left(d + e x^{2}\right)^{4}}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)**3/sqrt(a + c*x**4)` | $\frac{\left(d + e x^{2}\right)^{3}}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)**2/sqrt(a + c*x**4)` | $\frac{\left(d + e x^{2}\right)^{2}}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/sqrt(a + c*x**4)` | $\frac{d + e x^{2}}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `1/(sqrt(a + c*x**4)*(d + e*x**2))` | $\frac{1}{\sqrt{a + c x^{4}} \left(d + e x^{2}\right)}$ |
| partial | parametric | `1/(sqrt(a + c*x**4)*(d + e*x**2)**2)` | $\frac{1}{\sqrt{a + c x^{4}} \left(d + e x^{2}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(a + c*x**4)*(d + e*x**2)**3)` | $\frac{1}{\sqrt{a + c x^{4}} \left(d + e x^{2}\right)^{3}}$ |
| partial | parametric | `(d + e*x**2)**3/sqrt(a - c*x**4)` | $\frac{\left(d + e x^{2}\right)^{3}}{\sqrt{a - c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)**2/sqrt(a - c*x**4)` | $\frac{\left(d + e x^{2}\right)^{2}}{\sqrt{a - c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/sqrt(a - c*x**4)` | $\frac{d + e x^{2}}{\sqrt{a - c x^{4}}}$ |
| partial | parametric | `1/(sqrt(a - c*x**4)*(d + e*x**2))` | $\frac{1}{\sqrt{a - c x^{4}} \left(d + e x^{2}\right)}$ |
| partial | parametric | `1/(sqrt(a - c*x**4)*(d + e*x**2)**2)` | $\frac{1}{\sqrt{a - c x^{4}} \left(d + e x^{2}\right)^{2}}$ |
| partial | parametric | `1/(sqrt(a - c*x**4)*(d + e*x**2)**3)` | $\frac{1}{\sqrt{a - c x^{4}} \left(d + e x^{2}\right)^{3}}$ |
| partial | parametric | `1/(sqrt(a - c*x**4)*(d + e*x**2)**4)` | $\frac{1}{\sqrt{a - c x^{4}} \left(d + e x^{2}\right)^{4}}$ |
| partial | parametric | `(d + e*x**2)/sqrt(-a + c*x**4)` | $\frac{d + e x^{2}}{\sqrt{- a + c x^{4}}}$ |
| partial | parametric | `1/(sqrt(-a + c*x**4)*(d + e*x**2))` | $\frac{1}{\sqrt{- a + c x^{4}} \left(d + e x^{2}\right)}$ |
| partial | parametric | `(sqrt(a) + sqrt(c)*x**2)/sqrt(-a + c*x**4)` | $\frac{\sqrt{a} + \sqrt{c} x^{2}}{\sqrt{- a + c x^{4}}}$ |
| partial | parametric | `(x**2*sqrt(c/a) + 1)/sqrt(-a + c*x**4)` | $\frac{x^{2} \sqrt{\frac{c}{a}} + 1}{\sqrt{- a + c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/sqrt(-a - c*x**4)` | $\frac{d + e x^{2}}{\sqrt{- a - c x^{4}}}$ |
| partial | parametric | `1/(sqrt(-a - c*x**4)*(d + e*x**2))` | $\frac{1}{\sqrt{- a - c x^{4}} \left(d + e x^{2}\right)}$ |
| partial | parametric | `1/(sqrt(4 - 5*x**4)*(a + b*x**2))` | $\frac{1}{\sqrt{4 - 5 x^{4}} \left(a + b x^{2}\right)}$ |
| partial | parametric | `1/((a + b*x**2)*sqrt(5*x**4 + 4))` | $\frac{1}{\left(a + b x^{2}\right) \sqrt{5 x^{4} + 4}}$ |
| partial | parametric | `1/((a + b*x**2)*sqrt(-d*x**4 + 4))` | $\frac{1}{\left(a + b x^{2}\right) \sqrt{- d x^{4} + 4}}$ |
| partial | parametric | `1/((a + b*x**2)*sqrt(d*x**4 + 4))` | $\frac{1}{\left(a + b x^{2}\right) \sqrt{d x^{4} + 4}}$ |
| partial | parametric | `sqrt(a + b*x**2)/sqrt(1 - x**4)` | $\frac{\sqrt{a + b x^{2}}}{\sqrt{1 - x^{4}}}$ |
| partial | parametric | `(d + e*x**2)**(3/2)/(d**2 - e**2*x**4)` | $\frac{\left(d + e x^{2}\right)^{\frac{3}{2}}}{d^{2} - e^{2} x^{4}}$ |
| partial | parametric | `sqrt(d + e*x**2)/(d**2 - e**2*x**4)` | $\frac{\sqrt{d + e x^{2}}}{d^{2} - e^{2} x^{4}}$ |
| partial | parametric | `1/(sqrt(d + e*x**2)*(d**2 - e**2*x**4))` | $\frac{1}{\sqrt{d + e x^{2}} \left(d^{2} - e^{2} x^{4}\right)}$ |
| partial | parametric | `1/((d + e*x**2)**(3/2)*(d**2 - e**2*x**4))` | $\frac{1}{\left(d + e x^{2}\right)^{\frac{3}{2}} \left(d^{2} - e^{2} x^{4}\right)}$ |
| partial | parametric | `(a + b*x**2)**(5/2)/sqrt(a**2 - b**2*x**4)` | $\frac{\left(a + b x^{2}\right)^{\frac{5}{2}}}{\sqrt{a^{2} - b^{2} x^{4}}}$ |
| partial | parametric | `(a + b*x**2)**(3/2)/sqrt(a**2 - b**2*x**4)` | $\frac{\left(a + b x^{2}\right)^{\frac{3}{2}}}{\sqrt{a^{2} - b^{2} x^{4}}}$ |
| partial | parametric | `sqrt(a + b*x**2)/sqrt(a**2 - b**2*x**4)` | $\frac{\sqrt{a + b x^{2}}}{\sqrt{a^{2} - b^{2} x^{4}}}$ |
| partial | parametric | `1/(sqrt(a + b*x**2)*sqrt(a**2 - b**2*x**4))` | $\frac{1}{\sqrt{a + b x^{2}} \sqrt{a^{2} - b^{2} x^{4}}}$ |
| partial | parametric | `1/((a + b*x**2)**(3/2)*sqrt(a**2 - b**2*x**4))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{3}{2}} \sqrt{a^{2} - b^{2} x^{4}}}$ |
| partial | parametric | `1/((a + b*x**2)**(5/2)*sqrt(a**2 - b**2*x**4))` | $\frac{1}{\left(a + b x^{2}\right)^{\frac{5}{2}} \sqrt{a^{2} - b^{2} x^{4}}}$ |
| partial | parametric | `(a - b*x**2)**(5/2)/sqrt(a**2 - b**2*x**4)` | $\frac{\left(a - b x^{2}\right)^{\frac{5}{2}}}{\sqrt{a^{2} - b^{2} x^{4}}}$ |
| partial | parametric | `(a - b*x**2)**(3/2)/sqrt(a**2 - b**2*x**4)` | $\frac{\left(a - b x^{2}\right)^{\frac{3}{2}}}{\sqrt{a^{2} - b^{2} x^{4}}}$ |
| partial | parametric | `sqrt(a - b*x**2)/sqrt(a**2 - b**2*x**4)` | $\frac{\sqrt{a - b x^{2}}}{\sqrt{a^{2} - b^{2} x^{4}}}$ |
| partial | parametric | `1/(sqrt(a - b*x**2)*sqrt(a**2 - b**2*x**4))` | $\frac{1}{\sqrt{a - b x^{2}} \sqrt{a^{2} - b^{2} x^{4}}}$ |
| partial | parametric | `1/((a - b*x**2)**(3/2)*sqrt(a**2 - b**2*x**4))` | $\frac{1}{\left(a - b x^{2}\right)^{\frac{3}{2}} \sqrt{a^{2} - b^{2} x^{4}}}$ |
| partial | parametric | `1/((a - b*x**2)**(5/2)*sqrt(a**2 - b**2*x**4))` | $\frac{1}{\left(a - b x^{2}\right)^{\frac{5}{2}} \sqrt{a^{2} - b^{2} x^{4}}}$ |
| partial | concrete | `sqrt(x**2 - 1)/sqrt(x**4 - 1)` | $\frac{\sqrt{x^{2} - 1}}{\sqrt{x^{4} - 1}}$ |
| partial | parametric | `(d + e*x**2)**(5/2)/(b*d*e + b*e**2*x**2 - c*d**2 + c*e**2*x**4)` | $\frac{\left(d + e x^{2}\right)^{\frac{5}{2}}}{b d e + b e^{2} x^{2} - c d^{2} + c e^{2} x^{4}}$ |
| partial | parametric | `(d + e*x**2)**(3/2)/(b*d*e + b*e**2*x**2 - c*d**2 + c*e**2*x**4)` | $\frac{\left(d + e x^{2}\right)^{\frac{3}{2}}}{b d e + b e^{2} x^{2} - c d^{2} + c e^{2} x^{4}}$ |
| partial | parametric | `sqrt(d + e*x**2)/(b*d*e + b*e**2*x**2 - c*d**2 + c*e**2*x**4)` | $\frac{\sqrt{d + e x^{2}}}{b d e + b e^{2} x^{2} - c d^{2} + c e^{2} x^{4}}$ |
| partial | parametric | `1/(sqrt(d + e*x**2)*(b*d*e + b*e**2*x**2 - c*d**2 + c*e**2*x**4))` | $\frac{1}{\sqrt{d + e x^{2}} \left(b d e + b e^{2} x^{2} - c d^{2} + c e^{2} x^{4}\right)}$ |
| partial | parametric | `1/((d + e*x**2)**(3/2)*(b*d*e + b*e**2*x**2 - c*d**2 + c*e**2*x**4))` | $\frac{1}{\left(d + e x^{2}\right)^{\frac{3}{2}} \left(b d e + b e^{2} x^{2} - c d^{2} + c e^{2} x^{4}\right)}$ |
| partial | concrete | `(x**2 + 1)**3*sqrt(x**4 + x**2 + 1)` | $\left(x^{2} + 1\right)^{3} \sqrt{x^{4} + x^{2} + 1}$ |
| partial | concrete | `(x**2 + 1)**2*sqrt(x**4 + x**2 + 1)` | $\left(x^{2} + 1\right)^{2} \sqrt{x^{4} + x^{2} + 1}$ |
| partial | concrete | `(x**2 + 1)*sqrt(x**4 + x**2 + 1)` | $\left(x^{2} + 1\right) \sqrt{x^{4} + x^{2} + 1}$ |
| partial | concrete | `sqrt(x**4 + x**2 + 1)/(x**2 + 1)` | $\frac{\sqrt{x^{4} + x^{2} + 1}}{x^{2} + 1}$ |
| partial | concrete | `sqrt(x**4 + x**2 + 1)/(x**2 + 1)**2` | $\frac{\sqrt{x^{4} + x^{2} + 1}}{\left(x^{2} + 1\right)^{2}}$ |
| partial | concrete | `sqrt(x**4 + x**2 + 1)/(x**2 + 1)**3` | $\frac{\sqrt{x^{4} + x^{2} + 1}}{\left(x^{2} + 1\right)^{3}}$ |
| partial | concrete | `sqrt(x**4 + x**2 + 1)/(x**2 + 1)**4` | $\frac{\sqrt{x^{4} + x^{2} + 1}}{\left(x^{2} + 1\right)^{4}}$ |
| partial | concrete | `(x**2 + 1)**3/sqrt(x**4 + x**2 + 1)` | $\frac{\left(x^{2} + 1\right)^{3}}{\sqrt{x^{4} + x^{2} + 1}}$ |
| partial | concrete | `(x**2 + 1)**2/sqrt(x**4 + x**2 + 1)` | $\frac{\left(x^{2} + 1\right)^{2}}{\sqrt{x^{4} + x^{2} + 1}}$ |
| partial | concrete | `(x**2 + 1)/sqrt(x**4 + x**2 + 1)` | $\frac{x^{2} + 1}{\sqrt{x^{4} + x^{2} + 1}}$ |
| partial | concrete | `1/((x**2 + 1)*sqrt(x**4 + x**2 + 1))` | $\frac{1}{\left(x^{2} + 1\right) \sqrt{x^{4} + x^{2} + 1}}$ |
| partial | concrete | `1/((x**2 + 1)**2*sqrt(x**4 + x**2 + 1))` | $\frac{1}{\left(x^{2} + 1\right)^{2} \sqrt{x^{4} + x^{2} + 1}}$ |
| partial | concrete | `1/((x**2 + 1)**3*sqrt(x**4 + x**2 + 1))` | $\frac{1}{\left(x^{2} + 1\right)^{3} \sqrt{x^{4} + x^{2} + 1}}$ |
| partial | concrete | `(x**2 + 1)**3/(x**4 + x**2 + 1)**(3/2)` | $\frac{\left(x^{2} + 1\right)^{3}}{\left(x^{4} + x^{2} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x**2 + 1)**2/(x**4 + x**2 + 1)**(3/2)` | $\frac{\left(x^{2} + 1\right)^{2}}{\left(x^{4} + x^{2} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x**2 + 1)/(x**4 + x**2 + 1)**(3/2)` | $\frac{x^{2} + 1}{\left(x^{4} + x^{2} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((x**2 + 1)*(x**4 + x**2 + 1)**(3/2))` | $\frac{1}{\left(x^{2} + 1\right) \left(x^{4} + x^{2} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((x**2 + 1)**2*(x**4 + x**2 + 1)**(3/2))` | $\frac{1}{\left(x^{2} + 1\right)^{2} \left(x^{4} + x^{2} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((x**2 + 1)**3*(x**4 + x**2 + 1)**(3/2))` | $\frac{1}{\left(x^{2} + 1\right)^{3} \left(x^{4} + x^{2} + 1\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x**2)**(5/2)*(a + b*x**2 + c*x**4)` | $\left(d + e x^{2}\right)^{\frac{5}{2}} \left(a + b x^{2} + c x^{4}\right)$ |
| partial | parametric | `(d + e*x**2)**(3/2)*(a + b*x**2 + c*x**4)` | $\left(d + e x^{2}\right)^{\frac{3}{2}} \left(a + b x^{2} + c x^{4}\right)$ |
| partial | parametric | `sqrt(d + e*x**2)*(a + b*x**2 + c*x**4)` | $\sqrt{d + e x^{2}} \left(a + b x^{2} + c x^{4}\right)$ |
| partial | parametric | `(a + b*x**2 + c*x**4)/sqrt(d + e*x**2)` | $\frac{a + b x^{2} + c x^{4}}{\sqrt{d + e x^{2}}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)/(d + e*x**2)**(3/2)` | $\frac{a + b x^{2} + c x^{4}}{\left(d + e x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)/(d + e*x**2)**(5/2)` | $\frac{a + b x^{2} + c x^{4}}{\left(d + e x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)/(d + e*x**2)**(7/2)` | $\frac{a + b x^{2} + c x^{4}}{\left(d + e x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)/(d + e*x**2)**(9/2)` | $\frac{a + b x^{2} + c x^{4}}{\left(d + e x^{2}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)/(d + e*x**2)**(11/2)` | $\frac{a + b x^{2} + c x^{4}}{\left(d + e x^{2}\right)^{\frac{11}{2}}}$ |
| SOLVED-both | parametric | `(a + b*x**2 + c*x**4)/(d + e*x**2)**(13/2)` | $\frac{a + b x^{2} + c x^{4}}{\left(d + e x^{2}\right)^{\frac{13}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)**3*sqrt(x**4 + 3*x**2 + 2)` | $\left(5 x^{2} + 7\right)^{3} \sqrt{x^{4} + 3 x^{2} + 2}$ |
| partial | concrete | `(5*x**2 + 7)**2*sqrt(x**4 + 3*x**2 + 2)` | $\left(5 x^{2} + 7\right)^{2} \sqrt{x^{4} + 3 x^{2} + 2}$ |
| partial | concrete | `(5*x**2 + 7)*sqrt(x**4 + 3*x**2 + 2)` | $\left(5 x^{2} + 7\right) \sqrt{x^{4} + 3 x^{2} + 2}$ |
| partial | concrete | `sqrt(x**4 + 3*x**2 + 2)` | $\sqrt{x^{4} + 3 x^{2} + 2}$ |
| partial | concrete | `sqrt(x**4 + 3*x**2 + 2)/(5*x**2 + 7)**2` | $\frac{\sqrt{x^{4} + 3 x^{2} + 2}}{\left(5 x^{2} + 7\right)^{2}}$ |
| partial | concrete | `sqrt(x**4 + 3*x**2 + 2)/(5*x**2 + 7)**3` | $\frac{\sqrt{x^{4} + 3 x^{2} + 2}}{\left(5 x^{2} + 7\right)^{3}}$ |
| partial | concrete | `(5*x**2 + 7)**3*(x**4 + 3*x**2 + 2)**(3/2)` | $\left(5 x^{2} + 7\right)^{3} \left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5*x**2 + 7)**2*(x**4 + 3*x**2 + 2)**(3/2)` | $\left(5 x^{2} + 7\right)^{2} \left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5*x**2 + 7)*(x**4 + 3*x**2 + 2)**(3/2)` | $\left(5 x^{2} + 7\right) \left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(x**4 + 3*x**2 + 2)**(3/2)` | $\left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(x**4 + 3*x**2 + 2)**(3/2)/(5*x**2 + 7)` | $\frac{\left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}}{5 x^{2} + 7}$ |
| partial | concrete | `(5*x**2 + 7)**3/sqrt(x**4 + 3*x**2 + 2)` | $\frac{\left(5 x^{2} + 7\right)^{3}}{\sqrt{x^{4} + 3 x^{2} + 2}}$ |
| partial | concrete | `(5*x**2 + 7)**2/sqrt(x**4 + 3*x**2 + 2)` | $\frac{\left(5 x^{2} + 7\right)^{2}}{\sqrt{x^{4} + 3 x^{2} + 2}}$ |
| partial | concrete | `(5*x**2 + 7)/sqrt(x**4 + 3*x**2 + 2)` | $\frac{5 x^{2} + 7}{\sqrt{x^{4} + 3 x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(x**4 + 3*x**2 + 2)` | $\frac{1}{\sqrt{x^{4} + 3 x^{2} + 2}}$ |
| partial | concrete | `1/((5*x**2 + 7)*sqrt(x**4 + 3*x**2 + 2))` | $\frac{1}{\left(5 x^{2} + 7\right) \sqrt{x^{4} + 3 x^{2} + 2}}$ |
| partial | concrete | `1/((5*x**2 + 7)**2*sqrt(x**4 + 3*x**2 + 2))` | $\frac{1}{\left(5 x^{2} + 7\right)^{2} \sqrt{x^{4} + 3 x^{2} + 2}}$ |
| partial | concrete | `1/((5*x**2 + 7)**3*sqrt(x**4 + 3*x**2 + 2))` | $\frac{1}{\left(5 x^{2} + 7\right)^{3} \sqrt{x^{4} + 3 x^{2} + 2}}$ |
| partial | concrete | `(5*x**2 + 7)**5/(x**4 + 3*x**2 + 2)**(3/2)` | $\frac{\left(5 x^{2} + 7\right)^{5}}{\left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)**4/(x**4 + 3*x**2 + 2)**(3/2)` | $\frac{\left(5 x^{2} + 7\right)^{4}}{\left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)**3/(x**4 + 3*x**2 + 2)**(3/2)` | $\frac{\left(5 x^{2} + 7\right)^{3}}{\left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)**2/(x**4 + 3*x**2 + 2)**(3/2)` | $\frac{\left(5 x^{2} + 7\right)^{2}}{\left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)/(x**4 + 3*x**2 + 2)**(3/2)` | $\frac{5 x^{2} + 7}{\left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x**4 + 3*x**2 + 2)**(-3/2)` | $\frac{1}{\left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((5*x**2 + 7)**2*(x**4 + 3*x**2 + 2)**(3/2))` | $\frac{1}{\left(5 x^{2} + 7\right)^{2} \left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((5*x**2 + 7)**3*(x**4 + 3*x**2 + 2)**(3/2))` | $\frac{1}{\left(5 x^{2} + 7\right)^{3} \left(x^{4} + 3 x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)**4*sqrt(-x**4 + x**2 + 2)` | $\left(5 x^{2} + 7\right)^{4} \sqrt{- x^{4} + x^{2} + 2}$ |
| partial | concrete | `(5*x**2 + 7)**3*sqrt(-x**4 + x**2 + 2)` | $\left(5 x^{2} + 7\right)^{3} \sqrt{- x^{4} + x^{2} + 2}$ |
| partial | concrete | `(5*x**2 + 7)**2*sqrt(-x**4 + x**2 + 2)` | $\left(5 x^{2} + 7\right)^{2} \sqrt{- x^{4} + x^{2} + 2}$ |
| partial | concrete | `(5*x**2 + 7)*sqrt(-x**4 + x**2 + 2)` | $\left(5 x^{2} + 7\right) \sqrt{- x^{4} + x^{2} + 2}$ |
| partial | concrete | `sqrt(-x**4 + x**2 + 2)` | $\sqrt{- x^{4} + x^{2} + 2}$ |
| partial | concrete | `sqrt(-x**4 + x**2 + 2)/(5*x**2 + 7)` | $\frac{\sqrt{- x^{4} + x^{2} + 2}}{5 x^{2} + 7}$ |
| partial | concrete | `sqrt(-x**4 + x**2 + 2)/(5*x**2 + 7)**2` | $\frac{\sqrt{- x^{4} + x^{2} + 2}}{\left(5 x^{2} + 7\right)^{2}}$ |
| partial | concrete | `sqrt(-x**4 + x**2 + 2)/(5*x**2 + 7)**3` | $\frac{\sqrt{- x^{4} + x^{2} + 2}}{\left(5 x^{2} + 7\right)^{3}}$ |
| partial | concrete | `(5*x**2 + 7)**4*(-x**4 + x**2 + 2)**(3/2)` | $\left(5 x^{2} + 7\right)^{4} \left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5*x**2 + 7)**3*(-x**4 + x**2 + 2)**(3/2)` | $\left(5 x^{2} + 7\right)^{3} \left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5*x**2 + 7)**2*(-x**4 + x**2 + 2)**(3/2)` | $\left(5 x^{2} + 7\right)^{2} \left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5*x**2 + 7)*(-x**4 + x**2 + 2)**(3/2)` | $\left(5 x^{2} + 7\right) \left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(-x**4 + x**2 + 2)**(3/2)` | $\left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}$ |
| partial | concrete | `(-x**4 + x**2 + 2)**(3/2)/(5*x**2 + 7)` | $\frac{\left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}}{5 x^{2} + 7}$ |
| partial | concrete | `(-x**4 + x**2 + 2)**(3/2)/(5*x**2 + 7)**2` | $\frac{\left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}}{\left(5 x^{2} + 7\right)^{2}}$ |
| partial | concrete | `(-x**4 + x**2 + 2)**(3/2)/(5*x**2 + 7)**3` | $\frac{\left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}}{\left(5 x^{2} + 7\right)^{3}}$ |
| partial | concrete | `(5*x**2 + 7)**3/sqrt(-x**4 + x**2 + 2)` | $\frac{\left(5 x^{2} + 7\right)^{3}}{\sqrt{- x^{4} + x^{2} + 2}}$ |
| partial | concrete | `(5*x**2 + 7)**2/sqrt(-x**4 + x**2 + 2)` | $\frac{\left(5 x^{2} + 7\right)^{2}}{\sqrt{- x^{4} + x^{2} + 2}}$ |
| partial | concrete | `(5*x**2 + 7)/sqrt(-x**4 + x**2 + 2)` | $\frac{5 x^{2} + 7}{\sqrt{- x^{4} + x^{2} + 2}}$ |
| partial | concrete | `1/sqrt(-x**4 + x**2 + 2)` | $\frac{1}{\sqrt{- x^{4} + x^{2} + 2}}$ |
| partial | concrete | `1/((5*x**2 + 7)*sqrt(-x**4 + x**2 + 2))` | $\frac{1}{\left(5 x^{2} + 7\right) \sqrt{- x^{4} + x^{2} + 2}}$ |
| partial | concrete | `1/((5*x**2 + 7)**2*sqrt(-x**4 + x**2 + 2))` | $\frac{1}{\left(5 x^{2} + 7\right)^{2} \sqrt{- x^{4} + x^{2} + 2}}$ |
| partial | concrete | `1/((5*x**2 + 7)**3*sqrt(-x**4 + x**2 + 2))` | $\frac{1}{\left(5 x^{2} + 7\right)^{3} \sqrt{- x^{4} + x^{2} + 2}}$ |
| partial | concrete | `(5*x**2 + 7)**5/(-x**4 + x**2 + 2)**(3/2)` | $\frac{\left(5 x^{2} + 7\right)^{5}}{\left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)**4/(-x**4 + x**2 + 2)**(3/2)` | $\frac{\left(5 x^{2} + 7\right)^{4}}{\left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)**3/(-x**4 + x**2 + 2)**(3/2)` | $\frac{\left(5 x^{2} + 7\right)^{3}}{\left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)**2/(-x**4 + x**2 + 2)**(3/2)` | $\frac{\left(5 x^{2} + 7\right)^{2}}{\left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)/(-x**4 + x**2 + 2)**(3/2)` | $\frac{5 x^{2} + 7}{\left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(-x**4 + x**2 + 2)**(-3/2)` | $\frac{1}{\left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((5*x**2 + 7)*(-x**4 + x**2 + 2)**(3/2))` | $\frac{1}{\left(5 x^{2} + 7\right) \left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((5*x**2 + 7)**2*(-x**4 + x**2 + 2)**(3/2))` | $\frac{1}{\left(5 x^{2} + 7\right)^{2} \left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((5*x**2 + 7)**3*(-x**4 + x**2 + 2)**(3/2))` | $\frac{1}{\left(5 x^{2} + 7\right)^{3} \left(- x^{4} + x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)**4*sqrt(x**4 + 3*x**2 + 4)` | $\left(5 x^{2} + 7\right)^{4} \sqrt{x^{4} + 3 x^{2} + 4}$ |
| partial | concrete | `(5*x**2 + 7)**3*sqrt(x**4 + 3*x**2 + 4)` | $\left(5 x^{2} + 7\right)^{3} \sqrt{x^{4} + 3 x^{2} + 4}$ |
| partial | concrete | `(5*x**2 + 7)**2*sqrt(x**4 + 3*x**2 + 4)` | $\left(5 x^{2} + 7\right)^{2} \sqrt{x^{4} + 3 x^{2} + 4}$ |
| partial | concrete | `(5*x**2 + 7)*sqrt(x**4 + 3*x**2 + 4)` | $\left(5 x^{2} + 7\right) \sqrt{x^{4} + 3 x^{2} + 4}$ |
| partial | concrete | `sqrt(x**4 + 3*x**2 + 4)` | $\sqrt{x^{4} + 3 x^{2} + 4}$ |
| partial | concrete | `sqrt(x**4 + 3*x**2 + 4)/(5*x**2 + 7)` | $\frac{\sqrt{x^{4} + 3 x^{2} + 4}}{5 x^{2} + 7}$ |
| partial | concrete | `sqrt(x**4 + 3*x**2 + 4)/(5*x**2 + 7)**2` | $\frac{\sqrt{x^{4} + 3 x^{2} + 4}}{\left(5 x^{2} + 7\right)^{2}}$ |
| partial | concrete | `sqrt(x**4 + 3*x**2 + 4)/(5*x**2 + 7)**3` | $\frac{\sqrt{x^{4} + 3 x^{2} + 4}}{\left(5 x^{2} + 7\right)^{3}}$ |
| partial | concrete | `(5*x**2 + 7)**4*(x**4 + 3*x**2 + 4)**(3/2)` | $\left(5 x^{2} + 7\right)^{4} \left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5*x**2 + 7)**3*(x**4 + 3*x**2 + 4)**(3/2)` | $\left(5 x^{2} + 7\right)^{3} \left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5*x**2 + 7)**2*(x**4 + 3*x**2 + 4)**(3/2)` | $\left(5 x^{2} + 7\right)^{2} \left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}$ |
| partial | concrete | `(5*x**2 + 7)*(x**4 + 3*x**2 + 4)**(3/2)` | $\left(5 x^{2} + 7\right) \left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}$ |
| partial | concrete | `(x**4 + 3*x**2 + 4)**(3/2)` | $\left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}$ |
| partial | concrete | `(x**4 + 3*x**2 + 4)**(3/2)/(5*x**2 + 7)` | $\frac{\left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}}{5 x^{2} + 7}$ |
| partial | concrete | `(x**4 + 3*x**2 + 4)**(3/2)/(5*x**2 + 7)**3` | $\frac{\left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}}{\left(5 x^{2} + 7\right)^{3}}$ |
| partial | concrete | `(5*x**2 + 7)**3/sqrt(x**4 + 3*x**2 + 4)` | $\frac{\left(5 x^{2} + 7\right)^{3}}{\sqrt{x^{4} + 3 x^{2} + 4}}$ |
| partial | concrete | `(5*x**2 + 7)**2/sqrt(x**4 + 3*x**2 + 4)` | $\frac{\left(5 x^{2} + 7\right)^{2}}{\sqrt{x^{4} + 3 x^{2} + 4}}$ |
| partial | concrete | `(5*x**2 + 7)/sqrt(x**4 + 3*x**2 + 4)` | $\frac{5 x^{2} + 7}{\sqrt{x^{4} + 3 x^{2} + 4}}$ |
| partial | concrete | `1/sqrt(x**4 + 3*x**2 + 4)` | $\frac{1}{\sqrt{x^{4} + 3 x^{2} + 4}}$ |
| partial | concrete | `1/((5*x**2 + 7)*sqrt(x**4 + 3*x**2 + 4))` | $\frac{1}{\left(5 x^{2} + 7\right) \sqrt{x^{4} + 3 x^{2} + 4}}$ |
| partial | concrete | `1/((5*x**2 + 7)**2*sqrt(x**4 + 3*x**2 + 4))` | $\frac{1}{\left(5 x^{2} + 7\right)^{2} \sqrt{x^{4} + 3 x^{2} + 4}}$ |
| partial | concrete | `1/((5*x**2 + 7)**3*sqrt(x**4 + 3*x**2 + 4))` | $\frac{1}{\left(5 x^{2} + 7\right)^{3} \sqrt{x^{4} + 3 x^{2} + 4}}$ |
| partial | concrete | `(5*x**2 + 7)**5/(x**4 + 3*x**2 + 4)**(3/2)` | $\frac{\left(5 x^{2} + 7\right)^{5}}{\left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)**4/(x**4 + 3*x**2 + 4)**(3/2)` | $\frac{\left(5 x^{2} + 7\right)^{4}}{\left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)**3/(x**4 + 3*x**2 + 4)**(3/2)` | $\frac{\left(5 x^{2} + 7\right)^{3}}{\left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)**2/(x**4 + 3*x**2 + 4)**(3/2)` | $\frac{\left(5 x^{2} + 7\right)^{2}}{\left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(5*x**2 + 7)/(x**4 + 3*x**2 + 4)**(3/2)` | $\frac{5 x^{2} + 7}{\left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x**4 + 3*x**2 + 4)**(-3/2)` | $\frac{1}{\left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((5*x**2 + 7)*(x**4 + 3*x**2 + 4)**(3/2))` | $\frac{1}{\left(5 x^{2} + 7\right) \left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((5*x**2 + 7)**2*(x**4 + 3*x**2 + 4)**(3/2))` | $\frac{1}{\left(5 x^{2} + 7\right)^{2} \left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((5*x**2 + 7)**3*(x**4 + 3*x**2 + 4)**(3/2))` | $\frac{1}{\left(5 x^{2} + 7\right)^{3} \left(x^{4} + 3 x^{2} + 4\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x**2)**3/sqrt(a + b*x**2 + c*x**4)` | $\frac{\left(d + e x^{2}\right)^{3}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)**2/sqrt(a + b*x**2 + c*x**4)` | $\frac{\left(d + e x^{2}\right)^{2}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/sqrt(a + b*x**2 + c*x**4)` | $\frac{d + e x^{2}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/((d + e*x**2)*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{\left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/((d + e*x**2)**2*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{\left(d + e x^{2}\right)^{2} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)**3/sqrt(a + b*x**2 - c*x**4)` | $\frac{\left(d + e x^{2}\right)^{3}}{\sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)**2/sqrt(a + b*x**2 - c*x**4)` | $\frac{\left(d + e x^{2}\right)^{2}}{\sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/sqrt(a + b*x**2 - c*x**4)` | $\frac{d + e x^{2}}{\sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `1/((d + e*x**2)*sqrt(a + b*x**2 - c*x**4))` | $\frac{1}{\left(d + e x^{2}\right) \sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `1/((d + e*x**2)**2*sqrt(a + b*x**2 - c*x**4))` | $\frac{1}{\left(d + e x^{2}\right)^{2} \sqrt{a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/sqrt(-a + b*x**2 + c*x**4)` | $\frac{d + e x^{2}}{\sqrt{- a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/((d + e*x**2)*sqrt(-a + b*x**2 + c*x**4))` | $\frac{1}{\left(d + e x^{2}\right) \sqrt{- a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/sqrt(-a + b*x**2 - c*x**4)` | $\frac{d + e x^{2}}{\sqrt{- a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `1/((d + e*x**2)*sqrt(-a + b*x**2 - c*x**4))` | $\frac{1}{\left(d + e x^{2}\right) \sqrt{- a + b x^{2} - c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)**3/sqrt(x**4 + 3*x**2 + 2)` | $\frac{\left(d + e x^{2}\right)^{3}}{\sqrt{x^{4} + 3 x^{2} + 2}}$ |
| partial | parametric | `(d + e*x**2)**2/sqrt(x**4 + 3*x**2 + 2)` | $\frac{\left(d + e x^{2}\right)^{2}}{\sqrt{x^{4} + 3 x^{2} + 2}}$ |
| partial | parametric | `(d + e*x**2)/sqrt(x**4 + 3*x**2 + 2)` | $\frac{d + e x^{2}}{\sqrt{x^{4} + 3 x^{2} + 2}}$ |
| partial | parametric | `(f + g*x)/(sqrt(a + c*x**4)*(d + e*x))` | $\frac{f + g x}{\sqrt{a + c x^{4}} \left(d + e x\right)}$ |
| partial | parametric | `(f + g*x)/(sqrt(-a + c*x**4)*(d + e*x))` | $\frac{f + g x}{\sqrt{- a + c x^{4}} \left(d + e x\right)}$ |
| partial | concrete | `(x - sqrt(3) + 1)/((x + 1 + sqrt(3))*sqrt(x**4 + 4*sqrt(3)*x**2 - 4))` | $\frac{x - \sqrt{3} + 1}{\left(x + 1 + \sqrt{3}\right) \sqrt{x^{4} + 4 \sqrt{3} x^{2} - 4}}$ |
| partial | concrete | `(x + 1 + sqrt(3))/((x - sqrt(3) + 1)*sqrt(x**4 - 4*sqrt(3)*x**2 - 4))` | $\frac{x + 1 + \sqrt{3}}{\left(x - \sqrt{3} + 1\right) \sqrt{x^{4} - 4 \sqrt{3} x^{2} - 4}}$ |
| partial | concrete | `(2*x - sqrt(3) + 1)/((2*x + 1 + sqrt(3))*sqrt(4*x**4 + 4*sqrt(3)*x**2 - 1))` | $\frac{2 x - \sqrt{3} + 1}{\left(2 x + 1 + \sqrt{3}\right) \sqrt{4 x^{4} + 4 \sqrt{3} x^{2} - 1}}$ |
| partial | concrete | `(2*x + 1 + sqrt(3))/((2*x - sqrt(3) + 1)*sqrt(4*x**4 - 4*sqrt(3)*x**2 - 1))` | $\frac{2 x + 1 + \sqrt{3}}{\left(2 x - \sqrt{3} + 1\right) \sqrt{4 x^{4} - 4 \sqrt{3} x^{2} - 1}}$ |
| partial | parametric | `(f + g*x)/((d + e*x)*sqrt(a + b*x**2 + c*x**4))` | $\frac{f + g x}{\left(d + e x\right) \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(f + g*x)/((d + e*x)*sqrt(-a + b*x**2 + c*x**4))` | $\frac{f + g x}{\left(d + e x\right) \sqrt{- a + b x^{2} + c x^{4}}}$ |
| partial | concrete | `x**5*(3*x**2 + 2)*sqrt(x**4 + 5)` | $x^{5} \left(3 x^{2} + 2\right) \sqrt{x^{4} + 5}$ |
| partial | concrete | `x**3*(3*x**2 + 2)*sqrt(x**4 + 5)` | $x^{3} \left(3 x^{2} + 2\right) \sqrt{x^{4} + 5}$ |
| partial | concrete | `x*(3*x**2 + 2)*sqrt(x**4 + 5)` | $x \left(3 x^{2} + 2\right) \sqrt{x^{4} + 5}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5)/x` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5}}{x}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5)/x**3` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5}}{x^{3}}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5)/x**5` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5}}{x^{5}}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5)/x**7` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5}}{x^{7}}$ |
| partial | concrete | `x**4*(3*x**2 + 2)*sqrt(x**4 + 5)` | $x^{4} \left(3 x^{2} + 2\right) \sqrt{x^{4} + 5}$ |
| partial | concrete | `x**2*(3*x**2 + 2)*sqrt(x**4 + 5)` | $x^{2} \left(3 x^{2} + 2\right) \sqrt{x^{4} + 5}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5)` | $\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5)/x**2` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5}}{x^{2}}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5)/x**4` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5}}{x^{4}}$ |
| partial | concrete | `x**5*(3*x**2 + 2)*(x**4 + 5)**(3/2)` | $x^{5} \left(3 x^{2} + 2\right) \left(x^{4} + 5\right)^{\frac{3}{2}}$ |
| partial | concrete | `x**3*(3*x**2 + 2)*(x**4 + 5)**(3/2)` | $x^{3} \left(3 x^{2} + 2\right) \left(x^{4} + 5\right)^{\frac{3}{2}}$ |
| partial | concrete | `x*(3*x**2 + 2)*(x**4 + 5)**(3/2)` | $x \left(3 x^{2} + 2\right) \left(x^{4} + 5\right)^{\frac{3}{2}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5)**(3/2)/x` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5\right)^{\frac{3}{2}}}{x}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5)**(3/2)/x**3` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5)**(3/2)/x**5` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5)**(3/2)/x**7` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | concrete | `x**4*(3*x**2 + 2)*(x**4 + 5)**(3/2)` | $x^{4} \left(3 x^{2} + 2\right) \left(x^{4} + 5\right)^{\frac{3}{2}}$ |
| partial | concrete | `x**2*(3*x**2 + 2)*(x**4 + 5)**(3/2)` | $x^{2} \left(3 x^{2} + 2\right) \left(x^{4} + 5\right)^{\frac{3}{2}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5)**(3/2)` | $\left(3 x^{2} + 2\right) \left(x^{4} + 5\right)^{\frac{3}{2}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5)**(3/2)/x**2` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5)**(3/2)/x**4` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | concrete | `x**7*(3*x**2 + 2)/sqrt(x**4 + 5)` | $\frac{x^{7} \left(3 x^{2} + 2\right)}{\sqrt{x^{4} + 5}}$ |
| partial | concrete | `x**5*(3*x**2 + 2)/sqrt(x**4 + 5)` | $\frac{x^{5} \left(3 x^{2} + 2\right)}{\sqrt{x^{4} + 5}}$ |
| partial | concrete | `x**3*(3*x**2 + 2)/sqrt(x**4 + 5)` | $\frac{x^{3} \left(3 x^{2} + 2\right)}{\sqrt{x^{4} + 5}}$ |
| partial | concrete | `x*(3*x**2 + 2)/sqrt(x**4 + 5)` | $\frac{x \left(3 x^{2} + 2\right)}{\sqrt{x^{4} + 5}}$ |
| partial | concrete | `(3*x**2 + 2)/(x*sqrt(x**4 + 5))` | $\frac{3 x^{2} + 2}{x \sqrt{x^{4} + 5}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**3*sqrt(x**4 + 5))` | $\frac{3 x^{2} + 2}{x^{3} \sqrt{x^{4} + 5}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**5*sqrt(x**4 + 5))` | $\frac{3 x^{2} + 2}{x^{5} \sqrt{x^{4} + 5}}$ |
| partial | concrete | `x**4*(3*x**2 + 2)/sqrt(x**4 + 5)` | $\frac{x^{4} \left(3 x^{2} + 2\right)}{\sqrt{x^{4} + 5}}$ |
| partial | concrete | `x**2*(3*x**2 + 2)/sqrt(x**4 + 5)` | $\frac{x^{2} \left(3 x^{2} + 2\right)}{\sqrt{x^{4} + 5}}$ |
| partial | concrete | `(3*x**2 + 2)/sqrt(x**4 + 5)` | $\frac{3 x^{2} + 2}{\sqrt{x^{4} + 5}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**2*sqrt(x**4 + 5))` | $\frac{3 x^{2} + 2}{x^{2} \sqrt{x^{4} + 5}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**4*sqrt(x**4 + 5))` | $\frac{3 x^{2} + 2}{x^{4} \sqrt{x^{4} + 5}}$ |
| partial | concrete | `x**7*(3*x**2 + 2)/(x**4 + 5)**(3/2)` | $\frac{x^{7} \left(3 x^{2} + 2\right)}{\left(x^{4} + 5\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**5*(3*x**2 + 2)/(x**4 + 5)**(3/2)` | $\frac{x^{5} \left(3 x^{2} + 2\right)}{\left(x^{4} + 5\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**3*(3*x**2 + 2)/(x**4 + 5)**(3/2)` | $\frac{x^{3} \left(3 x^{2} + 2\right)}{\left(x^{4} + 5\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x*(3*x**2 + 2)/(x**4 + 5)**(3/2)` | $\frac{x \left(3 x^{2} + 2\right)}{\left(x^{4} + 5\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x**2 + 2)/(x*(x**4 + 5)**(3/2))` | $\frac{3 x^{2} + 2}{x \left(x^{4} + 5\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**3*(x**4 + 5)**(3/2))` | $\frac{3 x^{2} + 2}{x^{3} \left(x^{4} + 5\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**4*(3*x**2 + 2)/(x**4 + 5)**(3/2)` | $\frac{x^{4} \left(3 x^{2} + 2\right)}{\left(x^{4} + 5\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**2*(3*x**2 + 2)/(x**4 + 5)**(3/2)` | $\frac{x^{2} \left(3 x^{2} + 2\right)}{\left(x^{4} + 5\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**4 + 5)**(3/2)` | $\frac{3 x^{2} + 2}{\left(x^{4} + 5\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**2*(x**4 + 5)**(3/2))` | $\frac{3 x^{2} + 2}{x^{2} \left(x^{4} + 5\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**4*(x**4 + 5)**(3/2))` | $\frac{3 x^{2} + 2}{x^{4} \left(x^{4} + 5\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2*(d + e*x**2)/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{x^{2} \left(d + e x^{2}\right)}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| SOLVED-both | parametric | `x*(d + e*x**2)/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{x \left(d + e x^{2}\right)}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\frac{d + e x^{2}}{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/(x*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{d + e x^{2}}{x \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/(x**2*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{d + e x^{2}}{x^{2} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/(x**3*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | $\frac{d + e x^{2}}{x^{3} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}$ |
| partial | parametric | `x**2*(d + e*x**2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{x^{2} \left(d + e x^{2}\right)}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x*(d + e*x**2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{x \left(d + e x^{2}\right)}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x**2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | $\frac{d + e x^{2}}{\left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x**2)/(x*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | $\frac{d + e x^{2}}{x \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x**2)/(x**2*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | $\frac{d + e x^{2}}{x^{2} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x**2)/(x**3*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | $\frac{d + e x^{2}}{x^{3} \left(a^{2} + 2 a b x^{2} + b^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**5*(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)` | $x^{5} \left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}$ |
| partial | concrete | `x**3*(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)` | $x^{3} \left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}$ |
| partial | concrete | `x*(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)` | $x \left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)/x` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}}{x}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)/x**3` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}}{x^{3}}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)/x**5` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}}{x^{5}}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)/x**7` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}}{x^{7}}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)/x**9` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}}{x^{9}}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)/x**11` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}}{x^{11}}$ |
| partial | concrete | `x**4*(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)` | $x^{4} \left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}$ |
| partial | concrete | `x**2*(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)` | $x^{2} \left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)` | $\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)/x**2` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}}{x^{2}}$ |
| partial | concrete | `(3*x**2 + 2)*sqrt(x**4 + 5*x**2 + 3)/x**4` | $\frac{\left(3 x^{2} + 2\right) \sqrt{x^{4} + 5 x^{2} + 3}}{x^{4}}$ |
| partial | concrete | `x**5*(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)` | $x^{5} \left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `x**3*(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)` | $x^{3} \left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `x*(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)` | $x \left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)/x` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}{x}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)/x**3` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)/x**5` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)/x**7` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | concrete | `x**4*(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)` | $x^{4} \left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `x**2*(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)` | $x^{2} \left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)` | $\left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)/x**2` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)/x**4` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | concrete | `(3*x**2 + 2)*(x**4 + 5*x**2 + 3)**(3/2)/x**6` | $\frac{\left(3 x^{2} + 2\right) \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `x**5*(A + B*x**2)/sqrt(a + b*x**2 + c*x**4)` | $\frac{x^{5} \left(A + B x^{2}\right)}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**3*(A + B*x**2)/sqrt(a + b*x**2 + c*x**4)` | $\frac{x^{3} \left(A + B x^{2}\right)}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x*(A + B*x**2)/sqrt(a + b*x**2 + c*x**4)` | $\frac{x \left(A + B x^{2}\right)}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x*sqrt(a + b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x**3*sqrt(a + b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{3} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x**5*sqrt(a + b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{5} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x**7*sqrt(a + b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{7} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**4*(A + B*x**2)/sqrt(a + b*x**2 + c*x**4)` | $\frac{x^{4} \left(A + B x^{2}\right)}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**2*(A + B*x**2)/sqrt(a + b*x**2 + c*x**4)` | $\frac{x^{2} \left(A + B x^{2}\right)}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/sqrt(a + b*x**2 + c*x**4)` | $\frac{A + B x^{2}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x**2*sqrt(a + b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{2} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(x**4*sqrt(a + b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{x^{4} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | concrete | `x**7*(3*x**2 + 2)/sqrt(x**4 + 5*x**2 + 3)` | $\frac{x^{7} \left(3 x^{2} + 2\right)}{\sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `x**5*(3*x**2 + 2)/sqrt(x**4 + 5*x**2 + 3)` | $\frac{x^{5} \left(3 x^{2} + 2\right)}{\sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `x**3*(3*x**2 + 2)/sqrt(x**4 + 5*x**2 + 3)` | $\frac{x^{3} \left(3 x^{2} + 2\right)}{\sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `x*(3*x**2 + 2)/sqrt(x**4 + 5*x**2 + 3)` | $\frac{x \left(3 x^{2} + 2\right)}{\sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `(3*x**2 + 2)/(x*sqrt(x**4 + 5*x**2 + 3))` | $\frac{3 x^{2} + 2}{x \sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**3*sqrt(x**4 + 5*x**2 + 3))` | $\frac{3 x^{2} + 2}{x^{3} \sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**5*sqrt(x**4 + 5*x**2 + 3))` | $\frac{3 x^{2} + 2}{x^{5} \sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**7*sqrt(x**4 + 5*x**2 + 3))` | $\frac{3 x^{2} + 2}{x^{7} \sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `x**4*(3*x**2 + 2)/sqrt(x**4 + 5*x**2 + 3)` | $\frac{x^{4} \left(3 x^{2} + 2\right)}{\sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `x**2*(3*x**2 + 2)/sqrt(x**4 + 5*x**2 + 3)` | $\frac{x^{2} \left(3 x^{2} + 2\right)}{\sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `(3*x**2 + 2)/sqrt(x**4 + 5*x**2 + 3)` | $\frac{3 x^{2} + 2}{\sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**2*sqrt(x**4 + 5*x**2 + 3))` | $\frac{3 x^{2} + 2}{x^{2} \sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**4*sqrt(x**4 + 5*x**2 + 3))` | $\frac{3 x^{2} + 2}{x^{4} \sqrt{x^{4} + 5 x^{2} + 3}}$ |
| partial | concrete | `x**5*(3*x**2 + 2)/(x**4 + 5*x**2 + 3)**(3/2)` | $\frac{x^{5} \left(3 x^{2} + 2\right)}{\left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**3*(3*x**2 + 2)/(x**4 + 5*x**2 + 3)**(3/2)` | $\frac{x^{3} \left(3 x^{2} + 2\right)}{\left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | concrete | `x*(3*x**2 + 2)/(x**4 + 5*x**2 + 3)**(3/2)` | $\frac{x \left(3 x^{2} + 2\right)}{\left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x**2 + 2)/(x*(x**4 + 5*x**2 + 3)**(3/2))` | $\frac{3 x^{2} + 2}{x \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**3*(x**4 + 5*x**2 + 3)**(3/2))` | $\frac{3 x^{2} + 2}{x^{3} \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**4*(3*x**2 + 2)/(x**4 + 5*x**2 + 3)**(3/2)` | $\frac{x^{4} \left(3 x^{2} + 2\right)}{\left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**2*(3*x**2 + 2)/(x**4 + 5*x**2 + 3)**(3/2)` | $\frac{x^{2} \left(3 x^{2} + 2\right)}{\left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**4 + 5*x**2 + 3)**(3/2)` | $\frac{3 x^{2} + 2}{\left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**2*(x**4 + 5*x**2 + 3)**(3/2))` | $\frac{3 x^{2} + 2}{x^{2} \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x**2 + 2)/(x**4*(x**4 + 5*x**2 + 3)**(3/2))` | $\frac{3 x^{2} + 2}{x^{4} \left(x^{4} + 5 x^{2} + 3\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(f*x)**(3/2)*(d + e*x**2)*sqrt(a + b*x**2 + c*x**4)` | $\left(f x\right)^{\frac{3}{2}} \left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(f*x)*(d + e*x**2)*sqrt(a + b*x**2 + c*x**4)` | $\sqrt{f x} \left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `(d + e*x**2)*sqrt(a + b*x**2 + c*x**4)/sqrt(f*x)` | $\frac{\left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}}{\sqrt{f x}}$ |
| partial | parametric | `(d + e*x**2)*sqrt(a + b*x**2 + c*x**4)/(f*x)**(3/2)` | $\frac{\left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}}{\left(f x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(f*x)**(3/2)*(d + e*x**2)*(a + b*x**2 + c*x**4)**(3/2)` | $\left(f x\right)^{\frac{3}{2}} \left(d + e x^{2}\right) \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(f*x)*(d + e*x**2)*(a + b*x**2 + c*x**4)**(3/2)` | $\sqrt{f x} \left(d + e x^{2}\right) \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(d + e*x**2)*(a + b*x**2 + c*x**4)**(3/2)/sqrt(f*x)` | $\frac{\left(d + e x^{2}\right) \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{\sqrt{f x}}$ |
| partial | parametric | `(d + e*x**2)*(a + b*x**2 + c*x**4)**(3/2)/(f*x)**(3/2)` | $\frac{\left(d + e x^{2}\right) \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{\left(f x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(f*x)**(3/2)*(d + e*x**2)/sqrt(a + b*x**2 + c*x**4)` | $\frac{\left(f x\right)^{\frac{3}{2}} \left(d + e x^{2}\right)}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `sqrt(f*x)*(d + e*x**2)/sqrt(a + b*x**2 + c*x**4)` | $\frac{\sqrt{f x} \left(d + e x^{2}\right)}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/(sqrt(f*x)*sqrt(a + b*x**2 + c*x**4))` | $\frac{d + e x^{2}}{\sqrt{f x} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(d + e*x**2)/((f*x)**(3/2)*sqrt(a + b*x**2 + c*x**4))` | $\frac{d + e x^{2}}{\left(f x\right)^{\frac{3}{2}} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(f*x)**(3/2)*(d + e*x**2)/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{\left(f x\right)^{\frac{3}{2}} \left(d + e x^{2}\right)}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(f*x)*(d + e*x**2)/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{\sqrt{f x} \left(d + e x^{2}\right)}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x**2)/(sqrt(f*x)*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{d + e x^{2}}{\sqrt{f x} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x**2)/((f*x)**(3/2)*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{d + e x^{2}}{\left(f x\right)^{\frac{3}{2}} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**2/((x**2 + 1)*sqrt(x**4 + 1))` | $\frac{x^{2}}{\left(x^{2} + 1\right) \sqrt{x^{4} + 1}}$ |
| partial | concrete | `x**2/((1 - x**2)*sqrt(x**4 + 1))` | $\frac{x^{2}}{\left(1 - x^{2}\right) \sqrt{x^{4} + 1}}$ |
| partial | concrete | `x**2/(sqrt(1 - x**4)*(x**2 + 1))` | $\frac{x^{2}}{\sqrt{1 - x^{4}} \left(x^{2} + 1\right)}$ |
| partial | concrete | `x**2/((1 - x**2)*sqrt(1 - x**4))` | $\frac{x^{2}}{\left(1 - x^{2}\right) \sqrt{1 - x^{4}}}$ |
| partial | concrete | `x**2/((x**2 + 1)*sqrt(x**4 - 1))` | $\frac{x^{2}}{\left(x^{2} + 1\right) \sqrt{x^{4} - 1}}$ |
| partial | concrete | `x**2/((1 - x**2)*sqrt(x**4 - 1))` | $\frac{x^{2}}{\left(1 - x^{2}\right) \sqrt{x^{4} - 1}}$ |
| partial | concrete | `x**2/((x**2 + 1)*sqrt(-x**4 - 1))` | $\frac{x^{2}}{\left(x^{2} + 1\right) \sqrt{- x^{4} - 1}}$ |
| partial | concrete | `x**2/((1 - x**2)*sqrt(-x**4 - 1))` | $\frac{x^{2}}{\left(1 - x^{2}\right) \sqrt{- x^{4} - 1}}$ |
| partial | parametric | `x**2*sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $x^{2} \sqrt{c + d x^{2}} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| **SOLVED-NEW** | parametric | `x*sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $x \sqrt{c + d x^{2}} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| partial | parametric | `sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | $\sqrt{c + d x^{2}} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}$ |
| partial | parametric | `sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x` | $\frac{\sqrt{c + d x^{2}} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x}$ |
| partial | parametric | `sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**2` | $\frac{\sqrt{c + d x^{2}} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x^{2}}$ |
| partial | parametric | `sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**3` | $\frac{\sqrt{c + d x^{2}} \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}}}{x^{3}}$ |
| timeout | parametric | `1/(sqrt(f*x)*(d + e*x**2)*(a + b*x**2 + c*x**4))` | $\frac{1}{\sqrt{f x} \left(d + e x^{2}\right) \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**5*sqrt(a + b*x**2 + c*x**4)/(d + e*x**2)` | $\frac{x^{5} \sqrt{a + b x^{2} + c x^{4}}}{d + e x^{2}}$ |
| partial | parametric | `x**3*sqrt(a + b*x**2 + c*x**4)/(d + e*x**2)` | $\frac{x^{3} \sqrt{a + b x^{2} + c x^{4}}}{d + e x^{2}}$ |
| partial | parametric | `x*sqrt(a + b*x**2 + c*x**4)/(d + e*x**2)` | $\frac{x \sqrt{a + b x^{2} + c x^{4}}}{d + e x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/(x*(d + e*x**2))` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{x \left(d + e x^{2}\right)}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/(x**3*(d + e*x**2))` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{x^{3} \left(d + e x^{2}\right)}$ |
| partial | concrete | `sqrt(2*x**4 + 2*x**2 + 1)/(x**2*(2*x**2 + 3))` | $\frac{\sqrt{2 x^{4} + 2 x^{2} + 1}}{x^{2} \left(2 x^{2} + 3\right)}$ |
| partial | concrete | `sqrt(2*x**4 + 2*x**2 + 1)/(x**4*(2*x**2 + 3))` | $\frac{\sqrt{2 x^{4} + 2 x^{2} + 1}}{x^{4} \left(2 x^{2} + 3\right)}$ |
| partial | concrete | `sqrt(2*x**4 + 2*x**2 + 1)/(x**6*(2*x**2 + 3))` | $\frac{\sqrt{2 x^{4} + 2 x^{2} + 1}}{x^{6} \left(2 x^{2} + 3\right)}$ |
| partial | parametric | `x**5*(a + b*x**2 + c*x**4)**(3/2)/(d + e*x**2)` | $\frac{x^{5} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{d + e x^{2}}$ |
| partial | parametric | `x**3*(a + b*x**2 + c*x**4)**(3/2)/(d + e*x**2)` | $\frac{x^{3} \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{d + e x^{2}}$ |
| partial | parametric | `x*(a + b*x**2 + c*x**4)**(3/2)/(d + e*x**2)` | $\frac{x \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{d + e x^{2}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/(x*(d + e*x**2))` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x \left(d + e x^{2}\right)}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)/(x**3*(d + e*x**2))` | $\frac{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}{x^{3} \left(d + e x^{2}\right)}$ |
| partial | concrete | `(2*x**4 + 2*x**2 + 1)**(3/2)/(x**2*(3 - 2*x**2))` | $\frac{\left(2 x^{4} + 2 x^{2} + 1\right)^{\frac{3}{2}}}{x^{2} \left(3 - 2 x^{2}\right)}$ |
| partial | concrete | `(2*x**4 + 2*x**2 + 1)**(3/2)/(x**4*(3 - 2*x**2))` | $\frac{\left(2 x^{4} + 2 x^{2} + 1\right)^{\frac{3}{2}}}{x^{4} \left(3 - 2 x^{2}\right)}$ |
| partial | concrete | `(2*x**4 + 2*x**2 + 1)**(3/2)/(x**6*(3 - 2*x**2))` | $\frac{\left(2 x^{4} + 2 x^{2} + 1\right)^{\frac{3}{2}}}{x^{6} \left(3 - 2 x^{2}\right)}$ |
| partial | parametric | `x**5/((d + e*x**2)*sqrt(a + b*x**2 + c*x**4))` | $\frac{x^{5}}{\left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x**3/((d + e*x**2)*sqrt(a + b*x**2 + c*x**4))` | $\frac{x^{3}}{\left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `x/((d + e*x**2)*sqrt(a + b*x**2 + c*x**4))` | $\frac{x}{\left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x*(d + e*x**2)*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{x \left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/(x**3*(d + e*x**2)*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{x^{3} \left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | concrete | `x**4/((2*x**2 + 3)*sqrt(2*x**4 + 2*x**2 + 1))` | $\frac{x^{4}}{\left(2 x^{2} + 3\right) \sqrt{2 x^{4} + 2 x^{2} + 1}}$ |
| partial | concrete | `x**2/((2*x**2 + 3)*sqrt(2*x**4 + 2*x**2 + 1))` | $\frac{x^{2}}{\left(2 x^{2} + 3\right) \sqrt{2 x^{4} + 2 x^{2} + 1}}$ |
| partial | concrete | `1/((2*x**2 + 3)*sqrt(2*x**4 + 2*x**2 + 1))` | $\frac{1}{\left(2 x^{2} + 3\right) \sqrt{2 x^{4} + 2 x^{2} + 1}}$ |
| partial | concrete | `1/(x**2*(2*x**2 + 3)*sqrt(2*x**4 + 2*x**2 + 1))` | $\frac{1}{x^{2} \left(2 x^{2} + 3\right) \sqrt{2 x^{4} + 2 x^{2} + 1}}$ |
| partial | concrete | `1/(x**4*(2*x**2 + 3)*sqrt(2*x**4 + 2*x**2 + 1))` | $\frac{1}{x^{4} \left(2 x^{2} + 3\right) \sqrt{2 x^{4} + 2 x^{2} + 1}}$ |
| partial | parametric | `x**7/((d + e*x**2)*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{x^{7}}{\left(d + e x^{2}\right) \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5/((d + e*x**2)*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{x^{5}}{\left(d + e x^{2}\right) \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/((d + e*x**2)*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{x^{3}}{\left(d + e x^{2}\right) \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/((d + e*x**2)*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{x}{\left(d + e x^{2}\right) \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(d + e*x**2)*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{1}{x \left(d + e x^{2}\right) \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(d + e*x**2)*(a + b*x**2 + c*x**4)**(3/2))` | $\frac{1}{x^{3} \left(d + e x^{2}\right) \left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**7*sqrt(d + e*x**2)/(a + b*x**2 + c*x**4)` | $\frac{x^{7} \sqrt{d + e x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x**5*sqrt(d + e*x**2)/(a + b*x**2 + c*x**4)` | $\frac{x^{5} \sqrt{d + e x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x**3*sqrt(d + e*x**2)/(a + b*x**2 + c*x**4)` | $\frac{x^{3} \sqrt{d + e x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x*sqrt(d + e*x**2)/(a + b*x**2 + c*x**4)` | $\frac{x \sqrt{d + e x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(d + e*x**2)/(x*(a + b*x**2 + c*x**4))` | $\frac{\sqrt{d + e x^{2}}}{x \left(a + b x^{2} + c x^{4}\right)}$ |
| timeout | parametric | `sqrt(d + e*x**2)/(x**3*(a + b*x**2 + c*x**4))` | $\frac{\sqrt{d + e x^{2}}}{x^{3} \left(a + b x^{2} + c x^{4}\right)}$ |
| timeout | parametric | `sqrt(d + e*x**2)/(x**5*(a + b*x**2 + c*x**4))` | $\frac{\sqrt{d + e x^{2}}}{x^{5} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**4*sqrt(d + e*x**2)/(a + b*x**2 + c*x**4)` | $\frac{x^{4} \sqrt{d + e x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x**2*sqrt(d + e*x**2)/(a + b*x**2 + c*x**4)` | $\frac{x^{2} \sqrt{d + e x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(d + e*x**2)/(a + b*x**2 + c*x**4)` | $\frac{\sqrt{d + e x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(d + e*x**2)/(x**2*(a + b*x**2 + c*x**4))` | $\frac{\sqrt{d + e x^{2}}}{x^{2} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `sqrt(d + e*x**2)/(x**4*(a + b*x**2 + c*x**4))` | $\frac{\sqrt{d + e x^{2}}}{x^{4} \left(a + b x^{2} + c x^{4}\right)}$ |
| timeout | parametric | `sqrt(d + e*x**2)/(x**6*(a + b*x**2 + c*x**4))` | $\frac{\sqrt{d + e x^{2}}}{x^{6} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**3*(d + e*x**2)**(3/2)/(a + b*x**2 + c*x**4)` | $\frac{x^{3} \left(d + e x^{2}\right)^{\frac{3}{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x*(d + e*x**2)**(3/2)/(a + b*x**2 + c*x**4)` | $\frac{x \left(d + e x^{2}\right)^{\frac{3}{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `(d + e*x**2)**(3/2)/(x*(a + b*x**2 + c*x**4))` | $\frac{\left(d + e x^{2}\right)^{\frac{3}{2}}}{x \left(a + b x^{2} + c x^{4}\right)}$ |
| timeout | parametric | `(d + e*x**2)**(3/2)/(x**3*(a + b*x**2 + c*x**4))` | $\frac{\left(d + e x^{2}\right)^{\frac{3}{2}}}{x^{3} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**4*(d + e*x**2)**(3/2)/(a + b*x**2 + c*x**4)` | $\frac{x^{4} \left(d + e x^{2}\right)^{\frac{3}{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x**2*(d + e*x**2)**(3/2)/(a + b*x**2 + c*x**4)` | $\frac{x^{2} \left(d + e x^{2}\right)^{\frac{3}{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `(d + e*x**2)**(3/2)/(a + b*x**2 + c*x**4)` | $\frac{\left(d + e x^{2}\right)^{\frac{3}{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `(d + e*x**2)**(3/2)/(x**2*(a + b*x**2 + c*x**4))` | $\frac{\left(d + e x^{2}\right)^{\frac{3}{2}}}{x^{2} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `(d + e*x**2)**(3/2)/(x**4*(a + b*x**2 + c*x**4))` | $\frac{\left(d + e x^{2}\right)^{\frac{3}{2}}}{x^{4} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**5*sqrt(1 - x**2)/(a + b*x**2 + c*x**4)` | $\frac{x^{5} \sqrt{1 - x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x**3*sqrt(1 - x**2)/(a + b*x**2 + c*x**4)` | $\frac{x^{3} \sqrt{1 - x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x*sqrt(1 - x**2)/(a + b*x**2 + c*x**4)` | $\frac{x \sqrt{1 - x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(1 - x**2)/(x*(a + b*x**2 + c*x**4))` | $\frac{\sqrt{1 - x^{2}}}{x \left(a + b x^{2} + c x^{4}\right)}$ |
| timeout | parametric | `sqrt(1 - x**2)/(x**3*(a + b*x**2 + c*x**4))` | $\frac{\sqrt{1 - x^{2}}}{x^{3} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**4*sqrt(1 - x**2)/(a + b*x**2 + c*x**4)` | $\frac{x^{4} \sqrt{1 - x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `x**2*sqrt(1 - x**2)/(a + b*x**2 + c*x**4)` | $\frac{x^{2} \sqrt{1 - x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(1 - x**2)/(a + b*x**2 + c*x**4)` | $\frac{\sqrt{1 - x^{2}}}{a + b x^{2} + c x^{4}}$ |
| partial | parametric | `sqrt(1 - x**2)/(x**2*(a + b*x**2 + c*x**4))` | $\frac{\sqrt{1 - x^{2}}}{x^{2} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | concrete | `x**2*sqrt(1 - x**2)/(x**4 + x**2 - 1)` | $\frac{x^{2} \sqrt{1 - x^{2}}}{x^{4} + x^{2} - 1}$ |
| timeout | parametric | `x**8/(sqrt(d + e*x**2)*(a + b*x**2 + c*x**4))` | $\frac{x^{8}}{\sqrt{d + e x^{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**6/(sqrt(d + e*x**2)*(a + b*x**2 + c*x**4))` | $\frac{x^{6}}{\sqrt{d + e x^{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**4/(sqrt(d + e*x**2)*(a + b*x**2 + c*x**4))` | $\frac{x^{4}}{\sqrt{d + e x^{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**2/(sqrt(d + e*x**2)*(a + b*x**2 + c*x**4))` | $\frac{x^{2}}{\sqrt{d + e x^{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `1/(sqrt(d + e*x**2)*(a + b*x**2 + c*x**4))` | $\frac{1}{\sqrt{d + e x^{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `1/(x**2*sqrt(d + e*x**2)*(a + b*x**2 + c*x**4))` | $\frac{1}{x^{2} \sqrt{d + e x^{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `1/(x**4*sqrt(d + e*x**2)*(a + b*x**2 + c*x**4))` | $\frac{1}{x^{4} \sqrt{d + e x^{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| timeout | parametric | `1/(x**6*sqrt(d + e*x**2)*(a + b*x**2 + c*x**4))` | $\frac{1}{x^{6} \sqrt{d + e x^{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**4/((d + e*x**2)**(3/2)*(a + b*x**2 + c*x**4))` | $\frac{x^{4}}{\left(d + e x^{2}\right)^{\frac{3}{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `x**2/((d + e*x**2)**(3/2)*(a + b*x**2 + c*x**4))` | $\frac{x^{2}}{\left(d + e x^{2}\right)^{\frac{3}{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `1/((d + e*x**2)**(3/2)*(a + b*x**2 + c*x**4))` | $\frac{1}{\left(d + e x^{2}\right)^{\frac{3}{2}} \left(a + b x^{2} + c x^{4}\right)}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)**(3/2)*(d + e*x + f*x**2 + g*x**3)` | $\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}} \left(d + e x + f x^{2} + g x^{3}\right)$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)*(d + e*x + f*x**2 + g*x**3)` | $\sqrt{a + b x^{2} + c x^{4}} \left(d + e x + f x^{2} + g x^{3}\right)$ |
| partial | parametric | `(d + e*x + f*x**2 + g*x**3)/sqrt(a + b*x**2 + c*x**4)` | $\frac{d + e x + f x^{2} + g x^{3}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(d + e*x + f*x**2 + g*x**3)/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{d + e x + f x^{2} + g x^{3}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x + f*x**2 + g*x**3)/(a + b*x**2 + c*x**4)**(5/2)` | $\frac{d + e x + f x^{2} + g x^{3}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a*g - c*g*x**4)/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{a g - c g x^{4}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a*g - c*g*x**4 + e*x)/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{a g - c g x^{4} + e x}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a*g - c*g*x**4 + f*x**3)/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{a g - c g x^{4} + f x^{3}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `(a*g - c*g*x**4 + e*x + f*x**3)/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{a g - c g x^{4} + e x + f x^{3}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**2 + c*x**4)/(x**4*sqrt(d - e*x)*sqrt(d + e*x))` | $\frac{a + b x^{2} + c x^{4}}{x^{4} \sqrt{d - e x} \sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2 + c*x**4)/(x**6*sqrt(d - e*x)*sqrt(d + e*x))` | $\frac{a + b x^{2} + c x^{4}}{x^{6} \sqrt{d - e x} \sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2 + c*x**4)/(x**8*sqrt(d - e*x)*sqrt(d + e*x))` | $\frac{a + b x^{2} + c x^{4}}{x^{8} \sqrt{d - e x} \sqrt{d + e x}}$ |
| **SOLVED-NEW** | parametric | `(a + b*x**2 + c*x**4)/(x**10*sqrt(d - e*x)*sqrt(d + e*x))` | $\frac{a + b x^{2} + c x^{4}}{x^{10} \sqrt{d - e x} \sqrt{d + e x}}$ |
| partial | parametric | `(A + B*x**2)/sqrt(a + c*x**4)` | $\frac{A + B x^{2}}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(a + c*x**4)*(d + e*x**2))` | $\frac{A + B x^{2}}{\sqrt{a + c x^{4}} \left(d + e x^{2}\right)}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(a + c*x**4)*(d + e*x**2)**2)` | $\frac{A + B x^{2}}{\sqrt{a + c x^{4}} \left(d + e x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x**2)/(sqrt(a + c*x**4)*(d + e*x**2)**3)` | $\frac{A + B x^{2}}{\sqrt{a + c x^{4}} \left(d + e x^{2}\right)^{3}}$ |
| partial | parametric | `(A + B*x**2)*(d + e*x**2)**3/(a + c*x**4)**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(d + e x^{2}\right)^{3}}{\left(a + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(d + e*x**2)**2/(a + c*x**4)**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(d + e x^{2}\right)^{2}}{\left(a + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(d + e*x**2)/(a + c*x**4)**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(d + e x^{2}\right)}{\left(a + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(a + c*x**4)**(3/2)` | $\frac{A + B x^{2}}{\left(a + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/((a + c*x**4)**(3/2)*(d + e*x**2))` | $\frac{A + B x^{2}}{\left(a + c x^{4}\right)^{\frac{3}{2}} \left(d + e x^{2}\right)}$ |
| partial | parametric | `(A + B*x**2)/((a + c*x**4)**(3/2)*(d + e*x**2)**2)` | $\frac{A + B x^{2}}{\left(a + c x^{4}\right)^{\frac{3}{2}} \left(d + e x^{2}\right)^{2}}$ |
| partial | parametric | `(A + B*x**2)/((a + c*x**4)**(3/2)*(d + e*x**2)**3)` | $\frac{A + B x^{2}}{\left(a + c x^{4}\right)^{\frac{3}{2}} \left(d + e x^{2}\right)^{3}}$ |
| partial | concrete | `(x**2 + 2)/((x**2 + 1)*sqrt(x**4 + 3*x**2 + 2))` | $\frac{x^{2} + 2}{\left(x^{2} + 1\right) \sqrt{x^{4} + 3 x^{2} + 2}}$ |
| partial | parametric | `(A + B*x**2)*(d + e*x**2)**3/sqrt(a + b*x**2 + c*x**4)` | $\frac{\left(A + B x^{2}\right) \left(d + e x^{2}\right)^{3}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)*(d + e*x**2)**2/sqrt(a + b*x**2 + c*x**4)` | $\frac{\left(A + B x^{2}\right) \left(d + e x^{2}\right)^{2}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)*(d + e*x**2)/sqrt(a + b*x**2 + c*x**4)` | $\frac{\left(A + B x^{2}\right) \left(d + e x^{2}\right)}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/sqrt(a + b*x**2 + c*x**4)` | $\frac{A + B x^{2}}{\sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/((d + e*x**2)*sqrt(a + b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{\left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/((d + e*x**2)**2*sqrt(a + b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{\left(d + e x^{2}\right)^{2} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)/((d + e*x**2)**3*sqrt(a + b*x**2 + c*x**4))` | $\frac{A + B x^{2}}{\left(d + e x^{2}\right)^{3} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(A + B*x**2)*(d + e*x**2)**3/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(d + e x^{2}\right)^{3}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(d + e*x**2)**2/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(d + e x^{2}\right)^{2}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)*(d + e*x**2)/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{\left(A + B x^{2}\right) \left(d + e x^{2}\right)}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(A + B*x**2)/(a + b*x**2 + c*x**4)**(3/2)` | $\frac{A + B x^{2}}{\left(a + b x^{2} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(sqrt(a) + sqrt(c)*x**2)/((d + e*x**2)*sqrt(a + b*x**2 + c*x**4))` | $\frac{\sqrt{a} + \sqrt{c} x^{2}}{\left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(x**2*sqrt(c/a) + 1)/((d + e*x**2)*sqrt(a + b*x**2 + c*x**4))` | $\frac{x^{2} \sqrt{\frac{c}{a}} + 1}{\left(d + e x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | concrete | `(315*x**2 + 946)/((5*x**2 + 7)*sqrt(x**4 + 3*x**2 + 2))` | $\frac{315 x^{2} + 946}{\left(5 x^{2} + 7\right) \sqrt{x^{4} + 3 x^{2} + 2}}$ |
| partial | concrete | `x*(2*x**2 + 1)/(sqrt(x**2 + 1)*(x**4 + x**2 + 1))` | $\frac{x \left(2 x^{2} + 1\right)}{\sqrt{x^{2} + 1} \left(x^{4} + x^{2} + 1\right)}$ |
| partial | parametric | `sqrt(a + b*x**2 + c*x**4)/(a*d - c*d*x**4)` | $\frac{\sqrt{a + b x^{2} + c x^{4}}}{a d - c d x^{4}}$ |
| partial | parametric | `sqrt(a + b*x**2 - c*x**4)/(a*d + c*d*x**4)` | $\frac{\sqrt{a + b x^{2} - c x^{4}}}{a d + c d x^{4}}$ |
| timeout | parametric | `x*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)*sqrt(c + d*x**2 + e*x)` | $x \sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}} \sqrt{c + d x^{2} + e x}$ |
| timeout | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)*sqrt(c + d*x**2 + e*x)` | $\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}} \sqrt{c + d x^{2} + e x}$ |
| timeout | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)*sqrt(c + d*x**2 + e*x)/x` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}} \sqrt{c + d x^{2} + e x}}{x}$ |
| timeout | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)*sqrt(c + d*x**2 + e*x)/x**2` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}} \sqrt{c + d x^{2} + e x}}{x^{2}}$ |
| timeout | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)*sqrt(c + d*x**2 + e*x)/x**3` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}} \sqrt{c + d x^{2} + e x}}{x^{3}}$ |
| timeout | parametric | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)*sqrt(c + d*x**2 + e*x)/x**4` | $\frac{\sqrt{a^{2} + 2 a b x^{2} + b^{2} x^{4}} \sqrt{c + d x^{2} + e x}}{x^{4}}$ |
| partial | parametric | `1/(sqrt(a + c*x**4)*(d + e*x))` | $\frac{1}{\sqrt{a + c x^{4}} \left(d + e x\right)}$ |
| partial | parametric | `1/(sqrt(a + c*x**4)*(d + e*x)**2)` | $\frac{1}{\sqrt{a + c x^{4}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `1/((d + e*x)*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{\left(d + e x\right) \sqrt{a + b x^{2} + c x^{4}}}$ |
| timeout | parametric | `1/((d + e*x)**2*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{\left(d + e x\right)^{2} \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `(a*x**3 + b*x**6)**(5/3)` | $\left(a x^{3} + b x^{6}\right)^{\frac{5}{3}}$ |
| partial | parametric | `(a*x**3 + b*x**6)**(2/3)` | $\left(a x^{3} + b x^{6}\right)^{\frac{2}{3}}$ |
| **SOLVED-NEW** | parametric | `(a*x**3 + b*x**6)**(-2/3)` | $\frac{1}{\left(a x^{3} + b x^{6}\right)^{\frac{2}{3}}}$ |
| **SOLVED-NEW** | parametric | `(a*x**3 + b*x**6)**(-5/3)` | $\frac{1}{\left(a x^{3} + b x^{6}\right)^{\frac{5}{3}}}$ |
| **SOLVED-NEW** | parametric | `x**5*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | $x^{5} \sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}$ |
| **SOLVED-NEW** | parametric | `x**4*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | $x^{4} \sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}$ |
| **SOLVED-NEW** | parametric | `x**3*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | $x^{3} \sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}$ |
| **SOLVED-NEW** | parametric | `x**2*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | $x^{2} \sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}$ |
| **SOLVED-NEW** | parametric | `x*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | $x \sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | $\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x` | $\frac{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}{x}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**2` | $\frac{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}{x^{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**3` | $\frac{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}{x^{3}}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**4` | $\frac{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}{x^{4}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**5` | $\frac{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**6` | $\frac{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}{x^{6}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**7` | $\frac{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**8` | $\frac{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**9` | $\frac{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}{x^{9}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**10` | $\frac{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}{x^{10}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**11` | $\frac{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `x**9*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $x^{9} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x**8*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $x^{8} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x**7*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $x^{7} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x**6*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $x^{6} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x**5*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $x^{5} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x**4*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $x^{4} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x**3*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $x^{3} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x**2*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $x^{2} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $x \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**2` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{2}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**3` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**4` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{4}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**5` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**6` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**7` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**8` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**9` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{9}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**10` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{10}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**11` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**12` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{12}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**13` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{13}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**14` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{14}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**15` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{15}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**16` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{16}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**17` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}{x^{17}}$ |
| **SOLVED-NEW** | parametric | `x**13*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x^{13} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**12*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x^{12} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**11*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x^{11} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**10*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x^{10} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**9*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x^{9} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**8*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x^{8} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**7*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x^{7} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**6*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x^{6} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**5*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x^{5} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**4*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x^{4} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**3*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x^{3} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x**2*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x^{2} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `x*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $x \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**2` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{2}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**3` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{3}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**4` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{4}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**5` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{5}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**6` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{6}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**7` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{7}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**8` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{8}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**9` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{9}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**10` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{10}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**11` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{11}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**12` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{12}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**13` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{13}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**14` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{14}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**15` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{15}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**16` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{16}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**17` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{17}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**18` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{18}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**19` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{19}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**20` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{20}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**21` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{21}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**22` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{22}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**23` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{23}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**24` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{24}}$ |
| **SOLVED-NEW** | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**25` | $\frac{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}{x^{25}}$ |
| partial | parametric | `x**4/sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | $\frac{x^{4}}{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}$ |
| partial | parametric | `x**3/sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | $\frac{x^{3}}{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}$ |
| **SOLVED-NEW** | parametric | `x**2/sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | $\frac{x^{2}}{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}$ |
| partial | parametric | `x/sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | $\frac{x}{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}$ |
| partial | parametric | `1/sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | $\frac{1}{\sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}$ |
| partial | parametric | `1/(x*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6))` | $\frac{1}{x \sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}$ |
| partial | parametric | `1/(x**2*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6))` | $\frac{1}{x^{2} \sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}$ |
| partial | parametric | `1/(x**3*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6))` | $\frac{1}{x^{3} \sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}$ |
| partial | parametric | `1/(x**4*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6))` | $\frac{1}{x^{4} \sqrt{a^{2} + 2 a b x^{3} + b^{2} x^{6}}}$ |
| partial | parametric | `x**4/(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $\frac{x^{4}}{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $\frac{x^{3}}{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2/(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $\frac{x^{2}}{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | $\frac{x}{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(-3/2)` | $\frac{1}{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2))` | $\frac{1}{x \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2))` | $\frac{1}{x^{2} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2))` | $\frac{1}{x^{3} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2))` | $\frac{1}{x^{4} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**6/(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $\frac{x^{6}}{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**5/(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $\frac{x^{5}}{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**4/(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $\frac{x^{4}}{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**3/(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $\frac{x^{3}}{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2/(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $\frac{x^{2}}{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x/(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | $\frac{x}{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(-5/2)` | $\frac{1}{\left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2))` | $\frac{1}{x \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**2*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2))` | $\frac{1}{x^{2} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**3*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2))` | $\frac{1}{x^{3} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x**4*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2))` | $\frac{1}{x^{4} \left(a^{2} + 2 a b x^{3} + b^{2} x^{6}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**14*sqrt(a + b*x**3 + c*x**6)` | $x^{14} \sqrt{a + b x^{3} + c x^{6}}$ |
| partial | parametric | `x**11*sqrt(a + b*x**3 + c*x**6)` | $x^{11} \sqrt{a + b x^{3} + c x^{6}}$ |
| partial | parametric | `x**8*sqrt(a + b*x**3 + c*x**6)` | $x^{8} \sqrt{a + b x^{3} + c x^{6}}$ |
| partial | parametric | `x**5*sqrt(a + b*x**3 + c*x**6)` | $x^{5} \sqrt{a + b x^{3} + c x^{6}}$ |
| partial | parametric | `x**2*sqrt(a + b*x**3 + c*x**6)` | $x^{2} \sqrt{a + b x^{3} + c x^{6}}$ |
| partial | parametric | `sqrt(a + b*x**3 + c*x**6)/x` | $\frac{\sqrt{a + b x^{3} + c x^{6}}}{x}$ |
| partial | parametric | `sqrt(a + b*x**3 + c*x**6)/x**4` | $\frac{\sqrt{a + b x^{3} + c x^{6}}}{x^{4}}$ |
| partial | parametric | `sqrt(a + b*x**3 + c*x**6)/x**7` | $\frac{\sqrt{a + b x^{3} + c x^{6}}}{x^{7}}$ |
| partial | parametric | `sqrt(a + b*x**3 + c*x**6)/x**10` | $\frac{\sqrt{a + b x^{3} + c x^{6}}}{x^{10}}$ |
| partial | parametric | `sqrt(a + b*x**3 + c*x**6)/x**13` | $\frac{\sqrt{a + b x^{3} + c x^{6}}}{x^{13}}$ |
| partial | parametric | `sqrt(a + b*x**3 + c*x**6)/x**16` | $\frac{\sqrt{a + b x^{3} + c x^{6}}}{x^{16}}$ |
| partial | parametric | `x**3*sqrt(a + b*x**3 + c*x**6)` | $x^{3} \sqrt{a + b x^{3} + c x^{6}}$ |
| partial | parametric | `x*sqrt(a + b*x**3 + c*x**6)` | $x \sqrt{a + b x^{3} + c x^{6}}$ |
| partial | parametric | `sqrt(a + b*x**3 + c*x**6)` | $\sqrt{a + b x^{3} + c x^{6}}$ |
| partial | parametric | `sqrt(a + b*x**3 + c*x**6)/x**2` | $\frac{\sqrt{a + b x^{3} + c x^{6}}}{x^{2}}$ |
| partial | parametric | `sqrt(a + b*x**3 + c*x**6)/x**3` | $\frac{\sqrt{a + b x^{3} + c x^{6}}}{x^{3}}$ |
| partial | parametric | `x**14*(a + b*x**3 + c*x**6)**(3/2)` | $x^{14} \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**11*(a + b*x**3 + c*x**6)**(3/2)` | $x^{11} \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**8*(a + b*x**3 + c*x**6)**(3/2)` | $x^{8} \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**5*(a + b*x**3 + c*x**6)**(3/2)` | $x^{5} \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*(a + b*x**3 + c*x**6)**(3/2)` | $x^{2} \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)**(3/2)/x` | $\frac{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)**(3/2)/x**4` | $\frac{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)**(3/2)/x**7` | $\frac{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)**(3/2)/x**10` | $\frac{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}{x^{10}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)**(3/2)/x**13` | $\frac{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}{x^{13}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)**(3/2)/x**16` | $\frac{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}{x^{16}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)**(3/2)/x**19` | $\frac{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}{x^{19}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)**(3/2)/x**22` | $\frac{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}{x^{22}}$ |
| partial | parametric | `x**3*(a + b*x**3 + c*x**6)**(3/2)` | $x^{3} \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*(a + b*x**3 + c*x**6)**(3/2)` | $x \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)**(3/2)` | $\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)**(3/2)/x**2` | $\frac{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)**(3/2)/x**3` | $\frac{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `x**14/sqrt(a + b*x**3 + c*x**6)` | $\frac{x^{14}}{\sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `x**11/sqrt(a + b*x**3 + c*x**6)` | $\frac{x^{11}}{\sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `x**8/sqrt(a + b*x**3 + c*x**6)` | $\frac{x^{8}}{\sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `x**5/sqrt(a + b*x**3 + c*x**6)` | $\frac{x^{5}}{\sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `x**2/sqrt(a + b*x**3 + c*x**6)` | $\frac{x^{2}}{\sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x**3 + c*x**6))` | $\frac{1}{x \sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `1/(x**4*sqrt(a + b*x**3 + c*x**6))` | $\frac{1}{x^{4} \sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `1/(x**7*sqrt(a + b*x**3 + c*x**6))` | $\frac{1}{x^{7} \sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `1/(x**10*sqrt(a + b*x**3 + c*x**6))` | $\frac{1}{x^{10} \sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `1/(x**13*sqrt(a + b*x**3 + c*x**6))` | $\frac{1}{x^{13} \sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `x**3/sqrt(a + b*x**3 + c*x**6)` | $\frac{x^{3}}{\sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `x/sqrt(a + b*x**3 + c*x**6)` | $\frac{x}{\sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `1/sqrt(a + b*x**3 + c*x**6)` | $\frac{1}{\sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b*x**3 + c*x**6))` | $\frac{1}{x^{2} \sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `1/(x**3*sqrt(a + b*x**3 + c*x**6))` | $\frac{1}{x^{3} \sqrt{a + b x^{3} + c x^{6}}}$ |
| partial | parametric | `x**14/(a + b*x**3 + c*x**6)**(3/2)` | $\frac{x^{14}}{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**11/(a + b*x**3 + c*x**6)**(3/2)` | $\frac{x^{11}}{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**8/(a + b*x**3 + c*x**6)**(3/2)` | $\frac{x^{8}}{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**5/(a + b*x**3 + c*x**6)**(3/2)` | $\frac{x^{5}}{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**2/(a + b*x**3 + c*x**6)**(3/2)` | $\frac{x^{2}}{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a + b*x**3 + c*x**6)**(3/2))` | $\frac{1}{x \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**4*(a + b*x**3 + c*x**6)**(3/2))` | $\frac{1}{x^{4} \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**7*(a + b*x**3 + c*x**6)**(3/2))` | $\frac{1}{x^{7} \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**10*(a + b*x**3 + c*x**6)**(3/2))` | $\frac{1}{x^{10} \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**3/(a + b*x**3 + c*x**6)**(3/2)` | $\frac{x^{3}}{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a + b*x**3 + c*x**6)**(3/2)` | $\frac{x}{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)**(-3/2)` | $\frac{1}{\left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a + b*x**3 + c*x**6)**(3/2))` | $\frac{1}{x^{2} \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**3*(a + b*x**3 + c*x**6)**(3/2))` | $\frac{1}{x^{3} \left(a + b x^{3} + c x^{6}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x + c/x**2)**(5/2)` | $\left(a + \frac{b}{x} + \frac{c}{x^{2}}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a + b/x + c/x**2)**(3/2)` | $\left(a + \frac{b}{x} + \frac{c}{x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(a + b/x + c/x**2)` | $\sqrt{a + \frac{b}{x} + \frac{c}{x^{2}}}$ |
| partial | parametric | `1/sqrt(a + b/x + c/x**2)` | $\frac{1}{\sqrt{a + \frac{b}{x} + \frac{c}{x^{2}}}}$ |
| partial | parametric | `(a + b/x + c/x**2)**(-3/2)` | $\frac{1}{\left(a + \frac{b}{x} + \frac{c}{x^{2}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b/x + c/x**2)**(-5/2)` | $\frac{1}{\left(a + \frac{b}{x} + \frac{c}{x^{2}}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(a**2 + 2*a*b/x + b**2/x**2)` | $\sqrt{a^{2} + \frac{2 a b}{x} + \frac{b^{2}}{x^{2}}}$ |
| NIE | parametric | `sqrt(a + b*sqrt(x) + c*x)/x` | $\frac{\sqrt{a + b \sqrt{x} + c x}}{x}$ |
| SOLVED-both | parametric | `(b**2/(4*c) + b*sqrt(x) + c*x)**2` | $\left(\frac{b^{2}}{4 c} + b \sqrt{x} + c x\right)^{2}$ |
| NIE | parametric | `1/sqrt(a**2 + 2*a*b*sqrt(x) + b**2*x)` | $\frac{1}{\sqrt{a^{2} + 2 a b \sqrt{x} + b^{2} x}}$ |
| timeout | parametric | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(7/2)` | $\left(a^{2} + 2 a b \sqrt[3]{x} + b^{2} x^{\frac{2}{3}}\right)^{\frac{7}{2}}$ |
| timeout | parametric | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(5/2)` | $\left(a^{2} + 2 a b \sqrt[3]{x} + b^{2} x^{\frac{2}{3}}\right)^{\frac{5}{2}}$ |
| timeout | parametric | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(3/2)` | $\left(a^{2} + 2 a b \sqrt[3]{x} + b^{2} x^{\frac{2}{3}}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `sqrt(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))` | $\sqrt{a^{2} + 2 a b \sqrt[3]{x} + b^{2} x^{\frac{2}{3}}}$ |
| partial | parametric | `1/sqrt(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))` | $\frac{1}{\sqrt{a^{2} + 2 a b \sqrt[3]{x} + b^{2} x^{\frac{2}{3}}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(-3/2)` | $\frac{1}{\left(a^{2} + 2 a b \sqrt[3]{x} + b^{2} x^{\frac{2}{3}}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(-5/2)` | $\frac{1}{\left(a^{2} + 2 a b \sqrt[3]{x} + b^{2} x^{\frac{2}{3}}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(-7/2)` | $\frac{1}{\left(a^{2} + 2 a b \sqrt[3]{x} + b^{2} x^{\frac{2}{3}}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(-9/2)` | $\frac{1}{\left(a^{2} + 2 a b \sqrt[3]{x} + b^{2} x^{\frac{2}{3}}\right)^{\frac{9}{2}}}$ |
| SOLVED-both | parametric | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(-11/2)` | $\frac{1}{\left(a^{2} + 2 a b \sqrt[3]{x} + b^{2} x^{\frac{2}{3}}\right)^{\frac{11}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**(1/4) + b**2*sqrt(x))**(-3/2)` | $\frac{1}{\left(a^{2} + 2 a b \sqrt[4]{x} + b^{2} \sqrt{x}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**(1/6) + b**2*x**(1/3))**(-5/2)` | $\frac{1}{\left(a^{2} + 2 a b \sqrt[6]{x} + b^{2} \sqrt[3]{x}\right)^{\frac{5}{2}}}$ |
| NIE | parametric | `(a**2 + 2*a*b/sqrt(x) + b**2/x)**(3/2)` | $\left(a^{2} + \frac{2 a b}{\sqrt{x}} + \frac{b^{2}}{x}\right)^{\frac{3}{2}}$ |
| timeout | parametric | `(a**2 + 2*a*b/x**(1/3) + b**2/x**(2/3))**(7/2)` | $\left(a^{2} + \frac{2 a b}{\sqrt[3]{x}} + \frac{b^{2}}{x^{\frac{2}{3}}}\right)^{\frac{7}{2}}$ |
| timeout | parametric | `(a**2 + 2*a*b/x**(1/3) + b**2/x**(2/3))**(5/2)` | $\left(a^{2} + \frac{2 a b}{\sqrt[3]{x}} + \frac{b^{2}}{x^{\frac{2}{3}}}\right)^{\frac{5}{2}}$ |
| timeout | parametric | `(a**2 + 2*a*b/x**(1/3) + b**2/x**(2/3))**(3/2)` | $\left(a^{2} + \frac{2 a b}{\sqrt[3]{x}} + \frac{b^{2}}{x^{\frac{2}{3}}}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a**2 + 2*a*b/x**(1/3) + b**2/x**(2/3))` | $\sqrt{a^{2} + \frac{2 a b}{\sqrt[3]{x}} + \frac{b^{2}}{x^{\frac{2}{3}}}}$ |
| partial | parametric | `1/sqrt(a**2 + 2*a*b/x**(1/3) + b**2/x**(2/3))` | $\frac{1}{\sqrt{a^{2} + \frac{2 a b}{\sqrt[3]{x}} + \frac{b^{2}}{x^{\frac{2}{3}}}}}$ |
| partial | parametric | `(a**2 + 2*a*b/x**(1/3) + b**2/x**(2/3))**(-3/2)` | $\frac{1}{\left(a^{2} + \frac{2 a b}{\sqrt[3]{x}} + \frac{b^{2}}{x^{\frac{2}{3}}}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a**2 + 2*a*b/x**(1/3) + b**2/x**(2/3))**(-5/2)` | $\frac{1}{\left(a^{2} + \frac{2 a b}{\sqrt[3]{x}} + \frac{b^{2}}{x^{\frac{2}{3}}}\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a**2 + 2*a*b/x**(1/4) + b**2/sqrt(x))**(5/2)` | $\left(a^{2} + \frac{2 a b}{\sqrt[4]{x}} + \frac{b^{2}}{\sqrt{x}}\right)^{\frac{5}{2}}$ |
| timeout | parametric | `(a**2 + 2*a*b/x**(1/5) + b**2/x**(2/5))**(5/2)` | $\left(a^{2} + \frac{2 a b}{\sqrt[5]{x}} + \frac{b^{2}}{x^{\frac{2}{5}}}\right)^{\frac{5}{2}}$ |
| partial | parametric | `(a**2 + 2*a*b*x**(1/5) + b**2*x**(2/5))**(-5/2)` | $\frac{1}{\left(a^{2} + 2 a b \sqrt[5]{x} + b^{2} x^{\frac{2}{5}}\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `(a**2 + 2*a*b/x**(1/6) + b**2/x**(1/3))**(7/2)` | $\left(a^{2} + \frac{2 a b}{\sqrt[6]{x}} + \frac{b^{2}}{\sqrt[3]{x}}\right)^{\frac{7}{2}}$ |
| partial | parametric | `x/sqrt(a + b*(d + e*x)**3 + c*(d + e*x)**6)` | $\frac{x}{\sqrt{a + b \left(d + e x\right)^{3} + c \left(d + e x\right)^{6}}}$ |
| partial | parametric | `x**2/sqrt(a + b*(d + e*x)**3 + c*(d + e*x)**6)` | $\frac{x^{2}}{\sqrt{a + b \left(d + e x\right)^{3} + c \left(d + e x\right)^{6}}}$ |
| partial | parametric | `(d + e*x**3)**(5/2)*(a + b*x**3 + c*x**6)` | $\left(d + e x^{3}\right)^{\frac{5}{2}} \left(a + b x^{3} + c x^{6}\right)$ |
| partial | parametric | `(d + e*x**3)**(3/2)*(a + b*x**3 + c*x**6)` | $\left(d + e x^{3}\right)^{\frac{3}{2}} \left(a + b x^{3} + c x^{6}\right)$ |
| partial | parametric | `sqrt(d + e*x**3)*(a + b*x**3 + c*x**6)` | $\sqrt{d + e x^{3}} \left(a + b x^{3} + c x^{6}\right)$ |
| partial | parametric | `(a + b*x**3 + c*x**6)/sqrt(d + e*x**3)` | $\frac{a + b x^{3} + c x^{6}}{\sqrt{d + e x^{3}}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)/(d + e*x**3)**(3/2)` | $\frac{a + b x^{3} + c x^{6}}{\left(d + e x^{3}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)/(d + e*x**3)**(5/2)` | $\frac{a + b x^{3} + c x^{6}}{\left(d + e x^{3}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)/(d + e*x**3)**(7/2)` | $\frac{a + b x^{3} + c x^{6}}{\left(d + e x^{3}\right)^{\frac{7}{2}}}$ |
| partial | parametric | `(a + b*x**3 + c*x**6)/(d + e*x**3)**(9/2)` | $\frac{a + b x^{3} + c x^{6}}{\left(d + e x^{3}\right)^{\frac{9}{2}}}$ |
| timeout | parametric | `x**4*sqrt(d + e*x)*sqrt(a + b/x + c/x**2)` | $x^{4} \sqrt{d + e x} \sqrt{a + \frac{b}{x} + \frac{c}{x^{2}}}$ |
| timeout | parametric | `x**3*sqrt(d + e*x)*sqrt(a + b/x + c/x**2)` | $x^{3} \sqrt{d + e x} \sqrt{a + \frac{b}{x} + \frac{c}{x^{2}}}$ |
| timeout | parametric | `x**2*sqrt(d + e*x)*sqrt(a + b/x + c/x**2)` | $x^{2} \sqrt{d + e x} \sqrt{a + \frac{b}{x} + \frac{c}{x^{2}}}$ |
| timeout | parametric | `x*sqrt(d + e*x)*sqrt(a + b/x + c/x**2)` | $x \sqrt{d + e x} \sqrt{a + \frac{b}{x} + \frac{c}{x^{2}}}$ |
| timeout | parametric | `sqrt(d + e*x)*sqrt(a + b/x + c/x**2)` | $\sqrt{d + e x} \sqrt{a + \frac{b}{x} + \frac{c}{x^{2}}}$ |
| timeout | parametric | `sqrt(d + e*x)*sqrt(a + b/x + c/x**2)/x` | $\frac{\sqrt{d + e x} \sqrt{a + \frac{b}{x} + \frac{c}{x^{2}}}}{x}$ |
| timeout | parametric | `sqrt(d + e*x)*sqrt(a + b/x + c/x**2)/x**2` | $\frac{\sqrt{d + e x} \sqrt{a + \frac{b}{x} + \frac{c}{x^{2}}}}{x^{2}}$ |
| timeout | parametric | `(c**(1/3) - 2*d**(1/3)*x**(1/3))/(-c**(2/3)*d**(2/3)*x + c**(1/3)*d*x**(4/3) + c*d**(1/3)*x**(2/3))` | $\frac{\sqrt[3]{c} - 2 \sqrt[3]{d} \sqrt[3]{x}}{- c^{\frac{2}{3}} d^{\frac{2}{3}} x + \sqrt[3]{c} d x^{\frac{4}{3}} + c \sqrt[3]{d} x^{\frac{2}{3}}}$ |
| partial | parametric | `x**2*sqrt(a*x**2 + b*x**3 + c*x**4)` | $x^{2} \sqrt{a x^{2} + b x^{3} + c x^{4}}$ |
| partial | parametric | `x*sqrt(a*x**2 + b*x**3 + c*x**4)` | $x \sqrt{a x^{2} + b x^{3} + c x^{4}}$ |
| partial | parametric | `sqrt(a*x**2 + b*x**3 + c*x**4)` | $\sqrt{a x^{2} + b x^{3} + c x^{4}}$ |
| partial | parametric | `sqrt(a*x**2 + b*x**3 + c*x**4)/x` | $\frac{\sqrt{a x^{2} + b x^{3} + c x^{4}}}{x}$ |
| partial | parametric | `sqrt(a*x**2 + b*x**3 + c*x**4)/x**2` | $\frac{\sqrt{a x^{2} + b x^{3} + c x^{4}}}{x^{2}}$ |
| partial | parametric | `sqrt(a*x**2 + b*x**3 + c*x**4)/x**3` | $\frac{\sqrt{a x^{2} + b x^{3} + c x^{4}}}{x^{3}}$ |
| partial | parametric | `sqrt(a*x**2 + b*x**3 + c*x**4)/x**4` | $\frac{\sqrt{a x^{2} + b x^{3} + c x^{4}}}{x^{4}}$ |
| partial | parametric | `sqrt(a*x**2 + b*x**3 + c*x**4)/x**5` | $\frac{\sqrt{a x^{2} + b x^{3} + c x^{4}}}{x^{5}}$ |
| partial | parametric | `sqrt(a*x**2 + b*x**3 + c*x**4)/x**6` | $\frac{\sqrt{a x^{2} + b x^{3} + c x^{4}}}{x^{6}}$ |
| partial | parametric | `x*(a*x**2 + b*x**3 + c*x**4)**(3/2)` | $x \left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*x**2 + b*x**3 + c*x**4)**(3/2)` | $\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*x**2 + b*x**3 + c*x**4)**(3/2)/x` | $\frac{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(a*x**2 + b*x**3 + c*x**4)**(3/2)/x**2` | $\frac{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(a*x**2 + b*x**3 + c*x**4)**(3/2)/x**3` | $\frac{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `(a*x**2 + b*x**3 + c*x**4)**(3/2)/x**4` | $\frac{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}{x^{4}}$ |
| partial | parametric | `(a*x**2 + b*x**3 + c*x**4)**(3/2)/x**5` | $\frac{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}{x^{5}}$ |
| partial | parametric | `(a*x**2 + b*x**3 + c*x**4)**(3/2)/x**6` | $\frac{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}{x^{6}}$ |
| partial | parametric | `(a*x**2 + b*x**3 + c*x**4)**(3/2)/x**7` | $\frac{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}{x^{7}}$ |
| partial | parametric | `(a*x**2 + b*x**3 + c*x**4)**(3/2)/x**8` | $\frac{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}{x^{8}}$ |
| partial | parametric | `(a*x**2 + b*x**3 + c*x**4)**(3/2)/x**9` | $\frac{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}{x^{9}}$ |
| partial | parametric | `x**3/sqrt(a*x**2 + b*x**3 + c*x**4)` | $\frac{x^{3}}{\sqrt{a x^{2} + b x^{3} + c x^{4}}}$ |
| partial | parametric | `x**2/sqrt(a*x**2 + b*x**3 + c*x**4)` | $\frac{x^{2}}{\sqrt{a x^{2} + b x^{3} + c x^{4}}}$ |
| partial | parametric | `x/sqrt(a*x**2 + b*x**3 + c*x**4)` | $\frac{x}{\sqrt{a x^{2} + b x^{3} + c x^{4}}}$ |
| partial | parametric | `1/sqrt(a*x**2 + b*x**3 + c*x**4)` | $\frac{1}{\sqrt{a x^{2} + b x^{3} + c x^{4}}}$ |
| partial | parametric | `1/(x*sqrt(a*x**2 + b*x**3 + c*x**4))` | $\frac{1}{x \sqrt{a x^{2} + b x^{3} + c x^{4}}}$ |
| partial | parametric | `1/(x**2*sqrt(a*x**2 + b*x**3 + c*x**4))` | $\frac{1}{x^{2} \sqrt{a x^{2} + b x^{3} + c x^{4}}}$ |
| partial | parametric | `x**7/(a*x**2 + b*x**3 + c*x**4)**(3/2)` | $\frac{x^{7}}{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**6/(a*x**2 + b*x**3 + c*x**4)**(3/2)` | $\frac{x^{6}}{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**5/(a*x**2 + b*x**3 + c*x**4)**(3/2)` | $\frac{x^{5}}{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**4/(a*x**2 + b*x**3 + c*x**4)**(3/2)` | $\frac{x^{4}}{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | parametric | `x**3/(a*x**2 + b*x**3 + c*x**4)**(3/2)` | $\frac{x^{3}}{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a*x**2 + b*x**3 + c*x**4)**(3/2)` | $\frac{x^{2}}{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a*x**2 + b*x**3 + c*x**4)**(3/2)` | $\frac{x}{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*x**2 + b*x**3 + c*x**4)**(-3/2)` | $\frac{1}{\left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x*(a*x**2 + b*x**3 + c*x**4)**(3/2))` | $\frac{1}{x \left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**2*(a*x**2 + b*x**3 + c*x**4)**(3/2))` | $\frac{1}{x^{2} \left(a x^{2} + b x^{3} + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/sqrt(a*x + b*x**3 + c*x**5)` | $\frac{x}{\sqrt{a x + b x^{3} + c x^{5}}}$ |
| partial | parametric | `x**(3/2)*sqrt(a*x + b*x**3 + c*x**5)` | $x^{\frac{3}{2}} \sqrt{a x + b x^{3} + c x^{5}}$ |
| partial | parametric | `sqrt(x)*sqrt(a*x + b*x**3 + c*x**5)` | $\sqrt{x} \sqrt{a x + b x^{3} + c x^{5}}$ |
| partial | parametric | `sqrt(a*x + b*x**3 + c*x**5)/sqrt(x)` | $\frac{\sqrt{a x + b x^{3} + c x^{5}}}{\sqrt{x}}$ |
| partial | parametric | `sqrt(a*x + b*x**3 + c*x**5)/x**(3/2)` | $\frac{\sqrt{a x + b x^{3} + c x^{5}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `x**(3/2)*(a*x + b*x**3 + c*x**5)**(3/2)` | $x^{\frac{3}{2}} \left(a x + b x^{3} + c x^{5}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(x)*(a*x + b*x**3 + c*x**5)**(3/2)` | $\sqrt{x} \left(a x + b x^{3} + c x^{5}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(a*x + b*x**3 + c*x**5)**(3/2)/sqrt(x)` | $\frac{\left(a x + b x^{3} + c x^{5}\right)^{\frac{3}{2}}}{\sqrt{x}}$ |
| partial | parametric | `(a*x + b*x**3 + c*x**5)**(3/2)/x**(3/2)` | $\frac{\left(a x + b x^{3} + c x^{5}\right)^{\frac{3}{2}}}{x^{\frac{3}{2}}}$ |
| partial | parametric | `x**(3/2)/sqrt(a*x + b*x**3 + c*x**5)` | $\frac{x^{\frac{3}{2}}}{\sqrt{a x + b x^{3} + c x^{5}}}$ |
| partial | parametric | `sqrt(x)/sqrt(a*x + b*x**3 + c*x**5)` | $\frac{\sqrt{x}}{\sqrt{a x + b x^{3} + c x^{5}}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(a*x + b*x**3 + c*x**5))` | $\frac{1}{\sqrt{x} \sqrt{a x + b x^{3} + c x^{5}}}$ |
| partial | parametric | `1/(x**(3/2)*sqrt(a*x + b*x**3 + c*x**5))` | $\frac{1}{x^{\frac{3}{2}} \sqrt{a x + b x^{3} + c x^{5}}}$ |
| partial | parametric | `x**(3/2)/(a*x + b*x**3 + c*x**5)**(3/2)` | $\frac{x^{\frac{3}{2}}}{\left(a x + b x^{3} + c x^{5}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(x)/(a*x + b*x**3 + c*x**5)**(3/2)` | $\frac{\sqrt{x}}{\left(a x + b x^{3} + c x^{5}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(sqrt(x)*(a*x + b*x**3 + c*x**5)**(3/2))` | $\frac{1}{\sqrt{x} \left(a x + b x^{3} + c x^{5}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/(x**(3/2)*(a*x + b*x**3 + c*x**5)**(3/2))` | $\frac{1}{x^{\frac{3}{2}} \left(a x + b x^{3} + c x^{5}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(d + e*x**2)/sqrt(a*x + b*x**3 + c*x**5)` | $\frac{x \left(d + e x^{2}\right)}{\sqrt{a x + b x^{3} + c x^{5}}}$ |
| partial | concrete | `1/sqrt(x**6 - 3*x**4 + 3*x**2)` | $\frac{1}{\sqrt{x^{6} - 3 x^{4} + 3 x^{2}}}$ |
| partial | concrete | `1/sqrt(x**2*(x**4 - 3*x**2 + 3))` | $\frac{1}{\sqrt{x^{2} \left(x^{4} - 3 x^{2} + 3\right)}}$ |
| partial | concrete | `1/sqrt(1 - (1 - x**2)**3)` | $\frac{1}{\sqrt{1 - \left(1 - x^{2}\right)^{3}}}$ |
| partial | concrete | `sqrt(x**6 - 3*x**4 + 3*x**2)` | $\sqrt{x^{6} - 3 x^{4} + 3 x^{2}}$ |
| partial | concrete | `sqrt(x**2*(x**4 - 3*x**2 + 3))` | $\sqrt{x^{2} \left(x^{4} - 3 x^{2} + 3\right)}$ |
| partial | concrete | `sqrt(1 - (1 - x**2)**3)` | $\sqrt{1 - \left(1 - x^{2}\right)^{3}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x + c*x**2))` | $\frac{1}{x \sqrt{a + b x + c x^{2}}}$ |
| partial | parametric | `1/sqrt(x**2*(a + b*x + c*x**2))` | $\frac{1}{\sqrt{x^{2} \left(a + b x + c x^{2}\right)}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(x*(a + b*x + c*x**2)))` | $\frac{1}{\sqrt{x} \sqrt{x \left(a + b x + c x^{2}\right)}}$ |
| partial | parametric | `sqrt(x)/sqrt(x**3*(a + b*x + c*x**2))` | $\frac{\sqrt{x}}{\sqrt{x^{3} \left(a + b x + c x^{2}\right)}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x**2 + c*x**4))` | $\frac{1}{x \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | parametric | `1/sqrt(x**2*(a + b*x**2 + c*x**4))` | $\frac{1}{\sqrt{x^{2} \left(a + b x^{2} + c x^{4}\right)}}$ |
| partial | parametric | `1/(sqrt(x)*sqrt(x*(a + b*x**2 + c*x**4)))` | $\frac{1}{\sqrt{x} \sqrt{x \left(a + b x^{2} + c x^{4}\right)}}$ |
| partial | parametric | `sqrt(x)/sqrt(x**3*(a + b*x**2 + c*x**4))` | $\frac{\sqrt{x}}{\sqrt{x^{3} \left(a + b x^{2} + c x^{4}\right)}}$ |
| partial | concrete | `1/(x*sqrt(x**4 - 3*x**2 + 3))` | $\frac{1}{x \sqrt{x^{4} - 3 x^{2} + 3}}$ |
| partial | concrete | `1/sqrt(x**2*(x**4 - 3*x**2 + 3))` | $\frac{1}{\sqrt{x^{2} \left(x^{4} - 3 x^{2} + 3\right)}}$ |
| partial | concrete | `1/(sqrt(x)*sqrt(x*(x**2 - 3*x + 3)))` | $\frac{1}{\sqrt{x} \sqrt{x \left(x^{2} - 3 x + 3\right)}}$ |
