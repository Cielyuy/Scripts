from genericpath import isfile
import os
dirList = [x for x in os.listdir(".") if os.path.isfile(x)]
print(dirList)
t1 = ".py"
t2 = '.code-workspace'
for i in dirList:
    if (t1 in i) or (t2 in i) :
        pass
    else:
        os.remove(i)

print(dirList)