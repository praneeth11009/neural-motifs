# Changes made to migrate to pytorch1.0


0. Change the paramter async=True in .cuda() method to non_blocking=True
 
1. For create extensions use cpp_extensions, need to change the files for fpn/roi_align, fpn/nms, lstm.

2. Modify the extension builder build.py for nms.

3. Modify build.py for roi_align.

4. Modify build.py for highway_lstm (successful unlike the bug in previous 2 modifications)

5. An implementation of nms, roi_align is at lib/fpn/model/csrc, but arguments and functions names needs to be matched with our current requirements. (these functions are used in the .py wrapper file in functions dir)


# Bugs

1. undefined symbol _Z11ApplyNMSGPU... in the package nms1.so (Need to change cuda file ?)

2. similar error in roi_align : undefined symbol _Z22roi_align_forward_cudai.... (this kind of error is not there in highway_lstm)

3. Build will create the packages in current working directory, need to change the deafult output path to _ext, and fix package file name in the output.



