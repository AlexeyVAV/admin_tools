import paramiko

class sshConnect:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def sshConnection(self):
        paramiko.util.log_to_file('../log/paramiko.log')

        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.load_system_host_keys()

        sshc = s.connect(self.hostname, self.port, self.username, self.password)

        #return s

    def printInfo(self):
        print self.hostname, self.port, self.username, self.password

    def execCommand(self, icommand):
        stdin, stdout, stderr = self.exec_command(icommand)
        self.stdout = stdout
        return stdin, stdout, stderr

c1 = sshConnect('gbwatex2db02', 22, 'oracle', 'EarlWatf0rd#300')
c1.printInfo()

c1.sshConnection()
#sshc = c1.sshc

#stdin, stdout, stderr = sshc.exec_command('export ORACLE_HOME=/u01/app/oracle/product/12.1.0.2/dbhome_1; \
#                                           export PATH=$PATH:$ORACLE_HOME/bin; \
#                                           srvctl status database -d gbtukts1 2>&1')

stdin, stdout, stderr = c1.execCommand('export ORACLE_HOME=/u01/app/oracle/product/12.1.0.2/dbhome_1; \
                                           export PATH=$PATH:$ORACLE_HOME/bin; \
                                           srvctl status database -d gbtukts1 2>&1')

#print sshc.stdout.read()

### list of words in output
str_list = []
common_list = []
l = ''
w = ''
for line in stdout.read():
    #print line
    if line != '\n':
        if line != ' ':
            w = w + line
        else:
            str_list.append(w)
            w = ''
        l = l + line
    else:
        str_list.append(w)
        w = ''
        common_list.append(str_list)
        str_list = []
        #print l
        l = ''

ssh.close()

print common_list
# print common_list