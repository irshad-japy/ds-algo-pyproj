n = int(input('Enter number of students to be inserted:'))
d = {}
for i in range(n):
    name = input('Enter student name:')
    marks = int(input('Enter marks:'))
    d[name] = marks
print('Student data insertion completed')
print('*' * 30)
print('NAME', '\t\t', 'MARKS')
print('*' * 30)
for k, v in sorted(d.items()):
    print(k, '\t\t', v)
print('Search operation started...')
while True:
    sname = input('Enter student name to get martks:')
    smarks = d.get(sname, -1)
    if smarks == -1:
        print('Student not found')
    else:
        print('Marks of ', sname, 'are', smarks)
    option = input('Do you want to find another student marks [Yes/No]?:')
    if option.lower() == 'no':
        print('Thanks for using our application.')
        break
