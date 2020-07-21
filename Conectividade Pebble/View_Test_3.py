import psutil


f = open('UsedMem.txt', 'w')
f.write(str(psutil.virtual_memory().used))
f.close()



