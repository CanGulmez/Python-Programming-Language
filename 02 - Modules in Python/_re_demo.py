# DEMO 1 - RE (REGULAR EPRESSION) MODULE

import re 

print("Wellcome to Check Password Unit !!!")
print("-----------------------------------")

def checkPassword(yourPassword):

    passsword = input("Please, enter your password: ")

    if re.findall("[İÜüŞşÇçığĞ]", yourPassword):
        print("Your password can not contain turkish character !!!")
    elif re.search("0", yourPassword).start() == 0:
        print("Your password can not start with zero value !!!")
    elif re.findall(" ", yourPassword):
        print("Your password can not contain space character !!!")
    elif not re.findall("[^0-9]", yourPassword):
        print("Your password cantain numerical value !!!")
    elif not re.findall("[^a-zA-Z]", yourPassword):
        print("Your password cantain string value !!!")
    elif len(yourPassword) < 8:
        print("Your password have to be least 8 character")
    else:
        print("Your password is useful !!!")

# checkPassword(yourPassword=passsword)

# DEMO 2 - RE (REGULAR EXPRESSION) MODULE

file = open("C:/Users/90545/ARTIFICAL INTELLIGENCE/01 - Basics Python/Additional/_re_demo2.txt", mode="r", encoding="utf-8")

str_ = str(file.read())
print(str_)
result = re.findall("1969", str_)
print(result)

file.close()