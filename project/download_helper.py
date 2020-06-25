#Helper function that takes an instance of the sftp connection as parameter and downloads the file in our desired folder
def download_csv(sftp_connection):
    dir_contents = sftp_connection.listdir()
    for file in dir_contents:
        if file.endswith(".csv"):
            try:
                sftp_connection.get(file , 'data/' + file) #File will download to directory 'current directory + '/data/''
            except:
                print('No csv files present')
