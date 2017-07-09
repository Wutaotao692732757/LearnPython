#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

line = "Cats are smarter than dogs";

matchObj = re.match(r'dogs',line,re.M|re.I)

if matchObj:
    print "match --> matchObj.group() : ",matchObj.group()
else:
    print "No match!!"

matchObj2 = re.search(r'dogs',line, re.M|re.I)

if matchObj2:
    print "search --> matchObj2.group() : ", matchObj2.group()
else:
    print "NO match!!"

phone = "2004-959-559 #ssdadsada"

# 删除字符串中的Python 注释

num = re.sub(r'#.*$',"",phone)
print "电话号码是: ",num

num2 = re.sub(r'\D',"",phone)
print "处理后的电话是: ",num2