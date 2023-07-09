import os
from setuptools import setup, find_packages


# Helper function to load up readme as long description.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name = 'sa-qubo',
        version = '0.1',
        author='Zhili Xiao', 
        author_email='xiaozhili@wustl.edu',
        description=('A simple annealing solver for QUBO problems'),
        keywords = 'simulated annealing, QUBO, max cut',
        url='http://github.com/neuromorphs/qins23-hdc',
        packages=find_packages(),
        long_description=read('README.md'),
        classifiers=[
            'Development Status :: 1 - Planning',
            'Programming Language :: Python :: 3',
            'Environment :: Console', 
            'Topic :: Scientific/Engineering :: Artificial Intelligence'
            ],
        install_requires=[
            'numpy',
        ]
)