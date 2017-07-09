#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Classtest:
     def prt(self):
         print (self)
         print (self.__class__)
t = Classtest()
t.prt()