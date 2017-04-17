# -*- coding: utf-8 -*-

import os
import os.path
import shutil
import time
import click
import rogue.commands.config as cmd_config
import rogue.api.project.controler as api_project
import rogue.api.config.controler as api_config
from rogue.utilities import console
from rogue.utilities import system


@click.group()
def project(args=None):
    """Project managing"""


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


def display_list(basedir):
    projects = api_project.list(basedir)

    data = []
    for index, el in enumerate(projects, 1):
        modified = api_project.is_modified(os.path.join(basedir, el))
        tracked = api_project.is_tracked(os.path.join(basedir, el))
        data.append([index, el, tracked, modified])
    console.show_list(data, ['id', 'name', 'tracked', 'status'], 'projects')


@project.command()
@click.option('--config', default=".rogue.cfg",
              type=click.File())
@click.option('-rt', '--realtime', is_flag=True)
@click.option('-t', '--timer', default=2, type=int)
def list(config, realtime, timer):
    console.info("Your projects:")
    context = api_config.read(config.name)
    default = dict(context['default_project'])
    basedir = default['basedir']
    if not os.path.isdir(basedir):
        console.error("Configuration basedir not defined")
        console.error("rogue-config add default_project.basedir <yourdir> --global")
        return
    if realtime:
        while True:
            click.clear()
            display_list(basedir)
            console.info("refresh every {}s".format(timer))
            time.sleep(timer)
    display_list(basedir)


@project.command()
@click.argument('project')
@click.option('--config', default=".rogue.cfg",
              type=click.File())
def remove(project, config):
    console.info("Your projects:")
    context = api_config.read(config.name)
    default = dict(context['default_project'])
    basedir = default['basedir']
    if not os.path.isdir(basedir):
        console.error("Configuration basedir not defined")
        console.error("rogue-config add default_project.basedir <yourdir> --global")
        return
    choice = os.path.join(basedir, project)
    console.info("remove {}".format(choice))
    shutil.rmtree(choice)


@project.command()
@click.argument('project')
@click.option('--config', default=".rogue.cfg",
              type=click.File())
def open(project, config):
    console.info("Your projects:")
    context = api_config.read(config.name)
    default = dict(context['default_project'])
    basedir = default['basedir']
    if not os.path.isdir(basedir):
        console.error("Configuration basedir not defined")
        console.error("rogue-config add default_project.basedir <yourdir> --global")
        return
    choice = os.path.join(basedir, project)
    console.info("open {}".format(choice))
    os.chdir(choice)
    print(os.getcwd())


if __name__ == "__main__":
    project()
