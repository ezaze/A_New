import re

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"


asa_dict = {}


for conn in asa_conn.split("\n "):
    print(conn)
    re_result = re.match("\S+\s+\S+\s+(\S+):(\S+)\s+\S+\s+(\S+):(\S+),\s+\S+\s+\S+\s+\S+\s+(\d+)\S+\s+\S+\s+(\S+)",conn).groups()
    asa_dict[re_result[0], re_result[1], re_result[2], re_result[3]] = (re_result[4],re_result[5])
print("打印分析后的字典：\n")
print(asa_dict)

src = "src"
src_ip = "src_ip"
dst = "dst"
dst_ip = "dst_ip"
bytes_name = "bytes"
flags = "flags"
format_str1 = "{:^10s}:{:^15s}|{:^10s}:{:^15s}|{:^10s}:{:^10s}|{:^10s}:{:^10s}"
format_str2 = "{:^10s}:{:^15s}|{:^10s}:{:^15s}"

print("\n格式化打印输入\n")
for key, value in asa_dict.items():
    print(format_str1.format(src, key[0], src_ip, key[1], dst, key[2], dst_ip, key[3]))
    print(format_str2.format(src, value[0], src_ip, value[1]))
    print("="*len(format_str1.format(src,key[0], src_ip, key[1], dst, key[2], dst_ip, key[3])))
