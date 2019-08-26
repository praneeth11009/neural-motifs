#!/usr/bin/env bash

export CUDA_VISIBLE_DEVICES='1'
export PYTHONPATH=~/scene_graph/git_pytorch1/neural-motifs

echo "VISUALIZE MOTIFNET"
python models/_visualize.py -val_size 400 -m sgdet -model motifnet -order leftright -nl_obj 2 -nl_edge 4 -b 6 -clip 5 \
    -p 100 -hidden_dim 512 -pooling_dim 4096 -lr 1e-3 -ngpu 1 -test -ckpt checkpoints/motifnet-sgdet/vgrel-14.tar -nepoch 50 -cache motifnet_sgdet.pkl -use_bias
