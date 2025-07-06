def count_digit(num):
	temp = num
	count = 0
	while temp > 0:
		temp = temp// 10
		count+=1
	return count

print(count_digit(23432))