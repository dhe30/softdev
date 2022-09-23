# Shafiul Haque, Selena Ho, Daniel He
# SoftDev
# K04 -- Krewes/ Dictionary and random selection/ We learned dictionary syntax and we learned random. methods.
# 2022-09-22
# time spent: 1.3

# DISCO: 2, 7, 8 is the period numbers; random.choice chooses random element from list - can use for within the array of devos once period is randomly selected
# QCC:
# OPS SUMMARY: We used list() to create an array of keys in the dictionary, from there we used random.choice(<the array of keys>) to randomly select a period. We assigned that period to a variable and then used random.choice() again to randomly return an element from that period.
import random
krewes = {
           2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "RUIWEN"], 
           7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "KAREN"],
           8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "WANYING", "KEVIN"]
         }

# original method
periods = list(krewes)
period = random.choice(periods)
devo = random.choice(krewes[period])
print(devo + " from period " + str(period))

"""
#doing it with randint
periods = list(krewes)
period = periods[random.randint(0, len(periods))]
devo = krewes[period][random.randint(0, len(krewes[period]))]
print(devo)
"""