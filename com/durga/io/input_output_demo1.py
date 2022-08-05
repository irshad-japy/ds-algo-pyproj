from sys import argv

# a, b, c = [10, 20, 30]
# print(a, b, c)
# list comprehension demo
# a, b = [int(x) for x in input('Enter 2 numbers: ').split()]
# print('The Sum: ', a + b)

# a, b, c = [int(x) for x in input('Enter 3 numbers with comma separated: ').split(',')]
# print('The Sum: ', a + b + c)

# a, b, c = [eval(x) for x in input('Enter 3 numbers with comma separated: ').split(',')]
# print('The Sum: ', a + b + c)
l = argv[1:]
print(l[1])
