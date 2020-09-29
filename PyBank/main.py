import os
import csv

#Variables and lists
monthcount = 0
totalprofit = 0
profitlist = []
m2mavg = []
m2mtotal = 0.0
m2mchange = 0.0
monthlist = []
m2mbestv = 0.0
m2mbestm = ""
m2mleastv = 0.0
m2mleastm = ""

#Find the relative path, open file and set the header
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    #Start For loop to gather monthcount, total profit, profitlist and monthlist
    for row in csv_reader:
        #variable to count months
        monthcount += 1
        
        #varible to sum total profit
        totalprofit = totalprofit + float(row[1])

        #create profitlist and monthlist
        profitlist.append(row[1])
        monthlist.append(row[0])
        
    #Start count loop to calculate m2mchange, m2mtotal, m2m average & get best/least months
    for i in range((monthcount-1)):
        
        #m2m change calculated
        m2mchange = float(profitlist[i+1])-float(profitlist[i])
        
        #set m2m value & date for best month
        if m2mchange > m2mbestv:
            #m2mbest = [monthlist[i+1], m2mchange]
            m2mbestm = str(monthlist[i+1])
            m2mbestv = m2mchange

        #set m2m value & date for worse month
        if m2mchange < m2mleastv:
            #m2mleast = [monthlist[i], m2mchange]
            m2mleastm = str(monthlist[i+1])
            m2mleastv = m2mchange

        #set m2m total
        m2mtotal = m2mtotal + m2mchange
        
        #set m2m average
        m2mavg = m2mtotal/(monthcount-1)#  
        
    #Print results to terminal    
    print("Financial Analysis")
    print("-------------------------------------------------------")
    print(f" Total Months:   {monthcount}")
    print(f" Average Change:   ${round(m2mavg,2)}")
    print(f" Greatest Increase in Profits:   {m2mbestm}   ${int(m2mbestv)}")
    print(f" Greatest Decrease in Profits:   {m2mleastm}   ${int(m2mleastv)}")
    
    #create and open .txt file
    file = open("PyBankoutfile.txt","w+") 
 
    #print results to .txt file
    file.write("Financial Analysis\n")
    file.write("-------------------------------------------------------\n") 
    file.write(f" Total Months:   {monthcount}\n")
    file.write(f" Average Change:   ${round(m2mavg,2)}\n")
    file.write(f" Greatest Increase in Profits:   {m2mbestm}   ${int(m2mbestv)}\n")
    file.write(f" Greatest Decrease in Profits:   {m2mleastm}   ${int(m2mleastv)}\n")
    