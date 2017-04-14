# -*- coding: utf-8 -*-

import click
import rogue.api.project as project


@click.group()
def main(args=None):
    """Project managing"""
    click.echo("Replace this message by putting your code into "
               "installer.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


@main.command()
def create():
    """Create a new project"""
    project.create.create()


if __name__ == "__main__":
    main()
