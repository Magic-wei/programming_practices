//
// Created by wangwei on 19-4-12.
//

#include <iostream>
#include <string>
#include <memory>

using namespace std;

int main(){
    // initialization methods
    shared_ptr<string> p1 = make_shared<string>();
    shared_ptr<string> p2 = make_shared<string>("hello");
    shared_ptr<string> p3 = make_shared<string>(10, '9');
    auto p4 = make_shared<int>(10);
    char trim_character = ' ';
    cout << *p1 << trim_character
         << *p2 << trim_character
         << *p3 << trim_character
         << *p4 << endl;

    // member function
    std::shared_ptr<int> sp5(new int(22));
    std::shared_ptr<int> sp6 = sp5;
    std::shared_ptr<int> sp7(sp6);
    printf("%d\n", *sp5);               // 22
    printf("%d\n", *sp6);               // 22
    printf("%d\n", *sp7);               // 22
    printf("%d\n", sp5.use_count());    // 3
    printf("%d\n", sp6.use_count());    // 3
    printf("%d\n", sp7.use_count());    // 3
    sp5.reset(new int(33));
    printf("%d\n", sp5.use_count());    // 1
    printf("%d\n", sp6.use_count());    // 2
    printf("%d\n", sp7.use_count());    // 2
    printf("%d\n", *sp5);               // 33
    printf("%d\n", *sp6);               // 22
    printf("%d\n", *sp7);               // 22

}