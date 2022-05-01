variabila = input("Introdu un numar: ")
my_int = None

try:
    este_intreg = int(variabila)
    if my_int is None:
        raise ValueError
except ValueError as e:
    print(e.__doc__)
    print("Eroare de valoare", e)
except Exception as e:
    print(e.__doc__)
    print("A aparut o eroare", e)
else:
    print("Nu exista exceptii intalnite")
finally:
    print("Se ruleaza oricum")
print("Se ruleaza oricum")
