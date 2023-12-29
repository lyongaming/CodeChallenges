"""
    ÁREA DE UN POLÍGONO
    Crea una única funcion (importante que sólo sea una) que sea capaz 
    de calcular y retornar el área de un polígono.
    - La función recibirá por parámetro sólo UN polígono a la vez.
    - Los poligonos soportados serán Triángulo, Cuadrado y Rectángulo.
    - Imprime el cálculo del área de un polígono de cada tipo.
"""

from abc import ABC, abstractmethod

class Polygon(ABC):

    def __init__(self, base : float, height : float) -> None:
        super().__init__()
        self.base = base
        self.height = height

    @abstractmethod
    def area(self) -> float:
        pass

class Square(Polygon):
    def __init__(self, base : float, height : float):
        super.__init__(base, height)

    def area(self) -> float:
        return self.base * self.base
    
class Rectangle(Polygon):
    def __init__(self, base : float, height : float) -> None:
        super().__init__(base, height)

    def area(self) -> float:
        return self.base * self.height    

class Triangle(Polygon):
    def __init__(self, base : float, height : float) -> None:
        super().__init__(base, height)
    
    def area(self) -> float:
        return (self.base * self.height) / 2
    
def getArea(polygon : Polygon) -> float:
    return polygon.area()

triangle : Polygon = Triangle(10, 5)
rectangle : Polygon = Rectangle(2, 8)
square : Polygon = Square(3, 6)

print(getArea(triangle))
print(getArea(rectangle))
print(getArea(square))