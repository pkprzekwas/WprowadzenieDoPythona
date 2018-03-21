# coding=utf-8

"""Funkcje"""

# Definicje funkcji

#
# def say_hello():
#     print('Hello World!')
#
#
# def say_hello_to(name):
#     print('Hello {}!'.format(name))
#
#
# say_hello_to('Patryk')


# def sum_of_list(input_list):
#     acc = 0
#
#     for element in input_list:
#         acc = acc + element
#
#     return acc
#
# our_sum = sum_of_list([1, 2, 3, 4])
#
# print(our_sum)


def factorial(n):
    print('Current value: ', n)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)

#
# # Wywołania funkcji
#
#
# say_hello()
# say_hello_to('Patryk')
#
# test_list = [1, 2, 3]
# sum_of_test_list = sum_of_list(test_list)
# print(sum_of_test_list)
#
# factorial_of_five = factorial(5)
# print(factorial_of_five)
