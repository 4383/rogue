# -*- coding: utf-8 -*-

import click
from cookiecutter import repository


@click.command()
def main(args=None):
    """Rogue| DevOps CLI and API"""
    click.echo("Replace this message by putting your code into "
               "installer.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
