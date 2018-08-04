//
// Created by wangwei on 18-6-27.
//
#include <time.h>
#include <sys/time.h>
#include <iostream>
#include "math.h"
#include <vector>

using namespace std;

double getCurrentTime(void)
{
    struct timeval t;
    gettimeofday(&t,NULL);
    return (double) t.tv_sec + t.tv_usec/1000000.0;
}

double getPreviewHorizon(double PGC){
    double w = 3;
    double preview_horizon = round( 10.0 + 10 * exp(-w * PGC) ) / 100;
    return preview_horizon;
}

int main() {

    // Calculate time cost of some codes.
    double time_in = getCurrentTime();
    cout<<"time_in: "<<time_in<<"\n";

    // test codes
    std::vector<double> x,y;
    int number = 1000;
    double s = 0;
    for(int i=0;i<number;i++){
        x.push_back( i * 0.5 );
        y.push_back( sin(i) );
        double dt = getPreviewHorizon(x.at(i));
        s += sqrt( pow(x.at(i),2) + pow(x.at(i),2) );
        cout<<x.at(i)<<" "<<dt<<" "<<s<<"\n";
    }

    // end of test codes

    double time_out = getCurrentTime();
    cout<<"time_out: "<<time_out<<"\n";

    double cost = time_out - time_in; // here, we can get the final time cost, in unit second.
    cout<<"time cost: "<<cost<<"\n";

    return 0;
}
