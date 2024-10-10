from car import Car
from typing import List


def sort_price(items: List[Car]) -> List[Car]:
    sorted_cars = sorted(items, key=lambda car: car._car_price, reverse=True)
    return sorted_cars
def list_by_brand( brand, Cars ):
   sertanBrand = []
   for car in Cars:
      if (car._car_brand == brand):
         sertanBrand.append(car)
   return sertanBrand
def search_by_color( color, Cars ):
   sertanColor = []
   for car in Cars:
      if (car._car_color == color):
         sertanColor.append(car)
   sertanColor = sort_price(sertanColor)
   if(len(sertanColor)>0):
      return sertanColor[0]
   else:
      return "Car with this color doesnt exists"
def newest_car(Cars ):
   sertanBrand = []
   for car in Cars:
      if (car._manifacture_year == 2022):
         sertanBrand.append(car)
   return sertanBrand
