#This function returns an instance of the file if located on remote server
def csv_parser(path):
    if path:
        try:
            file =  open(path, 'r')
            return file
        except:
            print('Please provide correct path')
    else:
        print("Path not provided")
