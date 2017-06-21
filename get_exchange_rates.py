# -*- coding: utf-8 -*-
import requests
import re
from lxml import html

class ExchangeRates(object):
    def __init__(self, currency):
        self.__currency = currency

    def __get_html_tree(self):
        page = requests.get("http://www.banki.ru/products/currency/cb/")
        tree = html.fromstring(page.content)

        return tree

    def __get_cur_val(self, tree):
        data = tree.xpath('.//tr[@data-currency-code="' + self.__currency
                          + '"]//*[local-name()="td"]/text()')
        for item in data:
            cur_val = re.search('\d+\.\d\d\d\d', item)
            if cur_val is not None:
                return cur_val.group(0)
        return None

    def get_currency(self):
       tree = self.__get_html_tree()
       cur_val = self.__get_cur_val(tree)

       return cur_val
