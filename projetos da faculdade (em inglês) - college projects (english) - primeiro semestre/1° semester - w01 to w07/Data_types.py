age = input(f'How old are you?\n') 
print('On your next birthday, you will be ' + str(int(age)+1) + '\n')

egg_carton = input(f'How many egg cartons do you have?\n')
print('You have ' + str(int(egg_carton)*12) + ' eggs.')

cookies = input(f'How many cookies do you have?\n')
people = input(f'How many people are there?\n')
print('Each person may have ' + str(float(cookies) / float(people)) + ' cookies.')