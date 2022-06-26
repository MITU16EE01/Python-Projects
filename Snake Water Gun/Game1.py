import random

# Here we are making the decision
def game(comp, you):
    if comp == "s":
        if you == "w":
            return "lost"
        elif you == "g":
            return "won"
        else:
            return "darwed"
    elif comp == "w":
        if you == "s":
            return "won"
        elif you == "g":
            return "lost"
        else:
            return "darwed"
    elif comp == "g":
        if you == "s":
            return "lost"
        elif you == "w":
            return "won"
        else:
            return "darwed"


def again(a=0):
    if a == "yes":
        print("Computer turn: Snake(s) Water(w) or Gun(g)?")
        randNO = random.randint(1, 3)
        if randNO == 1:
            comp = "s"
        elif randNO == 2:
            comp = "w"
        elif randNO == 3:
            comp = "g"
        you = input("Your turn: Snake(s) Water(w) or Gun(g)?\n")
        result = game(comp, you)
        print(f"comp choose {comp}")
        print(f"you choose {you}")
        print(f"You {result} the game.")
        a = input("Do you want to play game again:\n (yes or No)\n")
        again(a)
    else:
        print("Thanks for Playing")

# To check if we want to run again
a = input("Do you want to play game:\n (yes or No)\n")
if a == "yes":
    again("yes")
else:
    print("No problem! Thank You!")
