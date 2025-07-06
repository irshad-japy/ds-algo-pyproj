def check_palindrome(num):
    original = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //=10
		
    if original == rev:
        print("this is palnidrome number")
    else:
        print("this is not palindrome")
        
check_palindrome(121)

def check_string_palindrome_v1(s):
	rev_string = s[::-1]
	return rev_string

s = 'iri'
result = check_string_palindrome_v1(s)
if result == s:
	print("Palindrome string")
else:
	print("Not a palindrome string")

def check_string_palindrome_v2(s):
	rev_s = ''
	for char in s:
		rev_s = char + rev_s
	return rev_s
	
s = 'irii'
result = check_string_palindrome_v2(s)
if result == s:
	print("Palindrome string")
else:
	print("Not a palindrome string")