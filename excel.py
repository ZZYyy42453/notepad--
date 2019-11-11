import xlrd, xlsxwriter

# 待合并的excel文件
allxls = ["C:\\Users\\zy\\Desktop\\a1.xlsx",
          "C:\\Users\\zy\\Desktop\\a2.xlsx"
          ]
# 目标excel文件
end_xls = "C:\\Users\\zy\\Desktop\\a3.xlsx"


def open_xls(file):
    try:
        fh = xlrd.open_workbook(file)
        return fh
    except Exception as e:
        print("打开文件错误!" + e)


'''
sheet表格数量,fh列表变量
fh=open_xls(allxls[0]).sheets()
print(fh)
'''


# 获取文件
def get_file_value(filename, sheetnum):
    rvalue = []
    fh = open_xls(filename)
    sheet = fh.sheets()[sheetnum]
    row_num = sheet.nrows
    # print(row_num)
    for rownum in range(0, row_num):
        rvalue.append(sheet.row_values(rownum))
    return rvalue


'''
#获取文件某个sheet下的内容
fh=get_file_value(allxls[0],1) 
print(fh)
'''

first_file_fh = open_xls(allxls[0])
first_file_sheet = first_file_fh.sheets()
first_file_sheet_num = len(first_file_sheet)
sheet_name = []
for sheetname in first_file_sheet:
    sheet_name.append(sheetname.name)

end_xls = xlsxwriter.Workbook(end_xls)
# 所有值
all_sheet_value = []

for sheet_num in range(0, first_file_sheet_num):
    all_sheet_value.append([])
    for file_name in allxls:
        print("正在读取" + file_name + "的第" + str(sheet_num + 1) + "个标签...")
        try:
            file_value = get_file_value(file_name, sheet_num)
            all_sheet_value[sheet_num].append(file_value)
        except Exception as err:
            print(file_name + "无第" + str(sheet_num + 1) + "个标签.")

# print(all_sheet_value)

num = -1

sheet_index = -1

# 写入数据
for sheet in all_sheet_value:
    sheet_index += 1
    end_xls.sheet = end_xls.add_worksheet(sheet_name[sheet_index])
    num += 1
    num1 = -1
    for sheet1 in sheet:
        for sheet2 in sheet1:
            num1 += 1
            num2 = -1
            for sheet3 in sheet2:
                num2 += 1
                end_xls.sheet.write(num1, num2, sheet3)

end_xls.close()