#Created by Light.
#Last edit: 7/14/2016
#Purpose: What is the largest prime factor of the number 600851475143?

import math

def generator(limit):
    a = [True] * limit # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i): # Mark factors non-prime
                a[n] = False

primes = generator(round(math.sqrt(600851475143)))
factors = []

for prime in primes:
    if 600851475143 % prime == 0:
        factors.append(prime)

print(max(factors))
