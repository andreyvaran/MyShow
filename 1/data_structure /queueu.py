from collections import deque
from multiprocessing import Queue
from functools import lru_cache


dq = deque(['a', 'b', 'c'])


dq.append('d')
dq.appendleft('z')

print(dq.pop())
print(dq.popleft())

print(dq)

que_list = []

que_list.append()
que_list.pop()