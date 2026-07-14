# Цикл while
"""i = 16
while i >= 2:
    print(i)
    i += 1"""

#Практичне використання
work = True
while work:
    user_input = input("Enter work STOP: ")
    if user_input == 'STOP':
        work = False
print("While loop is done")