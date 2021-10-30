print("Welcome to guess number.")
print("Guess number between 1 and 50.")
print("You just have 10 rigth.")
print("------------------------------------ ")

import random 

list_ = random.randint(0, 51)

def guess_number_game():

    right = 10
    score = 100

    while right > 0:

        guess_ = int(input("You guess: "))

        if guess_ == list_:

            print("Well done! Correct guess ...")
            print("Score: {}".format(score))
            print("----------------------------")
            break

        elif (guess_ < list_) and (0 <= guess_ <= 50):

            right -= 1
            score -= 10

            print("Wrong guess! Guess bigger number ...")
            print("Remaning right: {}".format(right))
            print("------------------------------------")

        elif (guess_ > list_) and (0 <= guess_ <= 50):

            right -= 1
            score -= 10

            print("Wrong guess! Guess smaller number ...")
            print("Remaning right: {}".format(right))
            print("------------------------------------ ")

        else:
            break

        if right == 0:
            print("Your right run out of ...")
            print("Number that chose computer was: {}".format(list_))
            break

guess_number_game()