#!/bin/python2

from parser import StringMath

print "Enter val:"
val = raw_input()

sm = StringMath(val)
print sm.eval()
