#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib
import re

import urllib2

post_param = {'action':'','start':'0','limit':'1'}

return_data = re.get("https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90",data =post_param, verify = False)


print return_data.text