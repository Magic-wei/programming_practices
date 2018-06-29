#include <iostream>
#include "lib1.hpp"

example_project::Lib1::Lib1() :
        display_(false),
        image_() {
    this->image_ = cv::Mat(500, 500, CV_8UC4, cv::Scalar(255, 255, 255));
    std::cout << "Constructor of lib1." << std::endl;
}


void example_project::Lib1::sayHelloFromLib1() {
    cv::imshow("WindowForLib1", this->display_);
    std::cout << "Hello from lib1." << std::endl;
}

