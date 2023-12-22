# Tuesday and Wednesday
# subtotal is $50 or greater (10% discount)

import datetime     # Import the date time library

week_day = datetime.datetime.now()      # calling the current day 

#   week_day.strftime("%A")    # changing from xx/xx/xx to the name of the day

discount = 0
total_amount_due = 0
sales_tax = 0

subtotal = float(input(f'What is the subtotal $? '))

if week_day.strftime("%A").lower() == 'tuesday' or 'wednesday':

    if subtotal >= 50:
        discount = (subtotal * 10) / 100

        print(f'The discount amount is {discount:.2f}')
    
    sales_tax = (subtotal * 6) / 100

    total_amount_due = subtotal - discount + sales_tax
    
    print(f'The sales tax is {sales_tax}%')
    print(f'Total: $ {total_amount_due:.2f}')


