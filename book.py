class Book:
    """
    Represents a book in the library.

    """
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_read = False # New book start as unread

    def mark_as_read(self):
        """
        Mark this book as read
        """
        self.is_read = True
        print(f"Marked '{self.title}' as read!")

    def mark_as_unread(self):
        """
        Mark this book as unread
        """
        self.is_Read = False
        print(f"Marked '{self.title}' as unread!")
    
    def __str__(self):
        """
        Return a nice string representation of the book
        """
        status ="Read" if self.is_read else "Unread"
        return f"{self.title} by {self.author} ({self.year}) - {status}"
    
    # Test code - we will remove this later

if __name__ == "__main__":
        print("Testing Book class....\n")

        # Create a book
        book1 = Book("The Hobbit","J.R.R. Tolkein", 1934)
        print(book1)

        # Mark it as read
        book1.mark_as_read()
        print(book1)

        #Create another book
        book2 = Book("1984" , "George Orwell",1949)
        print(book2)

        print("\n Book class working")

        # Create your own favorite book
        my_book = Book("Bhagvad Geeta","Krishna",2000)
        print(my_book)

        #Mark it as read
        my_book.mark_as_read()
        print(my_book)

        #change it back
        my_book.mark_as_unread()
        print(my_book)

        