#This function returns the contents of the file after parsing it
#DictReader returns a list of tuples here
import csv
def csv_parser(file):
    flag = open(file, 'r')
    csv_file = csv.DictReader(flag)
    return csv_file

