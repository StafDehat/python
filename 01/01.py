#!/usr/bin/python

# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import datetime

name = raw_input("Name: ")  
age = raw_input("Age: ")
now = datetime.datetime.now()

print name + " will turn 100 in the year " + str(now.year - int(age) + 100)


