from functools import reduce
from timeit import timeit

# hw1

# problem 6:
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.
# solution:
x = abs(sum([i*i for i in range(1, 101)]) - sum(range(1, 101)) ** 2)
print(x)

# problem 9:
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# solution:
# simple = [a * b * (1000 - a - b) for a in range(1, 1001) for b in range(1, 1001) if a * a + b * b == (1000 - a - b) ** 2][0]
euclid = [a * b * c for a, b, c in [(m * m - n * n, 2 * m * n, m * m + n * n) for m in range(1, 32) for n in range(1, 32)] if a * a + b * b == c * c and a + b + c == 1000][0]
print(euclid)
# print(simple)
# euclid is 500-800 times faster
# x = timeit("[a * b * (1000 - a - b) for a in range(1, 1001) for b in range(1, 1001) if a * a + b * b == (1000 - a - b) ** 2][0]", number=5)
# y = timeit("[a * b * c for a, b, c in [(m * m - n * n, 2 * m * n, m * m + n * n) for m in range(1, 32) for n in range(1, 32)] if a * a + b * b == c * c and a + b + c == 1000][0]", number=5)
# print(x / y)

# problem 40:
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value
# of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
# solution:
# val = reduce(lambda x, y: int(x) * int(y), [i[1] for i in enumerate(list("".join([str(i) for i in range(1, 1000001)])), 1) if i[0] in [10**j for j in range(6)]])
# print(val)

# problem 48:
# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
# solution:
last_ten = reduce(lambda x, y: x + y ** y, range(1, 1001)) % (10 ** 10)
print(last_ten)


# ------------------------------------------------------

# hw2
def is_armstrong(number):
    return number == sum(list(map(lambda x: int(x)**len(str(number)), list(str(number)))))

assert is_armstrong(153) == True, 'Число Армстронга'
assert is_armstrong(10) == False, 'Не число Армстронга'

# hw3

def collatz_steps(n):
    if isinstance(n, int) and n > 0:
        return n-1 if n == 1 else 1 + collatz_steps(n // 2) if n % 2 == 0 else 1 + collatz_steps(n * 3 + 1)

print(collatz_steps(12))

# assert collatz_steps(16) == 4
# assert collatz_steps(12) == 9
# assert collatz_steps(1000000) == 152