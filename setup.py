import glob
from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension


setup(
    name='test',
    ext_modules=[
        CppExtension(
            name='test',
            pkg='test',
            sources=glob.glob('*.cpp'))
    ],
    cmdclass={
        'build_ext': BuildExtension,
    }
)
