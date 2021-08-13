import shutil, os, sys


def listGet(a, b, c):
    numList = list()
    if (b - a) % c == 0:
        d = (b - a) / c
        i = 0
        while i <= d:
            numList.append(a + i * c)
            i = i + 1

    else:
        d = (b - a) / c
        i = 0
        while i <= d:
            numList.append(a + i * c)
            i = i + 1

        numList.append(b)

    return numList


# 前缀命名
VelocityOrPressure = False

FirstPara = -5000  ##################################

LastPara = -1000  ##################################

CountNum = 500

varNum = 85

catchList = listGet(FirstPara, LastPara, CountNum)

for j in catchList:
    print(j)

#for i in catchList:
    




absoluteDir = os.getcwd() + "\\"  #############         地址命名    ###############
Clip_Whole_Dir = os.path.abspath(os.path.dirname(os.getcwd())) + "\\"


Mesh_num_preffix = 'M100L_'

Mesh_load_dir_preffix = 'basic_Mesh'+'\\'
MeshName = 'M0720_100_long.msh'
Mesh_Load_Dir = Clip_Whole_Dir+Mesh_load_dir_preffix + MeshName

Specified_Dir_preffix_1 = "task"+"\\" +"0720" + "\\"  ###########!!!!!!!!!!
Specified_Dir_preffix_2 = 'V' + '_'  ###########!!!!!!!!!!!
#Specified_Dir = Specified_Dir_preffix_1 + Specified_Dir_preffix_2 + str(count_Total_Clip_Number) + '/'
Specified_Dir = Specified_Dir_preffix_1 + Specified_Dir_preffix_2+str(varNum)+ '\\'  ###############指定储存复制文件的特定文佳夹
if os.path.exists(Clip_Whole_Dir+Specified_Dir):
    pass
else:
    os.makedirs(Clip_Whole_Dir+Specified_Dir)

#清除之前生成的文件
print(os.getcwd())
#for files in os.listdir(os.getcwd()):
for files in os.listdir(Clip_Whole_Dir+Specified_Dir):
    if files.endswith(".bat"):
        os.remove(os.path.join(Clip_Whole_Dir+Specified_Dir, files))

for files in os.listdir(Clip_Whole_Dir+Specified_Dir):
    if files.endswith(".jou"):
        os.remove(os.path.join(Clip_Whole_Dir+Specified_Dir, files))

for files in os.listdir(Clip_Whole_Dir+Specified_Dir):
    if files.endswith(".cse"):
        os.remove(os.path.join(Clip_Whole_Dir+Specified_Dir, files))



Stored_Example_J_Name = 'Example_J.jou'
Stored_Example_J_middle_dir = 'basic_Mesh' + '\\'
Stored_Example_J_Dir = Clip_Whole_Dir + Stored_Example_J_middle_dir + Stored_Example_J_Name

Stored_Example_C_Name = 'Example_C.cse'
Stored_Example_C_middle_dir = 'basic_Mesh' + '\\'
Stored_Example_C_Dir = Clip_Whole_Dir + Stored_Example_C_middle_dir + Stored_Example_C_Name

B_J_middle_name_preffix = 'J_' + Mesh_num_preffix + str(varNum) + '_'
B_C_middle_name_preffix = 'C_' + Mesh_num_preffix + str(varNum) + '_'


B_J_Content_Preffix = 'call fluent 3ddp -t8 -g -wait -i '
B_C_Content_Preffix = "call cfdpost -batch "

# bat文件 和 cse文件
B_J_Name = 'BF_' + Mesh_num_preffix + str(FirstPara) + "_" + str(varNum) + ".bat"
B_J_Dir = Clip_Whole_Dir + Specified_Dir + B_J_Name
B_C_Name = 'BP_' + Mesh_num_preffix + str(FirstPara) + "_" + str(varNum) + ".bat"
B_C_Dir = Clip_Whole_Dir + Specified_Dir + B_C_Name


# 清除原先有的bat文件
