class Person:
    def __init__(self, age=0, name=''):
        self.age = age
        self.name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if 0 < age < 101:
            self.__age = age
        else:
            raise ValueError("The age must be above 0 and below 100")

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if 0 < len(name) < 8:  # Adjusted length check
            self.__name = name
        else:
            raise ValueError("The name must be below 8 symbols")  # Updated message

    def display(self):
        print(self.__str__())
    
    def __str__(self) -> str:
        return f"Person {self.__name} with age {self.__age}"

