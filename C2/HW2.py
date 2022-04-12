lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lista_ascendenta = sorted(lista)
print(lista_ascendenta)
lista_descendenta = sorted(lista, reverse=True)
print(lista_descendenta)
lista_pare = [number for number in lista if number % 2 == 0]
print(lista_pare)
lista_impare = [number for number in lista if number % 2 == 1]
print(lista_impare)
lista_mult_trei = [number for number in lista if number % 3 == 0]
print(lista_mult_trei)
