#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

first, second, result, index = 1, 1, 0, 1

while not result:
    first, second = second, first + second
    index +=1
    if len(str(first)) == 1000:
        result += index
print(result)
