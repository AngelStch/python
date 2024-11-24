
# testing lambda and list comprehensions
lst = [n*n for n in range(1,11)]
lst3 = map( lambda el : el+1, lst)
# lst2 = ', '.join(str(lst3))
print(list(lst3))


