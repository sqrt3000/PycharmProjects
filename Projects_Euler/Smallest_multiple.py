#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#Какое самое маленькое число делится нацело на все числа от 1 до 20?
# Ответ: 232792560

number_max = i = 21
namber_min = 1
z = 0

import time
start_time = time.time()

while i > 0:
    for j in range(namber_min, number_max):
        if z < number_max:
            if i % j == 0:
                z += 1
                smallest_multiple = (i-1)
                continue
            else:
                z = 0
                break
        else:
            i = -1
            break
    i += 1

print(smallest_multiple)
print("--- %s seconds ---" % (time.time() - start_time))
