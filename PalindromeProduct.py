#Created by Light.
#Last edit: 7/9/2016
#Purpose: Find the largest palindrome made from the product of two 3-digit numbers.

numbers = []

for num in range(100, 1000):
    for num2 in range(100, 1000):
        product = num * num2
        if str(product) == str(product)[::-1]:
            numbers.append(product)

print(max(numbers))
