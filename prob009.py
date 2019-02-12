"""
Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
found = False
for a in range(1, 333):
    b = a + 1
    c = 1000 - b - a
    while b < c:
        c = 1000 - b - a
        if a**2 + b**2 == c**2:
            # condition satidfied triplet found
            found = True
            break
        b += 1
    if found:
        break
print(a * b * c)
