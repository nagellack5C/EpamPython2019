from functools import reduce
from timeit import timeit

# hw1

# problem 6:
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.

x = abs(sum([i*i for i in range(1, 101)]) - sum(range(1, 101)) ** 2)
print(x)

# problem 9:
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

simple = [a * b * (1000 - a - b) for a in range(1, 1001) for b in range(1, 1001) if a*a + b*b == (1000 - a - b)**2][0]
euclid = [a * b * c for a, b, c in [(m * m - n * n, 2 * m * n, m * m + n * n) for m in range(1, 32) for n in range(1, 32)] if a * a + b * b == c * c and a + b + c == 1000][0]
print(simple, euclid)

# euclid is 500-800 times faster
x = timeit("[a * b * (1000 - a - b) for a in range(1, 1001) for b in range(1, 1001) if a*a + b*b == (1000 - a - b)**2][0]", number=5)
y = timeit("[a * b * c for a, b, c in [(m * m - n * n, 2 * m * n, m * m + n * n) for m in range(1, 32) for n in range(1, 32)] if a * a + b * b == c * c and a + b + c == 1000][0]", number=5)
print(x / y)