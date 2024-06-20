my_name = "Jack"
hello = "Hello World"
my_age = 27

my_list = [my_name, my_age, hello]

my_tuples = (my_name, my_age, hello)

print(my_list)

# the print above is for the full list. now if you want to print part you do this below

my_name = "Jack"
hello = "Hello World"
my_age = 27

my_list = [my_name, my_age, hello]

my_tuples = (my_name, my_age, hello)

# print(my_list[1:3])

# print(my_list[0:3])

# print(my_list[0:2]) #this is awesome.

#to modify in list you just write what you what to modify and the range. i.e where you want it to appear
# my_list[0] = my_age
# print("\nMy new list is", my_list)

#to remove anythin from the list you use .remove. for example we will remove my_age from the list
# there are 2 ways. you can also use pop. if you use pop you use index or range

# my_list.remove(my_age)
# print(my_list)

# we can use pop like this

# my_list.pop() # my default if you dont put index, it will remove the last word

# print(my_list)

# my_list.pop(1)
# print(my_list)


#when we add we use .append. for example

# my_list.append("Joshua is a student")
# print(my_list)

#to add 2 list we use this function .sum(+)

my_list2 = ["Football", "Achu", "Daniella"]

sum_total = my_list + my_list2

print(sum_total)
