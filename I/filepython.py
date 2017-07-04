#!/usr/bin/python
# -*- coding: UTF-8 -*-




fo = open("shoucan.txt","wb")
print "文件名: ", fo.name
print "是否已关闭: ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
# print "文件大小 : ",

fo.close()

fo2 = open("shoucan.txt","r+")
str2 = fo2.read(5)
print "读取的字符串是 : ", str2
fo2.close()
