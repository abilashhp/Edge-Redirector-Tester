# Python Script for Edge Redirector v2
# Input should be in CSV format.
# 'Sample_Redirect_Tester_Input_File.csv' = The names of the columns are expected to be Origin and Destination. If it differs from these, please update the script.
# 'Sample_Redirect_Tester_Output_File.csv' = Will have columns 'Source' 'Destination' 'Response Code' 'Redirect Location' 'Result'

import requests
import csv

# Sample_Redirect_Tester_Input_File.csv - Filename of the list of redirects. 
# Please insert complete paths unless you are running python from the same folder.

with open('Sample_Redirect_Tester_Input_File.csv') as csv_file_source:
    csv_reader = csv.reader(csv_file_source)
    print('Source', 'Destination', 'Response Code', 'Redirect Location', 'Result')
    for row in csv_reader:
        
        if row[0]=='Origin':
            continue
        else:
            response = requests.get(row[0], allow_redirects=False)
            if (response.status_code != 301) and (response.status_code != 302):
                result = 'No Redirect!'
                output = (row[0], row[1], response.status_code, '',result)
                print(row[0], row[1], response.status_code, '',result)

            elif (response.status_code == 301 or 302) and (response.headers['location']==row[1]):
                result = 'Success!'
                output = (row[0], row[1], response.status_code, response.headers['location'], result)
                print(row[0], row[1], response.status_code, response.headers['location'], result)
            else:
                result = 'Failure!'
                output = (row[0], row[1], response.status_code, response.headers['location'], result)
                print(row[0], row[1], response.status_code, response.headers['location'], result)

            with open('Sample_Redirect_Tester_Output_File.csv', 'a+') as csv_file_destination:  
                csvwriter = csv.writer(csv_file_destination)  
                csvwriter.writerow(output)
    csv_file_source.close()
