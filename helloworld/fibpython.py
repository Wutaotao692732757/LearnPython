#!/usr/bin/python
# -*- coding: UTF-8 -*-


def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b

    return a

print fib(10)

