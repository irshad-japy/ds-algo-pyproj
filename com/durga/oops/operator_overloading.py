class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __str__(self):
        return 'The total pages={}'.format(self.pages)


t1 = Book(101)
t2 = Book(102)
t3 = Book(103)

print(t1 + t2 + t3)
