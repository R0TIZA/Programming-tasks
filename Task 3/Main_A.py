from math import sin

if __name__ == '__main__':
    THRESHOLD = 1e-4
    x = float(input('Введите X: '))
    y = sin(x)
    while (abs(y)>=THRESHOLD):
        y = sin(y)
    print(f'Y = {y}')