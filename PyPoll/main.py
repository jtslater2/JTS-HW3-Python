import os
import csv

votecount = 0
totalprofit = 0
greatincrease = 0
greatdecrease = 0
increase = 0
decrease = 0
profit = 0
profitlist = []
avgtotal = 0
avglist = []
m2mavg = []
m2mname = []
m2mbest = ["year-month", "0"]
m2mleast = ["year-month", "0"]
m2mtotal = 0.0
m2mchange = 0.0
monthlist = []
canlist = []
uniname = ""


# stole this from geeksforgeeks.org and modified as needed - checks for name in list - True means it's NOT in the list
def check_in_list(list1, val): 
      
    # traverse in the list 
    for x in list1: 
  
        # compare with all the values 
        # with val 
        if val == x: 
            return False 
    return True



poll_csv = os.path.join("Resources", "election_data2.csv")

#poll_csv = os.path.join("Resources", "election_data.csv")
# line should be budget_csv = os.path.join("..", "Resources", "budget_data.csv")
#with open(poll_csv, "r") as csv_file:

with open(poll_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    #           print(csv_header)
    #           check = input("this is poll header")
    for row in csv_reader:
        votecount += 1
        #for uniname in range(len(candidatelist))
         #   if uniname != 
        #monthcount += 1   why doesn't this work
        #print(monthcount)
        #totalprofit = totalprofit + float(row[1])
        #print(totalprofit)
        uniname = row[2]
        print (uniname)
        if (check_in_list(canlist,uniname)):
            canlist.append(uniname)
        #profitlist.append(row[1])
        #monthlist.append(row[0])
        #print(profitlist)
        #candidate = csv_file[2]
        #print(candidate)
        #print(candidatelist)
        #check = input("this is candiddate list")
        #print = (str(row[2])
         #print(totalprofit)
        #               remove       profitlist.append(row[1])
        #               remove       monthlist.append(row[0])
        #print(profitlist)
        #check2 =input ("this is cand name currentllist")
        #check_in_list(candidatelist,row[2])
            #do nothing
         #   print("don't add to list")
        #else:
        #    candidatelist.append(row[2])
    print (votecount)
    check = input("this is the votecount")
    print (canlist)
    check = input("this is the can list ")
x=0
