# Without list comprehension
# Ex1
print('Without list comprehension')
fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = []
for x in fruits1:
    if 'a' in x:
        newlist1.append(x)
print('Ex1'*5)
print(newlist1)

# Ex2
numlist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
oddlist1 = []
for x in numlist1:
    if x % 2 == 1:
        oddlist1.append(x)
print('Ex2'*5)
print(oddlist1)

# With list comprehension
# syntax: newlist = [expression for item in iterable if condition == True] OR newlist = [expression for item in iterable]
# Ex1
print('With list comprehension')
fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist2 = [x for x in fruits2 if 'a' in x]
newlist3 = [x.upper() for x in fruits2 if 'a' in x]
print('Ex1'*5)
print(newlist2)
print('Ex2'*5)
print(newlist3)

# Ex2
numlist2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
oddlist1 = [x for x in numlist2 if x % 2 == 1]
oddlist2 = [x for x in range(10) if x % 2 == 1]
print('Ex3'*5)
print(oddlist1)
print('Ex4'*5)
print(oddlist2)

# Ex3
newlist4 = [x for x in range(10)]
print('Ex4'*5)
print(newlist4)
newlist5 = [x for x in range(10) if x < 5]
print('Ex5'*5)
print(newlist5)
print('Matrix using List comprehension')
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)
