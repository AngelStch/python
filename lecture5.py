# def suma(a,b):
#     return (a+b)
# def razlika(a,b):
#     return(a-b)

# def randomFunc(chislo):
#     if(chislo<0):
#         return
#     elif(chislo>100):
#         return 
#     print(chislo) 
import math
# def liceNaTr(operation,a,b,c):
#     if(operation=="S"):
#         return a*b/2
#     if(operation=="P"):
#         return a+b+c
# def liceNaKv(operation,a):
#     if(operation=="S"):
#         return a*a
#     if(operation=="P"):
#         return 4*a
# def liceNaPr(operation,a,b):
#     if(operation=="S"):
#         return a*b
#     if(operation=="P"):
#         return 2*a+2*b


# print("Choose a figure T-trinagle, S-Sqare, R-rectangule")
# typeFIg = input()
# if(typeFIg=="T"):
#     print("choose type: S-area, P-perimerur")
#     operation = input()
#     a = int(input("a="))
#     b = int(input("b="))
#     c = math.sqrt(math.pow(a,2)+ math.pow(b,2))
#     print(f"{operation} = {liceNaTr(operation,a,b,c)}")
# elif(typeFIg=="S"):
#     print("choose type: S-area, P-perimerur")
#     operation = input()
#     a = int(input("a="))
#     print(f"{operation} = {liceNaKv(operation,a)}")
# elif(typeFIg=="R"):
#     print("choose type: S-area, P-perimerur")
#     operation = input()
#     a = int(input("a="))
#     b = int(input("b="))
#     print(f"{operation} = {liceNaPr(a,b)}")

# print(suma(3,5))
# print(razlika(3,5))

# randomFunc(45)

# def isPalindome(a):
#     isTrue = True
#     for i in range(len(a)):
#         if(a[i]!=a[len(a)-1-i]):
#             isTrue = False
#     if(isTrue):
#         return 1
#     return 0

# a = input()
# print(isPalindome(a))


# def suma(a,b):
#     return (a+b)
# def razlika(a,b):
#     return(a-b)
# def umn(a,b):
#     return (a+b)
# def delene(a,b):
#     return(a-b)
# def stepen(a,b):
#     return math.pow(a,b)


# operation = input()
# a = int(input("a="))
# b = int(input("b="))
# if(operation=="+"):
#     print(suma(a,b))
# elif(operation== "-"):
#     print(razlika(a,b))
# elif(operation=="/"):
#     while(b==0):
#         print("b cnt be 0")
#         b= int(input("b="))
#     print(delene(a,b))
# elif(operation=="*"):
#     print(umn(a,b))
# elif(operation=="^"):
#     print(stepen(a,b))
import random

def zamenqne(lst,chislo):
    lst = list(lst)
    for i in range(len(lst)):
        if(lst[i]>chislo):
            lst[i]= 0

    return lst
    
lst = [random.randint(0, 100) for i in range(random.randint(0,20))]
chislo = int(input())
print(zamenqne(lst,chislo))