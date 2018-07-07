//
// Created by wangwei on 18-7-4.
//

#include "template/template_test.h"

#include <iostream>
#include <vector>

using namespace std;

#define maxsize 20

int main() {
    // test for single template function
    auto a_int = my_sum<int>(1,3);
    cout<<"a_int is "<<a_int<<endl;

    vector<int> vector1 = {1,2,3}, vector2 = {4,7,10};

    auto tmp_auto = my_sum(vector1, vector2);
    for (int i = 0; i < tmp_auto.size(); i++) {
        printf("tmp_auto[%d]:%d\n", i, tmp_auto[i]);
    }

    vector<int> v1 = {1,2}, v2 = {4,3};
    my_swap(v1,v2);
    for (int i = 0; i < v1.size(); i++) {
        printf("v1[%d]:%d\n", i, v1[i]);
    }
    for (int i = 0; i < v2.size(); i++) {
        printf("v2[%d]:%d\n", i, v2[i]);
    }

    vector<double> a = {1.0,2.0}, b = {4.0,3.0};
    my_swap<double>(a,b);
    for (int i = 0; i < a.size(); i++) {
        printf("a[%d]:%f\n", i, a[i]);
    }
    for (int i = 0; i < b.size(); i++) {
        printf("b[%d]:%f\n", i, b[i]);
    }

    // test for template class
    My_Stack<int, maxsize> intStack;
    for (int i = 0; i < maxsize; ++i) {
        intStack.push(i);
    }

    while (!intStack.isEmpty()) {
        printf("num:%d\n", intStack.pop());
    }


    return 0;
}