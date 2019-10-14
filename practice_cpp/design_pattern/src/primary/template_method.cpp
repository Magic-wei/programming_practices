//
// Created by wangwei on 2019/10/13.
//

#include <iostream>

using namespace std;

class AbstractClass{
public:
    virtual ~AbstractClass() {}

    void templateMethod(){

        primitiveOperation1();

        primitiveOperation2();
    }

    virtual void primitiveOperation1() = 0;
    virtual void primitiveOperation2() = 0;
}; // class AbstractClass

class ConcreteClass : public AbstractClass {
public:
    ~ConcreteClass() {}

    void primitiveOperation1() override {
        cout << "Primitive operation 1." << endl;
    }

    void primitiveOperation2() override {
        cout << "Primitive operation 2." << endl;
    }
}; // class ConcreteClass

int main(){
    AbstractClass *p = new ConcreteClass();
    p->templateMethod();

    delete p;

    return 0;
}