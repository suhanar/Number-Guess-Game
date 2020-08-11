from random import random
from random import randint



attempt = 0
ran1 = randint(1,10)
#print(ran1)



dec=input("Haii Welcome to the number guessing game do you want to play the game Yes/No : ")
name = input("First enter your name : ")
print("Hai {} welcome ".format(name))
print("First you need to guess a number between 0 to 10 you have 3 chances for guessing the correct number ")
#ran = randint(0,10)



while dec.lower() == 'yes':
    try:
        attempt += 1

        ran=ran1




        num = int(input("Enter the number : "))
        if(num<=10 and num>0):
            if(num==ran):

                print("you got it")
                print("you got answer in {} attempts ".format(attempt))
                dec=input("Do you want to play again Yes/No : ")
                ran1=randint(1,10)
                attempt= 0

            elif(num>ran):

                print("random number is lower than your number")
            elif(num<ran):

                print("random number is higher than your number")
        else:

            print("please enter number in between 1 and 10")
    except ValueError as err:
        print("Its not even a number please enter valid number")
        print(err)







else:
    print("That's ok see you ")
    exit()
