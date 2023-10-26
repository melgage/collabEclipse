import subprocess   # Import the subprocess function to execute command line arguments
import sys          # Import the sys function to execute command line arguments
import requests     # Import 
import json         # Import 
import csv          # Import csv 

#
# Every JSON API call to Collaborator is made using the POST type only.
# These can be formatted just as they would be for a URL request using 
# API test webservice. 808
loginTicketResponse = requests.post('http://collaborator.se.smartbear.io:8080/services/json/v1', 
    json=[{'command' : 'SessionService.getLoginTicket',
        'args' : {
            'login' : 'user',
            'password' : 'password'
        }}])
#print(type(loginTicketResponse))               # Output test
#print(type(loginTicketResponse.text))          # Output test

#
# Convert the JSON response str to JSON dict that referenced by index names.
resp=json.loads(loginTicketResponse.text)
print(resp)                                   # Output test

# Verify the JSON dict file type. Note that the index value is critical.
# Without the index, the variable is treated as a 'list', rather than a
# 'dict' type. Once properly defined, the values in the JSON dict can be addressed
# by their index identifiers.
#print(type(resp[0]))                           # Output test
#print(resp[0]['result']['loginTicket'])        # Output test

#
# Verify the JSON dict file type. Note that the index value is critical.
# Without the index, the variable is treated as a 'list', rather than a
# 'dict' type. Once properly defined, the values in the JSON dict can be addressed
# by their index identifiers.
#    print(type(resp[0]))   -(Used to validate the class of resp[0] as a dict)
#
# Capture the authentication token from the response in loginToken.
# This value will be used in all subsequent JSON API calls.
#
loginToken=(resp[0]['result']['loginTicket'])

# Load a CSV file for user information.
with open('CollaboratorLoadNinjaTest.csv', newline='') as csvfile:
    users = list(csv.reader(csvfile, delimiter=','))
#
# Create new Users in Collab.
#
# Format of the columns in CollaboratorLoadNinjaTest.csv:
# Column 0 = login
# Column 1 = password
# Column 2 = fullName
# Column 3 = email
#
# Working
n = 1    # Number of new Users to create. Equals the number of users in the CollaboratorLoadNinjaTest.csv file.
i = 1       # i = 1 ignores the header row in the CollaboratorLoadNinjaTest.csv file.
while i <= n :
    reviewInformation = requests.post('http://collaborator.se.smartbear.io:8080/services/json/v1', 
        json=[{'command' : 'SessionService.authenticate',
            'args' : {
                'login' : 'user',
                'ticket': loginToken
                }
            },
            {'command' : 'ReviewService.getParticipants',
            'args' : {
                'reviewId' : '604',
               }
            }

        ])
    i += 1  # Increment the index for the master loop.


# Working for JSON parsing and output to a file.
#
resp_dict=json.loads(reviewInformation.text)
resp_out=(json.dumps(resp_dict, indent=4))
print(resp_out)
#
#reviewInfoOut=open(r'C:\Trigger\reviewInfo.txt', 'w+')
#reviewInfoOut.writelines(resp_out)
#reviewInfoOut.close()