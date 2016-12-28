# -*- coding: utf-8 -*-
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')
f = codecs.open(sys.argv[1],"r","utf-8")
while True:
	line = f.readline()
	if not line:break
	line = line.replace("\n","")
	tmp = line.split("\t")
	#print tmp[0]+"\t"+str(len(tmp[0]))
	if len(tmp[0]) > 5 or len(tmp[0]) <2:continue
	print line
