// Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
#include <torch/extension.h>
#include "highway_lstm_cuda.h"

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("highway_lstm_forward_cuda", &highway_lstm_forward_cuda, "highway_lstm_forward_cuda");
  m.def("highway_lstm_backward_cuda", &highway_lstm_backward_cuda, "highway_lstm_backward_cuda");
}