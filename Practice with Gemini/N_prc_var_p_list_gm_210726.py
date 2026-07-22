import random as rnd #used the module

def show_history(history):                                      #functions 1
    #print("You have used", attempts, "attempts") #will not output attempts, this function down
    # print("See you history number:", history)
    print("See you history number:")
    for num in history:
        print("-", num)

def play_game():                                                #functions 2
    secret_number = rnd.randint(1,100)  #add random number
    user_number = 0  #create the var for cycle
    attempts = 0  #initial number of attempts
    history = []

    print("I'm thinking of a number betwen 1 and 100")   #last com


    while user_number != secret_number:                    #cycle<
        try:                                                #cycle for error<
            user_number = int(input("Enter your number: "))
        except ValueError:
            print("You Wrong, try again for number:")
            continue  # go to start cycle before error      #>cycle for error

        attempts += 1  #add 1 to attempts
        history.append(user_number)

        if user_number == secret_number:
            print("Correct")
        elif user_number > secret_number:
            print("Too high")
        else:
            print("Not enough!")                           #>cycle

    print("You have used", attempts, "attempts")
    show_history(history)



while True:
    play_game()                                             #go to F1 (F1/F2/...)

    again = input("\nDo you want to play again? (y/n): ").lower()       #if not wr '.lower()' you must write full yes or no
    if again != "y":
        print("Astalavista baby")
        break #finish cycle


#print(history)

#up to 3-8
#print("You have used", attempts, "attempts")
##print("See you history number:", history)
#print("See you history number:")
#for num in history:
#    print("-", num)

