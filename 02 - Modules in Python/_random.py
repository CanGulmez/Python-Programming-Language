# RANDOM MODULE

import random

result = random.random()         # It gives one float value between 0 and 1.
result = random.randint(10, 20)  # It gives one integer value between values that you entered
result = random.uniform(10, 20)  # It gives one float value between values that you entered

print(result)

list_ = ["Python", "C#", "PHP", "HTML", "CSS", "R", "Go"]

result = random.choice(list_)       # It choice a value from list.
result = random.shuffle(list_)      # It shuffle the list.
result = random.sample(list_, 2)    

print(result)

# DEMO 1 - RANDOM MODULE

print("Wellcome to Random Module Demo ...")
print("----------------------------------")

def findRealValue():

    right = 5
    realValue = random.randint(1, 10)

    while 0 < right:

        right = right - 1
        guessValue = int(input("Guess: "))

        if 0 < guessValue < realValue:
            print("Upper! Remaining right is {}".format(right))
        elif guessValue == realValue:
            print("Well done. Right guess !!!")
            break
        elif 11 > guessValue > realValue:
            print("Lower! Remaining right is {}".format(right))
        else:
            print("Invalid value !!!")
            break
        
findRealValue()