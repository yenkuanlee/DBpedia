import sys
f = open(sys.argv[1],'r')
Eset = set()
while True:
    line = f.readline()
    if not line:break
    entity = line.split("\t")[0]
    if entity not in Eset:
        print entity
        Eset.add(entity)

