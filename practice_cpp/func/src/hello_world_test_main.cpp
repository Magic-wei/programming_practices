//
// Created by wangwei on 18-8-4.
//

#include "hello_world/hello_world.h"

#include <iostream>
#include <cmath> // for complex calculation

int main(){
    hello_world test;
    test.sayhello(); // maybe we should say 100 times!
    for (int i = 0; i < 100; ++i) {
        test.sayhello();
    }
    int count = test.getCount(); // let's see how many times we use sayhello() function
    std::cout << "count before set zero: " << count << std::endl;
    test.setCountZero();
    count = test.getCount();
    std::cout << "count after set zero: " << count << std::endl;

    return 0;
}