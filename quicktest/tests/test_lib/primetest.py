def isPrime(n):
	for x in range(2, n//2):
		if n%x == 0:
			return False
	return True

def isPrime2(n):
	for x in range(2, int(n**0.5)):
		if n%x == 0:
			return False
	return True