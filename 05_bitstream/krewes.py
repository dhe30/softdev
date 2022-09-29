# 
# SoftDev
# K05 --
# 2022-09-28
# time spent: 

# DISCO:  
# QCC:
# OPS SUMMARY: 
import random

def populate():
    file = open("krewes.txt", "r")
    data = file.read().split("@@@") #the list version of file object
    dic = {}
    for e in data:
        s = e.split("$$$")
        if s[0] in dic:
            dic[s[0]] = dic[s[0]] + [s[1],s[2]]
        else:
            dic[s[0]] = [s[1],s[2]]
    return dic
    
def randomName():
    periods = list(krewes)
    period = random.choice(periods)
    devo = random.choice(krewes[period])
    print(devo + " from period " + str(period))

dictionary = populate()
print(dictionary["7"])

