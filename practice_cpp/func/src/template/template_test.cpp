//
// Created by wangwei on 18-7-7.
//

#include "template_test.h"

template<typename  T> T my_sum(T a, T b){
    return a + b;
}

template<> vector<int> my_sum(vector<int> a, vector<int> b){
    vector<int> result;
    for (int i = 0; i < a.size(); ++i) {
        result.push_back(a.at(i) + b.at(i));
    }
    return result;
}

template<typename U> void my_swap(U& a, U& b){
    U tmp_U;
    tmp_U = a;
    a = b;
    b = tmp_U;
}

template<> void my_swap(std::vector<int>& a, std::vector<int>& b) {
    a.swap(b);
}

template<class V> void my_swap(std::vector<V>& a, std::vector<V>& b) {
    a.swap(b);
}

// 模板类
template <class T,int maxsize> My_Stack<T, maxsize>::My_Stack(){
    m_maxSize = maxsize;
    m_size = 0;
    m_pT = new T[m_maxSize];
}
template <class T,int maxsize> My_Stack<T, maxsize>::~My_Stack() {
    delete [] m_pT ;
}

template <class T,int maxsize> void My_Stack<T, maxsize>::push(T t) {
    m_size++;
    m_pT[m_size - 1] = t;

}
template <class T,int maxsize> T My_Stack<T, maxsize>::pop() {
    T t = m_pT[m_size - 1];
    m_size--;
    return t;
}
template <class T,int maxsize> bool My_Stack<T, maxsize>::isEmpty() {
    return m_size == 0;
}

