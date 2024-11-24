
# lst = map(int, input().split(" "))
# lst = list(lst)
# # lst.append("abv")
# # lst += "abv"
# lst2 = [1,2,3,4,5,6,7,8]
# # print(lst)
# # print(lst2[1:-1])
# # print(lst2[-1])
# # print(lst[0][2] +" "+lst[1][4])
# # lst = map(lst.append,lst2)
# # lst = list(lst)
# # print(lst)
# # for i in range(len(lst)):
# #     print(lst[i])
# # print(4 in lst)
# # print(lst.index(4))
# lst.extend(lst2)
# print(lst)
# lst = tuple(lst)
# names = {"ivan":"Ivanow"}
# dictionary = {0: (1, 2, 3, 4, 5), 1: (1, 2, 3, 4, 5)}
# for i in range(len(dictionary)):
#     print(dictionary[i])


m = int(input())
n = int(input())

a =[]
for i in range(m):
    b = []
    for j in range(n):
        temp = int(input())
        b.append(temp)
    a.append(b)

for i in range(len(a)):
    print(a[i])


