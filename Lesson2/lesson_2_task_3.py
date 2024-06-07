from math import ceil

def square(a):
    s = a ** 2
    return s

a = float(input("Длина стороны квадрата: "))
result = square(a)
rounding_up = ceil(result)
print(f"Округленная в большую сторону сумма: {rounding_up}")
