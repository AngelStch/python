
# testing lambda and list comprehensions
lst = [n*n for n in range(1,11)]
lst = map( lambda x : str(x), lst)
lst2 = ', '.join(lst)
print(lst2)


