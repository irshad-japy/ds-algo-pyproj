from com.durga.oops.Student import Student


class College:
    def __init__(self):
        self.clg_name='AHCET'
        self.clg_addr='Hyd'

    def take_admission(self):
        print('Seat is not available to take admission')

s1=Student()
s1.talk()

c1=College()
c1.take_admission()