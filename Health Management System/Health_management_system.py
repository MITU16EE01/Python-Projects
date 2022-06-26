def getdate():
    import datetime
    return  datetime.datetime.now()


def HMS_L():
    a = input("Enter the client name:")
    b = input("Enter the diet-D or exercise-E:")
    if b=="D":
        z = "diet"
    else:
        z = "exercise"
    try:
        with open(f"{a}.{b}.txt","x") as f:
            y  = input(f"Enter the {z} for {a}: ")
            f.write(f"[{getdate()}] {y}\n")
    except:
        with open(f"{a}.{b}.txt","a") as f:
            y = input(f"Enter the {z} for {a}: ")
            f.write(f"[{getdate()}] {y}\n")


def HMS_R():
    a = input("Enter the client name:")
    b = input("Enter the diet-D or exercise-E:")
    if b=="D":
        z = "diet"
    else:
        z = "exercise"
    try:
        with open(f"{a}.{b}.txt","r") as f:
            print(f.read())
    except:
        print(f"No history found for {a}'s {z}. Please create a file first")


def HMS(n):
    n +=1
    x = input("What do you want from HMS to:\n for Log Press {L}\n for retrive press {R}\n")
    if x == "L":
        HMS_L()
        print("Data Has been entered Sucessfully")
        rerun(n)
    elif x =="R":
        HMS_R()
        print("Thanks for checking the data")
        rerun(n)
    else:
        print("Check the input")
        HMS()


def rerun(n):
    while(n<1):
        HMS()
        n+=1
    else:
        run  = input("Do you want to use HMS again?\n{y}--For yes\n{N}--For no\n")
        if run == "Y":
            HMS(n)
        else:
            print("Thanks for Using HMS")


HMS(0)
