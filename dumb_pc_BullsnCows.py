import random


def rand_num():
    """Returns a number between 1000 and 9999."""
    randNum = str(random.randint(100, 999))
    return randNum


def user_num():
    """Generates a random 'user' number between 1000 and 9999."""
    userNum = str(random.randint(100, 999))
    return userNum
    

def num_check(randNum, userNum):
    """Checks the number of cows and bulls."""
    bull = 0
    cow = 0
    for i in range(0, 3):
        if userNum[i] == randNum[i]:
            bull += 1
        else:
            cow += 1
    print("You have " + str(bull) + " bull(s) and you have " + str(cow) + " cow(s).")
    print()
    return bull


def game_loop():
    """Loops the game until the user finds the right number."""
    randNum = rand_num()
    numTry = 1
    while True:
        print("Guess #" + str(numTry))
        userNum = user_num()
        bull = num_check(randNum, userNum)
        numTry += 1
        if bull == 3:
            print("Congratulation, You found the right number in " + str(numTry) + " guesses!")
            return False


if __name__=="__main__":
    game_loop()
