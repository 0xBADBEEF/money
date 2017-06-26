# -*- coding: utf-8 -*-

import string
from exchange import *
from server_service import ServerService

class WrongCurrency(Exception):
    pass

class Parser(object):
    def __init__(self, str):
        service = ServerService()
        curs = service.get_currencies()
        s = str.split()
        cur = self.__prepare_cur(s[1])
        if cur != BaseCurrency.get() and cur not in curs:
            raise WrongCurrency

        self.__val = float(s[0])
        self.__cur = cur

    def __prepare_cur(self, str):
        return str.upper()

    def get_currency(self):
        return self.__cur

    def get_nominal(self):
        return self.__val

class StringMath(object):
    def __init__(self, str):
        self.__ops = []
        cur_str = ''
        cur_op = '+'
        for symbol in str:
            if symbol == '+' or symbol == '-':
                p = Parser(cur_str)
                er = ExchangeRates(p.get_currency())
                op = (cur_op, float(er.get_rate()) * p.get_nominal())
                self.__ops.append(op)
                cur_str = ''
                cur_op = symbol
                continue
            cur_str += symbol

        p = Parser(cur_str)
        er = ExchangeRates(p.get_currency())
        op = (cur_op, float(er.get_rate()) * p.get_nominal())
        self.__ops.append(op)

    def eval(self):
        res = 0
        for ops in self.__ops:
            if ops[0] == '+':
                res += ops[1]
            elif ops[0] == '-':
                res -= ops[1]

        return res
