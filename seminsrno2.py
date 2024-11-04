import math

# n = int(input())
# m = int(input())
# while(True):
#     if(n<m):
#         break
#     m = int(input())
#     n = int(input())

# lst = list()

# for i in range(n,m+1):
#     if(i%3==0 and i%4==0):
#         lst.append(i)

# suma = 1
# for i in range(len(lst)):
#     suma*=lst[i]

# print(suma)


# n = int(input())
# lst = list()
# for i in range(n):
#     lst.append(int(input()))
# lst.sort()
# print(f"the min element is {lst[0]} and the max is {lst[-1]}")


# fig = input("Izberete figura, Kvadrat, pravougulnik, triudulnik:")
# operaciq = input("izberetre oberaciq lice, perimetur")
# lstFig = ["Kvadrat", "pravougulnik","triudulnik"]
# lstOperacii = ["lice","obikolka"]

# if(fig == lstFig[0]):
#     if(lstOperacii[0]== operaciq):
#         input("izberete strana a: ")
#         print(a*a)
#     if(lstOperacii[1]== operaciq):
#         input("izberete strana a: ")
#         print(a+a*2)
# elif(fig == lstFig[1]):
#     if(lstOperacii[0]== operaciq):
#         input("izberete strana a: ")
#         input("izberete strana b: ")
#         print(a*b)
#     if(lstOperacii[1]== operaciq):
#         input("izberete strana a: ")
#         input("izberete strana b: ")
#         print(a+b*2)
# elif(fig == lstFig[2]):
#     if(lstOperacii[0]== operaciq):
#         input("izberete strana a: ")
#         input("izberete strana b: ")
#         c= math.sqrt(math.pow(a,2)+math.pow(b,2))
#         print(a*b/2)
#     if(lstOperacii[1]== operaciq):
#         input("izberete strana a: ")
#         input("izberete strana b: ")
#         print(a+b+c)

# d = int(input("Pick a calendar day"))
# m = int(input("Pick a calendar mounth"))
# y = int(input("Pick a calendar year") )
# deln = int(input("Pick a day"))
# daysAhead = int(input("days ahead:"))
# dni = ["ponedelnik","vtornik","srqda","chetv","petuk","subota","nedelq"]
# while(True):
#     if(((d>31 and m%2==0 and m<8)or (d>30 and m%2==1 and m<8)) or ((d>30 and m%2==0 and m>8)or (d>31 and m%2==1 and m>8))):
#         d = int(input("Pick a calendar day"))
#         m =int( input("Pick a calendar mounth"))
# d=d+daysAhead
# denq = d%7
# if(m==2):
#     while(d>28):
#         d -=28
#         m+=1
#     while(m>12):
#         m-=12
#         y+=1
# if(m%2  ==0 and m<8):
#     while(d>31):
#         d -=31
#         m+=1
#     while(m>12):
#         m-=12
#         y+=1
# elif(m%2  !=0 and m<8):
#     while(d>30):
#         d -=30
#         m+=1
#     while(m>12):
#         m-=12
#         y+=1
# if(m%2  ==0 and m>8):
#     while(d>30):
#         d -=30
#         m+=1
#     while(m>12):
#         m-=12
#         y+=1
# elif(m%2  !=0 and m<8):
#     while(d>31):
#         d -=31
#         m+=1
#     while(m>12):
#         m-=12
#         y+=1
    
# print("d\\m\\y", dni[denq])


command = input()
sumaProsti =0
sumaNeprosti =0
while(command!="stop"):
    n = int(command)
    if(n<0):
        print("number is nagative")
        command=input()
        continue
    isPrime = True
    for i in range(2,int(n/2+1)):
        if(n%i==0):
            sumaNeprosti+=n
            isPrime== False
            break
    if(isPrime== True):
        sumaProsti+=n
    command=input()

print(sumaProsti," e esumata na prostite chisla")
print(sumaNeprosti," e esumata na neprostite chisla")