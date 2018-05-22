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
    ssh_client = paramiko.SSHClient()
    ssh_connection = ssh_client
    ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connection.load_system_host_keys()
    hostname, port, username, password = connection_details()
    ssh_connection.connect(hostname, port, username, password)

    stdin, stdout, stderr = ssh_connection.exec_command('hostname -s')
    print stdout.read()

    #cmd_line = 'export ORACLE_HOME=/u01/app/oracle/product/12.1.0.2/dbhome_1; \
    #                                        export PATH=$PATH:$ORACLE_HOME/bin; \
    #                                        srvctl status database -d gbtukts1 2>&1'

    cmd_line = 'cat /etc/oratab|awk \'{FS=\":\"} {print $1}\''

    stdin, stdout, stderr = ssh_connection.exec_command(cmd_line)

    #print stdin
    #print stdout.read()

    # split stdin by words
    #inline = ''
    #for line in stdout.read():
    #    #print line
    #    if line != '\n':
    #        inline = inline + line
    #    else:
    #        print inline
    #        inline = ''

### list of words in output
    str_list = []
    common_list = []
    inline = ''
    inword = ''
    for line in stdout.read():
        #print line
        if line != '\n':
            if line != ' ':
                inword = inword + line
            else:
                str_list.append(inword)
                inword = ''
            inline = inline + line
        else:
            str_list.append(inword)
            inword = ''
            common_list.append(str_list)
            str_list = []
            #print inline
            inline = ''

    ssh_connection.close()
    print common_list[35:37]

if __name__ == '__main__':
    main()

