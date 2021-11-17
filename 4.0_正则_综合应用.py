import os,re

ifconfig_result = os.popen("ifconfig eth0").read()
# re.findall：只要能匹配上的字段，不论出现多少次，都直接存入列表内。
ipv4_add = re.findall("inet\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ifconfig_result)[0]
netmask = re.findall("netmask\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ifconfig_result)[0]
broadcast = re.findall("broadcast\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", ifconfig_result)[0]
mac_addr = re.findall("ether\s(\w+:\w+:\w+:\w+:\w+:\w+)", ifconfig_result)[0]

# 偷懒格式化
format_string = "{:<12s}：{}"
print(format_string.format("ipv4_add", ipv4_add))
print(format_string.format("netmask", netmask))
print(format_string.format("broadcast", broadcast))
print(format_string.format("mac_addr", mac_addr))

# 不假设，获取到正确网关
# iproute = os.popen("ip route").read()
# gateway = re.findall("default\svia\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", iproute)[0]
# print("\n我没有假设自己的网关，因此网关的真事地址为：" + gateway +"\n")

# 假设，如题要求假设是254：
ipv4_gw = re.sub("\d{1,3}$", "254", ipv4_add)
print("\n如题，我们假设要猜网关的IP地址最后一位是254。因此网关IP地址为：" + ipv4_gw + "\n")

# 假设网关为 254：
ping_result = os.popen("ping " + ipv4_gw + " -c 1").read()

# 真实网关：
# ping_result = os.popen("ping " + gateway + " -c 1").read()

re_ping_result = re.findall("1\sreceived", ping_result)

if re_ping_result:
    print("网关可达！")
else:
    print("网关不可达！")
