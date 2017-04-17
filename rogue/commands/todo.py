# -*- coding: utf-8 -*-

import os
import os.path
import shutil
import time
import click
import rogue.api.todo.controler as api_todo
import rogue.api.config.controler as api_config
from rogue.utilities import console
from rogue.utilities import system
from terminaltables import SingleTable


@click.group()
def todo(args=None):
    """Manage todo list"""


@todo.command()
@click.argument('task', type=str)
@click.option('-p', '--priority', default="normal",
              type=click.Choice(['hight', 'low', 'normal']))
@click.option('--config', default=".rogue.cfg",
              type=click.File())
def add(task, priority, config):
    """Add a new task to the todo list"""
    store = api_todo.Todo()
    store.add(task, priority)


@todo.command()
@click.option('--config', default=".rogue.cfg",
              type=click.File())
def list(config):
    """List the todo list"""
    store = api_todo.Todo()
    #tasks = api_sort(store.ls())
    tasks = store.ls()
    headers = ['id', 'Priority', 'done', 'description']
    data = []
    for el in tasks:
        identifier, content, _, _, active, priority = el
        data.append([identifier, priority, "" if active else "X", content])
    console.show_table(data, headers, 'tasks')
    #if task['hight']:
    #for el in tasks['hight']:
    #    display_row(el)
    #for el in tasks['normal']:
    #    display_row(el)
    #for el in tasks['low']:
    #    display_row(el)


@todo.command()
@click.argument('task', type=int, nargs=+1)
@click.option('--config', default=".rogue.cfg",
              type=click.File())
def delete(task, config):
    """Delete a task from the todo list"""
    store = api_todo.Todo()
    #for identifier in tasks:
        #store.delete(identifier)
    store.delete(task)


@todo.command()
@click.argument('task', nargs=+1)
@click.option('--config', default=".rogue.cfg",
              type=click.File())
def done(task, config):
    """Mark a task is done from the todo list"""
    store = api_todo.Todo()
    store.done(task)


@todo.command()
@click.argument('id', type=int, nargs=+1)
@click.option('--config', default=".rogue.cfg",
              type=click.File())
def info(id, config):
    """Get task information from the todo list"""
    store = api_todo.Todo()
    tasks = store.info(tasks)
    for el in tasks:
        print("Id: {}".format(el[0]))
        print("Description: {}".format(el[1]))
        print("Created: {}".format(el[2]))


if __name__ == "__main__":
    project()
