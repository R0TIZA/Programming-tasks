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