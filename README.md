### Overview

The `Book` class is designed to represent a book with relevant attributes such as title, author, ISBN, and price. It also provides two methods:

- **sell**: Simulates the selling of the book by printing a message indicating the book has been sold.
- **info**: Displays the book's information, including the title, author, ISBN, and price.

### Features

- **Attributes**:
  - `title` (str): The title of the book.
  - `author` (str): The author of the book.
  - `ISBN` (str, optional): The ISBN number of the book (optional).
  - `price` (float, optional): The price of the book (optional).

- **Methods**:
  - `sell`: Prints a message stating the book has been sold.
  - `info`: Prints the details of the book.

### Example Usage

```python
# Creating a Book object
book1 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", ISBN="1234567890", price=10.99)

# Getting the information about the book
book1.info()

# Selling the book
book1.sell()
```

### UML Class Diagram

Here is the UML class diagram for the `Book` class:

```plaintext
+-------------------------+
|         Book             |
+-------------------------+
| - title: str             |
| - author: str            |
| - ISBN: str (optional)   |
| - price: float (optional)|
+-------------------------+
| + __init__(title, author, ISBN, price) |
| + sell()                 |
| + info()                 |
+-------------------------+
```
