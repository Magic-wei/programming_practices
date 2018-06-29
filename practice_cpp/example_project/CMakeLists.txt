cmake_minimum_required(VERSION 3.5)

# project name
project(example_project)

# enable c++11 feature 
set(CMAKE_CXX_FLAGS "-Wall -Wextra -std=c++11 ${CMAKE_CXX_FLAGS}")

# find the thirdparty library 
find_package(OpenCV REQUIRED)

# declare the include directories 
include_directories(
        include
        ${OpenCV_INCLUDE_DIRS})

#######################################################
####     How to add a library for a project 
#######################################################

################## add lib1 ########################################
add_library(${PROJECT_NAME}_lib1 SHARED
        src/lib1.cpp)
# link other thirdparty libraries for your ${PROJECT_NAME}_lib1
target_link_libraries(${PROJECT_NAME}_lib1
        ${OpenCV_LIBRARIES})


################# add lib2 ######################################### 
add_library(${PROJECT_NAME}_lib2 SHARED
        src/lib2.cpp)

# link other thirdparty libraries for your ${PROJECT_NAME}_lib2
target_link_libraries(${PROJECT_NAME}_lib2
        ${OpenCV_LIBRARIES})


#######################################################
#####   How to add an executable example that links libs 
#######################################################

##################    example 1   #########################################
####    How to add an executable example that links lib1 lib2 and thirdparty libraries 
add_executable(${PROJECT_NAME}_example1
        src/example1.cpp)

# link library1 for example 1
target_link_libraries(${PROJECT_NAME}_example1
        ${PROJECT_NAME}_lib1)





##################     example 2  #########################################
####    How to add an executable example that links lib1 lib2 and thirdparty libraries 
add_executable(${PROJECT_NAME}_example2
        src/example2.cpp)

# link lib1 lib2 and opencv for example 2
target_link_libraries(${PROJECT_NAME}_example2
        ${PROJECT_NAME}_lib1
        ${PROJECT_NAME}_lib2
        ${OpenCV_LIBRARIES})


