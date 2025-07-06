def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

print("Reversed number is:", reverse_number(3762))

def reverse_string_v1(s):
	return s[::-1]

# print(reverse_string_v1('irshad'))

def reverse_string_v2(s):
	rev_s = ''
	for char in s:
		rev_s = char+rev_s
	return rev_s

print(reverse_string_v2('irshad'))