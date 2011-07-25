from setuptools import setup


setup(
        name = 'nptime',
        version = 0.1,
        author = 'Thomas Grenfell Smith',
        author_email = 'thomathom@gmail.com',
        description = 'Non-pedantic replacement for datetime.time',
        license = 'LICENSE.txt',
        keywords = 'time datetime timedelta',
        packages = 'nptime',

        tests_require = ['Nose'],
        )

