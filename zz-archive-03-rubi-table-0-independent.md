# 0. Independent test suites

All attempted radical cases from this part of the Rubi corpus, run through `risch_integrate(f, x, algebraic=True)` (sympy branch `risch-algebraic`).  **SOLVED-NEW** means solved here but not by sympy's non-risch `integrate()`; SOLVED-both means both solve it.  632 cases: partial 345 (55%), NIE 165 (26%), SOLVED-both 110 (17%), SOLVED-NEW 9 (1%), timeout 3 (0%).

| Status | Kind | SymPy expression | Math |
|---|---|---|---|
| SOLVED-both | concrete | `sqrt(2*x + 1)` | $\sqrt{2 x + 1}$ |
| SOLVED-both | concrete | `x*sqrt(3*x + 1)` | $x \sqrt{3 x + 1}$ |
| SOLVED-both | concrete | `x**2*sqrt(x + 1)` | $x^{2} \sqrt{x + 1}$ |
| SOLVED-both | concrete | `x/sqrt(2 - 3*x)` | $\frac{x}{\sqrt{2 - 3 x}}$ |
| SOLVED-both | concrete | `z*(z - 1)**(1/3)` | $z \sqrt[3]{z - 1}$ |
| NIE | concrete | `sqrt(4 - sin(2*x))*cos(2*x)` | $\sqrt{4 - \sin{\left(2 x \right)}} \cos{\left(2 x \right)}$ |
| NIE | concrete | `sin(x)/sqrt(cos(x)**3)` | $\frac{\sin{\left(x \right)}}{\sqrt{\cos^{3}{\left(x \right)}}}$ |
| NIE | concrete | `sin(sqrt(x + 1))/sqrt(x + 1)` | $\frac{\sin{\left(\sqrt{x + 1} \right)}}{\sqrt{x + 1}}$ |
| SOLVED-both | concrete | `x**5/sqrt(1 - x**6)` | $\frac{x^{5}}{\sqrt{1 - x^{6}}}$ |
| SOLVED-both | concrete | `t*(t + 1)**(1/4)` | $t \sqrt[4]{t + 1}$ |
| SOLVED-both | concrete | `(x**2 + 1)**(-3/2)` | $\frac{1}{\left(x^{2} + 1\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x**2*(8*x**3 + 27)**(2/3)` | $x^{2} \left(8 x^{3} + 27\right)^{\frac{2}{3}}$ |
| NIE | concrete | `(sin(x) + cos(x))/(sin(x) - cos(x))**(1/3)` | $\frac{\sin{\left(x \right)} + \cos{\left(x \right)}}{\sqrt[3]{\sin{\left(x \right)} - \cos{\left(x \right)}}}$ |
| NIE | concrete | `x/sqrt(x**2 + (x**2 + 1)**(3/2) + 1)` | $\frac{x}{\sqrt{x^{2} + \left(x^{2} + 1\right)^{\frac{3}{2}} + 1}}$ |
| NIE | concrete | `x/(sqrt(x**2 + 1)*sqrt(sqrt(x**2 + 1) + 1))` | $\frac{x}{\sqrt{x^{2} + 1} \sqrt{\sqrt{x^{2} + 1} + 1}}$ |
| SOLVED-both | concrete | `(x**2 - 2*x + 1)**(1/5)/(1 - x)` | $\frac{\sqrt[5]{x^{2} - 2 x + 1}}{1 - x}$ |
| partial | parametric | `(a**2 - x**2)**(5/2)` | $\left(a^{2} - x^{2}\right)^{\frac{5}{2}}$ |
| SOLVED-both | concrete | `x**5/sqrt(x**2 + 5)` | $\frac{x^{5}}{\sqrt{x^{2} + 5}}$ |
| partial | concrete | `t**3/sqrt(t**3 + 4)` | $\frac{t^{3}}{\sqrt{t^{3} + 4}}$ |
| SOLVED-both | concrete | `x*sqrt(x**2 + 1)` | $x \sqrt{x^{2} + 1}$ |
| NIE | concrete | `sin((x - 1)**(1/4))` | $\sin{\left(\sqrt[4]{x - 1} \right)}$ |
| NIE | concrete | `sqrt(3*cos(x)**2 + 1)*sin(2*x)` | $\sqrt{3 \cos^{2}{\left(x \right)} + 1} \sin{\left(2 x \right)}$ |
| SOLVED-both | concrete | `log(x)/(x*sqrt(log(x) + 1))` | $\frac{\log{\left(x \right)}}{x \sqrt{\log{\left(x \right)} + 1}}$ |
| partial | concrete | `exp(sqrt(x))` | $e^{\sqrt{x}}$ |
| partial | parametric | `1/sqrt(a**2 - x**2)` | $\frac{1}{\sqrt{a^{2} - x^{2}}}$ |
| partial | concrete | `1/sqrt(-x**2 - 2*x + 1)` | $\frac{1}{\sqrt{- x^{2} - 2 x + 1}}$ |
| NIE | concrete | `atan(sqrt(x))` | $\mathrm{atan}{\left(\sqrt{x} \right)}$ |
| NIE | concrete | `atan(sqrt(x))/(sqrt(x)*(x + 1))` | $\frac{\mathrm{atan}{\left(\sqrt{x} \right)}}{\sqrt{x} \left(x + 1\right)}$ |
| partial | concrete | `sqrt(1 - x**2)` | $\sqrt{1 - x^{2}}$ |
| NIE | concrete | `x*exp(atan(x))/(x**2 + 1)**(3/2)` | $\frac{x e^{\mathrm{atan}{\left(x \right)}}}{\left(x^{2} + 1\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `exp(atan(x))/(x**2 + 1)**(3/2)` | $\frac{e^{\mathrm{atan}{\left(x \right)}}}{\left(x^{2} + 1\right)^{\frac{3}{2}}}$ |
| partial | parametric | `sqrt((a + x)/(a - x))` | $\sqrt{\frac{a + x}{a - x}}$ |
| partial | parametric | `sqrt((-a + x)*(b - x))` | $\sqrt{\left(- a + x\right) \left(b - x\right)}$ |
| partial | parametric | `1/sqrt((-a + x)*(b - x))` | $\frac{1}{\sqrt{\left(- a + x\right) \left(b - x\right)}}$ |
| SOLVED-both | concrete | `x/(-x**2 + sqrt(4 - x**2) + 4)` | $\frac{x}{- x^{2} + \sqrt{4 - x^{2}} + 4}$ |
| partial | concrete | `sqrt(3 - x**2)` | $\sqrt{3 - x^{2}}$ |
| SOLVED-both | concrete | `x/sqrt(3 - x**2)` | $\frac{x}{\sqrt{3 - x^{2}}}$ |
| partial | concrete | `sqrt(3 - x**2)/x` | $\frac{\sqrt{3 - x^{2}}}{x}$ |
| partial | concrete | `sqrt(x**2 + x)/x` | $\frac{\sqrt{x^{2} + x}}{x}$ |
| partial | concrete | `sqrt(x**2 + 5)` | $\sqrt{x^{2} + 5}$ |
| partial | concrete | `x/sqrt(x**2 + x + 1)` | $\frac{x}{\sqrt{x^{2} + x + 1}}$ |
| partial | concrete | `1/sqrt(x**2 + x)` | $\frac{1}{\sqrt{x^{2} + x}}$ |
| partial | concrete | `sqrt(-x**2 - x + 2)/x**2` | $\frac{\sqrt{- x^{2} - x + 2}}{x^{2}}$ |
| partial | concrete | `1/sqrt(t**3 + 1)` | $\frac{1}{\sqrt{t^{3} + 1}}$ |
| NIE | concrete | `1/(sin(z) + cos(z) + sqrt(2))` | $\frac{1}{\sin{\left(z \right)} + \cos{\left(z \right)} + \sqrt{2}}$ |
| partial | concrete | `(sqrt(1 - x) + sqrt(x + 1))**(-2)` | $\frac{1}{\left(\sqrt{1 - x} + \sqrt{x + 1}\right)^{2}}$ |
| NIE | concrete | `sin(x)/sqrt(x + 1)` | $\frac{\sin{\left(x \right)}}{\sqrt{x + 1}}$ |
| NIE | concrete | `log(x + 1)/(x*sqrt(sqrt(x + 1) + 1))` | $\frac{\log{\left(x + 1 \right)}}{x \sqrt{\sqrt{x + 1} + 1}}$ |
| NIE | concrete | `sqrt(sqrt(x + 1) + 1)*log(x + 1)/x` | $\frac{\sqrt{\sqrt{x + 1} + 1} \log{\left(x + 1 \right)}}{x}$ |
| partial | concrete | `1/(sqrt(x + sqrt(x**2 + 1)) + 1)` | $\frac{1}{\sqrt{x + \sqrt{x^{2} + 1}} + 1}$ |
| partial | concrete | `sqrt(x + 1)/(x + sqrt(sqrt(x + 1) + 1))` | $\frac{\sqrt{x + 1}}{x + \sqrt{\sqrt{x + 1} + 1}}$ |
| partial | concrete | `1/(x - sqrt(sqrt(x + 1) + 1))` | $\frac{1}{x - \sqrt{\sqrt{x + 1} + 1}}$ |
| partial | concrete | `x/(x + sqrt(1 - sqrt(x + 1)))` | $\frac{x}{x + \sqrt{1 - \sqrt{x + 1}}}$ |
| NIE | concrete | `sqrt(x + sqrt(x + 1))/(sqrt(x + 1)*(x**2 + 1))` | $\frac{\sqrt{x + \sqrt{x + 1}}}{\sqrt{x + 1} \left(x^{2} + 1\right)}$ |
| NIE | concrete | `sqrt(x + sqrt(x + 1))/(x**2 + 1)` | $\frac{\sqrt{x + \sqrt{x + 1}}}{x^{2} + 1}$ |
| timeout | concrete | `sqrt(sqrt(x) + sqrt(2*sqrt(x) + 2*x + 1) + 1)` | $\sqrt{\sqrt{x} + \sqrt{2 \sqrt{x} + 2 x + 1} + 1}$ |
| timeout | concrete | `sqrt(sqrt(x) + sqrt(2*sqrt(2)*sqrt(x) + 2*x + 2) + sqrt(2))` | $\sqrt{\sqrt{x} + \sqrt{2 \sqrt{2} \sqrt{x} + 2 x + 2} + \sqrt{2}}$ |
| NIE | concrete | `sqrt(x + sqrt(x + 1))/x**2` | $\frac{\sqrt{x + \sqrt{x + 1}}}{x^{2}}$ |
| NIE | concrete | `sqrt(sqrt(1 + 1/x) + 1/x)` | $\sqrt{\sqrt{1 + \frac{1}{x}} + \frac{1}{x}}$ |
| partial | concrete | `sqrt(1 + exp(-x))/(exp(x) - exp(-x))` | $\frac{\sqrt{1 + e^{- x}}}{e^{x} - e^{- x}}$ |
| NIE | concrete | `sqrt(1 + exp(-x))/sinh(x)` | $\frac{\sqrt{1 + e^{- x}}}{\sinh{\left(x \right)}}$ |
| NIE | concrete | `sqrt(tanh(4*x) + 1)` | $\sqrt{\tanh{\left(4 x \right)} + 1}$ |
| NIE | concrete | `tanh(x)/sqrt(exp(2*x) + exp(x))` | $\frac{\tanh{\left(x \right)}}{\sqrt{e^{2 x} + e^{x}}}$ |
| partial | concrete | `log(x**2 + sqrt(1 - x**2))` | $\log{\left(x^{2} + \sqrt{1 - x^{2}} \right)}$ |
| partial | concrete | `log(x + sqrt(x + 1))/(x**2 + 1)` | $\frac{\log{\left(x + \sqrt{x + 1} \right)}}{x^{2} + 1}$ |
| partial | concrete | `log(x + sqrt(x + 1))**2/(x + 1)**2` | $\frac{\log{\left(x + \sqrt{x + 1} \right)}^{2}}{\left(x + 1\right)^{2}}$ |
| partial | concrete | `log(x + sqrt(x + 1))/x` | $\frac{\log{\left(x + \sqrt{x + 1} \right)}}{x}$ |
| NIE | concrete | `sqrt(x**2 + 1)*atan(x)**2` | $\sqrt{x^{2} + 1} \mathrm{atan}^{2}{\left(x \right)}$ |
| partial | concrete | `sqrt(x**8 + 1)*(2*x**8 + 1)/(x**17 + 2*x**9 + x)` | $\frac{\sqrt{x^{8} + 1} \left(2 x^{8} + 1\right)}{x^{17} + 2 x^{9} + x}$ |
| partial | concrete | `1/(x*sqrt(x**8 + 1))` | $\frac{1}{x \sqrt{x^{8} + 1}}$ |
| partial | concrete | `x/sqrt(1 - x**3)` | $\frac{x}{\sqrt{1 - x^{3}}}$ |
| partial | concrete | `1/(x*sqrt(1 - x**3))` | $\frac{1}{x \sqrt{1 - x^{3}}}$ |
| partial | concrete | `x/sqrt(x**4 + 10*x**2 - 96*x - 71)` | $\frac{x}{\sqrt{x^{4} + 10 x^{2} - 96 x - 71}}$ |
| partial | concrete | `(5*x**2 + 3*(x + exp(x))**(1/3) + (2*x**2 + 3*x)*exp(x))/(x*(x + exp(x))**(1/3))` | $\frac{5 x^{2} + 3 \sqrt[3]{x + e^{x}} + \left(2 x^{2} + 3 x\right) e^{x}}{x \sqrt[3]{x + e^{x}}}$ |
| SOLVED-both | concrete | `(1 + 1/x)/(x + log(x))**(3/2) + 1/x` | $\frac{1 + \frac{1}{x}}{\left(x + \log{\left(x \right)}\right)^{\frac{3}{2}}} + \frac{1}{x}$ |
| **SOLVED-NEW** | concrete | `(x**2 + 2*x*log(x) + (x + 1)*sqrt(x + log(x)) + log(x)**2)/(x**3 + 2*x**2*log(x) + x*log(x)**2)` | $\frac{x^{2} + 2 x \log{\left(x \right)} + \left(x + 1\right) \sqrt{x + \log{\left(x \right)}} + \log{\left(x \right)}^{2}}{x^{3} + 2 x^{2} \log{\left(x \right)} + x \log{\left(x \right)}^{2}}$ |
| NIE | concrete | `x*asin(x)/sqrt(1 - x**2)` | $\frac{x \mathrm{asin}{\left(x \right)}}{\sqrt{1 - x^{2}}}$ |
| NIE | concrete | `-asin(sqrt(x) - sqrt(x + 1))` | $- \mathrm{asin}{\left(\sqrt{x} - \sqrt{x + 1} \right)}$ |
| partial | concrete | `log(x*sqrt(x**2 + 1) + 1)` | $\log{\left(x \sqrt{x^{2} + 1} + 1 \right)}$ |
| NIE | concrete | `cos(x)**2/sqrt(cos(x)**4 + cos(x)**2 + 1)` | $\frac{\cos^{2}{\left(x \right)}}{\sqrt{\cos^{4}{\left(x \right)} + \cos^{2}{\left(x \right)} + 1}}$ |
| NIE | concrete | `sqrt(tan(x)**4 + 1)*tan(x)` | $\sqrt{\tan^{4}{\left(x \right)} + 1} \tan{\left(x \right)}$ |
| NIE | concrete | `tan(x)/sqrt(sec(x)**3 + 1)` | $\frac{\tan{\left(x \right)}}{\sqrt{\sec^{3}{\left(x \right)} + 1}}$ |
| NIE | concrete | `sqrt(tan(x)**2 + 2*tan(x) + 2)` | $\sqrt{\tan^{2}{\left(x \right)} + 2 \tan{\left(x \right)} + 2}$ |
| NIE | concrete | `sin(x)*atan(sqrt(sec(x) - 1))` | $\sin{\left(x \right)} \mathrm{atan}{\left(\sqrt{\sec{\left(x \right)} - 1} \right)}$ |
| partial | concrete | `x*log(x + sqrt(x**2 + 1))*log(x**2 + 1)/sqrt(x**2 + 1)` | $\frac{x \log{\left(x + \sqrt{x^{2} + 1} \right)} \log{\left(x^{2} + 1 \right)}}{\sqrt{x^{2} + 1}}$ |
| NIE | concrete | `atan(x + sqrt(1 - x**2))` | $\mathrm{atan}{\left(x + \sqrt{1 - x^{2}} \right)}$ |
| NIE | concrete | `x*atan(x + sqrt(1 - x**2))/sqrt(1 - x**2)` | $\frac{x \mathrm{atan}{\left(x + \sqrt{1 - x^{2}} \right)}}{\sqrt{1 - x^{2}}}$ |
| NIE | concrete | `log(x + sqrt(x**2 + 1))/(1 - x**2)**(3/2)` | $\frac{\log{\left(x + \sqrt{x^{2} + 1} \right)}}{\left(1 - x^{2}\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `asin(x)/(x**2 + 1)**(3/2)` | $\frac{\mathrm{asin}{\left(x \right)}}{\left(x^{2} + 1\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `log(x + sqrt(x**2 - 1))/(x**2 + 1)**(3/2)` | $\frac{\log{\left(x + \sqrt{x^{2} - 1} \right)}}{\left(x^{2} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `log(x)/(x**2*sqrt(x**2 - 1))` | $\frac{\log{\left(x \right)}}{x^{2} \sqrt{x^{2} - 1}}$ |
| partial | concrete | `sqrt(x**3 + 1)/x` | $\frac{\sqrt{x^{3} + 1}}{x}$ |
| partial | concrete | `x*log(x + sqrt(x**2 - 1))/sqrt(x**2 - 1)` | $\frac{x \log{\left(x + \sqrt{x^{2} - 1} \right)}}{\sqrt{x^{2} - 1}}$ |
| NIE | concrete | `x**3*asin(x)/sqrt(1 - x**4)` | $\frac{x^{3} \mathrm{asin}{\left(x \right)}}{\sqrt{1 - x^{4}}}$ |
| NIE | concrete | `x*log(x + sqrt(x**2 + 1))*atan(x)/sqrt(x**2 + 1)` | $\frac{x \log{\left(x + \sqrt{x^{2} + 1} \right)} \mathrm{atan}{\left(x \right)}}{\sqrt{x^{2} + 1}}$ |
| partial | concrete | `x*log(sqrt(1 - x**2) + 1)/sqrt(1 - x**2)` | $\frac{x \log{\left(\sqrt{1 - x^{2}} + 1 \right)}}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `x*log(x + sqrt(x**2 + 1))/sqrt(x**2 + 1)` | $\frac{x \log{\left(x + \sqrt{x^{2} + 1} \right)}}{\sqrt{x^{2} + 1}}$ |
| partial | concrete | `x*log(x + sqrt(1 - x**2))/sqrt(1 - x**2)` | $\frac{x \log{\left(x + \sqrt{1 - x^{2}} \right)}}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `log(x)/(x**2*sqrt(1 - x**2))` | $\frac{\log{\left(x \right)}}{x^{2} \sqrt{1 - x^{2}}}$ |
| NIE | concrete | `x*atan(x)/sqrt(x**2 + 1)` | $\frac{x \mathrm{atan}{\left(x \right)}}{\sqrt{x^{2} + 1}}$ |
| NIE | concrete | `atan(x)/(x**2*sqrt(1 - x**2))` | $\frac{\mathrm{atan}{\left(x \right)}}{x^{2} \sqrt{1 - x^{2}}}$ |
| NIE | concrete | `x*atan(x)/sqrt(1 - x**2)` | $\frac{x \mathrm{atan}{\left(x \right)}}{\sqrt{1 - x^{2}}}$ |
| NIE | concrete | `atan(x)/(x**2*sqrt(x**2 + 1))` | $\frac{\mathrm{atan}{\left(x \right)}}{x^{2} \sqrt{x^{2} + 1}}$ |
| NIE | concrete | `asin(x)/(x**2*sqrt(1 - x**2))` | $\frac{\mathrm{asin}{\left(x \right)}}{x^{2} \sqrt{1 - x^{2}}}$ |
| partial | concrete | `x*log(x)/sqrt(x**2 - 1)` | $\frac{x \log{\left(x \right)}}{\sqrt{x^{2} - 1}}$ |
| partial | concrete | `log(x)/(x**2*sqrt(x**2 + 1))` | $\frac{\log{\left(x \right)}}{x^{2} \sqrt{x^{2} + 1}}$ |
| NIE | concrete | `x*asec(x)/sqrt(x**2 - 1)` | $\frac{x \mathrm{asec}{\left(x \right)}}{\sqrt{x^{2} - 1}}$ |
| partial | concrete | `x*log(x)/sqrt(x**2 + 1)` | $\frac{x \log{\left(x \right)}}{\sqrt{x^{2} + 1}}$ |
| partial | concrete | `(x**2 + 1)/((1 - x**2)*sqrt(x**4 + 1))` | $\frac{x^{2} + 1}{\left(1 - x^{2}\right) \sqrt{x^{4} + 1}}$ |
| partial | concrete | `(1 - x**2)/((x**2 + 1)*sqrt(x**4 + 1))` | $\frac{1 - x^{2}}{\left(x^{2} + 1\right) \sqrt{x^{4} + 1}}$ |
| NIE | concrete | `sqrt(sin(x) + 1)*log(sin(x))` | $\sqrt{\sin{\left(x \right)} + 1} \log{\left(\sin{\left(x \right)} \right)}$ |
| NIE | concrete | `sec(x)/sqrt(sec(x)**4 - 1)` | $\frac{\sec{\left(x \right)}}{\sqrt{\sec^{4}{\left(x \right)} - 1}}$ |
| NIE | concrete | `tan(x)/sqrt(tan(x)**4 + 1)` | $\frac{\tan{\left(x \right)}}{\sqrt{\tan^{4}{\left(x \right)} + 1}}$ |
| NIE | concrete | `sqrt(-sqrt(sec(x) - 1) + sqrt(sec(x) + 1))` | $\sqrt{- \sqrt{\sec{\left(x \right)} - 1} + \sqrt{\sec{\left(x \right)} + 1}}$ |
| NIE | concrete | `atan(x*sqrt(x**2 + 1))` | $\mathrm{atan}{\left(x \sqrt{x^{2} + 1} \right)}$ |
| NIE | concrete | `asin(x/sqrt(1 - x**2))` | $\mathrm{asin}{\left(\frac{x}{\sqrt{1 - x^{2}}} \right)}$ |
| SOLVED-both | concrete | `sqrt(2)*x**2 + 2*x` | $\sqrt{2} x^{2} + 2 x$ |
| partial | parametric | `log(x)/sqrt(a*x + b)` | $\frac{\log{\left(x \right)}}{\sqrt{a x + b}}$ |
| partial | parametric | `sqrt(a + b*x)*sqrt(c + d*x)` | $\sqrt{a + b x} \sqrt{c + d x}$ |
| SOLVED-both | parametric | `sqrt(a + b*x)` | $\sqrt{a + b x}$ |
| SOLVED-both | parametric | `x*sqrt(a + b*x)` | $x \sqrt{a + b x}$ |
| SOLVED-both | parametric | `x**2*sqrt(a + b*x)` | $x^{2} \sqrt{a + b x}$ |
| partial | parametric | `sqrt(a + b*x)/x` | $\frac{\sqrt{a + b x}}{x}$ |
| partial | parametric | `sqrt(a + b*x)/x**2` | $\frac{\sqrt{a + b x}}{x^{2}}$ |
| SOLVED-both | parametric | `1/sqrt(a + b*x)` | $\frac{1}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `x/sqrt(a + b*x)` | $\frac{x}{\sqrt{a + b x}}$ |
| SOLVED-both | parametric | `x**2/sqrt(a + b*x)` | $\frac{x^{2}}{\sqrt{a + b x}}$ |
| partial | parametric | `1/(x*sqrt(a + b*x))` | $\frac{1}{x \sqrt{a + b x}}$ |
| partial | parametric | `1/(x**2*sqrt(a + b*x))` | $\frac{1}{x^{2} \sqrt{a + b x}}$ |
| NIE | concrete | `atan(sqrt(2)*(2*x - sqrt(2))/2)` | $\mathrm{atan}{\left(\frac{\sqrt{2} \left(2 x - \sqrt{2}\right)}{2} \right)}$ |
| partial | concrete | `1/sqrt(x**2 - 1)` | $\frac{1}{\sqrt{x^{2} - 1}}$ |
| partial | concrete | `sqrt(x)*sqrt(x + 1)` | $\sqrt{x} \sqrt{x + 1}$ |
| NIE | concrete | `sin(sqrt(x))` | $\sin{\left(\sqrt{x} \right)}$ |
| SOLVED-both | concrete | `x/(1 - x**2)**(9/8)` | $\frac{x}{\left(1 - x^{2}\right)^{\frac{9}{8}}}$ |
| partial | concrete | `x/sqrt(1 - x**4)` | $\frac{x}{\sqrt{1 - x^{4}}}$ |
| partial | concrete | `1/(x*sqrt(x**4 + 1))` | $\frac{1}{x \sqrt{x^{4} + 1}}$ |
| partial | concrete | `x/sqrt(x**4 + x**2 + 1)` | $\frac{x}{\sqrt{x^{4} + x^{2} + 1}}$ |
| partial | concrete | `1/(x*sqrt(-x**4 + x**2 - 1))` | $\frac{1}{x \sqrt{- x^{4} + x^{2} - 1}}$ |
| **SOLVED-NEW** | concrete | `(x + 1)/((1 - x)**2*sqrt(x**2 + 1))` | $\frac{x + 1}{\left(1 - x\right)^{2} \sqrt{x^{2} + 1}}$ |
| partial | concrete | `1/sqrt(x**2 + 1)` | $\frac{1}{\sqrt{x^{2} + 1}}$ |
| partial | concrete | `(sqrt(x)*sqrt(x + 1) + sqrt(x)*sqrt(x + 2) + sqrt(x + 1)*sqrt(x + 2))/(2*sqrt(x)*sqrt(x + 1)*sqrt(x + 2))` | $\frac{\sqrt{x} \sqrt{x + 1} + \sqrt{x} \sqrt{x + 2} + \sqrt{x + 1} \sqrt{x + 2}}{2 \sqrt{x} \sqrt{x + 1} \sqrt{x + 2}}$ |
| partial | concrete | `(5*x**4*sqrt(x**3 + 1) - 3*x**2*sqrt(x**5 - 2*x + 1) - 2*sqrt(x**3 + 1))/(2*sqrt(x**3 + 1)*sqrt(x**5 - 2*x + 1))` | $\frac{5 x^{4} \sqrt{x^{3} + 1} - 3 x^{2} \sqrt{x^{5} - 2 x + 1} - 2 \sqrt{x^{3} + 1}}{2 \sqrt{x^{3} + 1} \sqrt{x^{5} - 2 x + 1}}$ |
| partial | concrete | `1/sqrt(x**2 - 1) + 10/sqrt(x**2 - 4)` | $\frac{1}{\sqrt{x^{2} - 1}} + \frac{10}{\sqrt{x^{2} - 4}}$ |
| NIE | parametric | `sqrt(x + sqrt(a**2 + x**2))/x` | $\frac{\sqrt{x + \sqrt{a^{2} + x^{2}}}}{x}$ |
| SOLVED-both | concrete | `3*x**2/(2*x**3 + 2*sqrt(x**3 + 1) + 2)` | $\frac{3 x^{2}}{2 x^{3} + 2 \sqrt{x^{3} + 1} + 2}$ |
| partial | parametric | `1/sqrt(-alpha**2 + 2*h*r**2)` | $\frac{1}{\sqrt{- \alpha^{2} + 2 h r^{2}}}$ |
| partial | parametric | `1/(r*sqrt(-alpha**2 - epsilon**2 + 2*h*r**2))` | $\frac{1}{r \sqrt{- \alpha^{2} - \epsilon^{2} + 2 h r^{2}}}$ |
| partial | parametric | `1/(r*sqrt(-alpha**2 + 2*h*r**2 - 2*k*r))` | $\frac{1}{r \sqrt{- \alpha^{2} + 2 h r^{2} - 2 k r}}$ |
| partial | parametric | `1/(r*sqrt(-alpha**2 - epsilon**2 + 2*h*r**2 - 2*k*r))` | $\frac{1}{r \sqrt{- \alpha^{2} - \epsilon^{2} + 2 h r^{2} - 2 k r}}$ |
| SOLVED-both | parametric | `r/sqrt(-alpha**2 + 2*e*r**2)` | $\frac{r}{\sqrt{- \alpha^{2} + 2 e r^{2}}}$ |
| SOLVED-both | parametric | `r/sqrt(-alpha**2 + 2*e*r**2 - epsilon**2)` | $\frac{r}{\sqrt{- \alpha^{2} + 2 e r^{2} - \epsilon^{2}}}$ |
| partial | parametric | `r/sqrt(-alpha**2 + 2*e*r**2 - 2*k*r**4)` | $\frac{r}{\sqrt{- \alpha^{2} + 2 e r^{2} - 2 k r^{4}}}$ |
| partial | parametric | `r/sqrt(-alpha**2 + 2*e*r**2 - 2*k*r)` | $\frac{r}{\sqrt{- \alpha^{2} + 2 e r^{2} - 2 k r}}$ |
| partial | parametric | `1/(r*sqrt(-alpha**2 + 2*h*r**2 - 2*k*r**4))` | $\frac{1}{r \sqrt{- \alpha^{2} + 2 h r^{2} - 2 k r^{4}}}$ |
| partial | parametric | `1/(r*sqrt(-alpha**2 - epsilon**2 + 2*h*r**2 - 2*k*r**4))` | $\frac{1}{r \sqrt{- \alpha^{2} - \epsilon^{2} + 2 h r^{2} - 2 k r^{4}}}$ |
| SOLVED-both | concrete | `sqrt(x)/(x + 1)**(7/2)` | $\frac{\sqrt{x}}{\left(x + 1\right)^{\frac{7}{2}}}$ |
| partial | concrete | `1/(sqrt(x)*(2*x - 1))` | $\frac{1}{\sqrt{x} \left(2 x - 1\right)}$ |
| SOLVED-both | concrete | `sqrt(x)*(x**2 + 1)` | $\sqrt{x} \left(x^{2} + 1\right)$ |
| partial | parametric | `(-a + x)**(1/3)/x` | $\frac{\sqrt[3]{- a + x}}{x}$ |
| NIE | concrete | `sqrt(sin(x) + 1)` | $\sqrt{\sin{\left(x \right)} + 1}$ |
| NIE | concrete | `sqrt(1 - sin(x))` | $\sqrt{1 - \sin{\left(x \right)}}$ |
| NIE | concrete | `sqrt(cos(x) + 1)` | $\sqrt{\cos{\left(x \right)} + 1}$ |
| NIE | concrete | `sqrt(1 - cos(x))` | $\sqrt{1 - \cos{\left(x \right)}}$ |
| partial | concrete | `1/(sqrt(x) - sqrt(x - 1))` | $\frac{1}{\sqrt{x} - \sqrt{x - 1}}$ |
| partial | concrete | `1/(1 - sqrt(x + 1))` | $\frac{1}{1 - \sqrt{x + 1}}$ |
| partial | concrete | `x/sqrt(x**4 + 36)` | $\frac{x}{\sqrt{x^{4} + 36}}$ |
| partial | concrete | `1/(x**(1/3) + sqrt(x))` | $\frac{1}{\sqrt[3]{x} + \sqrt{x}}$ |
| **SOLVED-NEW** | concrete | `sqrt(x**4 + 2 + x**(-4))` | $\sqrt{x^{4} + 2 + \frac{1}{x^{4}}}$ |
| partial | concrete | `x*log(x + sqrt(x**2 + 1))` | $x \log{\left(x + \sqrt{x^{2} + 1} \right)}$ |
| partial | concrete | `1/sqrt(x**2 + 1)` | $\frac{1}{\sqrt{x^{2} + 1}}$ |
| partial | concrete | `sqrt(x**2 + 3)` | $\sqrt{x^{2} + 3}$ |
| partial | concrete | `1/sqrt(4*x**2 + 9)` | $\frac{1}{\sqrt{4 x^{2} + 9}}$ |
| partial | concrete | `1/sqrt(x**2 + 4)` | $\frac{1}{\sqrt{x^{2} + 4}}$ |
| partial | concrete | `(2*x**6 + 4*x**5 + 7*x**4 - 3*x**3 - x**2 - 8*x - 8)/((2*x**2 - 1)**2*sqrt(x**4 + 4*x**3 + 2*x**2 + 1))` | $\frac{2 x^{6} + 4 x^{5} + 7 x^{4} - 3 x^{3} - x^{2} - 8 x - 8}{\left(2 x^{2} - 1\right)^{2} \sqrt{x^{4} + 4 x^{3} + 2 x^{2} + 1}}$ |
| partial | concrete | `(2*y + 1)*sqrt(-5*y**2 - 5*y + 1)/(y*(y + 1)*(y + 2)*sqrt(-y**2 - y + 1))` | $\frac{\left(2 y + 1\right) \sqrt{- 5 y^{2} - 5 y + 1}}{y \left(y + 1\right) \left(y + 2\right) \sqrt{- y^{2} - y + 1}}$ |
| **SOLVED-NEW** | concrete | `x*(x**2*sqrt(x**2 - 4) + x**2*sqrt(x**2 - 1) - sqrt(x**2 - 4) - 4*sqrt(x**2 - 1))/((x**4 - 5*x**2 + 4)*(sqrt(x**2 - 4) + sqrt(x**2 - 1) + 1))` | $\frac{x \left(x^{2} \sqrt{x^{2} - 4} + x^{2} \sqrt{x^{2} - 1} - \sqrt{x^{2} - 4} - 4 \sqrt{x^{2} - 1}\right)}{\left(x^{4} - 5 x^{2} + 4\right) \left(\sqrt{x^{2} - 4} + \sqrt{x^{2} - 1} + 1\right)}$ |
| partial | concrete | `x*sqrt(9 - 4*sqrt(2)) - sqrt(2)*sqrt(x**4 + 2*x**2 + 4*x + 1)` | $x \sqrt{9 - 4 \sqrt{2}} - \sqrt{2} \sqrt{x^{4} + 2 x^{2} + 4 x + 1}$ |
| SOLVED-both | concrete | `(x**2 + x)/sqrt(x)` | $\frac{x^{2} + x}{\sqrt{x}}$ |
| SOLVED-both | concrete | `x*sqrt(x**2 + 1)` | $x \sqrt{x^{2} + 1}$ |
| SOLVED-both | concrete | `x*sqrt(x**2 + 1)` | $x \sqrt{x^{2} + 1}$ |
| SOLVED-both | concrete | `x**(3/2)` | $x^{\frac{3}{2}}$ |
| SOLVED-both | concrete | `x*sqrt(x + 1)` | $x \sqrt{x + 1}$ |
| NIE | concrete | `cos(sqrt(x))` | $\cos{\left(\sqrt{x} \right)}$ |
| SOLVED-both | concrete | `x*sqrt(x + 1)` | $x \sqrt{x + 1}$ |
| partial | concrete | `1/(x**(1/3) + sqrt(x))` | $\frac{1}{\sqrt[3]{x} + \sqrt{x}}$ |
| partial | concrete | `sqrt((x + 1)/(2*x + 3))` | $\sqrt{\frac{x + 1}{2 x + 3}}$ |
| partial | concrete | `x**4/(1 - x**2)**(5/2)` | $\frac{x^{4}}{\left(1 - x^{2}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(x)*(x + 1)**(5/2)` | $\sqrt{x} \left(x + 1\right)^{\frac{5}{2}}$ |
| partial | concrete | `x**4/(1 - x**2)**(5/2)` | $\frac{x^{4}}{\left(1 - x^{2}\right)^{\frac{5}{2}}}$ |
| partial | parametric | `sqrt(A**2 - B**2*y**2 + B**2)/(1 - y**2)` | $\frac{\sqrt{A^{2} - B^{2} y^{2} + B^{2}}}{1 - y^{2}}$ |
| NIE | concrete | `cos(sqrt(x))` | $\cos{\left(\sqrt{x} \right)}$ |
| NIE | concrete | `1/(sqrt(1 - x**2)*(asin(x)**2 + 1))` | $\frac{1}{\sqrt{1 - x^{2}} \left(\mathrm{asin}^{2}{\left(x \right)} + 1\right)}$ |
| partial | parametric | `-sqrt(A**2 + B**2*(1 - y**2))/(1 - y**2)` | $- \frac{\sqrt{A^{2} + B^{2} \left(1 - y^{2}\right)}}{1 - y^{2}}$ |
| partial | concrete | `x**4/(1 - x**2)**(5/2)` | $\frac{x^{4}}{\left(1 - x^{2}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `x**4/(1 - x**2)**(5/2)` | $\frac{x^{4}}{\left(1 - x^{2}\right)^{\frac{5}{2}}}$ |
| partial | concrete | `-x**2/(1 - x**2)**(3/2)` | $- \frac{x^{2}}{\left(1 - x^{2}\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(x**2 + 1)/sqrt(x)` | $\frac{x^{2} + 1}{\sqrt{x}}$ |
| partial | concrete | `x/sqrt(x**2 + 2*x + 5)` | $\frac{x}{\sqrt{x^{2} + 2 x + 5}}$ |
| partial | concrete | `(x + 1)/sqrt(-x**2 + 2*x)` | $\frac{x + 1}{\sqrt{- x^{2} + 2 x}}$ |
| partial | concrete | `x**4/(1 - x**2)**(5/2)` | $\frac{x^{4}}{\left(1 - x^{2}\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/(r*sqrt(2*H*r**2 - a**2))` | $\frac{1}{r \sqrt{2 H r^{2} - a^{2}}}$ |
| SOLVED-both | parametric | `1/(r*sqrt(2*H*r**2 - a**2 - e**2))` | $\frac{1}{r \sqrt{2 H r^{2} - a^{2} - e^{2}}}$ |
| SOLVED-both | parametric | `1/(r*sqrt(2*H*r**2 - 2*K*r**4 - a**2))` | $\frac{1}{r \sqrt{2 H r^{2} - 2 K r^{4} - a^{2}}}$ |
| SOLVED-both | parametric | `1/(r*sqrt(2*H*r**2 - 2*K*r**4 - a**2 - e**2))` | $\frac{1}{r \sqrt{2 H r^{2} - 2 K r^{4} - a^{2} - e^{2}}}$ |
| SOLVED-both | parametric | `1/(r*sqrt(2*H*r**2 - 2*K*r - a**2))` | $\frac{1}{r \sqrt{2 H r^{2} - 2 K r - a^{2}}}$ |
| SOLVED-both | parametric | `1/(r*sqrt(2*H*r**2 - 2*K*r - a**2 - e**2))` | $\frac{1}{r \sqrt{2 H r^{2} - 2 K r - a^{2} - e^{2}}}$ |
| SOLVED-both | parametric | `r/sqrt(-a**2 + 2*E*r**2)` | $\frac{r}{\sqrt{- a^{2} + 2 e r^{2}}}$ |
| SOLVED-both | parametric | `r/sqrt(-a**2 - e**2 + 2*E*r**2)` | $\frac{r}{\sqrt{- a^{2} - e^{2} + 2 e r^{2}}}$ |
| SOLVED-both | parametric | `r/sqrt(-2*K*r**4 - a**2 + 2*E*r**2)` | $\frac{r}{\sqrt{- 2 K r^{4} - a^{2} + 2 e r^{2}}}$ |
| SOLVED-both | parametric | `r/sqrt(-2*K*r**4 - a**2 - e**2 + 2*E*r**2)` | $\frac{r}{\sqrt{- 2 K r^{4} - a^{2} - e^{2} + 2 e r^{2}}}$ |
| SOLVED-both | parametric | `r/sqrt(2*H*r**2 - 2*K*r - a**2 - e**2)` | $\frac{r}{\sqrt{2 H r^{2} - 2 K r - a^{2} - e^{2}}}$ |
| SOLVED-both | concrete | `sqrt(t)*log(t)` | $\sqrt{t} \log{\left(t \right)}$ |
| partial | concrete | `exp(sqrt(x))` | $e^{\sqrt{x}}$ |
| SOLVED-both | concrete | `log(sqrt(x))` | $\log{\left(\sqrt{x} \right)}$ |
| NIE | concrete | `sin(sqrt(x))` | $\sin{\left(\sqrt{x} \right)}$ |
| SOLVED-both | concrete | `sqrt(x)*log(x)` | $\sqrt{x} \log{\left(x \right)}$ |
| NIE | concrete | `sin(x)**3*sqrt(cos(x))` | $\sin^{3}{\left(x \right)} \sqrt{\cos{\left(x \right)}}$ |
| NIE | concrete | `sqrt(sin(x))*cos(x)**3` | $\sqrt{\sin{\left(x \right)}} \cos^{3}{\left(x \right)}$ |
| NIE | concrete | `cos(sqrt(x))**2/sqrt(x)` | $\frac{\cos^{2}{\left(\sqrt{x} \right)}}{\sqrt{x}}$ |
| partial | concrete | `sqrt(9 - x**2)/x**2` | $\frac{\sqrt{9 - x^{2}}}{x^{2}}$ |
| SOLVED-both | concrete | `1/(x**2*sqrt(x**2 + 4))` | $\frac{1}{x^{2} \sqrt{x^{2} + 4}}$ |
| SOLVED-both | concrete | `x/sqrt(x**2 + 4)` | $\frac{x}{\sqrt{x^{2} + 4}}$ |
| partial | parametric | `1/sqrt(-a**2 + x**2)` | $\frac{1}{\sqrt{- a^{2} + x^{2}}}$ |
| SOLVED-both | concrete | `x**3/(4*x**2 + 9)**(3/2)` | $\frac{x^{3}}{\left(4 x^{2} + 9\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x/sqrt(-x**2 - 2*x + 3)` | $\frac{x}{\sqrt{- x^{2} - 2 x + 3}}$ |
| SOLVED-both | concrete | `1/(x**2*sqrt(1 - x**2))` | $\frac{1}{x^{2} \sqrt{1 - x^{2}}}$ |
| SOLVED-both | concrete | `x**3*sqrt(4 - x**2)` | $x^{3} \sqrt{4 - x^{2}}$ |
| SOLVED-both | concrete | `x/sqrt(1 - x**2)` | $\frac{x}{\sqrt{1 - x^{2}}}$ |
| SOLVED-both | concrete | `x*sqrt(4 - x**2)` | $x \sqrt{4 - x^{2}}$ |
| partial | concrete | `sqrt(1 - 4*x**2)` | $\sqrt{1 - 4 x^{2}}$ |
| SOLVED-both | concrete | `x**3/sqrt(x**2 + 4)` | $\frac{x^{3}}{\sqrt{x^{2} + 4}}$ |
| partial | concrete | `1/sqrt(x**2 + 9)` | $\frac{1}{\sqrt{x^{2} + 9}}$ |
| partial | concrete | `sqrt(x**2 + 1)` | $\sqrt{x^{2} + 1}$ |
| partial | concrete | `1/(x**3*sqrt(x**2 - 16))` | $\frac{1}{x^{3} \sqrt{x^{2} - 16}}$ |
| SOLVED-both | parametric | `sqrt(-a**2 + x**2)/x**4` | $\frac{\sqrt{- a^{2} + x^{2}}}{x^{4}}$ |
| partial | concrete | `sqrt(9*x**2 - 4)/x` | $\frac{\sqrt{9 x^{2} - 4}}{x}$ |
| SOLVED-both | concrete | `1/(x**2*sqrt(16*x**2 - 9))` | $\frac{1}{x^{2} \sqrt{16 x^{2} - 9}}$ |
| partial | parametric | `x**2/(a**2 - x**2)**(3/2)` | $\frac{x^{2}}{\left(a^{2} - x^{2}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**2/sqrt(5 - x**2)` | $\frac{x^{2}}{\sqrt{5 - x^{2}}}$ |
| partial | concrete | `1/(x*sqrt(x**2 + 3))` | $\frac{1}{x \sqrt{x^{2} + 3}}$ |
| SOLVED-both | concrete | `x/(x**2 + 4)**(5/2)` | $\frac{x}{\left(x^{2} + 4\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `x**3*sqrt(4 - 9*x**2)` | $x^{3} \sqrt{4 - 9 x^{2}}$ |
| partial | concrete | `x**2*sqrt(9 - x**2)` | $x^{2} \sqrt{9 - x^{2}}$ |
| SOLVED-both | concrete | `5*x*sqrt(x**2 + 1)` | $5 x \sqrt{x^{2} + 1}$ |
| SOLVED-both | concrete | `(4*x**2 - 25)**(-3/2)` | $\frac{1}{\left(4 x^{2} - 25\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(-x**2 + 2*x)` | $\sqrt{- x^{2} + 2 x}$ |
| partial | concrete | `1/sqrt(x**2 + 4*x + 8)` | $\frac{1}{\sqrt{x^{2} + 4 x + 8}}$ |
| partial | concrete | `1/sqrt(9*x**2 + 6*x - 8)` | $\frac{1}{\sqrt{9 x^{2} + 6 x - 8}}$ |
| partial | concrete | `x**2/sqrt(-x**2 + 4*x)` | $\frac{x^{2}}{\sqrt{- x^{2} + 4 x}}$ |
| SOLVED-both | concrete | `(-x**2 - 4*x + 5)**(-5/2)` | $\frac{1}{\left(- x^{2} - 4 x + 5\right)^{\frac{5}{2}}}$ |
| partial | concrete | `sqrt(9 - exp(2*t))*exp(t)` | $\sqrt{9 - e^{2 t}} e^{t}$ |
| partial | concrete | `sqrt(exp(2*t) - 9)` | $\sqrt{e^{2 t} - 9}$ |
| partial | parametric | `1/sqrt(a**2 + x**2)` | $\frac{1}{\sqrt{a^{2} + x^{2}}}$ |
| partial | concrete | `sqrt(x + 4)/x` | $\frac{\sqrt{x + 4}}{x}$ |
| partial | concrete | `1/(sqrt(x) - 1/x**(1/3))` | $\frac{1}{\sqrt{x} - \frac{1}{\sqrt[3]{x}}}$ |
| partial | concrete | `1/(sqrt(x) + 1)` | $\frac{1}{\sqrt{x} + 1}$ |
| partial | concrete | `1/(1 + x**(-1/3))` | $\frac{1}{1 + \frac{1}{\sqrt[3]{x}}}$ |
| partial | concrete | `sqrt(x)/(x + 1)` | $\frac{\sqrt{x}}{x + 1}$ |
| partial | concrete | `1/(x*sqrt(x + 1))` | $\frac{1}{x \sqrt{x + 1}}$ |
| SOLVED-both | concrete | `1/(-x**(1/3) + x)` | $\frac{1}{- \sqrt[3]{x} + x}$ |
| partial | concrete | `1/(x - sqrt(x + 2))` | $\frac{1}{x - \sqrt{x + 2}}$ |
| SOLVED-both | concrete | `x**2/sqrt(x - 1)` | $\frac{x^{2}}{\sqrt{x - 1}}$ |
| partial | concrete | `sqrt(x - 1)/(x + 1)` | $\frac{\sqrt{x - 1}}{x + 1}$ |
| partial | concrete | `1/sqrt(sqrt(x) + 1)` | $\frac{1}{\sqrt{\sqrt{x} + 1}}$ |
| partial | concrete | `sqrt(x)/(x**2 + x)` | $\frac{\sqrt{x}}{x^{2} + x}$ |
| partial | concrete | `(sqrt(x) + 1)/(sqrt(x) - 1)` | $\frac{\sqrt{x} + 1}{\sqrt{x} - 1}$ |
| partial | concrete | `(1 + x**(-1/3))/(-1 + x**(-1/3))` | $\frac{1 + \frac{1}{\sqrt[3]{x}}}{-1 + \frac{1}{\sqrt[3]{x}}}$ |
| SOLVED-both | concrete | `x**3/(x**2 + 1)**(1/3)` | $\frac{x^{3}}{\sqrt[3]{x^{2} + 1}}$ |
| partial | concrete | `sqrt(x)/(sqrt(x) - 1/x**(1/3))` | $\frac{\sqrt{x}}{\sqrt{x} - \frac{1}{\sqrt[3]{x}}}$ |
| partial | concrete | `1/(sqrt(x) + x**(-1/4))` | $\frac{1}{\sqrt{x} + \frac{1}{\sqrt[4]{x}}}$ |
| partial | concrete | `1/(x**(-1/3) + x**(-1/4))` | $\frac{1}{\frac{1}{\sqrt[3]{x}} + \frac{1}{\sqrt[4]{x}}}$ |
| partial | concrete | `sqrt((1 - x)/x)` | $\sqrt{\frac{1 - x}{x}}$ |
| partial | concrete | `1/sqrt(exp(x) + 1)` | $\frac{1}{\sqrt{e^{x} + 1}}$ |
| partial | concrete | `sqrt(1 - exp(x))` | $\sqrt{1 - e^{x}}$ |
| SOLVED-both | concrete | `sqrt(x)*(sqrt(x) + 1)` | $\sqrt{x} \left(\sqrt{x} + 1\right)$ |
| partial | concrete | `exp(sqrt(x))` | $e^{\sqrt{x}}$ |
| SOLVED-both | concrete | `1/(x*sqrt(log(x)))` | $\frac{1}{x \sqrt{\log{\left(x \right)}}}$ |
| SOLVED-both | concrete | `x/sqrt(1 - x**2)` | $\frac{x}{\sqrt{1 - x^{2}}}$ |
| partial | concrete | `sqrt(x - 2)/(x + 2)` | $\frac{\sqrt{x - 2}}{x + 2}$ |
| partial | concrete | `sqrt(log(x) + 1)/(x*log(x))` | $\frac{\sqrt{\log{\left(x \right)} + 1}}{x \log{\left(x \right)}}$ |
| SOLVED-both | concrete | `(sqrt(x) + 1)**8` | $\left(\sqrt{x} + 1\right)^{8}$ |
| partial | concrete | `sqrt(9 - x**2)/x` | $\frac{\sqrt{9 - x^{2}}}{x}$ |
| NIE | concrete | `cos(sqrt(x))` | $\cos{\left(\sqrt{x} \right)}$ |
| partial | concrete | `1/sqrt(9*x**2 + 12*x - 5)` | $\frac{1}{\sqrt{9 x^{2} + 12 x - 5}}$ |
| partial | concrete | `(1 - sqrt(x))/x**(1/3)` | $\frac{1 - \sqrt{x}}{\sqrt[3]{x}}$ |
| SOLVED-both | concrete | `1/(x + x**(-1/3))` | $\frac{1}{x + \frac{1}{\sqrt[3]{x}}}$ |
| partial | concrete | `1/sqrt(-x**2 - 4*x + 5)` | $\frac{1}{\sqrt{- x^{2} - 4 x + 5}}$ |
| SOLVED-both | concrete | `x/(-x**2 + sqrt(1 - x**2) + 1)` | $\frac{x}{- x^{2} + \sqrt{1 - x^{2}} + 1}$ |
| SOLVED-both | parametric | `x*(c + x)**(1/3)` | $x \sqrt[3]{c + x}$ |
| partial | concrete | `exp(x**(1/3))` | $e^{\sqrt[3]{x}}$ |
| partial | concrete | `1/(x + sqrt(x + 1) + 4)` | $\frac{1}{x + \sqrt{x + 1} + 4}$ |
| partial | concrete | `1/sqrt(16 - x**2)` | $\frac{1}{\sqrt{16 - x^{2}}}$ |
| partial | concrete | `sqrt(t)/(t**(1/3) + 1)` | $\frac{\sqrt{t}}{\sqrt[3]{t} + 1}$ |
| partial | concrete | `sqrt((x + 1)/(1 - x))` | $\sqrt{\frac{x + 1}{1 - x}}$ |
| partial | concrete | `x*log(x)/sqrt(x**2 - 1)` | $\frac{x \log{\left(x \right)}}{\sqrt{x^{2} - 1}}$ |
| partial | concrete | `sqrt(-x**2 + x + 1)` | $\sqrt{- x^{2} + x + 1}$ |
| partial | concrete | `1/(sqrt(x) + sqrt(x + 1))` | $\frac{1}{\sqrt{x} + \sqrt{x + 1}}$ |
| NIE | concrete | `atan(sqrt(x))/sqrt(x)` | $\frac{\mathrm{atan}{\left(\sqrt{x} \right)}}{\sqrt{x}}$ |
| partial | concrete | `1/(x*sqrt(2*x - 25))` | $\frac{1}{x \sqrt{2 x - 25}}$ |
| NIE | concrete | `sin(2*x)/sqrt(9 - cos(x)**4)` | $\frac{\sin{\left(2 x \right)}}{\sqrt{9 - \cos^{4}{\left(x \right)}}}$ |
| partial | concrete | `x**2/sqrt(5 - 4*x**2)` | $\frac{x^{2}}{\sqrt{5 - 4 x^{2}}}$ |
| partial | concrete | `x*sqrt(x**2 + 2*x + 4)` | $x \sqrt{x^{2} + 2 x + 4}$ |
| partial | concrete | `sqrt(9*x**2 - 1)/x**2` | $\frac{\sqrt{9 x^{2} - 1}}{x^{2}}$ |
| partial | concrete | `sqrt(4 - 3*x**2)/x` | $\frac{\sqrt{4 - 3 x^{2}}}{x}$ |
| NIE | concrete | `sin(x)*cos(x)/sqrt(sin(x) + 1)` | $\frac{\sin{\left(x \right)} \cos{\left(x \right)}}{\sqrt{\sin{\left(x \right)} + 1}}$ |
| partial | concrete | `sqrt(-x**2 - 4*x + 5)` | $\sqrt{- x^{2} - 4 x + 5}$ |
| SOLVED-both | concrete | `x**5/(x**2 + sqrt(2))` | $\frac{x^{5}}{x^{2} + \sqrt{2}}$ |
| NIE | concrete | `sqrt(3*cos(x) + 2)*tan(x)` | $\sqrt{3 \cos{\left(x \right)} + 2} \tan{\left(x \right)}$ |
| partial | concrete | `x/sqrt(x**2 - 4*x)` | $\frac{x}{\sqrt{x^{2} - 4 x}}$ |
| partial | concrete | `x**4/sqrt(x**10 - 2)` | $\frac{x^{4}}{\sqrt{x^{10} - 2}}$ |
| partial | concrete | `sqrt(exp(2*x) - 1)` | $\sqrt{e^{2 x} - 1}$ |
| partial | concrete | `x**2*sqrt(5 - x**2)` | $x^{2} \sqrt{5 - x^{2}}$ |
| SOLVED-both | concrete | `x*sqrt(2*x + 1)` | $x \sqrt{2 x + 1}$ |
| SOLVED-both | concrete | `x**5*sqrt(x**2 + 1)` | $x^{5} \sqrt{x^{2} + 1}$ |
| SOLVED-both | concrete | `(-sqrt(x) + x + 1)**2/x**2` | $\frac{\left(- \sqrt{x} + x + 1\right)^{2}}{x^{2}}$ |
| partial | concrete | `(2 - x**(2/3))*(sqrt(x) + x)/x**(3/2)` | $\frac{\left(2 - x^{\frac{2}{3}}\right) \left(\sqrt{x} + x\right)}{x^{\frac{3}{2}}}$ |
| partial | concrete | `1/((x + 1)**(1/3) + 1)` | $\frac{1}{\sqrt[3]{x + 1} + 1}$ |
| partial | parametric | `1/(sqrt(x)*(a*x + b))` | $\frac{1}{\sqrt{x} \left(a x + b\right)}$ |
| SOLVED-both | concrete | `x**3*sqrt(x**2 + 1)` | $x^{3} \sqrt{x^{2} + 1}$ |
| partial | parametric | `x/sqrt(a**4 - x**4)` | $\frac{x}{\sqrt{a^{4} - x^{4}}}$ |
| partial | parametric | `1/(x*sqrt(-a**2 + x**2))` | $\frac{1}{x \sqrt{- a^{2} + x^{2}}}$ |
| partial | parametric | `1/(x*sqrt(a**2 - x**2))` | $\frac{1}{x \sqrt{a^{2} - x^{2}}}$ |
| partial | parametric | `1/(x*sqrt(a**2 + x**2))` | $\frac{1}{x \sqrt{a^{2} + x^{2}}}$ |
| partial | concrete | `1/sqrt(-x**2 + x + 2)` | $\frac{1}{\sqrt{- x^{2} + x + 2}}$ |
| partial | concrete | `1/sqrt(3*x**2 - 4*x + 5)` | $\frac{1}{\sqrt{3 x^{2} - 4 x + 5}}$ |
| partial | concrete | `1/sqrt(-x**2 + x)` | $\frac{1}{\sqrt{- x^{2} + x}}$ |
| partial | concrete | `(2*x + 1)/sqrt(-x**2 + x + 2)` | $\frac{2 x + 1}{\sqrt{- x^{2} + x + 2}}$ |
| partial | concrete | `1/(x*sqrt(-x**2 + x + 2))` | $\frac{1}{x \sqrt{- x^{2} + x + 2}}$ |
| NIE | parametric | `sin(2*x)/(a**2 - 4*sin(x)**2)**(1/3)` | $\frac{\sin{\left(2 x \right)}}{\sqrt[3]{a^{2} - 4 \sin^{2}{\left(x \right)}}}$ |
| partial | concrete | `exp(x/2)/sqrt(exp(x) - 1)` | $\frac{e^{\frac{x}{2}}}{\sqrt{e^{x} - 1}}$ |
| NIE | parametric | `asin(x/a)**(3/2)/sqrt(a**2 - x**2)` | $\frac{\mathrm{asin}^{\frac{3}{2}}{\left(\frac{x}{a} \right)}}{\sqrt{a^{2} - x^{2}}}$ |
| NIE | concrete | `1/(sqrt(1 - x**2)*acos(x)**3)` | $\frac{1}{\sqrt{1 - x^{2}} \mathrm{acos}^{3}{\left(x \right)}}$ |
| SOLVED-both | concrete | `x**(3/2)*(2*sqrt(x) - x)**2*(x**2 + 1)` | $x^{\frac{3}{2}} \left(2 \sqrt{x} - x\right)^{2} \left(x^{2} + 1\right)$ |
| SOLVED-both | concrete | `(-3*x**(3/5) + x**(3/2))**2*(-x**(2/3)/3 + 4*x**(3/2))` | $\left(- 3 x^{\frac{3}{5}} + x^{\frac{3}{2}}\right)^{2} \left(- \frac{x^{\frac{2}{3}}}{3} + 4 x^{\frac{3}{2}}\right)$ |
| partial | concrete | `1/(sqrt(x + 1) + 1)` | $\frac{1}{\sqrt{x + 1} + 1}$ |
| partial | concrete | `x/(sqrt(x + 1) + 1)` | $\frac{x}{\sqrt{x + 1} + 1}$ |
| partial | concrete | `(sqrt(x + 1) + 1)/(sqrt(x + 1) - 1)` | $\frac{\sqrt{x + 1} + 1}{\sqrt{x + 1} - 1}$ |
| partial | concrete | `1/((x + 1)**(2/3) - sqrt(x + 1))` | $\frac{1}{\left(x + 1\right)^{\frac{2}{3}} - \sqrt{x + 1}}$ |
| partial | concrete | `(x**(1/4) + 1)**(1/3)/sqrt(x)` | $\frac{\sqrt[3]{\sqrt[4]{x} + 1}}{\sqrt{x}}$ |
| partial | concrete | `1/(x**3*(x + 1)**(3/2))` | $\frac{1}{x^{3} \left(x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**5*(1 - x)**(7/2))` | $\frac{1}{x^{5} \left(1 - x\right)^{\frac{7}{2}}}$ |
| partial | concrete | `1/(x**5*(x - 1)**(2/3))` | $\frac{1}{x^{5} \left(x - 1\right)^{\frac{2}{3}}}$ |
| partial | concrete | `sqrt((1 - x)/(x + 1))` | $\sqrt{\frac{1 - x}{x + 1}}$ |
| partial | concrete | `sqrt(x - 5)*sqrt(x + 3)/((x - 1)*(x**2 - 25))` | $\frac{\sqrt{x - 5} \sqrt{x + 3}}{\left(x - 1\right) \left(x^{2} - 25\right)}$ |
| partial | concrete | `((x - 1)**2*(x + 1))**(-1/3)` | $\frac{1}{\sqrt[3]{\left(x - 1\right)^{2} \left(x + 1\right)}}$ |
| partial | concrete | `((x - 1)**2*(x + 1))**(1/3)/x**2` | $\frac{\sqrt[3]{\left(x - 1\right)^{2} \left(x + 1\right)}}{x^{2}}$ |
| SOLVED-both | concrete | `(x**2 - 2*x - 3)**(-5/2)` | $\frac{1}{\left(x^{2} - 2 x - 3\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/sqrt(x**3 - 5*x**2 + 3*x + 9)` | $\frac{1}{\sqrt{x^{3} - 5 x^{2} + 3 x + 9}}$ |
| partial | concrete | `(x**3 - 5*x**2 + 3*x + 9)**(-3/2)` | $\frac{1}{\left(x^{3} - 5 x^{2} + 3 x + 9\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(x**3 - 5*x**2 + 3*x + 9)**(-1/3)` | $\frac{1}{\sqrt[3]{x^{3} - 5 x^{2} + 3 x + 9}}$ |
| **SOLVED-NEW** | concrete | `(x**3 - 5*x**2 + 3*x + 9)**(-2/3)` | $\frac{1}{\left(x^{3} - 5 x^{2} + 3 x + 9\right)^{\frac{2}{3}}}$ |
| **SOLVED-NEW** | concrete | `(x**3 - 5*x**2 + 3*x + 9)**(-4/3)` | $\frac{1}{\left(x^{3} - 5 x^{2} + 3 x + 9\right)^{\frac{4}{3}}}$ |
| partial | concrete | `1/sqrt(-2*x**2 + 3*x + 4)` | $\frac{1}{\sqrt{- 2 x^{2} + 3 x + 4}}$ |
| partial | concrete | `1/sqrt(-x**2 + 4*x - 3)` | $\frac{1}{\sqrt{- x^{2} + 4 x - 3}}$ |
| partial | concrete | `1/sqrt(-3*x**2 - 5*x - 2)` | $\frac{1}{\sqrt{- 3 x^{2} - 5 x - 2}}$ |
| partial | concrete | `1/(sqrt(1 - x**2)*(x**2 + 4))` | $\frac{1}{\sqrt{1 - x^{2}} \left(x^{2} + 4\right)}$ |
| partial | concrete | `1/((x**2 + 4)*sqrt(4*x**2 + 1))` | $\frac{1}{\left(x^{2} + 4\right) \sqrt{4 x^{2} + 1}}$ |
| partial | concrete | `x/((3 - x**2)*sqrt(5 - x**2))` | $\frac{x}{\left(3 - x^{2}\right) \sqrt{5 - x^{2}}}$ |
| partial | concrete | `x/(sqrt(3 - x**2)*(5 - x**2))` | $\frac{x}{\sqrt{3 - x^{2}} \left(5 - x^{2}\right)}$ |
| partial | concrete | `1/(sqrt(x**2 + 2)*(x**4 - 1))` | $\frac{1}{\sqrt{x^{2} + 2} \left(x^{4} - 1\right)}$ |
| partial | concrete | `x/((x**2 - 1)*sqrt(x**2 + 2*x + 4))` | $\frac{x}{\left(x^{2} - 1\right) \sqrt{x^{2} + 2 x + 4}}$ |
| partial | concrete | `1/((x**3 - 8)*sqrt(x**2 + 2*x + 5))` | $\frac{1}{\left(x^{3} - 8\right) \sqrt{x^{2} + 2 x + 5}}$ |
| partial | concrete | `x/((x**2 + x + 4)*sqrt(4*x**2 + 4*x + 5))` | $\frac{x}{\left(x^{2} + x + 4\right) \sqrt{4 x^{2} + 4 x + 5}}$ |
| partial | concrete | `(x + 3)/((x**2 + 1)*sqrt(x**2 + x + 1))` | $\frac{x + 3}{\left(x^{2} + 1\right) \sqrt{x^{2} + x + 1}}$ |
| partial | concrete | `(2*x + 1)/(sqrt(x**2 + 6*x - 1)*(3*x**2 + 4*x + 4))` | $\frac{2 x + 1}{\sqrt{x^{2} + 6 x - 1} \left(3 x^{2} + 4 x + 4\right)}$ |
| partial | concrete | `(x - 2)/((5*x**2 - 18*x + 17)*sqrt(10*x**2 - 22*x + 13))` | $\frac{x - 2}{\left(5 x^{2} - 18 x + 17\right) \sqrt{10 x^{2} - 22 x + 13}}$ |
| partial | concrete | `x**4*sqrt(5 - x**2)` | $x^{4} \sqrt{5 - x^{2}}$ |
| SOLVED-both | concrete | `1/(x**6*sqrt(x**2 + 2))` | $\frac{1}{x^{6} \sqrt{x^{2} + 2}}$ |
| SOLVED-both | concrete | `(2*x**2 + 3)**(-7/2)` | $\frac{1}{\left(2 x^{2} + 3\right)^{\frac{7}{2}}}$ |
| SOLVED-both | parametric | `x/(a*sqrt(x**2 + 1) + x**2 + 1)` | $\frac{x}{a \sqrt{x^{2} + 1} + x^{2} + 1}$ |
| partial | concrete | `(x**2 - x + 1)/(x**2 + 1)**(3/2)` | $\frac{x^{2} - x + 1}{\left(x^{2} + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `sqrt(x**2 + 1)/(x**2 + 2)` | $\frac{\sqrt{x^{2} + 1}}{x^{2} + 2}$ |
| partial | concrete | `1/(sqrt(x**2 + 1)*(x**2 + 2)**2)` | $\frac{1}{\sqrt{x^{2} + 1} \left(x^{2} + 2\right)^{2}}$ |
| partial | concrete | `x**2/((x**2 - 6)*sqrt(x**2 - 2))` | $\frac{x^{2}}{\left(x^{2} - 6\right) \sqrt{x^{2} - 2}}$ |
| partial | concrete | `(x**2 + 5)/(sqrt(1 - x**2)*(x**2 + 1)**2)` | $\frac{x^{2} + 5}{\sqrt{1 - x^{2}} \left(x^{2} + 1\right)^{2}}$ |
| partial | concrete | `(4*x - sqrt(1 - x**2))/(sqrt(1 - x**2) + 5)` | $\frac{4 x - \sqrt{1 - x^{2}}}{\sqrt{1 - x^{2}} + 5}$ |
| partial | concrete | `x**2*(2 - sqrt(x**2 + 1))/(sqrt(x**2 + 1)*(-x**3 + (x**2 + 1)**(3/2) + 1))` | $\frac{x^{2} \left(2 - \sqrt{x^{2} + 1}\right)}{\sqrt{x^{2} + 1} \left(- x^{3} + \left(x^{2} + 1\right)^{\frac{3}{2}} + 1\right)}$ |
| partial | parametric | `x*sqrt(2*r*x - x**2)` | $x \sqrt{2 r x - x^{2}}$ |
| partial | parametric | `x**2*sqrt(2*r*x - x**2)` | $x^{2} \sqrt{2 r x - x^{2}}$ |
| partial | parametric | `x**3*sqrt(2*r*x - x**2)` | $x^{3} \sqrt{2 r x - x^{2}}$ |
| partial | concrete | `1/((x**2 - 1)*sqrt(x**2 + 2*x))` | $\frac{1}{\left(x^{2} - 1\right) \sqrt{x^{2} + 2 x}}$ |
| partial | concrete | `(3*x - 2)/((x + 1)**3*sqrt(-x**2 + 2*x))` | $\frac{3 x - 2}{\left(x + 1\right)^{3} \sqrt{- x^{2} + 2 x}}$ |
| partial | concrete | `1/sqrt(x**2 + x + 1)` | $\frac{1}{\sqrt{x^{2} + x + 1}}$ |
| partial | concrete | `x**3/sqrt(x**2 + x + 1)` | $\frac{x^{3}}{\sqrt{x^{2} + x + 1}}$ |
| SOLVED-both | concrete | `(x**2 + x + 1)**(-3/2)` | $\frac{1}{\left(x^{2} + x + 1\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `x/(x**2 + x + 1)**(3/2)` | $\frac{x}{\left(x^{2} + x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**3/(x**2 + x + 1)**(3/2)` | $\frac{x^{3}}{\left(x^{2} + x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**2*sqrt(x**2 + x + 1)` | $x^{2} \sqrt{x^{2} + x + 1}$ |
| partial | concrete | `(x**2 + x + 1)**(3/2)` | $\left(x^{2} + x + 1\right)^{\frac{3}{2}}$ |
| partial | concrete | `(x**2 + x + 1)**(5/2)` | $\left(x^{2} + x + 1\right)^{\frac{5}{2}}$ |
| partial | concrete | `1/(x**2*sqrt(x**2 + x + 1))` | $\frac{1}{x^{2} \sqrt{x^{2} + x + 1}}$ |
| partial | concrete | `1/(x**3*sqrt(x**2 + x + 1))` | $\frac{1}{x^{3} \sqrt{x^{2} + x + 1}}$ |
| partial | concrete | `1/(x**2*(x**2 + x + 1)**(3/2))` | $\frac{1}{x^{2} \left(x^{2} + x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/(x**3*(x**2 + x + 1)**(3/2))` | $\frac{1}{x^{3} \left(x^{2} + x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `1/((x + 1)*sqrt(x**2 + x + 1))` | $\frac{1}{\left(x + 1\right) \sqrt{x^{2} + x + 1}}$ |
| partial | concrete | `1/((x**3 - x)*sqrt(x**2 + 2*x + 4))` | $\frac{1}{\left(x^{3} - x\right) \sqrt{x^{2} + 2 x + 4}}$ |
| partial | concrete | `sqrt(x**2 + 2*x + 4)/(x - 1)**2` | $\frac{\sqrt{x^{2} + 2 x + 4}}{\left(x - 1\right)^{2}}$ |
| partial | concrete | `(2*x + 3)/((x**2 + 2*x + 3)**2*sqrt(x**2 + 2*x + 4))` | $\frac{2 x + 3}{\left(x^{2} + 2 x + 3\right)^{2} \sqrt{x^{2} + 2 x + 4}}$ |
| **SOLVED-NEW** | concrete | `(2*x**3 + 3*x**2)/(sqrt(x**2 + 2*x - 3)*(2*x**2 + x - 3))` | $\frac{2 x^{3} + 3 x^{2}}{\sqrt{x^{2} + 2 x - 3} \left(2 x^{2} + x - 3\right)}$ |
| partial | concrete | `(x**4 + 1)/((x**2 + x + 1)*sqrt(x**2 + x + 2))` | $\frac{x^{4} + 1}{\left(x^{2} + x + 1\right) \sqrt{x^{2} + x + 2}}$ |
| SOLVED-both | concrete | `(x**2 + 2*x + 4)**(-7/2)` | $\frac{1}{\left(x^{2} + 2 x + 4\right)^{\frac{7}{2}}}$ |
| SOLVED-both | concrete | `(3*x**2 + 8*x + 1)**(-5/2)` | $\frac{1}{\left(3 x^{2} + 8 x + 1\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(-3*x**2 + 4*x + 5)**(-5/2)` | $\frac{1}{\left(- 3 x^{2} + 4 x + 5\right)^{\frac{5}{2}}}$ |
| partial | concrete | `1/(sqrt(x**2 + 2*x + 2) + 1)` | $\frac{1}{\sqrt{x^{2} + 2 x + 2} + 1}$ |
| partial | concrete | `1/(x + sqrt(x**2 + x + 1))` | $\frac{1}{x + \sqrt{x^{2} + x + 1}}$ |
| partial | concrete | `x**2/(2*x + 2*sqrt(x**2 + x + 1) + 1)` | $\frac{x^{2}}{2 x + 2 \sqrt{x^{2} + x + 1} + 1}$ |
| partial | concrete | `(-3*x + sqrt(x**2 + x + 1))/(sqrt(x**2 + x + 1) - 1)` | $\frac{- 3 x + \sqrt{x^{2} + x + 1}}{\sqrt{x^{2} + x + 1} - 1}$ |
| partial | concrete | `(x + 1)/(-sqrt(x**2 + x + 1) + sqrt(x**2 + 2*x + 4))` | $\frac{x + 1}{- \sqrt{x^{2} + x + 1} + \sqrt{x^{2} + 2 x + 4}}$ |
| partial | concrete | `1/(x**3*sqrt(x - 1))` | $\frac{1}{x^{3} \sqrt{x - 1}}$ |
| SOLVED-both | concrete | `1/(x**2*(1 - 3/x)**(4/3))` | $\frac{1}{x^{2} \left(1 - \frac{3}{x}\right)^{\frac{4}{3}}}$ |
| partial | concrete | `(3*x - 1)**(4/3)/x**2` | $\frac{\left(3 x - 1\right)^{\frac{4}{3}}}{x^{2}}$ |
| SOLVED-both | concrete | `x**2*(4 - 3*x)**(4/3)` | $x^{2} \left(4 - 3 x\right)^{\frac{4}{3}}$ |
| partial | concrete | `(1 - 2*x**(1/3))**(3/4)/x` | $\frac{\left(1 - 2 \sqrt[3]{x}\right)^{\frac{3}{4}}}{x}$ |
| partial | concrete | `x/(3 - 2*sqrt(x))**(3/4)` | $\frac{x}{\left(3 - 2 \sqrt{x}\right)^{\frac{3}{4}}}$ |
| partial | concrete | `(2*sqrt(x) - 1)**(5/4)/x**2` | $\frac{\left(2 \sqrt{x} - 1\right)^{\frac{5}{4}}}{x^{2}}$ |
| SOLVED-both | concrete | `x**6*(x**7 + 1)**(1/3)` | $x^{6} \sqrt[3]{x^{7} + 1}$ |
| SOLVED-both | concrete | `x**6/(x**7 + 1)**(5/3)` | $\frac{x^{6}}{\left(x^{7} + 1\right)^{\frac{5}{3}}}$ |
| partial | concrete | `1/(x*(2*x**7 - 27)**(2/3))` | $\frac{1}{x \left(2 x^{7} - 27\right)^{\frac{2}{3}}}$ |
| partial | concrete | `(x**7 + 1)**(2/3)/x**8` | $\frac{\left(x^{7} + 1\right)^{\frac{2}{3}}}{x^{8}}$ |
| partial | concrete | `(4*x**4 + 3)**(1/4)/x**2` | $\frac{\sqrt[4]{4 x^{4} + 3}}{x^{2}}$ |
| partial | concrete | `x**2*(4*x**4 + 3)**(5/4)` | $x^{2} \left(4 x^{4} + 3\right)^{\frac{5}{4}}$ |
| partial | concrete | `x**6*(4*x**4 + 3)**(1/4)` | $x^{6} \sqrt[4]{4 x^{4} + 3}$ |
| partial | concrete | `(x*(1 - x**2))**(1/3)` | $\sqrt[3]{x \left(1 - x^{2}\right)}$ |
| partial | concrete | `x**3/((x**4 - 1)*sqrt(2*x**8 + 1))` | $\frac{x^{3}}{\left(x^{4} - 1\right) \sqrt{2 x^{8} + 1}}$ |
| partial | concrete | `x**9*sqrt(x**10 + x**5 + 1)` | $x^{9} \sqrt{x^{10} + x^{5} + 1}$ |
| partial | concrete | `1/(x**5*sqrt(x**4 + 2*x**2 + 4))` | $\frac{1}{x^{5} \sqrt{x^{4} + 2 x^{2} + 4}}$ |
| partial | concrete | `(x**2 - 1)/(x*sqrt(x**4 + 3*x**2 + 1))` | $\frac{x^{2} - 1}{x \sqrt{x^{4} + 3 x^{2} + 1}}$ |
| SOLVED-both | concrete | `(2*x**3 - 3*x)*(x**4 - 3*x**2)**(3/5)` | $\left(2 x^{3} - 3 x\right) \left(x^{4} - 3 x^{2}\right)^{\frac{3}{5}}$ |
| partial | concrete | `(3*x**8 - 2*x**5 - x**2*(3*x**3 - 1)**(2/3))/(3*x**3 - 1)**(3/4)` | $\frac{3 x^{8} - 2 x^{5} - x^{2} \left(3 x^{3} - 1\right)^{\frac{2}{3}}}{\left(3 x^{3} - 1\right)^{\frac{3}{4}}}$ |
| partial | concrete | `1/((x**3 - 1)*(x**3 + 2)**(1/3))` | $\frac{1}{\left(x^{3} - 1\right) \sqrt[3]{x^{3} + 2}}$ |
| partial | concrete | `1/((x**4 + 1)*(x**4 + 2)**(1/4))` | $\frac{1}{\left(x^{4} + 1\right) \sqrt[4]{x^{4} + 2}}$ |
| partial | concrete | `(x**3 - 1)/(x**3 + 2)**(1/3)` | $\frac{x^{3} - 1}{\sqrt[3]{x^{3} + 2}}$ |
| partial | concrete | `(x**4 + 1)**(3/4)/(x**4 + 2)**2` | $\frac{\left(x^{4} + 1\right)^{\frac{3}{4}}}{\left(x^{4} + 2\right)^{2}}$ |
| partial | concrete | `1/((x**3 + 3*x**2 + 3*x)*(x**3 + 3*x**2 + 3*x + 3)**(1/3))` | $\frac{1}{\left(x^{3} + 3 x^{2} + 3 x\right) \sqrt[3]{x^{3} + 3 x^{2} + 3 x + 3}}$ |
| partial | concrete | `(1 - x**2)/((x**2 + 1)*sqrt(x**4 + 1))` | $\frac{1 - x^{2}}{\left(x^{2} + 1\right) \sqrt{x^{4} + 1}}$ |
| partial | concrete | `(x**2 + 1)/((1 - x**2)*sqrt(x**4 + 1))` | $\frac{x^{2} + 1}{\left(1 - x^{2}\right) \sqrt{x^{4} + 1}}$ |
| partial | concrete | `(x**2 + 1)/((1 - x**2)*sqrt(x**4 + x**2 + 1))` | $\frac{x^{2} + 1}{\left(1 - x^{2}\right) \sqrt{x^{4} + x^{2} + 1}}$ |
| partial | concrete | `(1 - x**2)/((x**2 + 1)*sqrt(x**4 + x**2 + 1))` | $\frac{1 - x^{2}}{\left(x^{2} + 1\right) \sqrt{x^{4} + x^{2} + 1}}$ |
| **SOLVED-NEW** | concrete | `(x**4 - 1)/(x**2*sqrt(x**4 + x**2 + 1))` | $\frac{x^{4} - 1}{x^{2} \sqrt{x^{4} + x^{2} + 1}}$ |
| partial | parametric | `(1 - x**2)/((2*a*x + x**2 + 1)*sqrt(2*a*x**3 + 2*a*x + 2*b*x**2 + x**4 + 1))` | $\frac{1 - x^{2}}{\left(2 a x + x^{2} + 1\right) \sqrt{2 a x^{3} + 2 a x + 2 b x^{2} + x^{4} + 1}}$ |
| NIE | concrete | `1/(sqrt(-x**2 + sqrt(x**4 + 1))*(x**4 + 1))` | $\frac{1}{\sqrt{- x^{2} + \sqrt{x^{4} + 1}} \left(x^{4} + 1\right)}$ |
| NIE | concrete | `tan(x)**5*sec(x)**(3/2)` | $\tan^{5}{\left(x \right)} \sec^{\frac{3}{2}}{\left(x \right)}$ |
| NIE | concrete | `tan(x)**(3/2)*sec(x)**4` | $\tan^{\frac{3}{2}}{\left(x \right)} \sec^{4}{\left(x \right)}$ |
| NIE | concrete | `sqrt(sin(2*x) + 1)` | $\sqrt{\sin{\left(2 x \right)} + 1}$ |
| NIE | concrete | `sqrt(1 - sin(2*x))` | $\sqrt{1 - \sin{\left(2 x \right)}}$ |
| NIE | concrete | `1/sqrt(cos(2*x) + 1)` | $\frac{1}{\sqrt{\cos{\left(2 x \right)} + 1}}$ |
| NIE | concrete | `1/sqrt(1 - cos(2*x))` | $\frac{1}{\sqrt{1 - \cos{\left(2 x \right)}}}$ |
| NIE | concrete | `(1 - cos(3*x))**(-3/2)` | $\frac{1}{\left(1 - \cos{\left(3 x \right)}\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `(1 - sin(2*x/3))**(5/2)` | $\left(1 - \sin{\left(\frac{2 x}{3} \right)}\right)^{\frac{5}{2}}$ |
| NIE | concrete | `(2*(2*sin(x) + 1)**(1/4) - cos(x)**2)*cos(x)/(2*sin(x) + 1)**(3/2)` | $\frac{\left(2 \sqrt[4]{2 \sin{\left(x \right)} + 1} - \cos^{2}{\left(x \right)}\right) \cos{\left(x \right)}}{\left(2 \sin{\left(x \right)} + 1\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `sqrt(tan(x))` | $\sqrt{\tan{\left(x \right)}}$ |
| NIE | concrete | `(3*tan(2*x) + 4)**(-3/2)` | $\frac{1}{\left(3 \tan{\left(2 x \right)} + 4\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `(-sqrt(4 - 3*tan(x)) + 3*tan(x))/((4 - 3*tan(x))**(3/2)*cos(x)**2)` | $\frac{- \sqrt{4 - 3 \tan{\left(x \right)}} + 3 \tan{\left(x \right)}}{\left(4 - 3 \tan{\left(x \right)}\right)^{\frac{3}{2}} \cos^{2}{\left(x \right)}}$ |
| NIE | concrete | `tan(x)/(sqrt(tan(x)) - 1)**2` | $\frac{\tan{\left(x \right)}}{\left(\sqrt{\tan{\left(x \right)}} - 1\right)^{2}}$ |
| NIE | concrete | `sin(x)/sqrt(sin(2*x))` | $\frac{\sin{\left(x \right)}}{\sqrt{\sin{\left(2 x \right)}}}$ |
| NIE | concrete | `cos(x)/sqrt(sin(2*x))` | $\frac{\cos{\left(x \right)}}{\sqrt{\sin{\left(2 x \right)}}}$ |
| NIE | concrete | `sin(x)*sqrt(sin(2*x))` | $\sin{\left(x \right)} \sqrt{\sin{\left(2 x \right)}}$ |
| NIE | concrete | `(-sin(x) + cos(x))*sqrt(sin(2*x))` | $\left(- \sin{\left(x \right)} + \cos{\left(x \right)}\right) \sqrt{\sin{\left(2 x \right)}}$ |
| NIE | concrete | `sin(x)**7/sin(2*x)**(7/2)` | $\frac{\sin^{7}{\left(x \right)}}{\sin^{\frac{7}{2}}{\left(2 x \right)}}$ |
| NIE | concrete | `cos(x)**7/sin(2*x)**(7/2)` | $\frac{\cos^{7}{\left(x \right)}}{\sin^{\frac{7}{2}}{\left(2 x \right)}}$ |
| NIE | concrete | `sin(2*x)**(3/2)/sin(x)**5` | $\frac{\sin^{\frac{3}{2}}{\left(2 x \right)}}{\sin^{5}{\left(x \right)}}$ |
| NIE | concrete | `1/(sqrt(sin(2*x))*cos(x)**3)` | $\frac{1}{\sqrt{\sin{\left(2 x \right)}} \cos^{3}{\left(x \right)}}$ |
| NIE | concrete | `1/(sin(x)*sin(2*x)**(3/2))` | $\frac{1}{\sin{\left(x \right)} \sin^{\frac{3}{2}}{\left(2 x \right)}}$ |
| NIE | concrete | `(sin(x)**2/cos(x)**14)**(1/3)` | $\sqrt[3]{\frac{\sin^{2}{\left(x \right)}}{\cos^{14}{\left(x \right)}}}$ |
| NIE | concrete | `(sin(x)**13*cos(x)**11)**(-1/4)` | $\frac{1}{\sqrt[4]{\sin^{13}{\left(x \right)} \cos^{11}{\left(x \right)}}}$ |
| NIE | concrete | `(sin(x)**2 + 5*cos(x)**2)**(5/2)*cos(x)` | $\left(\sin^{2}{\left(x \right)} + 5 \cos^{2}{\left(x \right)}\right)^{\frac{5}{2}} \cos{\left(x \right)}$ |
| NIE | concrete | `(-5*sin(x)**2 - cos(x)**2)**(3/2)*cos(x)` | $\left(- 5 \sin^{2}{\left(x \right)} - \cos^{2}{\left(x \right)}\right)^{\frac{3}{2}} \cos{\left(x \right)}$ |
| NIE | concrete | `sin(x)/(-2*sin(x)**2 + 5*cos(x)**2)**(7/2)` | $\frac{\sin{\left(x \right)}}{\left(- 2 \sin^{2}{\left(x \right)} + 5 \cos^{2}{\left(x \right)}\right)^{\frac{7}{2}}}$ |
| NIE | concrete | `cos(x)*cos(2*x)/(2 - 5*sin(x)**2)**(3/2)` | $\frac{\cos{\left(x \right)} \cos{\left(2 x \right)}}{\left(2 - 5 \sin^{2}{\left(x \right)}\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `sin(5*x)/(9*sin(x)**2 + 5*cos(x)**2)**(5/2)` | $\frac{\sin{\left(5 x \right)}}{\left(9 \sin^{2}{\left(x \right)} + 5 \cos^{2}{\left(x \right)}\right)^{\frac{5}{2}}}$ |
| NIE | concrete | `sin(3*x)*cos(x)*cos(2*x)/(4*sin(x)**2 - 5)**(5/2)` | $\frac{\sin{\left(3 x \right)} \cos{\left(x \right)} \cos{\left(2 x \right)}}{\left(4 \sin^{2}{\left(x \right)} - 5\right)^{\frac{5}{2}}}$ |
| NIE | concrete | `(2 - 3*sin(x)**2)**(3/5)*sin(4*x)` | $\left(2 - 3 \sin^{2}{\left(x \right)}\right)^{\frac{3}{5}} \sin{\left(4 x \right)}$ |
| NIE | concrete | `cos(x)*sqrt(cos(2*x))` | $\cos{\left(x \right)} \sqrt{\cos{\left(2 x \right)}}$ |
| NIE | concrete | `sin(x)*cos(2*x)**(3/2)` | $\sin{\left(x \right)} \cos^{\frac{3}{2}}{\left(2 x \right)}$ |
| NIE | concrete | `sin(x)/cos(2*x)**(5/2)` | $\frac{\sin{\left(x \right)}}{\cos^{\frac{5}{2}}{\left(2 x \right)}}$ |
| NIE | concrete | `cos(2*x)**(3/2)/cos(x)**3` | $\frac{\cos^{\frac{3}{2}}{\left(2 x \right)}}{\cos^{3}{\left(x \right)}}$ |
| NIE | concrete | `(4 - 5*sec(x)**2)**(3/2)` | $\left(4 - 5 \sec^{2}{\left(x \right)}\right)^{\frac{3}{2}}$ |
| NIE | concrete | `(4 - 5*sec(x)**2)**(-3/2)` | $\frac{1}{\left(4 - 5 \sec^{2}{\left(x \right)}\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `(cos(2*x) - 3)/(sqrt(4 - cot(x)**2)*cos(x)**4)` | $\frac{\cos{\left(2 x \right)} - 3}{\sqrt{4 - \cot^{2}{\left(x \right)}} \cos^{4}{\left(x \right)}}$ |
| NIE | concrete | `(sin(x)**2 + 3)*tan(x)**3/((5 - 4*sec(x)**2)**(3/2)*(cos(x)**2 - 2))` | $\frac{\left(\sin^{2}{\left(x \right)} + 3\right) \tan^{3}{\left(x \right)}}{\left(5 - 4 \sec^{2}{\left(x \right)}\right)^{\frac{3}{2}} \left(\cos^{2}{\left(x \right)} - 2\right)}$ |
| NIE | concrete | `(-3*sqrt(5*tan(x)**2 + 4*sec(x)**2)*tan(x) + sec(x)**2)/((5*tan(x)**2 + 4*sec(x)**2)**(3/2)*sin(x)**2)` | $\frac{- 3 \sqrt{5 \tan^{2}{\left(x \right)} + 4 \sec^{2}{\left(x \right)}} \tan{\left(x \right)} + \sec^{2}{\left(x \right)}}{\left(5 \tan^{2}{\left(x \right)} + 4 \sec^{2}{\left(x \right)}\right)^{\frac{3}{2}} \sin^{2}{\left(x \right)}}$ |
| NIE | concrete | `(5*tan(x)**2 + 1)**(5/2)*tan(x)` | $\left(5 \tan^{2}{\left(x \right)} + 1\right)^{\frac{5}{2}} \tan{\left(x \right)}$ |
| NIE | concrete | `tan(x)/(5*tan(x)**2 + 1)**(5/2)` | $\frac{\tan{\left(x \right)}}{\left(5 \tan^{2}{\left(x \right)} + 1\right)^{\frac{5}{2}}}$ |
| NIE | parametric | `tan(x)/(a**3 + b**3*tan(x)**2)**(1/3)` | $\frac{\tan{\left(x \right)}}{\sqrt[3]{a^{3} + b^{3} \tan^{2}{\left(x \right)}}}$ |
| NIE | concrete | `(1 - 7*tan(x)**2)**(2/3)*tan(x)` | $\left(1 - 7 \tan^{2}{\left(x \right)}\right)^{\frac{2}{3}} \tan{\left(x \right)}$ |
| NIE | parametric | `cot(x)/(a**4 + b**4*csc(x)**2)**(1/4)` | $\frac{\cot{\left(x \right)}}{\sqrt[4]{a^{4} + b^{4} \csc^{2}{\left(x \right)}}}$ |
| NIE | parametric | `cot(x)/(a**4 - b**4*csc(x)**2)**(1/4)` | $\frac{\cot{\left(x \right)}}{\sqrt[4]{a^{4} - b^{4} \csc^{2}{\left(x \right)}}}$ |
| NIE | concrete | `(-cos(2*x) + 2*tan(x)**2)/((tan(x)*tan(2*x))**(3/2)*cos(x)**2)` | $\frac{- \cos{\left(2 x \right)} + 2 \tan^{2}{\left(x \right)}}{\left(\tan{\left(x \right)} \tan{\left(2 x \right)}\right)^{\frac{3}{2}} \cos^{2}{\left(x \right)}}$ |
| NIE | concrete | `sin(x)**9*cot(x)/(2 - 5*sin(x)**3)**(4/3)` | $\frac{\sin^{9}{\left(x \right)} \cot{\left(x \right)}}{\left(2 - 5 \sin^{3}{\left(x \right)}\right)^{\frac{4}{3}}}$ |
| NIE | concrete | `((1 - 8*tan(x)**2)**(1/3) + 1)*tan(x)/((1 - 8*tan(x)**2)**(2/3)*cos(x)**2)` | $\frac{\left(\sqrt[3]{1 - 8 \tan^{2}{\left(x \right)}} + 1\right) \tan{\left(x \right)}}{\left(1 - 8 \tan^{2}{\left(x \right)}\right)^{\frac{2}{3}} \cos^{2}{\left(x \right)}}$ |
| NIE | concrete | `cos(x)**4*cos(2*x)**(2/3)*tan(x)` | $\cos^{4}{\left(x \right)} \cos^{\frac{2}{3}}{\left(2 x \right)} \tan{\left(x \right)}$ |
| NIE | concrete | `sin(x)**6*tan(x)/cos(2*x)**(3/4)` | $\frac{\sin^{6}{\left(x \right)} \tan{\left(x \right)}}{\cos^{\frac{3}{4}}{\left(2 x \right)}}$ |
| NIE | concrete | `sqrt(cot(2*x)/cot(x))` | $\sqrt{\frac{\cot{\left(2 x \right)}}{\cot{\left(x \right)}}}$ |
| partial | concrete | `1/(x*(x**2 - 2)**(5/2))` | $\frac{1}{x \left(x^{2} - 2\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(x**2 - 10)**(5/2)/x` | $\frac{\left(x^{2} - 10\right)^{\frac{5}{2}}}{x}$ |
| SOLVED-both | concrete | `x**3*(x**2 + 1)**(9/14)` | $x^{3} \left(x^{2} + 1\right)^{\frac{9}{14}}$ |
| SOLVED-both | concrete | `x**5/(x**2 - 4)**(13/6)` | $\frac{x^{5}}{\left(x^{2} - 4\right)^{\frac{13}{6}}}$ |
| SOLVED-both | concrete | `(2*x**2 + 1)**(-5/2)` | $\frac{1}{\left(2 x^{2} + 1\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(x**2 - 2*x - 1)**(-5/2)` | $\frac{1}{\left(x^{2} - 2 x - 1\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `1/(x**4*(x**2 - 8)**(3/2))` | $\frac{1}{x^{4} \left(x^{2} - 8\right)^{\frac{3}{2}}}$ |
| SOLVED-both | concrete | `(x**2 + 5)**2/x**(13/3)` | $\frac{\left(x^{2} + 5\right)^{2}}{x^{\frac{13}{3}}}$ |
| **SOLVED-NEW** | concrete | `((x**2 + 2)/x**2)**(7/9)/(x**2 + 2)**(3/2)` | $\frac{\left(\frac{x^{2} + 2}{x^{2}}\right)^{\frac{7}{9}}}{\left(x^{2} + 2\right)^{\frac{3}{2}}}$ |
| partial | concrete | `x**2/(3 - x**2)**(3/2)` | $\frac{x^{2}}{\left(3 - x^{2}\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(25 - x**2)**(3/2)/x**4` | $\frac{\left(25 - x^{2}\right)^{\frac{3}{2}}}{x^{4}}$ |
| SOLVED-both | concrete | `(1 - 2*x**2)**(-7/2)` | $\frac{1}{\left(1 - 2 x^{2}\right)^{\frac{7}{2}}}$ |
| SOLVED-both | concrete | `(-x**2 + 6*x - 7)**(-5/2)` | $\frac{1}{\left(- x^{2} + 6 x - 7\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(3*x + 1)/(2*x**2 - 8*x + 1)**(5/2)` | $\frac{3 x + 1}{\left(2 x^{2} - 8 x + 1\right)^{\frac{5}{2}}}$ |
| SOLVED-both | concrete | `(8*x**3 - 8*x - 1)/(-4*x**2 + 2*x + 1)**(5/2)` | $\frac{8 x^{3} - 8 x - 1}{\left(- 4 x^{2} + 2 x + 1\right)^{\frac{5}{2}}}$ |
| partial | concrete | `(1 - 2*exp(x/3))**(1/4)` | $\sqrt[4]{1 - 2 e^{\frac{x}{3}}}$ |
| partial | parametric | `exp(x)/sqrt(a**2 + exp(2*x))` | $\frac{e^{x}}{\sqrt{a^{2} + e^{2 x}}}$ |
| partial | parametric | `exp(x)/sqrt(-a**2 + exp(2*x))` | $\frac{e^{x}}{\sqrt{- a^{2} + e^{2 x}}}$ |
| partial | concrete | `exp(3*x/4)/((exp(3*x/4) - 2)*sqrt(exp(3*x/4) + exp(3*x/2) - 2))` | $\frac{e^{\frac{3 x}{4}}}{\left(e^{\frac{3 x}{4}} - 2\right) \sqrt{e^{\frac{3 x}{4}} + e^{\frac{3 x}{2}} - 2}}$ |
| SOLVED-both | concrete | `exp(2*x)/(3 - exp(x/2))**(3/4)` | $\frac{e^{2 x}}{\left(3 - e^{\frac{x}{2}}\right)^{\frac{3}{4}}}$ |
| NIE | concrete | `(-x**2 - x + 1)*exp(x)/sqrt(1 - x**2)` | $\frac{\left(- x^{2} - x + 1\right) e^{x}}{\sqrt{1 - x^{2}}}$ |
| NIE | concrete | `(sin(x/2) + cos(x/2))/exp(x)**(1/3)` | $\frac{\sin{\left(\frac{x}{2} \right)} + \cos{\left(\frac{x}{2} \right)}}{\sqrt[3]{e^{x}}}$ |
| NIE | concrete | `cos(x/3)**3/sqrt(exp(x))` | $\frac{\cos^{3}{\left(\frac{x}{3} \right)}}{\sqrt{e^{x}}}$ |
| NIE | concrete | `tanh(x)**5*sech(x)**(3/4)` | $\tanh^{5}{\left(x \right)} \mathrm{sech}^{\frac{3}{4}}{\left(x \right)}$ |
| NIE | concrete | `sinh(x)/(4*cosh(x)**2 - 9)**(5/2)` | $\frac{\sinh{\left(x \right)}}{\left(4 \cosh^{2}{\left(x \right)} - 9\right)^{\frac{5}{2}}}$ |
| NIE | concrete | `sinh(x)**2*sinh(2*x)/(1 - sinh(x)**2)**(3/2)` | $\frac{\sinh^{2}{\left(x \right)} \sinh{\left(2 x \right)}}{\left(1 - \sinh^{2}{\left(x \right)}\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `cosh(x)/sqrt(cosh(2*x))` | $\frac{\cosh{\left(x \right)}}{\sqrt{\cosh{\left(2 x \right)}}}$ |
| SOLVED-both | concrete | `log(x)**2/x**(5/2)` | $\frac{\log{\left(x \right)}^{2}}{x^{\frac{5}{2}}}$ |
| partial | parametric | `1/(x*sqrt(a**2 + log(x)**2))` | $\frac{1}{x \sqrt{a^{2} + \log{\left(x \right)}^{2}}}$ |
| partial | parametric | `1/(x*sqrt(-a**2 + log(x)**2))` | $\frac{1}{x \sqrt{- a^{2} + \log{\left(x \right)}^{2}}}$ |
| partial | parametric | `1/(x*sqrt(a**2 - log(x)**2))` | $\frac{1}{x \sqrt{a^{2} - \log{\left(x \right)}^{2}}}$ |
| partial | parametric | `1/(x*sqrt(a**2 + log(x)**2)*log(x))` | $\frac{1}{x \sqrt{a^{2} + \log{\left(x \right)}^{2}} \log{\left(x \right)}}$ |
| partial | parametric | `1/(x*sqrt(a**2 - log(x)**2)*log(x))` | $\frac{1}{x \sqrt{a^{2} - \log{\left(x \right)}^{2}} \log{\left(x \right)}}$ |
| partial | parametric | `1/(x*sqrt(-a**2 + log(x)**2)*log(x))` | $\frac{1}{x \sqrt{- a^{2} + \log{\left(x \right)}^{2}} \log{\left(x \right)}}$ |
| partial | concrete | `log(x - sqrt(x**2 + 1))` | $\log{\left(x - \sqrt{x^{2} + 1} \right)}$ |
| NIE | concrete | `sqrt(1 - x**2)*asin(x)` | $\sqrt{1 - x^{2}} \mathrm{asin}{\left(x \right)}$ |
| NIE | concrete | `sqrt(1 - x**2)*acos(x)` | $\sqrt{1 - x^{2}} \mathrm{acos}{\left(x \right)}$ |
| NIE | concrete | `x*sqrt(1 - x**2)*acos(x)` | $x \sqrt{1 - x^{2}} \mathrm{acos}{\left(x \right)}$ |
| NIE | concrete | `(1 - x**2)**(3/2)*asin(x)` | $\left(1 - x^{2}\right)^{\frac{3}{2}} \mathrm{asin}{\left(x \right)}$ |
| NIE | concrete | `x*(1 - x**2)**(3/2)*asin(x)` | $x \left(1 - x^{2}\right)^{\frac{3}{2}} \mathrm{asin}{\left(x \right)}$ |
| NIE | concrete | `x**3*(1 - x**2)**(3/2)*acos(x)` | $x^{3} \left(1 - x^{2}\right)^{\frac{3}{2}} \mathrm{acos}{\left(x \right)}$ |
| NIE | concrete | `(1 - x**2)**(3/2)*acos(x)/x` | $\frac{\left(1 - x^{2}\right)^{\frac{3}{2}} \mathrm{acos}{\left(x \right)}}{x}$ |
| NIE | concrete | `(1 - x**2)**(3/2)*asin(x)/x**6` | $\frac{\left(1 - x^{2}\right)^{\frac{3}{2}} \mathrm{asin}{\left(x \right)}}{x^{6}}$ |
| NIE | concrete | `x**2*asin(x)/sqrt(1 - x**2)` | $\frac{x^{2} \mathrm{asin}{\left(x \right)}}{\sqrt{1 - x^{2}}}$ |
| NIE | concrete | `x**4*asin(x)/sqrt(1 - x**2)` | $\frac{x^{4} \mathrm{asin}{\left(x \right)}}{\sqrt{1 - x^{2}}}$ |
| NIE | concrete | `x*asin(x)/(1 - x**2)**(3/2)` | $\frac{x \mathrm{asin}{\left(x \right)}}{\left(1 - x^{2}\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `x*acos(x)/(1 - x**2)**(3/2)` | $\frac{x \mathrm{acos}{\left(x \right)}}{\left(1 - x^{2}\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `asin(x)/(1 - x**2)**(5/2)` | $\frac{\mathrm{asin}{\left(x \right)}}{\left(1 - x^{2}\right)^{\frac{5}{2}}}$ |
| NIE | concrete | `x**3*asin(x)/(1 - x**2)**(3/2)` | $\frac{x^{3} \mathrm{asin}{\left(x \right)}}{\left(1 - x^{2}\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `asin(x)/(x*(1 - x**2)**(3/2))` | $\frac{\mathrm{asin}{\left(x \right)}}{x \left(1 - x^{2}\right)^{\frac{3}{2}}}$ |
| NIE | concrete | `acos(x)/(x**4*sqrt(1 - x**2))` | $\frac{\mathrm{acos}{\left(x \right)}}{x^{4} \sqrt{1 - x^{2}}}$ |
| NIE | concrete | `x*sqrt(1 - x**2)*acos(x)**2` | $x \sqrt{1 - x^{2}} \mathrm{acos}^{2}{\left(x \right)}$ |
| NIE | concrete | `x**2*asin(x)**3/sqrt(1 - x**2)` | $\frac{x^{2} \mathrm{asin}^{3}{\left(x \right)}}{\sqrt{1 - x^{2}}}$ |
| NIE | concrete | `sqrt(x**2 - 1)*asec(x)/x**4` | $\frac{\sqrt{x^{2} - 1} \mathrm{asec}{\left(x \right)}}{x^{4}}$ |
| NIE | concrete | `asec(x)/(x**2*sqrt(x**2 - 1))` | $\frac{\mathrm{asec}{\left(x \right)}}{x^{2} \sqrt{x^{2} - 1}}$ |
| NIE | parametric | `asin(sqrt((-a + x)/(a + x)))` | $\mathrm{asin}{\left(\sqrt{\frac{- a + x}{a + x}} \right)}$ |
| NIE | parametric | `atan(sqrt((-a + x)/(a + x)))` | $\mathrm{atan}{\left(\sqrt{\frac{- a + x}{a + x}} \right)}$ |
| NIE | concrete | `asin(sqrt(1 - x**2))/sqrt(1 - x**2)` | $\frac{\mathrm{asin}{\left(\sqrt{1 - x^{2}} \right)}}{\sqrt{1 - x^{2}}}$ |
| NIE | concrete | `x*atan(sqrt(x**2 + 1))/sqrt(x**2 + 1)` | $\frac{x \mathrm{atan}{\left(\sqrt{x^{2} + 1} \right)}}{\sqrt{x^{2} + 1}}$ |
| NIE | concrete | `asin(x)/(1 - x)**(5/2)` | $\frac{\mathrm{asin}{\left(x \right)}}{\left(1 - x\right)^{\frac{5}{2}}}$ |
| SOLVED-both | parametric | `1/sqrt(-a*x + 1)` | $\frac{1}{\sqrt{- a x + 1}}$ |
| partial | concrete | `(2*x + sqrt(x**2 + 1))**(-2)` | $\frac{1}{\left(2 x + \sqrt{x^{2} + 1}\right)^{2}}$ |
| partial | concrete | `1/(sqrt(x**2 - 1)*(3*x**2 - 4)**2)` | $\frac{1}{\sqrt{x^{2} - 1} \left(3 x^{2} - 4\right)^{2}}$ |
| partial | concrete | `(2*sqrt(x) + sqrt(x + 1))**(-2)` | $\frac{1}{\left(2 \sqrt{x} + \sqrt{x + 1}\right)^{2}}$ |
| partial | concrete | `sqrt(x**2 - 1)/(x - I)**2` | $\frac{\sqrt{x^{2} - 1}}{\left(x - i\right)^{2}}$ |
| partial | concrete | `1/(sqrt(x**2 - 1)*(x**2 + 1)**2)` | $\frac{1}{\sqrt{x^{2} - 1} \left(x^{2} + 1\right)^{2}}$ |
| partial | concrete | `1/((sqrt(x) + sqrt(x - 1))**2*sqrt(x - 1))` | $\frac{1}{\left(\sqrt{x} + \sqrt{x - 1}\right)^{2} \sqrt{x - 1}}$ |
| partial | concrete | `1/((sqrt(x) + sqrt(x**2 - 1))**2*sqrt(x**2 - 1))` | $\frac{1}{\left(\sqrt{x} + \sqrt{x^{2} - 1}\right)^{2} \sqrt{x^{2} - 1}}$ |
| timeout | concrete | `(sqrt(x) - sqrt(x**2 - 1))**2/(sqrt(x**2 - 1)*(-x**2 + x + 1)**2)` | $\frac{\left(\sqrt{x} - \sqrt{x^{2} - 1}\right)^{2}}{\sqrt{x^{2} - 1} \left(- x^{2} + x + 1\right)^{2}}$ |
| partial | concrete | `sqrt(2)/(2*(x + 1)**2*sqrt(x**2 + I)) + sqrt(2)/(2*(x + 1)**2*sqrt(x**2 - I))` | $\frac{\sqrt{2}}{2 \left(x + 1\right)^{2} \sqrt{x^{2} + i}} + \frac{\sqrt{2}}{2 \left(x + 1\right)^{2} \sqrt{x^{2} - i}}$ |
| NIE | concrete | `sqrt(x**2 + sqrt(x**4 + 1))/((x + 1)**2*sqrt(x**4 + 1))` | $\frac{\sqrt{x^{2} + \sqrt{x^{4} + 1}}}{\left(x + 1\right)^{2} \sqrt{x^{4} + 1}}$ |
| NIE | concrete | `sqrt(x**2 + sqrt(x**4 + 1))/((x + 1)*sqrt(x**4 + 1))` | $\frac{\sqrt{x^{2} + \sqrt{x^{4} + 1}}}{\left(x + 1\right) \sqrt{x^{4} + 1}}$ |
| NIE | concrete | `sqrt(x**2 + sqrt(x**4 + 1))/sqrt(x**4 + 1)` | $\frac{\sqrt{x^{2} + \sqrt{x^{4} + 1}}}{\sqrt{x^{4} + 1}}$ |
| NIE | concrete | `sqrt(-x**2 + sqrt(x**4 + 1))/sqrt(x**4 + 1)` | $\frac{\sqrt{- x^{2} + \sqrt{x^{4} + 1}}}{\sqrt{x^{4} + 1}}$ |
| partial | concrete | `((x - 1)**(3/2) + (x + 1)**(3/2))/((x - 1)**(3/2)*(x + 1)**(3/2))` | $\frac{\left(x - 1\right)^{\frac{3}{2}} + \left(x + 1\right)^{\frac{3}{2}}}{\left(x - 1\right)^{\frac{3}{2}} \left(x + 1\right)^{\frac{3}{2}}}$ |
| partial | concrete | `(3*x**2 - x + 1)/(sqrt(x**2 - x + 1)*(x**2 + x + 1)**2)` | $\frac{3 x^{2} - x + 1}{\sqrt{x^{2} - x + 1} \left(x^{2} + x + 1\right)^{2}}$ |
| NIE | parametric | `sqrt(x + sqrt(a**2 + x**2))/sqrt(a**2 + x**2)` | $\frac{\sqrt{x + \sqrt{a^{2} + x^{2}}}}{\sqrt{a^{2} + x^{2}}}$ |
| NIE | parametric | `sqrt(b*x + sqrt(a + b**2*x**2))/sqrt(a + b**2*x**2)` | $\frac{\sqrt{b x + \sqrt{a + b^{2} x^{2}}}}{\sqrt{a + b^{2} x^{2}}}$ |
| NIE | parametric | `1/(x*sqrt(a**2 + x**2)*sqrt(x + sqrt(a**2 + x**2)))` | $\frac{1}{x \sqrt{a^{2} + x^{2}} \sqrt{x + \sqrt{a^{2} + x^{2}}}}$ |
| NIE | parametric | `sqrt(x + sqrt(a**2 + x**2))/x` | $\frac{\sqrt{x + \sqrt{a^{2} + x^{2}}}}{x}$ |
| partial | concrete | `1/(x*(1 - x**2)**(1/3))` | $\frac{1}{x \sqrt[3]{1 - x^{2}}}$ |
| partial | concrete | `1/(x*(1 - x**2)**(2/3))` | $\frac{1}{x \left(1 - x^{2}\right)^{\frac{2}{3}}}$ |
| partial | concrete | `(1 - x**3)**(-1/3)` | $\frac{1}{\sqrt[3]{1 - x^{3}}}$ |
| partial | concrete | `1/(x*(1 - x**3)**(1/3))` | $\frac{1}{x \sqrt[3]{1 - x^{3}}}$ |
| partial | concrete | `1/((1 - x**3)**(1/3)*(x + 1))` | $\frac{1}{\sqrt[3]{1 - x^{3}} \left(x + 1\right)}$ |
| partial | concrete | `x/((1 - x**3)**(1/3)*(x + 1))` | $\frac{x}{\sqrt[3]{1 - x^{3}} \left(x + 1\right)}$ |
| partial | concrete | `1/(x*(x**2 - 3*x + 2)**(1/3))` | $\frac{1}{x \sqrt[3]{x^{2} - 3 x + 2}}$ |
| partial | concrete | `(x**3 - 3*x**2 + 7*x - 5)**(-1/3)` | $\frac{1}{\sqrt[3]{x^{3} - 3 x^{2} + 7 x - 5}}$ |
| partial | parametric | `(x*(-q + x**2))**(-1/3)` | $\frac{1}{\sqrt[3]{x \left(- q + x^{2}\right)}}$ |
| partial | parametric | `((x - 1)*(q + x**2 - 2*x))**(-1/3)` | $\frac{1}{\sqrt[3]{\left(x - 1\right) \left(q + x^{2} - 2 x\right)}}$ |
| partial | parametric | `1/(x*((x - 1)*(-2*q*x + q + x**2))**(1/3))` | $\frac{1}{x \sqrt[3]{\left(x - 1\right) \left(- 2 q x + q + x^{2}\right)}}$ |
| partial | parametric | `(-x*(k + 1) + 2)/((x*(1 - x)*(-k*x + 1))**(1/3)*(-x*(k + 1) + 1))` | $\frac{- x \left(k + 1\right) + 2}{\sqrt[3]{x \left(1 - x\right) \left(- k x + 1\right)} \left(- x \left(k + 1\right) + 1\right)}$ |
| partial | parametric | `(-k*x + 1)/((x*(1 - x)*(-k*x + 1))**(2/3)*(x*(k - 2) + 1))` | $\frac{- k x + 1}{\left(x \left(1 - x\right) \left(- k x + 1\right)\right)^{\frac{2}{3}} \left(x \left(k - 2\right) + 1\right)}$ |
| partial | parametric | `(a + b*x + c*x**2)/((1 - x**3)**(1/3)*(x**2 - x + 1))` | $\frac{a + b x + c x^{2}}{\sqrt[3]{1 - x^{3}} \left(x^{2} - x + 1\right)}$ |
| partial | concrete | `1/((3 - 2*x)**(11/2)*(2*x**2 + x + 1)**5)` | $\frac{1}{\left(3 - 2 x\right)^{\frac{11}{2}} \left(2 x^{2} + x + 1\right)^{5}}$ |
| partial | concrete | `1/((3 - 2*x)**(21/2)*(2*x**2 + x + 1)**10)` | $\frac{1}{\left(3 - 2 x\right)^{\frac{21}{2}} \left(2 x^{2} + x + 1\right)^{10}}$ |
| partial | concrete | `1/((3 - 2*x)**(41/2)*(2*x**2 + x + 1)**20)` | $\frac{1}{\left(3 - 2 x\right)^{\frac{41}{2}} \left(2 x^{2} + x + 1\right)^{20}}$ |
| partial | concrete | `1/((x**2 - 2*x + 3)**(11/2)*(2*x**2 + x + 1)**5)` | $\frac{1}{\left(x^{2} - 2 x + 3\right)^{\frac{11}{2}} \left(2 x^{2} + x + 1\right)^{5}}$ |
| partial | concrete | `1/((x**2 - 2*x + 3)**(21/2)*(2*x**2 + x + 1)**10)` | $\frac{1}{\left(x^{2} - 2 x + 3\right)^{\frac{21}{2}} \left(2 x^{2} + x + 1\right)^{10}}$ |
| partial | parametric | `(-a + x - sqrt(a**2 + 1))/(sqrt((-a + x)*(x**2 + 1))*(-a + x + sqrt(a**2 + 1)))` | $\frac{- a + x - \sqrt{a^{2} + 1}}{\sqrt{\left(- a + x\right) \left(x^{2} + 1\right)} \left(- a + x + \sqrt{a^{2} + 1}\right)}$ |
| partial | parametric | `(a + b*x)/((1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{a + b x}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | parametric | `(a + b*x)/((3 - x**2)*(x**2 + 1)**(1/3))` | $\frac{a + b x}{\left(3 - x^{2}\right) \sqrt[3]{x^{2} + 1}}$ |
| partial | concrete | `1/(x*(3*x**2 - 6*x + 4)**(1/3))` | $\frac{1}{x \sqrt[3]{3 x^{2} - 6 x + 4}}$ |
| partial | concrete | `x*(1 - x**3)**(1/3)` | $x \sqrt[3]{1 - x^{3}}$ |
| partial | concrete | `(1 - x**3)**(1/3)/x` | $\frac{\sqrt[3]{1 - x^{3}}}{x}$ |
| partial | concrete | `(1 - x**3)**(1/3)/(x + 1)` | $\frac{\sqrt[3]{1 - x^{3}}}{x + 1}$ |
| partial | concrete | `(1 - x**3)**(1/3)/(x**2 - x + 1)` | $\frac{\sqrt[3]{1 - x^{3}}}{x^{2} - x + 1}$ |
| partial | concrete | `sqrt(1 - x**4)/(x**4 + 1)` | $\frac{\sqrt{1 - x^{4}}}{x^{4} + 1}$ |
| partial | concrete | `sqrt(x**4 + 1)/(1 - x**4)` | $\frac{\sqrt{x^{4} + 1}}{1 - x^{4}}$ |
| partial | parametric | `sqrt(p*x**2 + x**4 + 1)/(1 - x**4)` | $\frac{\sqrt{p x^{2} + x^{4} + 1}}{1 - x^{4}}$ |
| partial | parametric | `sqrt(p*x**2 - x**4 + 1)/(x**4 + 1)` | $\frac{\sqrt{p x^{2} - x^{4} + 1}}{x^{4} + 1}$ |
| partial | parametric | `(a + b*x)/((2 - x**2)*(x**2 - 1)**(1/4))` | $\frac{a + b x}{\left(2 - x^{2}\right) \sqrt[4]{x^{2} - 1}}$ |
| partial | parametric | `(a + b*x)/((-x**2 - 1)**(1/4)*(x**2 + 2))` | $\frac{a + b x}{\sqrt[4]{- x^{2} - 1} \left(x^{2} + 2\right)}$ |
| partial | parametric | `(a + b*x)/((1 - x**2)**(1/4)*(2 - x**2))` | $\frac{a + b x}{\sqrt[4]{1 - x^{2}} \left(2 - x^{2}\right)}$ |
| partial | parametric | `(a + b*x)/((x**2 + 1)**(1/4)*(x**2 + 2))` | $\frac{a + b x}{\sqrt[4]{x^{2} + 1} \left(x^{2} + 2\right)}$ |
| partial | concrete | `x/(sqrt(1 - x**3)*(4 - x**3))` | $\frac{x}{\sqrt{1 - x^{3}} \left(4 - x^{3}\right)}$ |
| partial | parametric | `x/((-d*x**3 + 4)*sqrt(d*x**3 - 1))` | $\frac{x}{\left(- d x^{3} + 4\right) \sqrt{d x^{3} - 1}}$ |
| partial | concrete | `x/(sqrt(x**3 - 1)*(x**3 + 8))` | $\frac{x}{\sqrt{x^{3} - 1} \left(x^{3} + 8\right)}$ |
| partial | parametric | `x/((-d*x**3 + 8)*sqrt(d*x**3 + 1))` | $\frac{x}{\left(- d x^{3} + 8\right) \sqrt{d x^{3} + 1}}$ |
| partial | concrete | `1/((1 - 3*x**2)**(1/3)*(3 - x**2))` | $\frac{1}{\sqrt[3]{1 - 3 x^{2}} \left(3 - x^{2}\right)}$ |
| partial | concrete | `1/((x**2 + 3)*(3*x**2 + 1)**(1/3))` | $\frac{1}{\left(x^{2} + 3\right) \sqrt[3]{3 x^{2} + 1}}$ |
| partial | concrete | `1/((1 - x**2)**(1/3)*(x**2 + 3))` | $\frac{1}{\sqrt[3]{1 - x^{2}} \left(x^{2} + 3\right)}$ |
| partial | concrete | `1/((3 - x**2)*(x**2 + 1)**(1/3))` | $\frac{1}{\left(3 - x^{2}\right) \sqrt[3]{x^{2} + 1}}$ |
| partial | parametric | `(a + x)/((-a + x)*sqrt(a**2*x + x**3 - x**2*(a**2 + 1)))` | $\frac{a + x}{\left(- a + x\right) \sqrt{a^{2} x + x^{3} - x^{2} \left(a^{2} + 1\right)}}$ |
| partial | parametric | `(a + x - 2)/((-a + x)*sqrt(a*x*(2 - a) + x**3 + x**2*(a**2 - 2*a - 1)))` | $\frac{a + x - 2}{\left(- a + x\right) \sqrt{a x \left(2 - a\right) + x^{3} + x^{2} \left(a^{2} - 2 a - 1\right)}}$ |
| partial | parametric | `(-a + x*(2*a - 1))/((-a + x)*sqrt(a**2*x + x**3*(2*a - 1) - x**2*(a**2 + 2*a - 1)))` | $\frac{- a + x \left(2 a - 1\right)}{\left(- a + x\right) \sqrt{a^{2} x + x^{3} \left(2 a - 1\right) - x^{2} \left(a^{2} + 2 a - 1\right)}}$ |
| partial | concrete | `(-2**(1/3)*x + 1)/((x + 2**(2/3))*sqrt(x**3 + 1))` | $\frac{- \sqrt[3]{2} x + 1}{\left(x + 2^{\frac{2}{3}}\right) \sqrt{x^{3} + 1}}$ |
| partial | concrete | `(x + 1)/((x - 2)*sqrt(x**3 + 1))` | $\frac{x + 1}{\left(x - 2\right) \sqrt{x^{3} + 1}}$ |
| partial | concrete | `x/(sqrt(x**3 + 1)*(x**3 + 10 + 6*sqrt(3)))` | $\frac{x}{\sqrt{x^{3} + 1} \left(x^{3} + 10 + 6 \sqrt{3}\right)}$ |
| partial | concrete | `x/(sqrt(x**3 + 1)*(x**3 - 6*sqrt(3) + 10))` | $\frac{x}{\sqrt{x^{3} + 1} \left(x^{3} - 6 \sqrt{3} + 10\right)}$ |
| partial | concrete | `x/(sqrt(x**3 - 1)*(x**3 - 6*sqrt(3) - 10))` | $\frac{x}{\sqrt{x^{3} - 1} \left(x^{3} - 6 \sqrt{3} - 10\right)}$ |
| partial | concrete | `x/(sqrt(x**3 - 1)*(x**3 - 10 + 6*sqrt(3)))` | $\frac{x}{\sqrt{x^{3} - 1} \left(x^{3} - 10 + 6 \sqrt{3}\right)}$ |
| partial | concrete | `(x - sqrt(3) + 1)/((x + 1 + sqrt(3))*sqrt(x**4 + 4*sqrt(3)*x**2 - 4))` | $\frac{x - \sqrt{3} + 1}{\left(x + 1 + \sqrt{3}\right) \sqrt{x^{4} + 4 \sqrt{3} x^{2} - 4}}$ |
| partial | concrete | `(x + 1 + sqrt(3))/((x - sqrt(3) + 1)*sqrt(x**4 - 4*sqrt(3)*x**2 - 4))` | $\frac{x + 1 + \sqrt{3}}{\left(x - \sqrt{3} + 1\right) \sqrt{x^{4} - 4 \sqrt{3} x^{2} - 4}}$ |
| partial | concrete | `(x - 1)/((x + 1)*(x**3 + 2)**(1/3))` | $\frac{x - 1}{\left(x + 1\right) \sqrt[3]{x^{3} + 2}}$ |
| partial | concrete | `1/((x + 1)*(x**3 + 2)**(1/3))` | $\frac{1}{\left(x + 1\right) \sqrt[3]{x^{3} + 2}}$ |
| partial | concrete | `(x + 1)/((1 - x**3)**(1/3)*(x**2 - x + 1))` | $\frac{x + 1}{\sqrt[3]{1 - x^{3}} \left(x^{2} - x + 1\right)}$ |
| partial | concrete | `(x + 1)**2/((1 - x**3)**(1/3)*(x**3 + 1))` | $\frac{\left(x + 1\right)^{2}}{\sqrt[3]{1 - x^{3}} \left(x^{3} + 1\right)}$ |
| SOLVED-both | concrete | `(3*x - 5)**2/(2*x - 1)**(7/2)` | $\frac{\left(3 x - 5\right)^{2}}{\left(2 x - 1\right)^{\frac{7}{2}}}$ |
