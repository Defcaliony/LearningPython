import random as rnd #used the module

secret_number = rnd.randint(1,100)  #add random number
#user_number = int(input("Which number do you want? "))
user_number = 0  #create the var for cycle
attempts = 0  #initial number of attempts

print("I'm thinking of a number betwen 1 and 100")   #last com


while user_number != secret_number:                    #cycle<
    try:                                                #cycle for error<
        user_number = int(input("Enter your number: "))
    except ValueError:
        print("You Wrong, try again for number:")
        continue  # go to start cycle before error      #>cycle for error

    attempts += 1  #add 1 to attempts

    if user_number == secret_number:
        print("Correct")
    elif user_number > secret_number:
        print("Too high")
    else:
        print("Not enough!")                           #>cycle

print("You have used", attempts, "attempts")


#while user_number is None:
#    try:
#        user_number = int(input("Enter a number: "))
#    except ValueError:
#        print("You Wrong, try again to number")