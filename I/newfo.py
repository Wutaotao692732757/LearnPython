#!/usr/bin/python
# -*- coding: UTF-8 -*-


fo = open("test2.txt","r+")

str0 = fo.name;
print "读取的文件名字是:",str0

str = fo.read(10);

print "读取的字符串是 : ",str

position = fo.tell();
print "当前文件位置 : ", position

position = fo.seek(0,0);

str2 = fo.read(3);
print "重新读取字符串 : ", str2

fo.close()


