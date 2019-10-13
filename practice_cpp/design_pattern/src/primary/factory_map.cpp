//
// Created by wangwei on 2019/10/13.
//

#include <iostream>
#include <map>
using namespace std;

class Product {
public:
    virtual ~Product() {
        cout << "delete Product" << endl;
    }
    virtual void action() = 0;
}; // class ProductA

class ConcreteProduct : public Product {
public:
    ConcreteProduct(int new_state): state(new_state) {}
    ~ConcreteProduct() {
        cout << "delete Concrete Product with state " << state << "." << endl;
    }
    void action() {
        cout << "Concrete Product with state " << state << endl;
    }

private:
    int state;
}; // class ConcreteProduct

class Factory {
public:
    virtual ~Factory() {
        for(auto pair : products){
            delete pair.second;
        }
    }

    Product* getProduct(const int key) {
        if(products.find(key) != products.end()){
            return products[key];
        }
        Product *product = new ConcreteProduct(key);
        products.insert(std::pair<int, Product*>(key, product));
        return product;
    }

private:
    std::map<int, Product*> products;
}; // class Factory

int main(){
    Factory factory;
    factory.getProduct(1)->action();
    factory.getProduct(2)->action();

    return 0;
}
