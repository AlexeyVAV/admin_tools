import paramiko

class sshConnect:
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password


    def printInfo(self):
        print self.hostname, self.port, self.username, self.password

c1 = sshConnect('gbwatex2db01', 22, 'oracle', 'EarlWatf0rd#300')

c1.printInfo()

