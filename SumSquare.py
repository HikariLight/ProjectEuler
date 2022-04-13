#Created by Light.
#Last edit: 7/9/2016
#Purpose: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

summed_squares_list = []
squared_sums_list = []

for num in range(1, 101):
    summed_squares_list.append(num**2)
    summed_square = sum(summed_squares_list)

    squared_sums_list.append(num)
    squared_sum = sum(squared_sums_list)
    squared_sums = squared_sum **2

print(squared_sums - summed_square)
#25164150 is the solution.
