def outer():
    print('outer fn execution started')

    def inner():
        print('inner fn execution')
    inner()
    inner()
    inner()
    inner()

    print('outer fn execution completed')


outer()
#inner()