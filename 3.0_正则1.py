import re
x = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
y = re.split(" ",x)
print("{:<12s}：{}\n{:<12s}：{}\n{:<12s}：{}\n{:<12s}：{}\n".format(
    "VLAN ID", y[0], "MAC", y[1], "Type", y[2], "Interface", y[3]))
