import areas

vid = input("Vuvedetre ime na figurata:  ")

if(vid== "triangle"):
    a = int(input("Vuvdedete strana 1 :"))
    b = int(input("Vuvdedete strana 2"))
    print(areas.AreaTringle(a,b))
elif(vid== "square"):
    a = int(input("Vuvdedete strana 1"))
    print(areas.AreaSquare(a))
elif(vid== "rectangulare"):
    a = int(input("Vuvdedete strana 1"))
    b = int(input("Vuvdedete strana 2"))
    print(areas.AreaRectangulate(a,b))
elif(vid== "romb"):
    a = int(input("Vuvdedete strana 1"))
    b = int(input("Vuvdedete visochina 1"))
    print(areas.AreaRomb(a,b))
elif(vid== "triangle"):
    a = int(input("Vuvdedete strana 1"))
    b = int(input("Vuvdedete strana 2"))
    h = int(input("Vuvdedete visochina 1"))
    print(areas.AreaTrapec(a,b,h))

