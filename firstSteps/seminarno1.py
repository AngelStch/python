
# zad 1
# n = float(input())
# print(n*2.54)

# zad2
# n = input()
# print(f"Hello, {n}!")

# zad 3
# name = input()
# surname = input()
# age = input()
# town = input()
# print(f"You are {name} {surname}, a {age} years old person from {town}.")

# zad 4
# try:
#     zelenchuk = float(input("Цена за килограм заленчук: "))
#     plod = float(input("Цена за килограм плод: "))
#     zelenchukObs = int(input("Общо заленчуци: "))
#     plodObsh = int(input("Общо плодове: "))
#     if(zelenchuk<=0 or plod<=0 or zelenchukObs<=0 or plodObsh<=0):
#         raise ValueError(" ne moje <=0 ")
#     print(((zelenchuk*zelenchukObs+plod*plodObsh)/1.9))
# except e:
#  print(e)   

# zad 5
# while(True):
#     try:
#         dollar = float(input("100-5000: "))
#         liri = int(input("100-5000: "))
#         komiss = int(input("Komissionna: "))
#         kommis = "0.0"+f"{komiss}"
#         kommis =100 - float(kommis)
#         if(dollar<100 or dollar>5000 or liri<100 or liri>5000 or komiss>6 or komiss<1):
#             raise ValueError("Check the interval")
#         all = ((dollar*1.76 + liri*0.052)/1.96)/kommis
#         print(all)
#         break
#     except e:
#      print(e) 

# zad 6
# while(True):
#     try:
#         kucheHrana = int(input("hrana za kucheta(opakovki): "))
#         kotkaHr = int(input("hrana za kotkim(opakovki): "))
#         if(kucheHrana<0 or kotkaHr<0):
#             raise ValueError("Hraanata ne moje da e negativna")
#             break
#         print(f"{kucheHrana*2.5+kotkaHr*4} lv.")
        
#     except e:
#        print(e)

