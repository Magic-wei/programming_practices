## Math in Python

- [SciPy](https://docs.scipy.org/doc/) 
  - [x] non-constrained and constrained optimization: scipy.optimize.minimize()
  - [x] 曲线拟合 scipy.optimize.curve_fit()
  - [x] 最小二乘 scipy.optimize.least_squares(), 线性最小二乘 scipy.optimize.lsq_linear()
- [SymPy](https://www.sympy.org/en/index.html)
  - [x] pretty print: pprint(...) function
  - [x] 变量值代入 subs() 和 表达式估算 evalf()
  - [x] 表达式简化 simplify(), powsimp()，expand(), factor(), cancel()
  - [x] 判断两式相等 a.equals(b) OR simplify(a-b) == 0
  - [x] SymPy整数类型与Python int类型的使用区别 S(1)/3
  - [x] 有效数字 Float(100, 4), S(0.25).n(10)，不同有效数字之和会有误差
  - [x] sympy.abc 包含了内置常用变量的声明，可以import，省去自定义
  - [x] 特殊表达式：factorial(n) means n! 和 binomial(n,k) 二项式系数，组合
  - [x] 微积分：直接出结果 diff(), integrate(), 先得到表达式Derivative(), Integral()，用.doit()得到最终结果。
  - [x] 极限：limit(f(x), x, x0)
  - [x] 级数：.series()
  - [x] 方程求解：solveset(), dsolve()
  - [x] 矩阵：Matrix([[...],[...]]), 特征值，特征向量，特征分解
  - [x] plotting of functions, find the intersection point
  - [ ] 矩阵符号运算

* CVXPY
  - [x] constraints definition
  - [x] variables definition
  - [x] parameters definition
  - [x] problem setting
  - [x] parallel solving
  - [ ] practices on real problems