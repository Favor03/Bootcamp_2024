# fruits = ["Banana", "Guava", "Apple", "Mango"]
# print(len(fruits))


list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in  list1:
#we were asked to use index. so we have to let the computer know the index value of 2o before replacing it

    new_value = list1.index(20)# this new value has become the index. so to replace it with 200 is as below
    
print(new_value)

list1[new_value] = 200

print(list1)


    
