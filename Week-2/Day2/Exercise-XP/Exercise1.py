my_fav_numbers = {2, 5, 13, 11, 7, 9, 15, 30, 70}

# print(my_fav_numbers)

# my_fav_numbers.add(58)

# my_fav_numbers.add(88)

# print(my_fav_numbers)

# my_fav_numbers.remove(30)

# print(my_fav_numbers)

friend_fav_numbers = {13, 11, 16, 18, 33, 37}

our_fav_numbers = f"this is the union of {my_fav_numbers|friend_fav_numbers}" #when adding 2  set we use |(called union)

print(our_fav_numbers)

our_fav_numbers = f"this is the intersection {my_fav_numbers&friend_fav_numbers}"

print(our_fav_numbers)