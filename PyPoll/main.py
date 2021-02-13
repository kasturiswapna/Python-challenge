# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 23:05:20 2021

@author: kastu
"""
import os
import csv

#1.Open the csvfile
csvpath = os.path.join('Resources',"election_data.csv")

cnt = 0

#2.Read the csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    
#3.Loop through and perform calculations
for rows in csvreader:
    cnt = cnt + 1

#print the output to console            
print ("Election Results")
print ("================")
print ("Total Votes:"+ str(cnt))
print ("================")
print ("================")
print ("Winner: ")
print ("================")


# write the output to a text file
with open('Analysis/output.txt', 'w') as f:
    f.write ('Election Results')
    f.write ('\n')
    f.write('==================')
    f.write ('\n')
    f.write('Total Votes:'+ str(cnt))
    f.write ('\n')
    f.write('==================')
    f.write ('\n')
    f.write('==================')
    f.write ('\n')
    f.write('Winner:')
    f.write ('\n')
    f.write('==================')
