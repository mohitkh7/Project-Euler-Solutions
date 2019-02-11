"""
Sum square difference

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# using property = (1+2+3+...+n)^2 = ((n(n+1))^2)/4
# and property = (1^2 + 2^2 + ....+ n^2) = n*(n+1)*(2n+1)*(1/6)
n = 100

sum_of_square = (n * (n + 1) * ((2 * n) + 1)) // 6
square_of_sum = ((n * (n + 1))**2) // 4

# Difference
print(square_of_sum - sum_of_square)
