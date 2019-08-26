#include <THC/THC.h>
int nms_apply(THIntTensor* keep, THCudaTensor* boxes_sorted, const float nms_thresh);