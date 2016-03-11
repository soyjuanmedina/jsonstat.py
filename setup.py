# stdlib
# from builtins import exec

import sys
import os
from setuptools import setup

# version_file = open(os.path.join(mypackage_root_dir, 'VERSION'))
# version = version_file.read().strip()

exec(open('jsonstat/version.py').read())


# execfile is only python 2
# execfile('jsonstat/version.py')

# if sys.version_info >= (3,2):
#     install_requires = ["threadpool >= 1.2.7"]
# else:
#     install_requires = ["threadpool >= 1.2.3"]
#
# setup(..., install_requires=install_requires)

# from https://pythonhosted.org/an_example_pypi_project/setuptools.html
# Utility function to read the README file.
# Used for the long_description.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="jsonstat.py",
    description='Library for reading JSON-stat format data.',
    long_description=read('README.rst'),
    keywords="jsonstat json statistics",

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Environment :: Console',

        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],

    version=__version__,
    url='https://github.com/26fe/jsonstat.py',

    author='26fe',
    author_email='gf@26fe.com',

    license='LGPL',
    # packages= setup.find_packages(exclude=['examples', 'docs', 'tests*', 'tmp']),
    packages=[
        'jsonstat', 'jsonstat.cli', 'istat'
    ],

    install_requires=[
        'pandas',
        'requests',
        'click'
    ],

    tests_require=[
        'httpretty',
        'sure',
        'runipy'
    ],

    entry_points={
        'console_scripts': [
            'jsonstat=jsonstat.cli.cli_jsonstat:main',  # command=package.module:function
        ],
    },

)
