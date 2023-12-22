
print(f"What is the year and country that has the lowest life expectancy in the dataset?\n")

chosen_year = input(f'Enter the year of interest: ')
print('\n')
chosen_country = input(f'Choose a country: ')

with open("w11/life-expectancy.csv") as spanish_flu_file:           #Accessing the file
    
    lowest_life_expectancy = 100    #Any number lower than 100 will be counted in the for loop
    lowest_country = ""             #This variable will keep the country with lowest life expectancy
    lowest_year = 0                 ##This variable will keep the year with lowest life expectancy

    highest_life_expectancy = 0     #Any number greater than 0 will be counted in the for loop
    highest_country = ""            #This variable will keep the country with highest life expectancy
    highest_year = 0                #This variable will keep the year with highest life expectancy

    average_life_expectancy = 0         #Calculate the average of life expectancy
    count_expectancy = 0                #variable that will count the expectancy
    count_life_expectancy_times = 0     #Calculate how many times life expectancy will be counted

    highest_chosen_country = ""                 #Will show up the country with greater life expectancy in the year chosen by the user
    highest_chosen_life_expectancy = 0          ##Will show up the greater life expectancy in the year and country chosen by the user
    
    lowest_chosen_country = ""                  #Will show up the country with lowest life expectancy in the year chosen by the user
    lowest_chosen_life_expectancy = 100         ##Will show up the lowest life expectancy in the year and country chosen by the user

    max_life_expectancy = 0                     #Showing Creativity and Exceeding Requirements
    min_life_expectancy = 100
    average_user_chooice = 0
    count_user_choice = 0                       #variable that will count the expectancy
    count_times = 0                             ##Calculate how many times life expectancy will be counted


    next(spanish_flu_file)
    for file in spanish_flu_file:               #Entity,Code,Year,Life expectancy (years)
        clean_data = file.strip()
        data = clean_data.split(',')            #Split the comma to separete the data into pieces
 

        entity = data[0]
        code = data[1]
        year = data[2]
        life_expectancy = float(data[3])


        if life_expectancy < lowest_life_expectancy:            #Finding lowest life expectancy in general
            
            lowest_life_expectancy = life_expectancy
            lowest_country = entity
            lowest_year = year

        if life_expectancy > highest_life_expectancy:           #Finding highest life expectancy in general
            
            highest_life_expectancy = life_expectancy
            highest_country = entity
            highest_year = year
    
        if chosen_year == year:                         #If the user types any year in the yearlist it will search for that information
            count_life_expectancy_times += 1            #How many times life expectancy will be counted
            count_expectancy += life_expectancy         #Total amounto of life expectancy since the year the user typed 
            
            if life_expectancy > highest_chosen_life_expectancy:                #Calculate the highest life expectancy in the year the user chose
                highest_chosen_life_expectancy = life_expectancy
                highest_chosen_country = entity                                 #Finding the country with highest life expectancy in the year the user chose

            if life_expectancy < lowest_chosen_life_expectancy:                 #Calculate the lowest life expectancy in the year the user chose
                lowest_chosen_life_expectancy = life_expectancy
                lowest_chosen_country = entity                                  #Finding the country with lowest life expectancy in the year the user chose

        if chosen_country == entity:                                            #Showing Creativity and Exceeding Requirements
            if life_expectancy > max_life_expectancy:                           #maximum life expectancy since the country the user typed
                max_life_expectancy = life_expectancy                                

            if life_expectancy < min_life_expectancy:                           #manimum life expectancy since the country the user typed
                min_life_expectancy = life_expectancy
            
            count_times += 1            
            count_user_choice += life_expectancy

    average_user_chooice = count_user_choice / count_times                          #Calculating the life expectancy average since the country the user typed

    average_life_expectancy = count_expectancy / count_life_expectancy_times        #Calculating the life expectancy average since the year the user typed

    print('\n')

    print(f'Min life expectancy: {lowest_life_expectancy}, Country: {lowest_country}, Year:{lowest_year}\n')
    print(f'Max life expectancy: {highest_life_expectancy}, Country: {highest_country}, Year:{highest_year}\n')

    print(f'For the year 1959:')
    print(f'The average life expectancy across all countries was {average_life_expectancy:.2f}')
    print(f'The max life expectancy was in {highest_chosen_country} with {highest_chosen_life_expectancy}\n')
    print(f'The min life expectancy was in {lowest_chosen_country} with {lowest_chosen_life_expectancy}\n')


    print(f'\nSecond part of the assignment')
    print(f'The min life expectancy {lowest_life_expectancy}')
    print(f'The max life expectancy {highest_life_expectancy}\n')

    
    print(f'Your chosen country: {chosen_country}, minimum life expectancy: {min_life_expectancy:.2f}, maximum life expectancy: {max_life_expectancy:.2f} and the average: {average_user_chooice:.2f} ')
    
