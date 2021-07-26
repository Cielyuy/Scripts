# def add(x, lst=[1,2,3]):
#     if x not in lst:
#         lst.append(x)
#
#     return lst
#
# def main():
#     list1 = add(1)
#     print(list1)
#
#     list2 = add(2)
#     print(list2)
#
#     list3 = add(3, [11, 12, 13, 14])
#     print(list3)
#
#     list4 = add(4)
#     print(list4)
#
# main()

def devideSqueue(num, list=[]):
    # list_Div[][]= None
    # i = 0
    shang = len(list) // num
    yu = len(list) % num
    list_Div = []

    # for i in range(num):
    #     list_Div.append([])

    if len(list) <= num:
        for i in range(len(list)):
            list_Div.append(list[i])

        print('single squeu')
        # return list_Div
    else:
        # shang = len(list) // (num - 1)
        # yu = len(list) % (num - 1)
        k = -1
        for i in range(0, len(list)):
            if yu == 0:
                if i % shang == 0:
                    list_Div.append([])
                    k = k + 1
                    # list_Div.append([])
                    list_Div[k].append(list[i])
                else:
                    list_Div[k].append(list[i])

            elif k < yu & yu != 0:
                if i % (shang + 1) == 0:
                    list_Div.append([])
                    k = k + 1
                    # list_Div.append([])
                    list_Div[k].append(list[i])
                else:
                    list_Div[k].append(list[i])


            elif ((i - yu * (shang + 1)) % shang) == 0:
                list_Div.append([])
                k = k + 1
                list_Div[k].append(list[i])
            else:
                list_Div[k].append(list[i])


    return list_Div

    #


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 13, 23, 354, 545, 2323, 32, 234342, 234234, 343234, 45245, 7356, 36254, 7635, 36563,
     413414, 134134]
b = 4
print(len(a))
c = devideSqueue(b, a)
# print(len(c))
# print(len(c[2]))
#
#print (len(c[5]))
# for i2 in range(len(c[0])):
#     print(c[0][i2])

for i1 in range(len(c)):
    print (c[i1])


