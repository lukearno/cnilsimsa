import os

from setuptools import setup, find_packages, Extension


with open('README.md') as readme_file:
    README = readme_file.read().strip()

PROJECT = README.strip('#').split('\n')[0].strip().split()[0].lower()
DESCRIPTION = README.split('\n')[2]

with open('%s/VERSION' % PROJECT, 'rb') as version_file:
    VERSION = version_file.read().strip()


setup(name=PROJECT,
      version=VERSION,
      description=DESCRIPTION,
      long_description=README,
      license='GPL2+',
      author='Luke Arno',
      author_email='luke.arno@gmail.com',
      url='http://github.com/lukearno/cnilsimsa',
      ext_modules=[Extension('_nilsimsa', sources=['cnilsimsa/_nilsimsa.c'])],
      packages=[PROJECT],
      include_package_data=True,
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved '
                   ':: GNU General Public License v2 or later (GPLv2+)',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: C',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Utilities'])
