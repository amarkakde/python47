def primes_upto_n(n):
	primes = []

	for i in range(2, n+1):
		if i == 2:
			primes.append(i)
			continue

		token = True
		for j in range(2, i):
			if i % j == 0:
				token = False
				break
		if token:
			primes.append(i)
	return primes


def good_pairs(nums:list[int]) -> int:
	""" good pairs nums[i]==nums[j] when i < j"""

	count_of_good_pairs = 0
	length_of_list = len(nums)

	for i in range(length_of_list):
		for j in range(i+1, length_of_list):
			if nums[i] == nums[j]:
				count_of_good_pairs += 1
	
	return count_of_good_pairs
