import configparser

def read(configfile):
    config = configparser.ConfigParser()
    config.read(configfile)
    return config


def write(config, cfgfile):
    with open(cfgfile, "w+") as configfile:
        config.write(configfile)
