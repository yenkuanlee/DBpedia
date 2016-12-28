# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
Bset = ["（"]
f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    tmp = line.split("\t")
    try:
        tmpp = tmp[0].split("\"")
        if len(tmpp) != 3:continue
        #for x in Bset:
        #    if x in tmpp[1]:continue
        if "(" in tmpp[1] or "（" in tmpp[1] or "“" in tmpp[1] or "{" in tmpp[1] or "/" in tmpp[1]:continue
        if "·" in tmpp[1] : continue
        elif "：" in tmpp[1] : continue
        elif "?" in tmpp[1] : continue
        elif ":" in tmpp[1] : continue

        if "," in tmpp[1]:
            tmppp = tmpp[1].split(",")
            for x in tmppp:
                print x+"\t"+tmp[1]
            continue
        elif "、" in tmpp[1]:
            tmppp = tmpp[1].split("、")
            for x in tmppp:
                print x+"\t"+tmp[1]
            continue
        elif "，" in tmpp[1]:
            tmppp = tmpp[1].split("，")
            for x in tmppp:
                print x+"\t"+tmp[1]
            continue
        print tmpp[1]+"\t"+tmp[1]
    except:
        pass
