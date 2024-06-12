cars = 100 #This line creates a name variable type: int
print("\nThe number of cars I have is {}".format(cars))

space_in_a_car = 4.0 #This line creates a name variable type: float
print("\nThere are only {} spaces in the car".format(space_in_a_car))

drivers = 30 #This line creates a name variable type: int
print("\nI have only {} drivers".format(drivers))

passengers = 90 #This line creates a name variable type: int

print("\nWe have more than {} passengers".format(passengers))

cars_not_driven = cars - drivers

print(f'\n the substraction of cars and drivers is {cars_not_driven}')

cars_driven = drivers

print(f"\n the value of cars driven is {drivers}")

carpool_capacity = cars_driven * space_in_a_car

print(f"\n The multiplication of cars driven and space in a car is {carpool_capacity}")

average_passengers_per_car = passengers / cars_driven

print(f"\n the division of passengers and cars driven is {average_passengers_per_car}")
