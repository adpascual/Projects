from Pizza import *
from CustomPizza import *
from SpecialtyPizza import *
from PizzaOrder import *
from OrderQueue import *

def testpizzas():
    sp1 = SpecialtyPizza("S", "Carne-more")
    cp1 = CustomPizza("M")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")

    assert cp1.getPizzaDetails() == \
    "CUSTOM PIZZA\n\
    Size: M\n\
    Toppings:\n\
            + extra cheese\n\
            + sausage\n\
    Price: $11.50\n"
    assert sp1.getPizzaDetails() == \
    "SPECIALTY PIZZA\n\
    Size: S\n\
    Name: Carne-more\n\
    Price: $12.00\n"
def testPizzaOrder():
    bh = OrderQueue()
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carnivore")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)
    cp1 = CustomPizza("M")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("M", "Carnivore")
    order2 = PizzaOrder(113000) #12:30:00PM
    order2.addPizza(cp1)
    order2.addPizza(sp1)
    bh.addOrder(order)
    bh.addOrder(order2)

    assert bh.processNextOrder() == \
    "******\n\
    Order Time: 113000\n\
    CUSTOM PIZZA\n\
    Size: M\n\
    Toppings:\n\
            + extra cheese\n\
            + sausage\n\
    Price: $11.50\n\
    \n\
    ----\n\
    SPECIALTY PIZZA\n\
    Size: M\n\
    Name: Carnivore\n\
    Price: $14.00\n\
    \n\
    ----\n\
    TOTAL ORDER PRICE: $25.50\n\
    ******\n"

    assert bh.processNextOrder() == \
    "******\n\
    Order Time: 123000\n\
    CUSTOM PIZZA\n\
    Size: S\n\
    Toppings:\n\
            + extra cheese\n\
            + sausage\n\
    Price: $9.00\n\
    \n\
    ----\n\
    SPECIALTY PIZZA\n\
    Size: S\n\
    Name: Carnivore\n\
    Price: $12.00\n\
    \n\
    ----\n\
    TOTAL ORDER PRICE: $21.00\n\
    ******\n"
