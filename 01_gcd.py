# Uses python3
import sys, time, numpy

def gcd_naive(a, b):
	current_gcd = 1
	for d in range(2, min(a, b) + 1):
		if a % d == 0 and b % d == 0:
			if d > current_gcd:
				current_gcd = d
	return current_gcd

def gcd_euclid(a, b):
	remainder = min([a,b])
	dividend = max([a,b])
	while not (remainder == 0):
		temp = remainder
		remainder = dividend % remainder
		dividend = temp	 
	return dividend

def stress_test(t_min):
	t_end = time.time() + 60 * t_min
	while time.time() < t_end:
		n = numpy.random.randint(1, high=1000, size = 2)
		if gcd_euclid(n[0],n[1]) == gcd_naive(n[0],n[1]):			
			print("OK for a = ", n[0], " b = ", n[1])
		else:
			print("test failed for a = ", n[0], " b = ", n[1])
			return "Failed"
	return "Passed"



if __name__ == "__main__":
	input = sys.stdin.read()
	a, b = map(int, input.split())
	#print(gcd_naive(a, b))
	print(gcd_euclid(a, b))
	#print("Result of stress test:", stress_test(1))
