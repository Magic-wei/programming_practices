//
// Created by wangwei on 2019/10/13.
//

#include <iostream>

using namespace std;

class Implementor {
public:
    virtual ~Implementor() {}
    virtual void action() = 0;
}; // class Implementor

class ConcreteImplementor : public Implementor {
public:
    ~ConcreteImplementor() {}

    void action(){
        cout << "Concrete implementor action." << endl;
    }
};  // class ConcreteImplementor

class Abstraction {
public:
    virtual ~Abstraction() {}
    virtual void operation() = 0;
}; // class Abstraction

class ConcreteAbstraction : public Abstraction {
public:
    ConcreteAbstraction(Implementor *impr): implementor(impr) {}
    ~ConcreteAbstraction() {}
    void operation() {
        implementor->action();
    }
private:
    Implementor *implementor;
}; // class ConcreteAbstraction

int main(){
    Implementor *pi = new ConcreteImplementor();
    Abstraction *abstract = new ConcreteAbstraction(pi);
    abstract->operation();

    delete pi;
    delete abstract;

    return 0;
}