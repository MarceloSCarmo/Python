
#   Open the provinces.txt file for reading
with open("2° semester - w05/provinces.txt") as txt_file:
    #   Create a list
    provinces_list = []

    reader = txt_file

    # Read the contents of the file into a list where each line 
    # of text in the file is stored in a separate element in the list.
    for files in reader:
        
        provinces_list.append(files)

    #   Print the entire list    
    print(provinces_list)
    print()

    #   Remove the first element from the list.
    print(provinces_list.remove("Alberta\n"))
    print()

    #   Remove the last element from the list.
    print(provinces_list.pop())
    print()

    #   Replace all occurrences of "AB" in the list with "Alberta".
    #   Get the index where AB is stored in the provinces list.
    while "AB\n" in provinces_list:
        ab_index = provinces_list.index("AB\n")
        provinces_list[ab_index] = "Alberta"

    print(provinces_list)
    print()

    #   Count the number of elements that are "Alberta" and 
    #   print that number.
    print(provinces_list.count("Alberta"))
    print()
    

    
    
     


