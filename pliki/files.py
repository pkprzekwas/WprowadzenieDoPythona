# coding=utf-8

"""Operacje na plikach"""


# Zapisywanie

test_file_name = 'test_file.txt'

test_file = open(test_file_name, 'w+')

print('Writing "1, 2, 3" to test file.')

test_file.write('1, 2, 3')

test_file.close()


# Odczytywanie

test_file_for_reading = open(test_file_name, 'r')

print('Reading file content.')

file_content = test_file_for_reading.read()

print(file_content)

test_file_for_reading.close()


# Operacje na pliku z użyciem kontekst managera

with open(test_file_name, 'r') as f:
    print('Reading file in context manager:')
    print(f.read())
