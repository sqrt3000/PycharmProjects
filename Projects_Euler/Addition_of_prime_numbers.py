#Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#Найдите сумму всех простых чисел меньше двух миллионов.

prime_numbers = []
number = 100
n = 2
const = 2000000

import time
start_time = time.time()

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


while n <= const:
    if isprime(n):
        prime_numbers.append(n)
    n += 1

print(sum(prime_numbers))

print("--- %s seconds ---" % (time.time() - start_time))
