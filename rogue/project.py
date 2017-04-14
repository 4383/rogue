# -*- coding: utf-8 -*-

import click
from cookiecutter import repository


@click.command()
def main(args=None):
    """Rogue a DevOps CLI and API"""
    click.echo("Replace this message by putting your code into "
               "installer.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


@main.command()
def project():
    """Manage projects"""
    repository.determine_repo_dir(
        template='https://github.com/audreyr/cookiecutter-pypackage',
        abbreviations={},
        clone_to_dir='test',
        checkout="master",
        no_input=True
    )



if __name__ == "__main__":
    main()
