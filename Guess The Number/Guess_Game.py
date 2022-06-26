import random
count= 1 
n = random.randint(1,100)
while(count<=10):
     x= int(input("Enter the guess number between 1 and 100 including terminal value\n"))

     if x < n:
         print("Entered value is less than than actual value. Try again!""                ",10-count,"no. of trail left\n")
         count = count + 1
         continue
     elif x > n:
         print("Entered value is greater than than actual value. Try again!""              ",10-count,"no. of trail left\n")
         count = count + 1
         continue
     else:
         count = count
         print("You Won! in ",count,"trail" )
         break
else:
    print("You lost the game :( ")
