#Created by Light.
#Last edit: 7/16/2016
#Purpose: Find the sum of all the multiples of 3 or 5 below 1000.

result = 0

for num in range(1000):
    if num % 3 == 0 or num % 5 ==0:
        result += num

print(result)
