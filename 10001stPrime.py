#Created by Light.
#Last edit: 7/9/2016
#Purpose: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import math

def generator(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

primes = []

#while len(primes) <= 10001:
for num in generator(104750):
    primes.append(num)
print(max(primes))
