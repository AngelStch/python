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

def test(combined):
    ls = []
    s2 = ""
    for s in combined.replace(' ', ''):
        s2 += s
        if s2.count("(") == s2.count(")"):
            ls.append(s2)
            s2 = ""
    return ls

combined = '( ()) ((()()())) (()) ()'
print("Parentheses string:")
print(combined)
print("Separate parentheses groups of the said string:")
print(test(combined))

combined = '() (( ( )() (  )) ) ( ())'
print("\nParentheses string:")
print(combined)
print("Separate parentheses groups of the said string:")
print(test(combined))



data = [ random.randint(-20,20) for i in range(20)]
suma = map(sum,data)
print(suma)