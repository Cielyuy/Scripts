import shutil,os

abs = os.getcwd()

# Clip_Whole_Dir = os.path.abspath(os.getcwd())
Sim_Clip_Whole_Dir = os.path.abspath(os.path.dirname(os.getcwd()))
Clip_Whole_Dir = os.path.abspath(os.path.dirname(Sim_Clip_Whole_Dir))
dirList = [x for x in os.listdir('.')]
moveDir1 = []

clipName = '0819'

t1 = ".txt"
# t2 = '.code-workspace'
for i in dirList:
    # if (t1 in i) or (t2 in i) :
    if (t1 in i) :
        # pass
        a = os.path.join(abs,i)
        b = os.path.join(Clip_Whole_Dir,"TONGBU/CI",i)
        moveDir1.append(a,b)
    else:
        # os.remove(i)
        pass

# a = 1
