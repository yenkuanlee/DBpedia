# -*- coding: utf-8 -*-
import sys
f = open(sys.argv[1],'r')
# EntityId_which_has_infobox_with_name.txt
IdDict = dict()
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    tmp = line.split("\t")
    IdDict[tmp[0]] = tmp[1]

f2 = open(sys.argv[2],'r')
# Entity_NameAndNickName.txt
while True:
    line = f2.readline()
    if not line:break
    line = line.replace("\n","")
    tmp = line.split("\t")
    try:
        print tmp[1]+"\t"+IdDict[tmp[0]]
    except:
        pass
