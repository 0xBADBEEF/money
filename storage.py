# -*- coding: utf-8 -*-

import sqlite3

class Storage(object):
    DB_FILE = ":memory:"
    CREATE = "CREATE TABLE "
    INSERT = "INSERT INTO "
    VALS = " VALUES "
    SELECT_ALL = "SELECT * FROM "
    WHERE = " WHERE "
    AND = " AND "

    def __init__(self):
        self.conn = sqlite3.connect(self.DB_FILE)
        self.c = self.conn.cursor()

    # args - array of typles (field name, type)
    def create_table(self, name, *args):
        cmd = self.CREATE + name + ' ('
        add_comma = False
        for item in args:
            if add_comma is True:
                cmd += ', '
            cmd += item[0] + ' ' + item[1]
            add_comma = True
        cmd += ');'
        self.c.execute(cmd)

    # args - array of arguments to insert
    def insert(self, table, *args):
        cmd = self.INSERT + table + self.VALS + '('
        add_comma = False
        for item in args:
            if add_comma is True:
                cmd += ', '
            cmd += "'" + str(item) + "'"
            add_comma = True
        cmd += ');'
        self.c.execute(cmd)

    # array - array of typles to insert
    def insert_array(self, table, array):
        pass

    def select_all(self, table):
        cmd = self.SELECT_ALL + table
        return self.c.execute(cmd)

    # params - array of typles (field name, field value)
    def select_and(self, table, *params):
        cmd = self.SELECT_ALL + table + self.WHERE
        add_and = False
        for item in params:
            if add_and is True:
                cmd += self.AND
            cmd += item[0] + " = '" + item[1] + "'"
            add_and = True
        cmd += ';'
        return self.c.execute(cmd)

    # TODO Try to remove it
    def close(self):
        self.conn.close()
