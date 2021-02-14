# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 23:05:20 2021

@author: kastu
"""
import os
import csv

#1.Open the csvfile
csvpath = os.path.join("Resources","election_data.csv")

cnt = 0
khancnt = 0
correycnt = 0
licnt = 0
otooleycnt = 0

#2.Read the csvfile
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)
    
    #3.Loop through and perform calculations
    for rows in csvreader:
        cnt = cnt + 1
        if rows[2] == "Khan":
            khancnt = khancnt + 1
        elif rows[2] == "Correy": 
            correycnt = correycnt + 1
        elif rows[2] == "Li":
            licnt = licnt + 1
        elif rows[2] == "O'Tooley":
            otooleycnt = otooleycnt + 1
    
    if khancnt > correycnt and khancnt > licnt and khancnt > otooleycnt:
        winner = "Khan"
    elif correycnt > khancnt and correycnt > licnt and correycnt > otooleycnt:
        winner = "Correy"
    elif licnt > khancnt and licnt > correycnt and licnt > otooleycnt:
        winner  = "Li"
    elif otooleycnt > khancnt and otooleycnt > correycnt and otooleycnt > licnt:
        winner = "O'Tooley"
    
#print the output to console            
print ("Election Results")
print ("================")
print ("Total Votes:"+ str(cnt))
print ("================")
print ("Khan: "+ str(round(khancnt*100 /cnt,2)) +" (" + str(khancnt) +")")
print ("Correy: "+ str(round(correycnt*100 /cnt,2)) +" (" + str(correycnt) +")")
print ("Li: " + str(round(licnt*100 /cnt,2)) +" ("+ str(licnt) +")")
print ("O'Tooley: "+ str(round(otooleycnt*100 /cnt,2)) +" ("+ str(otooleycnt) +")")
print ("================")
print ("Winner: "+ winner)
print ("================")


# write the output to a text file
with open('Analysis/output.txt', 'w') as f:
    f.write ('Election Results')
    f.write ('\n')
    f.write ('==================')
    f.write ('\n')
    f.write ('Total Votes:'+ str(cnt))
    f.write ('\n')
    f.write ('==================')
    f.write ('\n')
    f.write ("Khan: "+ str(round(khancnt*100 /cnt,2)) +" (" + str(khancnt) +")")
    f.write ('\n')
    f.write ("Correy: "+ str(round(correycnt*100 /cnt,2)) +" (" + str(correycnt) +")")
    f.write ('\n')
    f.write ("Li: " + str(round(licnt*100 /cnt,2)) +" ("+ str(licnt) +")")
    f.write ('\n')
    f.write ("O'Tooley: "+ str(round(otooleycnt*100 /cnt,2)) +" ("+ str(otooleycnt) +")")    
    f.write ('\n')
    f.write ('==================')
    f.write ('\n')
    f.write ('Winner:' + winner)
    f.write ('\n')
    f.write ('==================')
