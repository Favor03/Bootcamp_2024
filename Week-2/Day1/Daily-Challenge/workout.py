my_string = input("Write a character with at least ten words:")

if my_string < 10:
    print("string not long enough")
elif my_string > 10:
    print("string too long")
else:
    print("perfect string")