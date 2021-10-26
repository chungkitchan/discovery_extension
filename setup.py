#!/usr/bin/env python

from setuptools import setup
from os import path

__version__ = '0.1'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as file:
    readme_file = file.read()

setup(name='discovery_extension',
      version=__version__,
      description='An extension to Discovery SDK with beta curation API',
      # list folders, not files
      packages=['discovery_extension'],
      license='Apache 2.0',
      author='Chan Chung Kit',
      author_email='chanck@sg.ibm.com',
      long_description=readme_file,
      long_description_content_type='text/markdown',
      url='https://github.com/chungkitchan/discovery_extension',
      include_package_data=False,
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: Libraries :: Application '
          'Frameworks',
      ],
      zip_safe=True
     )