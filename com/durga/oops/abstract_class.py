from abc import *


class Test(ABC):
    @abstractmethod
    def m1(self):
        pass


class TTest(Test):
    def m1(self):
        print('m1-method')

    @abstractmethod
    def m2(self):
        pass


class TTTest(TTest):
    def m2(self):
        print('m2-method')


t = TTTest()
print(id(t))
t.m1()
t.m2()