cmake_minimum_required(VERSION 2.8.3)
project(design_pattern)

set(CMAKE_CXX_STANDARD 11)

# bridge
add_executable(${PROJECT_NAME}_bridge
        src/primary/bridge.cpp
        )

# adapter
add_executable(${PROJECT_NAME}_adapter
        src/primary/adapter.cpp
        )

# facade
add_executable(${PROJECT_NAME}_facade
        src/primary/facade.cpp
        )

# factory
add_executable(${PROJECT_NAME}_factory
        src/primary/factory.cpp
        )

# factory_map
add_executable(${PROJECT_NAME}_factory_map
        src/primary/factory_map.cpp
        )

# observer
add_executable(${PROJECT_NAME}_observer
        src/primary/observer.cpp
        )