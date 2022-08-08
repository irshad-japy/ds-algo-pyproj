class Test:
    def m1(self):
        def calc(a, b):
            print('The sum is: ', a + b)
            print('The difference is: ', a - b)
            print('The product is: ', a * b)
            print('The average is: ', (a + b) / 2)

        calc(10, 20)
        calc(100, 200)
        calc(1000, 2000)


t = Test()
t.m1()
