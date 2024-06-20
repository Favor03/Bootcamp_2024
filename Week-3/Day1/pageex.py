class Car():

    def __init__(self, name, price):

        self.name = name
        self.price = price

my_car1 = Car("BMW", 2000)

my_car2 = Car("Lexus", 4000)

my_car3 = Car("Toyota", 5000)

print(f"\n The name of my first car is {my_car1.name} and the price is ${my_car1.price}\n")

print(f"\n The name of my second car is {my_car2.name} and the price is ${my_car2.price}\n")

print(f"\n The name of my first car is {my_car3.name} and the price is ${my_car3.price}\n")
        