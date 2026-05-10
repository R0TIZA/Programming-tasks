input_string = input('Введите строку: ').replace(' ', '').lower()
is_palindrome = True

for char_index in range((len(input_string)-1)//2):
    left_char = input_string[char_index]
    right_char = input_string[len(input_string) - 1 - char_index]
    if left_char != right_char:
        is_palindrome = False
        break

print(f'Строка {"" if is_palindrome else "не "}является палиндромом.')