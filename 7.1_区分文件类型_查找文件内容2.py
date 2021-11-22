import os,re

"""
常用的几个os函数：
1，os.getcwd()   获得目录的当前系统程序工作路劲
2，os. chdir(‘目标目录’)  切换到目标目录
3，os.listdir(‘字符串目录’)     列出字符串目录下的所有文件
4，os.mkdir('目录')   创建目录
5，os.remove('1.txt')       删除文件，文件不存在时会报错
6，os.linesep      打印操作系统的分隔符，linux系统的分隔符\n，windows系统的分隔符\r\n，mac系统的分隔符\r
7，os.path.join(os.getcwd(),'aaa', ‘bbb’, ‘ccc’)   拼接出来多级目录：E:\test\aaa\bbb\ccc
8，os.path.exists(‘目录’)  判断目录是否存在
9，os.path.split(‘文件或者目录’)  把最后的一个目录或者文件和前面的目录分开，返回一个tuple
10，os.path.splitext(‘文件’)    把文件的后缀名和前面分开，返回一个tuple
"""

print("文件中包含“qytang”关键字的文件为:")
print("方案一：")
for file_or_dir in os.listdir(os.getcwd()):
    if os.path.isdir(file_or_dir):
        if file_or_dir == "test":
            for i in os.listdir(file_or_dir):
                temp = file_or_dir + "/" + i
                if os.path.isfile(temp):
                    for x in open(temp, "r"):
                        if re.findall("qytang", x):
                            print("{:>15s}".format(i))
print("方案二：")
# 更优化的递归方案
# topdown的用途：
#       True：从主目录扫描到子目录
#       False：从子目录扫描到主目录
for root, dirs,files in os.walk(os.getcwd(), topdown=False):
    for dir in dirs:
        if dir == "test":
            os.chdir("./test")  #切换到目标目录
            for root, dirs, files in os.walk(os.getcwd(), topdown=False):
            # for root, dirs, files in os.walk(os.getcwd()+"/"+dir, topdown=False):
                for name in files:
                    for x in open(root+"/"+name, "r"):
                        if re.findall("qytang", x):
                            print("{:>15s}".format(name))

        
# 完成清理工作
print(os.getcwd())
os.chdir("..")
for root, dirs, files in os.walk('test', topdown=False):
    for name in files:
        # print(name)
        os.remove(os.path.join(root, name))
    for name in dirs:
        # print(name)
        os.rmdir(os.path.join(root, name))
os.removedirs('test')




