def wish(name):
    print('Good morning', name)


greeting = wish

print(id(wish))
print(id(greeting))

wish('Durga')
greeting('Durga')

del wish
greeting('Sunny')