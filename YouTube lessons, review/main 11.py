#working with files
data = input("Hobby: ")
file = open('../data/myfile.txt', 'a')
file.write(data + '\n')
file.close()
