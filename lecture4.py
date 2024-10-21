# stack = []

# stack.append(1)

# stack.append(2)

# stack.append(3)

# print(stack)
# print(stack.pop())


from collections import deque
import random
# queue = deque()
# queue.append(1)
# queue.append(2)
# queue.append(3)
# print(queue)
# print(queue.popleft())

data = [ random.randint(-20,20) for i in range(20)]
suma = map(sum,data)
print(suma)