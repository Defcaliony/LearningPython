#Робота з текстом
from main6 import result

text = 'football,basketball,skate,drive'
hobbies = text.split(',')

for i in range(0, len(hobbies)):
    hobbies[i] = hobbies[i].capitalize()

result = ",".join(hobbies)
print(result)