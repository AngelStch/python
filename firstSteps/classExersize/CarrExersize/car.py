class Car():
   def __init__(self,car_brand,car_model,car_price,car_color,manifacture_year):
      self._car_brand =car_brand
      self._car_model =car_model
      self._car_price = car_price
      self._car_color = car_color
      self._manifacture_year =manifacture_year

   def display_info(self):
      return f"Car brand: {self._car_brand}\n"+ f"Car model: {self._car_model}"+f"Car price: {self._car_price}\n"+ f"Car color: {self._car_color}\n"+f"Manifacture year: {self._manifacture_year}"
      








