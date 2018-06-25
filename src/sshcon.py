#!/usr/bin/python3
# -*- coding:utf-8 -*-  
'''
Created on 2018年6月25日

@author: s00171836
'''
import paramiko
import time
import sys
class SshCon:
    def __init__(self,ip,port,username,passwd):
        self.info = {"ip":ip,"port":port,"username":username,"passwd":passwd}
        self.shell = None
    def login(self):
        ssh = paramiko.SSHClient()    # 定义ssh client，SSHClient()就是paramiko里的一个函数
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #定义登录policy，抄的，都这么写
        try:
            ssh.connect(hostname=self.info['ip'],port=self.info['port'],
                             username=self.info['username'],password=self.info['passwd'])
#             ssh.get_transport()
            #self.info['ip'] 其实就是字典中{'ip': ip} 对应的value，也就是实际IP
#             ssh.get_pty()
            self.shell = ssh.invoke_shell()   #登录到远程主机，开一个终端
            buff = '' #定义空字符串
            recv = str(self.shell.recv(65535),encoding='ascii')   #收到打印返回    可以尝试不加decoding返回结果
            print(recv) 
            sys.stdout.flush()
        except paramiko.AuthenticationException as e:  #登录失败报错
            raise e
    
    def execute(self,cmd):
        if self.shell is None:   #如果没有登录，执行login 函数
            self.login()
        self.shell.send(cmd)   #在登录主机上发送指令
        buff = '' #定义空字符串
        time.sleep(1)  # 返回可能有延迟，等待1s，正常应该通过判断--- END字符串来判断返回是否完成
        recv = str(self.shell.recv(65535),encoding='ascii')   #收到打印返回    可以尝试不加decoding返回结果
        print(recv) 
        sys.stdout.flush()
        return len(recv)

if __name__ == '__main__':    #定义程序入口
    sshcon = SshCon(ip= "192.16.3.49", port = 22, username = "root", passwd = 'root')  #定义初始值
    outlen = sshcon.execute(cmd= 'pwd\n')   #输入指令
