#include <iostream>
#include "lib2.hpp"

example_project::Lib2::Lib2() :
        display_(false) {
    std::cout << "Constructor of lib2." << std::endl;
}


void example_project::Lib2::sayHelloFromLib2() {
    std::cout << "Hello from lib2." << std::endl;
}

