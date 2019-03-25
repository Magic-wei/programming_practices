cmake_minimum_required(VERSION 2.8.3)
project(optimization)

set(CMAKE_CXX_STANDARD 11)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake")
message(STATUS "CMAKE SOURCE DIR:" ${CMAKE_MODULE_PATH} )

include_directories(
        include
)

# Ipopt & CppAD
find_package(IPOPT REQUIRED)
set(SOURCE_FILES
        src/opt_ipopt_cppad_quickstart.cpp
        )
add_executable(${PROJECT_NAME}_Ipopt_CppAD ${SOURCE_FILES})
target_link_libraries(${PROJECT_NAME}_Ipopt_CppAD
        ${IPOPT_LIBRARIES}
        ${LINKER_LIBS}
        )
