from setuptools import setup, find_packages

from torch.utils.cpp_extension import BuildExtension, CUDAExtension

NVCC_ARGS = [
    '-D__CUDA_NO_HALF_OPERATORS__',
    '-D__CUDA_NO_HALF_CONVERSIONS__',
    '-D__CUDA_NO_HALF2_OPERATORS__',
]

setup(
    name='carafe',
    version='0.0.1',
    license='MIT',
    ext_modules=[
        CUDAExtension(
            'carafe_ext', [
                'carafe/src/cuda/carafe_cuda.cpp',
                'carafe/src/cuda/carafe_cuda_kernel.cu',
                'carafe/src/carafe_ext.cpp'
            ],
            define_macros=[('WITH_CUDA', None)],
            extra_compile_args={
                'cxx': [],
                'nvcc': NVCC_ARGS
            }),
        CUDAExtension(
            'carafe_naive_ext', [
                'carafe/src/cuda/carafe_naive_cuda.cpp',
                'carafe/src/cuda/carafe_naive_cuda_kernel.cu',
                'carafe/src/carafe_naive_ext.cpp'
            ],
            define_macros=[('WITH_CUDA', None)],
            extra_compile_args={
                'cxx': [],
                'nvcc': NVCC_ARGS
            })
    ],
    packages=find_packages(exclude=('test', )),
    cmdclass={'build_ext': BuildExtension},
    zip_safe=False,
)
