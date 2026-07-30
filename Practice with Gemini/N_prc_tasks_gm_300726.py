tasks = []

while True:
    task = str(input("Enter your task there:"))

    if task == "":
        print("Please enter a task!")
        continue


    if task == "0":
        break

    tasks.append(task)

if not len(tasks):
    print("Your tasks is empty")
else:
    print("\n--- YOUR TASK TO-DO LIST ---")
    for index, item in enumerate(tasks, 1):
        print(f"{index}. {item}")
#print(tasks)
