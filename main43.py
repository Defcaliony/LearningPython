#Оператори в циклах

for i in range(1, 11):

    if i % 2 == 0:
        continue #пропускає певну ітерацію

    if i == 7:
        break #повний вихід із циклу

    print("El:",i)