#Робота з функціями working with functions

def info(word):
    print(word, end="")
    print("!")


def summa(a, b):
    res = a + b
    info(res)
    return res

res1 = summa(5, 6)
res2 = summa(5.6, 4.4)
res3 = summa("hi", " world")
print(res1)
