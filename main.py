#!/bin/python2

from parser import *
from exchange import ExchangeRates
from savings import Savings
import string

save = Savings()
save.create('80000', '2017-03-12', '2018-03-11', '8.5', '12', True)
save.create('80000', '2017-08-14', '2018-03-11', '8.5', '12', False)
items = save.get_all()
for i in items:
    print i
save.get_saves_today()


#s.create_table('test_table', ('name', 'text'), ('second', 'text'))
#s.insert('test_table', 'some_name1', 'is_second1')
#s.insert('test_table', 'some_name2', 'is_second2')
#s.insert('test_table', 'some_name3', 'is_second3')
#s.insert('test_table', 'some_name3', 'is_second4')
#items = s.select_all('test_table')
#for i in items:
#    print i
#items = s.select_and('test_table', ('name', 'some_name3'), ('second', 'is_second4'))
#for i in items:
#    print i

#print "Enter val:"
#val = raw_input()
#
#sm = StringMath(val)
#print sm.eval()
#
#print "Enter nominal, currency and date in fmt (DD.MM.YYYY):"
#str = raw_input()
#data = str.split()
#
#p = Parser(data[0] + ' ' + data[1], data[2])
#er = ExchangeRates(p.get_currency(), data[2])
#print float(er.get_rate()) * p.get_nominal()
