import heapq

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

heapq.heapify(numbers)
print("После heapify:", numbers)

heapq.heappush(numbers, 8)
print("После heappush(8):", numbers)

print("heappop():", heapq.heappop(numbers))
print("После heappop():", numbers)

print("3 наибольших элемента:", heapq.nlargest(3, numbers))
print("3 наименьших элемента:", heapq.nsmallest(3, numbers))
