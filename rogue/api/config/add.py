def add(path, options):
    print("add")
    print(path)
    with open(path, "w+") as config:
        config.write(str(options))
