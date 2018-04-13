#!/usr/bin/env python

from setuptools import setup

def readme():
    with open('README.md') as readme_file:
        return readme_file.read()


setup(name='persimmon',
      version='0.0.2',
      description='Python implementation persistent images representation of persistence diagrams.',
      long_description=readme(),
      author='Nathaniel Saul',
      author_email='nathaniel.saul@wsu.edu',
      url='https://github.com/sauln/persistence-images',
      license='MIT',
      packages=['persimmon'],
      include_package_data=True,
      install_requires=[
        'numpy',
        'matplotlib',
        'scipy'
      ],
      python_requires='>=2.7,!=3.1,!=3.2,!=3.3',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
      ],
      keywords='persistent homology, persistence images, persistence diagrams, topology data analysis, algebraic topology, unsupervised learning'
     )
