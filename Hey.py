"""
The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms,
and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

def generator(limit):
    numbers = [True] * limit
    numbers[0] = numbers[1] = False #0 and 1 aren't primes.

    for (num, isprime) in enumerate(numbers):
        if isprime:
            yield num
            for n in range(num*num, limit, num):
                numbers[n] = False #Marking the multiples as not primes.

primes = []
result = 0

for prime in generator(1000):
    primes.append(prime)

for prime in primes:
    result += prime
    if (result < 1000) and (result in primes):
        print(result)
