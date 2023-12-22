
print("You are going to go on vaccation, however, you don't know what to do.\nYour wife gives you 3 oppitions\nCAMPING\nTravel to the PARKS in california\nMOUNTAINS.\n")

choice = str(input("Which one will you choose?\n"))

if choice.lower() == "camping" :
    print("The camping will be close to the Salmon River, it's a place where We'll be able to enjoy nature and it's beauties.\n")
elif choice.lower() == "parks" :
    print("It's gonna be very fun to get in Calirfonia and enjoy the parks over there, We know that this aren't cheap, but we'll start earning the money soon.\n")
elif choice.lower() == "mountain":
    print("The mountains in Utah are very beautyful, you'll love to spend sometime there with family. You won't repent of choosing it.\n")
else:
    print("Option is not available.")

input(f'Why did you choose to go {choice}?\n')
print("You did a great choice, I hope you will have too much fun on this vaccation.")

transportation = str(input("Will you use a VAN or a BUS for this trip?\n"))

if transportation.lower() == "van":
    print("Good, a little bit less space.\n")
elif transportation.lower() == "bus":
    print("Much space for the intire family.")
else:
    print("Option is not available.")