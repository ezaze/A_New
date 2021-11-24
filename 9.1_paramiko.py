import paramiko,re

def ssh_get_route(ip, username, key_file, port=22, cmd="route -n"):
    ssh = paramiko.SSHClient()
    private_key = paramiko.RSAKey.from_private_key_file(key_file)
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username,
                pkey=private_key, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    y = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\S+\s+UG", x)
    return y[0]

if __name__ == '__main__':
    # 注：因为学习用的Centos8用的云主机，没配密码登录。以下用了秘钥登录展示
    print(qytang_ssh_key("120.92.44.10","root","/root/.ssh/id_rsa"))
    print(qytang_ssh_key("120.92.44.10","root","/root/.ssh/id_rsa",\
        cmd="pwd"))
    print("网关为：")
    print(ssh_get_route("120.92.44.10","root","/root/.ssh/id_rsa"))