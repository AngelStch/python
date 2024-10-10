from car import Car
from carListFunctions import *

class main:
   car1 = Car("Toyota", "Corolla", 20000, "Red", 2022)
   car2 = Car("Honda", "Civic", 22000, "Blue", 2021)
   car3 = Car("Ford", "Mustang", 30000, "Black", 2019)
   car4 = Car("BMW", "3 Series", 35000, "White", 2022)
   car5 = Car("Audi", "A4", 40000, "Green", 2021)
   car6 = Car("BMW", "Model 3", 45000, "Gray", 2023)
   car7 = Car("Volkswagen", "Golf", 25000, "Green", 2020)
   carList= [car1,car2,car3,car4,car5,car6,car7]

   sortedCars = sort_price(carList)
   for car in sortedCars:
     print(car.display_info())

   print("--------------------------------------")
   carsBrand = list_by_brand("BMW",carList)
   for car in carsBrand:
      print(car.display_info())
   print("--------------------------------------")
   carColor = search_by_color("Green", carList)
   if(type(carColor) == Car):
     print(carColor.display_info())
   else:
      print(carColor)
   print("--------------------------------------")
   newestCars = newest_car(carList)
   for car in newestCars:
      print(car.display_info())