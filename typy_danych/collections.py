# coding=utf-8

"""Kolekcje - podstawowe kolekcje (typy złożone) w języku Python."""

from utils.helpers import print_data_types


# Krotka / Tupla
tuple_sample = (1, 2, 3)
print(tuple_sample)
another_tuple = (1,)
yet_another_tuple = (1, 'Patryk', (1, 2))


# Lista
list_sample = [1, 2, 3]
list_sample[0] = 99
print(list_sample)
list_sample.append(4)
another_list = [1, 2, 'Patryk', (3, 4), [5, 6]]


# Słownik / Dictionary
dict_sample = {
    (2,): 'some value',
    '2': 1
}
lectures_dict = {
    'matematyka dyskretna': {
        'prowadzacy': 'Jan Kowalski',
        'ocena': 3.5
    },
    'obwody': {
        'prowadzacy': 'Adam Nowak',
        'ocena': 3.
    },
    'bazy danych': {
        'prowadzacy': 'Lech Kowalski',
        'ocena': 4.
    }
}

# print_data_types(tuple_sample, another_tuple, yet_another_tuple, list_sample, another_list, dict_sample, lectures_dict)
