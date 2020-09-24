import os
import csv

monthcount = 0
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



poll_csv = os.path.join("Resources", "election_data.csv")
# line should be budget_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(poll_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(csv_header)
    check = input("this is poll header")
    #with open(cereal_csv) as csv_file:
    #   csv_reader = csv.reader(csv_file, delimiter=",")
    #   csv_header = next(csv_file)
    for row in csv_reader:
        monthcount = monthcount +1
        #monthcount += 1   why doesn't this work
        #print(monthcount)
        totalprofit = totalprofit + float(row[1])
        #print(totalprofit)
        profitlist.append(row[1])
        monthlist.append(row[0])
        #print(profitlist)