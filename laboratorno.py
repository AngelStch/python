from random import randint
# num = input()  
# kortej1  = tuple(int(digit) for digit in num)  
# kortej2 = tuple(int(digit) for digit in reversed(num))  
# print(kortej1)
# print(kortej2)

# n= int(input())
# lst = list()
# for i in range(n):
#     lst.append(randint(1,10))

# print(lst)
# for i in range(0,len(lst),2):
#     temp = lst[i]+lst[i+1]
#     lst.insert(i+1,temp)
# print(lst)

# text = input("Enter text: ")
# dictonary = {}
# for i in range(len(text)):
#     if text[i] == " ":
#         continue
#     elif text[i] in dictonary.keys():
#         dictonary[text[i]] += 1
#     else:
#         dictonary[text[i]] = 1

# print(dictonary)


# n = int(input())
# lst = list()

# for i in range(1,n+1):
#     lst.append(i)

# dictonary = {}
# temp =1
# for i in range(n-1,0,-1):
#     dictonary[temp] = lst[i]
#     temp+=1
# print(dictonary)

# movies = (
#     ("The Shawshank Redemption", 9.3),
#     ("The Godfather", 9.2),
#     ("The Dark Knight", 9.0),
#     ("Schindler's List", 8.9),
#     ("Pulp Fiction", 8.9),
#     ("The Lord of the Rings: The Return of the King", 8.9),
#     ("Forrest Gump", 8.8),
#     ("Inception", 8.8),
#     ("Fight Club", 8.8),
#     ("The Matrix", 8.7),
# )

# dictonary = {}
# for i in  range(len(movies)):
#     if movies[i][1] in dictonary.keys():
    
#         dictonary[movies[i][1]] += {movies[i][0]}
#     else:
#         dictonary[movies[i][1]] = movies[i][0]

# for key, value in sorted(dictonary.items(),reverse=True):
#     print(key, value)


print("add is for add item, check order:[orderr number] returns the clients that made that order, unique is for printing the unique orders that have been made.")
lst = list()
while(True):
    command = map(str,input().split(" "))
    command = list(command)
    if(command[0]=="add"):
        try:
            temp = command[1].split(":")
            temp = list(temp)
            orderNum = temp[0]
            clientName = temp[1]
            order = temp[2]
            lst.append((orderNum,clientName,order))
            break
        except Exception as e:
            print(e)

print(lst)

