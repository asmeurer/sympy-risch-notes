# 2-3. Exponentials and logarithms (radical cases)

All attempted radical cases from this part of the Rubi corpus, run through `risch_integrate(f, x, algebraic=True)` (sympy branch `risch-algebraic`).  **SOLVED-NEW** means solved here but not by sympy's non-risch `integrate()`; SOLVED-both means both solve it.  131 cases: partial 82 (63%), NIE 21 (16%), SOLVED-both 21 (16%), SOLVED-NEW 6 (5%), timeout 1 (1%).

| Status | Kind | SymPy expression | Math |
|---|---|---|---|
| NIE | parametric | `x**(13/2)*exp(-b*x)` | $x^{\frac{13}{2}} e^{- b x}$ |
| NIE | parametric | `(a + b*exp(x))*sqrt(c + d*x)` | $\left(a + b e^{x}\right) \sqrt{c + d x}$ |
| NIE | parametric | `(a + b*exp(x))**2*sqrt(c + d*x)` | $\left(a + b e^{x}\right)^{2} \sqrt{c + d x}$ |
| NIE | parametric | `(a + b*exp(x))**3*sqrt(c + d*x)` | $\left(a + b e^{x}\right)^{3} \sqrt{c + d x}$ |
| partial | parametric | `sqrt(c + d*x)/(a + b*exp(x))` | $\frac{\sqrt{c + d x}}{a + b e^{x}}$ |
| partial | parametric | `sqrt(c + d*x)/(a + b*exp(x))**2` | $\frac{\sqrt{c + d x}}{\left(a + b e^{x}\right)^{2}}$ |
| partial | parametric | `sqrt(c + d*x)/(a + b*exp(x))**3` | $\frac{\sqrt{c + d x}}{\left(a + b e^{x}\right)^{3}}$ |
| SOLVED-both | parametric | `exp(4*x)/(a + b*exp(2*x))**(2/3)` | $\frac{e^{4 x}}{\left(a + b e^{2 x}\right)^{\frac{2}{3}}}$ |
| partial | concrete | `exp(sqrt(3*x + 5))` | $e^{\sqrt{3 x + 5}}$ |
| NIE | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(7/2)*exp(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{7}{2}} e^{a + b x + c x^{2}}$ |
| NIE | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(5/2)*exp(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{5}{2}} e^{a + b x + c x^{2}}$ |
| NIE | parametric | `(b + 2*c*x)*(a + b*x + c*x**2)**(3/2)*exp(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \left(a + b x + c x^{2}\right)^{\frac{3}{2}} e^{a + b x + c x^{2}}$ |
| NIE | parametric | `(b + 2*c*x)*sqrt(a + b*x + c*x**2)*exp(a + b*x + c*x**2)` | $\left(b + 2 c x\right) \sqrt{a + b x + c x^{2}} e^{a + b x + c x^{2}}$ |
| NIE | parametric | `(b + 2*c*x)*exp(a + b*x + c*x**2)/sqrt(a + b*x + c*x**2)` | $\frac{\left(b + 2 c x\right) e^{a + b x + c x^{2}}}{\sqrt{a + b x + c x^{2}}}$ |
| NIE | parametric | `(b + 2*c*x)*exp(a + b*x + c*x**2)/(a + b*x + c*x**2)**(3/2)` | $\frac{\left(b + 2 c x\right) e^{a + b x + c x^{2}}}{\left(a + b x + c x^{2}\right)^{\frac{3}{2}}}$ |
| NIE | parametric | `(b + 2*c*x)*exp(a + b*x + c*x**2)/(a + b*x + c*x**2)**(5/2)` | $\frac{\left(b + 2 c x\right) e^{a + b x + c x^{2}}}{\left(a + b x + c x^{2}\right)^{\frac{5}{2}}}$ |
| NIE | parametric | `(b + 2*c*x)*exp(a + b*x + c*x**2)/(a + b*x + c*x**2)**(7/2)` | $\frac{\left(b + 2 c x\right) e^{a + b x + c x^{2}}}{\left(a + b x + c x^{2}\right)^{\frac{7}{2}}}$ |
| NIE | parametric | `(b + 2*c*x)*exp(a + b*x + c*x**2)/(a + b*x + c*x**2)**(9/2)` | $\frac{\left(b + 2 c x\right) e^{a + b x + c x^{2}}}{\left(a + b x + c x^{2}\right)^{\frac{9}{2}}}$ |
| partial | concrete | `exp(-x)/sqrt(1 - exp(-2*x))` | $\frac{e^{- x}}{\sqrt{1 - e^{- 2 x}}}$ |
| partial | concrete | `sqrt(3 - 4*exp(2*x))*exp(x)` | $\sqrt{3 - 4 e^{2 x}} e^{x}$ |
| partial | concrete | `sqrt(1 - exp(2*x))*exp(x)` | $\sqrt{1 - e^{2 x}} e^{x}$ |
| partial | concrete | `exp(x)/sqrt(exp(2*x) + exp(x) + 1)` | $\frac{e^{x}}{\sqrt{e^{2 x} + e^{x} + 1}}$ |
| partial | concrete | `exp(x)/sqrt(1 - exp(2*x))` | $\frac{e^{x}}{\sqrt{1 - e^{2 x}}}$ |
| partial | concrete | `exp(x)/sqrt(exp(2*x) + 1)` | $\frac{e^{x}}{\sqrt{e^{2 x} + 1}}$ |
| partial | concrete | `exp(sqrt(x + 4))/sqrt(x + 4)` | $\frac{e^{\sqrt{x + 4}}}{\sqrt{x + 4}}$ |
| partial | concrete | `x/sqrt(exp(2*x**2) - 1)` | $\frac{x}{\sqrt{e^{2 x^{2}} - 1}}$ |
| partial | concrete | `sqrt(exp(2*x) + 9)*exp(x)` | $\sqrt{e^{2 x} + 9} e^{x}$ |
| partial | concrete | `sqrt(exp(2*x) + 1)*exp(x)` | $\sqrt{e^{2 x} + 1} e^{x}$ |
| partial | concrete | `x**2*exp(x**(3/2))` | $x^{2} e^{x^{\frac{3}{2}}}$ |
| partial | concrete | `exp(x)/sqrt(exp(2*x) - 3)` | $\frac{e^{x}}{\sqrt{e^{2 x} - 3}}$ |
| partial | concrete | `exp(4*x)/sqrt(exp(8*x) + 16)` | $\frac{e^{4 x}}{\sqrt{e^{8 x} + 16}}$ |
| partial | concrete | `exp(sqrt(x))/sqrt(x)` | $\frac{e^{\sqrt{x}}}{\sqrt{x}}$ |
| partial | concrete | `exp(x**(1/3))/x**(2/3)` | $\frac{e^{\sqrt[3]{x}}}{x^{\frac{2}{3}}}$ |
| SOLVED-both | concrete | `exp(2*x)/(exp(x) + 1)**(1/3)` | $\frac{e^{2 x}}{\sqrt[3]{e^{x} + 1}}$ |
| SOLVED-both | concrete | `exp(2*x)/(exp(x) + 1)**(1/4)` | $\frac{e^{2 x}}{\sqrt[4]{e^{x} + 1}}$ |
| partial | concrete | `(2*exp(2*x) - exp(x))/sqrt(3*exp(2*x) - 6*exp(x) - 1)` | $\frac{2 e^{2 x} - e^{x}}{\sqrt{3 e^{2 x} - 6 e^{x} - 1}}$ |
| partial | parametric | `1/sqrt(a + b*exp(c + d*x))` | $\frac{1}{\sqrt{a + b e^{c + d x}}}$ |
| partial | parametric | `1/sqrt(-a + b*exp(c + d*x))` | $\frac{1}{\sqrt{- a + b e^{c + d x}}}$ |
| partial | parametric | `sqrt(a + b*exp(c + d*x))` | $\sqrt{a + b e^{c + d x}}$ |
| partial | parametric | `sqrt(-a + b*exp(c + d*x))` | $\sqrt{- a + b e^{c + d x}}$ |
| SOLVED-both | concrete | `exp(-x)/sqrt(exp(2*x) + 1)` | $\frac{e^{- x}}{\sqrt{e^{2 x} + 1}}$ |
| partial | concrete | `sqrt(9 - exp(2*x))*exp(x)` | $\sqrt{9 - e^{2 x}} e^{x}$ |
| SOLVED-both | concrete | `sqrt(9 - exp(2*x))*exp(6*x)` | $\sqrt{9 - e^{2 x}} e^{6 x}$ |
| SOLVED-both | concrete | `exp(6*x)/(9 - exp(x))**(5/2)` | $\frac{e^{6 x}}{\left(9 - e^{x}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x*sqrt(1 - exp(2*x**2))*exp(x**2)` | $x \sqrt{1 - e^{2 x^{2}}} e^{x^{2}}$ |
| partial | concrete | `exp(3*x)/sqrt(16*exp(2*x) + 25)` | $\frac{e^{3 x}}{\sqrt{16 e^{2 x} + 25}}$ |
| SOLVED-both | concrete | `(exp(x) + 1)/sqrt(x + exp(x))` | $\frac{e^{x} + 1}{\sqrt{x + e^{x}}}$ |
| **SOLVED-NEW** | concrete | `exp(x)/sqrt(x + exp(x)) + 1/sqrt(x + exp(x))` | $\frac{e^{x}}{\sqrt{x + e^{x}}} + \frac{1}{\sqrt{x + e^{x}}}$ |
| partial | concrete | `x*(exp(x) + 1)/sqrt(x + exp(x)) + 2*sqrt(x + exp(x))` | $\frac{x \left(e^{x} + 1\right)}{\sqrt{x + e^{x}}} + 2 \sqrt{x + e^{x}}$ |
| partial | concrete | `x*exp(x)/sqrt(x + exp(x)) + x/sqrt(x + exp(x)) + 2*sqrt(x + exp(x))` | $\frac{x e^{x}}{\sqrt{x + e^{x}}} + \frac{x}{\sqrt{x + e^{x}}} + 2 \sqrt{x + e^{x}}$ |
| partial | concrete | `x*(exp(x) + 1)/sqrt(x + exp(x))` | $\frac{x \left(e^{x} + 1\right)}{\sqrt{x + e^{x}}}$ |
| partial | concrete | `x*exp(x)/sqrt(x + exp(x)) + x/sqrt(x + exp(x))` | $\frac{x e^{x}}{\sqrt{x + e^{x}}} + \frac{x}{\sqrt{x + e^{x}}}$ |
| partial | concrete | `x*exp(x)/sqrt(x + exp(x))` | $\frac{x e^{x}}{\sqrt{x + e^{x}}}$ |
| partial | concrete | `x**2*(3*x**2 + 5*exp(x))/(5*sqrt(x**3 + 5*exp(x))) + 4*x*sqrt(x**3 + 5*exp(x))/5` | $\frac{x^{2} \left(3 x^{2} + 5 e^{x}\right)}{5 \sqrt{x^{3} + 5 e^{x}}} + \frac{4 x \sqrt{x^{3} + 5 e^{x}}}{5}$ |
| partial | concrete | `x**2*exp(x)/sqrt(x**3 + 5*exp(x))` | $\frac{x^{2} e^{x}}{\sqrt{x^{3} + 5 e^{x}}}$ |
| SOLVED-both | concrete | `(-exp(x) - 1)/(x + exp(x))**(1/3)` | $\frac{- e^{x} - 1}{\sqrt[3]{x + e^{x}}}$ |
| partial | concrete | `x/(x + exp(x))**(1/3) - (x + exp(x))**(2/3) - 1/(x + exp(x))**(1/3)` | $\frac{x}{\sqrt[3]{x + e^{x}}} - \left(x + e^{x}\right)^{\frac{2}{3}} - \frac{1}{\sqrt[3]{x + e^{x}}}$ |
| partial | concrete | `x/(x + exp(x))**(1/3)` | $\frac{x}{\sqrt[3]{x + e^{x}}}$ |
| **SOLVED-NEW** | concrete | `(5*x + (2*x + 3)*exp(x))/(x + exp(x))**(1/3)` | $\frac{5 x + \left(2 x + 3\right) e^{x}}{\sqrt[3]{x + e^{x}}}$ |
| partial | concrete | `2*x*exp(x)/(x + exp(x))**(1/3) + 2*x/(x + exp(x))**(1/3) + 3*(x + exp(x))**(2/3)` | $\frac{2 x e^{x}}{\sqrt[3]{x + e^{x}}} + \frac{2 x}{\sqrt[3]{x + e^{x}}} + 3 \left(x + e^{x}\right)^{\frac{2}{3}}$ |
| partial | concrete | `x**2/sqrt(x + exp(x))` | $\frac{x^{2}}{\sqrt{x + e^{x}}}$ |
| partial | concrete | `(5*x**2 + 3*(x + exp(x))**(1/3) + (2*x**2 + 3*x)*exp(x))/(x*(x + exp(x))**(1/3))` | $\frac{5 x^{2} + 3 \sqrt[3]{x + e^{x}} + \left(2 x^{2} + 3 x\right) e^{x}}{x \sqrt[3]{x + e^{x}}}$ |
| partial | concrete | `x*sqrt(x**2 + 4)*log(x)` | $x \sqrt{x^{2} + 4} \log{\left(x \right)}$ |
| partial | concrete | `x*log(x)/sqrt(x**2 - 1)` | $\frac{x \log{\left(x \right)}}{\sqrt{x^{2} - 1}}$ |
| **SOLVED-NEW** | parametric | `(a + b*log(sqrt(-c*x + 1)/sqrt(c*x + 1)))**3/(-c**2*x**2 + 1)` | $\frac{\left(a + b \log{\left(\frac{\sqrt{- c x + 1}}{\sqrt{c x + 1}} \right)}\right)^{3}}{- c^{2} x^{2} + 1}$ |
| SOLVED-both | parametric | `(a + b*log(sqrt(-c*x + 1)/sqrt(c*x + 1)))**2/(-c**2*x**2 + 1)` | $\frac{\left(a + b \log{\left(\frac{\sqrt{- c x + 1}}{\sqrt{c x + 1}} \right)}\right)^{2}}{- c^{2} x^{2} + 1}$ |
| SOLVED-both | parametric | `(a + b*log(sqrt(-c*x + 1)/sqrt(c*x + 1)))/(-c**2*x**2 + 1)` | $\frac{a + b \log{\left(\frac{\sqrt{- c x + 1}}{\sqrt{c x + 1}} \right)}}{- c^{2} x^{2} + 1}$ |
| SOLVED-both | parametric | `1/((a + b*log(sqrt(-c*x + 1)/sqrt(c*x + 1)))*(-c**2*x**2 + 1))` | $\frac{1}{\left(a + b \log{\left(\frac{\sqrt{- c x + 1}}{\sqrt{c x + 1}} \right)}\right) \left(- c^{2} x^{2} + 1\right)}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*log(sqrt(-c*x + 1)/sqrt(c*x + 1)))**2*(-c**2*x**2 + 1))` | $\frac{1}{\left(a + b \log{\left(\frac{\sqrt{- c x + 1}}{\sqrt{c x + 1}} \right)}\right)^{2} \left(- c^{2} x^{2} + 1\right)}$ |
| **SOLVED-NEW** | parametric | `1/((a + b*log(sqrt(-c*x + 1)/sqrt(c*x + 1)))**3*(-c**2*x**2 + 1))` | $\frac{1}{\left(a + b \log{\left(\frac{\sqrt{- c x + 1}}{\sqrt{c x + 1}} \right)}\right)^{3} \left(- c^{2} x^{2} + 1\right)}$ |
| **SOLVED-NEW** | parametric | `log(sqrt(-a*x + 1)/sqrt(a*x + 1))/(-a**2*x**2 + 1)` | $\frac{\log{\left(\frac{\sqrt{- a x + 1}}{\sqrt{a x + 1}} \right)}}{- a^{2} x^{2} + 1}$ |
| NIE | parametric | `log(c*(d + e*x))**(5/2)` | $\log{\left(c \left(d + e x\right) \right)}^{\frac{5}{2}}$ |
| NIE | parametric | `log(c*(d + e*x))**(3/2)` | $\log{\left(c \left(d + e x\right) \right)}^{\frac{3}{2}}$ |
| NIE | parametric | `sqrt(log(c*(d + e*x)))` | $\sqrt{\log{\left(c \left(d + e x\right) \right)}}$ |
| NIE | parametric | `1/sqrt(log(c*(d + e*x)))` | $\frac{1}{\sqrt{\log{\left(c \left(d + e x\right) \right)}}}$ |
| NIE | parametric | `log(c*(d + e*x))**(-3/2)` | $\frac{1}{\log{\left(c \left(d + e x\right) \right)}^{\frac{3}{2}}}$ |
| NIE | parametric | `log(c*(d + e*x))**(-5/2)` | $\frac{1}{\log{\left(c \left(d + e x\right) \right)}^{\frac{5}{2}}}$ |
| NIE | parametric | `log(c*(d + e*x))**(-7/2)` | $\frac{1}{\log{\left(c \left(d + e x\right) \right)}^{\frac{7}{2}}}$ |
| partial | parametric | `(d + e*x)**(3/2)*log(a + b*x)/(a + b*x)` | $\frac{\left(d + e x\right)^{\frac{3}{2}} \log{\left(a + b x \right)}}{a + b x}$ |
| partial | parametric | `sqrt(d + e*x)*log(a + b*x)/(a + b*x)` | $\frac{\sqrt{d + e x} \log{\left(a + b x \right)}}{a + b x}$ |
| partial | parametric | `log(a + b*x)/((a + b*x)*sqrt(d + e*x))` | $\frac{\log{\left(a + b x \right)}}{\left(a + b x\right) \sqrt{d + e x}}$ |
| partial | parametric | `log(a + b*x)/((a + b*x)*(d + e*x)**(3/2))` | $\frac{\log{\left(a + b x \right)}}{\left(a + b x\right) \left(d + e x\right)^{\frac{3}{2}}}$ |
| partial | parametric | `log(a + b*x)/((a + b*x)*(d + e*x)**(5/2))` | $\frac{\log{\left(a + b x \right)}}{\left(a + b x\right) \left(d + e x\right)^{\frac{5}{2}}}$ |
| partial | parametric | `log(a + b*sqrt(x))/sqrt(x)` | $\frac{\log{\left(a + b \sqrt{x} \right)}}{\sqrt{x}}$ |
| partial | concrete | `x**3*log(4*x + 4*sqrt(x*(x - 1)) - 1)` | $x^{3} \log{\left(4 x + 4 \sqrt{x \left(x - 1\right)} - 1 \right)}$ |
| partial | concrete | `x**2*log(4*x + 4*sqrt(x*(x - 1)) - 1)` | $x^{2} \log{\left(4 x + 4 \sqrt{x \left(x - 1\right)} - 1 \right)}$ |
| partial | concrete | `x*log(4*x + 4*sqrt(x*(x - 1)) - 1)` | $x \log{\left(4 x + 4 \sqrt{x \left(x - 1\right)} - 1 \right)}$ |
| partial | concrete | `log(4*x + 4*sqrt(x*(x - 1)) - 1)` | $\log{\left(4 x + 4 \sqrt{x \left(x - 1\right)} - 1 \right)}$ |
| partial | concrete | `log(4*x + 4*sqrt(x*(x - 1)) - 1)/x` | $\frac{\log{\left(4 x + 4 \sqrt{x \left(x - 1\right)} - 1 \right)}}{x}$ |
| partial | concrete | `log(4*x + 4*sqrt(x*(x - 1)) - 1)/x**2` | $\frac{\log{\left(4 x + 4 \sqrt{x \left(x - 1\right)} - 1 \right)}}{x^{2}}$ |
| partial | concrete | `log(4*x + 4*sqrt(x*(x - 1)) - 1)/x**3` | $\frac{\log{\left(4 x + 4 \sqrt{x \left(x - 1\right)} - 1 \right)}}{x^{3}}$ |
| partial | concrete | `x**(3/2)*log(4*x + 4*sqrt(x*(x - 1)) - 1)` | $x^{\frac{3}{2}} \log{\left(4 x + 4 \sqrt{x \left(x - 1\right)} - 1 \right)}$ |
| partial | concrete | `sqrt(x)*log(4*x + 4*sqrt(x*(x - 1)) - 1)` | $\sqrt{x} \log{\left(4 x + 4 \sqrt{x \left(x - 1\right)} - 1 \right)}$ |
| partial | concrete | `log(4*x + 4*sqrt(x*(x - 1)) - 1)/sqrt(x)` | $\frac{\log{\left(4 x + 4 \sqrt{x \left(x - 1\right)} - 1 \right)}}{\sqrt{x}}$ |
| partial | concrete | `log(4*x + 4*sqrt(x*(x - 1)) - 1)/x**(3/2)` | $\frac{\log{\left(4 x + 4 \sqrt{x \left(x - 1\right)} - 1 \right)}}{x^{\frac{3}{2}}}$ |
| partial | concrete | `log(4*x + 4*sqrt(x*(x - 1)) - 1)/x**(5/2)` | $\frac{\log{\left(4 x + 4 \sqrt{x \left(x - 1\right)} - 1 \right)}}{x^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `sqrt(log(x) + 1)/x` | $\frac{\sqrt{\log{\left(x \right)} + 1}}{x}$ |
| SOLVED-both | concrete | `1/(x*sqrt(log(x)))` | $\frac{1}{x \sqrt{\log{\left(x \right)}}}$ |
| partial | concrete | `1/(x*sqrt(log(x)**2 - 3))` | $\frac{1}{x \sqrt{\log{\left(x \right)}^{2} - 3}}$ |
| partial | concrete | `1/(x*sqrt(4 - 9*log(x)**2))` | $\frac{1}{x \sqrt{4 - 9 \log{\left(x \right)}^{2}}}$ |
| partial | concrete | `1/(x*sqrt(log(x)**2 + 4))` | $\frac{1}{x \sqrt{\log{\left(x \right)}^{2} + 4}}$ |
| partial | concrete | `sqrt(log(x)**2 + 1)*log(x)**2/x` | $\frac{\sqrt{\log{\left(x \right)}^{2} + 1} \log{\left(x \right)}^{2}}{x}$ |
| SOLVED-both | concrete | `log(x)/(x*sqrt(log(x) + 1))` | $\frac{\log{\left(x \right)}}{x \sqrt{\log{\left(x \right)} + 1}}$ |
| SOLVED-both | concrete | `log(x)/(x*sqrt(4*log(x) - 1))` | $\frac{\log{\left(x \right)}}{x \sqrt{4 \log{\left(x \right)} - 1}}$ |
| partial | concrete | `sqrt(log(x) + 1)/(x*log(x))` | $\frac{\sqrt{\log{\left(x \right)} + 1}}{x \log{\left(x \right)}}$ |
| NIE | concrete | `log(sin(sqrt(x)))` | $\log{\left(\sin{\left(\sqrt{x} \right)} \right)}$ |
| SOLVED-both | concrete | `log(x)/sqrt(x)` | $\frac{\log{\left(x \right)}}{\sqrt{x}}$ |
| partial | concrete | `1/(x*sqrt(1 - log(x)**2))` | $\frac{1}{x \sqrt{1 - \log{\left(x \right)}^{2}}}$ |
| SOLVED-both | parametric | `log(sqrt(a + b*x))` | $\log{\left(\sqrt{a + b x} \right)}$ |
| SOLVED-both | concrete | `x*log(sqrt(x + 2))` | $x \log{\left(\sqrt{x + 2} \right)}$ |
| SOLVED-both | concrete | `x*log((3*x + 1)**(1/3))` | $x \log{\left(\sqrt[3]{3 x + 1} \right)}$ |
| partial | concrete | `log(x + sqrt(x**2 + 1))` | $\log{\left(x + \sqrt{x^{2} + 1} \right)}$ |
| partial | concrete | `log(x + sqrt(x**2 - 1))` | $\log{\left(x + \sqrt{x^{2} - 1} \right)}$ |
| partial | concrete | `log(x - sqrt(x**2 - 1))` | $\log{\left(x - \sqrt{x^{2} - 1} \right)}$ |
| timeout | concrete | `log(sqrt(x) + sqrt(x + 1))` | $\log{\left(\sqrt{x} + \sqrt{x + 1} \right)}$ |
| SOLVED-both | concrete | `x**(1/3)*log(x)` | $\sqrt[3]{x} \log{\left(x \right)}$ |
| partial | concrete | `log(x + sqrt(x + 1) + 1)` | $\log{\left(x + \sqrt{x + 1} + 1 \right)}$ |
| partial | parametric | `1/sqrt(-log(a*x**2))` | $\frac{1}{\sqrt{- \log{\left(a x^{2} \right)}}}$ |
| partial | parametric | `1/sqrt(-log(a/x**2))` | $\frac{1}{\sqrt{- \log{\left(\frac{a}{x^{2}} \right)}}}$ |
| partial | concrete | `log(sqrt(x) - x + 1)/x` | $\frac{\log{\left(\sqrt{x} - x + 1 \right)}}{x}$ |
| partial | concrete | `log(sqrt(x) + x)` | $\log{\left(\sqrt{x} + x \right)}$ |
| partial | parametric | `log(I*sqrt(-a*x + 1)/sqrt(a*x + 1) + 1)/(-a**2*x**2 + 1)` | $\frac{\log{\left(\frac{i \sqrt{- a x + 1}}{\sqrt{a x + 1}} + 1 \right)}}{- a^{2} x^{2} + 1}$ |
| partial | parametric | `log(-I*sqrt(-a*x + 1)/sqrt(a*x + 1) + 1)/(-a**2*x**2 + 1)` | $\frac{\log{\left(- \frac{i \sqrt{- a x + 1}}{\sqrt{a x + 1}} + 1 \right)}}{- a^{2} x^{2} + 1}$ |
| partial | concrete | `log(sqrt((x + 1)/x) + 2)` | $\log{\left(\sqrt{\frac{x + 1}{x}} + 2 \right)}$ |
| partial | concrete | `log(sqrt((x + 1)/x) + 1)` | $\log{\left(\sqrt{\frac{x + 1}{x}} + 1 \right)}$ |
| SOLVED-both | concrete | `log(sqrt((x + 1)/x))` | $\log{\left(\sqrt{\frac{x + 1}{x}} \right)}$ |
| partial | concrete | `log(sqrt((x + 1)/x) - 1)` | $\log{\left(\sqrt{\frac{x + 1}{x}} - 1 \right)}$ |
| partial | parametric | `log(x)/sqrt(a + b*log(x))` | $\frac{\log{\left(x \right)}}{\sqrt{a + b \log{\left(x \right)}}}$ |
| partial | parametric | `log(x)/sqrt(a - b*log(x))` | $\frac{\log{\left(x \right)}}{\sqrt{a - b \log{\left(x \right)}}}$ |
| partial | parametric | `(A + B*log(x))/sqrt(a + b*log(x))` | $\frac{A + B \log{\left(x \right)}}{\sqrt{a + b \log{\left(x \right)}}}$ |
| partial | parametric | `(A + B*log(x))/sqrt(a - b*log(x))` | $\frac{A + B \log{\left(x \right)}}{\sqrt{a - b \log{\left(x \right)}}}$ |
