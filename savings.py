# -*- coding: utf-8 -*-

import datetime
from storage import Storage

class Savings(object):
    TABLE_NAME = "Savings"
    AMOUNT = ('amount', 'decimal(18, 4)')
    START_DATE = ('start_date', 'date')
    END_DATE = ('end_date', 'date')
    RATE = ('rate', 'decimal(3,4)')
    PAY_DAY = ('pay_day', 'tinyint')
    CAPITALIZED = ('cap', 'tinyint')

    def __init__(self):
        self.__storage = Storage()
        self.__is_db = False #TODO REMOVE!!!

    def create(self, amount, start, end, rate, payday, capitalized):
        if self.__is_db is False:
            self.__storage.create_table('Savings', ('amount', 'decimal(18, 4)'), ('start_date', 'date'), ('end_date', 'date'), ('rate', 'decimal(3,4)'), ('pay_day', 'smallint'), ('cap', 'tinyint'))
            self.__is_db = True

        #TODO Add check for existance and table creation!
        self.__storage.insert(self.TABLE_NAME, float(amount), start, end, float(rate), int(payday), int(capitalized))

    def get_all(self):
        return self.__storage.select_all(self.TABLE_NAME)

    def get_saves_today(self):
        all_saves = self.get_all()
        today = datetime.date.today()
        for save in all_saves:
            sd = datetime.datetime.strptime(save[1], '%Y-%m-%d')
            delta = today - sd.date()
