// Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
#include <torch/extension.h>
#include "roi_align_cuda.h"
#include "roi_align.h"

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("roi_align_forward_cuda", &roi_align_forward_cuda, "roi_align_forward_cuda");
  m.def("roi_align_backward_cuda", &roi_align_forward_cuda, "roi_align_forward_cuda");
  m.def("roi_align_forward", &roi_align_forward, "roi_align_forward");
  m.def("roi_align_backward", &roi_align_forward, "roi_align_forward");
}