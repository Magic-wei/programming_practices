//
// Created by wangwei on 18-8-4.
//

#ifndef FUNC_TEST_HELLO_WORLD_H
#define FUNC_TEST_HELLO_WORLD_H


class hello_world {
public:
    hello_world(); // 成员函数
    ~hello_world();
    void sayhello();
    int getCount();
private:
    int count; // 成员变量
};


#endif //FUNC_TEST_HELLO_WORLD_H
