from math import *


def calculate_a(x: str, y: str) -> float:
    try:
        x = float(x)
        y = float(y)
    except:
        raise ValueError("X, Y и Z должны быть типа flat или int")

    return round((sqrt(abs(x-1))-cbrt(abs(y))) / (1 + (pow(x, 2)/2) + (pow(y, 2)/4)), 7)

def calculate_b(x: str, z: str) -> float:
    try:
        x = float(x)
        z = float(z)
    except:
        raise ValueError("X, Y и Z должны быть типа flat или int")

    return round(x*(atan(z)+exp(-(x+3))), 6)

if __name__ == '__main__':
    input_x = input('Введите x: ')
    input_y = input('Введите y: ')
    input_z = input('Введите z: ')

    a = calculate_a(input_x, input_y)
    b = calculate_b(input_x, input_z)

    print(f"a = {a}")
    print(f"b = {b}")