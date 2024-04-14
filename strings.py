"""
 Write a Python program to count the number of characters (character frequency) in a string.
 """

def character_frequency_in_string(string) -> dict:
	char_frequency_dict = {}

	for char in string:
		if char in char_frequency_dict:
			char_frequency_dict[char] += 1
		else:
			char_frequency_dict[char] = 1

	return char_frequency_dict

"""
Write a Python program to capitalize the first letter of each word in a given string.
"""

def capitalize_first_letter_of_each_string(string) -> str:
	words = [word.capitalize() for word in string.split()]

	return ' '.join(words)

"""
Write a Python function to remove all consecutive duplicates from a given string.
"""

def remove_consecutive_duplicate_from_string():
	pass


"""
Write a Python program to check if a string contains only digits.
"""

def check_string_contains_only_digits(string):
	return True if string.isdigit() else False


"""
Write a Python function that takes a string and returns the reverse of that string.
"""

def reverse_of_string(string):
	reverse_string = ''

	for char in reversed(range(len(string))):
		reverse_string = reverse_string + string[char]

	return reverse_string

"""
Write a Python program to count the occurrences of a substring in a string.
"""

def count_of_occurances_of_substring(string, substring):
	pass