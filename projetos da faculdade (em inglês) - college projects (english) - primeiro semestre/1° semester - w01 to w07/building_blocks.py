
positive_number = float(input(f'Please, type a positive number: '))


while positive_number < 0:
    print(f"Sorry, this isn't a positive number")
    positive_number = float(input(f'Please, type again a positive number: '))

print(f'The number is: {positive_number:.2f}')

answer = ""

while answer != "yes":
        answer = input(f"May I have a piece of candy?\n")

print(f"Thank you.")