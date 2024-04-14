"""
 Write a Python program to count the number of characters (character frequency) in a string.
 """

def character_frequency_in_string(string):
	char_frequency_dict = {}

	for char in string:
		if char in char_frequency_dict:
			char_frequency_dict[char] += 1
		else:
			char_frequency_dict[char] = 1

	return char_frequency_dict
