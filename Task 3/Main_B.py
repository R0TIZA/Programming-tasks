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