import os
import time
import re


while True:
    a = os.popen("ss -tulnp")
    # print(a.read())
    if re.findall("tcp\s+[\S\s]+\s+0.0.0.0:80\s+[\S\s]+", a.read()):
        print("HTTP (TCP/80) 服务已经被打开")
        break
    else:
        print("等待一秒重新开始监控!")
    time.sleep(1)