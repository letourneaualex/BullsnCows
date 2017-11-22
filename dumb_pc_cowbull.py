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
    cow = 0
    bull = 0
    for i in range(0, 3):
        if userNum[i] == randNum[i]:
            cow += 1
        else:
            bull += 1
    print("You have " + str(cow) + " cow(s) and you have " + str(bull) + " bull(s).")
    print()
    return cow


def game_loop():
    """Loops the game until the user finds the right number."""
    randNum = rand_num()
    numTry = 1
    while True:
        print("Guess #" + str(numTry))
        userNum = user_num()
        cow = num_check(randNum, userNum)
        numTry += 1
        if cow == 3:
            print("Congratulation, You found the right number in " + str(numTry) + " guesses!")
            return False


if __name__=="__main__":
    game_loop()
