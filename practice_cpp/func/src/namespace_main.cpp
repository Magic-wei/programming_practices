#include <iostream>

namespace initial_ = std; // declare alternative namespace

using initial_::cout; // declare simplified use, we can directly use cout and endl in the following codes.
using std::endl;

namespace test{ // namespace declaration is better used in header files, here is just a demo.

    int double2int(double val){
        return int(val);
    }
} // namespace test

namespace test2 {

    void display(){
        cout<<"Hello world from namespace test2."<<endl;
    }
} // namespace test2

using test2::display; // here we declare an alternative using style

int main() {
    double a_double = 2.5;
    const int a_int = test::double2int(a_double);

    // Since we have declared above, display means test2::display here.
    display();
    // The same using.
    cout << "Hello, World! Here is int " << a_int << " from double " << a_double << endl;
    // But you can still use the style initial_::cout or std::cout.
    initial_::cout<<"But you can still use the style std::cout"<<std::endl;
    return 0;
} // main

