# -*- coding: utf-8 -*-

import os
import sys
import click
from cookiecutter import main as cookiecutter
from rogue.utilities import console


def is_valid(context):
    ok = True
    if 'template' not in context:
        ok = False
    if 'basedir' not in context:
        ok = False
    return ok


def list(path):
    return [el for el in os.listdir(path) if os.path.isdir(os.path.join(path, el, '.rogue'))]


def create(context={}):
    """Create a new project"""
    if not is_valid(context):
        console.error('No template defined')
        sys.exit(1)
    template = context["template"]
    cookiecutter.cookiecutter(
        template=template,
        extra_context=context,
        output_dir=context['basedir'],
        checkout="master",
        no_input=True
    )
