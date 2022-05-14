class Student:
    def __init__(self):
        print('constructor execution...')
        self.name = 'Durga'
        self.rollno = 101
        self.marks = 90

    def talk(self):
        print('Hello I am: ', self.name)
        print('My Roll No: ', self.rollno)
        print('My Marks: ', self.marks)


s1 = Student()
print(s1.name)
print(s1.rollno)
print(s1.marks)
s1.talk()

s2 = Student()
print(id(s1))
print(id(s2))