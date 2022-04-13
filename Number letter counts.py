"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
 how many letters would be used?
"""

from num2words import num2words
result = 0

for i in range(1, 1001):
    num_word = num2words(i)
    length = len(num_word)

    if " " in num_word:
        length -= num_word.count(" ")

    elif "-" in num_word:
        length -=1

    result += length

print(result)
#21124
