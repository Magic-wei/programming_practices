//
// Created by wangwei on 18-3-23.
//

#include "eigen3/Eigen/Dense"
#include <vector>
#include "stdio.h"
#include "iostream"
#include <math.h>

using namespace std;
using namespace Eigen;

// declaration
Eigen::VectorXd polyfit(const Eigen::VectorXd& xvals, const Eigen::VectorXd& yvals, int order);
void test_Eigen();

int main(){
    std::vector<double> a = {1,2};
    cout<<a[0]<<endl;
    test_Eigen();
    return 0;
}

Eigen::VectorXd polyfit(const Eigen::VectorXd& xvals, const Eigen::VectorXd& yvals, int order) {
    assert(xvals.size() == yvals.size());
    assert(order >= 1 && order <= xvals.size() - 1);
    Eigen::MatrixXd A(xvals.size(), order + 1);

    for (int i = 0; i < xvals.size(); ++i) {
        A(i, 0) = 1.0;
    }

    for (int j = 0; j < xvals.size(); ++j) {
        for (int i = 0; i < order; i++) {
            A(j, i + 1) = A(j, i) * xvals(j);
        }
    }

    auto Q = A.householderQr();
//    cout<<"Q is"<<Q.matrixQR()<<endl;
    auto result = Q.solve(yvals);
    return result;
}

void test_Eigen(){
    Eigen::MatrixXd mat(3,2);
    Eigen::Matrix2d a;
    a << 1,2,3,4;
    mat<<1,2,3,4,5,6;
    cout<<a<<endl;
    cout<<mat<<endl;

    Eigen::VectorXd wayPtPolynomialCoeffs;
    Eigen::VectorXd xvals(4), yvals(4);
//    xvals.setRandom();
//    yvals.setRandom();
    xvals<<1,1,1,1;
    yvals<<1,1,1,1;
    Eigen::VectorXd LocalPathx(13), LocalPathy(13);
    LocalPathx << 0.02, 0.72, 1.71, 2.22, 2.80, 3.65, 4.54, 5.45, 6.36, 7.27, 8.20, 9.20, 9.98;
    LocalPathy << 0.28, 0.27, 0.27, 0.26, 0.25, 0.29, 0.38, 0.41, 0.46, 0.56,0.63, 0.69, 0.75;

    Eigen::MatrixXd tmp_m(15,3);
    tmp_m <<
          0,-0.27, 2.68,
            1, -0.25, 2.86,
            2, -0.24, 2.94,
            3, -0.23, 3.03,
            4, -0.21, 3.21,
            5, -0.31, 3.31,
            6, -0.29, 3.48,
            7, -0.28, 3.57,
            8, -0.26, 3.74,
            9, -0.24, 3.92,
            10, -0.23, 4.01,
            11, -0.32, 4.19,
            12, -0.30, 4.37,
            13, -0.28, 4.54,
            14, -0.37, 4.73;
//    std::cout<<tmp<<std::endl;
    Eigen::VectorXd LocalPathx1 = tmp_m.col(1);
    Eigen::VectorXd LocalPathy1 = tmp_m.col(2);
    Eigen::VectorXd num(tmp_m.rows());
    for (int i = 0; i < tmp_m.rows(); ++i) {
        num[i] = tmp_m(i,0);
    }
    std::cout<<num<<std::endl;
    std::cout<<LocalPathx1<<std::endl;
    std::cout<<LocalPathy1<<std::endl;
    wayPtPolynomialCoeffs = polyfit(LocalPathx1,LocalPathy1,3);
    cout<<"wayPtPolynomialCoeffs is \n"<<wayPtPolynomialCoeffs<<endl;
}
