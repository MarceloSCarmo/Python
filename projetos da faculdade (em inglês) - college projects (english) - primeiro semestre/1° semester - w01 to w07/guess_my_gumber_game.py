
import random

keep_playing = "yes"

while keep_playing.lower() == 'yes':
    number = random.randint(1, 100) 
    user_number = 0
    count = 0 ## This variable will count how many gesses the user has made.

    print(f"What's the magic number? {number}")


    while number != user_number:  ## Works the programm while these two numbers are different
        user_number = int(input(f"What's your guess? "))
    
        count == count  ## variable initialize as the valeu of 0
        count += 1 ## sum of count + 1, as long as the user try to guess, 1 attemp will be added at this point.
    
        if number > user_number:
            print("Higher")
        elif number == user_number:
            print(f'You guessed it!\n')
            print(f"Attempts: {count}")
        else:
            print('Lower')

    keep_playing = input(f"Do you want to play again (yes/no)? ")



 ## input(f"Do you want to play again? ")
