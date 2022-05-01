import datetime

print("Mesaj in consola")

variabila = 1
print("Mesajul nr {}".format(variabila))

raspuns_utilizator = input("Care este numele tau: ")
print(raspuns_utilizator)


def functia_mea():
    pass


def suma(a_func: int, b_func: int = 1) -> (int, int):
    """
    :param a_func: primul numar
    :param b_func: al doilea numar
    :return: suma, diferenta
    """
    if type(a_func) == str:
        return a_func, b_func
    return a_func + b_func, a_func - b_func


suma_mea, diferenta = suma(3, 4)
print(suma_mea, diferenta)


def my_function(*param_1):
    print(type(param_1))
    return param_1


print(my_function("string", 'strin1', 'string2'))


def suma_nr_infinite(param1, param2=1, *var):
    suma_func = 0
    for item in var:
        suma_func += item
    return suma_func


print(suma_nr_infinite(1, 2, 3, 4, 5, 6, 7))


def catalog(param1, *args, **kwargs):
    print(type(kwargs))
    return param1


print(catalog(1, nume="Ion", prenume="Vasile", varsta="12"))
print(catalog(1))


def suma(a_func_sum, b_func_sum):
    a_func_sum = diferenta(a_func_sum, b_func_sum)
    return a_func_sum + b_func_sum


def diferenta(a_func_diff, b_func_diff):
    return a_func_diff - b_func_diff


print(suma(diferenta(1, 2), 2))
print(suma(1, 2))

a, b = 10, 20

if a < b:
    min = a
else:
    min = b


min2 = a if a < b else b
print(min2)

lista_produse = ["ciocolata", 'suc', 'paine', 'mere', "apa"]
lista_noua = []
for x in lista_produse:
    if "a" in x:
        lista_noua.append(x)
lista_noua = [x for x in lista_produse if "a" in x]
lista_noua2 = [x if "a" in x else "b" for x in lista_produse]

print(lista_noua)
print(lista_noua2)

min = None
if suma := a + b:
    print(suma)
else:
    min = b

data = '05/05/05'
print(datetime.datetime.strptime(data, '%d/%m/%y'))
