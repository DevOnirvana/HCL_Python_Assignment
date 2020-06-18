import csv
from project import filetransfer, db, parser
class Driver:
    def __init__(self):
        self.sftpConnection = None
        self.getFile = None
        self.connection = None
        self.csv_file = None

    #This function creates an sftp connection to remote server and downloads the desired file to the data folder
    # TODO : Use Singleton Design Pattern so that only one connection instance is established at a time

    def create_connection_sftp(self):
        myHostname = input('Enter Hostname')
        myUsername = input('Enter Username')
        myPassword = input('Enter Password')
        if not self.sftpConnection:

            #an sftp connection instance is returned
            self.sftpConnection = filetransfer.sftp_connect(myHostname , myUsername , myPassword)

            # To check if the file exists in remote location (Can use try/except block for this too)
            if self.sftpConnection.isfile("/file.csv"):

                #This is where the file is downloaded from the remote location to the desired local location
                self.sftpConnection.get('/file.csv', '../data/file.csv')

                #Close the connection
                self.sftpConnection.close()
            else:
                #If file is not present in remote server
                print('File not in remote directory')

    #Create a datatbase instance and insert data

    def create_connection_db(self):
        #User input to specify which database to connect to
        database_name = input('Which database do you wish to connect to ?')

        #Create a connection to database
        self.connection = db.db_connect(database_name)

        #Create cursor object to make sql commands
        c = self.connection.cursor()

        #Execute sql commands using the cursor object created above
        #TODO: The INSERT command inserts the data(python dictionary) that has been parsed by function parse_csv
        try:
            c.execute('''INSERT INTO people (Result Time, Granularity Period, Object Name,  Cell ID, CallAttempts) 
                                    VALUES ('2016-10-21', '13:45,15', 'LIMRNC03/BSC6900UCell:Label=LHU30047c1_Mandingo', 30047, 20)''')
        except:
            c.execute('''CREATE TABLE people
                                (name, class, number)''')

            #TODO: Dummy Data to be replaced with the output of function parse_csv
            c.execute('''INSERT INTO people (Result Time, Granularity Period, Object Name,  Cell ID, CallAttempts) 
                                    VALUES ('2016-10-21', '13:45,15', 'LIMRNC03/BSC6900UCell:Label=LHU30047c1_Mandingo', 30047, 20)''')

        # for row in c.execute('SELECT * FROM people'):
        #     print(row)
        self.connection.close()
        print('Closed database connection successfully')

    #Parse the csv file downloaded to folder 'data' through sftp to a list of python dictionaries
    #TODO: This python dictionary will be inserted as input to the database that the user connect to

    def parse_csv(self):
        #User input for the csv to be parse
        #TODO: This path is automatically the path of fie that has been downloaded via sftp
        path = input('Enter path of csv')  # use path = "data/people.csv"

        #Returns a DictReader instance to the parsed data
        self.csv_file = csv.DictReader(parser.csv_parser(path))
        for row in self.csv_file:
            print(dict(row))

#Initialize an object of Driver class
obj = Driver()

# obj.parse_csv()
# obj.create_connection_db()
# obj.create_connection_sftp()



