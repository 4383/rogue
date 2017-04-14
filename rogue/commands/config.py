# -*- coding: utf-8 -*-

import os
from os.path import expanduser
import click
from rogue.utilities import console
from rogue.commands.init import DEFAULT_CONFIG_FILE
import rogue.api.config as api_config


@click.group()
def config():
    """Initialize rogue environment"""
    console.info("Initialize rogue environment")

@config.command()
@click.argument("options", nargs=-1)
@click.option("--glob", is_flag=True)
@click.option("--local", is_flag=True)
def add(options, glob, local):
    """Add rogue configuration"""
    console.info("Initialize rogue environment")
    if glob:
        path = DEFAULT_CONFIG_FILE
    elif local:
        path = '.'
    else:
        path = '.'
    path = os.path.join(path, ".rogue.cfg")
    api_config.add.add(path, options)
    print("ici")


@config.command()
@click.option("--glob", is_flag=True)
@click.option("--local", is_flag=True)
def read(glob, local):
    """Add rogue configuration"""
    if glob:
        path = DEFAULT_CONFIG_FILE
    elif local:
        path = '.'
    else:
        path = '.'
    path = os.path.join(path, ".rogue.cfg")
    api_config.controler.read(path)

if __name__ == "__main__":
    main()
