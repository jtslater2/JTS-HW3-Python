import os
import csv

#variables and lists
votecount = 0
candlist = []
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

#function to calculate candidate votes, percent won, winner, winnerpercent for each individual candidate
def candstats(candidate):
    global winnerpercent
    global winner
    candvotes = 0
    #set loop to count votes per candidate
    for x in votelist:
        if x == candidate:
            candvotes += 1
    #set percent won per candidate
    percentwon = (candvotes/votecount)*100
    #set winner and percent won
    if percentwon > winnerpercent:
        winner = candidate
        winnerpercent = percentwon
    #print candidate stats to terminal
    print(f"{each}      \t:{round(percentwon,3)}%\t {candvotes}")
    
    #print candidate stats to file
    file.write(f"{each}      \t:{round(percentwon,3)}%\t {candvotes}\n")
     

#Find the relative path, open file and set the header
poll_csv = os.path.join("Resources", "election_data.csv")

with open(poll_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    
    #set loop to count votes, create votelist & candidate list
    for row in csv_reader:
        votecount += 1
        
        #create votelist
        uniname = row[2]
        votelist.append(uniname)

        #checks if candidate is in list if no - Add to list
        if (check_in_list(candlist,uniname)):
            candlist.append(uniname)

    #Print results to terminal    
    print("Election Results")
    print("-----------------------------------")
    print(f" Total Votes:   {votecount}")
    print("-----------------------------------")
    
    #create and open .txt file
    file = open("PyPolloutfile.txt","w+") 
    #print results to .txt file
    file.write("Election Results\n") 
    file.write("-----------------------------------\n") 
    file.write(f" Total Votes:   {votecount}\n")
    file.write("-----------------------------------\n")
    
    #set winner percent 
    winnerpercent = 0
    
    #set loop to run thru candidate list and call candstats function
    for each in candlist:
        candstats(each)

    #Print winner to terminal
    print("-----------------------------------")
    print(f"Winner: {winner}")
    #Print winner to .txt file
    file.write("-----------------------------------\n")
    file.write(f"Winner: {winner}")
    