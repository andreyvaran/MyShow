from collections import deque

dq = deque(['a', 'b', 'c'])

dq.append('d')
dq.appendleft('z')

print(dq.pop())
print(dq.popleft())

print(dq)
