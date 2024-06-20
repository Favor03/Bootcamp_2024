class Car():

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def print_my_price(self):
        print(f"\n My price is ${self.price}\n")

    def change_price(self, percentage):
        self.price = (self.price - (self.price * percentage)/100)
        return self.price    


my_car1 = Car("BMW", 2000)
my_car2 = Car("Lexus", 4000)
my_car3 = Car("Toyota", 5000)   

my_car2.print_my_price()
my_car2.change_price(50)
my_car2.print_my_price()