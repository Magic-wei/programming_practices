//
// Created by wangwei on 18-8-4.
//

#include "hello_world.h"

#include "iostream"


hello_world::hello_world(){
    count = 0; // init value is set to zero
}

hello_world::~hello_world(){

}

void hello_world::sayhello(){
    std::cout << "hello world" << std::endl;
    count++; // every time we use this function, count + 1
}

int hello_world::getCount(){
    return count;
}
