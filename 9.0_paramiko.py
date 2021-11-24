#安装基本依赖:
#yum install gcc libffi-devel python-devel openssl-devel

#安装paramiko依赖的python模块、安装paramiko模块: 
# python3 -m pip install --upgrade --force pip # Centos7 需要
# pip3.8 install -i https://pypi.douban.com/simple/ pycparser
# pip3.8 install -i https://pypi.douban.com/simple/ cryptography==2.4.2
# pip3.8 install -i https://pypi.douban.com/simple/ paramiko

import paramiko

# 密码登录
def qytang_ssh(ip, username,password , port=22,cmd="ls"):
    ssh = paramiko.SSHClient() 
    ssh.load_system_host_keys()  # 读取本地的 host验证 
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 如果没有则自动加入 host验证 （跳过首次连接的yes确认环节）
    ssh.connect(ip, port=port, username=username,
                password=password, timeout=5, compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

# 秘钥登录：
def qytang_ssh_key(ip, username, key_file, port=22, cmd="ls"):
    ssh = paramiko.SSHClient()
    private_key = paramiko.RSAKey.from_private_key_file(key_file)
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username,
                pkey=private_key, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

if __name__ == '__main__':
    # 注：因为学习用的Centos8用的云主机，没配密码登录。以下用了秘钥登录展示
    print(qytang_ssh_key("120.92.44.10","root","/root/.ssh/id_rsa"))
    print(qytang_ssh_key("120.92.44.10","root","/root/.ssh/id_rsa",\
        cmd="pwd"))