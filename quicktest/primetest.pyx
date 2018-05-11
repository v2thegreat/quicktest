#from libcpp cimport bool

cpdef isPrime(long long unsigned int n):
	cdef long long unsigned int x
	for x in range(2, n//2):
		if n%x == 0:
			return False
	return True

cpdef isPrime2(long long unsigned int n):
	cdef long long unsigned int x
	for x in range(2, int(n**0.5)):
		if n%x == 0:
			return False
	return True