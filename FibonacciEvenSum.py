#Created by Light.
#Last edit: 7/7/2016
#Purpose: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def evenSum():
    first, second, result = 1, 1, 0
    for i in range(40):
        first, second = second, first + second
        if first > 1 and first % 2 == 0 and first < 4000000:
            result += first

    return result

print(evenSum())
#4613732
