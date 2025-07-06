def factorial(n):
	if n==0 or n==1:
		return 1
	return (n*(factorial(n-1)))

def is_strong_nuber(n):
	num_str = str(n)
	total = 0
	for digit in num_str:
		fact = factorial(int(digit))
		total += fact
	return total == n
	
n=145
if is_strong_nuber(n):
	print(f'{n} is strong number')
else:
	print(f'{n} is not strong number')