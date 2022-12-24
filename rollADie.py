import random

oneDie = " ------- \n |     | \n |  0  | \n |     | \n -------"
twoDie = " ------- \n |   0 | \n |     | \n | 0   | \n -------"
threeDie = " ------- \n | 0   | \n |  0  | \n |   0 | \n -------"
fourDie = " ------- \n | 0 0 | \n |     | \n | 0 0 | \n -------"
fiveDie = " ------- \n | 0 0 | \n |  0  | \n | 0 0 | \n -------"
sixDie = " ------- \n | 0 0 | \n | 0 0 | \n | 0 0 | \n -------"

def roll1():
    roll = random.randint(1, 6)
    if roll == 1:
        print(oneDie)
    elif roll == 2:
        print(twoDie)
    elif roll == 3:
        print(threeDie)
    elif roll == 4:
        print(fourDie)
    elif roll == 5:
        print(fiveDie)
    else:
        print(sixDie)


if __name__ == "__main__":
    userinput = input("Enter number of die to roll: ")
    for i in range(int(userinput)):
        roll1()