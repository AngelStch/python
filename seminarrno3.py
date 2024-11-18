# a = input()
# dic = {}

# for i in range(len(a)):
#     if(a[i] not in dic):
#         temp = a.replace(a[i], "")
#         dic[a[i]] = temp
# print(dic)


# lst = map(str, input().split(" "))
# lst = list(lst)
# minE =len(lst[0])
# maxE =len( lst[1])
# for i in range(len(lst)):
#     if(len(lst[i])<minE):
#         minE = len(lst[i])
#     elif(len(lst[i])>maxE):
#         maxE = len(lst[i])

# lst.remove(maxE)
# lst.remove(minE)
# prin(lst)



# lst = map(str, input().split(" "))
# lst = list(lst)
# maxCount =0
# maxStastIndex = 0
# for i in range(len(lst)):
#     elFirst = lst[i]
#     stastIndex = i
#     count = 1
#     for j in range(i+1, len(lst)):
#         if(elFirst== lst[j]):
#             count+=1
#         else:
#             break
#     if(count>maxCount):
#         maxStastIndex = stastIndex
#         maxCount = count
# for i in range(maxStastIndex,len(lst)):
#     maxCount-=1
#     print(lst[i], end=",")
#     if(maxCount==0):
#         break

# import random
# m = int(input())
# n = int(input())
# matrix = []
# for i in range(m):
#     rtemp =[]
#     for j in range(n):
#         rtemp.append(random.randint(10,100))
#     matrix.append(rtemp)
# print(matrix)
# c = int(input())
# r = int(input())
# matrix.pop(r-1)
# for i in range(len(matrix)):
#     lst = list(matrix[i])
#     lst.pop(c-1)
#     matrix[i]=lst
# print(matrix)



# lst = map(int, input().split(" "))
# set1 = set(lst)
# lst2 = map(int, input().split(" "))
# set2 = set(lst2)

# print(len(set1))
# print(len(set2))

# set3 = set1.union(set2)
# print(set3)

# set4 = set1.difference(set2)
# print(set4)

# set5 = set1.symmetric_difference(set2)
# print(set5)
# element = int(input())
# set1.discard(element=element)

# set1.clear()
# set2.clear()


english_to_bg = {
    "hello": "здравей",
    "goodbye": "довиждане",
    "please": "моля",
    "thank you": "благодаря",
    "yes": "да",
    "no": "не",
    "morning": "сутрин",
    "night": "нощ",
    "friend": "приятел",
    "family": "семейство",
    "food": "храна",
    "water": "вода",
    "house": "къща",
    "car": "кола",
    "book": "книга",
    "computer": "компютър",
    "phone": "телефон",
    "cat": "котка",
    "dog": "куче",
    "love": "любов"
}

command  = input()
while(command!="Exit"):
    commands = command.split(' ')
    if(commands[0]== "add"):
        if(commands[1] not in english_to_bg):
            english_to_bg[commands[1]] = commands[2]
        else:
            print("the word alredy exists")
    elif(commands[0] == "Print"):
        print(english_to_bg)
    elif(commands[0]== "remove"):
        if(commands[1]  in english_to_bg):
            english_to_bg.popitem(commands[1], commands[2])
    elif(commands[0]== "chek"):
        if(commands[1] in english_to_bg):
            print(english_to_bg[commands[1]])            
        else:
            print("please enter the buldarian meaning")
            translate = input()
            english_to_bg[commands[1]] = translate

    else:
        print("wrong command")
    command = input()









