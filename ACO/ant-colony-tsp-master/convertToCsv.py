import pandas as pd
import json
import csv

def convertCSV():

    filename = "./data/output/output.json"
    listObj = []

    # Read JSON file
    with open(filename) as fp:
        listObj = json.load(fp)

    print(listObj)

    data_file = open("./data/output/output.csv", 'w', newline='')

    # create the csv writer object
    csv_writer = csv.writer(data_file)
    
    # Counter variable used for writing
    # headers to the CSV file
    count = 0
    for x in listObj:
        if count == 0:
            # Writing headers of CSV file
            header = x.keys()
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        csv_writer.writerow(x.values())
    
    data_file.close()