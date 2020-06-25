import os
from project.db import DBConnection, insert_to_db, lookup_db
from helpers.parser import csv_parser
from project.filetransfer import SftpConnection
from project.download_helper import download_csv

#Driver function to carry out the operations given in the technical task

def driver():
    my_hostname = '192.168.233.3'
    my_username = 'vagrant'
    my_password = 'vagrant'
    database_name = 'db'

    #Create a database connection
    db_connection = DBConnection().db_connect(database_name)
    #Create an sftp connection with the remote server
    sftp_connection = SftpConnection().sftp_connect(my_hostname, my_username, my_password)
    #Download the files from sftp server
    download_csv(sftp_connection)
    #We iterate over the files that have been downloaded and make the database operations
    for file in os.listdir(r"data/"):
        if file.endswith(".csv"):
            file_contents = csv_parser("data/" + file) #Parses csv file and returns a list of tuples
            c = db_connection.cursor()
            insert_to_db(file_contents, c) #Inserts parsed data to database
            lookup_db(c) #Lookup the table from database
    db_connection.close()
    sftp_connection.close()
    print('Database disconnected')
    print('Sftp Server disconnected')

if __name__ == '__main__':
    driver()





