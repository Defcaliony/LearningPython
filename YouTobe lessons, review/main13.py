#Менеджер "With...as"
try:
  with open('text.txt', 'r', encoding='utf-8') as file:
      print(file.read())
except FileNotFoundError:
    print("File not found")




#3file = open('text.txt', 'r')
#print(file.read())