import os
import sys
from setuptools import setup, find_packages

version = '0.1'

install_requires = [
    'setuptools',
    'pyramid >= 1.9',
]

tests_require = install_requires + [
    'nose'
]


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


setup(name='p2s',
      version=version,
      description=('P2S is the platform for to sale'),
      long_description='\n\n'.join((read('README.rst'), read('CHANGES.txt'))),
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.6",
          "Framework :: Pyramid",
      ],
      author='Bohdan Tsekhanskiy',
      author_email='kirweb@gmail.com',
      url='https://github.com/samael/p2s',
      license='BSD-derived',
      packages=find_packages(),
      install_requires=install_requires,
      extras_require=dict(test=tests_require),
      tests_require=tests_require,
      test_suite='nose.collector',
      include_package_data=True,
      zip_safe=False,
      entry_points={
      },
      )
