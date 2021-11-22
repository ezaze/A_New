import re,os

x = os.popen("route -n").read()

y = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S+\s+UG", x)
print("网关为："+ y[0])