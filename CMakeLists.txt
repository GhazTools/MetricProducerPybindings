cmake_minimum_required(VERSION 3.23)
project(MetricProducer)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include_directories("lib")

add_subdirectory(lib/pybind11)
add_subdirectory(lib/MetricProducer)

set(SOURCE_DIR "src/metric_producer")
set(SOURCES "${SOURCE_DIR}/metric_producer_bindings.cpp")


pybind11_add_module(metric_producer_bindings ${SOURCES})
target_link_libraries(metric_producer_bindings PRIVATE MetricProducer)