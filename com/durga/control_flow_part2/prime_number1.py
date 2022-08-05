number = int(input('Enter the number:'))
if number <= 1:
    print('Its not prime number')
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print('Its prime number')
    else:
        print('Its not prime number')
