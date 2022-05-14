class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks


n = int(input('Enter number of student:'))
students = []
for i in range(n):
    s = Student()
    name = input('Enter student name:')
    marks = int(input('Enter marks:'))
    s.setName(name)
    s.setMarks(marks)
    students.append(s)
for s in students:
    print('Hello', s.getName())
    print('Your marks are:', s.getMarks())
    print()
