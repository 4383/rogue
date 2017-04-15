# -*- coding: utf-8 -*-


import click
from terminaltables import AsciiTable


def error(message):
    click.echo(click.style(message, "red"))


def info(message):
    click.echo(click.style(message, "green"))


def underline(color="white"):
    click.echo(click.style("____________", color))


def show_config(config):
    for section in config.sections():
        table_data = [['option', 'value']]
        for option in config[section]:
            table_data.append([option, config[section][option]])
        table = AsciiTable(table_data)
        table.title = " " + section + " "
        print(table.table)
