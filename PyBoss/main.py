import os
import csv

#Lists which will be zipped into a CSV file
emplist = []
fnlist = []
lnlist = []
newdoblist = []
newssnlist = []
stateabblist = []

#borrowed library from github
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

#Find the relative path, open file and set the header
boss_csv = os.path.join("employee_data.csv")

with open(boss_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    
    # set for loop to create emplist, fnlist, lnlist, newdoblist, newssnlist, stateabblist
    for row in csv_reader:
        emplist.append(row[0])

        #get first last name and split into 2 values and add to fnlist & lnlist
        namesplit = row[1]
        first_last = namesplit.split(" ",1)
        fnlist.append(first_last[0])
        lnlist.append(first_last[1])

        #get dob, split into 3 values, reorder the variables, create new dob & add to newdoblist
        dob = row[2]
        datelist = dob.split("-")
        newdob = str(datelist[1])+"/"+str(datelist[2])+"/"+str(datelist[0])
        newdoblist.append(newdob)

        #get ssn, split into 3 values, replace numbers with **'s, create new ssn & add to ssnlist
        ssn = row[3]
        ssnlist = ssn.split("-")
        newssn = "***-**-"+str(ssnlist[2])
        newssnlist.append(newssn)

        #get state info, use for list to search dict to return state abbreviation
        staterow = row[4]
        for key,value in us_state_abbrev.items():
            if key == staterow:
                stateabb = value
        stateabblist.append(stateabb)

    #create zip file from emplist, fnlist, lnlist, newdoblist, newssnlist & stateabblist
    newziplist = zip(emplist, fnlist, lnlist, newdoblist, newssnlist, stateabblist)
            
    #create oupt .csv file
    output_path = os.path.join("PyBossoutfile.csv")

    with open(output_path, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        
        #write .csv header
        csvwriter.writerow(["Emp ID", "First Name","Last Name","DOB","SSN","State"])
        #write zip file to rows in .csv file    
        csvwriter.writerows(newziplist)
