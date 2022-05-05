# file = open('data.txt', 'r+')
# # r -> citire, fara adaugare, e default pt. open
# # w -> drept de scriere, creare fisier daca nu exista
# # a -> drept de adaugare, datele existente raman
# # r+ -> sdeschidere cu scriere & citire
#
# file.write("Hello2Hello")
# file.close()
# file = open('data3.txt', 'w')
# try:
#     file.write("hello")
# finally:
#     file.close()
#
# with open("data.txt", 'w') as file:
#     file.write("curs python1\n")
#     file.write("curs python2\n")
# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)
# with open('data.txt', 'r') as file:
#     for line in list(file):
#         print(line)
with open("data.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)