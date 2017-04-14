# -*- coding: utf-8 -*-

import click
from cookiecutter import main as cookiecutter
from rogue.api.project.project import Github


def create():
    """Create a new project"""
    context = Github()
    print(context)
    print(context.get())
    print(context.project.template)
    cookiecutter.cookiecutter(
        template=context.project.template,
        extra_context=context.get(),
        output_dir='test',
        checkout="master",
        no_input=True
    )
