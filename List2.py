# list question

'''
Write a Python function called remove_duplicates_sorted that
takes a sorted list of integers as input and removes duplicates in-place, 
without using any additional space. The function should return the modified 
list with unique elements only.
'''

import time

def remove_duplicates_sorted(lst: list[int]) -> list[int]:
	lst[:] = [lst[i] for i in range(len(lst)) if lst[i] not in lst[i+1:]]
	return lst



