#This function returns a connection instance to the sftp server based on the user credentials provided by user
# TODO : Use Singleton Design Pattern so that only one sftp connection instance is established at a time
import pysftp
cnopts = pysftp.CnOpts()

def sftp_connect(myHostname = "localhost", myUsername = "username", myPassword = "password"):
    try:
        sftp = pysftp.Connection(host=myHostname, username=myUsername, password=myPassword)
        return sftp
    except:
        print('User credentials not correct')

