# print("Mesaj in consola")
# variabila = 1
# print("Mesajul nr {}".format(variabila))
# raspuns_utilizator = input("Care este numele tau:")
# print(raspuns_utilizator)

# def functi_mea(param_1):
#     pass

def suma(a, b = 1):
    if type(a) == str:
        return a
    return a + b

suma_mea = suma(3, 4)
print(suma_mea)