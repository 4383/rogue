# -*- coding: utf-8 -*-

import os
import sqlite3


BASE_PATH = os.path.dirname(__file__)
USER_PATH = os.path.expanduser('~')
TODO_PATH = os.path.join(USER_PATH, '.rogue')
DATABASE_PATH = os.path.join(TODO_PATH, 'todo.db')


def sort(tasks):
    sorted_tasks = {
        'hight': [],
        'low': [],
        'normal': []
    }
    for el in tasks:
        priority = humanize(el[5])
        sorted_tasks[priority].append(el)
    return sorted_tasks


def convert_for_database(priority):
    binding = {'hight': 'H', 'low': 'L', 'normal': 'N'}
    return binding[priority]


def humanize(priority):
    binding = {'H': 'hight', 'L': 'low', 'N': 'normal'}
    return binding[priority]


class Todo():

    connection = None
    cursor = None

    def __init__(self):
        if not self.__can_store():
            self.__connect()
            self.__initialize()
        else:
            self.__connect()

    def __del__(self):
        self.__disconnect()

    def __connect(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.connection.cursor()

    def __disconnect(self):
        self.connection.close()

    def __can_store(self):
        if not os.path.isfile(DATABASE_PATH):
            return False
        return True

    def __initialize(self):
        if not os.path.isdir(TODO_PATH):
            os.makedirs(TODO_PATH)

        self.cursor.execute('''
            CREATE TABLE tasks
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                finished_at DATETIME,
                active BOOLEAN DEFAULT 1 CHECK (active IN (0, 1)),
                priority TEXT DEFAULT 'N' CHECK (priority IN ('H', 'L', 'N'))
            )
        ''')
        self.connection.commit()

    def add(self, task, priority):
        self.cursor.execute('''
            INSERT INTO tasks (content, priority) VALUES (?, ?)
        '''
        , [task, convert_for_database(priority)])
        self.connection.commit()

    def ls(self, active=False):
        return self.cursor.execute('''
            SELECT * FROM tasks
        ''')


    def info(self, identifiers):
        request = '''
            SELECT * FROM tasks WHERE id IN ({})
        '''.format(','.join(['?']*len(identifiers)))
        return self.cursor.execute(request, identifiers)

    def done(self, identifier):
        self.cursor.execute('''
            UPDATE tasks SET
                active = 0
            WHERE id=?
        ''', [identifier])
        self.connection.commit()

    def delete(self, identifier):
        self.cursor.execute('''
            DELETE FROM tasks
            WHERE id=?
        ''', [identifier])
        self.connection.commit()

