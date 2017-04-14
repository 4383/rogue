# -*- coding: utf-8 -*-

import os
from os.path import expanduser
import click
from rogue.utilities import console


DEFAULT_CONFIG_FILE = expanduser("~")


@click.command()
@click.argument('path', default=".", type=click.Path())
def init(path):
    """Initialize rogue environment"""
    console.info("Initialize rogue environment")
    print(path)
    path = os.path.join(path, '.rogue.cfg')
    with open(path, "w+") as config:
        config.write("ok")



if __name__ == "__main__":
    main()
