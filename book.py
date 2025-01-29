class Book:
    # constructor - special method to initialize attributes
    def __init__(self, title, author, ISBN=None, price=None):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price

    # methods
    def sell(self):
        print('Book', self.title, 'is_sold')

    def info(self):
        print('Book title=', self.title, 'author=', self.author, 'ISBN=', self.ISBN, 'price=', self.price)
