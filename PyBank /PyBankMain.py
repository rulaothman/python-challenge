
#Pybank

#Import OS
from statistics import mean
import os

#write CSV path 
csvpath=os.path.join("CSV","/Users/rulaothman/Desktop/python-challenge/PyBank /budget_data_1.csv")


#Improved Reading using CSV module 
import csv
with open(csvpath, newline='') as csvfile: 
    #CSV reader delimiter and variable 
    csvreader= csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    csvlist=list(csvreader)
    
    #list creation
    dates = []
    revenues = []
    
    #run for loop for every row 
    for dog in csvlist:
        dates.append(dog[0])
        revenues.append(int(dog[1]))
    
    #create revenue change list 
    revchange = []
    
    #run loop through revenues to find the month-to-month change 
    revchange= [revenues[i+1] - revenues[i] for i in range(len(revenues)-1)]
    
    #variables 
    max_change = max(revchange)
    big_loss = min(revchange)
    avg_change = mean(revchange)
    total_month = len(dates)
    max_month = None 
    loss_month = None
    total_revenue= sum(revenues)
    
    #Use for loop to find corresponding date 
    initial_val = None
    for row in csvlist: 
        if initial_val is None: 
            initial_val= int(row[1])
            continue 
        if abs(int(row[1]) - initial_val) == big_loss:
            loss_month= row[0]
        initial_val = int(row[1])
    
    initial_val2= None
    for row in csvlist: 
        if initial_val2 is None: 
            initial_val2 = int(row[1])
            continue 
        if abs(int(row[1]) -initial_val2) == max_change: 
            max_month = row[0] 
        initial_val2 = int(row[1])
        
    print("Financial Analysis")
    print("--------------------------------------------------------")
    print(f"Total Months: {total_month}")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Average Revenue Change: ${avg_change}")
    print(f"Greatest Increase in Revenue: {max_month} ${max_change}")
    print(f"Greatest Decrease in Revenue: {loss_month} ${big_loss}")

#Export results to a text file 
file_to_load = "/Users/rulaothman/Desktop/python-challenge/PyBank /budget_data_2.csv"
file_to_output = "/Users/rulaothman/Desktop/python-challenge/PyBank /budget_analysis.txt"    

with open(file_to_output, 'w') as txt_file: 
    txt_file.write(f"Total Months: {total_month}")
    txt_file.write("\n")
    txt_file.write(f"Total Revenue: ${total_revenue}")
    txt_file.write("\n")
    txt_file.write(f"Average Revenue Change: ${avg_change}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Revenue: {max_month} ${max_change}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Revenue: {loss_month} ${big_loss}")

        
