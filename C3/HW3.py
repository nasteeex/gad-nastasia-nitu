def my_function(*args, **kwargs) -> float:
    """This function returns the sum of the numeric parameters"""
    suma = 0
    for elem in args:
        if type(elem) == int or type(elem) == float:
            suma += elem
    return float(suma)


def sum_up_to_n(n: int) -> int:
    """This function returns the sum of all numbers up to n"""
    return sum(range(n + 1))


def sum_of_even(n: int) -> int:
    """This function returns the sum of all even numbers up to n"""
    if n <= 0:
        return 0
    if not n % 2 == 0:
        return sum_of_even(n-1)
    else:
        return n + sum_of_even(n-1)


def sum_of_odd(n: int) -> int:
    """This function returns the sum of all even numbers up to n"""
    if n <= 0:
        return 0
    if n % 2 == 0:
        return sum_of_odd(n-1)
    else:
        return n + sum_of_odd(n-1)


def is_int() -> bool:
    """This function returns True if the n input is of type int, Flase otherwise"""
    try:
        n = int(input("Anything: "))
        return True
    except ValueError:
        return False


print(my_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', param_1=2))

print(sum_up_to_n(0))
print(sum_of_even(0))
print(sum_of_odd(0))

print(sum_up_to_n(3))
print(sum_of_even(3))
print(sum_of_odd(3))

print(sum_up_to_n(6))
print(sum_of_even(6))
print(sum_of_odd(6))

print(is_int())