# coding=utf-8

from utils.helpers import print_data_types

"""
Kolekcje

Podstawowe kolekcje (typy złożone) w języku Python.
"""


# Krotka / Tupla
tuple_sample = (1, 2, 3)
another_tuple = (1,)
yet_another_tuple = (1, 'Patryk', (1, 2))

# Lista
list_sample = [1, 2, 3]
another_list = [1, 2, 'Patryk', (3, 4), [5, 6]]

# Słownik / Dictionary
dict_sample = {
    'some_key': 'some value',
    'another_key': 1
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


print_data_types(tuple_sample, another_tuple, yet_another_tuple, list_sample, another_list, dict_sample, lectures_dict)
