lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
x = [i for i in lista]
x.sort()
print(x)
x.reverse()
print(x)
x.sort()
print(x[1:len(x): 2])
print(x[0:len(x): 2])
print(x[2:len(x): 3])
