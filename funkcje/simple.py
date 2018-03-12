# coding=utf-8

"""Funkcje"""

# Definicje funkcji


def say_hello():
    print('Hello World!')


def say_hello_to(name):
    print('Hello {}!'.format(name))


def sum_of_list(input_list):
    acc = 0
    for element in input_list:
        acc += element
    return acc


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


# Wywołania funkcji


say_hello()
say_hello_to('Patryk')

test_list = [1, 2, 3]
sum_of_test_list = sum_of_list(test_list)
print(sum_of_test_list)

factorial_of_five = factorial(5)
print(factorial_of_five)
