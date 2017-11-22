import random


def rand_num():
    """Returns the digits of a number between 100 and 999 in a list."""
    randNum = str(random.randint(100, 999))
    randDigitList = []
    for digit in randNum:
        randDigitList.append(digit)
    print(randDigitList)
    return randDigitList

def pcNum():
    pcNum = rand_num()
    

rand_num()
