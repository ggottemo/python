#! python3
#removeCsvHeader.py - Removes the header from all CSV files in 
#the current working directory - from AtBS

import csv, os

os.makedir('headerRemoved', exist_ok=True)

#Loop through every file in the current working directory.

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue #skip non-csv files
        
    print('Removing the header from ' + csvFilename + '...')
    
    
    #Read CSV File (skip first row)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue #skip first row
        csvRows.append(row)
    csvFileObj.close()
    
    
    #Writer out the CSV File
    csvFileObj = open(os.path.join('headerRemoved', csvFilename),'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
