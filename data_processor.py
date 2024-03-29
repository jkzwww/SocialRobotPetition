import os
import csv
import sys

# operation variables
skipNextIter = False;
sameResp = False;

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

# data storage folder path
data_path = 'testRawData'
# data directories
data_dirs = os.listdir(data_path)

# data files from pepper example
# file_path = 'testRawData/2023-06-01_02_56.csv'

for file_idx in range(len(data_dirs)):

    file_path = os.path.join(data_path,data_dirs[file_idx]) 
    file_name = data_dirs[file_idx]
    trial_name = file_name.split('_')[-1]

    # check data file exists
    if (os.path.exists(file_path) == 0):
        print("data file is not found!\n")
        sys.exit() 
    else:
        data = read_csv_file(file_path)

    # list of responses
    resp_list = []
    resp_id = 0
    sameResp = False;
    # read data
    for row in data:

        for col in range(len(row)):

            # skipping current iter
            if(skipNextIter == True): # check if recorded
                skipNextIter = False
                continue
            elif(row[col] == ""): #empty col
                continue    
            elif(col == 0): #check date
                testDate = row[col]
                resp_list.append([testDate,trial_name])
                continue
            
            # temporary response storage
            if(sameResp == False):
                temp_resp = []
                # participant id
                resp_id += 1;
                temp_resp.append(resp_id)

            # current data (action)
            dataWord = row[col]
            # split action for classfication
            dataParts = dataWord.split('_')


            
            
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

                elif(dataType == "small"): #foot-in-the-door

                    if(dataParts[1] == "agree"):
                        sameResp = True;
                    
                    temp_resp.append(dataWord)
                
                elif(dataType == "ans"):
                    temp_resp.append(dataWord)
                    sameResp = True;

                    
            if(sameResp == True & ((dataParts[0] == "small" or dataParts[0] == "ans")== False) ):
                sameResp = False

            # record interaction
            if(sameResp == False):
                resp_list.append(temp_resp)

            

    with open(storage_path, 'a', newline='') as store_file:
        writer = csv.writer(store_file)
        writer.writerows(resp_list)