#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import urllib2

downjoyMainUrl = "http://money.downjoy.com/connectchannel/login.jsp"

resp = urllib2.urlopen(downjoyMainUrl)

html = resp.read().decode('utf-8').encode('gb2312')

print html

