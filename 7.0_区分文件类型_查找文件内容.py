import os,re

# 获得当前目录
rootpath = os.getcwd()
# 打开 test 目录
filePath = '/test'
scan_dir = rootpath + filePath
# 获得具体路径
print("文件中包含“qytang”关键字的文件为:")
for i in os.listdir(scan_dir):
    temp = scan_dir +"/" + i 
    if os.path.isdir(temp):
        pass
    elif os.path.isfile(temp):
        for x in open(temp, "r"):
            if re.findall("qytang",x):
                print("{:>15s}".format(i))
            else:
                pass
    else:
        pass






# for i,j,k in os.walk(filePath):
#     # print(i,j,k)
#     if len(j) != 0:
#         for jj in k:
#             print(str(i)+ "/" + str(jj))
#     else:
#         print(i)   
#         # for jj in j:
#         #     print(j)
