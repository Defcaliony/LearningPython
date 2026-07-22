# обробка вийнятків
try:
    a = 10
    b = int(input("Enter num: "))
    print(a / b)
except ValueError:    #Exceptoin не показує конкретну помилку
    print("No way")
except ZeroDivisionError:
    print("No way")
else:
    print("Good")
finally:
    print("Get home bitch")