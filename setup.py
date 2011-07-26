from setuptools import setup
from version import __release__

setup(
        name = 'nptime',
        version = __release__,
        author = 'Thomas Grenfell Smith',
        author_email = 'thomathom@gmail.com',
        url = 'https://github.com/tgs/nptime',
        description = 'Extends datetime.time, allowing time arithmetic',
        long_description = open('README.rst').read(),
        license = 'LICENSE.txt',
        keywords = 'time datetime timedelta',
        py_modules = ['nptime'],

        test_suite = 'nose.collector',
        tests_require = ['Nose'],
        )

