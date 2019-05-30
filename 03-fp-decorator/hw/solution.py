from functools import reduce

# hw1

# problem 6:
# Find the difference between the sum of the squares of the
# first one hundred natural numbers and the square of the sum.

x = abs(sum([i*i for i in range(1, 101)]) - sum(range(1, 101)) ** 2)
print(x)

# problem 9:
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

mbyn = [[(m*m - n*n, 2*m*n, m*m + n*n) for m in range(1, 32) if (m*m - n*n)**2 + (2*m*n)**2 == (m*m + n*n)**2 and 2*m*m + 2*m*n == 1000] for n in range(1, 32)]
print(mbyn)