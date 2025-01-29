from book import Book

if __name__ == '__main__':

    # Creating a Book object
    book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", ISBN="1234567890", price=10.99)

    # Getting the information about the book
    book1.info()

    # Selling the book
    book1.sell()
