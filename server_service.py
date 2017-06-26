# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re

class ServerService(object):
    SITE_BASE = 'https://www.cbr.ru/currency_base/daily.aspx?date_req='
    def __init__(self, modifier):
        response = requests.get(self.SITE_BASE + modifier)
        self.__soup = BeautifulSoup(response.text, 'lxml')

    def get_currencies(self):
        curs = []
        for data in self.__soup.find(attrs={'class' : 'data'}):
            for string in data:
                cur = re.search('[A-Z]{3}', unicode(string))
                if cur is not None:
                    curs.append(cur.group(0))

        return curs

    def get_cur_value(self, cur):
        data = self.__soup.find_all('tr')
        for strings in data:
            c = re.search('<td>' + cur + '</td>', unicode(strings))
            if c is None:
                continue

            for str in strings.find_all('td'):
                cur_val = re.search('\d+\,\d\d\d\d', unicode(str))
                if cur_val is not None:
                    return re.sub(',', '.', cur_val.group(0))

        return None
