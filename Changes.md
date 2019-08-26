# Changes made to migrate to pytorch1.0


```
# 


0. Change the paramter async=True in .cuda() method to non_blocking=True
 
1. For create extensions use cpp_extensions, need to change the files for fpn/roi_align, fpn/nms, lstm.

2. Modify the extension builder build.py for nms.

3. Modify build.py for roi_align.


#Bugs

1. undefined symbol _Z11ApplyNMSGPU... in the package nms1.so (Need to change cuda file ?)

2. similar error in roi_align : undefined symbol _Z22roi_align_forward_cudai....

3. Build will create the packages in current working directory, need to change the deafult output path to _ext, and fix package file name in the output.



