
#----------------------------CORE REQUIREMENTS-------------------------

with open("w11/hr_system.txt") as hr_file:
    for file in hr_file:
        clean_line = file.strip()
        name = clean_line.split() #Now -> file = ['Alexia' =[0], '1913'=[1], 'Engineer'=[2], '84000'=[3]]
        
        employee = name[0]
        id = name[1]
        title = name[2]
        salary = float(name[3])

        pay_check = salary / 24

        if title.lower() == "engineer":
            pay_check += 1000
        
        print(f'{employee} (ID: {id}), {title} - ${pay_check:.2f}')




    