print("Wellcome to  Who can write faster game...")
print("-----------------------------------------")

from datetime import datetime

def writeFaster():
    
    start = datetime.now()
    
    str(input("Text: "))
    
    finish = datetime.now()

    print("--------------------------------")
    print("The passing time: {}".format(finish - start))
    
writeFaster()