# 赋值功能测试
# 同样是 1+2 可以通过传参实现
# pip3.8 install fire
# python example.py add 10 20

import fire
def add(x, y):
    z = x + y
    a = "计算 {0} + {1} 的结果：\n计算结果为{2}".format(x, y, z)
    return a
# a = "计算 {x} + {y} 的结果：\n计算结果为{z}".format(x=x,y=y,z=z)


if __name__ == '__main__':
    fire.Fire()
