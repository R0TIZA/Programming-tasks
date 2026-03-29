from math import *

if __name__ == '__main__':
    x = float(input('Введите x: '))
    y = float(input('Введите y: '))
    z = float(input('Введите z: '))

    a = (sqrt(abs(x-1))-cbrt(abs(y))) / (1 + (pow(x, 2)/2) + (pow(y, 2)/4))
    b = x*(atan(z)+exp(-(x+3)))

    print(f"a = {round(a, 7)}")
    print(f"b = {round(b, 7)}")