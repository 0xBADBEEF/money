# -*- coding: utf-8 -*-

import sqlite3

class Storage(object):
    DB_FILE = ":memory:"
    CREATE = "CREATE TABLE "
    INSERT = "INSERT INTO "
    VALS = " VALUES "
    SELECT_ALL = "SELECT * FROM "
    WHERE = " WHERE "

    def __init__(self):
        self.conn = sqlite3.connect(self.DB_FILE)
        self.c = self.conn.cursor()

    # args - array of typles (field name, type)
    def create_table(self, name, *args):
        pass

    # args - array of arguments to insert
    def insert(self, table, *args):
        pass

    # array - array of typles to insert
    def insert_array(self, table, array):
        pass

    def select_all(self, table):
        pass

    # params - array of typles (field name, field value)
    def select(self, table, *params):
        pass

    # TODO Try to remove it
    def close(self):
        self.conn.close()
