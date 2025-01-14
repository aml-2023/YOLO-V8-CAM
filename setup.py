from setuptools import setup, find_packages

setup(
    name='yolocam',
    version='0.1',
    packages=find_packages(),
    install_requires=['jupyter',
                      'numpy',
                      'pandas',
                      'matplotlib',
                      'ultralytics',
                      'torch',
                      'torchvision',
                      'opencv-python',
                      'ttach']
)