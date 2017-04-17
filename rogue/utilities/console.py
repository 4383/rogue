# -*- coding: utf-8 -*-


import click
from terminaltables import AsciiTable
from terminaltables import SingleTable

TableObject = SingleTable


def error(message):
    click.echo(click.style(message, "red"))


def success(message):
    click.echo(click.style(message, "green"))


def info(message):
    click.echo(click.style(message, "blue"))


def underline(color="white"):
    click.echo(click.style("____________", color))


def show_config(config):
    for section in config.sections():
        table_data = [['option', 'value']]
        for option in config[section]:
            table_data.append([option, config[section][option]])
        table = TableObject(table_data)
        table.title = " " + section + " "
        print(table.table)


def show_list(data, headers, title):
    show_table(data, headers, title)


def show_table(data, headers, title):
    table_data = [headers]
    for el in data:
        table_data.append(el)
    table = TableObject(table_data)
    table.title = " " + title + " "
    print(table.table)
