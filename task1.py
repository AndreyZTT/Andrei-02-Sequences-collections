"""Task 1: Second Largest Number.

This program returns the second largest number in the list handling duplicates.
"""

numbers = [4, 6, 2, 11, 1, 11, 5]

ind = 0
next_ind = 1

numbers.sort(reverse=True)

while next_ind < len(numbers):
    if numbers[ind] == numbers[next_ind]:
        numbers.pop(next_ind)
    else:
        ind += 1
        next_ind += 1

print(numbers[1])
