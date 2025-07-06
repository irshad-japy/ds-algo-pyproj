n = 8
def check_prime(n):
    if n < 2:
        return "Not Prime"
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

print(check_prime(n))  # Output: Prime if n is a prime number, otherwise Not Prime