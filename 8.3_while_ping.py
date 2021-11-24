# pip3 install -i https://pypi.douban.com/simple/ kamene
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 关闭不必要的报错
from kamene.all import *

def qytang_ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()  # 制造一个Ping包
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:   
        return ip + " 通！"
    else:
        return ip + " 不通！"

if __name__ == '__main__':
    result = qytang_ping("10.64.20.1")
    print(result)

