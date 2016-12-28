# -*- coding: utf-8 -*-
import sys
f = open(sys.argv[1],'r')
Iset = set()
while True:
    line = f.readline()
    if not line:
        break
    tmp = line.split(" ")
    if len(tmp) != 4 : continue
    try:
        entity = tmp[0]
        #entity = tmp[0].split("http://zh.dbpedia.org/resource/")[1].split(">")[0]
        if entity in Iset:
            continue
        else:
            #print entity
            if tmp[1]=="<http://zh.dbpedia.org/property/姓名>" or tmp[1]=="<http://zh.dbpedia.org/property/name>":
                Iset.add(entity)
    except:
        pass

f2 = open(sys.argv[2],'r')
while True:
    line = f2.readline()
    if not line:break
    tmp = line.split(" ")
    if len(tmp) != 4 : continue
    if tmp[0] not in Iset:continue
    Wid = tmp[2].split("\"")[1]
    print tmp[0]+"\t"+Wid
