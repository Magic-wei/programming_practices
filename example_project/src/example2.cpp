#include "lib1.hpp"
#include "lib2.hpp"

// include some header files you used from thirdparty libraries
int main( int argc, char **argv )
{
    (void)argv;
    (void)argc;
    example_project::Lib1 object1;
    example_project::Lib2 object2;
    object2.sayHelloFromLib2();
    object1.sayHelloFromLib1();
    
    // some codes that call functions from thirdparty libraries
    
    cv::Mat main_image = cv::Mat(800, 800, CV_8UC4, cv::Scalar(255, 255, 255));
    cv::imshow("MainWindow", main_image);
    cv::waitKey(-1);  // wait for keyboard input to terminate
    return 0;
}