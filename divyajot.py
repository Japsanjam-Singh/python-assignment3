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

