# -*- coding: utf-8 -*-

import click
from cookiecutter import main as cookiecutter


default_template = 'https://github.com/audreyr/cookiecutter-pypackage'


def create(context={}):
    """Create a new project"""
    if not context['template']:
        context['template'] = default_template
    cookiecutter.cookiecutter(
        template=context.['template'],
        extra_context=context,
        output_dir='test',
        checkout="master",
        no_input=True
    )
