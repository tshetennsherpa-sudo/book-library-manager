from book import Book #Import our Book class

class Library:
    """
    Manages a collection of Books
    """

    def __init__(self):
        self.books = [] # Empty shelf to start

    def add_book(self, title, author, year):
        """
        Add a book to the library
    
        """

        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f"Added '{title}' to your library")

    def view_books(self):
        """
        Display all books in the library

        """
        if not self.books: # If the shelf is empty
            print("Your library is empty. Add some books!")
            return
        
        print("\n----Your Library-------")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}.{book}")
        print(f"\nTotal books : {len(self.books)}")

    def delete_book(self, title):
        """
        Remove a book from the library by title
        """

        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Remove '{title}' from your Library.")
                return

        print(f"Book '{title}] not found in your library.")    
        
    def mark_book_read(self, title):
        """
        Find a book by title and mark it as read.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
               book.mark_as_read()
               return
        
        print(f"Book '{title}] not found in your library.")   

if __name__ == "__main__":
    print("Testing Library class....\n")

    #Create a library
    my_Library = Library()

    #Test empty Library
    my_Library.view_books()

    #Add some books
    my_Library.add_book("The Hobbit","J.R.R Tolkein", 1937)
    my_Library.add_book("1984","George Orwell", 1949)
    my_Library.add_book("Python Crash Course","Eric Matthes",2019)

    # View All Books
    my_Library.view_books()

    # Mark one as read
    my_Library.mark_book_read("1984")
    my_Library.view_books()

    #Delete a book
    my_Library.delete_book("The Hobbit")
    my_Library.view_books()

    #Try to delete a book that doesnot exist
    my_Library.delete_book("Harry Potter")
    

    print("\n Library class working")

