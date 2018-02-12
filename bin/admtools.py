#import pandas
#import flask
#import cx_Oracle
import sys
import paramiko
#
# from paramiko import SSHClient

hostname = ''
port = 22
username = 'root'
password = ''

if __name__ == '__main__':
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    print stdout.read()
    stdin, stdout, stderr = s.exec_command('hostname -s')
    print stdout.read()
    s.close()


