from Pizza import Pizza
class SpecialtyPizza(Pizza):
  
  def __init__(self,size,name):
    self.name = name
    super().__init__(size)
    if size=="S":
      super().setPrice(12)
    elif size=="M":
      super().setPrice(14)
    elif size=="L":
      super().setPrice(16)
  def getPizzaDetails(self):
    return f"SPECIALTY PIZZA\n\
Size: {super().getSize()}\n\
Name: {self.name}\n\
Price: ${super().getPrice():.2f}\n"
