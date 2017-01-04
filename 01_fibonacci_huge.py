# Uses python3
import sys, time, numpy

def get_fibonacci_huge_naive(n, m):
	if n <= 1:
		return n
	previous = 0
	current  = 1
	for _ in range(n - 1):
	        previous, current = current, previous + current
	return current % m

def check_pattern(Fib_list):
	n = int(len(Fib_list) / 2)
	if Fib_list[:n] == Fib_list[n:]:
		return 1
	else:
		return 0

def get_fibonacci_huge(n, m):
	if n <= 1:
		return n
	for i in range(1,20):
		if 10**i == m:
			return(get_fibonacci_huge_naive(n % (6*m),m))
			
	pattern = 0
	Fib_list = [0,1]
	i = 2
	while (pattern == 0) and (i < n+2):
		Fib_list.append((Fib_list[i-1] + Fib_list[i-2]) % m)
		if ((i+1) % 2 == 0):
			pattern = check_pattern(Fib_list)
		i = i + 1
	if i == n+2:
		return Fib_list[n]
	pisano_number = int(i/2)
	return Fib_list[n % pisano_number]


def stress_test(t_min):
	t_end = time.time() + 60 * t_min
	n = 0
	while time.time() < t_end:
		m = numpy.random.randint(1, high=100)
		if get_fibonacci_huge(n,m) == get_fibonacci_huge_naive(n,m):
			n = n + 1
			print("OK for n = ", n, " m = ", m)
		else:
			print("test failed for n = ", n, " m = ", m)
			print("Correct = ", get_fibonacci_huge_naive(n,m), " Obtained = ", get_fibonacci_huge(n,m))
			return "Failed"
	return "Passed"

if __name__ == '__main__':
	input = sys.stdin.read();
	n, m = map(int, input.split())
	#print(get_fibonacci_huge_naive(n, m))
	print(get_fibonacci_huge(n, m))
	#print("Result of stress test:", stress_test(1))







