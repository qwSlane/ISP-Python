from setuptools import setup

setup(
    name='dumplibrary',
    packages=[
        'parsers',
        'parsers/core',
    ],
    version='1.0.1',
    author='ФИФТИСЭНТ',
    license='MIT',
    install_requires=[],
    test_suite='tests',
    scripts=['dump_service.py']
)