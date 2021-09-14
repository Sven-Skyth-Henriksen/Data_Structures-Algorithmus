import random
import sys

numbers = [1, 5, 8, 2, 3, 4, 7, 6]

def is_sorted(values):
	for index in range(len(values) - 1):
		if values[index] > values[index + 1]:
			return False
	return True

def bogo_sort(values):
	attempts = 0
	while not is_sorted(values):
		print(attempts)
		random.shuffle(values)
		attempts += 1
	return values

print(bogo_sort(numbers))
