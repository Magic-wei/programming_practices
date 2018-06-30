//
// Created by wangwei on 18-6-28.
//
#include <cppad/cppad.hpp>

using namespace std;
using CppAD::AD;

int main() {
    AD<double> x=1.0;
    double tmp;
    tmp = Value(x);
    cout<<tmp<<endl;
    return 0;
}
