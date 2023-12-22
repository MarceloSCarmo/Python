
with open("w12/books_and_chapters.txt") as scriptures:      #open the file "books_and_chapters.txt"
    
    user_suggestion = input(f'which volume of scriptures you would like to learn about? ')
    count_user_suggestion = 0                       #this variable will count the amount of chapters in the largest book present in the volume of scriptures the user choose
    largest_book_user_suggestion = ''               #this variable will keep the name of the largest book in the volume of scriptures the user choose

    largest_book = 0                                #keep how many chapters the largest book has        
    book_name = ''                                  #keep the name of the largest book

    book_of_mormon = ''                             #Variable used to print all the books in the book of mormon
    count_book_of_mormon = 0                        #variable used to count the chapters in the book of Mormon
    name_book_of_mormon = ''                        #variable used to print the largest book in the book of Mormon
    
    for books in scriptures:

        clean_data = books.strip()
        data = clean_data.split(':')                #break the information in the file

        book = data[0]                              #the column with the name of the books  
        chapters = int(data[1])                     #the column with the number of chapters
        scripture = data[2]                         #the column with the naqme of scriptures volume


        if largest_book < chapters:                             #find the book that has the largest number of chapters in the scriptures.
            
            largest_book = chapters
            book_name = book

        if scripture.lower() == 'book of mormon':               #only prints the books in the Book of Mormon.

            book_of_mormon = book
            print(book_of_mormon)

            if count_book_of_mormon < chapters:                 #Find the book in the Book of Mormon that has the largest number of chapters.
                count_book_of_mormon = chapters
                name_book_of_mormon = book

        if scripture.lower() == user_suggestion:                #find the book in that volume of scripture that has the largest number of chapters.
            
            if count_user_suggestion < chapters:
                count_user_suggestion = chapters
                largest_book_user_suggestion = book
    
    
    print(f'\nThe book of {name_book_of_mormon.upper()} has the largest number of chapters in the book of Mormon: {count_book_of_mormon}\n')
    print(f'\nThe book of {book_name.upper()} has the largest number of chapters in the scriptures: {largest_book}\n')
    print(f'The book in this volume of scripture that the user suggested which has the largest number of chapters is: {largest_book_user_suggestion}\n')