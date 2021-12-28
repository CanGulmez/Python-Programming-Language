# DATETIME MODULE

import datetime

result = dir(datetime)
# print(result)

from datetime import time

result = time.fromisoformat("22:57")    # It creates time.
result = time.max
result = time.min
result = time.resolution
result = time.mro()                     # It shows type of object.

# print(result)

from datetime import date

result = date.fromisocalendar(year=2002, week=3, day=5)   # It give date.
result = date.fromisoformat("2002-03-15")                 # It creates date.
result = date.fromordinal(20)                             # It creates date but I do not understand how to define date.
result = date.fromtimestamp(20000)                        # It creates date but I do not understand how to define date.
result = date.max
result = date.min

# print(result)

from datetime import datetime

result = datetime.max
result = datetime.fromisoformat("2002-03-15 22:11:20")     # It creates a new datetime

result = datetime.now()
result = datetime.now().day
result = datetime.now().hour
result = datetime.now().year               # ==> You know what does it do these block.
result = datetime.now().microsecond
result = datetime.now().month
result = datetime.today()

# print(result)

print("---------------------------------------------------------")

# DEMO 1 - DATETIME MODULE

import random
from datetime import time, date, datetime

def produceArtificialTime():

    artificialHour = random.randint(0, 23)
    artificialMinute = random.randint(0, 59)
    artificialSecond = random.randint(0, 59)

    if len(str(artificialHour)) == 1 and len(str(artificialMinute)) == 1 and len(str(artificialSecond)) == 1:
        artificialTime = time.fromisoformat("0" + str(artificialHour) + ":0" + str(artificialMinute) + ":0" + str(artificialSecond))

    elif len(str(artificialHour)) == 1 and len(str(artificialMinute)) == 1 and len(str(artificialSecond)) == 2:
        artificialTime = time.fromisoformat("0" + str(artificialHour) + ":0" + str(artificialMinute) + ":" + str(artificialSecond))

    elif len(str(artificialHour)) == 1 and len(str(artificialMinute)) == 2 and len(str(artificialSecond)) == 2:
        artificialTime = time.fromisoformat("0" + str(artificialHour) + ":" + str(artificialMinute) + ":" + str(artificialSecond))

    elif len(str(artificialHour)) == 1 and len(str(artificialMinute)) == 2 and len(str(artificialSecond)) == 1:
        artificialTime = time.fromisoformat("0" + str(artificialHour) + ":" + str(artificialMinute) + ":0" + str(artificialSecond))

    elif len(str(artificialHour)) == 2 and len(str(artificialMinute)) == 1 and len(str(artificialSecond)) == 2:
        artificialTime = time.fromisoformat(str(artificialHour) + ":0" + str(artificialMinute) + ":" + str(artificialSecond))

    elif len(str(artificialHour)) == 2 and len(str(artificialMinute)) == 2 and len(str(artificialSecond)) == 1:
        artificialTime = time.fromisoformat(str(artificialHour) + ":" + str(artificialMinute) + ":0" + str(artificialSecond))

    elif len(str(artificialHour)) == 2 and len(str(artificialMinute)) == 1 and len(str(artificialSecond)) == 1:
        artificialTime = time.fromisoformat(str(artificialHour) + ":0" + str(artificialMinute) + ":0" + str(artificialSecond))

    elif len(str(artificialHour)) == 2 and len(str(artificialMinute)) == 2 and len(str(artificialSecond)) == 2:
        artificialTime = time.fromisoformat(str(artificialHour) + ":" + str(artificialMinute) + ":" + str(artificialSecond))
    else:
        pass

    print("Produced time: {}".format(artificialTime))

    realHour = datetime.now().hour
    realMibute = datetime.now().minute
    realSecond = datetime.now().second

    if len(str(realHour)) == 1 and len(str(realMibute)) == 1 and len(str(realSecond)) == 1:
        realTime = time.fromisoformat("0" + str(realHour) + ":0" + str(realMibute) + ":0" + str(realSecond))

    elif len(str(realHour)) == 1 and len(str(realMibute)) == 1 and len(str(realSecond)) == 2:
        realTime = time.fromisoformat("0" + str(realHour) + ":0" + str(realMibute) + ":" + str(realSecond))

    elif len(str(realHour)) == 1 and len(str(realMibute)) == 2 and len(str(realSecond)) == 2:
        realTime = time.fromisoformat("0" + str(realHour) + ":" + str(realMibute) + ":" + str(realSecond))

    elif len(str(realHour)) == 1 and len(str(realMibute)) == 2 and len(str(realSecond)) == 1:
        realTime = time.fromisoformat("0" + str(realHour) + ":" + str(realMibute) + ":0" + str(realSecond))

    elif len(str(realHour)) == 2 and len(str(realMibute)) == 1 and len(str(realSecond)) == 2:
        realTime = time.fromisoformat(str(realHour) + ":0" + str(realMibute) + ":" + str(realSecond))

    elif len(str(realHour)) == 2 and len(str(realMibute)) == 2 and len(str(realSecond)) == 1:
        realTime = time.fromisoformat(str(realHour) + ":" + str(realMibute) + ":0" + str(realSecond))

    elif len(str(realHour)) == 2 and len(str(realMibute)) == 1 and len(str(realSecond)) == 1:
        realTime = time.fromisoformat(str(realHour) + ":0" + str(realMibute) + ":0" + str(realSecond))

    elif len(str(realHour)) == 2 and len(str(realMibute)) == 2 and len(str(realSecond)) == 2:
        realTime = time.fromisoformat(str(realHour) + ":" + str(realMibute) + ":" + str(realSecond))
    else:
        pass

    print("Real time: {}".format(realTime))

produceArtificialTime()