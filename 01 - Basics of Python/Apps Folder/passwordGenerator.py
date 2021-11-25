print("Wellcome to Password Generator Application ...")

class PasswordGenerator:
    
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", 
            "l", "z", "x", "c", "v", "b", "n", "m"]

    def __init__(self, numberCount, smallLetterCount, lageLetterCount):
        
        self.numberCount = numberCount
        self.smallLetterCount = smallLetterCount
        self.largeLetterCount = lageLetterCount
        
        
    def generatePassword(self):
        
        import random
        
        newList = []
        
        numbers_ = random.sample(PasswordGenerator.numbers, self.numberCount)
        smallLetter_ = random.sample(PasswordGenerator.letters, self.smallLetterCount)
        largeLetter_ = random.sample(PasswordGenerator.letters, self.largeLetterCount)
                
        for i in smallLetter_:
            newList.append(i)
            
        for w in largeLetter_:
            newList.append(w.upper())
            
        for j in numbers_:
            newList.append(j)
        
        random.shuffle(newList)
        
        newPassword = ""
        
        for q in newList:
            
            newPassword = newPassword + str(q)   
            
        print(newPassword) 

input_1 = int(input("Number Count: "))
input_2 = int(input("Small Letter Count: "))
input_3 = int(input("Large Letter Count: "))
print("---------------------")
        
result = PasswordGenerator(numberCount = input_1, smallLetterCount = input_2, lageLetterCount = input_3)
result.generatePassword()