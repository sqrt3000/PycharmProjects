#Напишите код для функции sum
def sum(list):
    if list == ([]):
        return 0
    return list[0] + sum(list[1:])

print (sum(list = [1, 3, 5, 8]))

#Напишите рекурсивную функцию для подсчета элементов в списке
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print(count(list = [1, 4, 6, 7]))

#Найдите наибольшее число в списке - не решено!

#Быстрая сортировка
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]#выбираем опорный элемент (в данном примере это 10
        less = [i for i in array[1:] if i <= pivot]#значения меньшие опорного
        greater = [i for i in array[1:] if i > pivot]#значения большие опорного
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))
