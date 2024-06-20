# user = int(input("\nwrite a number between 1 and 100"))

# if user %3 ==0:
#     print("Frizz")
# elif user %5 ==0:
#     print("Buzz")
# elif user (%3 ==0 and %5==0):

#     print("FrizzBuzz") this my own is wrong. the correct one is below

nb = int(input("\nEnter a number between 1 and 100\n"))

if nb < 1 or nb > 100:
    print("\nThis number is not between 1 and 100\n")
else:
    if nb % 3 == 0 and nb % 5 == 0:
        print("\nFrizzBuzz\n")
    elif nb % 3 == 0:
        print("\nFrizz\n")
    elif nb % 5 == 0:
        print("\nBuzz\n")
    else:
        print("\nThis number is not a multile of 3 and 5")
