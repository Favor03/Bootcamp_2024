# number = int(input("Enter a number:"))
# length = int(len("Enter the length in cm:"))

number = int(input("Enter a number:"))
length = int(input("Enter the length in cm:"))
 
multiple = number
my_list = []
while len(my_list) < length:
     my_list.append(multiple)
     multiple +=number
print(my_list)
