import os
import csv
import sys

# operation variables
skipNextIter = False;

# storage file for participant response list
storage_path = 'dataRecord/respList.csv'

# function to read csv
def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = []
        for row in reader:
            data.append(row)
    return data

# data storage path
data_path = 'testRawData'
# data directories
data_dirs = os.listdir(data_path)

# data files from pepper
# file_path = 'testRawData/2023-06-01_02_56.csv'

for file_idx in range(len(data_dirs)):

    file_path = os.path.join(data_path,data_dirs[file_idx]) 

    # check data file exists
    if (os.path.exists(file_path) == 0):
        print("data file is not found!\n")
        sys.exit() 
    else:
        data = read_csv_file(file_path)

    # list of responses
    resp_list = []
    resp_id = 0

    # read data

    for row in data:

        for col in range(len(row)):

            # temporary response storage
            temp_resp = []
            # current data (action)
            dataWord = row[col]
            # split action for classfication
            dataParts = dataWord.split('_')

            # skipping current iter
            if(skipNextIter == True): # check if recorded
                skipNextIter = False
                continue
            elif(col == 0): #check date
                testDate = dataWord
                resp_list.append([testDate])
                continue

            # participant id
            temp_resp.append(resp_id)
            resp_id += 1;

            # check actions
            if(dataWord == "stopped"):
                temp_resp.append(dataWord)

            elif(len(dataParts) == 2):
                dataType = dataParts[0] # check data type

                if(dataType == "token"): #direct sign
                    temp_resp.append(dataWord)

                    # check feedback given
                    if(col+1 < len(row)):
                        dataNext = row[col+1]
                        
                        if(dataNext.split('_')[0] == 'fb'):
                            temp_resp.append(dataNext)
                            skipNextIter = True

                elif(dataType == "cancel"): #reject
                    temp_resp.append(dataWord)
            
            # record interaction
            resp_list.append(temp_resp)

    with open(storage_path, 'a', newline='') as store_file:
        writer = csv.writer(store_file)
        writer.writerows(resp_list)