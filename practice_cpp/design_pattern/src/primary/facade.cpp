//
// Created by wangwei on 2019/10/13.
//

#include <iostream>

using namespace std;

class SubsystemA {
public:
    ~SubsystemA() {
        cout << "delete Subsystem A." << endl;
    }
    void suboperation(){
        cout << "Subsystem A operation." << endl;
    }
}; // class SubsystemA

class SubsystemB {
public:
    ~SubsystemB() {
        cout << "delete Subsystem B." << endl;
    }
    void suboperation(){
        cout << "Subsystem B operation." << endl;
    }
}; // class SubsystemB

class SubsystemC {
public:
    ~SubsystemC() {
        cout << "delete Subsystem C." << endl;
    }
    void suboperation(){
        cout << "Subsystem C operation." << endl;
    }
}; // class SubsystemC

class Facade {
public:
    Facade(): subsystemA(),
              subsystemB(),
              subsystemC() {}
    ~Facade() {
        cout << "delete facade." << endl;
    }
    void operation1(){
        subsystemA.suboperation();
        subsystemB.suboperation();
    }

    void operation2(){
        subsystemC.suboperation();
    }

private:
    SubsystemA subsystemA;
    SubsystemB subsystemB;
    SubsystemC subsystemC;
}; // class Facade

class Facade2 {
public:
    Facade2(): subsystemA(new SubsystemA()),
              subsystemB(new SubsystemB()),
              subsystemC(new SubsystemC()) {}
    ~Facade2() {
        cout << "delete facade." << endl;
        delete subsystemA;
        delete subsystemB;
        delete subsystemC;
    }
    void operation1(){
        subsystemA->suboperation();
        subsystemB->suboperation();
    }

    void operation2(){
        subsystemC->suboperation();
    }

private:
    SubsystemA *subsystemA;
    SubsystemB *subsystemB;
    SubsystemC *subsystemC;
};

int main(){
    Facade *facade = new Facade();
    facade->operation1();
    facade->operation2();
    delete facade;

    Facade2 *facade2 = new Facade2();
    facade2->operation1();
    facade2->operation2();
    delete facade2;

    return 0;
}