import random

matrix_size = random.randint(2, 10)

matrix = [[random.randint(0, 9) for _ in range(matrix_size)] for _ in range(matrix_size)]

print('Матрица:\n')
for row in matrix:
    print(' '.join(map(str, row)))

coord = [0, 0]
min_sum = matrix[coord[0]][coord[1]]

while sum(coord) < (matrix_size - 1) * 2:
    if coord[1] < len(matrix) - 1:
        coord[1] += 1
    else:
        coord[0] += 1
    
    temp_row = coord[0]
    temp_col = coord[1]
    temp_sum = 0
    while temp_row <= len(matrix)-1 and temp_col >= 0:
        temp_sum += matrix[temp_row][temp_col]
        temp_row += 1
        temp_col -= 1
    
    if temp_sum < min_sum:
        min_sum = temp_sum

print(f'\nМинимальная сумма диагонали, параллельной побочной: {min_sum}')