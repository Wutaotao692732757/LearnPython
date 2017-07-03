#!/usr/bin/python
# -*- coding: UTF-8 -*-

import support

support.print_func("something good")


Money = 2000
def AddMoney():
    global Money
    Money = Money + 1

print Money
AddMoney()
print Money;