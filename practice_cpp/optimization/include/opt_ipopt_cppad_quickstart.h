//
// Created by wangwei on 19-3-22.
//

#ifndef OPTIMIZATION_OPT_IPOPT_CPPAD_H
#define OPTIMIZATION_OPT_IPOPT_CPPAD_H

/* minimize f(x) = x1 * x2 + x1^2 + x3^2
 * subject to: x1 = x2 * x3
 *             -5 < x2, x3 < 10
 *             x1 * (x2 + x3) < 10
 * 
 * fg[0] = f(x), fg[1:n+1] = g(x)[0:n];
 *
 * set(FG_eval):
 *      x = [x1, x2, x3]
 *      xl = [-10e9, -5.0, -5.0]
 *      xu = [10e9, 10.0, 10.0]
 *      g(x) = [x1 - x2 * x3, x1 * (x2 + x3)]
 *      gl = [0, -10e9]
 *      gu = [0, 10]
 * or(FG_eval2):
 *      x = [x1, x2, x3]
 *      xl = [-10e9, -10e9, -10e9]
 *      xu = [10e9, 10e9, 10e9]
 *      g(x) = [x1 - x2 * x3, x1 * (x2 + x3), x2, x3]
 *      gl = [0, -10e9, -5, -5]
 *      gu = [0, 10, -10, -10]
 */

# include <cppad/ipopt/solve.hpp>

namespace cppad_ipopt_quickstart {
using CppAD::AD;

class FG_eval {
public:
    typedef CPPAD_TESTVECTOR(AD<double>) ADvector;

    void operator()(ADvector &fg, const ADvector &x) {
        std::cout << "size of fg: " << fg.size() << "\n";
        std::cout << "size of x: " << x.size() << "\n";
        // Fortran style indexing
        AD<double> x1 = x[0];
        AD<double> x2 = x[1];
        AD<double> x3 = x[2];
        // f(x)
        fg[0] = x1 * x2 + pow(x1, 2) + pow(x3, 2);
        // g(x)[0]
        fg[1] = x1 - x2 * x3;
        // g(x)[1]
        fg[2] = x1 * (x2 + x3);
        //
        return;
    }
};

class FG_eval2 {
public:
    typedef CPPAD_TESTVECTOR(AD<double>) ADvector;

    void operator()(ADvector &fg, const ADvector &x) {
        std::cout << "size of fg: " << fg << "\n";
        std::cout << "size of x: " << x << "\n";
        // Fortran style indexing
        AD<double> x1 = x[0];
        AD<double> x2 = x[1];
        AD<double> x3 = x[2];
        // f(x)
        fg[0] = x1 * x2 + pow(x1, 2) + pow(x3, 2);
        // g(x)[0]
        fg[1] = x1 - x2 * x3;
        // g(x)[1]
        fg[2] = x1 * (x2 + x3);
        // g(x)[2]
        fg[3] = x2;
        // g(x)[3]
        fg[4] = x3;
        return;
    }
};

bool solve(void) {
    bool ok = true;
    size_t i;
    typedef CPPAD_TESTVECTOR(double) Dvector;

    /* setting #1 */
    // number of independent variables (domain dimension for f and g)
    size_t nx = 3;
    // number of constraints (range dimension for g)
    size_t ng = 2;
    // initial value of the independent variables
    Dvector xi(nx);
    xi[0] = 0.0; xi[1] = 0.0; xi[2] = 0.0;
    // lower and upper limits for x
    Dvector xl(nx), xu(nx);
    xl[0] = -10e9; xl[1] = -5.0; xl[2] = -5.0;
    xu[0] = 10e9; xu[1] = 10.0; xu[2] = 10.0;
    // lower and upper limits for g
    Dvector gl(ng), gu(ng);
    gl[0] = 0.0; gl[1] = -10e9;
    gu[0] = 0.0; gu[1] = 10.0;

    // object that computes objective and constraints
    FG_eval fg_eval;

    /* setting #2 */
    // number of independent variables (domain dimension for f and g)
    size_t nx2 = 3;
    // number of constraints (range dimension for g)
    size_t ng2 = 4;
    // initial value of the independent variables
    Dvector xi2(nx);
    xi[0] = 0.0; xi[1] = 0.0; xi[2] = 0.0;
    // lower and upper limits for x
    Dvector xl2(nx), xu2(nx);
    for(int i = 0; i < nx2; ++i){
        xl2[i] = -10e9;
        xu2[i] = 10e9;
    }
    // lower and upper limits for g
    Dvector gl2(ng2), gu2(ng2);
    gl2[0] = 0.0; gl2[1] = -10e9; gl2[2] = -5.0; gl2[3] = -5.0;
    gu2[0] = 0.0; gu2[1] = 10.0; gu2[2] = 10.0; gu2[3] = 10.0;
    
    // object that computes objective and constraints
    FG_eval2 fg_eval2;

    // options
    std::string options;
    // turn off any printing
    options += "Integer print_level  0\n";
    options += "String  sb           yes\n";
    // maximum number of iterations
//    options += "Integer max_iter     10\n";
    // NOTE: Setting sparse to true allows the solver to take advantage
    // of sparse routines, this makes the computation MUCH FASTER. If you
    // can uncomment 1 of these and see if it makes a difference or not but
    // if you uncomment both the computation time should go up in orders of
    // magnitude.
    options += "Sparse  true        forward\n";
    options += "Sparse  true        reverse\n";
    // approximate accuracy in first order necessary conditions;
    // see Mathematical Programming, Volume 106, Number 1,
    // Pages 25-57, Equation (6)
    options += "Numeric tol          1e-6\n";
    // derivative testing
    options += "String  derivative_test            second-order\n";
    // maximum amount of random pertubation; e.g.,
    // when evaluation finite diff
    options += "Numeric point_perturbation_radius  0.\n";
    // NOTE: Currently the solver has a maximum time limit of 0.5 seconds.
    // Change this as you see fit.
    options += "Numeric max_cpu_time          0.1\n";

    // place to return solution
    CppAD::ipopt::solve_result<Dvector> solution;
    CppAD::ipopt::solve_result<Dvector> solution2;

    // solve the problem
    CppAD::ipopt::solve<Dvector, FG_eval>(
            options, xi, xl, xu, gl, gu, fg_eval, solution
    );
    CppAD::ipopt::solve<Dvector, FG_eval2>(
            options, xi2, xl2, xu2, gl2, gu2, fg_eval2, solution2
    );

    //
    // Check some of the solution values
    //
    ok &= solution.status == CppAD::ipopt::solve_result<Dvector>::success;
    ok &= solution2.status == CppAD::ipopt::solve_result<Dvector>::success;
    //
    std::cout << "solution1: " << solution.status << " " << solution.x << " f(x): " << solution.obj_value << " g(x): " << solution.g << "\n";
    std::cout << "solution1: " << solution2.status << " " << solution2.x << " f(x): " << solution2.obj_value << " g(x): " << solution2.g << "\n";
    double rel_tol = 1e-6;  // relative tolerance
    double abs_tol = 1e-6;  // absolute tolerance
    for (i = 0; i < nx; i++) {
        ok &= CppAD::NearEqual(
                solution.x[i], solution2.x[i], rel_tol, abs_tol
        );
    }
    ok &= CppAD::NearEqual(
            solution.obj_value, solution2.obj_value, rel_tol, abs_tol
    );
    return ok;
}
}
#endif //OPTIMIZATION_OPT_IPOPT_CPPAD_H
