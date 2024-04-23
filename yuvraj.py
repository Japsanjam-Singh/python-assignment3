def borrow_book(book_list):
    # this function is use to borrow the book after entering the isbn number. 
    isbn = input("Enter the 13-Digit ISBN (format 999-9999999999): ")
    book = next((book for book in book_list if book.get_isbn().lower() == isbn.lower()), None)
    if book:
        if book.get_availability() == "Available":
            book.borrow_it()
            print(f"'{book.get_title()}' with ISBN {isbn} succesfully borrowed.")
        else:
            print(f"'{book.get_title()}' with ISBN {isbn} is not currently available.")
    else:
        print("No book found with that ISBN.")
              
def search_books(book_list, search_string):
    # this function is use to search the book from the catalog when the desired information is entered
    search_result = []
    for book in book_list:
        if search_string.lower() in book.get_isbn().lower() \
            or search_string.lower() in book.get_title().lower() \
            or search_string.lower() in book.get_author().lower() \
            or search_string.lower() in book.get_genre_name().lower():  
            search_result.append(book)
    return search_result



def return_book(book_list):
    # to return the book after the isbn number.
    isbn = input("Enter the 13-Digit ISBN (format 999-9999999999): ")
    book = next((book for book in book_list if book.get_isbn().lower() == isbn.lower()), None)
    if book:
        if book.get_availability() == "Borrowed":
            book.return_it()
            print(f"'{book.get_title()}' with ISBN {isbn} successfully returned.")
        else:
            print(f"'{book.get_title()}' with ISBN {isbn} is not currently borrowed.")
    else:
        print("No book found with that ISBN.")