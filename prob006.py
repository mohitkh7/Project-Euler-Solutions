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

sum_of_square = 0
sum_of_number = 0

for n in range(1, 101):
    sum_of_square += n**2
    sum_of_number += n

square_of_sum = sum_of_number**2

# Difference
print(square_of_sum - sum_of_square)
