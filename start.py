import math

age = 20
gender = 'female'
if age >= 21 and (gender == 'female' or gender == 'male'):
    print('go have a drink')
else:
    print('go have your parents buy you a drink')

for x in range(20, -50, -5):
    print("{0} to the {1} power is {2}".format(x, 2, x ** 2))

# make list of tuples where first number is even & second number is the square
evens = [(x, x ** 2, y, y ** 3, x * y) for x in range(20) for y in range(3, 12, 3) if x % 2 == 0]

print(evens)


def add(a, b):
    return a + b


awesome = add(5, 7)

print(awesome)


def volume(h, r):
    return math.pi * r ** 2 * h

# import variable directly
from math import pi


def volume2(h, r):
    return pi * r ** 2 * h

# can do from math import *, but peeps be saying don't do that shit

print(volume(5, 5))
print(volume2(5, 5))

def bin_to_dec(str):
    num = 0
    for i, dig in enumerate(reversed([int(x) for x in list(str)])):
        num = num + ((2 ** i) * dig)
    return num

print(bin_to_dec('1001'))
print(bin_to_dec('10'))

def test_p_int(str):
    return int(str, 2)

print(test_p_int('1001'))

def bin_to_hex(str):
    pass