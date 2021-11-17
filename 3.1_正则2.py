import re
x = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
y = re.split("[\s\,]",x)
z = re.split(":",y[7])

time = "{:<2s}小时 {:<2s}分钟 {:<2s}秒".format(z[0],z[1],z[2])
all = "{:<12s}：{}\n{:<12s}：{}\n{:<12s}：{}\n{:<12s}：{}\n{:<12s}：{}\n{:<12s}：{}\n".format(
    "protocol", y[0], y[1], y[2], y[3], y[4], y[6], time, y[9], y[10], y[12], y[13])
print(all)


