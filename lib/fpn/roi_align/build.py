from __future__ import print_function
import os
import torch

## OLD
# from torch.utils.ffi import create_extension

## NEW
import glob
from setuptools import find_packages
from setuptools import setup
from torch.utils.cpp_extension import CUDA_HOME
from torch.utils.cpp_extension import CppExtension
from torch.utils.cpp_extension import CUDAExtension


## OLD
# sources = ['src/roi_align.c']
# headers = ['src/roi_align.h']
# extra_objects = []
# #sources = []
# #headers = []
# defines = []
# with_cuda = False

# this_file = os.path.dirname(os.path.realpath(__file__))
# print(this_file)

# if torch.cuda.is_available():
#     print('Including CUDA code.')
#     sources += ['src/roi_align_cuda.c']
#     headers += ['src/roi_align_cuda.h']
#     defines += [('WITH_CUDA', None)]
#     with_cuda = True
    
#     extra_objects = ['src/roi_align_kernel.cu.o']
#     extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]

# ffi = create_extension(
#     '_ext.roi_align',
#     headers=headers,
#     sources=sources,
#     define_macros=defines,
#     relative_to=__file__,
#     with_cuda=with_cuda,
#     extra_objects=extra_objects
# )

# if __name__ == '__main__':
#     ffi.build()

equirements = ["torch", "torchvision"]


def get_extensions():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    extensions_dir = os.path.join(this_dir, "src")

    main_cpp = glob.glob(os.path.join(extensions_dir, "main.cpp"))
    source_cpp = glob.glob(os.path.join(extensions_dir, "roi_align.cpp"))
    source_cuda = glob.glob(os.path.join(extensions_dir, "roi_align_cuda.cpp"))
    source_cuda = source_cuda + glob.glob(os.path.join(extensions_dir, "roi_align_kernel.cu"))

    sources = main_cpp + source_cpp
    extension = CppExtension

    extra_compile_args = {"cxx": []}
    define_macros = []

    if torch.cuda.is_available() and CUDA_HOME is not None:
        extension = CUDAExtension
        sources = sources + source_cuda
        define_macros += [("WITH_CUDA", None)]
        extra_compile_args["nvcc"] = [
            "-DCUDA_HAS_FP16=1",
            "-D__CUDA_NO_HALF_OPERATORS__",
            "-D__CUDA_NO_HALF_CONVERSIONS__",
            "-D__CUDA_NO_HALF2_OPERATORS__",
        ]

    sources = [os.path.join(extensions_dir, s) for s in sources]
    print('sources', sources)

    include_dirs = [extensions_dir]

    ext_modules = [
        extension(
            "roi_align1",
            sources,
            include_dirs=include_dirs,
            define_macros=define_macros,
            extra_compile_args=extra_compile_args,
        )
    ]

    return ext_modules


setup(
    name="faster_rcnn",
    version="0.1",
    description="object detection in pytorch",
    packages=find_packages(exclude=("configs", "tests",)),
    # install_requires=requirements,
    ext_modules=get_extensions(),
    cmdclass={"build_ext": torch.utils.cpp_extension.BuildExtension},
)