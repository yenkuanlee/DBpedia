import sys
reload(sys)
sys.setdefaultencoding('utf-8')
f = open(sys.argv[1],'r')

cnt = 0
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    tmp = line.split("\t")
    print tmp[0]+"\t"+str(len(tmp[0]))
    if cnt > 10:break
    cnt += 1
