def sum(*n):
    total = 0
    for x in n:
        total = total + x;
    print('The sum is: ', total)


sum(10, 20)
sum(10, 20, 30)
