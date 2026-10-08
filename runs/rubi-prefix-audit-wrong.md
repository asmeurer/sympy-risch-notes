# Pre-fix audit: all WRONG cases (worktree a1c2226052)

Every solved case whose derivative failed the numerical oracle
at some sample point, with the attribution class and the first
failing point.  Classes: radicand-split (the known unconditional
factor-split bug, fixed by the branch-ratio commits);
dependent-radicands (proportional radicands through the
is_deriv_k rewrite, fixed in 97ef0340ca); complex-only (fails
only at complex sample points).

| chapter | module | class | integrand | first bad point |
|---|---|---|---|---|
| t 0 independent test sui | apostol_problems | radicand-split | `x**5/sqrt(1 - x**6)` | `-333/64` |
| t 0 independent test sui | apostol_problems | radicand-split | `x/(-x**2 + sqrt(4 - x**2) + 4)` | `-333/64` |
| t 0 independent test sui | hearn_problems | radicand-split | `x/(1 - x**2)**(9/8)` | `-333/64` |
| t 0 independent test sui | hearn_problems | complex-only | `sqrt(x**4 + 2 + x**(-4))` | `33/64 + 3*I/4` |
| t 0 independent test sui | hearn_problems | radicand-split | `x*(x**2*sqrt(x**2 - 4) + x**2*sqrt(x**2 - 1) - sqrt(x**2 - 4) - 4*sqrt(x**2 - 1))/((x**4 - 5*x**2 + 4)*(sqrt(x**2 - 4) + sqrt(x**2 - 1) + 1))` | `-333/64` |
| t 0 independent test sui | stewart_problems | radicand-split | `1/(x**2*sqrt(1 - x**2))` | `-333/64` |
| t 0 independent test sui | stewart_problems | radicand-split | `x**3*sqrt(4 - x**2)` | `-333/64` |
| t 0 independent test sui | stewart_problems | radicand-split | `x/sqrt(1 - x**2)` | `-333/64` |
| t 0 independent test sui | stewart_problems | radicand-split | `x*sqrt(4 - x**2)` | `-333/64` |
| t 0 independent test sui | stewart_problems | radicand-split | `sqrt(-a**2 + x**2)/x**4` | `-333/64` |
| t 0 independent test sui | stewart_problems | radicand-split | `1/(x**2*sqrt(16*x**2 - 9))` | `-333/64` |
| t 0 independent test sui | stewart_problems | radicand-split | `x**3*sqrt(4 - 9*x**2)` | `-333/64` |
| t 0 independent test sui | stewart_problems | radicand-split | `(4*x**2 - 25)**(-3/2)` | `-333/64` |
| t 0 independent test sui | stewart_problems | radicand-split | `(-x**2 - 4*x + 5)**(-5/2)` | `-6` |
| t 0 independent test sui | stewart_problems | radicand-split | `x/sqrt(1 - x**2)` | `-333/64` |
| t 0 independent test sui | stewart_problems | radicand-split | `x/(-x**2 + sqrt(1 - x**2) + 1)` | `-333/64` |
| t 0 independent test sui | timofeev_problems | radicand-split | `(x**2 - 2*x - 3)**(-5/2)` | `-333/64` |
| t 0 independent test sui | timofeev_problems | radicand-split | `(x**3 - 5*x**2 + 3*x + 9)**(-2/3)` | `-333/64` |
| t 0 independent test sui | timofeev_problems | radicand-split | `(x**3 - 5*x**2 + 3*x + 9)**(-4/3)` | `-333/64` |
| t 0 independent test sui | timofeev_problems | radicand-split | `(2*x**3 + 3*x**2)/(sqrt(x**2 + 2*x - 3)*(2*x**2 + x - 3))` | `-333/64` |
| t 0 independent test sui | timofeev_problems | radicand-split | `(2*x**3 - 3*x)*(x**4 - 3*x**2)**(3/5)` | `-333/64` |
| t 0 independent test sui | timofeev_problems | complex-only | `(x**4 - 1)/(x**2*sqrt(x**4 + x**2 + 1))` | `-47/64 - 5*I/4` |
| t 0 independent test sui | timofeev_problems | radicand-split | `x**5/(x**2 - 4)**(13/6)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | dependent-radicands | `1/(sqrt(-3*x - 2)*sqrt(3*x + 2))` | `-29/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((a*x + a)**(3/2)*(-c*x + c)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((a*x + a)**(5/2)*(-c*x + c)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((a*x + a)**(7/2)*(-c*x + c)**(7/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((a*x + a)**(9/2)*(-c*x + c)**(9/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((a + b*x)**(3/2)*(a*c - b*c*x)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((a + b*x)**(5/2)*(a*c - b*c*x)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((a + b*x)**(7/2)*(a*c - b*c*x)**(7/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((a + b*x)**(9/2)*(a*c - b*c*x)**(9/2))` | `-173/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((3 - 6*x)**(3/2)*(4*x + 2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((3 - 6*x)**(5/2)*(4*x + 2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((3 - 6*x)**(7/2)*(4*x + 2)**(7/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((6 - 2*x)**(3/2)*(x + 3)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `1/((-2*b*x + 6)**(3/2)*(b*x + 3)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `(a + b*x)**5*(a*c + b*c*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `(a + b*x)**5*sqrt(a*c + b*c*x)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `(a + b*x)**5/sqrt(a*c + b*c*x)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `(a + b*x)**5/(a*c + b*c*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `(a + b*x)**5/(a*c + b*c*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `(a + b*x)**5/(a*c + b*c*x)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `(a + b*x)**5/(a*c + b*c*x)**(9/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `(a + b*x)**5/(a*c + b*c*x)**(11/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | radicand-split | `(a + b*x)**5/(a*c + b*c*x)**(13/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_2 | dependent-radicands | `1/(sqrt(-b*x - 2)*sqrt(b*x + 2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_3 | dependent-radicands | `x**2*sqrt(a + b*x)/sqrt(-a - b*x)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_3 | dependent-radicands | `x*sqrt(a + b*x)/sqrt(-a - b*x)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_3 | dependent-radicands | `sqrt(a + b*x)/sqrt(-a - b*x)` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_3 | dependent-radicands | `sqrt(a + b*x)/(x*sqrt(-a - b*x))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_3 | dependent-radicands | `sqrt(a + b*x)/(x**2*sqrt(-a - b*x))` | `-333/64` |
| t 1 algebraic functions | t_1_1_1_3 | dependent-radicands | `sqrt(a + b*x)/(x**3*sqrt(-a - b*x))` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x**5*sqrt(9 - 4*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x**3*sqrt(9 - 4*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x*sqrt(9 - 4*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `sqrt(9 - 4*x**2)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x**5*sqrt(4*x**2 - 9)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x**3*sqrt(4*x**2 - 9)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x*sqrt(4*x**2 - 9)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `sqrt(4*x**2 - 9)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x**5/sqrt(9 - 4*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x**3/sqrt(9 - 4*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x/sqrt(9 - 4*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `1/(x**2*sqrt(9 - 4*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `1/(x**4*sqrt(9 - 4*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x**5/sqrt(4*x**2 - 9)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x**3/sqrt(4*x**2 - 9)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x/sqrt(4*x**2 - 9)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `1/(x**2*sqrt(4*x**2 - 9))` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `1/(x**4*sqrt(4*x**2 - 9))` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_2 | radicand-split | `x*(x**2 - 1)**(7/3)` | `-333/64` |
| t 1 algebraic functions | t_1_1_2_3 | radicand-split | `1/(sqrt(2 - 2*x**2)*sqrt(x**2 - 1))` | `-3/4` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**5/sqrt(1 - x**3)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**2/sqrt(1 - x**3)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**5/sqrt(-x**3 - 1)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**2/sqrt(-x**3 - 1)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**7/sqrt(1 - x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**3/sqrt(1 - x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**7/(1 - x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**3/(1 - x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x/(1 - x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**7/sqrt(16 - x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**3/sqrt(16 - x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | complex-only | `1/(x**(7/2)*sqrt(x**5 + 1))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_1_3_2 | complex-only | `1/(x**(17/2)*sqrt(x**5 + 1))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(a + b/x)/x**2` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(a + b/x)/x**3` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(a + b/x)/x**4` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(a + b/x)/x**5` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(a + b/x)/x**6` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x)**(3/2)/x**2` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x)**(3/2)/x**3` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x)**(3/2)/x**4` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x)**(3/2)/x**5` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x)**(3/2)/x**6` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x)**(3/2)/x**7` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x)**(5/2)/x**2` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x)**(5/2)/x**3` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x)**(5/2)/x**4` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x)**(5/2)/x**5` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x)**(5/2)/x**6` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**2*sqrt(a + b/x))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**3*sqrt(a + b/x))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**4*sqrt(a + b/x))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**5*sqrt(a + b/x))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**6*sqrt(a + b/x))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**2*(a + b/x)**(3/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**3*(a + b/x)**(3/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**4*(a + b/x)**(3/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**5*(a + b/x)**(3/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**6*(a + b/x)**(3/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**7*(a + b/x)**(3/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**2*(a + b/x)**(5/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**3*(a + b/x)**(5/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**4*(a + b/x)**(5/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**5*(a + b/x)**(5/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**6*(a + b/x)**(5/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**7*(a + b/x)**(5/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(7/2)*sqrt(a + b/x)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(5/2)*sqrt(a + b/x)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(3/2)*sqrt(a + b/x)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(x)*sqrt(a + b/x)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(9/2)*(a + b/x)**(3/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(7/2)*(a + b/x)**(3/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(5/2)*(a + b/x)**(3/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(3/2)*(a + b/x)**(3/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(11/2)*(a + b/x)**(5/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(9/2)*(a + b/x)**(5/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(7/2)*(a + b/x)**(5/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(5/2)*(a + b/x)**(5/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(7/2)/sqrt(a + b/x)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(5/2)/sqrt(a + b/x)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(3/2)/sqrt(a + b/x)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(x)/sqrt(a + b/x)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(sqrt(x)*sqrt(a + b/x))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(5/2)/(a + b/x)**(3/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(3/2)/(a + b/x)**(3/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(x)/(a + b/x)**(3/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(sqrt(x)*(a + b/x)**(3/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**(3/2)*(a + b/x)**(3/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(5/2)/(a + b/x)**(5/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**(3/2)/(a + b/x)**(5/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(x)/(a + b/x)**(5/2)` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(sqrt(x)*(a + b/x)**(5/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**(3/2)*(a + b/x)**(5/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**(5/2)*(a + b/x)**(5/2))` | `-87/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**2*sqrt(a + b/x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**3*sqrt(a + b/x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**5*sqrt(a + b/x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**7*sqrt(a + b/x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**9*sqrt(a + b/x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**4/sqrt(a + b/x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**2/sqrt(a + b/x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/sqrt(a + b/x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**3*(a + b/x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**5*(a + b/x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**7*(a + b/x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**9*(a + b/x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**4/(a + b/x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**2/(a + b/x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x**2)**(-3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**2*(a + b/x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**3*(a + b/x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**5*(a + b/x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**7*(a + b/x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**9*(a + b/x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `x**2/(a + b/x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x**2)**(-5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**2*(a + b/x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**4*(a + b/x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(1 + x**(-2))**(1/3)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(1 + x**(-2))**(5/3)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(a + b/x**3)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(a + b/x**3)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(a + b/x**3)/x**10` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(a + b/x**3)/x**13` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x**3)**(3/2)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x**3)**(3/2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x**3)**(3/2)/x**10` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `(a + b/x**3)**(3/2)/x**13` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**4*sqrt(a + b/x**3))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**7*sqrt(a + b/x**3))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**10*sqrt(a + b/x**3))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**13*sqrt(a + b/x**3))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**4*(a + b/x**3)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**7*(a + b/x**3)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**10*(a + b/x**3)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `1/(x**13*(a + b/x**3)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | complex-only | `x/sqrt(a + b/x**4)` | `1/2 + 3*I/4` |
| t 1 algebraic functions | t_1_1_3_2 | complex-only | `x/(a + b/x**4)**(3/2)` | `1/2 + 3*I/4` |
| t 1 algebraic functions | t_1_1_3_2 | complex-only | `1/(x**3*(a + b/x**4)**(3/2))` | `1/2 + 3*I/4` |
| t 1 algebraic functions | t_1_1_3_2 | complex-only | `x/(a + b/x**4)**(5/2)` | `1/2 + 3*I/4` |
| t 1 algebraic functions | t_1_1_3_2 | complex-only | `1/(x**3*(a + b/x**4)**(5/2))` | `1/2 + 3*I/4` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt((10*x + 6)**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_2 | radicand-split | `sqrt(sqrt(1/x) + 1/x)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `x**10*(a + b/x**2)*sqrt(c + d/x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `x**8*(a + b/x**2)*sqrt(c + d/x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `x**6*(a + b/x**2)*sqrt(c + d/x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `x**4*(a + b/x**2)*sqrt(c + d/x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `x**12*(a + b/x**2)*(c + d/x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `x**10*(a + b/x**2)*(c + d/x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `x**8*(a + b/x**2)*(c + d/x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `x**6*(a + b/x**2)*(c + d/x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `(a + b/x**2)/(x**3*sqrt(c + d/x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `(a + b/x**2)/(x**5*sqrt(c + d/x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `(a + b/x**2)/(x**7*sqrt(c + d/x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `x**4*(a + b/x**2)/sqrt(c + d/x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `x**2*(a + b/x**2)/sqrt(c + d/x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `(a + b/x**2)/(x**3*(c + d/x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `(a + b/x**2)/(x**5*(c + d/x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `(a + b/x**2)/(x**7*(c + d/x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `(a + b/x**2)/(x**9*(c + d/x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `x**4*(a + b/x**2)/(c + d/x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `x**2*(a + b/x**2)/(c + d/x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_3_4 | radicand-split | `(a + b/x**2)/(c + d/x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**(27/2)/(a*x + b*x**3)**(9/2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**(23/2)/(a*x + b*x**3)**(9/2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**(21/2)/(a*x + b*x**3)**(9/2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**(19/2)/(a*x + b*x**3)**(9/2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**(17/2)/(a*x + b*x**3)**(9/2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**(15/2)/(a*x + b*x**3)**(9/2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**(13/2)/(a*x + b*x**3)**(9/2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**(11/2)/(a*x + b*x**3)**(9/2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**(9/2)/(a*x + b*x**3)**(9/2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**(5/2)/(a*x + b*x**3)**(9/2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `sqrt(x)/(a*x + b*x**3)**(9/2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(x**2*sqrt(a*x + b*x**4))` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(x**5*sqrt(a*x + b*x**4))` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(x**8*sqrt(a*x + b*x**4))` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**2*sqrt(a*x**2 + b*x**3)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x*sqrt(a*x**2 + b*x**3)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `sqrt(a*x**2 + b*x**3)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `sqrt(a*x**2 + b*x**3)/x` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**2*(a*x**2 + b*x**3)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x*(a*x**2 + b*x**3)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `(a*x**2 + b*x**3)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `(a*x**2 + b*x**3)**(3/2)/x` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `(a*x**2 + b*x**3)**(3/2)/x**2` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `(a*x**2 + b*x**3)**(3/2)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**4/sqrt(a*x**2 + b*x**3)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**3/sqrt(a*x**2 + b*x**3)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**2/sqrt(a*x**2 + b*x**3)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x/sqrt(a*x**2 + b*x**3)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**6/(a*x**2 + b*x**3)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**5/(a*x**2 + b*x**3)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**4/(a*x**2 + b*x**3)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**3/(a*x**2 + b*x**3)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(sqrt(x)*sqrt(a*x**2 + b*x**3))` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(x**(3/2)*sqrt(a*x**2 + b*x**3))` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(x**(5/2)*sqrt(a*x**2 + b*x**3))` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(x**(7/2)*sqrt(a*x**2 + b*x**3))` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**9/sqrt(a*x**2 + b*x**5)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**6/sqrt(a*x**2 + b*x**5)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x**3/sqrt(a*x**2 + b*x**5)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(x**(3/2)*sqrt(a*x**2 + b*x**5))` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(x**(9/2)*sqrt(a*x**2 + b*x**5))` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/sqrt(a*x**3 + b*x**4)` | `-1/2` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(x*sqrt(a*x**3 + b*x**4))` | `-1/2` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(x**2*sqrt(a*x**3 + b*x**4))` | `-1/2` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(x**3*sqrt(a*x**3 + b*x**4))` | `-1/2` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `1/(x**4*sqrt(a*x**3 + b*x**4))` | `-1/2` |
| t 1 algebraic functions | t_1_1_4_2 | radicand-split | `x*sqrt(a*x**2 + b*x**5)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**11` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)/x**13` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `x**4*(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `x**2*(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `(A + B*x**2)*sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**11` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**13` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**15` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**17` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**19` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `x**4*(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `x**2*(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `(A + B*x**2)*(b*x**2 + c*x**4)**(3/2)/x**2` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `x**6*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `x**4*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `x**2*(A + B*x**2)/sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `x*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `x**8*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `x**6*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_1_4_3 | radicand-split | `x**4*(A + B*x**2)/(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `(b*x + c*x**2)**(-7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `(-4*x**2 + 3*x)**(-3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `(-4*x**2 + 3*x)**(-5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `(-4*x**2 + 3*x)**(-7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `(9*x**2 + 12*x + 4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `sqrt(9*x**2 + 12*x + 4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `1/sqrt(9*x**2 + 12*x + 4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `(9*x**2 + 12*x + 4)**(-3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `sqrt(9*x**2 - 12*x + 4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `1/sqrt(9*x**2 - 12*x + 4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `sqrt(-9*x**2 + 12*x - 4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `1/sqrt(-9*x**2 + 12*x - 4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `sqrt(-9*x**2 - 12*x - 4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `1/sqrt(-9*x**2 - 12*x - 4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `(x**2 + 3*x + 2)**(-3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `(4*x**2 - 24*x + 27)**(-3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `x/(-x**2 - 4*x + 5)**(3/2)` | `-6` |
| t 1 algebraic functions | t_1_2_1_1 | radicand-split | `(-x**2 - 4*x + 5)**(-5/2)` | `-6` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(b*x + c*x**2)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(b*x + c*x**2)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(b*x + c*x**2)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(b*x + c*x**2)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(b*x + c*x**2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*x + c*x**2)**(3/2)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*x + c*x**2)**(3/2)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*x + c*x**2)**(3/2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*x + c*x**2)**(3/2)/x**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*x + c*x**2)**(3/2)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*x + b*x**2)**(5/2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*x + b*x**2)**(5/2)/x**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*x + b*x**2)**(5/2)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*x + b*x**2)**(5/2)/x**10` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*x + b*x**2)**(5/2)/x**11` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*x + b*x**2)**(5/2)/x**12` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x*sqrt(b*x + c*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**2*sqrt(b*x + c*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**3*sqrt(b*x + c*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**4*sqrt(b*x + c*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**5*sqrt(b*x + c*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*x + c*x**2)**(-3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x*(b*x + c*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**2*(b*x + c*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**3*(b*x + c*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**3/(a*x + b*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**2/(a*x + b*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/(a*x + b*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*x + b*x**2)**(-5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x*(a*x + b*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**2*(a*x + b*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(7/2)*sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(5/2)*sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(3/2)*sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(x)*sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(b*x + c*x**2)/sqrt(x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(7/2)*(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(5/2)*(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(3/2)*(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(x)*(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*x + c*x**2)**(3/2)/sqrt(x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*x + c*x**2)**(3/2)/x**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(7/2)/sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(5/2)/sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(3/2)/sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(x)/sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(13/2)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(11/2)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(9/2)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(7/2)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(5/2)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**(3/2)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**4*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**3*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**2*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/x` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**5*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**4*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**5*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**4*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**10` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**11` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**12` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**4/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**3/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**2/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**2*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**3*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**4*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**4/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**3/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**2/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(-3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**6/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**5/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**4/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**3/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x**2/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(-5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x*(4*x**2 + 12*x + 9)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x*(4*x**2 + 12*x + 9)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x*sqrt(4*x**2 + 12*x + 9)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/sqrt(4*x**2 + 12*x + 9)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/(4*x**2 + 12*x + 9)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/(4*x**2 + 12*x + 9)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/(4*x**2 + 12*x + 9)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/sqrt(9*x**2 + 12*x + 4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/sqrt(9*x**2 - 12*x + 4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/sqrt(-9*x**2 + 12*x - 4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `x/sqrt(-9*x**2 - 12*x - 4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*x + c*x**2)**(-3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*x + c*x**2)**(-5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((x + 2)*sqrt(x**2 + 2*x))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 - b**2*x**2)/(a + b*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 - b**2*x**2)/(a + b*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 - b**2*x**2)/(a + b*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 - b**2*x**2)/(a + b*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 - b**2*x**2)/(a + b*x)**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 - b**2*x**2)**(3/2)/(a + b*x)**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**10` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**11` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**12` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d**2 - e**2*x**2)**(7/2)/(d + e*x)**13` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(1 - x**2)/(1 - x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*sqrt(d**2 - e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**2*sqrt(d**2 - e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**4*sqrt(d**2 - e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**5*sqrt(d**2 - e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3/(d**2 - e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2/(d**2 - e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(d**2 - e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**2*(d**2 - e**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**3*(d**2 - e**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**4*(d**2 - e**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**5/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**4/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*(d**2 - e**2*x**2)**(7/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**2*(d**2 - e**2*x**2)**(7/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**3*(d**2 - e**2*x**2)**(7/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**4*(d**2 - e**2*x**2)**(7/2))` | `-173/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**5*(d**2 - e**2*x**2)**(7/2))` | `-173/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(5/2)*sqrt(c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(3/2)*sqrt(c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(d + e*x)*sqrt(c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(c*d**2 - c*e**2*x**2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(5/2)*(c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(3/2)*(c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(d + e*x)*(c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 - c*e**2*x**2)**(3/2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(7/2)/sqrt(c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(5/2)/sqrt(c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(3/2)/sqrt(c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(d + e*x)/sqrt(c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(9/2)/(c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(7/2)/(c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(5/2)/(c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(3/2)/(c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(e*x + 2)**(5/2)*sqrt(-3*e**2*x**2 + 12)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(e*x + 2)**(3/2)*sqrt(-3*e**2*x**2 + 12)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(e*x + 2)*sqrt(-3*e**2*x**2 + 12)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(-3*e**2*x**2 + 12)/sqrt(e*x + 2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(e*x + 2)**(5/2)*(-3*e**2*x**2 + 12)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(e*x + 2)**(3/2)*(-3*e**2*x**2 + 12)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(e*x + 2)*(-3*e**2*x**2 + 12)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(-3*e**2*x**2 + 12)**(3/2)/sqrt(e*x + 2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(-3*e**2*x**2 + 12)**(3/2)/(e*x + 2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(e*x + 2)**(7/2)/sqrt(-3*e**2*x**2 + 12)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(e*x + 2)**(5/2)/sqrt(-3*e**2*x**2 + 12)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(e*x + 2)**(3/2)/sqrt(-3*e**2*x**2 + 12)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(e*x + 2)/sqrt(-3*e**2*x**2 + 12)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(e*x + 2)**(11/2)/(-3*e**2*x**2 + 12)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(e*x + 2)**(9/2)/(-3*e**2*x**2 + 12)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(e*x + 2)**(7/2)/(-3*e**2*x**2 + 12)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(e*x + 2)**(5/2)/(-3*e**2*x**2 + 12)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(e*x + 2)**(3/2)/(-3*e**2*x**2 + 12)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(-3*e**2*x**2 + 12)**(1/4)/(e*x + 2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(-3*e**2*x**2 + 12)**(1/4)/(e*x + 2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(-3*e**2*x**2 + 12)**(1/4)/(e*x + 2)**(9/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(-3*e**2*x**2 + 12)**(1/4)/(e*x + 2)**(11/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((e*x + 2)**(3/2)*(-3*e**2*x**2 + 12)**(1/4))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((e*x + 2)**(5/2)*(-3*e**2*x**2 + 12)**(1/4))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((e*x + 2)**(7/2)*(-3*e**2*x**2 + 12)**(1/4))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((e*x + 2)**(9/2)*(-3*e**2*x**2 + 12)**(1/4))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)/(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)/(d + e*x)**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)/(d + e*x)**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)/(d + e*x)**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**4/sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3/sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2/sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**2*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**3*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**4*sqrt(c*d**2 + 2*c*d*e*x + c*e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**4/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(-3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**2*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**3*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**6/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**5/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**4/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(-5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**2*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**3*(c*d**2 + 2*c*d*e*x + c*e**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*d + 2*c*d*x)**(5/2)*(a + b*x + c*x**2)` | `1198373/16777216` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*d + 2*c*d*x)**(3/2)*(a + b*x + c*x**2)` | `1198373/16777216` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2)` | `1198373/16777216` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(b*d + 2*c*d*x)**(3/2)*(a + b*x + c*x**2)**2` | `1198373/16777216` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2)**2` | `1198373/16777216` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(b*d + 2*c*d*x)*(a + b*x + c*x**2)**3` | `1198373/16777216` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(17/3)` | `1198373/16777216` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(23/3)` | `1198373/16777216` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a + b*x + c*x**2)**(4/3)/(b*d + 2*c*d*x)**(29/3)` | `1198373/16777216` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(x + 1)/(x**2 + 2*x - 3)**(2/3)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**4*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**5*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**4*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**5*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**4*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**4/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**2*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**3*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**4*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**4/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(-3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**6/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**5/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**4/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(-5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)*(4*x**2 + 12*x + 9)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)*(4*x**2 + 12*x + 9)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)*sqrt(4*x**2 + 12*x + 9)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/sqrt(4*x**2 + 12*x + 9)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(4*x**2 + 12*x + 9)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(4*x**2 + 12*x + 9)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(4*x**2 + 12*x + 9)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(5/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(3/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(9/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(11/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(9/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(11/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(13/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(15/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**10` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**2*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**3*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**4*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(-3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**3/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**2/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(-5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(7/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(5/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(3/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(5/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(7/2)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(5/2)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(3/2)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `sqrt(d + e*x)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(7/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(5/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(3/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(7/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(d + e*x)**(5/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `(x + 1)/(x**2 + 3*x + 2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*sqrt(b**2/(4*c) + b*x + c*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((d + e*x)*sqrt(b*x + c*x**2 + (b*d*e - c*d**2)/e**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/((b*e/(2*c) + e*x)*sqrt(b**2/(4*c) + b*x + c*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x*sqrt(a**2 - 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x*sqrt(-a**2 + 2*a*b*x - b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_2 | radicand-split | `1/(x*sqrt(-a**2 - 2*a*b*x - b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(b*x + c*x**2)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(b*x + c*x**2)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(b*x + c*x**2)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(b*x + c*x**2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(b*x + c*x**2)/x**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**10` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**10` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**11` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**12` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**2*sqrt(b*x + c*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**3*sqrt(b*x + c*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**4*sqrt(b*x + c*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**5*sqrt(b*x + c*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**6*sqrt(b*x + c*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x*(b*x + c*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**2*(b*x + c*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**3*(b*x + c*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**4*(b*x + c*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**2*(A + B*x)/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x*(A + B*x)/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x*(b*x + c*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**2*(b*x + c*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**3*(b*x + c*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)/(b*x + c*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)/(b*x + c*x**2)**(9/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(7/2)*(A + B*x)*sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(5/2)*(A + B*x)*sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(3/2)*(A + B*x)*sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `sqrt(x)*(A + B*x)*sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(b*x + c*x**2)/sqrt(x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(5/2)*(A + B*x)*(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(3/2)*(A + B*x)*(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `sqrt(x)*(A + B*x)*(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(3/2)/sqrt(x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(3/2)/x**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(3/2)*(A + B*x)*(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `sqrt(x)*(A + B*x)*(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(5/2)/sqrt(x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(b*x + c*x**2)**(5/2)/x**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(7/2)*(A + B*x)/sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(5/2)*(A + B*x)/sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(3/2)*(A + B*x)/sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `sqrt(x)*(A + B*x)/sqrt(b*x + c*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(9/2)*(A + B*x)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(7/2)*(A + B*x)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(5/2)*(A + B*x)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(3/2)*(A + B*x)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(11/2)*(A + B*x)/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(9/2)*(A + B*x)/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(7/2)*(A + B*x)/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(5/2)*(A + B*x)/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**4*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**3*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**2*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**5*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**4*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**3*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**2*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**10` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**11` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**12` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**6*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**5*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**4*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**3*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**2*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**10` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**11` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**12` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**13` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**4*(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**3*(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**2*(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x*(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**2*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**3*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**4*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**5*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**4*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**3*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**2*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**4*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**3*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**2*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x*(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(x**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(7/2)*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(5/2)*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(3/2)*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `sqrt(x)*(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/sqrt(x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/x**(9/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(7/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(5/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(3/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `sqrt(x)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/sqrt(x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/x**(9/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(7/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(5/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `x**(3/2)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `sqrt(x)*(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/sqrt(x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/x**(9/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(b*x + c*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**2/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(b*x + c*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**4*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**3*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**2*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**5*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**4*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**6*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**5*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**4*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**3/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**2/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/((d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/((d + e*x)**2*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/((d + e*x)**3*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/((d + e*x)**4*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**4/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**3/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**2/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/((d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/((d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/((d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**2/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/((d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/((d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)/((d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**(7/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**(5/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**(3/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/sqrt(d + e*x)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(3/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(5/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(7/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/sqrt(d + e*x)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(3/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(5/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(7/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**(7/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/sqrt(d + e*x)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(3/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(5/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(A + B*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(7/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**5*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**4*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**3*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**2*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**7*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**6*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**5*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**4*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**9*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**8*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**7*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**6*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**5*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**4*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**4/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**3/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**2/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)**2*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)**3*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)**4*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)**5*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**4/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**3/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**2/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**5/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**4/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**3/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**2/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)**2*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)**3*(a**2 + 2*a*b*x + b**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**(7/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**(5/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**(3/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2)/(d + e*x)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(9/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(11/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(3/2)/(d + e*x)**(13/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**(5/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**(3/2)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(d + e*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(9/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(11/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(13/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(15/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(a**2 + 2*a*b*x + b**2*x**2)**(5/2)/(d + e*x)**(17/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**(7/2)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**(5/2)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*(d + e*x)**(3/2)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)*sqrt(d + e*x)/sqrt(a**2 + 2*a*b*x + b**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/(sqrt(d + e*x)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)**(3/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)**(5/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(a + b*x)/((d + e*x)**(7/2)*sqrt(a**2 + 2*a*b*x + b**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(f + g*x)/((d + e*x)**2*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(f + g*x)/((d + e*x)**3*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**2*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(5/2)*(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(3/2)*(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `sqrt(d + e*x)*(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(f + g*x)*sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(5/2)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(3/2)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `sqrt(d + e*x)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(5/2)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(3/2)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `sqrt(d + e*x)*(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(f + g*x)*(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(5/2)*(f + g*x)/sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(3/2)*(f + g*x)/sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `sqrt(d + e*x)*(f + g*x)/sqrt(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(9/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(7/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(5/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(3/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(13/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(11/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(9/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(7/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(d + e*x)**(5/2)*(f + g*x)/(-b*d*e - b*e**2*x + c*d**2 - c*e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(5 - x)/(3*x**2 + 5*x + 2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(5 - x)*(2*x + 3)**2/(3*x**2 + 5*x + 2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(5 - x)*(2*x + 3)/(3*x**2 + 5*x + 2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_3 | radicand-split | `(5 - x)/(3*x**2 + 5*x + 2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2*(d + e*x)/(d**2 - e**2*x**2)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**4*(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**3*(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2*(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x*(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2*(d + e*x)/(d**2 - e**2*x**2)**(9/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2*(d + e*x)/(d**2 - e**2*x**2)**(11/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**3*(d + e*x)**2/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2*(d + e*x)**2/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x*(d + e*x)**2/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**2/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2*(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x*(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `1/((d + e*x)*sqrt(d**2 - e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2/((d + e*x)*(d**2 - e**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x/((d + e*x)*(d**2 - e**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `1/((d + e*x)*(d**2 - e**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**4/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**3/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `1/((d + e*x)*(d**2 - e**2*x**2)**(5/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**3/((d + e*x)*(d**2 - e**2*x**2)**(7/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2/((d + e*x)*(d**2 - e**2*x**2)**(7/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `1/((a*x + 1)*sqrt(-a**2*x**2 + 1))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**3/((d + e*x)**2*(d**2 - e**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x/((d + e*x)**2*(d**2 - e**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `1/((d + e*x)**2*(d**2 - e**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `1/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x*sqrt(d**2 - e**2*x**2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(d**2 - e**2*x**2)/(d + e*x)**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2*sqrt(-a**2*x**2 + 1)/(-a*x + 1)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**3/((d + e*x)**4*(d**2 - e**2*x**2)**(7/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2/((d + e*x)**4*(d**2 - e**2*x**2)**(7/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x/((d + e*x)**4*(d**2 - e**2*x**2)**(7/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `1/((d + e*x)**4*(d**2 - e**2*x**2)**(7/2))` | `-173/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `1/((d + e*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x**2/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `x/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `1/((d + e*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**3*(f + g*x)**2/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**3*(f + g*x)/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**3/(d**2 - e**2*x**2)**(7/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(d + e*x)*(f + g*x)**3/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(d + e*x)*(f + g*x)**2/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(d + e*x)*(f + g*x)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(d + e*x)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)*(f + g*x)**3/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)*(f + g*x)**2/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)*(f + g*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(5/2)*(f + g*x)**3/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(5/2)*(f + g*x)**2/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(5/2)*(f + g*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(5/2)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(f + g*x)**4*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(f + g*x)**3*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(f + g*x)**2*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(f + g*x)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/sqrt(d + e*x)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(f + g*x)**4*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(f + g*x)**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(f + g*x)**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(f + g*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/(d + e*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(f + g*x)**4*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(f + g*x)**3*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(f + g*x)**2*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(f + g*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/(d + e*x)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(d + e*x)/((f + g*x)**(3/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(d + e*x)/((f + g*x)**(5/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(d + e*x)/((f + g*x)**(7/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(d + e*x)/((f + g*x)**(9/2)*sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2)))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)/(sqrt(f + g*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)/((f + g*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)/((f + g*x)**(5/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)/((f + g*x)**(7/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(5/2)*sqrt(f + g*x)/(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(5/2)/(sqrt(f + g*x)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(5/2)/((f + g*x)**(3/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(5/2)/((f + g*x)**(5/2)*(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x)**(5/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x)**(7/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))/(sqrt(d + e*x)*(f + g*x)**(9/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**(7/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**(9/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(3/2)/((d + e*x)**(3/2)*(f + g*x)**(11/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**(9/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**(11/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**(13/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))**(5/2)/((d + e*x)**(5/2)*(f + g*x)**(15/2))` | `-13/2` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)*(f + g*x)**4/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)*(f + g*x)**3/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)*(f + g*x)**2/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)*(f + g*x)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_4 | radicand-split | `(d + e*x)**(3/2)/sqrt(a*d*e + c*d*e*x**2 + x*(a*e**2 + c*d**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_6 | radicand-split | `(g + h*x)*sqrt(a + b*x + c*x**2)/(a*d + b*d*x + c*d*x**2)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_6 | radicand-split | `(2*x - 3)*(x**2 - 3*x)**(2/3)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_6 | radicand-split | `x*(2*x**2 - 9*x + 9)/(x**2 - 3*x)**(1/3)` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_9 | radicand-split | `sqrt(d**2 - e**2*x**2)*(A + B*x + C*x**2)/(d + e*x)**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_9 | radicand-split | `sqrt(d**2 - e**2*x**2)*(A + B*x + C*x**2)/(d + e*x)**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_9 | radicand-split | `(A + B*x + C*x**2)/((d + e*x)**3*sqrt(d**2 - e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_9 | radicand-split | `(A + B*x + C*x**2)/((d + e*x)**4*sqrt(d**2 - e**2*x**2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_1_9 | radicand-split | `(d + e*x + f*x**2)/((g + h*x)*(b*g*h + b*h**2*x - c*g**2 + c*h**2*x**2)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(b*x**2 + c*x**4)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(b*x**2 + c*x**4)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(b*x**2 + c*x**4)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(b*x**2 + c*x**4)/x**11` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(b*x**2 + c*x**4)/x**13` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**4*sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**2*sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(b*x**2 + c*x**4)**(3/2)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(b*x**2 + c*x**4)**(3/2)/x**11` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(b*x**2 + c*x**4)**(3/2)/x**13` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(b*x**2 + c*x**4)**(3/2)/x**15` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(b*x**2 + c*x**4)**(3/2)/x**17` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**6*(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**4*(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**2*(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(b*x**2 + c*x**4)**(3/2)/x**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**4/sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**2/sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**3/(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x/(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**6/(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**4/(b*x**2 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**5*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**3*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**3` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**5` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**7` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**9` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**11` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**4*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**2*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**2` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**4` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**6` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**8` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/x**10` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**9*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**7*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**3*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**3` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**5` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**7` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**9` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**11` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**13` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**15` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**17` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**8*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**6*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**4*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**2*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**2` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**4` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**6` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**8` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**10` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**12` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**14` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/x**16` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**13*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**11*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**9*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**7*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**5*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**3*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**3` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**5` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**7` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**9` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**11` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**13` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**15` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**17` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**19` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**21` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**23` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**25` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**12*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**10*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**8*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**6*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**4*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**2*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**2` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**4` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**6` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**8` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**10` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**12` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**14` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**16` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**18` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**20` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**22` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/x**24` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**5/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**3/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/(x*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/(x**3*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**4/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**2/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/(x**2*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/(x**4*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**7/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**5/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/(x*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/(x**3*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**4/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**2/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(-3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/(x**2*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/(x**4*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**11/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**9/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**7/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**5/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**3/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/(x*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/(x**3*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**6/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**4/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**2/(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(-5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/(x**2*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `1/(x**4*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(d*x)**(5/2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(d*x)**(3/2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(d*x)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/sqrt(d*x)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/(d*x)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/(d*x)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)/(d*x)**(7/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(d*x)**(5/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(d*x)**(3/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(d*x)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/sqrt(d*x)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/(d*x)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/(d*x)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)/(d*x)**(7/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(d*x)**(5/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(d*x)**(3/2)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `sqrt(d*x)*(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/sqrt(d*x)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/(d*x)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/(d*x)**(5/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `(a**2 + 2*a*b*x**2 + b**2*x**4)**(5/2)/(d*x)**(7/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**4/sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_2 | radicand-split | `x**2/sqrt(b*x**2 + c*x**4)` | `-333/64` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `x**2*(d + e*x**2)/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `x*(d + e*x**2)/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `(d + e*x**2)/sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `(d + e*x**2)/(x*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `(d + e*x**2)/(x**2*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `(d + e*x**2)/(x**3*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `x**2*(d + e*x**2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `x*(d + e*x**2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `(d + e*x**2)/(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `(d + e*x**2)/(x*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `(d + e*x**2)/(x**2*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `(d + e*x**2)/(x**3*(a**2 + 2*a*b*x**2 + b**2*x**4)**(3/2))` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_2_4 | radicand-split | `x*sqrt(c + d*x**2)*sqrt(a**2 + 2*a*b*x**2 + b**2*x**4)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a*x**3 + b*x**6)**(5/3)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a*x**3 + b*x**6)**(2/3)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a*x**3 + b*x**6)**(-2/3)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a*x**3 + b*x**6)**(-5/3)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**5*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**4*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**3*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**2*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**10` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)/x**11` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**9*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**8*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**7*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**6*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**5*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**4*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**3*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**2*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**10` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**11` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**12` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**13` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**14` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**15` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**16` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)/x**17` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**13*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**12*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**11*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**10*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**9*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**8*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**7*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**6*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**5*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**4*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**3*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**2*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**2` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**3` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**4` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**5` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**7` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**8` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**9` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**10` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**11` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**12` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**13` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**14` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**15` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**16` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**17` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**18` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**19` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**20` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**21` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**22` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**23` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**24` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)/x**25` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**4/sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**3/sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**2/sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x/sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/sqrt(a**2 + 2*a*b*x**3 + b**2*x**6)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/(x*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6))` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/(x**2*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6))` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/(x**3*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6))` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/(x**4*sqrt(a**2 + 2*a*b*x**3 + b**2*x**6))` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**4/(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**3/(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**2/(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x/(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(-3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/(x*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/(x**2*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/(x**3*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/(x**4*(a**2 + 2*a*b*x**3 + b**2*x**6)**(3/2))` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**6/(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**5/(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**4/(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**3/(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x**2/(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `x/(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2)` | `-173/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**3 + b**2*x**6)**(-5/2)` | `-173/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/(x*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2))` | `-173/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/(x**2*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2))` | `-173/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/(x**3*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2))` | `-173/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `1/(x**4*(a**2 + 2*a*b*x**3 + b**2*x**6)**(5/2))` | `-173/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b/x + b**2/x**2)` | `-87/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(7/2)` | `-87/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(5/2)` | `-87/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(3/2)` | `-87/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `sqrt(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))` | `-87/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(-5/2)` | `-87/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(-7/2)` | `-87/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(-9/2)` | `-87/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b*x**(1/3) + b**2*x**(2/3))**(-11/2)` | `-87/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b/x**(1/3) + b**2/x**(2/3))**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_3_2 | radicand-split | `(a**2 + 2*a*b/x**(1/5) + b**2/x**(2/5))**(5/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_4_2 | radicand-split | `x**4/(a*x**2 + b*x**3 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_2_4_2 | radicand-split | `x**3/(a*x**2 + b*x**3 + c*x**4)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | complex-only | `sqrt(a/x**7)/sqrt(x**5 + 1)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_3_2 | complex-only | `sqrt(a/x**17)/sqrt(x**5 + 1)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `x**2*sqrt(-a/x + b)/sqrt(a - b*x)` | `13981013/16777216` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `x*sqrt(-a/x + b)/sqrt(a - b*x)` | `13981013/16777216` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(-a/x + b)/sqrt(a - b*x)` | `13981013/16777216` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(-a/x + b)/(x*sqrt(a - b*x))` | `13981013/16777216` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(-a/x + b)/(x**2*sqrt(a - b*x))` | `13981013/16777216` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `x**2*sqrt(-a/x**2 + b)/sqrt(a - b*x**2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `x*sqrt(-a/x**2 + b)/sqrt(a - b*x**2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(-a/x**2 + b)/sqrt(a - b*x**2)` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(-a/x**2 + b)/(x*sqrt(a - b*x**2))` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(-a/x**2 + b)/(x**2*sqrt(a - b*x**2))` | `-10273905/16777216` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `(x**3 - 1)/(x**4 - 4*x)**(2/3)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `(2 - x**2)*(-x**3 + 6*x)**(1/4)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | complex-only | `(5*x**4 + 2)*sqrt(x**5 + 2*x)` | `-3/4 - 5*I/4` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `(3*x**2 + x)/sqrt(2*x**3 + x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(-1 + x**(-2))/(x*(x**2 - 1)**2)` | `1/4` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(-1 + x**(-2))/(x*(x**2 - 1)**3)` | `1/4` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `x*sqrt(1 + x**(-2))/(x**2 + 1)**2` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `1/(x*sqrt(1 + x**(-2))*(x**2 + 1))` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `x/(sqrt((1 - x)/(x + 1))*(x + 1))` | `-3/4` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `x/(sqrt(-1 + 2/(x + 1))*(x + 1))` | `-3/4` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(1 + 1/x)/(x + 1)**2` | `-3/4` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `x*(sqrt(1 - x**2) + 1)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `-3/(5*x + 4)**2 - (4*x + 5)/(sqrt(1 - x**2)*(5*x + 4)**2)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `-9*x**2 + x/sqrt(1 - 9*x**2) + 1` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(x + 1)/sqrt(1 - x**2)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(1 - x**2)/sqrt(x + 1)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt((x**2 - 1)**2/(x*(x**2 + 1)))/(x**2 + 1)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt((x**2 - 1)**2/(x**3 + x))/(x**2 + 1)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(2*x/(x**2 + 1) + 1)/(x**2 + 1)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `(x + 3)/(x**2 + 6*x)**(1/3)` | `-7` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `(x + 4)/(-x**2 + 6*x)**(3/2)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `(x - 1)/sqrt(-x**2 + 2*x)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | complex-only | `(1 - x**2)*sqrt(1/(2 - x**2))` | `-5/4 + I/3` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `1/((x + 1)**(2/3)*(x**2 - 1)**(2/3))` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `(1 - x**6)**(2/3) + (1 - x**6)**(2/3)/x**6` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `(2*x + 1)/sqrt(x**2 + x)` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `1/(x*sqrt(-x**2 + 6*x))` | `-333/64` |
| t 1 algebraic functions | t_1_3_2 | radicand-split | `sqrt(x**3 + x**2)` | `-333/64` |
| t 2 exponentials | t_2_3 | radicand-split | `sqrt(9 - exp(2*x))*exp(6*x)` | `-173/64` |
| t 4 trig functions | t_4_3_1_2 | radicand-split | `(I*a*tan(c + d*x) + a)**(3/2)*cos(c + d*x)` | `-333/64` |
| t 4 trig functions | t_4_3_1_2 | radicand-split | `(I*a*tan(c + d*x) + a)**(5/2)*cos(c + d*x)` | `-333/64` |
| t 4 trig functions | t_4_3_1_2 | radicand-split | `(I*a*tan(c + d*x) + a)**(5/2)*cos(c + d*x)**3` | `-333/64` |
| t 4 trig functions | t_4_3_1_2 | radicand-split | `(I*a*tan(c + d*x) + a)**(7/2)*cos(c + d*x)` | `-333/64` |
| t 4 trig functions | t_4_3_1_2 | radicand-split | `(I*a*tan(c + d*x) + a)**(7/2)*cos(c + d*x)**3` | `-333/64` |
| t 4 trig functions | t_4_3_1_2 | radicand-split | `(I*a*tan(c + d*x) + a)**(7/2)*cos(c + d*x)**5` | `-333/64` |
| t 4 trig functions | t_4_3_1_2 | radicand-split | `sqrt(e*cos(c + d*x))*sqrt(I*a*tan(c + d*x) + a)` | `-87/64` |
| t 4 trig functions | t_4_3_1_2 | radicand-split | `sqrt(I*a*tan(c + d*x) + a)/sqrt(e*cos(c + d*x))` | `-29/64` |
| t 4 trig functions | t_4_3_1_2 | radicand-split | `sqrt(e*cos(c + d*x))/sqrt(I*a*tan(c + d*x) + a)` | `-29/64` |
| t 4 trig functions | t_4_3_1_2 | radicand-split | `1/(sqrt(e*cos(c + d*x))*sqrt(I*a*tan(c + d*x) + a))` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(5/2)*sqrt(-I*c*tan(e + f*x) + c)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(3/2)*sqrt(-I*c*tan(e + f*x) + c)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `sqrt(I*a*tan(e + f*x) + a)*sqrt(-I*c*tan(e + f*x) + c)` | `23/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `sqrt(-I*c*tan(e + f*x) + c)/sqrt(I*a*tan(e + f*x) + a)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(5/2)*(-I*c*tan(e + f*x) + c)**(3/2)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(3/2)*(-I*c*tan(e + f*x) + c)**(3/2)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `sqrt(I*a*tan(e + f*x) + a)*(-I*c*tan(e + f*x) + c)**(3/2)` | `23/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(-I*c*tan(e + f*x) + c)**(3/2)/(I*a*tan(e + f*x) + a)**(3/2)` | `23/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(5/2)*(-I*c*tan(e + f*x) + c)**(5/2)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(3/2)*(-I*c*tan(e + f*x) + c)**(5/2)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `sqrt(I*a*tan(e + f*x) + a)*(-I*c*tan(e + f*x) + c)**(5/2)` | `23/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(-I*c*tan(e + f*x) + c)**(5/2)/(I*a*tan(e + f*x) + a)**(5/2)` | `-333/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(7/2)/sqrt(-I*c*tan(e + f*x) + c)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(5/2)/sqrt(-I*c*tan(e + f*x) + c)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(3/2)/sqrt(-I*c*tan(e + f*x) + c)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `sqrt(I*a*tan(e + f*x) + a)/sqrt(-I*c*tan(e + f*x) + c)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `1/(sqrt(I*a*tan(e + f*x) + a)*sqrt(-I*c*tan(e + f*x) + c))` | `23/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `1/((I*a*tan(e + f*x) + a)**(3/2)*sqrt(-I*c*tan(e + f*x) + c))` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `1/((I*a*tan(e + f*x) + a)**(5/2)*sqrt(-I*c*tan(e + f*x) + c))` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `1/((I*a*tan(e + f*x) + a)**(7/2)*sqrt(-I*c*tan(e + f*x) + c))` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(9/2)/(-I*c*tan(e + f*x) + c)**(3/2)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(7/2)/(-I*c*tan(e + f*x) + c)**(3/2)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(5/2)/(-I*c*tan(e + f*x) + c)**(3/2)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(3/2)/(-I*c*tan(e + f*x) + c)**(3/2)` | `23/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `sqrt(I*a*tan(e + f*x) + a)/(-I*c*tan(e + f*x) + c)**(3/2)` | `23/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `1/(sqrt(I*a*tan(e + f*x) + a)*(-I*c*tan(e + f*x) + c)**(3/2))` | `23/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `1/((I*a*tan(e + f*x) + a)**(3/2)*(-I*c*tan(e + f*x) + c)**(3/2))` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `1/((I*a*tan(e + f*x) + a)**(5/2)*(-I*c*tan(e + f*x) + c)**(3/2))` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `1/((I*a*tan(e + f*x) + a)**(7/2)*(-I*c*tan(e + f*x) + c)**(3/2))` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(11/2)/(-I*c*tan(e + f*x) + c)**(5/2)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(9/2)/(-I*c*tan(e + f*x) + c)**(5/2)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(7/2)/(-I*c*tan(e + f*x) + c)**(5/2)` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(5/2)/(-I*c*tan(e + f*x) + c)**(5/2)` | `-333/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `(I*a*tan(e + f*x) + a)**(3/2)/(-I*c*tan(e + f*x) + c)**(5/2)` | `23/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `sqrt(I*a*tan(e + f*x) + a)/(-I*c*tan(e + f*x) + c)**(5/2)` | `23/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `1/(sqrt(I*a*tan(e + f*x) + a)*(-I*c*tan(e + f*x) + c)**(5/2))` | `23/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `1/((I*a*tan(e + f*x) + a)**(3/2)*(-I*c*tan(e + f*x) + c)**(5/2))` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `1/((I*a*tan(e + f*x) + a)**(5/2)*(-I*c*tan(e + f*x) + c)**(5/2))` | `-87/64` |
| t 4 trig functions | t_4_3_2_1 | radicand-split | `1/((I*a*tan(e + f*x) + a)**(7/2)*(-I*c*tan(e + f*x) + c)**(5/2))` | `-87/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*sqrt(I*a*tan(e + f*x) + a)*(-I*c*tan(e + f*x) + c)**(7/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*sqrt(I*a*tan(e + f*x) + a)*(-I*c*tan(e + f*x) + c)**(5/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*sqrt(I*a*tan(e + f*x) + a)*(-I*c*tan(e + f*x) + c)**(3/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*sqrt(I*a*tan(e + f*x) + a)*sqrt(-I*c*tan(e + f*x) + c)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*sqrt(I*a*tan(e + f*x) + a)/sqrt(-I*c*tan(e + f*x) + c)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*sqrt(I*a*tan(e + f*x) + a)/(-I*c*tan(e + f*x) + c)**(3/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*sqrt(I*a*tan(e + f*x) + a)/(-I*c*tan(e + f*x) + c)**(5/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*sqrt(I*a*tan(e + f*x) + a)/(-I*c*tan(e + f*x) + c)**(7/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(3/2)*(-I*c*tan(e + f*x) + c)**(7/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(3/2)*(-I*c*tan(e + f*x) + c)**(5/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(3/2)*(-I*c*tan(e + f*x) + c)**(3/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(3/2)*sqrt(-I*c*tan(e + f*x) + c)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(3/2)/sqrt(-I*c*tan(e + f*x) + c)` | `-87/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(3/2)/(-I*c*tan(e + f*x) + c)**(3/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(3/2)/(-I*c*tan(e + f*x) + c)**(5/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(3/2)/(-I*c*tan(e + f*x) + c)**(7/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(3/2)/(-I*c*tan(e + f*x) + c)**(9/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(3/2)/(-I*c*tan(e + f*x) + c)**(11/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(5/2)*(-I*c*tan(e + f*x) + c)**(5/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(5/2)*(-I*c*tan(e + f*x) + c)**(3/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(5/2)*sqrt(-I*c*tan(e + f*x) + c)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(5/2)/sqrt(-I*c*tan(e + f*x) + c)` | `-87/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(5/2)/(-I*c*tan(e + f*x) + c)**(3/2)` | `-87/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(5/2)/(-I*c*tan(e + f*x) + c)**(5/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(5/2)/(-I*c*tan(e + f*x) + c)**(7/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(5/2)/(-I*c*tan(e + f*x) + c)**(9/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(7/2)*sqrt(-I*c*tan(e + f*x) + c)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(7/2)/sqrt(-I*c*tan(e + f*x) + c)` | `-87/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(7/2)/(-I*c*tan(e + f*x) + c)**(3/2)` | `-87/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(7/2)/(-I*c*tan(e + f*x) + c)**(5/2)` | `-87/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(7/2)/(-I*c*tan(e + f*x) + c)**(7/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))*(I*a*tan(e + f*x) + a)**(7/2)/(-I*c*tan(e + f*x) + c)**(9/2)` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))/(sqrt(I*a*tan(e + f*x) + a)*sqrt(-I*c*tan(e + f*x) + c))` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))/(sqrt(I*a*tan(e + f*x) + a)*(-I*c*tan(e + f*x) + c)**(3/2))` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))/(sqrt(I*a*tan(e + f*x) + a)*(-I*c*tan(e + f*x) + c)**(5/2))` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))/((I*a*tan(e + f*x) + a)**(3/2)*sqrt(-I*c*tan(e + f*x) + c))` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))/((I*a*tan(e + f*x) + a)**(3/2)*(-I*c*tan(e + f*x) + c)**(3/2))` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))/((I*a*tan(e + f*x) + a)**(3/2)*(-I*c*tan(e + f*x) + c)**(5/2))` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))/((I*a*tan(e + f*x) + a)**(5/2)*sqrt(-I*c*tan(e + f*x) + c))` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))/((I*a*tan(e + f*x) + a)**(5/2)*(-I*c*tan(e + f*x) + c)**(3/2))` | `-333/64` |
| t 4 trig functions | t_4_3_3_1 | radicand-split | `(A + B*tan(e + f*x))/((I*a*tan(e + f*x) + a)**(5/2)*(-I*c*tan(e + f*x) + c)**(5/2))` | `-333/64` |
| t 6 hyperbolic functions | t_6_1_1 | radicand-split | `x**4*sqrt(I*a*sinh(e + f*x) + a)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_1 | radicand-split | `x**3*sqrt(I*a*sinh(e + f*x) + a)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_1 | radicand-split | `x**2*sqrt(I*a*sinh(e + f*x) + a)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_1 | radicand-split | `x*sqrt(I*a*sinh(e + f*x) + a)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_1 | radicand-split | `x**3*(I*a*sinh(e + f*x) + a)**(3/2)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_1 | radicand-split | `x**2*(I*a*sinh(e + f*x) + a)**(3/2)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_1 | radicand-split | `x*(I*a*sinh(e + f*x) + a)**(3/2)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_1 | radicand-split | `x**3*(I*a*sinh(c + d*x) + a)**(5/2)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_1 | radicand-split | `x**2*(I*a*sinh(c + d*x) + a)**(5/2)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_1 | radicand-split | `x*(I*a*sinh(c + d*x) + a)**(5/2)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_5 | radicand-split | `sinh(x)/sqrt(I*a*sinh(x) + a)` | `23/64` |
| t 6 hyperbolic functions | t_6_1_5 | radicand-split | `sinh(x)/sqrt(-I*a*sinh(x) + a)` | `-333/64` |
| t 6 hyperbolic functions | t_6_1_5 | radicand-split | `(I*a*sinh(c + d*x) + a)**(5/2)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_5 | radicand-split | `(I*a*sinh(c + d*x) + a)**(3/2)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_5 | radicand-split | `sqrt(I*a*sinh(c + d*x) + a)` | `-79/64 + I/3` |
| t 6 hyperbolic functions | t_6_1_5 | radicand-split | `(A + B*sinh(x))*(I*a*sinh(x) + a)**(3/2)` | `-333/64` |
| t 6 hyperbolic functions | t_6_1_5 | radicand-split | `(A + B*sinh(x))*sqrt(I*a*sinh(x) + a)` | `23/64` |
| t 6 hyperbolic functions | t_6_1_5 | radicand-split | `(A + B*sinh(x))/sqrt(I*a*sinh(x) + a)` | `23/64` |
