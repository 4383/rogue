#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        develop.run(self)
        from rogue.commands import init
        from rogue.utilities import console
        console.info("Prepare rogue environnement")
        init.init(".")

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        install.run(self)
        from rogue.commands import init
        from rogue.utilities import console
        console.info("Prepare rogue environnement")
        init.init(".")

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'cookiecutter',
    'terminaltables',
    'GitPython',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='rogue',
    version='0.1.0',
    description="DevOps CLI and API",
    long_description=readme + '\n\n' + history,
    author="Hervé Beraud",
    author_email='herveberaud.pro@gmail.com',
    url='https://github.com/4383/rogue',
    packages=find_packages(),
    package_dir={'rogue':
                 'rogue'},
    entry_points={
        'console_scripts': [
            'rogue=rogue.cli:main',
            'rogue-project=rogue.commands.project:project',
            'rogue-config=rogue.commands.config:config',
            'rogue-init=rogue.commands.init:init',
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='rogue',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
)
