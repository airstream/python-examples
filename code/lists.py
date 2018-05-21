# LISTS

lista = ['a', 'b', '2']
listb = ['c', 'd', '4']

# length of list
print(len(lista))
# 3

# change first value of list "lista"
lista[0] = "1"
print(lista)
# ['1', 'b', '2']

# add value 3 and 5 to list "lista"
lista.append(3)
lista.append(5)
print(lista)
# ['1', 'b', '2', 3, 5]

# remove value 3 from list "lista"
lista.remove('b')
print(lista)
# ['1', '2', 3, 5]

# remove 1 index from list "lista"
lista.pop(0)
print(lista)
# ['2', 3, 5]

for i in lista:
    for j in listb:
        print(i, j)
# a c
# a d
# a 4
# b c
# b d
# b 4
# 2 c
# 2 d
# 2 4
