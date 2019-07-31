#Простые делители числа 13195 - это 5, 7, 13 и 29.
#Каков самый большой делитель числа 600851475143, являющийся простым числом?

i = 2
simple_dividers = []
number = 13195

import time
start_time = time.time()


""" def is_simple_number(x):
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            continue
        divisor += 1
    return x
"""
while i <= number:
    if number % i == 0:
        simple_dividers.append(i)
        for n in range(2, i):
            if i % n == 0:
                simple_dividers.remove(i)
                break
    i += 1

print(simple_dividers[-1])
print("--- %s seconds ---" % (time.time() - start_time))
