# -*- coding: utf-8 -*-

import click
from cookiecutter import main as cookiecutter


def create(context):
    """Create a new project"""
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
