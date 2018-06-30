#include <iostream>

namespace test{

    int double2int(double val){
        return int(val);
    }
}

int main() {
    double a_double = 2.5;
    const int a_int = test::double2int(a_double);
    std::cout << "Hello, World! Here is int " << a_int << " from double " << a_double << std::endl;
    return 0;
}
