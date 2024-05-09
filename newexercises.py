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


