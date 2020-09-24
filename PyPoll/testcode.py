
# Python3 code to demonstrate  
# to get index and value 
# using naive method 
  
# initializing list 
test_list = [1, 4, 5, 6, 7] 
  
# Printing list  
print ("Original list is : " + str(test_list)) 
  
# using naive method to 
# get index and value 
print ("List index-value are : ") 
for i in range(len(test_list)): 
    print (i, end = " ") 
    print (test_list[i]) 

import os
import csv

poll_csv = os.path.join("Resources", "election_data2.csv")
os.listdir()



#poll_csv = os.path.join("Resources", "election_data.csv")
# line should be budget_csv = os.path.join("..", "Resources", "budget_data.csv")
#with open(poll_csv, "r") as csv_file:

with open(poll_csv, "r") as csv_file:
    x=0