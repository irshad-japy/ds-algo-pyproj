# WAP to generate prime numbers which are less than or equal to the given number.
number = int(input('Enter the number:'))
n1 = 2
while n1 <= number:
    is_prime = True
    for i in range(2, n1 // 2 + 1):
        if n1 % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(n1)
    n1 = n1 + 1
