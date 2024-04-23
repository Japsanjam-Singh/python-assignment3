import csv

class Book:
    GENRE_NAMES = {
        0: "Romance",
        1: "Mystery",
        2: "Science Fiction",
        3: "Thriller",
        4: "Young Adult",
        5: "Children's Fiction",
        6: "Self-help",
        7: "Fantasy",
        8: "Historical Fiction",
        9: "Poetry"
    }
    
    def __init__(self, isbn, title, author, genre_code, available):
        #this initialiser section contains 5 attributes
        self.isbn = isbn
        self.title = title
        self.author = author
        self.genre_code = genre_code
        self.available = available
    
    def get_genre_name(self):
        # this method gets genre names of books
        return self.GENRE_NAMES.get(self.genre_code, "Unknown Genre")

    def __str__(self):
        # this string method returns the 5 attributes in a string
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Genre Code: {self.genre_code}, Available: {self.available}"

    def get_isbn(self):
        # this method gets the isbn number of the book
        return self.isbn

    def get_title(self):
        # this method gets the title of the book
        return self.title

    def get_author(self):
        # ṭhis method gets the author of the book
        return self.author

    def get_genre_code(self):
        # this method gets the genre code of the book
        return self.genre_code

    def get_availability(self):
        # this method gets the avalibility of the book
        return "Available" if self.available else "Borrowed"

    def borrow_it(self):
        # this method returns the availibilty of book to false if the book is borrowed 
        self.available = False

    def return_it(self):
        # this method returns the availibilty of book to true if the book is returned back

        self.available = True

def load_books(book_list, csv_path):
    # this method loads the whole catalog when the csv file is entered.
    while True:
        try:
            with open(csv_path, 'r', newline='') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  
                loaded_books = 0  
                for row in csv_reader:
                    if len(row) == 5:  
                        isbn, title, author, genre_code, available = row
                        genre_code = int(genre_code)  
                        available = available.lower() == 'true'  
                        book_list.append(Book(isbn, title, author, genre_code, available))
                        loaded_books += 1                     
            print("Book catalog has been loaded.")
            return loaded_books  
        except FileNotFoundError:
            csv_path = input("File not found. Re-enter the path to the CSV data file: ")
            continue
        except Exception as e:
            print(f"Error occurred while loading books: {e}")
            return 0


def print_menu(menu_heading, menu_options):
    # this function is use to print the menu when the correct csv file path is entered.
    print(menu_heading)
    print("=" * len(menu_heading))
    for keys, values in menu_options.items():
        print(f"{keys}: {values}")
    while True:
        user_input = input("Enter your selection: ")
        if user_input in menu_options:
            return user_input
        if user_input == '2130':
            return user_input
        else :
            print("invalid option.") 
            if user_input in menu_options: 
                return user_input

def print_books(book_list):
    # this function print the catalog in the terminal whenever the linked option number is entered.
    print("Print book catalog")
    print("ISBN".ljust(15), "Title".ljust(25), "Author".ljust(25), "Genre".ljust(20), "Availability".ljust(15))
    print("-" * 15, "-" * 25, "-" * 25, "-" * 20, "-" * 15)
    for book in book_list:
        genre_name = Book.GENRE_NAMES.get(book.get_genre_code(), "Unknown Genre")
        print(book.isbn.ljust(15), book.title.ljust(25), book.author.ljust(25), genre_name.ljust(20), book.get_availability().ljust(15))


            
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

def find_book_by_isbn(book_list, isbn):
    # to find the book with isbn number
  """Finds a book by ISBN and returns its index"""
  for i, book in enumerate(book_list):
    if book.get_isbn() == isbn:
      return i
  return -1


def add_book(book_list):
    # function to add the book in the catalog
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    genre_valid = False
    while not genre_valid:
        genre_input = input("Enter genre: ").title()
        genre_code = next((code for code, name in Book.GENRE_NAMES.items() if name.lower() == genre_input.lower()), None)
        if genre_code is not None:
            genre_valid = True
        else:
            print(f"Invalid genre name. Valid genre choices are: {', '.join(Book.GENRE_NAMES.values())}")
        
    book_added = Book(isbn, title, author, genre_code, True)
    book_list.append(Book(isbn, title, author, genre_code, True))
    with open( 'books.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([book_added.isbn, book_added.title, book_added.author, book_added.genre_code, book_added.available])  
    print(f"'{title}' with ISBN {isbn} successfully added.")



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