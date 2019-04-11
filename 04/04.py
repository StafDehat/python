#!/usr/bin/python

dividend = raw_input("Enter dividend: ")

for divisor in range(2,int(dividend)):
  if int(dividend) % divisor == 0:
    print divisor
  # End if
# End for
