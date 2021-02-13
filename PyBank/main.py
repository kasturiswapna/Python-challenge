# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 23:05:20 2021

@author: kastu
"""
import os
import csv

#1.Open the csvfile
csvpath = os.path.join('Resources',"budget_data.csv")

cnt = 0
totalProfitLoss = 0
greatestmnt = ""
cgreatestinc = 0
fgreatestinc = 0
flowestinc = 0

#2.Read the csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    
#3.Loop through and perform calculations
for rows in csvreader:
    cnt = cnt + 1
    totalProfitLoss = totalProfitLoss + int(rows[1])
                
    fmonth = rows[0]
    cgreatestinc = int(rows[1])
        
    if (fgreatestinc < cgreatestinc):
        fgreatestinc = cgreatestinc
        fgrtmnth = fmonth            
     
    if (flowestinc > cgreatestinc):
        flowestinc = cgreatestinc
        flstmnth = fmonth

#print the output to console            
print ("Financial Analysis")
print ("==================")
print ("Total Months:"+ str(cnt))
print ("Total: $"+str(totalProfitLoss))
print ("Average Change: ")
print ("Greatest Increase in Profits: "+fgrtmnth+" ($"+str(fgreatestinc)+")")
print ("Greatest Decrease in Profits: "+flstmnth+" ($"+str(flowestinc)+")")

# write the output to a text file
with open('Analysis/output.txt', 'w') as f:
    f.write ('Financial Analysis')
    f.write ('\n')
    f.write('==================')
    f.write ('\n')
    f.write('Total Months:'+ str(cnt))
    f.write ('\n')
    f.write('Total: $'+str(totalProfitLoss))
    f.write ('\n')
    f.write('Average Change: ')
    f.write ('\n')
    f.write('Greatest Increase in Profits: '+fgrtmnth+' ($'+str(fgreatestinc)+')')
    f.write ('\n')
    f.write('Greatest Decrease in Profits: '+flstmnth+' ($'+str(flowestinc)+')')