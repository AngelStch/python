from person1 import Person

class main:
    try:
        p = Person(25, "Aneliq")
        p.display()
        p.age = -11  
    except Exception as e:
        print(e)
    
    try:
        p2 = Person(101, "Aneliq") 
        p2.display()
    except Exception as e:
        print(e)
    
    try:
        p3 = Person(25, "qqqqqqqqqq")  
        p3.display()
    except Exception as e:
        print(e)
