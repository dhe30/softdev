# NADH -- Nakib Abedin, Daniel He
# SoftDev pd08
# K06 -- working with a txt
# 2022-29-2022
#
# Disco
# QCC
# OPS
# 0) Store all of the information from the CSV file in a dictionary
# 1) 
#
#

def reading():
    file = open("occupations.csv", "r")
    retVal = {} #dictionary to be returned
    occs = list(file) #convert the CSV to a list
    occs.pop(0) # remove the first line because it is not a part of the data set
    for job in occs:
        if '"' in job:
           #different method to address names with commas 
        data = job.split(",") # seperates the job and the percentage
        job_title =  data[0]
        job_percentage = data[1][:-1]
reading()