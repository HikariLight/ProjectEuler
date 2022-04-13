#Created by Light.
#Last edit: 7/8/2016
#Purpose: What is the largest prime factor of the number 600851475143?

from math import sqrt

def main():
    while True:
        a, b, c = 600851475143, 2, int
        if a % b == 0:
            a /= b
            c = b
            b = 2
        elif a % b != 0:
            b +=1
    return c
print(main())
