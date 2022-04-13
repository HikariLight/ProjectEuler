#Created by Light.
#Last edit: 7/9/2016
#Purpose: Find the sum of all the primes below two million.

def generator(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

primes = []

for prime in generator(2000000):
    primes.append(prime)

print(sum(primes))
