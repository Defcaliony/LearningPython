#working with files
file = open('data/myfile.txt', 'r')
# print(file.read(10))
for line in file:
    print(line, end="")
file.close()
