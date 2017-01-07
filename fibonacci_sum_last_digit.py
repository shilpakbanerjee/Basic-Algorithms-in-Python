# Uses python3
import sys

def fibonacci_sum_naive(n):
	if n <= 1:
		return n
	previous = 0
	current  = 1
	sum      = 1

	for _ in range(n - 1):
		previous, current = current, previous + current
		sum += current
	#print(previous, current)
	return sum % 10

def fibonacci_sum(n):
	if n <= 1:
		return n
	Fib_list = [0,1]
	i = 2
	while i < 60:
		Fib_list.append((Fib_list[i-1] + Fib_list[i-2]) % 10)
		i = i + 1
	#print(Fib_list)
	#print(len(Fib_list))
	return (((n // 60) * sum(Fib_list)) % 10) + (sum(Fib_list[:n % 60 + 1]) % 10) 

if __name__ == '__main__':
	input = sys.stdin.read()
	n = int(input)
	
	print(fibonacci_sum(n))
	#print(fibonacci_sum_naive(n))
