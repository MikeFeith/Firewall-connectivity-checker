import socket
import pandas as pd
import sys
data=pd.read_excel("Firewallchecklist.xlsx",index_col=False) #Excel file location
sys.stdout = open("output.txt", "w") # outputs the result to output.txt

def chkdomreach(index,ipadres,port): #Main functie, controlleert of het domein en de poort toegankelijk zijn.
    excelloc = index + 1 # each request +1
    location = (ipadres, port)
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a_socket.settimeout(2) #2 second time out between request. should be enough.
    result_of_check = a_socket.connect_ex(location)

    if result_of_check == 0:
        print(excelloc, " SUCCESS Domain can be reached:", location) #This will go in the output.txt if the domain CAN be reached
    else:
        print(excelloc," FAIL Domain cannot be reached:", location) #This will go in the output.txt if the domain CANNOT be reached but CAN be resolved
    a_socket.close()

for index, row in data.iterrows():
    try:
        output = chkdomreach(index,row["Destination"], row["Port"]) #change this to the correct column names!
    except:
        Destination=row["Destination"] #For fixing the annoying integer error
        excelloc = index + 1
        print(excelloc, " Error! The domain can most likely not be resolved: "+Destination) #This error will be displayed if the domain can most likely not be resolved

sys.stdout.close()
