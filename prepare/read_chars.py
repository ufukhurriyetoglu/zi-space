#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs

chars = codecs.open("chars.txt", "r", 'utf-8')
data = chars.read().replace('\n', '')


import re
areas = [m.end() for m in re.finditer("\>\<FONT SIZE\=\+2>", data)]
list = codecs.open("simp_chars.txt", 'w', 'utf-8')
for i in xrange(len(areas)):
	list.write(data[areas[i]])
	list.write('\n')
