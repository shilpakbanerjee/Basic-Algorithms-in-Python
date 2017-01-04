# Uses python3

import time 


def calc_fib(n):
	if (n <= 1):
		return n
	return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fastfib(n):
	Fib_list = [0,1]
	if n<=1:
		return n
	else:
		for i in range(2, n+1):
			Fib_list.append(Fib_list[i-1]+Fib_list[i-2])
		return Fib_list[n]
    
def stress_test(t_min):
	t_end = time.time() + 60 * t_min
	n = 0
	while time.time() < t_end:
		if calc_fib(n) == calc_fastfib(n) and calc_fib(-n) == calc_fastfib(-n):
			n = n + 1
			print("OK for n = ", n)
		else:
			print("test failed for n = ", n)
			return "Failed"
	return "Passed"


n = int(input())
#print(calc_fib(n))
print(calc_fastfib(n))
#print("Result of stress test:", stress_test(1))
