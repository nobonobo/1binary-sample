from __future__ import absolute_import, unicode_literals, print_function, division

import os
from setuptools import setup, find_packages

VERSION='0.1.0'
ROOT = os.path.realpath(os.path.dirname(__file__))

install_requires = [
    'django>=1.9.2',
    'pytz>=2015.7',
    'django-bootstrap3>=6.2.2',
    'gevent>=1.1rc3',
]

setup(
    name='app',
    version=VERSION,
    author='accense',
    author_email='sample@sample.org',
    url='http://sample.org',
    description='sample webui server.',
    long_description='''
sample
''',
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    extras_require={},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'main = app.serve:main',
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development'
    ],
)
