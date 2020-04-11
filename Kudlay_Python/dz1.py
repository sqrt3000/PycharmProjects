#My variant
for i in range(1, 2):
    print(f'\t')
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}\t\t'
              f'{i+1} * {j} = {(i+1) * j}\t\t'
              f'{i+2} * {j} = {(i+2) * j}\t\t'
              f'{i+3} * {j} = {(i+3) * j}\t\t'
              f'{i+4} * {j} = {(i+4)* j}')
    print(f'\t')
    for j in range(1, 11):
        print(f'{i+4} * {j} = {i * j}\t\t'
              f'{i+5} * {j} = {(i+5) * j}\t\t'
              f'{i+6} * {j} = {(i+6) * j}\t\t'
              f'{i+7} * {j} = {(i+7) * j}\t\t'
              f'{i+8} * {j} = {(i+8)* j}')

#Kudlay variant
print('Таблица умножения')
for i in range(1, 10):
    for k in range(2, 10):
        print(f'{i} * {k} = {i * k}\t', end='')
    print('')
else:
    print('Well done')
