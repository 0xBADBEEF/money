#!/bin/python2

from parser import *
from exchange import ExchangeRates
from storage import Storage
import string

s = Storage()

print "Enter val:"
val = raw_input()

sm = StringMath(val)
print sm.eval()

print "Enter nominal, currency and date in fmt (DD.MM.YYYY):"
str = raw_input()
data = str.split()

p = Parser(data[0] + ' ' + data[1], data[2])
er = ExchangeRates(p.get_currency(), data[2])
print float(er.get_rate()) * p.get_nominal()
