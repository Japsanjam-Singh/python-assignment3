def remove_book(book_list):
    # to remove the book from the database after the correct information is entered.
    isbn = input("Enter the 13-digit ISBN format (999-9999999999): ")

    index = find_book_by_isbn(book_list, isbn)
    if index != -1:
        removed_book = book_list.pop(index)
        print(f"Book with ISBN {isbn} titled '{removed_book.get_title()}' has been removed from the library.")
    else:
        print("No book found with that ISBN.")

        # Save the updated book catalog to the CSV file
        with open('books.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["ISBN", "Title", "Author", "Genre Code", "Available"])
            for book in book_list:
                csv_writer.writerow([book.isbn, book.title, book.author, book.genre_code, book.available])

def main():
    # the main function of the whole program that regulates the whole projects function.
    print('Starting the system ...')
    csv_path = input("Enter the path to the CSV data file: ")
    book_list = []
    books_loaded = load_books(book_list, csv_path)
    if books_loaded > 0:
        menu_options = {
            '1': 'Search for books',
            '2': 'Borrow a book',
            '3': 'Return a book',
            '0': 'Exit the system',
        }

        choice = ''
        while choice != '0':
            choice = print_menu("\nReader's Guild Library - Main Menu", menu_options)

            if choice == '1':
                print("\n--search for book--")
                search_string = input("Enter your search value: ")
                search_result = search_books(book_list, search_string)
                if search_result:
                    print_books(search_result)
                else:
                    print("No matching books found.")
            elif choice == '2':
                print("\n--Borrow a book--")
                borrow_book(book_list)
            elif choice == '3':
                print("\n--Return a book--")
                return_book(book_list)
            elif choice == '2130':
                extented_menu = {
                    '1': 'Search for books',
                    '2': 'Borrow a book',
                    '3': 'Return a book',
                    '4': 'Add book',
                    '5': 'Remove book',
                    '6': 'Print all books',
                    '0': 'Exit the system',
                }
                while choice != '0':
                    choice = print_menu("\nReader's Guild Library - Librarian Menu", extented_menu)

                    if choice == '1':
                        print("\n--search for book--")
                        search_string = input("Enter your search query: ")
                        search_result = search_books(book_list, search_string)
                        if search_result:
                            print_books(search_result)
                        else:
                            print("No matching books found.")
                    elif choice == '2':
                        print("\n--Borrow a book--")
                        borrow_book(book_list)
                    elif choice == '3':
                        print("\n--Return a book--")
                        return_book(book_list)
                    elif choice == '4':
                        print("\n--Add a book--")
                        add_book(book_list)
                    elif choice == '5':
                        print("\n--Remove a book--")
                        remove_book(book_list)
                    elif choice == '6':
                        print("\n--Print all books--")
                        print_books(book_list)
                    elif choice== '0':
                        print("\n--Exit the system--")
                        print("Book catalog has been saved.")
                        print("Good Bye!")
                        exit()
                choice = ''
        with open(csv_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["ISBN", "Title", "Author", "Genre Code", "Available"])
            for book in book_list:
                csv_writer.writerow([book.isbn, book.title, book.author, book.genre_code, book.available])
        
        print("\n--Exit the system--")
        print("Book catalog has been saved.")
        print("Good Bye!")

if __name__ == "__main__":
    main()