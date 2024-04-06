from collections import defaultdict

dd = defaultdict(int)

dd['apple'] += 1
dd['banana'] += 1
dd['banana'] += 2

print(dd['kiwi'])

print(dict(dd))
