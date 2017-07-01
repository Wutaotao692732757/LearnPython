#!/usr/bin/python
# -*- coding: UTF-8 -*-


def printme ( str ):
    print str
    return

printme("我要挑用用户自定义函数!");
printme("再次调用同一个珊瑚颂");



def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print  b


def changeme ( mylist ):

    print "函数内取值: ", mylist
    mylist.append([1,2,3,4]);

    return

mylist = [10,20,30];
changeme( mylist );
print "函数外取值: ", mylist

def printlogme( str ):

    print  str;
    return ;

printlogme( str = "MY string");


def printinfo(name, age):
    print "Name: ", name;
    print "Age ",age;
    return ;

printinfo(age=50, name="miki");


def printinfo(name, age = 35):
    print "Name: ", name;
    print "Age ", age;
    return ;

printinfo(age=50, name="miki");
printinfo(name="jack");

def printinfo2(arg1, *vartuple):
    print "输出: "
    print arg1
    for var in vartuple:
        print  var
    return ;

printinfo2( 10 );
printinfo2( 70, 60, 50);


sum = lambda arg1, arg2: arg1 + arg2;

print  "相加后的值为 : ", sum(10, 20)
print  "相加后的值为 : ", sum( 20, 20)


sum2 = lambda arg1, arg2: arg1*arg2;

print "相乘后的值为 : ", sum2(20,30)
print "相乘后的值为2 :",sum2(30,30)


def sumtotal(arg1, arg2):
    total = arg1 + arg2
    print  "函数内 : 0",total
    return total;

print "total函数的值为 : ", sumtotal(90,90)






