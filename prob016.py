"""
Power digit sum
Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
str_n = str(2**1000)
ans = 0
for ch in str_n:
    ans += int(ch)

print(ans)
