# Uses python3
import sys

def lcm_naive(a, b):
	for l in range(1, a*b + 1):
		if l % a == 0 and l % b == 0:
			return l
	return a*b

def gcd_euclid(a, b):
	remainder = min([a,b])
	dividend = max([a,b])
	while not (remainder == 0):
		temp = remainder
		remainder = dividend % remainder
		dividend = temp	 
	return dividend

def lcm_euclid(a, b):
	if a==0 or b==0:
		return 0
	return int(a * b // gcd_euclid(a,b))

if __name__ == '__main__':
	input = sys.stdin.read()
	a, b = map(int, input.split())
	#print(lcm_naive(a, b))
	print(lcm_euclid(a, b))

