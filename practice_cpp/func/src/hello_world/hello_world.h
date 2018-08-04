//
// Created by wangwei on 18-8-4.
//

#ifndef FUNC_TEST_HELLO_WORLD_H
#define FUNC_TEST_HELLO_WORLD_H


class hello_world {
public:
    hello_world(); // member function
    ~hello_world();
    void sayhello();
    int getCount();
private:
    int count; // member variable
};


#endif //FUNC_TEST_HELLO_WORLD_H
