print("Wellcome to Number Arrangement Games !!!")

print("----------------------------------------")
print("The biggest number: BN")
print("The smallest number: SN")
print("----------------------------------------")

input_1 = int(input("How many value do you want to enter into app : "))
input_3 = input("What mode do you enter :")

def NAG(mode = input_3, values = input_1):

    list_ = []

    while 0 < values:

        values = values - 1

        input_2 = int(input("Value: "))

        list_.append(input_2)

        list_.sort()

    if mode == "BN":
        print("The biggest number is {}".format(list_[-1]))
    elif mode == "SN":
        print("The smallest number is {}".format(list_[0]))
    elif values == 1:
        pass
    else:
        print("Invalid value !!!")
    
NAG()