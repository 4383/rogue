from rogue.api.config import file as configfile


def add(path, options):
        cfg = configfile.read(path)
        section, key = options[0].split('.')
        value = options[1]
        if section not in cfg.sections():
            cfg.add_section(section)

        cfg.set(section, key, value)
        configfile.write(cfg, path)
