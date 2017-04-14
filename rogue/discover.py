# -*- coding: utf-8 -*-

import os
import click
from cookiecutter import repository


plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')

class MyCLI(click.MultiCommand):

    def list_commands(self):
        print("list")
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py'):
                rv.append(filename[:-3])
        print(rv)
        rv.sort()
        return rv

    def get_command(self, name):
        print("run")
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']

cli = MyCLI(help='This tool\'s subcommands are loaded from a '
            'plugin folder dynamically.')


def main():
    print(plugin_folder)
    cli = MyCLI(help='This tool\'s subcommands are loaded from a '
            'plugin folder dynamically.')
    cli.list_commands()
    #cli()


if __name__ == '__main__':
    cli()
