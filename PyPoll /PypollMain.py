#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:26:53 2018

@author: rulaothman
"""

#Import OS 
import os 
from collections import Counter

#write CSV path 
csvpath=os.path.join("csv","/Users/rulaothman/Desktop/python-challenge/PyPoll /election_data_2.csv")


#Import CSV
import csv
with open(csvpath, newline='') as csvfile: 
    #CSV reader delimiter and variable 
    csvreader= csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    
    #Make lists 
    voterid = []
    county = []
    candidates = []
    
    #Create for loop for every row 
    for dog in csvreader: 
        voterid.append(dog[0])
        county.append(dog[1])
        candidates.append(dog[2])
    
    #Find set of candidate and total vote using counter 
    can_set = set(candidates)
    tot_vote = len(voterid)
    cnt = Counter(candidates)
    
    #create a list with unique names 
    can_names= []
    
    for row in can_set: 
        can_names.append(row)
        
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {tot_vote}")
    print("-------------------------")
    
    dictionary_can={}
    can_count = 0
    for row in can_names: 
        candidate_name= str(can_names[can_count])
        votes = candidates.count(candidate_name)
        votes = int(votes)
        percentage = round(votes / tot_vote * 100,2)
        dictionary_can.update({ candidate_name : votes})
        print(f"{candidate_name}: {percentage}% ({votes} votes)")
        can_count = can_count + 1
    
    winner = max(dictionary_can, key=lambda key: dictionary_can[key])
    
    print("-------------------------")
    print("Winner: ",winner)

#Export results to a text file 

file_to_load = "/Users/rulaothman/Desktop/python-challenge/PyPoll /election_data_2.csv"
file_to_output = "/Users/rulaothman/Desktop/python-challenge/Pypoll /election_results.txt"

with open(file_to_output, 'w') as txt_file: 
    txt_file.write(f"Total Votes: {tot_vote}")
    txt_file.write("\n")
    txt_file.write(f"{candidate_name}: {percentage}% ({votes} votes)")
    txt_file.write("\n")
    txt_file.write("Winner: {winner} ")
    
    
        