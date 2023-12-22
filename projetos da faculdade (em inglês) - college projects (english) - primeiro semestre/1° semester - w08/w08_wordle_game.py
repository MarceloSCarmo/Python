import random


words = ['sword', 'earth', 'eagle', 'green', 'shoes'] 
index = random.randint(0, len(words))
secret = words[index]
guess = ''
count = 1

print(secret)

output = ["_", "_", "_", "_", "_"]
while secret != guess and count <= 5:
   while True:
      guess = input(f'What is your {count}° guess? ')  
      if len(guess) != len(secret):
         print(f'Your guess must have {len(secret)} letters.')
      else:
         break
   
   for x in range(len(guess)):
      found = False
      for y in range(len(secret)):
         if guess[x] == secret[y]:
            if x == y:
               output[x] = guess[x].capitalize()
               
               break
            else:
               output[x] = guess[x].lower()

   print(f"{output[0]} {output[1]} {output[2]} {output[3]} {output[4]}")

               
      
   count += 1   
         
if guess == secret: 
   print('Congratulations, you did it!')  
else:
   print('Game Over!')


