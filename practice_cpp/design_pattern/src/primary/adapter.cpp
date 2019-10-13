//
// Created by wangwei on 2019/10/13.
//

#include <iostream>

using namespace std;

class Target {
public:
    virtual ~Target() = 0;
    virtual void request() = 0;
}; // class Target

class Adaptee{
public:
    void specificRequest(){
        cout << "Specific request from adaptee." << endl;
    }
}; // class Adaptee

class Adapter : public Target {
public:
    Adapter() : adaptee() {}
    ~Adapter() override {
        delete adaptee;
    }

    void request() override{
        adaptee->specificRequest();
    }
private:
    Adaptee *adaptee;
}; // class Adapter

int main(){
    Target *target = new Adapter();
    target->request();
    delete target;

    return 0;
}