# Write a Python program to check the sum of three elements 
# (each from an array) from three arrays is equal to a target value.
#  Print all those three-element combinations.

# x = map(int, input("x = ").split())
# x = list(x)
# y= map(int, input("y = ").split())
# y = list(y)
# z = map(int, input("z = ").split())
# z = list(z)
# dedicatedSum = int(input())
# isfount = False
# for i in range(len(x)):
#    for c in range(len(y)):
#       for j in range(len(z)):
#          if(x[i]+y[c]+z[j]==dedicatedSum):
#             print(f"purvoto sreshtane na zadsdenata suma e pri elementite {i+1} = {x[i]} ot masiv x, {c+1} = {y[c]} ot masiv y, {j+1} = {z[j]} ot masiv z")
#             isfount = True
#             break
# if(isfount == False):
#    print("Ne moje da se napravi takava suma ot 3te masiva")
# print("x = ", x)
# print("y = ", y)
# print("z = ", z)

   



# Write a Python program that accepts six numbers as input and sorts them in descending order.
# Input consists of six numbers n1, n2, n3, n4, n5, n6 (-100000 <= n1, n2, n3, n4, n5, n6 <= 100000). The six numbers are separated by a space.
# try:
#     nums = map(int, input("Enter the nums you want to sort (6):\n").split())
#     nums = list(nums)
#     if(len(nums)>6):
#         raise ValueError()
#     nums.sort()
#     print(nums)
# except ValueError:
#     print("All numbers must be between -100000 and 100000 and max count is 6")


# 65. Write a Python program to move all zero digits to the end of a given list of numbers.
# Expected output

# lst = map(int, input().split(", "))
# lst = list(lst)
# for i in range(len(lst)):
#     if(lst[i] == 0):
#         lst.remove(0)
#         lst.append(0)
#         isDone = True
#         for j in range(i,len(lst)):
#             if(lst[j]!=0):
#                 isDone =False
#         if(isDone == True):
#             break
#         else:
#             i =0
# print(lst)
    

#     Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]

# lst = map(str, input().split(", "))
# lst = list(lst)
# listCompare = lst.copy()
# for i in range(len(lst)):
#     tempStr =  lst[i]
#     sumTemp =0
#     lsttemp = tempStr.split(",")
#     elFirst = list(lsttemp[0])
#     elFirst.pop(0)
#     elLast =list(lsttemp[len(lsttemp)-1])
#     elLast.pop(len(elLast)-1)
#     lsttemp.pop(0)
#     lsttemp.pop(len(lsttemp)-1)
#     lsttemp.insert(0,''.join(elFirst))
#     lsttemp.insert(len(lsttemp),''.join(elLast))
#     for j in range(len(lsttemp)):
#         sumTemp+=int(lsttemp[j])
#     lst[i] = sumTemp
# maxSum = lst.index(max(lst))
# print(listCompare[maxSum])
