# -*- coding: utf-8 -*-


import click


def info(message):
    click.echo(click.style(message, "green"))


def underline(color="white"):
    click.echo(click.style("____________", color))
