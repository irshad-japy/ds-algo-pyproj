rows = 5

for i in range(rows):
    for j in range(i):
        print('1', end=' ')
    print('')
print('#' * 30)
for i in range(rows, 0, -1):
    for j in range(i):
        print('1', end=' ')
    print('')
