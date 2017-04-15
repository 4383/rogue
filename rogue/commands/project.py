# -*- coding: utf-8 -*-

import os
import os.path
import click
import rogue.commands.config as cmd_config
import rogue.api.project.controler as api_project
import rogue.api.config.controler as api_config
from rogue.utilities import console
from rogue.utilities import system


@click.group()
def project(args=None):
    """Project managing"""
    click.echo("Replace this message by putting your code into "
               "installer.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


@project.command()
@click.option('--config', default=".rogue.cfg",
              type=click.File())
def create(config):
    """Create a new project"""
    context = api_config.read(config.name)
    console.show_config(context)
    default = dict(context['default_project'])
    project_path = os.path.join(default['basedir'], default['project_slug'])
    if os.path.isdir(project_path):
        console.error("Project already exist")
        return
    api_project.create(default)
    system.store(context, project_path)


if __name__ == "__main__":
    project()
