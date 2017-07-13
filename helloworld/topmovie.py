#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import re


pre_url = 'http://movie.douban.com/top250?start='

top_urls = []

for num in range(4):
    top_urls.append(pre_url + str(num * 25))

top_content = []
top_tag = re.compile(r'<span class="title">(.+?)</span>')

for url in top_urls:
    content = urllib2.urlopen(url).read()
    pre_content = re.findall(top_tag, content)

    for item in pre_content:
        if item.find(' ') == -1:
            top_content.append(item)

top_num = 1
for item in top_content:
    print 'Top' + str(top_num) + '  ' + item
    top_num +=1

