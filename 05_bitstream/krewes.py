import random

def randomName():
    periods = list(krewes)
    period = random.choice(periods)
    devo = random.choice(krewes[period])
    print(devo + " from period " + str(period))

