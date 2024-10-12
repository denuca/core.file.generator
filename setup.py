from setuptools import setup, find_packages

setup(
    name='core.file.generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # For image manipulation in PPTX files
        'python-pptx',  # For PowerPoint generation
        'openpyxl',  # For Excel generation
    ],
    author='Your Name',
    description='A core library for generating PPTX, Excel, and other files.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
