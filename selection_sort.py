import random
import sys

numbers = [1, 5, 8, 2, 3, 4, 7, 6]

def selection_sort(values):
	sorted_list = []
	print("%-25s %-25s" % (values, sorted_list)) # Can be removedti
	for i in range(0, len(values)):
		index_to_move = index_of_min(values)
		sorted_list.append(values.pop(index_to_move))
		print("%-25s %-25s" % (values, sorted_list)) # Can be removed
	return sorted_list

def index_of_min(values):
	min_index = 0
	for i in range(1, len(values)):
		if values[i] < values[min_index]:
			min_index = i
	return min_index

print(selection_sort(numbers))