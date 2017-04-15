import os
import rogue.api.config.file as configfile


def store(config, project_path):
    print(project_path)
    if not os.path.isdir(project_path):
        return False
    rogue_instance = os.path.join(project_path, '.rogue')
    print(rogue_instance)
    os.makedirs(rogue_instance)
    configfile.write(config, os.path.join(rogue_instance, '.rogue.cfg'))
