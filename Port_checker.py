import paramiko
import socket
import os

"""Ip address and port number are stored as environment variable in Lambda function"""

host= os.environ('PrivateIp')
port= os.environ('portNum')

def ssh():
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(host, username='ec2-user', key_filename='./ssh.pub')

    stdin, stdout, stderr = ssh.exec_command('ls')
    print("conneted with linux system")

    port()

    ssh.close()


def port():
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    location = (host, port)
    result_of_check = a_socket.connect_ex(location)

    if result_of_check == 0:
        print("Port is open")
    else:
        print("Port is not open")

    a_socket.close()

def index():
    ssh()