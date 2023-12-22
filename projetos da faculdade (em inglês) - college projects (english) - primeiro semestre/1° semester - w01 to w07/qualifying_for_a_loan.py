
from doctest import OutputChecker


print('Answer the questions below rating from 1 to 10.')

loan = int(input(f'How large is the loan? '))
credit_history = int(input(f'How good is your credit history? '))
income = int(input(f'How high is your income? '))
payment = int(input(f'How large is your down payment? '))

## check if the loan size is at least 5
status_loan = False

if loan >= 5:
    if credit_history >= 7 and income >= 7:
        status_loan = True
    elif credit_history >= 7 or income >= 7:
        if payment >= 5:
            status_loan= True
        else:
            status_loan = False
    else:
        status_loan = False
else:
    if loan <= 4:
        status_loan = False
    else:
        if credit_history >= 7 or income >= 7:
            status_loan = True
        elif credit_history >= 4 and income >= 4:
            status_loan = True 
        else:
            status_loan = False

if status_loan:
    print('Congratulations, you will recieve a loan:')
else:
    print('So sorry, you are not able to recieve a loan at this time.')