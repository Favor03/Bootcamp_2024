# a = 33
# b = 200

# if a < b:
#     print("a is less than b")
# else:
#     print("a is not less than b")

note = float(input("\n Enter your mark"))

if note < 8 :
    print("\n You are very weak!!!")
elif note >= 8 and note < 12:
    print("\n You are weak")
elif note >= 12 and note < 15:
    print("\n You are average")
elif 15 <= note <= 20:
    print("\n You are excellent")
else:
    print("\n Write a valid value")



