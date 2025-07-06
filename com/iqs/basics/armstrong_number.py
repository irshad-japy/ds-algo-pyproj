# def is_armstrong(n):
# 	num_str = str(n)
# 	power = len(num_str)
# 	total = 0
# 	for num in num_str:
# 		raised = int(num)**power
# 		total+=raised
# 	return total==n

# n=121
# if is_armstrong(n):
# 	print("Armstrong number")
# else:
# 	print("Not Armstrong numner")

def check_armstrong_number(n):
	num_str = str(n)
	power = len(num_str)
	total = 0
	for digit in num_str:
		raised = int(digit)**power
		total += raised
	return total == n

n=153
if check_armstrong_number(n):
	print(f"this is armstrong number of {n}")
else:
	print(f"this is not arstrong number of {n}")