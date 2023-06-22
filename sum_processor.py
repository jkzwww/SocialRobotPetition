import os
import csv
import sys

# operation variables
skipNextIter = False;


# to read csv
def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = []
        for row in reader:
            data.append(row)
    return data

# to read token
def record_tokens(numToken,isSecPrompt):

    global totalSign
    totalSign += 1
    if(isSecPrompt == False):
       
        if numToken == 1:
            global sumToken_1
            sumToken_1 += 1
        elif numToken == 2:
            global sumToken_2
            sumToken_2 += 1
        elif numToken == 3:
            global sumToken_3 
            sumToken_3 += 1
        else:
            print("invalid token number recorded!\n")

    # else:

    #     if numToken == 1:
    #         global sumReToken_1 
    #         sumReToken_1 += 1
    #     elif numToken == 2:
    #         global sumReToken_2 
    #         sumReToken_2 += 1
    #     elif numToken == 3:
    #         global sumReToken_3
    #         sumReToken_3 += 1
    #     else:
    #         print("invalid token number recorded!\n")

# to process cancel (double prompt)
def process_cancel(dataWordNext):

    cancel_case = 0
    # 0 : clear rejection
    # 1 : prompted to sign
    # 2 : prompted and cancelled
    # 3 : error
    dataPartsNext = dataWordNext.split('_')

    if(dataWordNext == 'cancel_2'): #rejection
        return cancel_case

    elif(dataPartsNext[0] == 'token'): #signed after prompted
        cancel_case = 1
        numToken = int(dataPartsNext[1])
        record_tokens(numToken,True)
        return cancel_case

    elif(dataWordNext == 'cancel_1'): #cancel again after returning to petition screen
        cancel_case = 2
        return cancel_case

    else:   #user stop interaction after cancel once
        cancel_case = 3
        return cancel_case



# storage files for different setups
storage_path = 'dataRecord/respSum.csv'
# header = ['Date', 'Signs', 'Token_1','Token_2','Token_3','Rejection','Stopped','Feedback_1','Feedback_2','Feedback_3','Feedback_4','Feedback_5','ReToken_1','ReToken_2','ReToken_3']
header = ['Date', 'Signs', 'Token_1','Token_2','Token_3','Rejection','Stopped','Feedback_1','Feedback_2','Feedback_3','Feedback_4','Feedback_5']

# check output storage file exists
if (os.path.exists(storage_path) == 0):
    with open(storage_path, 'w', newline='') as store_file:
        writer = csv.writer(store_file)
        writer.writerow(header)

# data storage path
data_path = 'testRawData'
# data directories
data_dirs = os.listdir(data_path)


for file_idx in range(len(data_dirs)):

    # data files from pepper
    file_path = os.path.join(data_path,data_dirs[file_idx]) 

    # check data file exists
    if (os.path.exists(file_path) == 0):
        print("data file is not found!\n")
        sys.exit() 
    else:
        data = read_csv_file(file_path)


    # testing data variables to be recorded

    # testing date time
    testDate = data[0][0]

    # total number of signs (successful persuasion, dont care strength)
    totalSign = 0;

    # sum of different choice of token signs
    sumToken_1 = 0;
    sumToken_2 = 0;
    sumToken_3 = 0;

    # sum of different choice of token signs AFTER prompted twice
    # sumReToken_1 = 0;
    # sumReToken_2 = 0;
    # sumReToken_3 = 0;

    # total number of rejection (not signing at all)
    totalRejection = 0;

    # record for incomplete interactions
    totalStops = 0;

    # sum of individual feedbacks
    sumFb_1 = 0;
    sumFb_2 = 0;
    sumFb_3 = 0;
    sumFb_4 = 0;
    sumFb_5 = 0;


    # read data

    for row in data:

        for col in range(len(row)):
            # print(skipNextIter)
            dataWord = row[col]
            print(dataWord)
            dataParts = dataWord.split('_')

            if(skipNextIter == True):
                skipNextIter = False
                continue

            # check date
            if(col == 0):
                testDate = dataWord
            
            # check half interaction
            if(dataWord == "stopped"):
                totalStops += 1

            # check valid recorded data
            if(len(dataParts) == 2):
                
                dataType = dataParts[0] # check data type

                if dataType == "token": #direct sign

                    numToken = int(dataParts[1])
                    record_tokens(numToken,False)

                elif dataType == "cancel": #cancelling
                    
                    totalRejection += 1 #user rejected once
                    # numCancel = int(dataParts[1])

                    # if(numCancel == 1):

                    #     if(col+1 < len(row)):
                    #         dataWordNext = row[col+1] #observe next reaction
                            
                    #         cancel_case = process_cancel(dataWordNext) #process interaction flow
                    #         # print(cancel_case)
                    #         if(cancel_case == 0): #rejected petition
                    #             totalRejection += 1
                    #         elif(cancel_case == 1): #decided to sign after prompted
                    #             skipNextIter = True
                    #         elif(cancel_case == 3): #user rejected once and gave up
                    #             totalRejection += 1
                    #     else:
                    #         totalRejection += 1 #user rejected once

                elif dataType == "fb": #feedbacks

                    fbReaction = int(dataParts[1])    
                    
                    if(fbReaction == 1):
                        sumFb_1 += 1
                    elif(fbReaction == 2):
                        sumFb_2 += 1
                    elif(fbReaction == 3):
                        sumFb_3 += 1
                    elif(fbReaction == 4):
                        sumFb_4 += 1
                    elif(fbReaction == 5):
                        sumFb_5 += 1
                    else:
                        print("invalid feedback!\n")
                
    # record data of the file
    # outputData = [testDate,totalSign,sumToken_1,sumToken_2,sumToken_3,totalRejection,totalStops,sumFb_1,sumFb_2,sumFb_3,sumFb_4,sumFb_5,sumReToken_1,sumReToken_2,sumReToken_3]
    outputData = [testDate,totalSign,sumToken_1,sumToken_2,sumToken_3,totalRejection,totalStops,sumFb_1,sumFb_2,sumFb_3,sumFb_4,sumFb_5]
    with open(storage_path, 'a', newline='') as store_file:
        writer = csv.writer(store_file)
        writer.writerow(outputData)