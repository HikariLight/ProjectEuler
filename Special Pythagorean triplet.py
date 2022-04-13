#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

c = 1
result = 0

while not result:
    c+=1
    for a in range(1, c):
        for b in range(1, c):
            if (a + b + c == 1000) and (a**2 + b**2 == c**2):
                result = a * b * c
print(result)
