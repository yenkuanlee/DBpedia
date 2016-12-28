# -*- coding: utf-8 -*-
import sys
edge = "http://zh.dbpedia.org/property/"
target = ['姓名','绰号','name','nickname']
Eset = set()
for x in target:
    Eset.add("<"+edge+x+">")

f = open(sys.argv[1],'r')
# infobox
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    tmp = line.split(" ")
    if len(tmp) !=4 : continue
    if tmp[1] in Eset and "@zh" in tmp[2]:
        print tmp[0]+"\t"+tmp[2]
