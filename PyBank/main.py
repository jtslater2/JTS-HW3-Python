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
#2mbest = ["year-month", "0"]
#m2mleast = ["year-month", "0"]
m2mtotal = 0.0
m2mchange = 0.0
monthlist = []
m2mbestv = 0.0
m2mbestm = ""
m2mleastv = 0.0
m2mleastm = ""







budget_csv = os.path.join("Resources", "budget_data.csv")
# line should be budget_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    #with open(cereal_csv) as csv_file:
    #   csv_reader = csv.reader(csv_file, delimiter=",")
    #   csv_header = next(csv_file)
    for row in csv_reader:
        monthcount += 1
        #monthcount += 1   why doesn't this work
        #print(monthcount)
        totalprofit = totalprofit + float(row[1])
        #print(totalprofit)
        profitlist.append(row[1])
        monthlist.append(row[0])
        #print(profitlist)
        
        
        #nextrow = next(csv_reader)
        #print(nextrow)



        #   temp   profit = (int(row[1]) + int(nextrow[1]))/2
        #   temp   print(profit)
    for i in range((monthcount-1)):
        
        #print(i)
        #check = input("this is i")
        #print(len(profitlist))
        #check = input("this is profitlist length")

        #print (profitlist[i])
        #print (profitlist[i+1])
        
        #  don't need print((float(profitlist[i])+float(profitlist[i+1]))/2)

        #check = input("this is float i and  i+1 ")

        m2mchange = float(profitlist[i+1])-float(profitlist[i])
        #print (m2mchange)
        #check = input('this is m2mchange')

        if m2mchange > m2mbestv:
            # if m2mchange > float(m2mbest[1]):
            #m2mbest = [monthlist[i+1], m2mchange]
            m2mbestm = str(monthlist[i+1])
            m2mbestv = m2mchange

        #print (m2mbest)
        #check = input("this is the best m2m")

        #if m2mchange < float(m2mleast[1]):
        if m2mchange < m2mleastv:
            #m2mleast = [monthlist[i], m2mchange]
            m2mleastm = str(monthlist[i+1])
            m2mleastv = m2mchange

        #print (m2mleast)
        #check = input("this is the least m2m")

        m2mtotal = m2mtotal + m2mchange
        #print(m2mtotal)
        #check = input("this is m2mtotal")


        m2mavg = m2mtotal/(monthcount-1)#  
        #print (m2mavg)
        #check = input("this is the m2m change average")
        #avgtotal = float(profitlist(i) + profitlist[i+1]
        #print(avgtotal)
        #check2 = input("this is avg total")
        #avechange = (profitlist[i] + profitlist[i+1])/2
        #print(avechange)
        #check = input("is this right")
        #nextentry = int(entry)+1

        
        #print(nextentry)
        #nextentry = str(nextentry)


        #check = input("is this right")
        #avgchange = int(profitlist[int(entry)])
        #print(avgchange)
    #m2mavg = m2mtotal/len(monthlist-2)
    #print (m2mavg)
    #check = input("this is the m2m change average")

    print("Financial Analysis")
    print("-------------------------------------------------------")
    print(f" Total Months:   {monthcount}")
    print(f" Average Change:   ${round(m2mavg,2)}")
    print(f" Greatest Increase in Profits:   {m2mbestm}   ${int(m2mbestv)}")
    print(f" Greatest Decrease in Profits:   {m2mleastm}   ${int(m2mleastv)}")
    
    
    file = open("PyBankoutfile.txt","w+") 
 
    file.write("Financial Analysis\n")
    file.write("-------------------------------------------------------\n") 
    file.write(f" Total Months:   {monthcount}\n")
    file.write(f" Average Change:   ${round(m2mavg,2)}\n")
    file.write(f" Greatest Increase in Profits:   {m2mbestm}   ${int(m2mbestv)}\n")
    file.write(f" Greatest Decrease in Profits:   {m2mleastm}   ${int(m2mleastv)}\n")
    