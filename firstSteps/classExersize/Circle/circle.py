import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, radius):
        if 0 < radius :
            self._radius = radius
        else:
            raise ValueError("The age must be above 0")
        
    def perimetur(self):
        return  2*math.pi*self._radius
    
    def area(self):
        return math.pi*math.pow(self._radius,2)
    
    def display(self):
        print(self.__str__())
        
    def __str__(self) -> str:
        return f"Circle with perimetur: {self.perimetur():0.02f} and lice: {self.area():0.02f}"

