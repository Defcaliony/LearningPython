#dictionaries словники ключі
person = {'name': 'Alex', 'age': 15, 5: 12, True: 'False', (3, 5): 45}
#person[5] = 'Five'
#print(person[5])

person1 = dict(name='Alex', age=15)
#print(person1['name'])


#for key, values in person.items():
#    print(key, values, sep=" - ")

for el in person.values(): #вивести тільки значення
    print(el)
for el in person.keys(): #вивести тільки ключі
    print(el)