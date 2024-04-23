import csv

# Creating the class book and defining the dictionary of Genre names
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
