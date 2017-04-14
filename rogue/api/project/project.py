# -*- coding: utf-8 -*-


class Author():
    """Author representation"""

    def __init__(self):
        self.name = "hervé"
        self.email = "herveberaud.pro@gmail.com"


class Repos():
    """Repository representation"""

    def __init__(self):
        self.github = "4383"
        self.pypi = "4383"
        self.gitlab = "hberaud"


class Project():
    """Project representation"""

    def __init__(self):
        self.name = "test9"
        self.description = "projet test 8"
        self.template ='https://github.com/audreyr/cookiecutter-pypackage'


class Context():
    """Context representation"""

    def __init__(self):
        self.configure()

    def configure(self):
        self.get_author()
        self.get_repos()
        self.get_project()

    def get_project(self):
        self.project = Project()

    def get_repos(self):
        self.repos = Repos()

    def get_author(self):
        self.author = Author()

    def get(self):
        return {
            "project_name": self.project.name,
            "github_username": self.repos.github,
        }


class Github(Context):

    def get_repos(self):
        self.repos = Repos()
        self.repos.github = "ohyeah"
