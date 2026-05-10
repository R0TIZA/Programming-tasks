import random

FILE_NAME = './Task 7/File_A.txt'
nums = []

while len(nums) < 10:
    num = random.randint(1, 10**5)
    if(num%3 == 0 or num%7 == 0):
        nums.append(num)


with open(file=FILE_NAME, mode='w') as file:
    file.write(', '.join(map(str, nums)))