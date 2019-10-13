//
// Created by wangwei on 2019/10/13.
//

#include <iostream>

using namespace std;

class Product {
public:
    virtual ~Product() {
        cout << "delete Product" << endl;
    }
    virtual const char* getName() = 0;
}; // class ProductA

class ConcreteProductA : public Product {
public:
    ~ConcreteProductA() {
        cout << "delete Concrete Product A." << endl;
    }
    const char* getName() {
        return "A-X";
    }
}; // class ConcreteProductA

class ConcreteProductB : public Product {
public:
    ~ConcreteProductB() {
        cout << "delete Concrete Product B." << endl;
    }
    const char* getName() {
        return "B-Y";
    }
}; // class ConcreteProductB


class Factory {
public:
    virtual ~Factory() {}
    virtual Product* createProductA() = 0;
    virtual Product* createProductB() = 0;
    virtual void removeProduct(Product* product) = 0;
}; // class Factory

class ConcreteFactory : public Factory {
public:
    ~ConcreteFactory() {
        cout << "delete Concrete Factory." << endl;
    }
    Product* createProductA() {
        return new ConcreteProductA();
    }
    Product* createProductB() {
        return new ConcreteProductB();
    }

    void removeProduct(Product* product){
        delete product;
    }
}; // class ConcreteFactory

int main(){
    ConcreteFactory factory;
    Product *p1 = factory.createProductA();
    cout << "Product: " << p1->getName() << endl;
    Product *p2 = factory.createProductB();
    cout << "Product: " << p2->getName() << endl;
    delete p2;
    factory.removeProduct(p1);

    return 0;
}
