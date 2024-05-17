# def primes_upto_n(n):
# 	primes = []

# 	for i in range(2, n+1):
# 		if i == 2:
# 			primes.append(i)
# 			continue

# 		token = True
# 		for j in range(2, i):
# 			if i % j == 0:
# 				token = False
# 				break
# 		if token:
# 			primes.append(i)
# 	return primes


# def good_pairs(nums:list[int]) -> int:
# 	""" good pairs nums[i]==nums[j] when i < j"""

# 	count_of_good_pairs = 0
# 	length_of_list = len(nums)

# 	for i in range(length_of_list):
# 		for j in range(i+1, length_of_list):
# 			if nums[i] == nums[j]:
# 				count_of_good_pairs += 1
	
# 	return count_of_good_pairs

# def make_move(string):
# 	character_dictionary = {}

# 	new_string = []
# 	for character in string:
# 		if character in character_dictionary:
# 			new_string.append(character)
# 		else:
# 			character_dictionary[character] = character
# 	return ''.join(new_string)

# def remove_first_occurance(string:str)->str:
# 	list_of_characters = list(string)
# 	print(list_of_characters)

# 	last_val = ''

# 	while string:
# 		last_val = string
# 		string = make_move(string)

# 	return last_val


# # prefix sum

# def prefix_sum(nums:list[int]) -> list[int]:
# 	new_nums = []

# 	for index in range(len(nums)):
# 		if index == 0:
# 			new_nums.append(nums[index])
# 		else:
# 			new_nums.append(nums[index] + new_nums[index-1])

# 	return new_nums


# # Highest Altitude
# def highest_altitude(gain:list[int]) -> int:
# 	altitude_max = 0
# 	altitude_gain = 0

# 	for index in range(len(gain)):
# 		if index == 0:
# 			altitude_gain = gain[index]
# 		else:
# 			altitude_gain += gain[index]
# 		if altitude_gain > 0 and altitude_gain > altitude_max:
# 			altitude_max = altitude_gain
# 	return altitude_max

# # frequency of values
# def frequency_of_values(nums:list[int])-> dict:
# 	frequency_dictionary = {}

# 	for number in nums:
# 		if number in frequency_dictionary:
# 			frequency_dictionary[number] += 1
# 		else:
# 			frequency_dictionary[number] = 1

# 	return frequency_dictionary


# # frequency array character
def frequency_character_mapped_to_index(string:str):
	frequency_list = [0 for _ in range(26)]

	for char in string.lower():
		index = ord(char) - ord('a')
		frequency_list[index] += 1

	for index in range(26):
		if frequency_list[index] > 0:
			character = chr(index + ord('a'))
			print(f'{character} = {frequency_list[index]}', end=',')

