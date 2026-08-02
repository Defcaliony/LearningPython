#questions = []
#answers = []
#score = 0

questions = ["How old are you?",
             "Do you work?",
             "Is he smart?"]

answers = ["29", "yes", "so-so"]
score = 0

for i, q in enumerate(questions):
    user_answer = input(q + " ").lower().strip() #.lower() take all word small and .strep() delete space
    if user_answer == answers[i]:
        print("Correct")
        score += 1
    else:
        print("Oh nine" + answers[i]) #be must inside (....+answers[i])
print(f"\nYour score is {score} out of {len(questions)}")
