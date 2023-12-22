
friends = [] # friends with "S" means that i'm writing a list

name = None # This will be used in my loop to get the name of each friend
            # that I want to put in the list.

while name != 'end':
    name = input("Type the name of a friend: ")

    if name != 'end':
        friends.append(name)

print()
print("Your friends are:\n")

for friend in friends:
    print(friend)