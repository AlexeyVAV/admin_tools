import paramiko

class sshConnection:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

            try:
                sshClient = sshConnection._instance.sshClient = paramiko.SSHClient()
                sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                sshClient.load_system_host_keys()
                connect = paramiko.connect(self.hostname, self.port, self.username, self.password) = sshc._instance.connect()

