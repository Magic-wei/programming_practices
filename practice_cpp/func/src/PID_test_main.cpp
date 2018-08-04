#include <iostream>

// intermediate variables
double delta0=0,delta1=0,delta2=0,ctrl_last=0;

// const variables
const double u_max = 2;
const double u_min = -4;

double IncrementalPidCalcu(double measured_value, double Desire_value) {
    // set pid params
    double kp=1.0,ki=0.05,kd=0.1;
    // init
    double U=0;
    double delta_U=0;
    double U_upper=u_max;
    double U_lower=u_min;
    // calculate deviations
    delta0=Desire_value-measured_value;
    // calculate proportion, integral and differential compensation values
    double u_p = kp*(delta0-delta1);
    double u_i = ki*delta0;
    double u_d = kd*(delta0-2*delta1+delta2);
    // get the incremental value - put together all three parts
    delta_U= u_p + u_i + u_d;
    std::cout<<"u_p="<<u_p<<",u_i="<<u_i<<",u_d="<<u_d<<",";
    std::cout<<"delta0="<<delta0<<",delta1="<<delta1<<",delta2="<<delta2<<",delta_U="<<delta_U<<std::endl;
    // calculate final compensation output
    U = delta_U+ctrl_last;
    if(U > U_upper){
        U = U_upper;
    }
    else if(U < U_lower){
        U = U_lower;
    }

    // record historical information - last two deviations and last output
    delta2=delta1;
    delta1=delta0;
    ctrl_last=U;

    return U;
}

double update_acc(double &measured_value, double incremental_value){
    double acc_open = 0.1;
    double coeffi = 0.01;
    measured_value += coeffi*(acc_open + incremental_value);
}


int main() {
    std::cout << "pid example start ...!\n";
    int num_max = 10;
    double measured_value = 0;
    double desired_value = 0.5;
    double delta_a = 0;
    for (int i = 0; i < num_max; ++i) {
        delta_a = IncrementalPidCalcu(measured_value, desired_value);
        update_acc(measured_value, delta_a);
        printf("the %d trial, incremental acceleration is %lf \n",i+1,delta_a);
    }
    return 0;
}
