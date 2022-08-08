import time


class Test:
    def __init__(self):
        print('Object initialization...')

    def __del__(self):
        print('Fullfilling last wish and performing cleanup activities...')


t = Test()
t = None
time.sleep(10)
print('End of application')
