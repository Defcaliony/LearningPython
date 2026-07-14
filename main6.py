#Робат з текстом
word = list('itproger')
word[0] = 'I'
print(len(word)) #кількість букв
print(word.count('o')) #кількість 1 символа
word.append('!')
result = ''.join(word)  #обєднує
print(result.upper()) #Всі символи у верхньому регістрі
print(result.lower()) #Всі символи у нижньому регістрі
print(result.capitalize()) #Перший символ у верхньому регістрі
print(result.isupper())
print(result.islower())