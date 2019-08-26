#!/usr/bin/env bash
cuda_path=/usr/local/cuda/

cd ~/scene_graph/neural\-motifs\-master/lib/fpn/nms/src/cuda
echo "Compiling stnn kernels by nvcc..."
ls 
nvcc -c -o nms.cu.o nms_kernel.cu -x cu -Xcompiler -fPIC -arch=sm_52

cd ../../
python build.py