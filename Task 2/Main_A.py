def to_descending(x: str, y: str) -> (float, float):
    try:
        x = float(x)
        y = float(y)
    except:
        raise ValueError('X и Y должны иметь тип float или int')

    if x < y:
        return y, x

    return x, y

if __name__ == '__main__':
    input_x = input('Введите X: ')
    input_y = input('Введите Y: ')

    input_x, input_y = to_descending(input_x, input_y)

    print(f'X = {input_x}, Y = {input_y}')