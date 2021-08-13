import xlrd

data = xlrd.open_workbook(r'F:\FangZhen\Script\testExcel\test1.xlsx')#文件名以及路径，如果路径或者文件名有中文给前面加一个 r

#
table = data.sheets()[0]
name = data.sheet_names()
print (name)

nrows = table.nrows
print(nrows)
listRow = table.row(rowx)
#table = data.sheet_by_index(sheet_index)
