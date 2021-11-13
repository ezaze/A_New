import random

def ip():
    r = str(random.randint(0,255))
    return r

# 随机产生任意IPv4地址（不考虑产生的IP地址的具体用途）
result = ip() + "." + ip() + "." + ip() + "." + ip()
print(result)