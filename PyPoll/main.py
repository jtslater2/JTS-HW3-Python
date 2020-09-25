import os
import csv

votecount = 0
canlist = []
votelist = []
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

def candstats(candidate):
    global winnerpercent
    global winner
    global percentwon
    global candvotes
    candvotes = 0
    for x in votelist:
        if x == candidate:
            candvotes += 1
    percentwon = (candvotes/votecount)*100
    if percentwon > winnerpercent:
        winner = candidate
        winnerpercent = percentwon
    print(f"{each}      \t:{round(percentwon,3)}%\t {candvotes}")
    file.write(f"{each}      \t:{round(percentwon,3)}%\t {candvotes}\n")
    return(percentwon)
    return(candvotes)
 
 
 



poll_csv = os.path.join("Resources", "election_data.csv")

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
        votelist.append(uniname)
        #print (uniname)
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
    print("Election Results")
    print("-----------------------------------")
    print(f" Total Votes:   {votecount}")
    print("-----------------------------------")
    
    file = open("outfile.txt","w+") 
 
    file.write("Election Results\n") 
    file.write("-----------------------------------\n") 
    file.write(f" Total Votes:   {votecount}\n")
    file.write("-----------------------------------\n")





    winnerpercent = 0
    for each in canlist:
        candstats(each)

    #print(f"{each}      \t:{round(percentwon,3)}%\t {candvotes}")
    #file.write(f"{each}      \t:{round(percentwon,3)}%\t {candvotes}")
    #print(f"{each}      \t:{round(percentwon,3)}%\t {candvotes}")
    print("-----------------------------------")
    print(f"Winner: {winner}")
    #file.write(f"{each}      \t:{round(percentwon,3)}%\t {candvotes}")
    file.write("-----------------------------------\n")
    file.write(f"Winner: {winner}")
    
    x=0
    #for each in canlist
     #   votecount = countvotes(votelist,str(each))








x=0
y=0


