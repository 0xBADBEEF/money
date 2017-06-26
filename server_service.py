# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

class ServerService(object):
    def __init__(self):
        response = requests.get('http://www.banki.ru/products/currency/cb/')
        self.__soup = BeautifulSoup(response.text, 'lxml')

    def get_currencies(self):
        curs = []
        for string in self.__soup.find_all(attrs={'data-currency-code' : True}):
            curs.append(string.get('data-currency-code'))
        return curs

    def get_cur_value(self, cur):
        for string in self.__soup.find_all(attrs={'data-currency-code' : cur}):
            cur_val = re.search('\d+\.\d\d\d\d', string.text)
            if cur_val is not None:
                return cur_val.group(0)
        return None
