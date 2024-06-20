class Car():

    def __init__(self, name, price):

        self.name = name
        self.price = price

    def rename_Car(self, new_name):
        self.name = new_name

        #this next def helps us to reduce the lines of our codes. 

    def presentation_car(self):

        print(f"\n My name is {self.name} and my price is ${self.price}")  



mycar1 = Car("Toyota", 2000)

print(f"\n The name of my first car is {mycar1.name} and the price is ${mycar1.price}\n")

#i want to change the name of my car and this is how is its done. it starts with the def rename above

mycar1.rename_Car("Range Rover")

print(f"\n the new name of my car is {mycar1.name}\n")



