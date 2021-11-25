print("Wellcome to Average Calculation Application !!!")
print("-----------------------------------------------")

input_1 = int(input("How many values do you want to enter into apps: "))

input__ = input_1
total = 0

while 0 < input_1:

    input_1 = input_1 - 1

    input_2 = int(input("Value: "))

    if input_2:

        total += input_2
        average = total / input__
    
print("Average is {}".format(average))