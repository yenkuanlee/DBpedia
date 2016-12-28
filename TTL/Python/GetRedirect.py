import sys
EIdict = dict()
f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line : break
    line = line.replace("\n","")
    tmp = line.split("\t")
    if len(tmp) != 2:continue
    EIdict[tmp[0]] = tmp[1]

f2 = open(sys.argv[2],'r')
while True:
    line = f2.readline()
    if not line:break
    tmp = line.split(" ")
    if len(tmp) != 4:continue
    if tmp[0] in EIdict and tmp[2] not in EIdict:
        EIdict[tmp[2]] = EIdict[tmp[0]]
    elif tmp[2] in EIdict and tmp[0] not in EIdict:
        EIdict[tmp[0]] = EIdict[tmp[2]]

for x in EIdict:
    print x+"\t"+EIdict[x]
