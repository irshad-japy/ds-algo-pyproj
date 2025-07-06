a, b, c = 10, 5 , 15
# largest = max(a, b, c)
# print("Largest number is:", largest)
# largest = a if a > b and a > c else b if b > c else c
if a > b and b > c:
    largest = a  # All numbers are equal
else:
    if b > c:
        largest = b
    else:
        largest = c
    
print("The largest number is:", largest)  # Output: The largest number is: 15