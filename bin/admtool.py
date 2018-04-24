import paramiko

class sshConnect:
    _instance = None

    def __new__(cls):
        if cls._instance = None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        if cls._instance = None:
            cls._instance = object.__new__(cls)
            logfile = paramiko.util.log_to_file('../log/paramiko.log')
            try:
                sshclient = sshConnect._instance = paramiko.SSHClient()
                sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                sshc.load_system_host_keys()
                connect = paramiko.connect(self.hostname, self.port, self.username, self.password) = sshc._instance.connect()
        return cls._instance

    def sshConnection(self):

        return s

    def printInfo(self):
        print self.hostname, self.port, self.username, self.password

    def execCommand(self, icommand):
        stdin, stdout, stderr = self.exec_command(icommand)
        self.stdout = stdout
        return stdin, stdout, stderr

c1 = sshConnect('', 22, 'oracle', '')
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

/*
import psycopg2


class Postgres(object):
"""docstring for Postgres"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            # normally the db_credenials would be fetched from a config file or the enviroment
            # meaning shouldn't be hardcoded as follow
            db_config = {'dbname': 'demo', 'host': 'localhost',
                     'password': 'postgres', 'port': 5432, 'user': 'postgres'}
            try:
                print('connecting to PostgreSQL database...')
                connection = Postgres._instance.connection = psycopg2.connect(**db_config)
                cursor = Postgres._instance.cursor = connection.cursor()
                cursor.execute('SELECT VERSION()')
                db_version = cursor.fetchone()

            except Exception as error:
                print('Error: connection not established {}'.format(error))
                Postgres._instance = None

            else:
                print('connection established\n{}'.format(db_version[0]))

        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor

    def query(self, query):
        try:
            result = self.cursor.execute(query)
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return result

    def __del__(self):
        self.connection.close()
        self.cursor.close()
*/