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


'''
Write a Python function called rotate_matrix_clockwise that takes a 
square matrix (list of lists) as input and rotates the matrix 90 degrees clockwise. 
The function should modify the input matrix in-place and return the rotated matrix.
'''
# not completed
def rotate_matrix_clockwise(lst: list[list]) -> list[list]:
	matrix = []
	for i in range(len(lst)):
		temp = []
		for j in range(len(lst[0])):
			temp.append(lst[j][i])
		temp.reverse()
		matrix.append(temp)

	return  matrix


'''
Write a Python function called find_subarrays_with_sum that 
takes a list of integers and an integer target_sum as input 
and returns all subarrays (contiguous sublists) of the input 
list that sum up to the target_sum
'''

def subarray(lst:list[int]):
	for i in range(len(lst)):
		for j in range(i+1, len(lst)+1):
			yield lst[i:j]

def find_subarrays_with_sum(lst:list[int], target_sum:int) -> list[list]:
	lst[:] = [x for x in subarray(lst) if sum(x) == target_sum]
	return lst


'''
Write a Python function called largest_subarray_sum that takes a 
list of integers as input and returns the maximum sum of any 
contiguous subarray within the list. 
The function should have a time complexity of O(n) without using any extra space.
'''

def largest_subarray_sum(lst:list[int]) -> list[list]:
	lst[:] = [sum(x) for x in subarray(lst)]
	return max(lst)






