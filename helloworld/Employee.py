#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:

   empCount = 0

   def __init__(self, name, salary):
       self.name = name
       self.salary = salary
       Employee.empCount += 1

   def displayCount(self):
       print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
       print "Name : ", self.name,  ", Salary: ", self.salary



emp1 = Employee("Zara",2000)
emp2 = Employee("Manni",5000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee %d" % Employee.empCount


emp1.age = 7
emp1.age = 8

hasattr(emp1, 'age')
getattr(emp1, 'age')
setattr(emp1, 'age', 8)
delattr(emp1, 'age')



















