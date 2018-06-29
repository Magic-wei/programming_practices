
#ifndef SIMPLE_CPP_PROJECT_LIB2_HPP
#define SIMPLE_CPP_PROJECT_LIB2_HPP

namespace example_project {
class Lib2 {
 public:
    Lib2();
    void sayHelloFromLib2();
    void setDisplay(bool flag) { this->display_ = flag; };
    bool getDisplay() { return this->display_; };
 private:
    bool display_{};
};
}  // namespace example_project

#endif   // SIMPLE_CPP_PROJECT_LIB2_HPP
