#Returns a connection instance to the sftp server based on the user credentials provided by user
from helpers.singleton import Singleton
import pysftp
cnopts = pysftp.CnOpts()
#We create a class a class and we decorate it with the Singleton class
#The Singleton class implements the Singleton Design Pattern
#This makes sure there is a only one single instance of a sftp server at a time
@Singleton
class SftpConnection:
    sftp_connection = None
    def sftp_connect(self, myHostname = "localhost", myUsername = "username", myPassword = "password"):
        if self.sftp_connection is None: # Creates a new connection if only there is nno existing connection or returns the existing
            self.sftp_connection = pysftp.Connection(host=myHostname, username=myUsername, password=myPassword)
            print("Sftp server connected successfully")
        return self.sftp_connection



