def decor1(func):
    def inner1(name):
        names = ['CM', 'PM']
        if name in names:
            print('#' * 30)
            print('Hello {}, very very good morning, you are very important'.format(name))
            print('#' * 30)
        else:
            func(name)

    return inner1


@decor1
def wish(name):
    print('Good morning, ', name)


wish('Amin')
