from setuptools import setup, find_packages
import sys, os
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


version = '0.1'

setup(name='czml',
      version=version,
      description="Read and write CZML in Python",
      long_description=open('README.rst').read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='GIS JOSN CZML Cesium Globe',
      author='Christian Ledermann',
      author_email='christian.ledermann@gmail.com',
      url='https://github.com/cleder/czml',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      tests_require=['pytest'],
      cmdclass = {'test': PyTest},
      install_requires=[
          # -*- Extra requirements: -*-
          "pygeoif",
          'python-dateutil',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
