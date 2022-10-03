# NADH -- Nakib Abedin, Daniel He
# SoftDev pd08
# K06 -- working with a txt
# 2022-29-2022
#
# Disco :
# 0) random.choices weights argument does not accept decimal values
# 1) rsplit splits the string starting from the last value
# QCC:
# OPS
# 0) Store all of the information from the CSV file in a dictionary
# 1) Moved all of the occupations to a list and their weighted chances into a list
# 2) Used random.choices method to generate a random choice that is weighted
#
import random
def reading():
    file = open("occupations.csv", "r")
    retVal = {} #dictionary to be returned
    occs = list(file) #convert the CSV to a list
    occs.pop(0) # remove the first line because it is not a part of the data set
    occs.pop(len(occs) - 1)
    for job in occs:
        if '"' in job:
           #different method to address names with commas
            data = job.rsplit(",", 1) # seperates the job and the percentage
            job_title =  data[0]
            job_percentage = data[1][:-1]
        else:
            data = job.split(",") # seperates the job and the percentage
            job_title =  data[0]
            job_percentage = data[1][:-1]
        retVal[job_title] = job_percentage
    return (retVal)

def weighted_occs():
    occs = reading()
    keys = list(occs)
    weight = []
    for e in keys:
        weight.append(float(occs[e])*10)
    select = random.choices(keys, weight)
    return (select)

#testing
def many_times():
    sum = 0
    for e in range(100000):
        job = weighted_occs()[0]
        #print (job)
        if job == 'Sales':
            sum += 1
    print (sum/1000)
    
many_times()