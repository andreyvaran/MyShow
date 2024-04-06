from collections import namedtuple

Fruit = namedtuple('Fruit', ['name', 'quantity'])

apple = Fruit(name='Apple', quantity=5)
banana = Fruit(name='Banana', quantity=10)

print(apple.name, apple.quantity)
print(banana)

new_apple = apple._replace(quantity=8)
print(new_apple)
