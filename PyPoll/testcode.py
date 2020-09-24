
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

list1 = ["moe", "larry", "curly"]
#val = "moe"

# stole this from geeksforgeeks.org
def check(list1, val): 
      
    # traverse in the list 
    for x in list1: 
  
        # compare with all the values 
        # with val 
        if val == x: 
            return False 
    return True

val = input("put a stooge in?")

if (check(list1,val)):
    print (val + " is Not  in the list")
else:
    print (val  + " is in the list")
x=0
