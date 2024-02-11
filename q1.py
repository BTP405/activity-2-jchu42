import sys

#primes = [2]

# def isPrime(n):
# 	i = 0
# 	sqrt = n**0.5
# 	while (primes[i] <= sqrt and i < len(primes)):
# 		if (n % primes[i] == 0):
# 			return False
# 		i += 1
# 	return True

def isPrime(n):
	#i = 0
	#sqrt = n**0.5
	for i in range(2, int(n**0.5) + 1):
		if (n % i == 0):
			return False
		i += 1
	return True

def getPrimeNumbers(n):
	"""Compute prime numbers. 
	
	Keyword arguments: 
	n -- Primes from 2 to n are computed. 
	"""
	# for x in range(3, n, 1):
	# 	if (isPrime(x)):
	# 		primes.append(x)

	# primes = [2]
	# for x in range(3, n, 1):
	# 	i, sqrt = 0, x**0.5
	# 	while (primes[i] <= sqrt and i < len(primes)):
	# 		if (x % primes[i] == 0):
	# 			break
	# 		i += 1
	# 	else:
	# 		primes.append(x)
	# return primes
	return [i for i in range(2, n) if isPrime(i)]


def main() -> int:
    print (getPrimeNumbers(100))
    return 0

if __name__ == '__main__':
    sys.exit(main())
