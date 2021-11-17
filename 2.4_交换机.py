import re
# 手边没有思科设备，直接网上搜了一段当做文本，匹配状态是”up“ 所在行
cisco = """
Interface                  IP-Address           OK? Method Status                Protocol
FastEthernet0/0            192.168.189.254      YES unset  up                    up     
FastEthernet0/1            unassigned           YES unset  up                    down   
FastEthernet0/2            unassigned           YES unset  up                    down   
FastEthernet0/3            unassigned           YES unset  up                    down   
"""

ciscos = re.split("\n", cisco)

for x in ciscos:
    r = re.match("([F]+\S*)\s+(\d\S*)\s+\w+\s+\w+\s+(\w+)\s+(\w+)",x)
    if r != None:
        str1 = x
        print("{0:<12s}：{1} \n{2:<12s}：{3} \n{4:<12s}：{5} " \
              .format("接口", r.groups()[0], "IP地址", r.groups()[1], "状态",r.groups()[2]))



# 适配"长度、内容都不确定"的多个字符的分割： re.split(<要匹配的被分割的内容>，<文本内容>)
# re.split("[=-]+",x)
# m = re.split(" +", cisco)
# print(m)

# 替换内容： re.sub(<要匹配的内容>,<匹配后想替换的内容>,<文本内容>)
# s = re.sub(" +", ',', cisco)
# print(s)



'''
\d 任意一个数字
\w 大写小写数字下划线
\s 匹配所有任意空白（空格、空白、制表符等）
\S 匹配非空白
.  匹配任意一个字符  （除 \n）
.* 匹配任意字符 但匹配不到\n 后的内容
[\s\S]* 空白或非空白 + 任意长度

————————————————————————————
[]: 括号里的所有字符，只要有任意一个能匹配成功就算匹配成功，限一个字符。
    [0-9]       数字
    [^0-9]      非数字
    [a-zA-Z0-9] 任意字符和数字
    [-=]        匹配-或=

————————————————————————————
重复
{n}
?： 0次 或 1次
+： 至少 1次
*： 0 - 任意次
{3}:  3次
{3,5} ：至少3次，至多5次
{3,}： 至少3次
a|b：  a或b

'''
