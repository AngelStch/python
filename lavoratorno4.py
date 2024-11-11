class Person:
    def __init__(self, name, lastName, age, nationality):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.nationality = nationality

    @property
    def name(self):
        return self._name

    @property
    def lastName(self):
        return self._lastName

    @property
    def age(self):
        return self._age

    @property
    def nationality(self):
        return self._nationality

    @name.setter
    def name(self, name):
        self._name = name

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    @nationality.setter
    def nationality(self, nationality):
        self._nationality = nationality

    def isAdult(self):
        if self._age >= 18:
            print(f"{self._name} is an adult")
        else:
            print(f"{self._name} is not an adult")

    def changeNationality(self, nationality):
        self._nationality = nationality
        print(self.__str__())

    def display(self):
        print(self.__str__())

    def __str__(self) -> str:
        return f"{self._name} {self._lastName}, Age: {self._age}, Nationality: {self._nationality}"

class Student(Person):
    def __init__(self, name, lastName, age, nationality, university, yearOfStudy):
        super().__init__(name, lastName, age, nationality)
        self._university = university
        self._yearOfStudy = yearOfStudy

    def display(self):
        print(self.__str__())

    def __str__(self) -> str:
        return f"{self._name} {self._lastName}, Age: {self._age}, Nationality: {self._nationality}, University: {self._university}, Year of Study: {self._yearOfStudy}"

class Lecturer(Person):
    def __init__(self, name, lastName, age, nationality, university, opit):
            super().__init__(name, lastName, age, nationality)
            self._university = university
            self.opit = opit

    @property
    def opit(self):
        return self._opit

    @opit.setter
    def opit(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._opit = value

    def isPensionen(self):
        if(self.age>65):
            print(f"the {self._name} should retire.")

    def zaPovishenie(self):
        self.opit+=1
        if (self._opit>10):
            print(f"the lecturer {self._name} e za povishenie")

    def kandidactvane(self):
        if(self._opit>5):
            print(f"the lecturer {self._name} won a grand")

    def addAge(self,age):
        self._age+=age
        self.isPensionen()
        
    def title(self):
        if(self._opit<10):
            print("assistent")
        elif(self._opit<15):
            print("docent")
        elif(self._opit<20):
            print("doctor")


    def display(self):
        print(self.__str__())

    def __str__(self) -> str:
        return f"{self._name} {self._lastName}, Age: {self._age}, Nationality: {self._nationality}, University: {self._university}, Opit: {self._opit}"





class Main:
    try:
        person1 = Person("Ivan", "Ivanov", 22, "Bulgarian") 
        lecturer1 = Lecturer("Ivan", "Ivanov", 10, "Bulgarian", "My", 9)
        student1 = Student("Petur", "Petrov", 13, "Indian", "TY University", 2)
        lecturer1.isPensionen()
        lecturer1.zaPovishenie()
        student1.display()
        person1.changeNationality("Greek")
        person1.isAdult()
    except Exception as e:
        print(e)
