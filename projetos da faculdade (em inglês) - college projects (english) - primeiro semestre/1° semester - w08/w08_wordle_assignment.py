
print(f'Welcome to the word guessing game!')

secret_word = 'fly'
guess = ''
count = 0 # variable that will count the amount of guesses 

output = ["_", "_", "_"]

while guess != secret_word:
    guess = input('Whats is your guess? ')
    
    count += 1  # starts as count = 0 + 1
    count # always keep the last value of count
    
    if guess == secret_word:
        print('You guessed it!')
        print(f'It took you {count} guesses.\n')
        guess = True

    if len(guess) != len(secret_word):
        print('The guess must be the same number of letters as the secret.')

    for x in range(len(guess)):
      found = False
      for y in range(len(secret_word)):
         if guess[x] == secret_word[y]:
            if x == y:
               output[x] = guess[x].capitalize()
               
               break
            else:
               output[x] = guess[x].lower()
    print(f"Your hins is: {output[0]} {output[1]} {output[2]}") #Every time that the user inputs a word with the same lenght as the secret word, a hint will be given.


    


