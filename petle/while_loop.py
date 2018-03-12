# While

from random import randint


accumulator = 0

while accumulator < 10:
    print(accumulator)
    accumulator += 1


print('\n')
while accumulator != 5:
    accumulator = randint(0, 10)
    print(accumulator)
