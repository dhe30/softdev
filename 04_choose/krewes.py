# <Frist> <Lsat>
# SoftDev
# K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
# 2022-09-22
# time spent: <elapsed time in hours, rounded to nearest tenth>

# DISCO: 2, 7, 8 is the period numbers
# QCC:
# OPS SUMMARY: randomly select one of the keys (2, 7, or 8) and within the randomly selected keys, randomly select an int that is between 0 and the array length. Return the devo that has that index within the array.
import random
# random.choice chooses random element from list - can use for within the array of devos once period is randomly selected
krewes = {2:["a","b","c"],7:["d","e","f"],8:["g","h","i"]}
periods = [2,7,8]
period = random.choice(periods)
devo = random.choice(krewes[period])
print(devo)

