#include <iostream>

double delta0=0,delta1=0,delta2=0,ctrl_last=0;

#define u_max 2
#define u_min -4
#define slope_gas 1

double PIDforacc(double measured_value, double Desire_value) {
    double kp=1.0,ki=0.05,kd=0.1;
    double U=0;
    double delta_U=0;
    double U_upper=u_max;
    double U_lower=u_min;
    delta0=Desire_value-measured_value;
    double u_p = kp*(delta0-delta1);
    double u_i = ki*delta0;
    double u_d = kd*(delta0-2*delta1+delta2);
    delta_U= u_p + u_i + u_d;
    std::cout<<"u_p="<<u_p<<",u_i="<<u_i<<",u_d="<<u_d<<",";
    std::cout<<"delta0="<<delta0<<",delta1="<<delta1<<",delta2="<<delta2<<",delta_U="<<delta_U<<std::endl;
    U=delta_U+ctrl_last;

    if(U > U_upper)
        U = U_upper;
    else if(U < U_lower)
        U = U_lower;

    delta2=delta1;
    delta1=delta0;
    ctrl_last=U;
    return U;
}

double updata_acc(double & measured_value, double cremental_value){
    double acc_open = 0.1;
    double coeffi = 0.01;
    measured_value = 0;//measured_value + coeffi*(acc_open + cremental_value);
}

enum shift{Error=0,N,D,R};
int main() {
    std::cout << "Hello, World!" << std::endl;
    std::cout << D << std::endl;
    int num_max = 10;
    double measured_value = 0;
    double desired_value = 0.5;
    double delta_a = 0;
    for (int i = 0; i < num_max; ++i) {
        delta_a = PIDforacc(measured_value, desired_value);
        updata_acc(measured_value, delta_a);
        printf("the %d trial, incremental acceleration is %lf \n",i+1,delta_a);
    }
    return 0;
}
