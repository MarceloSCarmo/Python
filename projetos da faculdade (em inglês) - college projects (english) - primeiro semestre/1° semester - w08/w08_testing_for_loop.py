print('1° question\n')
colors = ["red", "blue", "green", "yellow"]
for color in colors:
    print(f'The color is: {color}')
print('\n')
print('2° question\n')
numbers = range(9)
for i in range(1, 9):  #for i in range(9): Essa não é a melhor forma
    print(i)           #    if i > 0:
                       #        print(i)
print('\n')
print('3° question\n')
even_numbers = range(21)
for number in range(2, 21, 2):
    print(number)