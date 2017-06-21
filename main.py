#!/bin/python2

from get_exchange_rates import ExchangeRates


print "Enter currency:"
cur = raw_input()
cur = cur.upper()

er = ExchangeRates(cur)
print er.get_currency()
