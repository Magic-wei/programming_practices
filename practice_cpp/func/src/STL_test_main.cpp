//
// Created by wangwei on 18-7-30.
//

#include <iostream>
#include <queue>
#include <array>
#include <list>
#include <vector>
#include <utility>
#include <map>
#include <unordered_map>
#include <algorithm>

using namespace std;


int main(){

    /** iterator
     *  Usage: vector<int>::iterator -OR- auto ...
     */
    vector<int> int_vec(10,1);
    for (vector<int>::iterator it_Int = int_vec.begin();it_Int!=int_vec.end(); ++it_Int) {
        *it_Int += it_Int - int_vec.begin();
        cout << *it_Int << " ";
    }
    cout << "\n";
    int_vec.clear();
    cout << "int_vec's size is " << int_vec.size() << endl;

    /** Containers - Part One
     *  array, queue, list
     */

    // array
    const size_t num_array = 10;
    array<float,num_array> array_Int = {};
    cout << "is empty? " << array_Int.empty() << endl;
    for (auto it = array_Int.begin(); it != array_Int.end(); ++it) {
        *it = it - array_Int.begin();
    }
    cout << "the first element is " << array_Int.front() << endl;
    cout << "the last element is " << array_Int.back() << endl;
    cout << "size: " << array_Int.size() << endl; // we usually use this.
    cout << "max size: " << array_Int.max_size() << endl; // maybe useful when use reverse(n)
    array_Int.fill(10); // overwrite all members by 10

    // queue
    queue<double> queue_ctrl;
    for (int i = 0; i < 10; ++i) {
        queue_ctrl.push(i*1.0);
    }
    while(!queue_ctrl.empty()){
        cout << queue_ctrl.front() << " ";
        queue_ctrl.pop(); // no return value, so if you want the first value, use front()
    }
    cout << "\n";
    queue_ctrl.push(1.5);
    queue<double> empty_q;
    swap(empty_q,queue_ctrl); // no clear function for queue container, swap with an empty queue to clear it.

    // list
    std::list<int> list1 = { 7, 5, 16, 8 };
    list1.push_front(25); // Add an integer to the front of the list
    list1.push_back(13); // Add an integer to the back of the list
    // Insert an integer before 16 by searching, <algorithm> is needed
    auto it = std::find(list1.begin(), list1.end(), 16);
    if (it != list1.end()) {
        list1.insert(it, 16);
    }
    // Iterate and print values of the list
    cout << "list output: ";
    for (int n : list1) {
        std::cout << n << ' ';
    }
    cout << "\n";
    list1.push_front(1);
    list1.push_front(1);
    list1.push_front(2);
    list1.push_front(2);
    list1.unique();
    for (int m : list1) {
        std::cout << m << ' ';
    }
    cout << "\n";

    /** Containers - Part Two
     *  pair, map, unordered_map
     */

    // pair - Defined in header <utility>
    pair<double, double> xy1 = {1.0, 5.0}, xy2 = {30.0, 2.0};
    cout << "first element is " << xy1.first << ", the second element is " << xy1.second << "\n";
    xy1.swap(xy2); // swap two pairs

    // map
    map<char,int> letter_counts = { {'a',27},{'b',12},{'c',2} };
    std::cout << "map initially - ";
    for (const auto &pair : letter_counts) {
        std::cout << pair.first << ": " << pair.second << "; ";
    }
    cout << "\n";

        // count the number of occurrences of each word
        // (the first call to operator[] initialized the counter with zero)
    std::map<std::string, size_t>  word_map;
    for (const auto &w : { "this", "sentence", "is", "not", "a", "sentence",
                           "this", "sentence", "is", "a", "hoax"}) {
        ++word_map[w];
    }
    for (const auto &pair : word_map) {
        std::cout << pair.second << " occurrences of word '" << pair.first << "'\n";
    }

    // unordered_map
    unordered_map<std::string, std::string> u = { {"RED","#FF0000"},
          {"GREEN","#00FF00"}, {"BLUE","#0000FF"} };
    u["BLACK"] = "#000000";
    u["WHITE"] = "#FFFFFF";
    std::cout << "The HEX of color RED is:[" << u["RED"] << "]\n";
    std::cout << "The HEX of color BLACK is:[" << u["BLACK"] << "]\n";


    /** Algorithms
     *
     */


}