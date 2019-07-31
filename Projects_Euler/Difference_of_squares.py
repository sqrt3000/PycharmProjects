#Сумма квадратов первых десяти натуральных чисел равна
#12 + 22 + ... + 102 = 385
#Квадрат суммы первых десяти натуральных чисел равен
#(1 + 2 + ... + 10)2 = 552 = 3025
#Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.
#Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.

natural_number_min = 1
natural_number_max = 101
squares = []
sums = []

for i in range(natural_number_min, natural_number_max):
    square = i*i
    squares.append(square)
    sums.append(i)

sum_squares = sum(squares)
s = sum(sums)
square_sum = s*s
difference = square_sum - sum_squares
print('Сумма квадратов:', sum_squares)
print('Квадрат суммы:', square_sum)
print('Разность между суммой квадратов и квадратом суммы:', difference)

