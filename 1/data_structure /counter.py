from collections import Counter

fruit_counter = Counter(['apple', 'orange', 'banana', 'apple', 'orange', 'banana', 'banana'])

print(fruit_counter.most_common(2))

fruit_counter.update(['apple', 'orange', 'kiwi'])

print(fruit_counter)

fruit_counter.subtract(['orange', 'orange', 'kiwi', 'kiwi', 'kiwi'])
fruit_counter.update([ 'kiwi','kiwi'])
print(fruit_counter)

print(list(fruit_counter.elements()))
