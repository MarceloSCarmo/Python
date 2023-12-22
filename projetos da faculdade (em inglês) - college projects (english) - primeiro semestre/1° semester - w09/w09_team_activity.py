

numbers = []
number = -1

# Input numbers
while number != 0:
    number = int(input("Type a number: "))

    if number != 0:
        numbers.append(number)

# Sum and average       
sum = 0
largets = -1
smallest = 100000000000000000000000000000000000
sorted_list = sorted(numbers)

for number in numbers:
    sum += number

    count = len(numbers)
    average = sum / count

    if number > largets:
        largets = number

    for number in numbers:
        if number > 0 and number < smallest: 
            smallest = number
        

print(f"The sum is: {sum}")
print(f"The average is: {average:.2f}")
print(largets)
print(smallest)


for number in sorted_list:
    print(number)





#for serie_of_number in serie_of_numbers:
    #print(serie_of_numbers, end='')



