def sum_digit(num):
	sum_digit = 0
	while num > 0:
		sum_digit+= num%10
		num//=10
	return sum_digit

num = 1234
print(sum_digit(num))
