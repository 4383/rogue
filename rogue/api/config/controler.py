import configparser
from rogue.api.config import file as configfile


def read(cfgfile):
    return configfile.read(cfgfile)


def add(path, options):
    cfg = configfile.read(path)
    section, key = options[0].split('.')
    value = options[1]
    if section not in cfg.sections():
        cfg.add_section(section)
    cfg.set(section, key, value)
    configfile.write(cfg, path)


def default():
    cfg = configparser.ConfigParser()
    cfg.read_dict({'default_project': {
        "full_name": "Hervé Beraud",
        "email": "herveberaud.pro@gmail.com",
        "github_username": "4383",
        "project_name": "package",
        "project_slug": "package",
        "project_short_description": "Python package.",
        "pypi_username": "4383",
        "version": "0.1.0",
        "use_pytest": "n",
        "use_pypi_deployment_with_travis": "y",
        "command_line_interface": "Click",
        "create_author_file": "y",
        "open_source_license": "MIT",
        "template": "https://github.com/audreyr/cookiecutter-pypackage",
        "basedir": "/home/herve/dev"
        }})
    return cfg


def initialize(cfgfile):
    cfg = default()
    configfile.write(cfg, cfgfile)
