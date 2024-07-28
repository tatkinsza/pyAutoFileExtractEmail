# importing the zipfile module 
from zipfile import ZipFile 
  
# loading the temp.zip and creating a zip object 
with ZipFile ("C:\\zip\\transaction_history_FNB_Gold_Credit_Account.zip", 'r') as zObject: 
  
    # Extracting all the members of the zip  
    # into a specific location. 
    zObject.extractall( 
        path="C:\\zip\\temp") 