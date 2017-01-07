# Uses python3
import sys
import time 


def get_fibonacci_last_digit_naive(n):
	if n <= 1:
		return n
	previous = 0
	current  = 1
	for _ in range(n - 1):
			previous, current = current, previous + current
	return current % 10

def get_fibonacci_last_digit(n):
	if n <= 1:
		return n
	previous = 0
	current  = 1
	for _ in range(n - 1):
			previous, current = current, (previous + current) % 10
	return current % 10

def stress_test(t_min):
	t_begin = time.time()
	t_end = t_begin + 60 * t_min
	n = 0
	while time.time() < t_end:
		if get_fibonacci_last_digit(n) == get_fibonacci_last_digit_naive(n) and get_fibonacci_last_digit(-n) == get_fibonacci_last_digit_naive(-n):
			n = n + 1
			print("OK for n = ", n)
		else:
			print("Test failed for n = ", n)
			return "Failed"
	return "Passed"



if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	#print(get_fibonacci_last_digit_naive(n))
	print(get_fibonacci_last_digit(n))
	#print("Result of stress test:", stress_test(1))
