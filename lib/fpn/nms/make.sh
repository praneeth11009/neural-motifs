#!/usr/bin/env bash
cuda_path=/usr/local/cuda/

echo "Compiling stnn kernels by nvcc..."

python build.py build_ext