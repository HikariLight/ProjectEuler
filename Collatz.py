"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def length(n):
    num = n
    i = 1

    while n >= 1:
        if (n % 2 == 0) and (n != 1):
            n /= 2
            i += 1

        elif (n % 2 != 0) and (n != 1):
            n = (3*n) + 1
            i += 1

        elif n == 1:
            break

    return i


length1 = 1
number = 0

for num in range(1, 1000000):
    length2 = length(num)

    if length2 > length1:
        number = num
        length1 = length2

print(number)
#837799
