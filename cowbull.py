import random


def rand_num():
    """Returns a number between 100 and 999."""
    randNum = str(random.randint(100, 999))
    return randNum


def user_num():
    """Asks user for a number between 100 and 999."""
    while True:
        try:
            userNum = int(input("Choose a number between 100 and 999: "))
        except ValueError:
            print("This isn't a number, try again.")
            print()
            continue
        if userNum < 100 or userNum > 999:
            print("Your number isn't between 100 and 999, try again.")
            print()
            continue
        else:
            break
    userNum = str(userNum)
    return userNum


def num_check(randNum, userNum):
    """Checks the number of bulls and cows."""
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
        cow = num_check(randNum, userNum)
        numTry += 1
        if bull == 3:
            print("Congratulation, You found the right number in " + str(numTry) + " guesses!")
            return False


if __name__=="__main__":
    game_loop()
