//
// Created by wangwei on 18-7-7.
//

#ifndef FUNC_TEST_TAMPLATE_TEST_H
#define FUNC_TEST_TAMPLATE_TEST_H

#include <vector>

using std::vector;

template <typename T> T my_sum(T a, T b);
template <typename U> void my_swap(U&a, U&b);

template <class T1,int maxsize = 100>  class My_Stack { // 模板栈
public:
    My_Stack();
    ~My_Stack();
    void push(T1 t);
    T1 pop();
    bool isEmpty();
private:
    T1 *m_pT;
    int m_maxSize;
    int m_size;
};

// 对于存在模板的定义，如果要将声明和实现分别放在.h和.cpp文件中，要在头文件中包含对应的实现文件。
#include "template_test.cpp"

#endif //FUNC_TEST_TAMPLATE_TEST_H
