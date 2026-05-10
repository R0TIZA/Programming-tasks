INPUT_EXAMPLE = '''
Пример ввода:
1 2 3
4 5 6
7 8 9

*Размерность матрицы произвольная

'''

matrix = []
matrix.append([int(num) for num in input(f'{INPUT_EXAMPLE}Введите матрицу:\n').split(' ')])
for row_index in range(1, len(matrix[0])):
    matrix.append([int(num) for num in input('').split(' ')])

max_value = float("-inf")
coords = []

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        num = matrix[row_index][col_index]
        if num > max_value:
            max_value = num
            coords = []
            coords.append([row_index, col_index])
        elif num == max_value:
            coords.append([row_index, col_index])

for coord in coords:
    row_index = coord[0]
    col_index = coord[1]
    matrix[row_index][col_index] = 0

print('\nНовая матрица:\n')
for row in matrix:
    print(" ".join(map(str, row)))