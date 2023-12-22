
favorite_letter = input("What's your favotie letter? ")

word = 'commitment'

##### Capital letter

for index in range(len(word)):
    letter = word[index]
    
    if letter == favorite_letter.lower():
        print(letter.capitalize(), end='')
    else:
        print(letter.lower(), end='')

##### Replace it with an underscore

print('\n')

for index in range(len(word)):
    letter = word[index]
    
    if letter == favorite_letter.lower():
        print(letter.replace(letter,"_"), end='')
    else:
        print(letter.lower(), end='')