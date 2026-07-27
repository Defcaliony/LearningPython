expenses = []   # 1.

def show_expenses(my_list):   #6.
    print("\n--- You expenses ---")
    for item in my_list:
        print("-", item)

    total = sum(my_list)
    print("Total:", total)


while True:   #3.
    try:
        user_exp = int(input("What is number?: "))   #2.
    except ValueError:
        print("Please you must enter number only")
        continue

    if user_exp == 0:   #4.
        break
    else:
        expenses.append(user_exp)   #5.

#print(user_exp) 3. or (expenses)
show_expenses(expenses)   #7.