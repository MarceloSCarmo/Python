# create a while loop and the whole code should be inside it.
# add a if to add things, remove and so on...
# After the if stemment I would add a for loop to show up the numbers of the items
# 
items = []
item = None
prices = []
price = 0

option = 0


while option != '5':
    #give the user instructions about wich number his gonna use.
    print('Instructions\n\n1. Add a new item')
    print('2. Display the contents of the shopping cart')
    print('3. Remove an item (only needed for the final project deliverable)')
    print('4. Compute the total (only needed for the final project deliverable)')
    print('5. Quit')

    option = input(f'\nChoose a option: ')
    
    if option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
        print(f'Please enter a number')

    elif option == '1':
        print(f'type quit when done with buies')
    
        #the user needs to input informations
        while item != 'quit':
            item = input(f"What's the name of the item? ") # Add a new item in the cart
            if item != 'quit': # Ask for the price of the item
                
                price = float(input(f"What's the price of the {item}? $ "))
                print(f'{item} has been added to the cart.\n')
            
                items.append(item) # keep each item in the memory
                prices.append(price) # keep each price in the memory
    
    elif option == '2':
        print(f'The items added in the shopping cart are:')
        i = 0
        for item in items:
            i += 1
            print(f'{i}.{str(item).capitalize()}')
    
    #elif buy = number...
    elif option == '3':#elif buy = number...
        remove = input(f'Would you like to remove an item? ') # Remove an item of the list
        remove_number = 0

        if remove.lower() == 'yes':
            i = 1
            for item in items:
                print(f'{i}.{str(item).capitalize()}')
                i += 1
            remove_number = int(input(f'Which item would you like to remove? ')) # User will remove an especific item of the list.
            if remove_number > len(items):
                print('Sorry, that is not a valid item number.')
            else:
                items.pop(remove_number - 1)
                i = 1
                for item in items:
                    print(f'{i}.{str(item).capitalize()}')
                    i += 1
    
    elif option == '4':
        i = 0
        for price in prices:
            i += price
            
    
        print(f'The total is: $ {i:.2f}')
    

print(f'Thank you for shopping with us!')  