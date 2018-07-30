cmake_minimum_required(VERSION 2.8.3)
project(func_test)

set(CMAKE_CXX_STANDARD 11)

# namespace_main
set(SOURCE_FILES src/namespace_main.cpp)
add_executable(namespace_main ${SOURCE_FILES})

# costime_test_main
add_executable(costime_test_main
        src/costime_test_main.cpp
        )

# CppAD_test_main
add_executable(CppAD_test_main
        src/cppad_test_main.cpp
        )

# Eigen_nan2inf_main
add_executable(Eigen_nan2inf_main
        src/Eigen_nan2inf_main.cpp
        )

# PID_test_main
add_executable(PID_test_main
        src/PID_test_main.cpp
        )

# matplotlib_test_main
find_package(PythonLibs 2.7)
add_executable(matplotlib_test_main
        src/matplotlib_test_main.cpp
        src/matplotlib/matplotlibcpp.h
        )
target_include_directories(matplotlib_test_main PRIVATE ${PYTHON_INCLUDE_DIRS})
target_link_libraries(matplotlib_test_main ${PYTHON_LIBRARIES})

# template_test_main
add_executable(template_test_main
        src/template_test_main.cpp
#         src/template/template_test.cpp # 如果包含这个文件会报错说redifinition，回头找一下原因
        )