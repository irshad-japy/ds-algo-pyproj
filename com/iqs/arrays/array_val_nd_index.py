import random

stat_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
rand_arr = random.sample(range(1, 101, 1), 10)
# rand_arr = [1, 7, 6, 32, 5, 77, 13, 97, 55, 86]
# print(sample_list)
while True:
    num1 = input('Enter num1:')
    if len(num1) != 2:
        print('Please Enter two-digit number')
        num1 = eval(input('Enter num1:'))
    num2 = input('Enter num2:')
    if len(num2) != 2:
        print('Please Enter two-digit number')
        num2 = eval(input('Enter num2:'))
    # avg = int(int(num1) + int(num2) / 2)
    avg = (int(num1) + int(num2)) / 2
    print('average-', avg)
    val = 0
    index = 0
    result = 0
    if avg < 15:
        val = 10
        index = 0
        result = rand_arr[index]
    if avg > 15 and avg <= 20:
        val = 20
        index = 1
        result = rand_arr[index]
    if avg > 20 and avg <= 25:
        val = 20
        index = 1
        result = rand_arr[index]
    if avg > 25 and avg <= 30:
        val = 30
        index = 2
        result = rand_arr[index]
    if avg > 30 and avg <= 35:
        val = 30
        index = 2
        result = rand_arr[index]

    if avg > 35 and avg <= 40:
        val = 40
        index = 3
        result = rand_arr[index]
    if avg > 40 and avg <= 45:
        val = 40
        index = 3
        result = rand_arr[index]

    if avg > 45 and avg <= 50:
        val = 50
        index = 4
        result = rand_arr[index]
    if avg > 50 and avg <= 55:
        val = 50
        index = 4
        result = rand_arr[index]

    if avg > 55 and avg <= 60:
        val = 60
        index = 5
        result = rand_arr[index]
    if avg > 60 and avg <= 65:
        val = 60
        index = 5
        result = rand_arr[index]

    if avg > 65 and avg <= 70:
        val = 70
        index = 6
        result = rand_arr[index]
    if avg > 70 and avg <= 75:
        val = 70
        index = 6
        result = rand_arr[index]

    if avg > 75 and avg <= 80:
        val = 80
        index = 7
        result = rand_arr[index]
    if avg > 80 and avg <= 85:
        val = 80
        index = 7
        result = rand_arr[index]

    if avg > 85 and avg <= 90:
        val = 90
        index = 8
        result = rand_arr[index]
    if avg > 90 and avg <= 95:
        val = 90
        index = 8
        result = rand_arr[index]

    if avg > 95 and avg <= 100:
        val = 100
        index = 9
        result = rand_arr[index]

    print('Nearest value is {}, index is {} and result is {}'.format(val, index, result))
    break
