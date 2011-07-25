from setuptools import setup


setup(
        name = 'nptime',
        version = 0.1,
        author = 'Thomas Grenfell Smith',
        author_email = 'thomathom@gmail.com',
        description = 'Non-pedantic replacement for datetime.time',
        license = 'LICENSE.txt',
        keywords = 'time datetime timedelta',
        py_modules = ['nptime'],

        tests_require = ['Nose'],
        )

