#Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
#Какое число является 10001-ым простым числом?
#Ответ: 104743  --- 108.05018019676208 seconds ---

prime_numbers = []
number = 100
n = 2
xor = 0

import time
start_time = time.time()

def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    return True


while(True):
    if isprime(n):
        xor += 1
        if xor == 10001:
            print(n)
            break
    n += 1


print("--- %s seconds ---" % (time.time() - start_time))
