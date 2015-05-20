import sys
import os 
import re
def search():
	file = open('out.txt','r')
	txt = file.read()
	a = raw_input(u'请输入中文字符')
	b = a.decode('gb2312').encode('utf8')
	p = re.compile(r'=(%s)=(.*)' %b)
	print p.search(txt).group(2)