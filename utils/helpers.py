# coding=utf-8


def print_data_types(*args):
    for each in args:
        print('Nazwa typu danych: {} \t Wartość: {}'.format(type(each), each))
