from com.durga.oops.interface import InterfaceDemo


class TTest(InterfaceDemo):
    def m1(self):
        print('m1-method')

    def m2(self):
        print('m2-method')


t = TTest()
t.m1()
t.m2()
