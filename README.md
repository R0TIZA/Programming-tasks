## Решение задач по программированию

**Студент:** Калинин М. М.  
**Вариант:** 17

---

### Задача 1

Даны $x$, $y$, $z$. Вычислить $a$, $b$, если:

$$
a = \frac{\sqrt{|x-1|} - \sqrt[3]{|y|}}{1 + \frac{x^2}{2} + \frac{y^2}{4}}
$$

$$
b = x \bigl( \text{arctg } z + e^{-(x+3)} \bigr)
$$

Решение на Python:

```python
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
```

---

### Задача 2

#### А (Задачи на применение оператора `if … else …`)

Перераспределить значения переменных $X$ и $Y$ так, чтобы в $X$ оказалось большее из этих значений, а в $Y$ – меньшее.

Решение на Python:

```python
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
```

#### Б (Задачи на применение оператора выбора `switch … case …`)

По введённой цифре:
- $1$ — хлопок,
- $2$ — синтетика,
- $3$ — шерсть,
- $4$ — быстрая стирка,

Программа выводит рекомендуемую температуру и длительность стирки.

Решение на Python:

```python
def get_mode_text(mode: str) -> str:
    try:
        mode = int(mode)
    except:
        raise ValueError('Режим должен быть типа int')

    match mode:
        case 1:
            return '''Рекомендуемые параметры для режима стирки \'Хлопок\':
                      Температура: 30-40°C
                      Время стирки: 1-2 часа
                      '''
        case 2:
            return '''Рекомендуемые параметры для режима стирки \'Синтетика\':
                      Температура: 30-40°C
                      Время стирки: 45-60 минут
                      '''
        case 3:
            return '''Рекомендуемые параметры для режима стирки \'Шерсть\':
                      Температура: 20-30°C
                      Время стирки: 40-55 минут
                      '''
        case 4:
            return '''Рекомендуемые параметры для режима стирки \'Быстрая стирка\':
                      Температура: 30-40°C
                      Время стирки: 15-30 минут
                      '''
        case _:
            return 'Неизвестный режим стирки!'

if __name__ == '__main__':
    input_mode = input('Введите режим работы (1-4): ')
    print(get_mode_text(input_mode))
```

---

### Задача 3

#### А (Задачи для применения цикла с предусловием или с постусловием)

Вычислить $y$ — первое из чисел $\sin x$, $\sin \sin x$, $\sin \sin \sin x$, $\dots$, меньшее по модулю $10^{-4}$.

Решение на Python:

```python
from math import sin

if __name__ == '__main__':
    THRESHOLD = 1e-4
    x = float(input('Введите X: '))
    y = sin(x)
    while (abs(y)>=THRESHOLD):
        y = sin(y)
    print(f'Y = {y}')
```

#### Б (Задачи для применения цикла с параметром)

Дано $10$ вещественных чисел. Определить, образуют ли они возрастающую последовательность.

Решение на Python:

```python
if __name__ == '__main__':
    nums = [float(num) for num in input('Введите последовательность числе через пробел:\n').split(' ')]
    previous = nums[0]
    isIncreasing = True
    for num in nums:
        if num < previous:
            isIncreasing = False
            break
        previous = num
    print(f'Числа {'не ' if not isIncreasing else ''}образуют возрастающую последовательность')
```

### Задача 4

#### А (Задачи на одномерные массивы)

В массиве из 10 чисел переставить все нули в конец массива, не меняя порядок ненулевых элементов.

**Контрольный пример:**  
Исходный массив: `[1, 0, 3, 4, 0, 0, 7, 0, 9, 10]`  
Результат: `[1, 3, 4, 7, 9, 10, 0, 0, 0, 0]`

Решение на Python:

```python
nums = [int(num) for num in input('Введите массив чисел через пробел:\n').split(' ')]
zero_counter = 0
for num_index in range(len(nums)):
    if nums[num_index] == 0:
        zero_counter += 1
    else:
        nums[num_index-zero_counter] = nums[num_index]
    
    if len(nums) - (num_index + 1) <= zero_counter:
        nums[num_index] = 0

print(f'Отсортированный массив: {nums}')
```

#### Б (Задачи на двумерные массивы)

Все элементы с наибольшим значением в данной целочисленной квадратной матрице порядка 6 заменить нулями. 

Решение на Python:

```python
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
```

---

### Задача 5

#### А (Организация данных в подпрограммах)

Напишите функцию, вычисляющую, минимум среди сумм элементов диагоналей, параллельных побочной диагонали. Элементы массива заполнять случайными числами, используя генератор случайных чисел.

Решение на Python:

```python
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
```

---

### Задача 6

#### А (Работа со строками)

Дана фраза, в которой, кроме букв, имеются пробелы. Проверить, является ли она палиндромом без учета пробелов (например, фраза палиндромом является). 

Решение на Python:

```python
input_string = input('Введите строку: ').replace(' ', '').lower()
is_palindrome = True

for char_index in range((len(input_string)-1)//2):
    left_char = input_string[char_index]
    right_char = input_string[len(input_string) - 1 - char_index]
    if left_char != right_char:
        is_palindrome = False
        break

print(f'Строка {"" if is_palindrome else "не "}является палиндромом.')
```

---

### Задача 7

#### А (Задачи на создание и запись файла)

Написать программу, которая записывает в файл 10 произвольных чисел кратных 3 или 7. Список при поиске числе не использовать.

Решение на Python:

```python
import random

FILE_NAME = './Task 7/File_A.txt'
nums = []

while len(nums) < 10:
    num = random.randint(1, 10**5)
    if(num%3 == 0 or num%7 == 0):
        nums.append(num)


with open(file=FILE_NAME, mode='w') as file:
    file.write(', '.join(map(str, nums)))
```

#### Б (Задачи на создание файла, его запись  и считывание из файла)

Написать программу, которая с начала записывает текст в файл, затем считывает текст из файла и выводит его на экран, после каждого предложения добавляя, сколько раз встретилось в нем введенное с клавиатуры слово.

Решение на Python:

```python
FILE_NAME = './Task 7/File_B.txt'

input_string = input('Введите текст:\n')

with open(FILE_NAME, 'r+', encoding='utf-8') as file:
    file.write(input_string)
    file.seek(0)
    sentences_from_file = [sentence for sentence in file.read().split('.') if sentence]
    word = input('\nВведите слово: ')
    print('')
    for sentence in sentences_from_file:
        occurrences_amount = sentence.count(word)
        print(f'{sentence}. Количество вхождений слова {word} в предложение - {occurrences_amount}.')
```