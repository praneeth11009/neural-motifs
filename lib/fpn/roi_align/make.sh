#!/usr/bin/env bash

CUDA_PATH=/usr/local/cuda/

echo "Compiling my_lib kernels by nvcc..."
python build.py build_ext
