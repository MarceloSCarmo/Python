
## Asking the data from the user.
porcentage = float(input("What's your grade porcentage?\n"))

## Calculating the grade.

if porcentage >= 90 :
    print('Grade A\n')
elif porcentage >= 80 :
    print('Grade B\n')
elif porcentage >= 70 :
    print('Grade C\n')
elif porcentage >= 60 : 
    print('Grade D\n')
else:
    print("Grade F\n")
 
print(f'Your letter grade is {porcentage:.2f}%')

## Calculate if the student was approved in the course.

if porcentage >= 70 :
    print('Congratulations, you are approved in the course.\n')
else:
    print('So sorry, you need to study more.\n')