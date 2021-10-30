print("Well come to stone, paper, scissors game.")
print("stone ==> st \npaper ==> pa \nscissors ==> sc")
print("---------------")

import random

def stone_paper_scissors():

    right = 5
    your_score = 0
    computer_score = 0

    while right > 0:

        list_ = ["st", "pa", "sc"]
        x = random.choice(list_)

        input_ = input("Your choise (st, pa, sc): ")

        if input_ == "st" and x == "st":

            right = right - 1
            your_score = your_score + 0
            computer_score = computer_score + 0

            print("Draw !!!")
            print("Computer's choise is {}".format(x))
            print("Score: Computer ==> {}, You ==> {}".format(computer_score, your_score))
            print("--------------------------------")

        elif input_ == "st" and x == "pa":

            right = right - 1
            your_score = your_score + 0
            computer_score = computer_score + 1

            print("Computer won !!!")
            print("Computer's choise is {}".format(x))
            print("Score: Computer ==> {}, You ==> {}".format(computer_score, your_score))
            print("--------------------------------")

        elif input_ == "st" and x == "sc":

            right = right - 1
            your_score = your_score + 1
            computer_score = computer_score + 0

            print("You won !!!")
            print("Computer's choise is {}".format(x))
            print("Score: Computer ==> {}, You ==> {}".format(computer_score, your_score))
            print("--------------------------------")

        elif input_ == "pa" and x == "pa":

            right = right - 1
            your_score = your_score + 0
            computer_score = computer_score + 0

            print("Draw !!!")
            print("Computer's choise is {}".format(x))
            print("Score: Computer ==> {}, You ==> {}".format(computer_score, your_score))
            print("--------------------------------")

        elif input_ == "pa" and x == "sc":

            right = right - 1
            your_score = your_score + 0
            computer_score = computer_score + 1

            print("Computer won !!!")
            print("Computer's choise is {}".format(x))
            print("Score: Computer ==> {}, You ==> {}".format(computer_score, your_score))
            print("--------------------------------")

        elif input_ == "pa" and x == "st":

            right = right - 1
            your_score = your_score + 1
            computer_score = computer_score + 0

            print("You won !!!")
            print("Computer's choise is {}".format(x))
            print("Score: Computer ==> {}, You ==> {}".format(computer_score, your_score))
            print("--------------------------------")

        elif input_ == "sc" and x == "sc":

            right = right - 1
            your_score = your_score + 0
            computer_score = computer_score + 0

            print("Draw !!!")
            print("Computer's choise is {}".format(x))
            print("Score: Computer ==> {}, You ==> {}".format(computer_score, your_score))
            print("--------------------------------")

        elif input_ == "sc" and x == "st":

            right = right - 1
            your_score = your_score + 0
            computer_score = computer_score + 1

            print("Computer won !!!")
            print("Computer's choise is {}".format(x))
            print("Score: Computer ==> {}, You ==> {}".format(computer_score, your_score))
            print("--------------------------------")

        elif input_ == "sc" and x == "pa":

            right = right - 1
            your_score = your_score + 1
            computer_score = computer_score + 0

            print("You won !!!")
            print("Computer's choise is {}".format(x))
            print("Score: Computer ==> {}, You ==> {}".format(computer_score, your_score))
            print("--------------------------------")

        else:
            break

        if right == 0:
            print("Your right run out of...")

stone_paper_scissors()