from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

chain = ChainMap(dict1, dict2)

print(chain['a'])
print(chain['b'])
print(chain['c'])

new_dict = {'d': 5}
new_chain = chain.new_child(new_dict)
print(new_chain['d'])
