# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.isAvailable = True
#         self.takenCount = 0

#     def takeAbook(self):
#         if self.isAvailable:
#             print(f"You have checked out the book '{self.title}'.")
#             self.isAvailable = False
#             self.takenCount += 1
#         else:
#             print(f"The book '{self.title}' is already checked out.")

#     def redeemBook(self):
#         if not self.isAvailable:
#             print(f"You have returned the book '{self.title}'.")
#             self.isAvailable = True
#         else:
#             print(f"The book '{self.title}' was already available.")

#     def display(self):
#         print(self.__str__())

#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

# class Library:
#     def __init__(self):
#         self.books = []

#     def addBook(self, title, author, year):
#         book = Book(title, author, year)
#         self.books.append(book)
#         print(f"Book '{title}' added to the library.")

#     def printAll(self):
#         if not self.books:
#             print("No books in the library.")
#         else:
#             for book in self.books:
#                 book.display()

#     def searchBookByTitle(self, title):
#         for book in self.books:
#             if book.title == title:
#                 return book
#         return None

#     def checkoutBook(self, title):
#         book = self.searchBookByTitle(title)
#         if book:
#             if book.isAvailable:
#                 book.takeAbook()
#                 return book
#             else:
#                 print("The book is already checked out.")
#         else:
#             print("There is no book with this name in the library.")

#     def returnBook(self, title):
#         book = self.searchBookByTitle(title)
#         if book:
#             if not book.isAvailable:
#                 book.redeemBook()
#             else:
#                 print("The book is already returned.")
#         else:
#             print("There is no book with this name in the library.")

#     def searchBookByTitleORAuthor(self, text):
#         for book in self.books:
#             if book.author == text or text in book.title:
#                 return book
#         return None

#     def notAvailableBooks(self):
#         for book in self.books:
#             if not book.isAvailable:
#                 print(f"{book.title} by {book.author}")

# class Reader:
#     def __init__(self):
#         self.takenBooks = []

#     def takeABook(self, book):
#         if len(self.takenBooks) >= 3:
#             print("You don't have permission to take more books.")
#         else:
#             self.takenBooks.append(book)
#             print(f"Book '{book.title}' added to your list.")

# class main:
#     lib = Library()
#     reader = Reader()

#     lib.addBook("The Great Gatsby", "F. Scott Fitzgerald", 1925)
#     lib.addBook("To Kill a Mockingbird", "Harper Lee", 1960)
#     lib.addBook("1984", "George Orwell", 1949)

#     lib.printAll()

#     lib.checkoutBook("Moby Dick")

#     book_checked_out = lib.checkoutBook("1984")
#     if book_checked_out:
#         reader.takeABook(book_checked_out)

#     lib.checkoutBook("1984")

#     lib.returnBook("1984")

#     lib.returnBook("1984")




class Animal:
    def __init__(self,name,species,age,health):
        self.name = name
        self.species = species
        self.age = age
        self.health = health
    
    @property
    def health(self):
        return self._health

    @health.setter
    def age(self, health):
        if 0 <= age <= 10:
            self._health = health
        else:
            raise ValueError("The health must be between 0 and 10")


    def print_info(self):
        print(self.__str__())

    def __str__(self):
        return f"Name: {self.name}, Vid: {self.species}, Age: {self.age}, Health: {self._health}"

class Mammal(Animal):
    def __init__(self,name,species,age,health,fur_color,diet):
            super().__init__(self,name,species,age,health)
            self.fur_color = fur_color
            self.diet = diet
    def print_info(self):
        print(super.print_info()+f", fur color: {self.fur_color}, diet: {self.diet}")

    
class Bird(Animal):
    def __init__(self,name,species,age,health,wing_span,can_fly):
            super().__init__(self,name,species,age,health)
            self.wing_span = wing_span
            self.can_fly = can_fly

    def print_info(self):
        print(super.print_info()+f", wing span: {self.wing_span}, can fly: {self.can_fly}")


class Reptile(Animal):
    def __init__(self,name,species,age,health,is_venomous,prefered_temperature):
            super().__init__(self,name,species,age,health)
            self.is_venomous = is_venomous
            self.prefered_temperature = prefered_temperature

    def print_info(self):
        print(super.print_info()+f", is venomous: {self.is_venomous}, prefered temperature: {self.prefered_temperature}")

class Zoo:
    def __init__(self):
        self.enclosures = {}

    def add_annimal(self,animal, enclosure_number):
        self.enclosures[enclosure_number] = animal

    def remove_animal(self,name):
        for i in range(len(self.enclosures)):
            if(self.enclosures[i].name == name):
                self.enclosures.pop(i)

    def list_animals_in_enclosures(self, enclosure):
        for i in range(self.enclosures[enclosure]):
            for j in range(len(i)):
                j.print_info()

    def transfer_animal(self,animal,enclosure_number):
        self.remove_animal(animal.name)
        self.add_annimal(animal,enclosure_number)

    def find_animal_by_Species(specie):
         for i in range(self.enclosures.items):
            for j in range(len(i)):
                if j is specie:
                    j.print_info()



