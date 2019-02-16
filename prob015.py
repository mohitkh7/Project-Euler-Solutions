"""
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

"""
Approach: Number of shortest path i.e. only right down are combination of sum of rows & cols to either row or columns
ans = r+c C r
"""
ROWS = 20
COLUMNS = 20


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def cal_combination(n, r):
    """
    Calculate combination i.e nCr
    """
    return factorial(n) // (factorial(n - r) * factorial(r))

print(cal_combination(ROWS + COLUMNS, ROWS))
