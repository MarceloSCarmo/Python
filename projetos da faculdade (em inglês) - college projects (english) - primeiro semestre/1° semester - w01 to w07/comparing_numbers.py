number_1 = int(input('What is the first number?\n'))
number_2 = int(input('What is the second number?\n'))

if number_1 > number_2:
    print('The first number is greater')
else: 
    print('The first number is not greater')
if number_1 == number_2:
    print('The numbers are equal')
else:
    print('The numbers are not equal')
if number_1 < number_2:
    print('The second number is greater\n')
else:
    print('The second number is not greater\n')

favorite_animal = input(f'whats is your favorite animal?\n')

print()

if favorite_animal.lower() == "dog":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
