#Created by Light.
#Last edit: 7/9/2016
#Purpose: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#First try
def checking_divisible(number):
    divisible = []
    for num in range(1, 21):
        if number % num == 0:
            divisible.append(True)
    if len(divisible) == 20:
        return True
    elif len(divisible) != 20:
        return False

result = 0
i = 21

while not result:
    i += 1
    if checking_divisible(i):
        result += 1
print(result)
#232792560 is the solution. Took some time to actually calculate it.
"""

result = 0
num = 21
check = []

while not result:
    num += 1
    for divisor in range(1, 21):
        if num % divisor == 0 and (divisor == 20):
            result += num

print(result)
"""
