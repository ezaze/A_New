# sort + lambda 最佳文档链接
# https://blog.csdn.net/weihongrao/article/details/16877595?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-3.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-3.no_search_link

import re
port_list = ['eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7', 'eth 1/101/2/46', 'eth 1/101/1/34','eth 1/101/1/18', 'eth 1/101/1/13', 'eth 1/101/1/32', 'eth 1/101/1/25', 'eth 1/101/1/45', 'eth 1/101/2/8']

# lambda 一句话方案
r_match = "\S+\s+\d+/\d+/(\d+)/(\d+)"
port_list.sort(key=lambda x: (re.match(r_match,x).groups()[0], int(re.match(r_match, x).groups()[1])))
print(port_list)



# 非lambda方案
# def sw1(x):
#     r = re.match("\S+\s+\d+/\d+/(\d+)/(\d+)", x).groups()
#     r1 = int(r[0])*100+int(r[1])
#     # print(r1)
#     return r1

# port_list = ['eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7', 'eth 1/101/2/46', 'eth 1/101/1/34','eth 1/101/1/18', 'eth 1/101/1/13', 'eth 1/101/1/32', 'eth 1/101/1/25', 'eth 1/101/1/45', 'eth 1/101/2/8']

# port_list.sort(key=sw1)
