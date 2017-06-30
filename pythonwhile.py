#!/usr/bin/python
# -*- coding: UTF-8 -*-


numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0 :
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
print str(even)
print str(odd)

var = 1
while var == 1 :
    num = raw_input("Enter a number :")
    print "You entered: ",num
print  "Good bye"