from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza

class PizzaOrder(CustomPizza, SpecialtyPizza):

    def __init__(self, time):
        self.time = time
        self.pizzas = []

    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        piz = ""
        shmoney = 0
        for x in self.pizzas:
            piz += x.getPizzaDetails() + "\n----\n"
            shmoney += x.getPrice()

        return "******\nOrder Time: {}\n{}TOTAL ORDER PRICE: ${:.2f}\n******\n"\
               .format(self.time, piz, shmoney)
