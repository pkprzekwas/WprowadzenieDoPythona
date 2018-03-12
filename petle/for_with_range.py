"""Range"""

print('\n')
range_example = range(0, 10)
print(range_example)


print('\n')
for num in range_example:
    print(num)


print('\n')
for num in range(0, 10):
    print(' --> ', num)


print('\n')
for num in range(0, 10):
    print(' --> {}'.format(num))


print('\n')
for num in range(0, 10, 2):
    print(' --> {}'.format(num))


print('\n')
for num in range(10, 0, -1):
    print(' --> {}'.format(num))

