class Car():

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def rename_Car(self, new_name):
        self.name = new_name

        #this next def helps us to reduce the lines of our codes. 

    def presentation_car(self):

        print(f"\n My name is {self.name} and my price is ${self.price}")

my_car1 = Car("BMW", 2000)

my_car2 = Car("Lexus", 4000)

my_car3 = Car("Toyota", 5000)

my_car1.presentation_car()
my_car1.rename_Car("Range Rover")
my_car1.presentation_car()

