from langconv import *
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
f = open(sys.argv[1],'r')
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    try:
        line = Converter('zh-hant').convert(line.decode('utf-8'))
        line = line.encode('utf-8')
        print line
    except:
        print line
        break
