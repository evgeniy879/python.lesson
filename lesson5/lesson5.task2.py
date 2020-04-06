counter_string = 1
with open('counter.txt') as file:
    for line in file:
        date = line.split()
        counter_word_per_string = len(date)
        couter_letters = 0
        for i in date:
            couter_letters += len(i)
        print(f'статистика {counter_string} строки')
        print(f'количество слов в строке равняется {counter_word_per_string}')
        print(f'общее количество букв в строке равняется {couter_letters}')
        print()
        counter_string += 1
