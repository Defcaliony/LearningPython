#Вийнятки обробка
num = None

while num is None:      # або через == замість *is*
    try:
        num = int(input("Enter num: "))
        num += 5
        print(num)
    except ValueError:
        print("Ви ввели щось не те")