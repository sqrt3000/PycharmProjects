# def get_square(num):
#     return num ** 2
#
#
# print(get_square(5))

# get_square = lambda num: num ** 2
# print(get_square(10))

# print((lambda num: num ** 2)(7))

l = [1, 2, 3] # [2, 4, 6]


# def get_double(l):
#     return [i * 2 for i in l]


def get_double(l):
    return list(map(lambda num: num * 2, l))


print(get_double(l))
