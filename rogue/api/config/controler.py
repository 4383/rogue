import configparser
from rogue.api.config import file as configfile
from terminaltables import AsciiTable


def read(cfgfile):
    cfg = configfile.read(cfgfile)
    table_data = [['sections']]
    for section in cfg.sections():
        table_data.append([section])
    table = AsciiTable(table_data)
    print(table.table)


def add(path, options):
    cfg = configfile.read(path)
    section, key = options[0].split('.')
    value = options[1]
    if section not in cfg.sections():
        cfg.add_section(section)
    cfg.set(section, key, value)
    configfile.write(cfg, path)


def initialize(cfgfile):
    cfg = configparser.ConfigParser()
    configfile.write(cfg, cfgfile)
