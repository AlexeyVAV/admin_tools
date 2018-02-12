import paramiko

hostname = ''
port = 22
username = 'oracle'
password = ''

if __name__ == '__main__':
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('hostname -s')
    print stdout.read()
    stdin, stdout, stderr = s.exec_command('export ORACLE_HOME=/u01/app/oracle/product/12.1.0.2/dbhome_1; \
                                            export PATH=$PATH:$ORACLE_HOME/bin; \
                                            srvctl status database -d gbtukts1 2>&1')
    #print stdin
    print stdout.read()
    s.close()


