#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='pipelinewise-tap-snowflake',
    version='3.0.0',
    description='Singer.io tap for extracting data from Snowflake - PipelineWise compatible',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="TransferWise",
    url='https://github.com/transferwise/pipelinewise-tap-snowflake',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
    ],
    py_modules=['tap_snowflake'],
    install_requires=[
        'pipelinewise-singer-python==1.*',
        'snowflake-connector-python[pandas]==3.13.1',
        'numpy>=1.23,<3',
        'pendulum>=2.1.2,<3',
        # Keep HTTP stack compatible with connector 3.13.1
        'requests>=2.28,<3',
        'urllib3>=1.26,<2',
        # Avoid pyOpenSSL upper-bound clashes on 3.13.1
        'pyOpenSSL<26.0.0',
    ],
    extras_require={
        'test': [
            'pylint==2.8.*',
            'pytest==6.2.*',
            'pytest-cov==2.12.*',
            'unify==0.5',
        ]
    },
    entry_points='''
        [console_scripts]
        tap-snowflake=tap_snowflake:main
    ''',
    packages=['tap_snowflake', 'tap_snowflake.sync_strategies'],
)