class Person:
    def __init__(self, name, dd, mm, yyyy):
        print('Person object creation...')
        self.nanme = name
        self.dob = self.Dob(dd, mm, yyyy)

    def info(self):
        print('Name: ', self.nanme)
        self.dob.display()

    class Dob:
        def __init__(self, dd, mm, yyyy):
            print('DOB object creation...')
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy

        def display(self):
            print('DOB={}/{}/{}'.format(self.dd, self.mm, self.yyyy))


p = Person('Durga', 24, 8, 1947)
p.info()
