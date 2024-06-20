class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self):
    print(f"Hello my name is  {self.name} and i am {self.age} years old")

  def rename_person(self, new_name):
    self.name = new_name



first_person = Person("John", 36)
first_person.show_details()

first_person.rename_person("Elvis")
first_person.show_details()






