class Test:
    def __init__(self):
        print('Object initialization...')

    def __del__(self):
        print('Fullfilling last wish and performing cleanup activities...')


t1 = Test()
t2 = Test()
print('End of application')
