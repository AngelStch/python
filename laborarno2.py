import math 

# x = 5
# y = 8
# print(x) if x<y else print(b)

# n = int(input())
# print("n>50") if n>50 else print("n<50")


# i = 1
# while(True):
#     print(i)
#     ++i
#     if i == 10:
#         break

# for i in range(1,11):
#     print(i)

# for i in range (97,123):
#     print(chr(i), end=" ")

# lst = []
# n = int(input())
# for i in range(n):
#     temp = int(input())
#     lst.append(temp)

# print(max(lst))


# n = int(input())
# max = int(input())
# for i in range(n-1):
#     temp = int(input())
#    if max<temp:
#          max = temp
#  print(max(lst))


# while(True):
#     y = int(input())
#     if(y== 0):
#         print("INNCORRECT INPUT")
#         continue
#     print("Select operation: +,-,*,/")
#     operation = input()
#     if(operation == "+"):
#             print(x+y)
#     elif(operation == "-"):
#             print(x-y)
#     elif(operation == "/"):
#         if(y== 0):
#             print("INNCORRECT INPUT")
#         print((x/y))
#     elif(operation == "*"):
#             print(x*y)
#     else:
#         print("Incorrect")

# n = int(input())
# for i in range(1,n+1,2):
#     print(' ' *((n-i)//2),'*' * i,sep="")


# n = int(input())
# if(n%2 == 0 or n%3 == 0 or n%4 == 0 or n%5 == 0 or n%7 == 0):
#     print("Isnt prime")
# else:
#     print("Is prime")

# n = int(input())
# if(n%2 == 0):
#     print(chetno)

# lst = map(int, input().split(" "))
# lst = list(lst)
# vzeli =""
# otl =""
# for i in range(len(lst)):
#     if(lst[i]<50):
#         print(lst[i],end=" ")
#         lst.remove(lst[i])
#         i = 0
#     elif(lst[i]<75):
#         vzeli+=lst[i]
#         lst.remove(lst[i])
#         i = 0
#     elif(lst[i]<101):
#         otl+=lst[i]
#         lst.remove(lst[i])
#         i = 0
#  print(vzeli)
#  print(otl)

        
   
stringInp = input()
count=0
count+=stringInp.count('a')    
count+=stringInp.count('o')  
count+=stringInp.count('e')
count+=stringInp.count('i')
count+=stringInp.count('y')  
count+=stringInp.count('u') 
print(count)   




