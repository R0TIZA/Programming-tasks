if __name__ == '__main__':
    x = float(input('Введите X: '))
    y = float(input('Введите Y: '))
    if (x<y):
        z = x
        x = y
        y = z
    print(f'X = {x}, Y = {y}')