# -*- coding: utf-8 -*-

from server_service import ServerService

class BaseCurrency(object):
    @staticmethod
    def get():
        return 'RUR'

class ExchangeRates(object):
    def __init__(self, currency, day):
        self.__service = ServerService(day)
        self.__currency = currency

    def get_rate(self):
        if self.__currency == BaseCurrency.get():
            return 1

        return self.__service.get_cur_value(self.__currency)
