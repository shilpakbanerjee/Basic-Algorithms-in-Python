# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
	if to <= 1:
 	       return to

	previous = 0
	current  = 1
	for _ in range(from_ - 1):
	        previous, current = current, previous + current
	sum = current
	for _ in range(to - from_):
	        previous, current = current, previous + current
	sum += current

	return sum % 10

def fibonacci_partial_sum(m,n):
	if n <= 1:
		return n
	Fib_list = [0,1]
	i = 2
	while i < 60:
		Fib_list.append((Fib_list[i-1] + Fib_list[i-2]) % 10)
		i = i + 1
	#print(Fib_list)
	#print(len(Fib_list))
	if n < 60:
		#print(Fib_list[m:n+1])
		return sum(Fib_list[m:n+1]) % 10
	return ((sum(Fib_list[m % 60 :]) % 10) + ((((n // 60) - (m // 60) - 1) * sum(Fib_list)) % 10) + (sum(Fib_list[:n % 60 + 1]) % 10)) % 10

if __name__ == '__main__':
	input = sys.stdin.read();
	from_, to = map(int, input.split())
	print(fibonacci_partial_sum(from_, to))
	#print(fibonacci_partial_sum_naive(from_, to))
