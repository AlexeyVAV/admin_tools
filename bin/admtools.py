import paramiko

def connection_details():
    hostname = ''
    port = 22
    username = 'oracle'
    password = ''
    return hostname, port, username, password


## MAIN ##
def main():
    paramiko.util.log_to_file('../log/paramiko.log')

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.load_system_host_keys()

    hostname, port, username, password = connection_details()
    s.connect(hostname, port, username, password)

    stdin, stdout, stderr = s.exec_command('hostname -s')
    print stdout.read()
    stdin, stdout, stderr = s.exec_command('export ORACLE_HOME=/u01/app/oracle/product/12.1.0.2/dbhome_1; \
                                            export PATH=$PATH:$ORACLE_HOME/bin; \
                                            srvctl status database -d gbtukts1 2>&1')
    #print stdin
    #print stdout.read()

    # split stdin by words
    #l = ''
    #for line in stdout.read():
    #    #print line
    #    if line != '\n':
    #        l = l + line
    #    else:
    #        print l
    #        l = ''

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
            print l
            l = ''

    s.close()
    print common_list

if __name__ == '__main__':
    main()

