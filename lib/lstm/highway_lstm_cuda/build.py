# pylint: disable=invalid-name
import os
import torch
# from torch.utils.cpp_extension import create_extension

import glob
from setuptools import find_packages
from setuptools import setup
from torch.utils.cpp_extension import CUDA_HOME
from torch.utils.cpp_extension import CppExtension
from torch.utils.cpp_extension import CUDAExtension


##OLD
# if not torch.cuda.is_available():
#     raise Exception('HighwayLSTM can only be compiled with CUDA')

# sources = ['src/highway_lstm_cuda.c']
# headers = ['src/highway_lstm_cuda.h']
# defines = [('WITH_CUDA', None)]
# with_cuda = True

# this_file = os.path.dirname(os.path.realpath(__file__))
# extra_objects = ['src/highway_lstm_kernel.cu.o']
# extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]

# ffi = create_extension(
#         '_ext.highway_lstm_layer',
#         headers=headers,
#         sources=sources,
#         define_macros=defines,
#         relative_to=__file__,
#         with_cuda=with_cuda,
#         extra_objects=extra_objects
#         )

# if __name__ == '__main__':
#     ffi.build()

### NEW
requirements = ["torch", "torchvision"]


def get_extensions():
    this_dir = os.path.dirname(os.path.abspath(__file__))
    extensions_dir = os.path.join(this_dir, "src")

    main_cpp = glob.glob(os.path.join(extensions_dir, "main.cpp"))
    source_cpp = glob.glob(os.path.join(extensions_dir, "highway_lstm_cuda.cpp"))
    source_cuda = glob.glob(os.path.join(extensions_dir, "highway_lstm_kernel.cu"))

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
            "highway_lstm_layer1",
            sources,
            include_dirs=include_dirs,
            define_macros=define_macros,
            extra_compile_args=extra_compile_args,
        )
    ]

    return ext_modules


setup(
    name="highway_lstm",
    version="0.1",
    description="lstm in pytorch",
    packages=find_packages(exclude=("configs", "tests",)),
    # install_requires=requirements,
    ext_modules=get_extensions(),
    cmdclass={"build_ext": torch.utils.cpp_extension.BuildExtension},
)
