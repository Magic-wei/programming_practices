//
// Created by wangwei on 2019/11/23.
//

#include <iostream>

using namespace std;

class Base{
private:
    double limit_;
    double cmd_;
public:
    Base(double limit){
        if(limit > 1.0){
            throw std::invalid_argument("limit should be between 0.0 and 1.0");
        }
        limit_ = limit;
        printf("(Base) Get limit: %f\n", limit_);
    }

    double getCommand(){
        return cmd_;
    }

    void setCommand(double command){
        cmd_ = command;
    }

    double getLimit(){
        return limit_;
    }

    void setLimit(double limit){
        limit_ = limit;
    }
};

class Derived : public Base{
public:
    Derived(double command, double limit): Base(limit){
        setCommand(command);
        printf("(Derived) Set command: %f, limit: %f\n", getCommand(), getLimit());
    }
};

int main(){
    Base b(1.0);

    Derived d(2.0, 1.9);

    printf("(main) Get Base current command: %f\n", b.getLimit());
    printf("(main) Get Derived current command: %f\n", d.getCommand());
    printf("(main) Get Derived current limit: %f\n", d.getLimit());

    return 0;
}