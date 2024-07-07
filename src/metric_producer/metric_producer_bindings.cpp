#include "MetricProducer/include/metric_producer.hpp"

// THIRD PARTY IMPORTS START HERE
#include "pybind11/include/pybind11/pybind11.h"
#include "pybind11/include/pybind11/stl.h"
// THIRD PARTY IMPORTS END HERE

namespace py = pybind11;

PYBIND11_MODULE(metric_producer_bindings, m)
{
    py::class_<MetricProducer>(m, "MetricProducerBindings")
        .def(py::init())
        .def("produce", &MetricProducer::produce);
}