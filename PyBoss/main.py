import os
import csv
import datetime


votecount = 0
candlist = []
votelist = []
uniname = ""
newlist = []
emplist = []
fnlist = []
lnlist = []
newdoblist = []
newssnlist = []
stateabblist = []



# stole this from geeksforgeeks.org and modified as needed - checks for name in list - True means it's NOT in the list
def check_in_list(list1, val): 
 
    # traverse in the list 
    for x in list1: 
  
        # compare with all the values 
        # with val 
        if val == x: 
            return False 
    return True


#borrowed from github
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}






def candstats(candidate):
    global winnerpercent
    global winner
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
     

boss_csv = os.path.join("employee_data.csv")

with open(boss_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    #print(csv_header)
    #check = input("this is csv header")
    #           print(csv_header)
    #           check = input("this is poll header")
    
    
    #newlist = ["Emp ID", "First Name","Last Name","DOB","SSN","State"]
    #print (newlist)
    #check = input("this is new list header")

       #csv_writer = csv.writer(newboss, delimiter=",")
# Specify the file to write to
    #output_path = os.path.join("PyBossoutfile.csv")

    # Open the file using "write" mode. Specify the variable to hold the contents
    #with open(output_path, 'w') as csvfile:
        # Initialize csv.writer
        #csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the first row (column headers)
        #csvwriter.writerow(["Emp ID", "First Name","Last Name","DOB","SSN","State"])

    for row in csv_reader:
        emplist.append(row[0])

        namesplit = row[1]
        first_last = namesplit.split(" ",1)
        #print(first_last)
        #check = input("first_last  list ")
        fnlist.append(first_last[0])
        lnlist.append(first_last[1])

        #print (newlist)
        #check = input("this is new list ")

        dob = row[2]
        datelist = dob.split("-")
        #print(datelist)
        #check = input("this is datelist")
        newdob = str(datelist[1])+"/"+str(datelist[2])+"/"+str(datelist[0])
        #print(newdob)
        #check = input("this is new dob")
        newdoblist.append(newdob)

        ssn = row[3]
        ssnlist = ssn.split("-")
        #print(ssnlist)
        newssn = "***-**-"+str(ssnlist[2])
        newssnlist.append(newssn)
        #print(newlist)

        staterow = row[4]
        #print(staterow)
        
        for key,value in us_state_abbrev.items():
            if key == staterow:
                #print(key)
                #print(staterow)
                stateabb = value
                # stateabb = Value
        #print(stateabb)
        #check = input("this is state abb")
        stateabblist.append(stateabb)

    newziplist = zip(emplist, fnlist, lnlist, newdoblist, newssnlist, stateabblist)
        #print(newlist)
        #check = input("this is the list for one pass thru")
    output_path = os.path.join("PyBossoutfile.csv")

    with open(output_path, 'w', newline="") as csvfile:
        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        # Write the new second row

        csvwriter.writerow(["Emp ID", "First Name","Last Name","DOB","SSN","State"])
            
        csvwriter.writerows(newziplist)
        
        # Three Lists
        #indexes = [1, 2, 3, 4]
        #employees = ["Michael", "Dwight", "Meredith", "Kelly"]
        #department = ["Boss", "Sales", "Sales", "HR"]

        # Zip all three lists together into tuples
        #roster = zip(indexes, employees, department)

        # save the output file path
        #output_file = os.path.join("output.csv")

        # open the output file, create a header row, and then write the zipped object to the csv
        #with open(output_file, "w") as datafile:
         #   writer = csv.writer(datafile)

         #   writer.writerow(["Index", "Employee", "Department"])

          #  writer.writerows(roster)

        


        #for uniname in range(len(candidatelist))
         #   if uniname != 
        #monthcount += 1   why doesn't this work
        #print(monthcount)
        #totalprofit = totalprofit + float(row[1])
        #print(totalprofit)
        #uniname = row[2]
        #votelist.append(uniname)
        #print (uniname)
        #if (check_in_list(candlist,uniname)):
        #   candlist.append(uniname)
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
    #print("Election Results")
    #print("-----------------------------------")
    #print(f" Total Votes:   {votecount}")
    #print("-----------------------------------")
    
    #file = open("PyBossoutfile.txt","w+") 
 
    #file.write(newlist) 
    #file.write("-----------------------------------\n") 
    #file.write(f" Total Votes:   {votecount}\n")
    #file.write("-----------------------------------\n")





    #winnerpercent = 0
    #for each in candlist:
    #   candstats(each)

    #print("-----------------------------------")
    #print(f"Winner: {winner}")
    #Print to file Winner
    #file.write("-----------------------------------\n")
    #file.write(f"Winner: {winner}")
    