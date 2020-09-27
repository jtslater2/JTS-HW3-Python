

import datetime

# Python3 code to demonstrate  
# to get index and value 
# using naive method 
  
# initializing list 
test_list = [1, 4, 5, 6, 7] 
  
# Printing list  
print ("Original list is : " + str(test_list)) 
  
# using naive method to 
# get index and value 
#print ("List index-value are : ") 
#for i in range(len(test_list)): 
 #   print (i, end = " ") 
  #  print (test_list[i]) 


#import csv

#with open("election_data2.csv", "r") as csv_file:
 #   csv_reader = csv.reader(csv_file, delimiter=",")
  #  csv_header = next(csv_file)
    #           print(csv_header)
    #           check = input("this is poll header")

newdate = datetime.strptime("2015-09-03 14:32:00", "%Y-%d-%m %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
