class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return isinstance(other, Product) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


"""
key - value 


hash(obj) in set -> true 

"""



"""
hash(a) == hash(b)



hash(a) = 10


10 - a -> b 

hash(a) = 3
hash(b) = 3


1
2
3 - a
4 - b
5


"""

product = Product('Laptop', 1000)
products_set = {product}

# print(product.__dict__)
# print(product in products_set)
#
# product.price = 900
# print(product in products_set)
#
# product.name = "New laptop"
# print(product in products_set)
#
# for elem in products_set:
#     print(elem.name)
#
#
# product.name = "Laptop"
# print(product in products_set)

# Короче аккуратно когда используете хеширование по какому-то полю. Если вы будете менять это поле получится жопа.
# Ибо потом вы эту штуку не отдебажите.

# 1 way to fix но тут есть нюансы с тем что
class IDProduct:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return isinstance(other, Product) and self.name == other.name

    def __hash__(self):
        # return id(self) - возвращаем адрес в памяти на обьект. Однако если у нас обьект будет наследоваться от
        # изменяемой структуры данных может получиться не кул
        return hash(id(self))

product = IDProduct('Laptop', 1000)
products_set = {product}
print(product in products_set)

product.price = 900
print(product in products_set)

product.name = "New laptop"
print(product in products_set)


