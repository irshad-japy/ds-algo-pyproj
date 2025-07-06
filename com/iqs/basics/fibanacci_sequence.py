# Print Fibonacci sequence
def fibonacci_sequence(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Test input
n = 10
result = fibonacci_sequence(n)
print(f"Fibonacci sequence for n = {n} is:\n{result}")
