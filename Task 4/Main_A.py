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