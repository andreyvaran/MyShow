from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['banana'] = 3
ordered_dict['apple'] = 4
ordered_dict['pear'] = 1

for key, value in ordered_dict.items():
    print(key, value)

ordered_dict.move_to_end('banana')
print(ordered_dict)

print(ordered_dict.popitem())
