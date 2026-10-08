# 1.3 Miscellaneous algebraic

All attempted radical cases from this part of the Rubi corpus, run through `risch_integrate(f, x, algebraic=True)` (sympy branch `risch-algebraic`).  **SOLVED-NEW** means solved here but not by sympy's non-risch `integrate()`; SOLVED-both means both solve it.  726 cases: partial 566 (78%), NIE 64 (9%), SOLVED-both 49 (7%), SOLVED-NEW 36 (5%), timeout 11 (2%).

| Status | Kind | SymPy expression | Math |
|---|---|---|---|
| partial | concrete | `x**2/sqrt(1 - (x + 1)**2)` | $\frac{x^{2}}{\sqrt{1 - \left(x + 1\right)^{2}}}$ |
| partial | parametric | `x**2/sqrt(1 - (a + b*x)**2)` | $\frac{x^{2}}{\sqrt{1 - \left(a + b x\right)^{2}}}$ |
| partial | parametric | `x**2/sqrt((a + b*x)**2 + 1)` | $\frac{x^{2}}{\sqrt{\left(a + b x\right)^{2} + 1}}$ |
| partial | concrete | `1/((x + 2**(2/3))*sqrt(x**3 + 1))` | $\frac{1}{\left(x + 2^{\frac{2}{3}}\right) \sqrt{x^{3} + 1}}$ |
| partial | concrete | `1/(sqrt(1 - x**3)*(-x + 2**(2/3)))` | $\frac{1}{\sqrt{1 - x^{3}} \left(- x + 2^{\frac{2}{3}}\right)}$ |
| partial | concrete | `1/((-x + 2**(2/3))*sqrt(x**3 - 1))` | $\frac{1}{\left(- x + 2^{\frac{2}{3}}\right) \sqrt{x^{3} - 1}}$ |
| partial | concrete | `1/((x + 2**(2/3))*sqrt(-x**3 - 1))` | $\frac{1}{\left(x + 2^{\frac{2}{3}}\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `1/(sqrt(a + b*x**3)*(2**(2/3)*a**(1/3) + b**(1/3)*x))` | $\frac{1}{\sqrt{a + b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `1/(sqrt(a - b*x**3)*(2**(2/3)*a**(1/3) - b**(1/3)*x))` | $\frac{1}{\sqrt{a - b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `1/(sqrt(-a + b*x**3)*(2**(2/3)*a**(1/3) - b**(1/3)*x))` | $\frac{1}{\sqrt{- a + b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `1/(sqrt(-a - b*x**3)*(2**(2/3)*a**(1/3) + b**(1/3)*x))` | $\frac{1}{\sqrt{- a - b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `1/((c + d*x)*sqrt(c**3 + 4*d**3*x**3))` | $\frac{1}{\left(c + d x\right) \sqrt{c^{3} + 4 d^{3} x^{3}}}$ |
| partial | concrete | `1/(sqrt(x**3 + 1)*(x + 1 + sqrt(3)))` | $\frac{1}{\sqrt{x^{3} + 1} \left(x + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `1/(sqrt(1 - x**3)*(-x + 1 + sqrt(3)))` | $\frac{1}{\sqrt{1 - x^{3}} \left(- x + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `1/(sqrt(x**3 - 1)*(-x + 1 + sqrt(3)))` | $\frac{1}{\sqrt{x^{3} - 1} \left(- x + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `1/(sqrt(-x**3 - 1)*(x + 1 + sqrt(3)))` | $\frac{1}{\sqrt{- x^{3} - 1} \left(x + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `1/((x + 3)*sqrt(x**3 + 1))` | $\frac{1}{\left(x + 3\right) \sqrt{x^{3} + 1}}$ |
| partial | concrete | `1/(sqrt(1 - x**3)*(x + 3))` | $\frac{1}{\sqrt{1 - x^{3}} \left(x + 3\right)}$ |
| partial | concrete | `1/((x + 3)*sqrt(x**3 - 1))` | $\frac{1}{\left(x + 3\right) \sqrt{x^{3} - 1}}$ |
| partial | concrete | `1/((x + 3)*sqrt(-x**3 - 1))` | $\frac{1}{\left(x + 3\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `1/((c + d*x)*(-c**3 + d**3*x**3)**(1/3))` | $\frac{1}{\left(c + d x\right) \sqrt[3]{- c^{3} + d^{3} x^{3}}}$ |
| partial | parametric | `1/((c + d*x)*(2*c**3 + d**3*x**3)**(1/3))` | $\frac{1}{\left(c + d x\right) \sqrt[3]{2 c^{3} + d^{3} x^{3}}}$ |
| partial | concrete | `(-2*x + 2**(2/3))/((x + 2**(2/3))*sqrt(x**3 + 1))` | $\frac{- 2 x + 2^{\frac{2}{3}}}{\left(x + 2^{\frac{2}{3}}\right) \sqrt{x^{3} + 1}}$ |
| partial | concrete | `(2*x + 2**(2/3))/(sqrt(1 - x**3)*(-x + 2**(2/3)))` | $\frac{2 x + 2^{\frac{2}{3}}}{\sqrt{1 - x^{3}} \left(- x + 2^{\frac{2}{3}}\right)}$ |
| partial | concrete | `(2*x + 2**(2/3))/((-x + 2**(2/3))*sqrt(x**3 - 1))` | $\frac{2 x + 2^{\frac{2}{3}}}{\left(- x + 2^{\frac{2}{3}}\right) \sqrt{x^{3} - 1}}$ |
| partial | concrete | `(-2*x + 2**(2/3))/((x + 2**(2/3))*sqrt(-x**3 - 1))` | $\frac{- 2 x + 2^{\frac{2}{3}}}{\left(x + 2^{\frac{2}{3}}\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(2**(2/3)*a**(1/3) - 2*b**(1/3)*x)/(sqrt(a + b*x**3)*(2**(2/3)*a**(1/3) + b**(1/3)*x))` | $\frac{2^{\frac{2}{3}} \sqrt[3]{a} - 2 \sqrt[3]{b} x}{\sqrt{a + b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(2**(2/3)*a**(1/3) + 2*b**(1/3)*x)/(sqrt(a - b*x**3)*(2**(2/3)*a**(1/3) - b**(1/3)*x))` | $\frac{2^{\frac{2}{3}} \sqrt[3]{a} + 2 \sqrt[3]{b} x}{\sqrt{a - b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(2**(2/3)*a**(1/3) + 2*b**(1/3)*x)/(sqrt(-a + b*x**3)*(2**(2/3)*a**(1/3) - b**(1/3)*x))` | $\frac{2^{\frac{2}{3}} \sqrt[3]{a} + 2 \sqrt[3]{b} x}{\sqrt{- a + b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(2**(2/3)*a**(1/3) - 2*b**(1/3)*x)/(sqrt(-a - b*x**3)*(2**(2/3)*a**(1/3) + b**(1/3)*x))` | $\frac{2^{\frac{2}{3}} \sqrt[3]{a} - 2 \sqrt[3]{b} x}{\sqrt{- a - b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(c - 2*d*x)/((c + d*x)*sqrt(c**3 + 4*d**3*x**3))` | $\frac{c - 2 d x}{\left(c + d x\right) \sqrt{c^{3} + 4 d^{3} x^{3}}}$ |
| partial | concrete | `(3*x + 2)/((x + 2**(2/3))*sqrt(x**3 + 1))` | $\frac{3 x + 2}{\left(x + 2^{\frac{2}{3}}\right) \sqrt{x^{3} + 1}}$ |
| partial | concrete | `(3*x + 2)/(sqrt(1 - x**3)*(-x + 2**(2/3)))` | $\frac{3 x + 2}{\sqrt{1 - x^{3}} \left(- x + 2^{\frac{2}{3}}\right)}$ |
| partial | concrete | `(3*x + 2)/((-x + 2**(2/3))*sqrt(x**3 - 1))` | $\frac{3 x + 2}{\left(- x + 2^{\frac{2}{3}}\right) \sqrt{x^{3} - 1}}$ |
| partial | concrete | `(3*x + 2)/((x + 2**(2/3))*sqrt(-x**3 - 1))` | $\frac{3 x + 2}{\left(x + 2^{\frac{2}{3}}\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(e + f*x)/((x + 2**(2/3))*sqrt(x**3 + 1))` | $\frac{e + f x}{\left(x + 2^{\frac{2}{3}}\right) \sqrt{x^{3} + 1}}$ |
| partial | parametric | `(e + f*x)/(sqrt(1 - x**3)*(-x + 2**(2/3)))` | $\frac{e + f x}{\sqrt{1 - x^{3}} \left(- x + 2^{\frac{2}{3}}\right)}$ |
| partial | parametric | `(e + f*x)/((-x + 2**(2/3))*sqrt(x**3 - 1))` | $\frac{e + f x}{\left(- x + 2^{\frac{2}{3}}\right) \sqrt{x^{3} - 1}}$ |
| partial | parametric | `(e + f*x)/((x + 2**(2/3))*sqrt(-x**3 - 1))` | $\frac{e + f x}{\left(x + 2^{\frac{2}{3}}\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(e + f*x)/(sqrt(a + b*x**3)*(2**(2/3)*a**(1/3) + b**(1/3)*x))` | $\frac{e + f x}{\sqrt{a + b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(e + f*x)/(sqrt(a - b*x**3)*(2**(2/3)*a**(1/3) - b**(1/3)*x))` | $\frac{e + f x}{\sqrt{a - b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(e + f*x)/(sqrt(-a + b*x**3)*(2**(2/3)*a**(1/3) - b**(1/3)*x))` | $\frac{e + f x}{\sqrt{- a + b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(e + f*x)/(sqrt(-a - b*x**3)*(2**(2/3)*a**(1/3) + b**(1/3)*x))` | $\frac{e + f x}{\sqrt{- a - b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(e + f*x)/((c + d*x)*sqrt(c**3 + 4*d**3*x**3))` | $\frac{e + f x}{\left(c + d x\right) \sqrt{c^{3} + 4 d^{3} x^{3}}}$ |
| partial | concrete | `x/((x + 2**(2/3))*sqrt(x**3 + 1))` | $\frac{x}{\left(x + 2^{\frac{2}{3}}\right) \sqrt{x^{3} + 1}}$ |
| partial | concrete | `x/(sqrt(1 - x**3)*(-x + 2**(2/3)))` | $\frac{x}{\sqrt{1 - x^{3}} \left(- x + 2^{\frac{2}{3}}\right)}$ |
| partial | concrete | `x/((-x + 2**(2/3))*sqrt(x**3 - 1))` | $\frac{x}{\left(- x + 2^{\frac{2}{3}}\right) \sqrt{x^{3} - 1}}$ |
| partial | concrete | `x/((x + 2**(2/3))*sqrt(-x**3 - 1))` | $\frac{x}{\left(x + 2^{\frac{2}{3}}\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `x/(sqrt(a + b*x**3)*(2**(2/3)*a**(1/3) + b**(1/3)*x))` | $\frac{x}{\sqrt{a + b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `x/(sqrt(a - b*x**3)*(2**(2/3)*a**(1/3) - b**(1/3)*x))` | $\frac{x}{\sqrt{a - b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `x/(sqrt(-a + b*x**3)*(2**(2/3)*a**(1/3) - b**(1/3)*x))` | $\frac{x}{\sqrt{- a + b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `x/(sqrt(-a - b*x**3)*(2**(2/3)*a**(1/3) + b**(1/3)*x))` | $\frac{x}{\sqrt{- a - b x^{3}} \left(2^{\frac{2}{3}} \sqrt[3]{a} + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `x/((c + d*x)*sqrt(c**3 + 4*d**3*x**3))` | $\frac{x}{\left(c + d x\right) \sqrt{c^{3} + 4 d^{3} x^{3}}}$ |
| partial | concrete | `(x + 1)/((2 - x)*sqrt(x**3 + 1))` | $\frac{x + 1}{\left(2 - x\right) \sqrt{x^{3} + 1}}$ |
| partial | concrete | `(1 - x)/(sqrt(1 - x**3)*(x + 2))` | $\frac{1 - x}{\sqrt{1 - x^{3}} \left(x + 2\right)}$ |
| partial | concrete | `(1 - x)/((x + 2)*sqrt(x**3 - 1))` | $\frac{1 - x}{\left(x + 2\right) \sqrt{x^{3} - 1}}$ |
| partial | concrete | `(x + 1)/((2 - x)*sqrt(-x**3 - 1))` | $\frac{x + 1}{\left(2 - x\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(a**(1/3) + b**(1/3)*x)/((2*a**(1/3) - b**(1/3)*x)*sqrt(a + b*x**3))` | $\frac{\sqrt[3]{a} + \sqrt[3]{b} x}{\left(2 \sqrt[3]{a} - \sqrt[3]{b} x\right) \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(a**(1/3) - b**(1/3)*x)/((2*a**(1/3) + b**(1/3)*x)*sqrt(a - b*x**3))` | $\frac{\sqrt[3]{a} - \sqrt[3]{b} x}{\left(2 \sqrt[3]{a} + \sqrt[3]{b} x\right) \sqrt{a - b x^{3}}}$ |
| partial | parametric | `(a**(1/3) - b**(1/3)*x)/((2*a**(1/3) + b**(1/3)*x)*sqrt(-a + b*x**3))` | $\frac{\sqrt[3]{a} - \sqrt[3]{b} x}{\left(2 \sqrt[3]{a} + \sqrt[3]{b} x\right) \sqrt{- a + b x^{3}}}$ |
| partial | parametric | `(a**(1/3) + b**(1/3)*x)/((2*a**(1/3) - b**(1/3)*x)*sqrt(-a - b*x**3))` | $\frac{\sqrt[3]{a} + \sqrt[3]{b} x}{\left(2 \sqrt[3]{a} - \sqrt[3]{b} x\right) \sqrt{- a - b x^{3}}}$ |
| partial | parametric | `(c - 2*d*x)/((c + d*x)*sqrt(c**3 - 8*d**3*x**3))` | $\frac{c - 2 d x}{\left(c + d x\right) \sqrt{c^{3} - 8 d^{3} x^{3}}}$ |
| partial | parametric | `(e + f*x)/((2 - x)*sqrt(x**3 + 1))` | $\frac{e + f x}{\left(2 - x\right) \sqrt{x^{3} + 1}}$ |
| partial | parametric | `(e + f*x)/(sqrt(1 - x**3)*(x + 2))` | $\frac{e + f x}{\sqrt{1 - x^{3}} \left(x + 2\right)}$ |
| partial | parametric | `(e + f*x)/((x + 2)*sqrt(x**3 - 1))` | $\frac{e + f x}{\left(x + 2\right) \sqrt{x^{3} - 1}}$ |
| partial | parametric | `(e + f*x)/((2 - x)*sqrt(-x**3 - 1))` | $\frac{e + f x}{\left(2 - x\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(e + f*x)/((2*a**(1/3) - b**(1/3)*x)*sqrt(a + b*x**3))` | $\frac{e + f x}{\left(2 \sqrt[3]{a} - \sqrt[3]{b} x\right) \sqrt{a + b x^{3}}}$ |
| partial | parametric | `(e + f*x)/((2*a**(1/3) + b**(1/3)*x)*sqrt(a - b*x**3))` | $\frac{e + f x}{\left(2 \sqrt[3]{a} + \sqrt[3]{b} x\right) \sqrt{a - b x^{3}}}$ |
| partial | parametric | `(e + f*x)/((2*a**(1/3) + b**(1/3)*x)*sqrt(-a + b*x**3))` | $\frac{e + f x}{\left(2 \sqrt[3]{a} + \sqrt[3]{b} x\right) \sqrt{- a + b x^{3}}}$ |
| partial | parametric | `(e + f*x)/((2*a**(1/3) - b**(1/3)*x)*sqrt(-a - b*x**3))` | $\frac{e + f x}{\left(2 \sqrt[3]{a} - \sqrt[3]{b} x\right) \sqrt{- a - b x^{3}}}$ |
| partial | parametric | `(e + f*x)/((c + d*x)*sqrt(c**3 - 8*d**3*x**3))` | $\frac{e + f x}{\left(c + d x\right) \sqrt{c^{3} - 8 d^{3} x^{3}}}$ |
| partial | concrete | `x/((2 - x)*sqrt(x**3 + 1))` | $\frac{x}{\left(2 - x\right) \sqrt{x^{3} + 1}}$ |
| partial | concrete | `x/(sqrt(1 - x**3)*(x + 2))` | $\frac{x}{\sqrt{1 - x^{3}} \left(x + 2\right)}$ |
| partial | concrete | `x/((x + 2)*sqrt(x**3 - 1))` | $\frac{x}{\left(x + 2\right) \sqrt{x^{3} - 1}}$ |
| partial | concrete | `x/((2 - x)*sqrt(-x**3 - 1))` | $\frac{x}{\left(2 - x\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `x/((2*a**(1/3) - b**(1/3)*x)*sqrt(a + b*x**3))` | $\frac{x}{\left(2 \sqrt[3]{a} - \sqrt[3]{b} x\right) \sqrt{a + b x^{3}}}$ |
| partial | parametric | `x/((2*a**(1/3) + b**(1/3)*x)*sqrt(a - b*x**3))` | $\frac{x}{\left(2 \sqrt[3]{a} + \sqrt[3]{b} x\right) \sqrt{a - b x^{3}}}$ |
| partial | parametric | `x/((2*a**(1/3) + b**(1/3)*x)*sqrt(-a + b*x**3))` | $\frac{x}{\left(2 \sqrt[3]{a} + \sqrt[3]{b} x\right) \sqrt{- a + b x^{3}}}$ |
| partial | parametric | `x/((2*a**(1/3) - b**(1/3)*x)*sqrt(-a - b*x**3))` | $\frac{x}{\left(2 \sqrt[3]{a} - \sqrt[3]{b} x\right) \sqrt{- a - b x^{3}}}$ |
| partial | parametric | `x/((c + d*x)*sqrt(c**3 - 8*d**3*x**3))` | $\frac{x}{\left(c + d x\right) \sqrt{c^{3} - 8 d^{3} x^{3}}}$ |
| partial | concrete | `(x + 1 + sqrt(3))/(sqrt(x**3 + 1)*(x - sqrt(3) + 1))` | $\frac{x + 1 + \sqrt{3}}{\sqrt{x^{3} + 1} \left(x - \sqrt{3} + 1\right)}$ |
| partial | concrete | `(-x + 1 + sqrt(3))/(sqrt(1 - x**3)*(-x - sqrt(3) + 1))` | $\frac{- x + 1 + \sqrt{3}}{\sqrt{1 - x^{3}} \left(- x - \sqrt{3} + 1\right)}$ |
| partial | concrete | `(-x + 1 + sqrt(3))/(sqrt(x**3 - 1)*(-x - sqrt(3) + 1))` | $\frac{- x + 1 + \sqrt{3}}{\sqrt{x^{3} - 1} \left(- x - \sqrt{3} + 1\right)}$ |
| partial | concrete | `(x + 1 + sqrt(3))/(sqrt(-x**3 - 1)*(x - sqrt(3) + 1))` | $\frac{x + 1 + \sqrt{3}}{\sqrt{- x^{3} - 1} \left(x - \sqrt{3} + 1\right)}$ |
| partial | parametric | `(a**(1/3)*(1 + sqrt(3)) + b**(1/3)*x)/(sqrt(a + b*x**3)*(a**(1/3)*(1 - sqrt(3)) + b**(1/3)*x))` | $\frac{\sqrt[3]{a} \left(1 + \sqrt{3}\right) + \sqrt[3]{b} x}{\sqrt{a + b x^{3}} \left(\sqrt[3]{a} \left(1 - \sqrt{3}\right) + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(a**(1/3)*(1 + sqrt(3)) - b**(1/3)*x)/(sqrt(a - b*x**3)*(a**(1/3)*(1 - sqrt(3)) - b**(1/3)*x))` | $\frac{\sqrt[3]{a} \left(1 + \sqrt{3}\right) - \sqrt[3]{b} x}{\sqrt{a - b x^{3}} \left(\sqrt[3]{a} \left(1 - \sqrt{3}\right) - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(a**(1/3)*(1 + sqrt(3)) - b**(1/3)*x)/(sqrt(-a + b*x**3)*(a**(1/3)*(1 - sqrt(3)) - b**(1/3)*x))` | $\frac{\sqrt[3]{a} \left(1 + \sqrt{3}\right) - \sqrt[3]{b} x}{\sqrt{- a + b x^{3}} \left(\sqrt[3]{a} \left(1 - \sqrt{3}\right) - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(a**(1/3)*(1 + sqrt(3)) + b**(1/3)*x)/(sqrt(-a - b*x**3)*(a**(1/3)*(1 - sqrt(3)) + b**(1/3)*x))` | $\frac{\sqrt[3]{a} \left(1 + \sqrt{3}\right) + \sqrt[3]{b} x}{\sqrt{- a - b x^{3}} \left(\sqrt[3]{a} \left(1 - \sqrt{3}\right) + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(x*(b/a)**(1/3) + 1 + sqrt(3))/(sqrt(a + b*x**3)*(x*(b/a)**(1/3) - sqrt(3) + 1))` | $\frac{x \sqrt[3]{\frac{b}{a}} + 1 + \sqrt{3}}{\sqrt{a + b x^{3}} \left(x \sqrt[3]{\frac{b}{a}} - \sqrt{3} + 1\right)}$ |
| partial | parametric | `(-x*(b/a)**(1/3) + 1 + sqrt(3))/(sqrt(a - b*x**3)*(-x*(b/a)**(1/3) - sqrt(3) + 1))` | $\frac{- x \sqrt[3]{\frac{b}{a}} + 1 + \sqrt{3}}{\sqrt{a - b x^{3}} \left(- x \sqrt[3]{\frac{b}{a}} - \sqrt{3} + 1\right)}$ |
| partial | parametric | `(-x*(b/a)**(1/3) + 1 + sqrt(3))/(sqrt(-a + b*x**3)*(-x*(b/a)**(1/3) - sqrt(3) + 1))` | $\frac{- x \sqrt[3]{\frac{b}{a}} + 1 + \sqrt{3}}{\sqrt{- a + b x^{3}} \left(- x \sqrt[3]{\frac{b}{a}} - \sqrt{3} + 1\right)}$ |
| partial | parametric | `(x*(b/a)**(1/3) + 1 + sqrt(3))/(sqrt(-a - b*x**3)*(x*(b/a)**(1/3) - sqrt(3) + 1))` | $\frac{x \sqrt[3]{\frac{b}{a}} + 1 + \sqrt{3}}{\sqrt{- a - b x^{3}} \left(x \sqrt[3]{\frac{b}{a}} - \sqrt{3} + 1\right)}$ |
| partial | concrete | `(x - sqrt(3) + 1)/(sqrt(x**3 + 1)*(x + 1 + sqrt(3)))` | $\frac{x - \sqrt{3} + 1}{\sqrt{x^{3} + 1} \left(x + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `(-x - sqrt(3) + 1)/(sqrt(1 - x**3)*(-x + 1 + sqrt(3)))` | $\frac{- x - \sqrt{3} + 1}{\sqrt{1 - x^{3}} \left(- x + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `(-x - sqrt(3) + 1)/(sqrt(x**3 - 1)*(-x + 1 + sqrt(3)))` | $\frac{- x - \sqrt{3} + 1}{\sqrt{x^{3} - 1} \left(- x + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `(x - sqrt(3) + 1)/(sqrt(-x**3 - 1)*(x + 1 + sqrt(3)))` | $\frac{x - \sqrt{3} + 1}{\sqrt{- x^{3} - 1} \left(x + 1 + \sqrt{3}\right)}$ |
| partial | parametric | `(a**(1/3)*(1 - sqrt(3)) + b**(1/3)*x)/(sqrt(a + b*x**3)*(a**(1/3)*(1 + sqrt(3)) + b**(1/3)*x))` | $\frac{\sqrt[3]{a} \left(1 - \sqrt{3}\right) + \sqrt[3]{b} x}{\sqrt{a + b x^{3}} \left(\sqrt[3]{a} \left(1 + \sqrt{3}\right) + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(a**(1/3)*(1 - sqrt(3)) - b**(1/3)*x)/(sqrt(a - b*x**3)*(a**(1/3)*(1 + sqrt(3)) - b**(1/3)*x))` | $\frac{\sqrt[3]{a} \left(1 - \sqrt{3}\right) - \sqrt[3]{b} x}{\sqrt{a - b x^{3}} \left(\sqrt[3]{a} \left(1 + \sqrt{3}\right) - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(a**(1/3)*(1 - sqrt(3)) - b**(1/3)*x)/(sqrt(-a + b*x**3)*(a**(1/3)*(1 + sqrt(3)) - b**(1/3)*x))` | $\frac{\sqrt[3]{a} \left(1 - \sqrt{3}\right) - \sqrt[3]{b} x}{\sqrt{- a + b x^{3}} \left(\sqrt[3]{a} \left(1 + \sqrt{3}\right) - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(a**(1/3)*(1 - sqrt(3)) + b**(1/3)*x)/(sqrt(-a - b*x**3)*(a**(1/3)*(1 + sqrt(3)) + b**(1/3)*x))` | $\frac{\sqrt[3]{a} \left(1 - \sqrt{3}\right) + \sqrt[3]{b} x}{\sqrt{- a - b x^{3}} \left(\sqrt[3]{a} \left(1 + \sqrt{3}\right) + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(x*(b/a)**(1/3) - sqrt(3) + 1)/(sqrt(a + b*x**3)*(x*(b/a)**(1/3) + 1 + sqrt(3)))` | $\frac{x \sqrt[3]{\frac{b}{a}} - \sqrt{3} + 1}{\sqrt{a + b x^{3}} \left(x \sqrt[3]{\frac{b}{a}} + 1 + \sqrt{3}\right)}$ |
| partial | parametric | `(-x*(b/a)**(1/3) - sqrt(3) + 1)/(sqrt(a - b*x**3)*(-x*(b/a)**(1/3) + 1 + sqrt(3)))` | $\frac{- x \sqrt[3]{\frac{b}{a}} - \sqrt{3} + 1}{\sqrt{a - b x^{3}} \left(- x \sqrt[3]{\frac{b}{a}} + 1 + \sqrt{3}\right)}$ |
| partial | parametric | `(-x*(b/a)**(1/3) - sqrt(3) + 1)/(sqrt(-a + b*x**3)*(-x*(b/a)**(1/3) + 1 + sqrt(3)))` | $\frac{- x \sqrt[3]{\frac{b}{a}} - \sqrt{3} + 1}{\sqrt{- a + b x^{3}} \left(- x \sqrt[3]{\frac{b}{a}} + 1 + \sqrt{3}\right)}$ |
| partial | parametric | `(x*(b/a)**(1/3) - sqrt(3) + 1)/(sqrt(-a - b*x**3)*(x*(b/a)**(1/3) + 1 + sqrt(3)))` | $\frac{x \sqrt[3]{\frac{b}{a}} - \sqrt{3} + 1}{\sqrt{- a - b x^{3}} \left(x \sqrt[3]{\frac{b}{a}} + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `(x + 1)/(sqrt(x**3 + 1)*(x + 1 + sqrt(3)))` | $\frac{x + 1}{\sqrt{x^{3} + 1} \left(x + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `(x + 1)/(sqrt(x**3 + 1)*(x - sqrt(3) + 1))` | $\frac{x + 1}{\sqrt{x^{3} + 1} \left(x - \sqrt{3} + 1\right)}$ |
| partial | parametric | `(e + f*x)/(sqrt(x**3 + 1)*(x + 1 + sqrt(3)))` | $\frac{e + f x}{\sqrt{x^{3} + 1} \left(x + 1 + \sqrt{3}\right)}$ |
| partial | parametric | `(e + f*x)/(sqrt(1 - x**3)*(-x + 1 + sqrt(3)))` | $\frac{e + f x}{\sqrt{1 - x^{3}} \left(- x + 1 + \sqrt{3}\right)}$ |
| partial | parametric | `(e + f*x)/(sqrt(x**3 - 1)*(-x + 1 + sqrt(3)))` | $\frac{e + f x}{\sqrt{x^{3} - 1} \left(- x + 1 + \sqrt{3}\right)}$ |
| partial | parametric | `(e + f*x)/(sqrt(-x**3 - 1)*(x + 1 + sqrt(3)))` | $\frac{e + f x}{\sqrt{- x^{3} - 1} \left(x + 1 + \sqrt{3}\right)}$ |
| partial | parametric | `(e + f*x)/(sqrt(a + b*x**3)*(a**(1/3)*(1 - sqrt(3)) + b**(1/3)*x))` | $\frac{e + f x}{\sqrt{a + b x^{3}} \left(\sqrt[3]{a} \left(1 - \sqrt{3}\right) + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(e + f*x)/(sqrt(a - b*x**3)*(a**(1/3)*(1 - sqrt(3)) - b**(1/3)*x))` | $\frac{e + f x}{\sqrt{a - b x^{3}} \left(\sqrt[3]{a} \left(1 - \sqrt{3}\right) - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(e + f*x)/(sqrt(-a + b*x**3)*(a**(1/3)*(1 - sqrt(3)) - b**(1/3)*x))` | $\frac{e + f x}{\sqrt{- a + b x^{3}} \left(\sqrt[3]{a} \left(1 - \sqrt{3}\right) - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(e + f*x)/(sqrt(-a - b*x**3)*(a**(1/3)*(1 - sqrt(3)) + b**(1/3)*x))` | $\frac{e + f x}{\sqrt{- a - b x^{3}} \left(\sqrt[3]{a} \left(1 - \sqrt{3}\right) + \sqrt[3]{b} x\right)}$ |
| partial | concrete | `x/(sqrt(x**3 + 1)*(x + 1 + sqrt(3)))` | $\frac{x}{\sqrt{x^{3} + 1} \left(x + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `x/(sqrt(1 - x**3)*(-x + 1 + sqrt(3)))` | $\frac{x}{\sqrt{1 - x^{3}} \left(- x + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `x/(sqrt(x**3 - 1)*(-x + 1 + sqrt(3)))` | $\frac{x}{\sqrt{x^{3} - 1} \left(- x + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `x/(sqrt(-x**3 - 1)*(x + 1 + sqrt(3)))` | $\frac{x}{\sqrt{- x^{3} - 1} \left(x + 1 + \sqrt{3}\right)}$ |
| partial | concrete | `x/(sqrt(x**3 + 1)*(x - sqrt(3) + 1))` | $\frac{x}{\sqrt{x^{3} + 1} \left(x - \sqrt{3} + 1\right)}$ |
| partial | parametric | `x/(sqrt(a + b*x**3)*(a**(1/3)*(1 - sqrt(3)) + b**(1/3)*x))` | $\frac{x}{\sqrt{a + b x^{3}} \left(\sqrt[3]{a} \left(1 - \sqrt{3}\right) + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `x/(sqrt(a - b*x**3)*(a**(1/3)*(1 - sqrt(3)) - b**(1/3)*x))` | $\frac{x}{\sqrt{a - b x^{3}} \left(\sqrt[3]{a} \left(1 - \sqrt{3}\right) - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `x/(sqrt(-a + b*x**3)*(a**(1/3)*(1 - sqrt(3)) - b**(1/3)*x))` | $\frac{x}{\sqrt{- a + b x^{3}} \left(\sqrt[3]{a} \left(1 - \sqrt{3}\right) - \sqrt[3]{b} x\right)}$ |
| partial | parametric | `x/(sqrt(-a - b*x**3)*(a**(1/3)*(1 - sqrt(3)) + b**(1/3)*x))` | $\frac{x}{\sqrt{- a - b x^{3}} \left(\sqrt[3]{a} \left(1 - \sqrt{3}\right) + \sqrt[3]{b} x\right)}$ |
| partial | parametric | `(x + 1 + sqrt(3))/((c + d*x)*sqrt(x**3 + 1))` | $\frac{x + 1 + \sqrt{3}}{\left(c + d x\right) \sqrt{x^{3} + 1}}$ |
| partial | parametric | `(-x + 1 + sqrt(3))/(sqrt(1 - x**3)*(c + d*x))` | $\frac{- x + 1 + \sqrt{3}}{\sqrt{1 - x^{3}} \left(c + d x\right)}$ |
| partial | parametric | `(-x + 1 + sqrt(3))/((c + d*x)*sqrt(x**3 - 1))` | $\frac{- x + 1 + \sqrt{3}}{\left(c + d x\right) \sqrt{x^{3} - 1}}$ |
| partial | parametric | `(x + 1 + sqrt(3))/((c + d*x)*sqrt(-x**3 - 1))` | $\frac{x + 1 + \sqrt{3}}{\left(c + d x\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(x - sqrt(3) + 1)/((c + d*x)*sqrt(x**3 + 1))` | $\frac{x - \sqrt{3} + 1}{\left(c + d x\right) \sqrt{x^{3} + 1}}$ |
| partial | parametric | `(-x - sqrt(3) + 1)/(sqrt(1 - x**3)*(c + d*x))` | $\frac{- x - \sqrt{3} + 1}{\sqrt{1 - x^{3}} \left(c + d x\right)}$ |
| partial | parametric | `(-x - sqrt(3) + 1)/((c + d*x)*sqrt(x**3 - 1))` | $\frac{- x - \sqrt{3} + 1}{\left(c + d x\right) \sqrt{x^{3} - 1}}$ |
| partial | parametric | `(x - sqrt(3) + 1)/((c + d*x)*sqrt(-x**3 - 1))` | $\frac{x - \sqrt{3} + 1}{\left(c + d x\right) \sqrt{- x^{3} - 1}}$ |
| partial | concrete | `(x + 1 + sqrt(3))/(x*sqrt(x**3 + 1))` | $\frac{x + 1 + \sqrt{3}}{x \sqrt{x^{3} + 1}}$ |
| partial | concrete | `(-x + 1 + sqrt(3))/(x*sqrt(1 - x**3))` | $\frac{- x + 1 + \sqrt{3}}{x \sqrt{1 - x^{3}}}$ |
| partial | concrete | `(-x + 1 + sqrt(3))/(x*sqrt(x**3 - 1))` | $\frac{- x + 1 + \sqrt{3}}{x \sqrt{x^{3} - 1}}$ |
| partial | concrete | `(x + 1 + sqrt(3))/(x*sqrt(-x**3 - 1))` | $\frac{x + 1 + \sqrt{3}}{x \sqrt{- x^{3} - 1}}$ |
| partial | concrete | `(x - sqrt(3) + 1)/(x*sqrt(x**3 + 1))` | $\frac{x - \sqrt{3} + 1}{x \sqrt{x^{3} + 1}}$ |
| partial | concrete | `(-x - sqrt(3) + 1)/(x*sqrt(1 - x**3))` | $\frac{- x - \sqrt{3} + 1}{x \sqrt{1 - x^{3}}}$ |
| partial | concrete | `(-x - sqrt(3) + 1)/(x*sqrt(x**3 - 1))` | $\frac{- x - \sqrt{3} + 1}{x \sqrt{x^{3} - 1}}$ |
| partial | concrete | `(x - sqrt(3) + 1)/(x*sqrt(-x**3 - 1))` | $\frac{x - \sqrt{3} + 1}{x \sqrt{- x^{3} - 1}}$ |
| partial | concrete | `x/((x + 3)*sqrt(x**3 + 1))` | $\frac{x}{\left(x + 3\right) \sqrt{x^{3} + 1}}$ |
| partial | concrete | `x/(sqrt(1 - x**3)*(x + 3))` | $\frac{x}{\sqrt{1 - x^{3}} \left(x + 3\right)}$ |
| partial | concrete | `x/((x + 3)*sqrt(x**3 - 1))` | $\frac{x}{\left(x + 3\right) \sqrt{x^{3} - 1}}$ |
| partial | concrete | `x/((x + 3)*sqrt(-x**3 - 1))` | $\frac{x}{\left(x + 3\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(e + f*x)/((c + d*x)*sqrt(x**3 + 1))` | $\frac{e + f x}{\left(c + d x\right) \sqrt{x^{3} + 1}}$ |
| partial | parametric | `(e + f*x)/(sqrt(1 - x**3)*(c + d*x))` | $\frac{e + f x}{\sqrt{1 - x^{3}} \left(c + d x\right)}$ |
| partial | parametric | `(e + f*x)/((c + d*x)*sqrt(x**3 - 1))` | $\frac{e + f x}{\left(c + d x\right) \sqrt{x^{3} - 1}}$ |
| partial | parametric | `(e + f*x)/((c + d*x)*sqrt(-x**3 - 1))` | $\frac{e + f x}{\left(c + d x\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(e + f*x)/(x*sqrt(x**3 + 1))` | $\frac{e + f x}{x \sqrt{x^{3} + 1}}$ |
| partial | parametric | `(e + f*x)/(x*sqrt(1 - x**3))` | $\frac{e + f x}{x \sqrt{1 - x^{3}}}$ |
| partial | parametric | `(e + f*x)/(x*sqrt(x**3 - 1))` | $\frac{e + f x}{x \sqrt{x^{3} - 1}}$ |
| partial | parametric | `(e + f*x)/(x*sqrt(-x**3 - 1))` | $\frac{e + f x}{x \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(c - d*x)/((c + d*x)*(2*c**3 + d**3*x**3)**(1/3))` | $\frac{c - d x}{\left(c + d x\right) \sqrt[3]{2 c^{3} + d^{3} x^{3}}}$ |
| partial | parametric | `(e + f*x)/((c + d*x)*(-c**3 + d**3*x**3)**(1/3))` | $\frac{e + f x}{\left(c + d x\right) \sqrt[3]{- c^{3} + d^{3} x^{3}}}$ |
| partial | parametric | `sqrt(c + d*x**3)/(a + b*x)` | $\frac{\sqrt{c + d x^{3}}}{a + b x}$ |
| partial | concrete | `(-x**2 - 2*x + 2)/((x**2 + 2)*sqrt(x**3 + 1))` | $\frac{- x^{2} - 2 x + 2}{\left(x^{2} + 2\right) \sqrt{x^{3} + 1}}$ |
| partial | concrete | `(-x**2 + 2*x + 2)/(sqrt(1 - x**3)*(x**2 + 2))` | $\frac{- x^{2} + 2 x + 2}{\sqrt{1 - x^{3}} \left(x^{2} + 2\right)}$ |
| partial | concrete | `(-x**2 + 2*x + 2)/((x**2 + 2)*sqrt(x**3 - 1))` | $\frac{- x^{2} + 2 x + 2}{\left(x^{2} + 2\right) \sqrt{x^{3} - 1}}$ |
| partial | concrete | `(-x**2 - 2*x + 2)/((x**2 + 2)*sqrt(-x**3 - 1))` | $\frac{- x^{2} - 2 x + 2}{\left(x^{2} + 2\right) \sqrt{- x^{3} - 1}}$ |
| partial | parametric | `(-x**2 - 2*x + 2)/(sqrt(x**3 + 1)*(d*x + d + x**2 + 2))` | $\frac{- x^{2} - 2 x + 2}{\sqrt{x^{3} + 1} \left(d x + d + x^{2} + 2\right)}$ |
| partial | parametric | `(-x**2 + 2*x + 2)/(sqrt(1 - x**3)*(d*x - d + x**2 + 2))` | $\frac{- x^{2} + 2 x + 2}{\sqrt{1 - x^{3}} \left(d x - d + x^{2} + 2\right)}$ |
| partial | parametric | `(-x**2 + 2*x + 2)/(sqrt(x**3 - 1)*(d*x - d + x**2 + 2))` | $\frac{- x^{2} + 2 x + 2}{\sqrt{x^{3} - 1} \left(d x - d + x^{2} + 2\right)}$ |
| partial | parametric | `(-x**2 - 2*x + 2)/(sqrt(-x**3 - 1)*(d*x + d + x**2 + 2))` | $\frac{- x^{2} - 2 x + 2}{\sqrt{- x^{3} - 1} \left(d x + d + x^{2} + 2\right)}$ |
| partial | parametric | `sqrt(a + c*x**4)*(d + e*x)**3` | $\sqrt{a + c x^{4}} \left(d + e x\right)^{3}$ |
| partial | parametric | `sqrt(a + c*x**4)*(d + e*x)**2` | $\sqrt{a + c x^{4}} \left(d + e x\right)^{2}$ |
| partial | parametric | `sqrt(a + c*x**4)*(d + e*x)` | $\sqrt{a + c x^{4}} \left(d + e x\right)$ |
| partial | parametric | `sqrt(a + c*x**4)` | $\sqrt{a + c x^{4}}$ |
| partial | parametric | `sqrt(a + c*x**4)/(d + e*x)` | $\frac{\sqrt{a + c x^{4}}}{d + e x}$ |
| partial | parametric | `sqrt(a + c*x**4)/(d + e*x)**2` | $\frac{\sqrt{a + c x^{4}}}{\left(d + e x\right)^{2}}$ |
| partial | parametric | `(d + e*x)**3/sqrt(a + c*x**4)` | $\frac{\left(d + e x\right)^{3}}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `(d + e*x)**2/sqrt(a + c*x**4)` | $\frac{\left(d + e x\right)^{2}}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `(d + e*x)/sqrt(a + c*x**4)` | $\frac{d + e x}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `1/sqrt(a + c*x**4)` | $\frac{1}{\sqrt{a + c x^{4}}}$ |
| partial | parametric | `1/(sqrt(a + c*x**4)*(d + e*x))` | $\frac{1}{\sqrt{a + c x^{4}} \left(d + e x\right)}$ |
| partial | parametric | `1/(sqrt(a + c*x**4)*(d + e*x)**2)` | $\frac{1}{\sqrt{a + c x^{4}} \left(d + e x\right)^{2}}$ |
| partial | parametric | `1/(sqrt(a + c*x**4)*(d + e*x)**3)` | $\frac{1}{\sqrt{a + c x^{4}} \left(d + e x\right)^{3}}$ |
| partial | parametric | `(d + e*x)**3/(a + c*x**4)**(3/2)` | $\frac{\left(d + e x\right)^{3}}{\left(a + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)**2/(a + c*x**4)**(3/2)` | $\frac{\left(d + e x\right)^{2}}{\left(a + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(d + e*x)/(a + c*x**4)**(3/2)` | $\frac{d + e x}{\left(a + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a + c*x**4)**(-3/2)` | $\frac{1}{\left(a + c x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `1/((a + c*x**4)**(3/2)*(d + e*x))` | $\frac{1}{\left(a + c x^{4}\right)^{\frac{3}{2}} \left(d + e x\right)}$ |
| partial | parametric | `1/(sqrt(a + b*x**4)*(c + d*x + e*x**2))` | $\frac{1}{\sqrt{a + b x^{4}} \left(c + d x + e x^{2}\right)}$ |
| partial | parametric | `sqrt(a*x**23)/sqrt(x**5 + 1)` | $\frac{\sqrt{a x^{23}}}{\sqrt{x^{5} + 1}}$ |
| partial | parametric | `sqrt(a*x**13)/sqrt(x**5 + 1)` | $\frac{\sqrt{a x^{13}}}{\sqrt{x^{5} + 1}}$ |
| partial | parametric | `sqrt(a*x**3)/sqrt(x**5 + 1)` | $\frac{\sqrt{a x^{3}}}{\sqrt{x^{5} + 1}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a/x**7)/sqrt(x**5 + 1)` | $\frac{\sqrt{\frac{a}{x^{7}}}}{\sqrt{x^{5} + 1}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a/x**17)/sqrt(x**5 + 1)` | $\frac{\sqrt{\frac{a}{x^{17}}}}{\sqrt{x^{5} + 1}}$ |
| partial | parametric | `sqrt(a*x**6)/(x*(1 - x**4))` | $\frac{\sqrt{a x^{6}}}{x \left(1 - x^{4}\right)}$ |
| partial | parametric | `sqrt(a*x**6)/(-x**5 + x)` | $\frac{\sqrt{a x^{6}}}{- x^{5} + x}$ |
| partial | parametric | `(a*x**6)**(3/2)/(x*(1 - x**4))` | $\frac{\left(a x^{6}\right)^{\frac{3}{2}}}{x \left(1 - x^{4}\right)}$ |
| partial | parametric | `1/(1 - x**4) - sqrt(a*x**6)/(x*(1 - x**4))` | $\frac{1}{1 - x^{4}} - \frac{\sqrt{a x^{6}}}{x \left(1 - x^{4}\right)}$ |
| partial | parametric | `-sqrt(a*x**6)/(-x**5 + x) + 1/(1 - x**4)` | $- \frac{\sqrt{a x^{6}}}{- x^{5} + x} + \frac{1}{1 - x^{4}}$ |
| partial | parametric | `sqrt(a*x**3)/(-x**3 + x)` | $\frac{\sqrt{a x^{3}}}{- x^{3} + x}$ |
| partial | parametric | `sqrt(a*x**4)/sqrt(x**2 + 1)` | $\frac{\sqrt{a x^{4}}}{\sqrt{x^{2} + 1}}$ |
| partial | parametric | `sqrt(a*x**3)/sqrt(x**2 + 1)` | $\frac{\sqrt{a x^{3}}}{\sqrt{x^{2} + 1}}$ |
| SOLVED-both | parametric | `sqrt(a*x**2)/sqrt(x**2 + 1)` | $\frac{\sqrt{a x^{2}}}{\sqrt{x^{2} + 1}}$ |
| partial | parametric | `sqrt(a*x)/sqrt(x**2 + 1)` | $\frac{\sqrt{a x}}{\sqrt{x^{2} + 1}}$ |
| partial | parametric | `sqrt(a/x)/sqrt(x**2 + 1)` | $\frac{\sqrt{\frac{a}{x}}}{\sqrt{x^{2} + 1}}$ |
| partial | parametric | `sqrt(a/x**2)/sqrt(x**2 + 1)` | $\frac{\sqrt{\frac{a}{x^{2}}}}{\sqrt{x^{2} + 1}}$ |
| partial | parametric | `sqrt(a/x**3)/sqrt(x**2 + 1)` | $\frac{\sqrt{\frac{a}{x^{3}}}}{\sqrt{x^{2} + 1}}$ |
| **SOLVED-NEW** | parametric | `sqrt(a/x**4)/sqrt(x**2 + 1)` | $\frac{\sqrt{\frac{a}{x^{4}}}}{\sqrt{x^{2} + 1}}$ |
| partial | parametric | `sqrt(a*x**4)/sqrt(x**3 + 1)` | $\frac{\sqrt{a x^{4}}}{\sqrt{x^{3} + 1}}$ |
| partial | parametric | `sqrt(a*x**3)/sqrt(x**3 + 1)` | $\frac{\sqrt{a x^{3}}}{\sqrt{x^{3} + 1}}$ |
| partial | parametric | `sqrt(a*x**2)/sqrt(x**3 + 1)` | $\frac{\sqrt{a x^{2}}}{\sqrt{x^{3} + 1}}$ |
| partial | parametric | `sqrt(a*x)/sqrt(x**3 + 1)` | $\frac{\sqrt{a x}}{\sqrt{x^{3} + 1}}$ |
| partial | parametric | `sqrt(a/x)/sqrt(x**3 + 1)` | $\frac{\sqrt{\frac{a}{x}}}{\sqrt{x^{3} + 1}}$ |
| partial | parametric | `sqrt(a/x**2)/sqrt(x**3 + 1)` | $\frac{\sqrt{\frac{a}{x^{2}}}}{\sqrt{x^{3} + 1}}$ |
| partial | parametric | `sqrt(a/x**3)/sqrt(x**3 + 1)` | $\frac{\sqrt{\frac{a}{x^{3}}}}{\sqrt{x^{3} + 1}}$ |
| partial | parametric | `sqrt(a/x**4)/sqrt(x**3 + 1)` | $\frac{\sqrt{\frac{a}{x^{4}}}}{\sqrt{x^{3} + 1}}$ |
| partial | parametric | `sqrt(a*x)/(sqrt(d + e*x)*sqrt(e + f*x))` | $\frac{\sqrt{a x}}{\sqrt{d + e x} \sqrt{e + f x}}$ |
| partial | parametric | `x**2/(sqrt(a + b*x) + sqrt(b*x + c))` | $\frac{x^{2}}{\sqrt{a + b x} + \sqrt{b x + c}}$ |
| partial | parametric | `x/(sqrt(a + b*x) + sqrt(b*x + c))` | $\frac{x}{\sqrt{a + b x} + \sqrt{b x + c}}$ |
| partial | parametric | `1/(sqrt(a + b*x) + sqrt(b*x + c))` | $\frac{1}{\sqrt{a + b x} + \sqrt{b x + c}}$ |
| partial | parametric | `1/(x*(sqrt(a + b*x) + sqrt(b*x + c)))` | $\frac{1}{x \left(\sqrt{a + b x} + \sqrt{b x + c}\right)}$ |
| partial | parametric | `1/(x**2*(sqrt(a + b*x) + sqrt(b*x + c)))` | $\frac{1}{x^{2} \left(\sqrt{a + b x} + \sqrt{b x + c}\right)}$ |
| partial | parametric | `x**2/(sqrt(a + b*x) + sqrt(b*x + c))**2` | $\frac{x^{2}}{\left(\sqrt{a + b x} + \sqrt{b x + c}\right)^{2}}$ |
| partial | parametric | `x/(sqrt(a + b*x) + sqrt(b*x + c))**2` | $\frac{x}{\left(\sqrt{a + b x} + \sqrt{b x + c}\right)^{2}}$ |
| partial | parametric | `1/(x*(sqrt(a + b*x) + sqrt(b*x + c))**2)` | $\frac{1}{x \left(\sqrt{a + b x} + \sqrt{b x + c}\right)^{2}}$ |
| partial | parametric | `1/(x**2*(sqrt(a + b*x) + sqrt(b*x + c))**2)` | $\frac{1}{x^{2} \left(\sqrt{a + b x} + \sqrt{b x + c}\right)^{2}}$ |
| partial | parametric | `x**2/(sqrt(a + b*x) + sqrt(b*x + c))**3` | $\frac{x^{2}}{\left(\sqrt{a + b x} + \sqrt{b x + c}\right)^{3}}$ |
| partial | parametric | `x/(sqrt(a + b*x) + sqrt(b*x + c))**3` | $\frac{x}{\left(\sqrt{a + b x} + \sqrt{b x + c}\right)^{3}}$ |
| partial | parametric | `1/(x*(sqrt(a + b*x) + sqrt(b*x + c))**3)` | $\frac{1}{x \left(\sqrt{a + b x} + \sqrt{b x + c}\right)^{3}}$ |
| partial | concrete | `1/(sqrt(x) + sqrt(x + 1))` | $\frac{1}{\sqrt{x} + \sqrt{x + 1}}$ |
| partial | concrete | `1/(sqrt(x) + sqrt(x - 1))` | $\frac{1}{\sqrt{x} + \sqrt{x - 1}}$ |
| partial | concrete | `1/(sqrt(x - 1) + sqrt(x + 1))` | $\frac{1}{\sqrt{x - 1} + \sqrt{x + 1}}$ |
| **SOLVED-NEW** | concrete | `x**3*(sqrt(1 - x) + sqrt(x + 1))**2` | $x^{3} \left(\sqrt{1 - x} + \sqrt{x + 1}\right)^{2}$ |
| partial | concrete | `x**2*(sqrt(1 - x) + sqrt(x + 1))**2` | $x^{2} \left(\sqrt{1 - x} + \sqrt{x + 1}\right)^{2}$ |
| **SOLVED-NEW** | concrete | `x*(sqrt(1 - x) + sqrt(x + 1))**2` | $x \left(\sqrt{1 - x} + \sqrt{x + 1}\right)^{2}$ |
| partial | concrete | `(sqrt(1 - x) + sqrt(x + 1))**2` | $\left(\sqrt{1 - x} + \sqrt{x + 1}\right)^{2}$ |
| partial | concrete | `(sqrt(1 - x) + sqrt(x + 1))**2/x` | $\frac{\left(\sqrt{1 - x} + \sqrt{x + 1}\right)^{2}}{x}$ |
| partial | concrete | `(sqrt(1 - x) + sqrt(x + 1))**2/x**2` | $\frac{\left(\sqrt{1 - x} + \sqrt{x + 1}\right)^{2}}{x^{2}}$ |
| partial | concrete | `(sqrt(1 - x) + sqrt(x + 1))**2/x**3` | $\frac{\left(\sqrt{1 - x} + \sqrt{x + 1}\right)^{2}}{x^{3}}$ |
| partial | parametric | `x**3/(sqrt(a + b*x) + sqrt(a + c*x))` | $\frac{x^{3}}{\sqrt{a + b x} + \sqrt{a + c x}}$ |
| partial | parametric | `x**2/(sqrt(a + b*x) + sqrt(a + c*x))` | $\frac{x^{2}}{\sqrt{a + b x} + \sqrt{a + c x}}$ |
| partial | parametric | `x/(sqrt(a + b*x) + sqrt(a + c*x))` | $\frac{x}{\sqrt{a + b x} + \sqrt{a + c x}}$ |
| partial | parametric | `1/(sqrt(a + b*x) + sqrt(a + c*x))` | $\frac{1}{\sqrt{a + b x} + \sqrt{a + c x}}$ |
| partial | parametric | `1/(x*(sqrt(a + b*x) + sqrt(a + c*x)))` | $\frac{1}{x \left(\sqrt{a + b x} + \sqrt{a + c x}\right)}$ |
| partial | parametric | `1/(x**2*(sqrt(a + b*x) + sqrt(a + c*x)))` | $\frac{1}{x^{2} \left(\sqrt{a + b x} + \sqrt{a + c x}\right)}$ |
| partial | parametric | `x**3/(sqrt(a + b*x) + sqrt(a + c*x))**2` | $\frac{x^{3}}{\left(\sqrt{a + b x} + \sqrt{a + c x}\right)^{2}}$ |
| partial | parametric | `x**2/(sqrt(a + b*x) + sqrt(a + c*x))**2` | $\frac{x^{2}}{\left(\sqrt{a + b x} + \sqrt{a + c x}\right)^{2}}$ |
| partial | parametric | `x/(sqrt(a + b*x) + sqrt(a + c*x))**2` | $\frac{x}{\left(\sqrt{a + b x} + \sqrt{a + c x}\right)^{2}}$ |
| partial | parametric | `(sqrt(a + b*x) + sqrt(a + c*x))**(-2)` | $\frac{1}{\left(\sqrt{a + b x} + \sqrt{a + c x}\right)^{2}}$ |
| partial | parametric | `1/(x*(sqrt(a + b*x) + sqrt(a + c*x))**2)` | $\frac{1}{x \left(\sqrt{a + b x} + \sqrt{a + c x}\right)^{2}}$ |
| partial | parametric | `1/(x**2*(sqrt(a + b*x) + sqrt(a + c*x))**2)` | $\frac{1}{x^{2} \left(\sqrt{a + b x} + \sqrt{a + c x}\right)^{2}}$ |
| partial | parametric | `x**4/(sqrt(a + b*x) + sqrt(a + c*x))**3` | $\frac{x^{4}}{\left(\sqrt{a + b x} + \sqrt{a + c x}\right)^{3}}$ |
| partial | parametric | `x**3/(sqrt(a + b*x) + sqrt(a + c*x))**3` | $\frac{x^{3}}{\left(\sqrt{a + b x} + \sqrt{a + c x}\right)^{3}}$ |
| partial | parametric | `x**2/(sqrt(a + b*x) + sqrt(a + c*x))**3` | $\frac{x^{2}}{\left(\sqrt{a + b x} + \sqrt{a + c x}\right)^{3}}$ |
| partial | concrete | `sqrt(1 - x)*(sqrt(1 - x) + sqrt(x + 1))` | $\sqrt{1 - x} \left(\sqrt{1 - x} + \sqrt{x + 1}\right)$ |
| **SOLVED-NEW** | concrete | `x**3*(-sqrt(1 - x) - sqrt(x + 1))*(sqrt(1 - x) + sqrt(x + 1))` | $x^{3} \left(- \sqrt{1 - x} - \sqrt{x + 1}\right) \left(\sqrt{1 - x} + \sqrt{x + 1}\right)$ |
| partial | concrete | `x**2*(-sqrt(1 - x) - sqrt(x + 1))*(sqrt(1 - x) + sqrt(x + 1))` | $x^{2} \left(- \sqrt{1 - x} - \sqrt{x + 1}\right) \left(\sqrt{1 - x} + \sqrt{x + 1}\right)$ |
| **SOLVED-NEW** | concrete | `x*(-sqrt(1 - x) - sqrt(x + 1))*(sqrt(1 - x) + sqrt(x + 1))` | $x \left(- \sqrt{1 - x} - \sqrt{x + 1}\right) \left(\sqrt{1 - x} + \sqrt{x + 1}\right)$ |
| partial | concrete | `(-sqrt(1 - x) - sqrt(x + 1))*(sqrt(1 - x) + sqrt(x + 1))` | $\left(- \sqrt{1 - x} - \sqrt{x + 1}\right) \left(\sqrt{1 - x} + \sqrt{x + 1}\right)$ |
| partial | concrete | `(-sqrt(1 - x) - sqrt(x + 1))*(sqrt(1 - x) + sqrt(x + 1))/x` | $\frac{\left(- \sqrt{1 - x} - \sqrt{x + 1}\right) \left(\sqrt{1 - x} + \sqrt{x + 1}\right)}{x}$ |
| partial | concrete | `(-sqrt(1 - x) - sqrt(x + 1))*(sqrt(1 - x) + sqrt(x + 1))/x**2` | $\frac{\left(- \sqrt{1 - x} - \sqrt{x + 1}\right) \left(\sqrt{1 - x} + \sqrt{x + 1}\right)}{x^{2}}$ |
| partial | concrete | `(-sqrt(1 - x) - sqrt(x + 1))*(sqrt(1 - x) + sqrt(x + 1))/x**3` | $\frac{\left(- \sqrt{1 - x} - \sqrt{x + 1}\right) \left(\sqrt{1 - x} + \sqrt{x + 1}\right)}{x^{3}}$ |
| partial | concrete | `(sqrt(1 - x) + sqrt(x + 1))/(-sqrt(1 - x) + sqrt(x + 1))` | $\frac{\sqrt{1 - x} + \sqrt{x + 1}}{- \sqrt{1 - x} + \sqrt{x + 1}}$ |
| partial | concrete | `(-sqrt(x - 1) + sqrt(x + 1))/(sqrt(x - 1) + sqrt(x + 1))` | $\frac{- \sqrt{x - 1} + \sqrt{x + 1}}{\sqrt{x - 1} + \sqrt{x + 1}}$ |
| partial | parametric | `(d + e*x + f*sqrt(a + e**2*x**2/f**2))**3` | $\left(d + e x + f \sqrt{a + \frac{e^{2} x^{2}}{f^{2}}}\right)^{3}$ |
| partial | parametric | `(d + e*x + f*sqrt(a + e**2*x**2/f**2))**2` | $\left(d + e x + f \sqrt{a + \frac{e^{2} x^{2}}{f^{2}}}\right)^{2}$ |
| partial | parametric | `d + e*x + f*sqrt(a + e**2*x**2/f**2)` | $d + e x + f \sqrt{a + \frac{e^{2} x^{2}}{f^{2}}}$ |
| partial | parametric | `1/(d + e*x + f*sqrt(a + e**2*x**2/f**2))` | $\frac{1}{d + e x + f \sqrt{a + \frac{e^{2} x^{2}}{f^{2}}}}$ |
| partial | parametric | `(d + e*x + f*sqrt(a + e**2*x**2/f**2))**(-2)` | $\frac{1}{\left(d + e x + f \sqrt{a + \frac{e^{2} x^{2}}{f^{2}}}\right)^{2}}$ |
| timeout | parametric | `(d + e*x + f*sqrt(a + e**2*x**2/f**2))**(-3)` | $\frac{1}{\left(d + e x + f \sqrt{a + \frac{e^{2} x^{2}}{f^{2}}}\right)^{3}}$ |
| NIE | parametric | `(d + e*x + f*sqrt(a + e**2*x**2/f**2))**(5/2)` | $\left(d + e x + f \sqrt{a + \frac{e^{2} x^{2}}{f^{2}}}\right)^{\frac{5}{2}}$ |
| NIE | parametric | `(d + e*x + f*sqrt(a + e**2*x**2/f**2))**(3/2)` | $\left(d + e x + f \sqrt{a + \frac{e^{2} x^{2}}{f^{2}}}\right)^{\frac{3}{2}}$ |
| NIE | parametric | `sqrt(d + e*x + f*sqrt(a + e**2*x**2/f**2))` | $\sqrt{d + e x + f \sqrt{a + \frac{e^{2} x^{2}}{f^{2}}}}$ |
| NIE | parametric | `1/sqrt(d + e*x + f*sqrt(a + e**2*x**2/f**2))` | $\frac{1}{\sqrt{d + e x + f \sqrt{a + \frac{e^{2} x^{2}}{f^{2}}}}}$ |
| NIE | parametric | `(d + e*x + f*sqrt(a + e**2*x**2/f**2))**(-3/2)` | $\frac{1}{\left(d + e x + f \sqrt{a + \frac{e^{2} x^{2}}{f^{2}}}\right)^{\frac{3}{2}}}$ |
| NIE | parametric | `(d + e*x + f*sqrt(a + e**2*x**2/f**2))**(-5/2)` | $\frac{1}{\left(d + e x + f \sqrt{a + \frac{e^{2} x^{2}}{f^{2}}}\right)^{\frac{5}{2}}}$ |
| NIE | concrete | `sqrt(x - sqrt(x**2 - 4))` | $\sqrt{x - \sqrt{x^{2} - 4}}$ |
| NIE | parametric | `sqrt(a*x + b*sqrt(a**2*x**2/b**2 + c))` | $\sqrt{a x + b \sqrt{\frac{a^{2} x^{2}}{b^{2}} + c}}$ |
| NIE | concrete | `sqrt(sqrt(1 - x**2) + 1)` | $\sqrt{\sqrt{1 - x^{2}} + 1}$ |
| NIE | concrete | `sqrt(sqrt(x**2 + 1) + 1)` | $\sqrt{\sqrt{x^{2} + 1} + 1}$ |
| NIE | concrete | `sqrt(sqrt(x**2 + 25) + 5)` | $\sqrt{\sqrt{x^{2} + 25} + 5}$ |
| NIE | parametric | `sqrt(a + b*sqrt(a**2/b**2 + c*x**2))` | $\sqrt{a + b \sqrt{\frac{a^{2}}{b^{2}} + c x^{2}}}$ |
| partial | parametric | `(d + e*x + f*sqrt(a + b*x + e**2*x**2/f**2))**3` | $\left(d + e x + f \sqrt{a + b x + \frac{e^{2} x^{2}}{f^{2}}}\right)^{3}$ |
| partial | parametric | `(d + e*x + f*sqrt(a + b*x + e**2*x**2/f**2))**2` | $\left(d + e x + f \sqrt{a + b x + \frac{e^{2} x^{2}}{f^{2}}}\right)^{2}$ |
| partial | parametric | `d + e*x + f*sqrt(a + b*x + e**2*x**2/f**2)` | $d + e x + f \sqrt{a + b x + \frac{e^{2} x^{2}}{f^{2}}}$ |
| partial | parametric | `1/(d + e*x + f*sqrt(a + b*x + e**2*x**2/f**2))` | $\frac{1}{d + e x + f \sqrt{a + b x + \frac{e^{2} x^{2}}{f^{2}}}}$ |
| timeout | parametric | `(d + e*x + f*sqrt(a + b*x + e**2*x**2/f**2))**(-2)` | $\frac{1}{\left(d + e x + f \sqrt{a + b x + \frac{e^{2} x^{2}}{f^{2}}}\right)^{2}}$ |
| timeout | parametric | `(d + e*x + f*sqrt(a + b*x + e**2*x**2/f**2))**(-3)` | $\frac{1}{\left(d + e x + f \sqrt{a + b x + \frac{e^{2} x^{2}}{f^{2}}}\right)^{3}}$ |
| timeout | parametric | `(d + e*x + f*sqrt(a + b*x + e**2*x**2/f**2))**(5/2)` | $\left(d + e x + f \sqrt{a + b x + \frac{e^{2} x^{2}}{f^{2}}}\right)^{\frac{5}{2}}$ |
| timeout | parametric | `(d + e*x + f*sqrt(a + b*x + e**2*x**2/f**2))**(3/2)` | $\left(d + e x + f \sqrt{a + b x + \frac{e^{2} x^{2}}{f^{2}}}\right)^{\frac{3}{2}}$ |
| NIE | parametric | `sqrt(d + e*x + f*sqrt(a + b*x + e**2*x**2/f**2))` | $\sqrt{d + e x + f \sqrt{a + b x + \frac{e^{2} x^{2}}{f^{2}}}}$ |
| timeout | parametric | `1/sqrt(d + e*x + f*sqrt(a + b*x + e**2*x**2/f**2))` | $\frac{1}{\sqrt{d + e x + f \sqrt{a + b x + \frac{e^{2} x^{2}}{f^{2}}}}}$ |
| timeout | parametric | `(d + e*x + f*sqrt(a + b*x + e**2*x**2/f**2))**(-3/2)` | $\frac{1}{\left(d + e x + f \sqrt{a + b x + \frac{e^{2} x^{2}}{f^{2}}}\right)^{\frac{3}{2}}}$ |
| timeout | parametric | `(d + e*x + f*sqrt(a + b*x + e**2*x**2/f**2))**(-5/2)` | $\frac{1}{\left(d + e x + f \sqrt{a + b x + \frac{e^{2} x^{2}}{f^{2}}}\right)^{\frac{5}{2}}}$ |
| timeout | parametric | `1/((a + b*x)*sqrt(c + d*x**2)*sqrt(e + f*x**2))` | $\frac{1}{\left(a + b x\right) \sqrt{c + d x^{2}} \sqrt{e + f x^{2}}}$ |
| partial | parametric | `x**5/(a*c + b*c*x**2 + d*sqrt(a + b*x**2))` | $\frac{x^{5}}{a c + b c x^{2} + d \sqrt{a + b x^{2}}}$ |
| partial | parametric | `x**3/(a*c + b*c*x**2 + d*sqrt(a + b*x**2))` | $\frac{x^{3}}{a c + b c x^{2} + d \sqrt{a + b x^{2}}}$ |
| SOLVED-both | parametric | `x/(a*c + b*c*x**2 + d*sqrt(a + b*x**2))` | $\frac{x}{a c + b c x^{2} + d \sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/(x*(a*c + b*c*x**2 + d*sqrt(a + b*x**2)))` | $\frac{1}{x \left(a c + b c x^{2} + d \sqrt{a + b x^{2}}\right)}$ |
| partial | parametric | `1/(x**3*(a*c + b*c*x**2 + d*sqrt(a + b*x**2)))` | $\frac{1}{x^{3} \left(a c + b c x^{2} + d \sqrt{a + b x^{2}}\right)}$ |
| partial | parametric | `x**2/(a*c + b*c*x**2 + d*sqrt(a + b*x**2))` | $\frac{x^{2}}{a c + b c x^{2} + d \sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/(a*c + b*c*x**2 + d*sqrt(a + b*x**2))` | $\frac{1}{a c + b c x^{2} + d \sqrt{a + b x^{2}}}$ |
| partial | parametric | `1/(x**2*(a*c + b*c*x**2 + d*sqrt(a + b*x**2)))` | $\frac{1}{x^{2} \left(a c + b c x^{2} + d \sqrt{a + b x^{2}}\right)}$ |
| partial | parametric | `x**8/(a*c + b*c*x**3 + d*sqrt(a + b*x**3))` | $\frac{x^{8}}{a c + b c x^{3} + d \sqrt{a + b x^{3}}}$ |
| partial | parametric | `x**5/(a*c + b*c*x**3 + d*sqrt(a + b*x**3))` | $\frac{x^{5}}{a c + b c x^{3} + d \sqrt{a + b x^{3}}}$ |
| **SOLVED-NEW** | parametric | `x**2/(a*c + b*c*x**3 + d*sqrt(a + b*x**3))` | $\frac{x^{2}}{a c + b c x^{3} + d \sqrt{a + b x^{3}}}$ |
| partial | parametric | `1/(x*(a*c + b*c*x**3 + d*sqrt(a + b*x**3)))` | $\frac{1}{x \left(a c + b c x^{3} + d \sqrt{a + b x^{3}}\right)}$ |
| partial | parametric | `1/(x**4*(a*c + b*c*x**3 + d*sqrt(a + b*x**3)))` | $\frac{1}{x^{4} \left(a c + b c x^{3} + d \sqrt{a + b x^{3}}\right)}$ |
| partial | parametric | `x**3/(a*c + b*c*x**3 + d*sqrt(a + b*x**3))` | $\frac{x^{3}}{a c + b c x^{3} + d \sqrt{a + b x^{3}}}$ |
| partial | parametric | `x/(a*c + b*c*x**3 + d*sqrt(a + b*x**3))` | $\frac{x}{a c + b c x^{3} + d \sqrt{a + b x^{3}}}$ |
| partial | parametric | `1/(a*c + b*c*x**3 + d*sqrt(a + b*x**3))` | $\frac{1}{a c + b c x^{3} + d \sqrt{a + b x^{3}}}$ |
| partial | parametric | `1/(x**2*(a*c + b*c*x**3 + d*sqrt(a + b*x**3)))` | $\frac{1}{x^{2} \left(a c + b c x^{3} + d \sqrt{a + b x^{3}}\right)}$ |
| partial | parametric | `1/(x**3*(a*c + b*c*x**3 + d*sqrt(a + b*x**3)))` | $\frac{1}{x^{3} \left(a c + b c x^{3} + d \sqrt{a + b x^{3}}\right)}$ |
| partial | concrete | `1/(4*x**(3/2) + sqrt(x))` | $\frac{1}{4 x^{\frac{3}{2}} + \sqrt{x}}$ |
| partial | concrete | `1/(-x**(5/2) + sqrt(x))` | $\frac{1}{- x^{\frac{5}{2}} + \sqrt{x}}$ |
| partial | concrete | `1/(-x**(1/4) + sqrt(x))` | $\frac{1}{- \sqrt[4]{x} + \sqrt{x}}$ |
| partial | concrete | `1/(x**(1/3) + sqrt(x))` | $\frac{1}{\sqrt[3]{x} + \sqrt{x}}$ |
| partial | concrete | `1/(x**(1/4) + sqrt(x))` | $\frac{1}{\sqrt[4]{x} + \sqrt{x}}$ |
| partial | concrete | `1/(x**(2/3) - x**(1/3))` | $\frac{1}{x^{\frac{2}{3}} - \sqrt[3]{x}}$ |
| partial | concrete | `1/(sqrt(x) + x**(-1/4))` | $\frac{1}{\sqrt{x} + \frac{1}{\sqrt[4]{x}}}$ |
| partial | concrete | `1/(x**(1/4) + x**(1/3))` | $\frac{1}{\sqrt[4]{x} + \sqrt[3]{x}}$ |
| partial | concrete | `1/(x**(-1/3) + x**(-1/4))` | $\frac{1}{\frac{1}{\sqrt[3]{x}} + \frac{1}{\sqrt[4]{x}}}$ |
| partial | concrete | `1/(sqrt(x) - 1/x**(1/3))` | $\frac{1}{\sqrt{x} - \frac{1}{\sqrt[3]{x}}}$ |
| partial | concrete | `sqrt(x)/(x**2 + x)` | $\frac{\sqrt{x}}{x^{2} + x}$ |
| partial | concrete | `x/(4*sqrt(x) + x)` | $\frac{x}{4 \sqrt{x} + x}$ |
| partial | concrete | `sqrt(x)/(x**(1/3) + x)` | $\frac{\sqrt{x}}{\sqrt[3]{x} + x}$ |
| partial | concrete | `x**(1/3)/(x**(1/4) + sqrt(x))` | $\frac{\sqrt[3]{x}}{\sqrt[4]{x} + \sqrt{x}}$ |
| partial | concrete | `sqrt(x)/(x**(1/4) + x**(1/3))` | $\frac{\sqrt{x}}{\sqrt[4]{x} + \sqrt[3]{x}}$ |
| partial | concrete | `sqrt(x)/(sqrt(x) - 1/x**(1/3))` | $\frac{\sqrt{x}}{\sqrt{x} - \frac{1}{\sqrt[3]{x}}}$ |
| **SOLVED-NEW** | parametric | `x**2*sqrt(-a/x + b)/sqrt(a - b*x)` | $\frac{x^{2} \sqrt{- \frac{a}{x} + b}}{\sqrt{a - b x}}$ |
| **SOLVED-NEW** | parametric | `x*sqrt(-a/x + b)/sqrt(a - b*x)` | $\frac{x \sqrt{- \frac{a}{x} + b}}{\sqrt{a - b x}}$ |
| **SOLVED-NEW** | parametric | `sqrt(-a/x + b)/sqrt(a - b*x)` | $\frac{\sqrt{- \frac{a}{x} + b}}{\sqrt{a - b x}}$ |
| **SOLVED-NEW** | parametric | `sqrt(-a/x + b)/(x*sqrt(a - b*x))` | $\frac{\sqrt{- \frac{a}{x} + b}}{x \sqrt{a - b x}}$ |
| **SOLVED-NEW** | parametric | `sqrt(-a/x + b)/(x**2*sqrt(a - b*x))` | $\frac{\sqrt{- \frac{a}{x} + b}}{x^{2} \sqrt{a - b x}}$ |
| **SOLVED-NEW** | parametric | `x**2*sqrt(-a/x**2 + b)/sqrt(a - b*x**2)` | $\frac{x^{2} \sqrt{- \frac{a}{x^{2}} + b}}{\sqrt{a - b x^{2}}}$ |
| **SOLVED-NEW** | parametric | `x*sqrt(-a/x**2 + b)/sqrt(a - b*x**2)` | $\frac{x \sqrt{- \frac{a}{x^{2}} + b}}{\sqrt{a - b x^{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(-a/x**2 + b)/sqrt(a - b*x**2)` | $\frac{\sqrt{- \frac{a}{x^{2}} + b}}{\sqrt{a - b x^{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(-a/x**2 + b)/(x*sqrt(a - b*x**2))` | $\frac{\sqrt{- \frac{a}{x^{2}} + b}}{x \sqrt{a - b x^{2}}}$ |
| **SOLVED-NEW** | parametric | `sqrt(-a/x**2 + b)/(x**2*sqrt(a - b*x**2))` | $\frac{\sqrt{- \frac{a}{x^{2}} + b}}{x^{2} \sqrt{a - b x^{2}}}$ |
| partial | parametric | `(c + d*x)**(3/2)/sqrt(a + b/x**2)` | $\frac{\left(c + d x\right)^{\frac{3}{2}}}{\sqrt{a + \frac{b}{x^{2}}}}$ |
| SOLVED-both | concrete | `(x**3 - 1)/(x**4 - 4*x)**(2/3)` | $\frac{x^{3} - 1}{\left(x^{4} - 4 x\right)^{\frac{2}{3}}}$ |
| SOLVED-both | concrete | `(2 - x**2)*(-x**3 + 6*x)**(1/4)` | $\left(2 - x^{2}\right) \sqrt[4]{- x^{3} + 6 x}$ |
| SOLVED-both | concrete | `(x**4 + 1)*sqrt(x**5 + 5*x)` | $\left(x^{4} + 1\right) \sqrt{x^{5} + 5 x}$ |
| SOLVED-both | concrete | `(5*x**4 + 2)*sqrt(x**5 + 2*x)` | $\left(5 x^{4} + 2\right) \sqrt{x^{5} + 2 x}$ |
| SOLVED-both | concrete | `(3*x**2 + x)/sqrt(2*x**3 + x**2)` | $\frac{3 x^{2} + x}{\sqrt{2 x^{3} + x^{2}}}$ |
| partial | concrete | `((1 - 5*x)**(1/3) + 2)/((1 - 5*x)**(1/3) + 3)` | $\frac{\sqrt[3]{1 - 5 x} + 2}{\sqrt[3]{1 - 5 x} + 3}$ |
| partial | concrete | `(sqrt(x) + 1)/(sqrt(x) - 1)` | $\frac{\sqrt{x} + 1}{\sqrt{x} - 1}$ |
| partial | concrete | `(1 - sqrt(3*x + 2))/(sqrt(3*x + 2) + 1)` | $\frac{1 - \sqrt{3 x + 2}}{\sqrt{3 x + 2} + 1}$ |
| partial | parametric | `(sqrt(a + b*x) - 1)/(sqrt(a + b*x) + 1)` | $\frac{\sqrt{a + b x} - 1}{\sqrt{a + b x} + 1}$ |
| SOLVED-both | parametric | `x**3*(a + b*sqrt(c + d*x))**2` | $x^{3} \left(a + b \sqrt{c + d x}\right)^{2}$ |
| SOLVED-both | parametric | `x**2*(a + b*sqrt(c + d*x))**2` | $x^{2} \left(a + b \sqrt{c + d x}\right)^{2}$ |
| SOLVED-both | parametric | `x*(a + b*sqrt(c + d*x))**2` | $x \left(a + b \sqrt{c + d x}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*sqrt(c + d*x))**2` | $\left(a + b \sqrt{c + d x}\right)^{2}$ |
| partial | parametric | `(a + b*sqrt(c + d*x))**2/x` | $\frac{\left(a + b \sqrt{c + d x}\right)^{2}}{x}$ |
| partial | parametric | `(a + b*sqrt(c + d*x))**2/x**2` | $\frac{\left(a + b \sqrt{c + d x}\right)^{2}}{x^{2}}$ |
| partial | parametric | `(a + b*sqrt(c + d*x))**2/x**3` | $\frac{\left(a + b \sqrt{c + d x}\right)^{2}}{x^{3}}$ |
| NIE | parametric | `x**3*sqrt(a + b*sqrt(c + d*x))` | $x^{3} \sqrt{a + b \sqrt{c + d x}}$ |
| NIE | parametric | `x**2*sqrt(a + b*sqrt(c + d*x))` | $x^{2} \sqrt{a + b \sqrt{c + d x}}$ |
| NIE | parametric | `x*sqrt(a + b*sqrt(c + d*x))` | $x \sqrt{a + b \sqrt{c + d x}}$ |
| NIE | parametric | `sqrt(a + b*sqrt(c + d*x))` | $\sqrt{a + b \sqrt{c + d x}}$ |
| NIE | parametric | `sqrt(a + b*sqrt(c + d*x))/x` | $\frac{\sqrt{a + b \sqrt{c + d x}}}{x}$ |
| NIE | parametric | `sqrt(a + b*sqrt(c + d*x))/x**2` | $\frac{\sqrt{a + b \sqrt{c + d x}}}{x^{2}}$ |
| NIE | parametric | `sqrt(a + b*sqrt(c + d*x))/x**3` | $\frac{\sqrt{a + b \sqrt{c + d x}}}{x^{3}}$ |
| partial | parametric | `x**3/(a + b*sqrt(c + d*x))` | $\frac{x^{3}}{a + b \sqrt{c + d x}}$ |
| partial | parametric | `x**2/(a + b*sqrt(c + d*x))` | $\frac{x^{2}}{a + b \sqrt{c + d x}}$ |
| partial | parametric | `x/(a + b*sqrt(c + d*x))` | $\frac{x}{a + b \sqrt{c + d x}}$ |
| partial | parametric | `1/(a + b*sqrt(c + d*x))` | $\frac{1}{a + b \sqrt{c + d x}}$ |
| partial | parametric | `1/(x*(a + b*sqrt(c + d*x)))` | $\frac{1}{x \left(a + b \sqrt{c + d x}\right)}$ |
| partial | parametric | `1/(x**2*(a + b*sqrt(c + d*x)))` | $\frac{1}{x^{2} \left(a + b \sqrt{c + d x}\right)}$ |
| partial | parametric | `1/(x**3*(a + b*sqrt(c + d*x)))` | $\frac{1}{x^{3} \left(a + b \sqrt{c + d x}\right)}$ |
| partial | parametric | `x**3/(a + b*sqrt(c + d*x))**2` | $\frac{x^{3}}{\left(a + b \sqrt{c + d x}\right)^{2}}$ |
| partial | parametric | `x**2/(a + b*sqrt(c + d*x))**2` | $\frac{x^{2}}{\left(a + b \sqrt{c + d x}\right)^{2}}$ |
| partial | parametric | `x/(a + b*sqrt(c + d*x))**2` | $\frac{x}{\left(a + b \sqrt{c + d x}\right)^{2}}$ |
| partial | parametric | `(a + b*sqrt(c + d*x))**(-2)` | $\frac{1}{\left(a + b \sqrt{c + d x}\right)^{2}}$ |
| partial | parametric | `1/(x*(a + b*sqrt(c + d*x))**2)` | $\frac{1}{x \left(a + b \sqrt{c + d x}\right)^{2}}$ |
| partial | parametric | `1/(x**2*(a + b*sqrt(c + d*x))**2)` | $\frac{1}{x^{2} \left(a + b \sqrt{c + d x}\right)^{2}}$ |
| partial | parametric | `1/(x**3*(a + b*sqrt(c + d*x))**2)` | $\frac{1}{x^{3} \left(a + b \sqrt{c + d x}\right)^{2}}$ |
| NIE | parametric | `x**3/sqrt(a + b*sqrt(c + d*x))` | $\frac{x^{3}}{\sqrt{a + b \sqrt{c + d x}}}$ |
| NIE | parametric | `x**2/sqrt(a + b*sqrt(c + d*x))` | $\frac{x^{2}}{\sqrt{a + b \sqrt{c + d x}}}$ |
| NIE | parametric | `x/sqrt(a + b*sqrt(c + d*x))` | $\frac{x}{\sqrt{a + b \sqrt{c + d x}}}$ |
| NIE | parametric | `1/sqrt(a + b*sqrt(c + d*x))` | $\frac{1}{\sqrt{a + b \sqrt{c + d x}}}$ |
| NIE | parametric | `1/(x*sqrt(a + b*sqrt(c + d*x)))` | $\frac{1}{x \sqrt{a + b \sqrt{c + d x}}}$ |
| NIE | parametric | `1/(x**2*sqrt(a + b*sqrt(c + d*x)))` | $\frac{1}{x^{2} \sqrt{a + b \sqrt{c + d x}}}$ |
| NIE | parametric | `1/(x**3*sqrt(a + b*sqrt(c + d*x)))` | $\frac{1}{x^{3} \sqrt{a + b \sqrt{c + d x}}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x))` | $\frac{1}{x \sqrt{a + b x}}$ |
| partial | concrete | `sqrt(-1 + x**(-2))*(x**2 - 1)**3/x` | $\frac{\sqrt{-1 + \frac{1}{x^{2}}} \left(x^{2} - 1\right)^{3}}{x}$ |
| partial | concrete | `sqrt(-1 + x**(-2))*(x**2 - 1)**2/x` | $\frac{\sqrt{-1 + \frac{1}{x^{2}}} \left(x^{2} - 1\right)^{2}}{x}$ |
| partial | concrete | `sqrt(-1 + x**(-2))*(x**2 - 1)/x` | $\frac{\sqrt{-1 + \frac{1}{x^{2}}} \left(x^{2} - 1\right)}{x}$ |
| SOLVED-both | concrete | `sqrt(-1 + x**(-2))/(x*(x**2 - 1))` | $\frac{\sqrt{-1 + \frac{1}{x^{2}}}}{x \left(x^{2} - 1\right)}$ |
| SOLVED-both | concrete | `sqrt(-1 + x**(-2))/(x*(x**2 - 1)**2)` | $\frac{\sqrt{-1 + \frac{1}{x^{2}}}}{x \left(x^{2} - 1\right)^{2}}$ |
| SOLVED-both | concrete | `sqrt(-1 + x**(-2))/(x*(x**2 - 1)**3)` | $\frac{\sqrt{-1 + \frac{1}{x^{2}}}}{x \left(x^{2} - 1\right)^{3}}$ |
| SOLVED-both | concrete | `x*sqrt(1 + x**(-2))/(x**2 + 1)**2` | $\frac{x \sqrt{1 + \frac{1}{x^{2}}}}{\left(x^{2} + 1\right)^{2}}$ |
| SOLVED-both | concrete | `1/(x*sqrt(1 + x**(-2))*(x**2 + 1))` | $\frac{1}{x \sqrt{1 + \frac{1}{x^{2}}} \left(x^{2} + 1\right)}$ |
| SOLVED-both | parametric | `x/(a + b*x**2 + sqrt(a + b*x**2))` | $\frac{x}{a + b x^{2} + \sqrt{a + b x^{2}}}$ |
| SOLVED-both | concrete | `x/(x**2 - (x**2)**(1/3))` | $\frac{x}{x^{2} - \sqrt[3]{x^{2}}}$ |
| SOLVED-both | concrete | `x*(x**2 + 1)**3*sqrt(x**4 + 2*x**2 + 2)` | $x \left(x^{2} + 1\right)^{3} \sqrt{x^{4} + 2 x^{2} + 2}$ |
| partial | concrete | `x*sqrt((1 - x**2)/(x**2 + 1))` | $x \sqrt{\frac{1 - x^{2}}{x^{2} + 1}}$ |
| partial | concrete | `x*sqrt((5 - 7*x**2)/(5*x**2 + 7))` | $x \sqrt{\frac{5 - 7 x^{2}}{5 x^{2} + 7}}$ |
| partial | concrete | `x**2*sqrt((1 - x**3)/(x**3 + 1))` | $x^{2} \sqrt{\frac{1 - x^{3}}{x^{3} + 1}}$ |
| SOLVED-both | concrete | `x**5*sqrt(1 - x**3)*(x**9 + 1)**2` | $x^{5} \sqrt{1 - x^{3}} \left(x^{9} + 1\right)^{2}$ |
| partial | concrete | `x**8*sqrt((1 - x**3)/(x**3 + 1))` | $x^{8} \sqrt{\frac{1 - x^{3}}{x^{3} + 1}}$ |
| partial | concrete | `x**9*sqrt((5 - 7*x**5)/(5*x**5 + 7))` | $x^{9} \sqrt{\frac{5 - 7 x^{5}}{5 x^{5} + 7}}$ |
| partial | parametric | `x/(sqrt(a + b*x**2)*(x**2 + 1)) + x/(a + b*x**2)**(3/2)` | $\frac{x}{\sqrt{a + b x^{2}} \left(x^{2} + 1\right)} + \frac{x}{\left(a + b x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x*(a + b*x**2 + x**2 + 1)/((a + b*x**2)**(3/2)*(x**2 + 1))` | $\frac{x \left(a + b x^{2} + x^{2} + 1\right)}{\left(a + b x^{2}\right)^{\frac{3}{2}} \left(x^{2} + 1\right)}$ |
| partial | parametric | `x/(sqrt(a + b*x**2)*(x**2 + 1)) + x/(a + b*x**2)**(3/2) + x/(a + b*x**2)**(5/2)` | $\frac{x}{\sqrt{a + b x^{2}} \left(x^{2} + 1\right)} + \frac{x}{\left(a + b x^{2}\right)^{\frac{3}{2}}} + \frac{x}{\left(a + b x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x*(a**2 + 2*a*b*x**2 + a*x**2 + a + b**2*x**4 + b*x**4 + b*x**2 + x**2 + 1)/((a + b*x**2)**(5/2)*(x**2 + 1))` | $\frac{x \left(a^{2} + 2 a b x^{2} + a x^{2} + a + b^{2} x^{4} + b x^{4} + b x^{2} + x^{2} + 1\right)}{\left(a + b x^{2}\right)^{\frac{5}{2}} \left(x^{2} + 1\right)}$ |
| partial | concrete | `1/sqrt(sqrt(x) + x)` | $\frac{1}{\sqrt{\sqrt{x} + x}}$ |
| partial | concrete | `sqrt(sqrt(x) + x)` | $\sqrt{\sqrt{x} + x}$ |
| SOLVED-both | concrete | `sqrt(-x)*(x + sqrt(-x))` | $\sqrt{- x} \left(x + \sqrt{- x}\right)$ |
| partial | concrete | `(x**(1/4) + 5)/(x - 6)` | $\frac{\sqrt[4]{x} + 5}{x - 6}$ |
| SOLVED-both | concrete | `1/(-x + sqrt(4 - x) + 4)` | $\frac{1}{- x + \sqrt{4 - x} + 4}$ |
| partial | concrete | `1/(x - sqrt(x + 2) + 1)` | $\frac{1}{x - \sqrt{x + 2} + 1}$ |
| partial | concrete | `1/(x + sqrt(x + 1) + 4)` | $\frac{1}{x + \sqrt{x + 1} + 4}$ |
| partial | concrete | `1/(x - sqrt(x + 1))` | $\frac{1}{x - \sqrt{x + 1}}$ |
| partial | concrete | `1/(x - sqrt(x + 2))` | $\frac{1}{x - \sqrt{x + 2}}$ |
| partial | concrete | `1/(x - sqrt(1 - x))` | $\frac{1}{x - \sqrt{1 - x}}$ |
| NIE | concrete | `sqrt(sqrt(x) + x + 1)` | $\sqrt{\sqrt{x} + x + 1}$ |
| NIE | concrete | `sqrt(x + sqrt(x + 1) + 1)` | $\sqrt{x + \sqrt{x + 1} + 1}$ |
| NIE | concrete | `sqrt(x + sqrt(x - 1))` | $\sqrt{x + \sqrt{x - 1}}$ |
| NIE | concrete | `sqrt(2*x + sqrt(2*x - 1))` | $\sqrt{2 x + \sqrt{2 x - 1}}$ |
| NIE | concrete | `sqrt(3*x + sqrt(8*x - 7))` | $\sqrt{3 x + \sqrt{8 x - 7}}$ |
| NIE | concrete | `1/sqrt(x + sqrt(x + 1))` | $\frac{1}{\sqrt{x + \sqrt{x + 1}}}$ |
| partial | concrete | `(x + 1)/(x + sqrt(6*x - 9) + 4)` | $\frac{x + 1}{x + \sqrt{6 x - 9} + 4}$ |
| partial | concrete | `(12 - x)/(x + sqrt(6*x - 9) + 4)` | $\frac{12 - x}{x + \sqrt{6 x - 9} + 4}$ |
| partial | concrete | `(x**3 - 1)/(sqrt(x)*(x**2 + 1))` | $\frac{x^{3} - 1}{\sqrt{x} \left(x^{2} + 1\right)}$ |
| NIE | concrete | `1/(2*sqrt(x - 1)*sqrt(x - sqrt(x - 1)))` | $\frac{1}{2 \sqrt{x - 1} \sqrt{x - \sqrt{x - 1}}}$ |
| partial | concrete | `(2*x + 4)/((2*x - 1)**(1/3) + sqrt(2*x - 1))` | $\frac{2 x + 4}{\sqrt[3]{2 x - 1} + \sqrt{2 x - 1}}$ |
| NIE | concrete | `1/sqrt(sqrt(sqrt(x) + 1) + 2)` | $\frac{1}{\sqrt{\sqrt{\sqrt{x} + 1} + 2}}$ |
| NIE | concrete | `sqrt(sqrt(sqrt(x) + 4) + 2)` | $\sqrt{\sqrt{\sqrt{x} + 4} + 2}$ |
| NIE | concrete | `sqrt(2 - sqrt(sqrt(5*x - 9) + 4))` | $\sqrt{2 - \sqrt{\sqrt{5 x - 9} + 4}}$ |
| NIE | concrete | `1/sqrt(sqrt(sqrt(x) + 1) + 2)` | $\frac{1}{\sqrt{\sqrt{\sqrt{x} + 1} + 2}}$ |
| timeout | concrete | `sqrt(sqrt(sqrt(sqrt(x) + 1) + 1) + 1)` | $\sqrt{\sqrt{\sqrt{\sqrt{x} + 1} + 1} + 1}$ |
| timeout | concrete | `sqrt(sqrt(sqrt(2*sqrt(x) - 1) + 3) + 2)` | $\sqrt{\sqrt{\sqrt{2 \sqrt{x} - 1} + 3} + 2}$ |
| NIE | concrete | `x*sqrt(sqrt(sqrt(x - 1) + 1) + 1)` | $x \sqrt{\sqrt{\sqrt{x - 1} + 1} + 1}$ |
| NIE | concrete | `1/(sqrt(x - 1)*sqrt(x - sqrt(x - 1)))` | $\frac{1}{\sqrt{x - 1} \sqrt{x - \sqrt{x - 1}}}$ |
| partial | parametric | `(p*x + q)/((f + sqrt(a*x + b))*sqrt(a*x + b))` | $\frac{p x + q}{\left(f + \sqrt{a x + b}\right) \sqrt{a x + b}}$ |
| NIE | concrete | `sqrt(-sqrt(x) - x + 1)` | $\sqrt{- \sqrt{x} - x + 1}$ |
| partial | concrete | `(6*sqrt(x) + x + 9)/(4*sqrt(x) + x)` | $\frac{6 \sqrt{x} + x + 9}{4 \sqrt{x} + x}$ |
| partial | concrete | `(6 - 8*x**(7/2))/(5 - 9*sqrt(x))` | $\frac{6 - 8 x^{\frac{7}{2}}}{5 - 9 \sqrt{x}}$ |
| NIE | concrete | `sqrt(-sqrt(x) + x - 1)/(sqrt(x)*(x - 1))` | $\frac{\sqrt{- \sqrt{x} + x - 1}}{\sqrt{x} \left(x - 1\right)}$ |
| NIE | concrete | `(2*sqrt(x + 1) + 1)/(x*sqrt(x + 1)*sqrt(x + sqrt(x + 1)))` | $\frac{2 \sqrt{x + 1} + 1}{x \sqrt{x + 1} \sqrt{x + \sqrt{x + 1}}}$ |
| partial | concrete | `1/(sqrt(x)*sqrt(x + 1))` | $\frac{1}{\sqrt{x} \sqrt{x + 1}}$ |
| partial | concrete | `sqrt(x/(x + 1))/x` | $\frac{\sqrt{\frac{x}{x + 1}}}{x}$ |
| partial | concrete | `sqrt(x)/sqrt(x + 1)` | $\frac{\sqrt{x}}{\sqrt{x + 1}}$ |
| partial | concrete | `sqrt(x/(x + 1))` | $\sqrt{\frac{x}{x + 1}}$ |
| partial | concrete | `sqrt(x - 1)/(x**2*sqrt(x + 1))` | $\frac{\sqrt{x - 1}}{x^{2} \sqrt{x + 1}}$ |
| partial | concrete | `sqrt((x - 1)/(x + 1))/x**2` | $\frac{\sqrt{\frac{x - 1}{x + 1}}}{x^{2}}$ |
| partial | concrete | `x**3*sqrt(x - 1)/sqrt(x + 1)` | $\frac{x^{3} \sqrt{x - 1}}{\sqrt{x + 1}}$ |
| partial | concrete | `x**3*sqrt((x - 1)/(x + 1))` | $x^{3} \sqrt{\frac{x - 1}{x + 1}}$ |
| partial | concrete | `sqrt(-x/(x + 1))/x` | $\frac{\sqrt{- \frac{x}{x + 1}}}{x}$ |
| partial | concrete | `sqrt((1 - x)/(x + 1))/(x - 1)` | $\frac{\sqrt{\frac{1 - x}{x + 1}}}{x - 1}$ |
| partial | parametric | `sqrt((a + b*x)/(-b*x + c))/(a + b*x)` | $\frac{\sqrt{\frac{a + b x}{- b x + c}}}{a + b x}$ |
| partial | parametric | `sqrt((a + b*x)/(c + d*x))/(a + b*x)` | $\frac{\sqrt{\frac{a + b x}{c + d x}}}{a + b x}$ |
| partial | concrete | `sqrt(-x/(x + 1))` | $\sqrt{- \frac{x}{x + 1}}$ |
| partial | concrete | `sqrt((1 - x)/(x + 1))` | $\sqrt{\frac{1 - x}{x + 1}}$ |
| partial | parametric | `sqrt((a + x)/(a - x))` | $\sqrt{\frac{a + x}{a - x}}$ |
| partial | parametric | `sqrt((-a + x)/(a + x))` | $\sqrt{\frac{- a + x}{a + x}}$ |
| partial | parametric | `sqrt((a + b*x)/(c + d*x))` | $\sqrt{\frac{a + b x}{c + d x}}$ |
| partial | concrete | `sqrt((x - 1)/(3*x + 5))` | $\sqrt{\frac{x - 1}{3 x + 5}}$ |
| partial | concrete | `sqrt((5*x - 1)/(7*x + 1))/x**2` | $\frac{\sqrt{\frac{5 x - 1}{7 x + 1}}}{x^{2}}$ |
| SOLVED-both | concrete | `x/(sqrt((1 - x)/(x + 1))*(x + 1))` | $\frac{x}{\sqrt{\frac{1 - x}{x + 1}} \left(x + 1\right)}$ |
| SOLVED-both | concrete | `x/(sqrt(-1 + 2/(x + 1))*(x + 1))` | $\frac{x}{\sqrt{-1 + \frac{2}{x + 1}} \left(x + 1\right)}$ |
| partial | concrete | `x/(sqrt((x + 2)/(x + 3))*(x + 1))` | $\frac{x}{\sqrt{\frac{x + 2}{x + 3}} \left(x + 1\right)}$ |
| SOLVED-both | concrete | `sqrt(1 + 1/x)/(x + 1)**2` | $\frac{\sqrt{1 + \frac{1}{x}}}{\left(x + 1\right)^{2}}$ |
| partial | concrete | `sqrt(1 + 1/x)/sqrt(1 - x**2)` | $\frac{\sqrt{1 + \frac{1}{x}}}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `1/(x + sqrt(-x**2 - 2*x + 3))` | $\frac{1}{x + \sqrt{- x^{2} - 2 x + 3}}$ |
| partial | concrete | `(x + sqrt(-x**2 - 2*x + 3))**(-2)` | $\frac{1}{\left(x + \sqrt{- x^{2} - 2 x + 3}\right)^{2}}$ |
| partial | concrete | `(x + sqrt(-x**2 - 2*x + 3))**(-3)` | $\frac{1}{\left(x + \sqrt{- x^{2} - 2 x + 3}\right)^{3}}$ |
| partial | concrete | `1/(x + sqrt(x**2 - 2*x - 3))` | $\frac{1}{x + \sqrt{x^{2} - 2 x - 3}}$ |
| partial | concrete | `(x + sqrt(x**2 - 2*x - 3))**(-2)` | $\frac{1}{\left(x + \sqrt{x^{2} - 2 x - 3}\right)^{2}}$ |
| partial | concrete | `(x + sqrt(x**2 - 2*x - 3))**(-3)` | $\frac{1}{\left(x + \sqrt{x^{2} - 2 x - 3}\right)^{3}}$ |
| partial | concrete | `1/(x + sqrt(-x**2 - 4*x - 3))` | $\frac{1}{x + \sqrt{- x^{2} - 4 x - 3}}$ |
| partial | concrete | `(x + sqrt(-x**2 - 4*x - 3))**(-2)` | $\frac{1}{\left(x + \sqrt{- x^{2} - 4 x - 3}\right)^{2}}$ |
| partial | concrete | `(x + sqrt(-x**2 - 4*x - 3))**(-3)` | $\frac{1}{\left(x + \sqrt{- x^{2} - 4 x - 3}\right)^{3}}$ |
| partial | concrete | `(-x**4 + 4*x**3 - 8*x**2 + 8*x)**(3/2)` | $\left(- x^{4} + 4 x^{3} - 8 x^{2} + 8 x\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(-x**4 + 4*x**3 - 8*x**2 + 8*x)` | $\sqrt{- x^{4} + 4 x^{3} - 8 x^{2} + 8 x}$ |
| partial | concrete | `1/sqrt(-x**4 + 4*x**3 - 8*x**2 + 8*x)` | $\frac{1}{\sqrt{- x^{4} + 4 x^{3} - 8 x^{2} + 8 x}}$ |
| partial | concrete | `(-x**4 + 4*x**3 - 8*x**2 + 8*x)**(-3/2)` | $\frac{1}{\left(- x^{4} + 4 x^{3} - 8 x^{2} + 8 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(-x**4 + 4*x**3 - 8*x**2 + 8*x)**(-5/2)` | $\frac{1}{\left(- x^{4} + 4 x^{3} - 8 x^{2} + 8 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(x*(2 - x)*(x**2 - 2*x + 4))**(3/2)` | $\left(x \left(2 - x\right) \left(x^{2} - 2 x + 4\right)\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(x*(2 - x)*(x**2 - 2*x + 4))` | $\sqrt{x \left(2 - x\right) \left(x^{2} - 2 x + 4\right)}$ |
| partial | concrete | `1/sqrt(x*(2 - x)*(x**2 - 2*x + 4))` | $\frac{1}{\sqrt{x \left(2 - x\right) \left(x^{2} - 2 x + 4\right)}}$ |
| partial | concrete | `(x*(2 - x)*(x**2 - 2*x + 4))**(-3/2)` | $\frac{1}{\left(x \left(2 - x\right) \left(x^{2} - 2 x + 4\right)\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x*(2 - x)*(x**2 - 2*x + 4))**(-5/2)` | $\frac{1}{\left(x \left(2 - x\right) \left(x^{2} - 2 x + 4\right)\right)^{\frac{5}{2}}}$ |
| partial | parametric | `(4*a*c + 4*c**2*x**2 + 4*c*d*x**3 + d**2*x**4)**(3/2)` | $\left(4 a c + 4 c^{2} x^{2} + 4 c d x^{3} + d^{2} x^{4}\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(4*a*c + 4*c**2*x**2 + 4*c*d*x**3 + d**2*x**4)` | $\sqrt{4 a c + 4 c^{2} x^{2} + 4 c d x^{3} + d^{2} x^{4}}$ |
| partial | parametric | `1/sqrt(4*a*c + 4*c**2*x**2 + 4*c*d*x**3 + d**2*x**4)` | $\frac{1}{\sqrt{4 a c + 4 c^{2} x^{2} + 4 c d x^{3} + d^{2} x^{4}}}$ |
| partial | parametric | `(4*a*c + 4*c**2*x**2 + 4*c*d*x**3 + d**2*x**4)**(-3/2)` | $\frac{1}{\left(4 a c + 4 c^{2} x^{2} + 4 c d x^{3} + d^{2} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt(8*a*e**2 - d**3*x + 8*d*e**2*x**3 + 8*e**3*x**4)` | $\sqrt{8 a e^{2} - d^{3} x + 8 d e^{2} x^{3} + 8 e^{3} x^{4}}$ |
| partial | parametric | `1/sqrt(8*a*e**2 - d**3*x + 8*d*e**2*x**3 + 8*e**3*x**4)` | $\frac{1}{\sqrt{8 a e^{2} - d^{3} x + 8 d e^{2} x^{3} + 8 e^{3} x^{4}}}$ |
| partial | parametric | `(8*a*e**2 - d**3*x + 8*d*e**2*x**3 + 8*e**3*x**4)**(-3/2)` | $\frac{1}{\left(8 a e^{2} - d^{3} x + 8 d e^{2} x^{3} + 8 e^{3} x^{4}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a - x**4 + 4*x**3 - 8*x**2 + 8*x)**(3/2)` | $\left(a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x\right)^{\frac{3}{2}}$ |
| partial | parametric | `sqrt(a - x**4 + 4*x**3 - 8*x**2 + 8*x)` | $\sqrt{a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x}$ |
| partial | parametric | `1/sqrt(a - x**4 + 4*x**3 - 8*x**2 + 8*x)` | $\frac{1}{\sqrt{a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x}}$ |
| partial | parametric | `(a - x**4 + 4*x**3 - 8*x**2 + 8*x)**(-3/2)` | $\frac{1}{\left(a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a - x**4 + 4*x**3 - 8*x**2 + 8*x)**(-5/2)` | $\frac{1}{\left(a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x*(a - x**4 + 4*x**3 - 8*x**2 + 8*x)**(3/2)` | $x \left(a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x\right)^{\frac{3}{2}}$ |
| partial | parametric | `x*sqrt(a - x**4 + 4*x**3 - 8*x**2 + 8*x)` | $x \sqrt{a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x}$ |
| partial | parametric | `x/sqrt(a - x**4 + 4*x**3 - 8*x**2 + 8*x)` | $\frac{x}{\sqrt{a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x}}$ |
| partial | parametric | `x/(a - x**4 + 4*x**3 - 8*x**2 + 8*x)**(3/2)` | $\frac{x}{\left(a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x/(a - x**4 + 4*x**3 - 8*x**2 + 8*x)**(5/2)` | $\frac{x}{\left(a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `x**2*(a - x**4 + 4*x**3 - 8*x**2 + 8*x)**(3/2)` | $x^{2} \left(a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x\right)^{\frac{3}{2}}$ |
| partial | parametric | `x**2*sqrt(a - x**4 + 4*x**3 - 8*x**2 + 8*x)` | $x^{2} \sqrt{a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x}$ |
| partial | parametric | `x**2/sqrt(a - x**4 + 4*x**3 - 8*x**2 + 8*x)` | $\frac{x^{2}}{\sqrt{a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x}}$ |
| partial | parametric | `x**2/(a - x**4 + 4*x**3 - 8*x**2 + 8*x)**(3/2)` | $\frac{x^{2}}{\left(a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `x**2/(a - x**4 + 4*x**3 - 8*x**2 + 8*x)**(5/2)` | $\frac{x^{2}}{\left(a - x^{4} + 4 x^{3} - 8 x^{2} + 8 x\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/sqrt(8*x**4 - x**3 + 8*x + 8)` | $\frac{1}{\sqrt{8 x^{4} - x^{3} + 8 x + 8}}$ |
| partial | concrete | `(8*x**4 - x**3 + 8*x + 8)**(-3/2)` | $\frac{1}{\left(8 x^{4} - x^{3} + 8 x + 8\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/sqrt(4*x**4 + 4*x**2 + 4*x + 1)` | $\frac{1}{\sqrt{4 x^{4} + 4 x^{2} + 4 x + 1}}$ |
| partial | concrete | `(4*x**4 + 4*x**2 + 4*x + 1)**(-3/2)` | $\frac{1}{\left(4 x^{4} + 4 x^{2} + 4 x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/sqrt(8*x**4 - 15*x**3 + 8*x**2 + 24*x + 8)` | $\frac{1}{\sqrt{8 x^{4} - 15 x^{3} + 8 x^{2} + 24 x + 8}}$ |
| partial | concrete | `(8*x**4 - 15*x**3 + 8*x**2 + 24*x + 8)**(-3/2)` | $\frac{1}{\left(8 x^{4} - 15 x^{3} + 8 x^{2} + 24 x + 8\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(8*x**4 - 15*x**3 + 8*x**2 + 24*x + 8)**(-5/2)` | $\frac{1}{\left(8 x^{4} - 15 x^{3} + 8 x^{2} + 24 x + 8\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/sqrt(3*x**4 + 15*x**3 - 44*x**2 - 6*x + 9)` | $\frac{1}{\sqrt{3 x^{4} + 15 x^{3} - 44 x^{2} - 6 x + 9}}$ |
| partial | concrete | `(3*x**4 + 15*x**3 - 44*x**2 - 6*x + 9)**(-3/2)` | $\frac{1}{\left(3 x^{4} + 15 x^{3} - 44 x^{2} - 6 x + 9\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(2*sqrt(3 - x) + 3/sqrt(x + 1))**2/x` | $\frac{\left(2 \sqrt{3 - x} + \frac{3}{\sqrt{x + 1}}\right)^{2}}{x}$ |
| partial | concrete | `(x**2 + x - 1)/(sqrt(x**2 + 1) + 1)` | $\frac{x^{2} + x - 1}{\sqrt{x^{2} + 1} + 1}$ |
| partial | concrete | `(x + 2*sqrt(x - 1))/(x*sqrt(x - 1))` | $\frac{x + 2 \sqrt{x - 1}}{x \sqrt{x - 1}}$ |
| SOLVED-both | parametric | `(a + b*x**(2/3) + c*sqrt(x))**2` | $\left(a + b x^{\frac{2}{3}} + c \sqrt{x}\right)^{2}$ |
| SOLVED-both | parametric | `(a + b*x**(2/3) + c*sqrt(x))**3` | $\left(a + b x^{\frac{2}{3}} + c \sqrt{x}\right)^{3}$ |
| partial | parametric | `(x**2 - 1)/(x**3*sqrt(a - b + b/x**2))` | $\frac{x^{2} - 1}{x^{3} \sqrt{a - b + \frac{b}{x^{2}}}}$ |
| partial | parametric | `(x**2 - 1)/(x**3*sqrt(a + b*(-1 + x**(-2))))` | $\frac{x^{2} - 1}{x^{3} \sqrt{a + b \left(-1 + \frac{1}{x^{2}}\right)}}$ |
| partial | concrete | `(x + 1)/((x**2 + 4)*sqrt(x**2 + 9))` | $\frac{x + 1}{\left(x^{2} + 4\right) \sqrt{x^{2} + 9}}$ |
| SOLVED-both | concrete | `x*(sqrt(1 - x**2) + 1)` | $x \left(\sqrt{1 - x^{2}} + 1\right)$ |
| **SOLVED-NEW** | concrete | `x*(sqrt(1 - x)*sqrt(x + 1) + 1)` | $x \left(\sqrt{1 - x} \sqrt{x + 1} + 1\right)$ |
| partial | concrete | `x*(1 + 1/(sqrt(x + 2)*sqrt(x + 3)))` | $x \left(1 + \frac{1}{\sqrt{x + 2} \sqrt{x + 3}}\right)$ |
| partial | concrete | `(x - sqrt(x**6))/(x*(1 - x**4))` | $\frac{x - \sqrt{x^{6}}}{x \left(1 - x^{4}\right)}$ |
| partial | concrete | `(1 - sqrt(x**6)/x)/(1 - x**4)` | $\frac{1 - \frac{\sqrt{x^{6}}}{x}}{1 - x^{4}}$ |
| partial | concrete | `(x - sqrt(x**6))/(-x**5 + x)` | $\frac{x - \sqrt{x^{6}}}{- x^{5} + x}$ |
| partial | concrete | `x/(x + sqrt(x**6))` | $\frac{x}{x + \sqrt{x^{6}}}$ |
| partial | concrete | `(sqrt(x) - sqrt(x**3))/(-x**3 + x)` | $\frac{\sqrt{x} - \sqrt{x^{3}}}{- x^{3} + x}$ |
| partial | concrete | `1/(sqrt(x) + sqrt(x**3))` | $\frac{1}{\sqrt{x} + \sqrt{x^{3}}}$ |
| partial | concrete | `1/(sqrt(x - 1) + sqrt((x - 1)**3))` | $\frac{1}{\sqrt{x - 1} + \sqrt{\left(x - 1\right)^{3}}}$ |
| **SOLVED-NEW** | concrete | `-3/(5*x + 4)**2 - (4*x + 5)/(sqrt(1 - x**2)*(5*x + 4)**2)` | $- \frac{3}{\left(5 x + 4\right)^{2}} - \frac{4 x + 5}{\sqrt{1 - x^{2}} \left(5 x + 4\right)^{2}}$ |
| partial | concrete | `(-4*x - 3*sqrt(1 - x**2) - 5)/(sqrt(1 - x**2)*(5*x + 4)**2)` | $\frac{- 4 x - 3 \sqrt{1 - x^{2}} - 5}{\sqrt{1 - x^{2}} \left(5 x + 4\right)^{2}}$ |
| partial | concrete | `1/(-3*x**2 + sqrt(1 - x**2)*(-4*x - 5) + 3)` | $\frac{1}{- 3 x^{2} + \sqrt{1 - x^{2}} \left(- 4 x - 5\right) + 3}$ |
| partial | concrete | `1/(-3*x**2 - 4*x*sqrt(1 - x**2) - 5*sqrt(1 - x**2) + 3)` | $\frac{1}{- 3 x^{2} - 4 x \sqrt{1 - x^{2}} - 5 \sqrt{1 - x^{2}} + 3}$ |
| partial | concrete | `(sqrt(1 - x**2) - 1)/(sqrt(1 - x**2)*(x - 2*sqrt(1 - x**2) + 2)**2)` | $\frac{\sqrt{1 - x^{2}} - 1}{\sqrt{1 - x^{2}} \left(x - 2 \sqrt{1 - x^{2}} + 2\right)^{2}}$ |
| partial | concrete | `sqrt(2*x**2 + 1)/(sqrt(2*x**2 + 1) + 1)` | $\frac{\sqrt{2 x^{2} + 1}}{\sqrt{2 x^{2} + 1} + 1}$ |
| partial | concrete | `sqrt(4*x**2 - 1)/(x + sqrt(4*x**2 - 1))` | $\frac{\sqrt{4 x^{2} - 1}}{x + \sqrt{4 x^{2} - 1}}$ |
| partial | parametric | `(a + b*x + c*x**2)/((d + e*x)**3*sqrt(x**2 - 1))` | $\frac{a + b x + c x^{2}}{\left(d + e x\right)^{3} \sqrt{x^{2} - 1}}$ |
| partial | concrete | `(2*x**8 + 1)/(x*(x**8 + 1)**(3/2))` | $\frac{2 x^{8} + 1}{x \left(x^{8} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(x**8 + 1)*(2*x**8 + 1)/(x**17 + 2*x**9 + x)` | $\frac{\sqrt{x^{8} + 1} \left(2 x^{8} + 1\right)}{x^{17} + 2 x^{9} + x}$ |
| SOLVED-both | concrete | `-9*x**2 + x/sqrt(1 - 9*x**2) + 1` | $- 9 x^{2} + \frac{x}{\sqrt{1 - 9 x^{2}}} + 1$ |
| partial | concrete | `(x + (1 - 9*x**2)**(3/2))/sqrt(1 - 9*x**2)` | $\frac{x + \left(1 - 9 x^{2}\right)^{\frac{3}{2}}}{\sqrt{1 - 9 x^{2}}}$ |
| partial | concrete | `(-3*sqrt(x) + x)**(2/3)*(2*sqrt(x) - 3)/sqrt(x)` | $\frac{\left(- 3 \sqrt{x} + x\right)^{\frac{2}{3}} \left(2 \sqrt{x} - 3\right)}{\sqrt{x}}$ |
| partial | concrete | `(-9*sqrt(x) + 2*x + 9)/(-3*sqrt(x) + x)**(1/3)` | $\frac{- 9 \sqrt{x} + 2 x + 9}{\sqrt[3]{- 3 \sqrt{x} + x}}$ |
| partial | concrete | `1/sqrt(4 - 9*x**2)` | $\frac{1}{\sqrt{4 - 9 x^{2}}}$ |
| partial | concrete | `1/(sqrt(2 - 3*x)*sqrt(3*x + 2))` | $\frac{1}{\sqrt{2 - 3 x} \sqrt{3 x + 2}}$ |
| partial | concrete | `1/sqrt((2 - 3*x)*(3*x + 2))` | $\frac{1}{\sqrt{\left(2 - 3 x\right) \left(3 x + 2\right)}}$ |
| partial | concrete | `1/sqrt(-x**2 - 2*x + 15)` | $\frac{1}{\sqrt{- x^{2} - 2 x + 15}}$ |
| partial | concrete | `1/(sqrt(3 - x)*sqrt(x + 5))` | $\frac{1}{\sqrt{3 - x} \sqrt{x + 5}}$ |
| partial | concrete | `1/sqrt((3 - x)*(x + 5))` | $\frac{1}{\sqrt{\left(3 - x\right) \left(x + 5\right)}}$ |
| partial | concrete | `1/sqrt(-x**2 - 8*x - 15)` | $\frac{1}{\sqrt{- x^{2} - 8 x - 15}}$ |
| partial | concrete | `1/(sqrt(-x - 3)*sqrt(x + 5))` | $\frac{1}{\sqrt{- x - 3} \sqrt{x + 5}}$ |
| partial | concrete | `1/sqrt((-x - 3)*(x + 5))` | $\frac{1}{\sqrt{\left(- x - 3\right) \left(x + 5\right)}}$ |
| SOLVED-both | concrete | `1 - sqrt(x)` | $1 - \sqrt{x}$ |
| partial | concrete | `(1 - x)/(sqrt(x) + 1)` | $\frac{1 - x}{\sqrt{x} + 1}$ |
| partial | concrete | `sqrt(1/(1 - x**2))` | $\sqrt{\frac{1}{1 - x^{2}}}$ |
| partial | concrete | `sqrt((x**2 + 1)/(1 - x**4))` | $\sqrt{\frac{x^{2} + 1}{1 - x^{4}}}$ |
| partial | concrete | `sqrt(1/(x**2 - 1))` | $\sqrt{\frac{1}{x^{2} - 1}}$ |
| partial | concrete | `sqrt((x**2 + 1)/(x**4 - 1))` | $\sqrt{\frac{x^{2} + 1}{x^{4} - 1}}$ |
| SOLVED-both | concrete | `1/sqrt(1 - x)` | $\frac{1}{\sqrt{1 - x}}$ |
| **SOLVED-NEW** | concrete | `sqrt(x + 1)/sqrt(1 - x**2)` | $\frac{\sqrt{x + 1}}{\sqrt{1 - x^{2}}}$ |
| SOLVED-both | concrete | `1/sqrt(x + 1)` | $\frac{1}{\sqrt{x + 1}}$ |
| **SOLVED-NEW** | concrete | `sqrt(1 - x)/sqrt(1 - x**2)` | $\frac{\sqrt{1 - x}}{\sqrt{1 - x^{2}}}$ |
| SOLVED-both | concrete | `sqrt(1 - x)` | $\sqrt{1 - x}$ |
| **SOLVED-NEW** | concrete | `sqrt(1 - x**2)/sqrt(x + 1)` | $\frac{\sqrt{1 - x^{2}}}{\sqrt{x + 1}}$ |
| SOLVED-both | concrete | `sqrt(x + 1)` | $\sqrt{x + 1}$ |
| **SOLVED-NEW** | concrete | `sqrt(1 - x**2)/sqrt(1 - x)` | $\frac{\sqrt{1 - x^{2}}}{\sqrt{1 - x}}$ |
| partial | concrete | `sqrt(3*x + 2)/sqrt(x + 1)` | $\frac{\sqrt{3 x + 2}}{\sqrt{x + 1}}$ |
| partial | concrete | `sqrt(1 - x)*sqrt(3*x + 2)/sqrt(1 - x**2)` | $\frac{\sqrt{1 - x} \sqrt{3 x + 2}}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `(x + 1)**(3/2)/(x*(1 - x)**(3/2))` | $\frac{\left(x + 1\right)^{\frac{3}{2}}}{x \left(1 - x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x + 1)**3/(x*(1 - x**2)**(3/2))` | $\frac{\left(x + 1\right)^{3}}{x \left(1 - x^{2}\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*x + 1)**(3/2)/(x*(-a*x + 1)**(3/2))` | $\frac{\left(a x + 1\right)^{\frac{3}{2}}}{x \left(- a x + 1\right)^{\frac{3}{2}}}$ |
| partial | parametric | `(a*x + 1)**3/(x*(-a**2*x**2 + 1)**(3/2))` | $\frac{\left(a x + 1\right)^{3}}{x \left(- a^{2} x^{2} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/sqrt(1 - x**2)` | $\frac{1}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `sqrt(x**2 + 1)/sqrt(1 - x**4)` | $\frac{\sqrt{x^{2} + 1}}{\sqrt{1 - x^{4}}}$ |
| partial | concrete | `1/sqrt(x**2 + 1)` | $\frac{1}{\sqrt{x^{2} + 1}}$ |
| partial | concrete | `sqrt(1 - x**2)/sqrt(1 - x**4)` | $\frac{\sqrt{1 - x^{2}}}{\sqrt{1 - x^{4}}}$ |
| partial | concrete | `sqrt(1 - x**2)` | $\sqrt{1 - x^{2}}$ |
| partial | concrete | `sqrt(1 - x**4)/sqrt(x**2 + 1)` | $\frac{\sqrt{1 - x^{4}}}{\sqrt{x^{2} + 1}}$ |
| partial | concrete | `sqrt(x**2 + 1)` | $\sqrt{x^{2} + 1}$ |
| partial | concrete | `sqrt(1 - x**4)/sqrt(1 - x**2)` | $\frac{\sqrt{1 - x^{4}}}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `1/(x - sqrt(x**2 + 1))` | $\frac{1}{x - \sqrt{x^{2} + 1}}$ |
| partial | concrete | `1/(x - sqrt(1 - x**2))` | $\frac{1}{x - \sqrt{1 - x^{2}}}$ |
| partial | concrete | `1/(x - sqrt(2*x**2 + 1))` | $\frac{1}{x - \sqrt{2 x^{2} + 1}}$ |
| partial | concrete | `(-x**3 + x**2*sqrt(2 - x**2) + 2*x)/(2*x**2 - 2)` | $\frac{- x^{3} + x^{2} \sqrt{2 - x^{2}} + 2 x}{2 x^{2} - 2}$ |
| partial | concrete | `x*sqrt(2 - x**2)/(x - sqrt(2 - x**2))` | $\frac{x \sqrt{2 - x^{2}}}{x - \sqrt{2 - x^{2}}}$ |
| partial | concrete | `x/(-x + sqrt(-x**2 + 2*x))` | $\frac{x}{- x + \sqrt{- x^{2} + 2 x}}$ |
| partial | concrete | `(x + sqrt(-x**2 + 2*x))/(2 - 2*x)` | $\frac{x + \sqrt{- x^{2} + 2 x}}{2 - 2 x}$ |
| partial | concrete | `(sqrt(x)*sqrt(2 - x) + x)/(2 - 2*x)` | $\frac{\sqrt{x} \sqrt{2 - x} + x}{2 - 2 x}$ |
| partial | concrete | `sqrt(x)/(-sqrt(x) + sqrt(2 - x))` | $\frac{\sqrt{x}}{- \sqrt{x} + \sqrt{2 - x}}$ |
| partial | concrete | `sqrt(x**2/(x**2 - 1))/(x**2 + 1)` | $\frac{\sqrt{\frac{x^{2}}{x^{2} - 1}}}{x^{2} + 1}$ |
| partial | parametric | `sqrt(x**2/(a + x**2*(a + 1) - 1))/(x**2 + 1)` | $\frac{\sqrt{\frac{x^{2}}{a + x^{2} \left(a + 1\right) - 1}}}{x^{2} + 1}$ |
| **SOLVED-NEW** | concrete | `(x**2 - 1)/(sqrt(x*(x**2 + 1))*(x**2 + 1))` | $\frac{x^{2} - 1}{\sqrt{x \left(x^{2} + 1\right)} \left(x^{2} + 1\right)}$ |
| **SOLVED-NEW** | concrete | `(x**2 - 1)/((x**2 + 1)*sqrt(x**3 + x))` | $\frac{x^{2} - 1}{\left(x^{2} + 1\right) \sqrt{x^{3} + x}}$ |
| **SOLVED-NEW** | concrete | `sqrt((x**2 - 1)**2/(x*(x**2 + 1)))/(x**2 + 1)` | $\frac{\sqrt{\frac{\left(x^{2} - 1\right)^{2}}{x \left(x^{2} + 1\right)}}}{x^{2} + 1}$ |
| **SOLVED-NEW** | concrete | `sqrt((x**2 - 1)**2/(x**3 + x))/(x**2 + 1)` | $\frac{\sqrt{\frac{\left(x^{2} - 1\right)^{2}}{x^{3} + x}}}{x^{2} + 1}$ |
| partial | parametric | `1/(sqrt(a + b/x**2)*sqrt(c + d*x**2))` | $\frac{1}{\sqrt{a + \frac{b}{x^{2}}} \sqrt{c + d x^{2}}}$ |
| partial | concrete | `sqrt(x**4 - 2*x**2)/((x**2 - 1)*(x**2 + 2))` | $\frac{\sqrt{x^{4} - 2 x^{2}}}{\left(x^{2} - 1\right) \left(x^{2} + 2\right)}$ |
| partial | concrete | `sqrt((x**4 - 2*x**2)/(x**2 - 1)**2)/(x**2 + 2)` | $\frac{\sqrt{\frac{x^{4} - 2 x^{2}}{\left(x^{2} - 1\right)^{2}}}}{x^{2} + 2}$ |
| partial | concrete | `(2*x/(x**2 + 1) + 1)**(5/2)` | $\left(\frac{2 x}{x^{2} + 1} + 1\right)^{\frac{5}{2}}$ |
| partial | concrete | `(2*x/(x**2 + 1) + 1)**(3/2)` | $\left(\frac{2 x}{x^{2} + 1} + 1\right)^{\frac{3}{2}}$ |
| partial | concrete | `sqrt(2*x/(x**2 + 1) + 1)` | $\sqrt{\frac{2 x}{x^{2} + 1} + 1}$ |
| partial | concrete | `1/sqrt(2*x/(x**2 + 1) + 1)` | $\frac{1}{\sqrt{\frac{2 x}{x^{2} + 1} + 1}}$ |
| partial | concrete | `(2*x/(x**2 + 1) + 1)**(-3/2)` | $\frac{1}{\left(\frac{2 x}{x^{2} + 1} + 1\right)^{\frac{3}{2}}}$ |
| **SOLVED-NEW** | concrete | `sqrt(2*x/(x**2 + 1) + 1)/(x**2 + 1)` | $\frac{\sqrt{\frac{2 x}{x^{2} + 1} + 1}}{x^{2} + 1}$ |
| partial | parametric | `x**2*(c/(a + b*x**2))**(3/2)` | $x^{2} \left(\frac{c}{a + b x^{2}}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `x*(c/(a + b*x**2))**(3/2)` | $x \left(\frac{c}{a + b x^{2}}\right)^{\frac{3}{2}}$ |
| SOLVED-both | parametric | `(c/(a + b*x**2))**(3/2)` | $\left(\frac{c}{a + b x^{2}}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(c/(a + b*x**2))**(3/2)/x` | $\frac{\left(\frac{c}{a + b x^{2}}\right)^{\frac{3}{2}}}{x}$ |
| **SOLVED-NEW** | parametric | `(c/(a + b*x**2))**(3/2)/x**2` | $\frac{\left(\frac{c}{a + b x^{2}}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(c/(a + b*x**2))**(3/2)/x**3` | $\frac{\left(\frac{c}{a + b x^{2}}\right)^{\frac{3}{2}}}{x^{3}}$ |
| partial | parametric | `x**2*(c*(a + b*x**2)**3)**(3/2)` | $x^{2} \left(c \left(a + b x^{2}\right)^{3}\right)^{\frac{3}{2}}$ |
| **SOLVED-NEW** | parametric | `x*(c*(a + b*x**2)**3)**(3/2)` | $x \left(c \left(a + b x^{2}\right)^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(c*(a + b*x**2)**3)**(3/2)` | $\left(c \left(a + b x^{2}\right)^{3}\right)^{\frac{3}{2}}$ |
| partial | parametric | `(c*(a + b*x**2)**3)**(3/2)/x` | $\frac{\left(c \left(a + b x^{2}\right)^{3}\right)^{\frac{3}{2}}}{x}$ |
| partial | parametric | `(c*(a + b*x**2)**3)**(3/2)/x**2` | $\frac{\left(c \left(a + b x^{2}\right)^{3}\right)^{\frac{3}{2}}}{x^{2}}$ |
| partial | parametric | `(c*(a + b*x**2)**3)**(3/2)/x**3` | $\frac{\left(c \left(a + b x^{2}\right)^{3}\right)^{\frac{3}{2}}}{x^{3}}$ |
| NIE | concrete | `sqrt(-x**2 + x)*F(x)` | $\sqrt{- x^{2} + x} F{\left(x \right)}$ |
| NIE | concrete | `F(x)/sqrt(-x**2 + x)` | $\frac{F{\left(x \right)}}{\sqrt{- x^{2} + x}}$ |
| NIE | concrete | `sqrt(x)*sqrt(1 - x)*F(x)` | $\sqrt{x} \sqrt{1 - x} F{\left(x \right)}$ |
| NIE | concrete | `F(x)/(sqrt(x)*sqrt(1 - x))` | $\frac{F{\left(x \right)}}{\sqrt{x} \sqrt{1 - x}}$ |
| NIE | parametric | `sqrt(b*x**2 + sqrt(a + b**2*x**4))/sqrt(a + b**2*x**4)` | $\frac{\sqrt{b x^{2} + \sqrt{a + b^{2} x^{4}}}}{\sqrt{a + b^{2} x^{4}}}$ |
| NIE | parametric | `sqrt(-b*x**2 + sqrt(a + b**2*x**4))/sqrt(a + b**2*x**4)` | $\frac{\sqrt{- b x^{2} + \sqrt{a + b^{2} x^{4}}}}{\sqrt{a + b^{2} x^{4}}}$ |
| NIE | parametric | `sqrt(2*x**2 + sqrt(4*x**4 + 3))/((c + d*x)*sqrt(4*x**4 + 3))` | $\frac{\sqrt{2 x^{2} + \sqrt{4 x^{4} + 3}}}{\left(c + d x\right) \sqrt{4 x^{4} + 3}}$ |
| NIE | parametric | `sqrt(2*x**2 + sqrt(4*x**4 + 3))/((c + d*x)**2*sqrt(4*x**4 + 3))` | $\frac{\sqrt{2 x^{2} + \sqrt{4 x^{4} + 3}}}{\left(c + d x\right)^{2} \sqrt{4 x^{4} + 3}}$ |
| partial | concrete | `(x - 4)/(sqrt(x)*(x**(1/3) + 1))` | $\frac{x - 4}{\sqrt{x} \left(\sqrt[3]{x} + 1\right)}$ |
| partial | concrete | `(sqrt(x) + 1)/(x**(7/6) + x**(5/6))` | $\frac{\sqrt{x} + 1}{x^{\frac{7}{6}} + x^{\frac{5}{6}}}$ |
| partial | concrete | `(sqrt(x) + 1)/(sqrt(x)*(x**(1/3) + 1))` | $\frac{\sqrt{x} + 1}{\sqrt{x} \left(\sqrt[3]{x} + 1\right)}$ |
| partial | parametric | `sqrt(b/x**2 + 2)/(b + 2*x**2)` | $\frac{\sqrt{\frac{b}{x^{2}} + 2}}{b + 2 x^{2}}$ |
| partial | parametric | `sqrt(-b/x**2 + 2)/(-b + 2*x**2)` | $\frac{\sqrt{- \frac{b}{x^{2}} + 2}}{- b + 2 x^{2}}$ |
| partial | parametric | `sqrt(a + c/x**2)/(d + e*x)` | $\frac{\sqrt{a + \frac{c}{x^{2}}}}{d + e x}$ |
| partial | parametric | `sqrt(a + b/x + c/x**2)/(d + e*x)` | $\frac{\sqrt{a + \frac{b}{x} + \frac{c}{x^{2}}}}{d + e x}$ |
| partial | concrete | `(x**(1/6) + (x**3)**(1/5))/sqrt(x)` | $\frac{\sqrt[6]{x} + \sqrt[5]{x^{3}}}{\sqrt{x}}$ |
| partial | concrete | `(x + 2)/sqrt(-x**2 + 4*x)` | $\frac{x + 2}{\sqrt{- x^{2} + 4 x}}$ |
| SOLVED-both | concrete | `(x + 3)/(x**2 + 6*x)**(1/3)` | $\frac{x + 3}{\sqrt[3]{x^{2} + 6 x}}$ |
| SOLVED-both | concrete | `(x + 4)/(-x**2 + 6*x)**(3/2)` | $\frac{x + 4}{\left(- x^{2} + 6 x\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((x + 1)*sqrt(x**2 + 2*x))` | $\frac{1}{\left(x + 1\right) \sqrt{x^{2} + 2 x}}$ |
| partial | concrete | `1/((2*x + 1)*sqrt(x**2 + x))` | $\frac{1}{\left(2 x + 1\right) \sqrt{x^{2} + x}}$ |
| SOLVED-both | concrete | `(x - 1)/sqrt(-x**2 + 2*x)` | $\frac{x - 1}{\sqrt{- x^{2} + 2 x}}$ |
| partial | concrete | `sqrt(-x**2 + x)/(x + 1)` | $\frac{\sqrt{- x^{2} + x}}{x + 1}$ |
| partial | concrete | `sqrt(x**(1/4) + x)` | $\sqrt{\sqrt[4]{x} + x}$ |
| partial | concrete | `sqrt(x**(3/2) + x)` | $\sqrt{x^{\frac{3}{2}} + x}$ |
| partial | concrete | `x*sqrt(x**(3/2) + x)` | $x \sqrt{x^{\frac{3}{2}} + x}$ |
| SOLVED-both | concrete | `(1 - x**2)*sqrt(1/(2 - x**2))` | $\left(1 - x^{2}\right) \sqrt{\frac{1}{2 - x^{2}}}$ |
| partial | concrete | `sqrt(-x**4 + x**3 + x**2)` | $\sqrt{- x^{4} + x^{3} + x^{2}}$ |
| **SOLVED-NEW** | parametric | `1/sqrt((a**2 + x**2)**3)` | $\frac{1}{\sqrt{\left(a^{2} + x^{2}\right)^{3}}}$ |
| partial | concrete | `sqrt(x)/(sqrt(x) + x + 1)` | $\frac{\sqrt{x}}{\sqrt{x} + x + 1}$ |
| partial | concrete | `x/(sqrt(x) + x + 1)` | $\frac{x}{\sqrt{x} + x + 1}$ |
| NIE | concrete | `1/(sqrt(x)*(sqrt(x) + x + 1)**(7/2))` | $\frac{1}{\sqrt{x} \left(\sqrt{x} + x + 1\right)^{\frac{7}{2}}}$ |
| partial | concrete | `(x - 1)/(sqrt(x**2 + 1) + 1)` | $\frac{x - 1}{\sqrt{x^{2} + 1} + 1}$ |
| **SOLVED-NEW** | concrete | `1/((x + 1)**(2/3)*(x**2 - 1)**(2/3))` | $\frac{1}{\left(x + 1\right)^{\frac{2}{3}} \left(x^{2} - 1\right)^{\frac{2}{3}}}$ |
| SOLVED-both | concrete | `(1 - x**6)**(2/3) + (1 - x**6)**(2/3)/x**6` | $\left(1 - x^{6}\right)^{\frac{2}{3}} + \frac{\left(1 - x^{6}\right)^{\frac{2}{3}}}{x^{6}}$ |
| SOLVED-both | concrete | `(-2*x**3 + x)/sqrt(3*x + 2)` | $\frac{- 2 x^{3} + x}{\sqrt{3 x + 2}}$ |
| partial | concrete | `1/((x + 1)**(1/4) + sqrt(x + 1))` | $\frac{1}{\sqrt[4]{x + 1} + \sqrt{x + 1}}$ |
| SOLVED-both | concrete | `(2*x + 1)/sqrt(x**2 + x)` | $\frac{2 x + 1}{\sqrt{x^{2} + x}}$ |
| partial | concrete | `1/(2*sqrt(x)*(x + 1))` | $\frac{1}{2 \sqrt{x} \left(x + 1\right)}$ |
| **SOLVED-NEW** | concrete | `1/(x*sqrt(-x**2 + 6*x))` | $\frac{1}{x \sqrt{- x^{2} + 6 x}}$ |
| SOLVED-both | concrete | `sqrt(x)*(sqrt(x) + 1)` | $\sqrt{x} \left(\sqrt{x} + 1\right)$ |
| partial | concrete | `(1 - sqrt(x))/x**(1/3)` | $\frac{1 - \sqrt{x}}{\sqrt[3]{x}}$ |
| partial | concrete | `sqrt(x)/(x**(1/3) + 1)` | $\frac{\sqrt{x}}{\sqrt[3]{x} + 1}$ |
| partial | concrete | `(sqrt(x) + 1)**(1/3)/x` | $\frac{\sqrt[3]{\sqrt{x} + 1}}{x}$ |
| SOLVED-both | concrete | `1 - sqrt(x)` | $1 - \sqrt{x}$ |
| SOLVED-both | concrete | `1 - x**(1/4)` | $1 - \sqrt[4]{x}$ |
| SOLVED-both | concrete | `(1 - sqrt(x))/(x**(1/4) + 1)` | $\frac{1 - \sqrt{x}}{\sqrt[4]{x} + 1}$ |
| partial | parametric | `1/sqrt((a + b*x)*(c + d*x))` | $\frac{1}{\sqrt{\left(a + b x\right) \left(c + d x\right)}}$ |
| partial | parametric | `1/sqrt((a + b*x)*(c - d*x))` | $\frac{1}{\sqrt{\left(a + b x\right) \left(c - d x\right)}}$ |
| partial | concrete | `1/(sqrt(x)*(1 - x**2))` | $\frac{1}{\sqrt{x} \left(1 - x^{2}\right)}$ |
| partial | concrete | `sqrt(x)/(-x**3 + x)` | $\frac{\sqrt{x}}{- x^{3} + x}$ |
| **SOLVED-NEW** | concrete | `sqrt(x**3 + x**2)` | $\sqrt{x^{3} + x^{2}}$ |
| partial | concrete | `1/((x + 1)*sqrt(x**2 + 2*x))` | $\frac{1}{\left(x + 1\right) \sqrt{x^{2} + 2 x}}$ |
| NIE | concrete | `sqrt(x)*sqrt(-sqrt(x) - x + 1)` | $\sqrt{x} \sqrt{- \sqrt{x} - x + 1}$ |
| NIE | concrete | `(sqrt(x - 3) + 1)**(1/3)` | $\sqrt[3]{\sqrt{x - 3} + 1}$ |
| NIE | concrete | `1/sqrt(sqrt(2*x - 1) + 3)` | $\frac{1}{\sqrt{\sqrt{2 x - 1} + 3}}$ |
| partial | concrete | `sqrt(1 - x)/(sqrt(x) + 1)` | $\frac{\sqrt{1 - x}}{\sqrt{x} + 1}$ |
| partial | concrete | `sqrt(1 - x)/(1 - sqrt(x))` | $\frac{\sqrt{1 - x}}{1 - \sqrt{x}}$ |
| partial | concrete | `x/(x - sqrt(x**2 + 1))` | $\frac{x}{x - \sqrt{x^{2} + 1}}$ |
| partial | concrete | `x/(x - sqrt(1 - x**2))` | $\frac{x}{x - \sqrt{1 - x^{2}}}$ |
| partial | concrete | `x/(x - sqrt(2*x**2 + 1))` | $\frac{x}{x - \sqrt{2 x^{2} + 1}}$ |
| partial | concrete | `sqrt(x)*sqrt(sqrt(x) + x)` | $\sqrt{x} \sqrt{\sqrt{x} + x}$ |
| partial | concrete | `(x**(1/3) + 1)/(sqrt(x) + 1)` | $\frac{\sqrt[3]{x} + 1}{\sqrt{x} + 1}$ |
| partial | concrete | `(x**(1/3) + 1)/(x**(1/4) + 1)` | $\frac{\sqrt[3]{x} + 1}{\sqrt[4]{x} + 1}$ |
| partial | concrete | `x**2/(x**2 + sqrt(1 - x**2) - 1)` | $\frac{x^{2}}{x^{2} + \sqrt{1 - x^{2}} - 1}$ |
| partial | concrete | `sqrt((x + 1)/x)` | $\sqrt{\frac{x + 1}{x}}$ |
| partial | concrete | `sqrt((1 - x)/x)` | $\sqrt{\frac{1 - x}{x}}$ |
| partial | concrete | `sqrt((x + 1)/x)/x` | $\frac{\sqrt{\frac{x + 1}{x}}}{x}$ |
| partial | concrete | `sqrt(x/(x + 1))` | $\sqrt{\frac{x}{x + 1}}$ |
| partial | concrete | `1/sqrt((-x - 1)/x)` | $\frac{1}{\sqrt{\frac{- x - 1}{x}}}$ |
| partial | concrete | `sqrt(x*(4 - x))` | $\sqrt{x \left(4 - x\right)}$ |
| partial | concrete | `1/sqrt(x*(1 - x))` | $\frac{1}{\sqrt{x \left(1 - x\right)}}$ |
| **SOLVED-NEW** | concrete | `x/(x*(x + 2))**(3/2)` | $\frac{x}{\left(x \left(x + 2\right)\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(1 + 1/x)/(1 - x**2)` | $\frac{\sqrt{1 + \frac{1}{x}}}{1 - x^{2}}$ |
| partial | parametric | `sqrt((-a + x)*(b - x))` | $\sqrt{\left(- a + x\right) \left(b - x\right)}$ |
| partial | parametric | `1/sqrt((-a + x)*(b - x))` | $\frac{1}{\sqrt{\left(- a + x\right) \left(b - x\right)}}$ |
| partial | concrete | `sqrt((1 - x**2)*(x**2 + 3))` | $\sqrt{\left(1 - x^{2}\right) \left(x^{2} + 3\right)}$ |
| partial | concrete | `1/sqrt((1 - x**2)*(x**2 + 3))` | $\frac{1}{\sqrt{\left(1 - x^{2}\right) \left(x^{2} + 3\right)}}$ |
| partial | parametric | `1/sqrt(a*x + b*x**2)` | $\frac{1}{\sqrt{a x + b x^{2}}}$ |
| partial | parametric | `1/sqrt(x*(a + b*x))` | $\frac{1}{\sqrt{x \left(a + b x\right)}}$ |
| partial | parametric | `1/sqrt(x**2*(a/x + b))` | $\frac{1}{\sqrt{x^{2} \left(\frac{a}{x} + b\right)}}$ |
| partial | parametric | `1/sqrt(x**3*(a/x**2 + b/x))` | $\frac{1}{\sqrt{x^{3} \left(\frac{a}{x^{2}} + \frac{b}{x}\right)}}$ |
| partial | parametric | `1/sqrt((a*x**2 + b*x**3)/x)` | $\frac{1}{\sqrt{\frac{a x^{2} + b x^{3}}{x}}}$ |
| partial | parametric | `1/sqrt((a*x**3 + b*x**4)/x**2)` | $\frac{1}{\sqrt{\frac{a x^{3} + b x^{4}}{x^{2}}}}$ |
| partial | parametric | `1/sqrt(a*c*x + b*c*x**2)` | $\frac{1}{\sqrt{a c x + b c x^{2}}}$ |
| partial | parametric | `1/sqrt(c*(a*x + b*x**2))` | $\frac{1}{\sqrt{c \left(a x + b x^{2}\right)}}$ |
| partial | parametric | `1/sqrt(c*x*(a + b*x))` | $\frac{1}{\sqrt{c x \left(a + b x\right)}}$ |
| partial | parametric | `1/sqrt(c*x**2*(a/x + b))` | $\frac{1}{\sqrt{c x^{2} \left(\frac{a}{x} + b\right)}}$ |
| NIE | concrete | `sqrt(-x**2 + x*sqrt(x**2 - 1) + 1)` | $\sqrt{- x^{2} + x \sqrt{x^{2} - 1} + 1}$ |
| NIE | concrete | `sqrt(sqrt(x)*sqrt(x + 1) - x)/sqrt(x + 1)` | $\frac{\sqrt{\sqrt{x} \sqrt{x + 1} - x}}{\sqrt{x + 1}}$ |
| partial | concrete | `(-x - 2*sqrt(x**2 + 1))/(x**3 + x + sqrt(x**2 + 1))` | $\frac{- x - 2 \sqrt{x^{2} + 1}}{x^{3} + x + \sqrt{x^{2} + 1}}$ |
| partial | concrete | `(2*x + 1)/((x**2 + 1)*sqrt(x**2 + 2*x + 2))` | $\frac{2 x + 1}{\left(x^{2} + 1\right) \sqrt{x^{2} + 2 x + 2}}$ |
| NIE | concrete | `1/(sqrt(-x**2 + sqrt(x**4 + 1))*(x**4 + 1))` | $\frac{1}{\sqrt{- x^{2} + \sqrt{x^{4} + 1}} \left(x^{4} + 1\right)}$ |
| NIE | parametric | `1/((a + b*x**4)*sqrt(c*x**2 + d*sqrt(a + b*x**4)))` | $\frac{1}{\left(a + b x^{4}\right) \sqrt{c x^{2} + d \sqrt{a + b x^{4}}}}$ |
| NIE | parametric | `1/((a + b*x**4)*sqrt(-c*x**2 + d*sqrt(a + b*x**4)))` | $\frac{1}{\left(a + b x^{4}\right) \sqrt{- c x^{2} + d \sqrt{a + b x^{4}}}}$ |
| partial | parametric | `x/sqrt(a + b*c**4 + 4*b*c**3*d*x + 6*b*c**2*d**2*x**2 + 4*b*c*d**3*x**3 + b*d**4*x**4)` | $\frac{x}{\sqrt{a + b c^{4} + 4 b c^{3} d x + 6 b c^{2} d^{2} x^{2} + 4 b c d^{3} x^{3} + b d^{4} x^{4}}}$ |
| partial | parametric | `1/sqrt(a + b*c**4 + 4*b*c**3*d*x + 6*b*c**2*d**2*x**2 + 4*b*c*d**3*x**3 + b*d**4*x**4)` | $\frac{1}{\sqrt{a + b c^{4} + 4 b c^{3} d x + 6 b c^{2} d^{2} x^{2} + 4 b c d^{3} x^{3} + b d^{4} x^{4}}}$ |
| partial | parametric | `(a - c*x**4)/(sqrt(a + b*x**2 + c*x**4)*(a*d + a*e*x**2 + c*d*x**4))` | $\frac{a - c x^{4}}{\sqrt{a + b x^{2} + c x^{4}} \left(a d + a e x^{2} + c d x^{4}\right)}$ |
| partial | parametric | `(a - c*x**4)/(sqrt(a - b*x**2 + c*x**4)*(a*d + a*e*x**2 + c*d*x**4))` | $\frac{a - c x^{4}}{\sqrt{a - b x^{2} + c x^{4}} \left(a d + a e x^{2} + c d x^{4}\right)}$ |
| partial | concrete | `1/((x**3 + 8)*sqrt(x**2 - 2*x + 5))` | $\frac{1}{\left(x^{3} + 8\right) \sqrt{x^{2} - 2 x + 5}}$ |
| SOLVED-both | concrete | `sqrt(x**2/(x**2 + 1))` | $\sqrt{\frac{x^{2}}{x^{2} + 1}}$ |
| partial | parametric | `(-e*f*x**2 + e*f)/((a*d*x**2 + a*d + b*d*x)*sqrt(a*x**4 + a + b*x**3 + b*x + c*x**2))` | $\frac{- e f x^{2} + e f}{\left(a d x^{2} + a d + b d x\right) \sqrt{a x^{4} + a + b x^{3} + b x + c x^{2}}}$ |
| partial | parametric | `(-e*f*x**2 + e*f)/((-a*d*x**2 - a*d + b*d*x)*sqrt(-a*x**4 - a + b*x**3 + b*x + c*x**2))` | $\frac{- e f x^{2} + e f}{\left(- a d x^{2} - a d + b d x\right) \sqrt{- a x^{4} - a + b x^{3} + b x + c x^{2}}}$ |
| NIE | parametric | `sqrt(a*x**2 + b*x*sqrt(a**2*x**2/b**2 - a/b**2))/(x*sqrt(a**2*x**2/b**2 - a/b**2))` | $\frac{\sqrt{a x^{2} + b x \sqrt{\frac{a^{2} x^{2}}{b^{2}} - \frac{a}{b^{2}}}}}{x \sqrt{\frac{a^{2} x^{2}}{b^{2}} - \frac{a}{b^{2}}}}$ |
| NIE | parametric | `sqrt(-a*x**2 + b*x*sqrt(a**2*x**2/b**2 + a/b**2))/(x*sqrt(a**2*x**2/b**2 + a/b**2))` | $\frac{\sqrt{- a x^{2} + b x \sqrt{\frac{a^{2} x^{2}}{b^{2}} + \frac{a}{b^{2}}}}}{x \sqrt{\frac{a^{2} x^{2}}{b^{2}} + \frac{a}{b^{2}}}}$ |
| NIE | parametric | `sqrt(x*(a*x + b*sqrt(a**2*x**2/b**2 - a/b**2)))/(x*sqrt(a**2*x**2/b**2 - a/b**2))` | $\frac{\sqrt{x \left(a x + b \sqrt{\frac{a^{2} x^{2}}{b^{2}} - \frac{a}{b^{2}}}\right)}}{x \sqrt{\frac{a^{2} x^{2}}{b^{2}} - \frac{a}{b^{2}}}}$ |
| NIE | parametric | `sqrt(x*(-a*x + b*sqrt(a**2*x**2/b**2 + a/b**2)))/(x*sqrt(a**2*x**2/b**2 + a/b**2))` | $\frac{\sqrt{x \left(- a x + b \sqrt{\frac{a^{2} x^{2}}{b^{2}} + \frac{a}{b^{2}}}\right)}}{x \sqrt{\frac{a^{2} x^{2}}{b^{2}} + \frac{a}{b^{2}}}}$ |
| SOLVED-both | concrete | `(x*sqrt(x - 4) + x*sqrt(x - 1) - sqrt(x - 4) - 4*sqrt(x - 1))/((x**2 - 5*x + 4)*(sqrt(x - 4) + sqrt(x - 1) + 1))` | $\frac{x \sqrt{x - 4} + x \sqrt{x - 1} - \sqrt{x - 4} - 4 \sqrt{x - 1}}{\left(x^{2} - 5 x + 4\right) \left(\sqrt{x - 4} + \sqrt{x - 1} + 1\right)}$ |
| partial | concrete | `1/(x*(x**2 + 3*x + 3)*(x**3 + 3*x**2 + 3*x + 3)**(1/3))` | $\frac{1}{x \left(x^{2} + 3 x + 3\right) \sqrt[3]{x^{3} + 3 x^{2} + 3 x + 3}}$ |
| partial | concrete | `(1 - x**2)/((1 - x**3)**(2/3)*(x**2 - x + 1))` | $\frac{1 - x^{2}}{\left(1 - x^{3}\right)^{\frac{2}{3}} \left(x^{2} - x + 1\right)}$ |
| partial | concrete | `x**2/(sqrt(x**4 - 1)*(x**4 + 1))` | $\frac{x^{2}}{\sqrt{x^{4} - 1} \left(x^{4} + 1\right)}$ |
| partial | parametric | `(a - c*x**4)/((d + e*x**2)*(a*e + c*d*x**2)*sqrt(a + b*x**2 + c*x**4))` | $\frac{a - c x^{4}}{\left(d + e x^{2}\right) \left(a e + c d x^{2}\right) \sqrt{a + b x^{2} + c x^{4}}}$ |
| partial | concrete | `1/(sqrt(1 - x**2) + 1/x)` | $\frac{1}{\sqrt{1 - x^{2}} + \frac{1}{x}}$ |
| partial | parametric | `x/sqrt(-44375*b**4 + 576000*b**3*c*x + 576000*b**2*c**2*x**2 + 5308416*c**4*x**4)` | $\frac{x}{\sqrt{- 44375 b^{4} + 576000 b^{3} c x + 576000 b^{2} c^{2} x^{2} + 5308416 c^{4} x^{4}}}$ |
