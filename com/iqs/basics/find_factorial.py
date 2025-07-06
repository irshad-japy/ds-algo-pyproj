# Approach 1 - Using a loop
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("Factorial of 5 is:", factorial(5))

# Approach 2 - Using recursion
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

print("Factorial of 5 using recursion is:", factorial_recursive(5))
