import random

number = (random.randint(1, 1000))
count = 0
running = True
while running:
    count += 1
    guess = int(input('Введите целое загаданное число (от 1 до 100) : '))
    if guess == number:
        print('Поздравляю, вы угадали!')
        print("""
        #                 ------------
        #                 |           |
        #                 |  0     0  |
        #                 |     <     |
        #                 |  .     .  |
        #                 |   `...`   |
        #                 ------------
        #                 """)
        print(f'Задуманное число угадано с: {count} попытки.')
        # Здесь можете выполнить всё что вам ещё нужно
        guess = input('Хотите еще сыграть? - N/Y : ')
        if guess == 'N':
            running = False  # это останавливает цикл while
        else:
            count = 0
            number = (random.randint(1, 100))
            running = True  # продолжаем цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Завершение...')
