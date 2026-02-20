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

    def save_to_file(self, filename="library.json"):
        """Save all books to a JSON File"""
        import json

        #Convert Book objects to dictionaries
        books_data = []
        for book in self.books:
            book_dict = {
                "title":book.title,
                "author":book.author,
                "year":book.year,
                "is_read": book.is_read,
                 "rating": book.rating 
            }
            books_data.append(book_dict)
            
        #Write to file
        with open(filename, 'w') as file:
            json.dump(books_data,file,indent=2)
        
        print(f"Library saved to {filename}")

    def load_from_file(self, filename="library.json"):
        """Load books from JSON file"""
        import json
        import os

        #Check if file exists   
        if not os.path.exists(filename):
            print("No saved library found. Start fresh!")
            return
        
        #Read from file
        try:
            with open(filename, 'r') as file:
                books_data = json.load(file)

            #Convert dictionaries back to Book objects
            self.books = []
            for book_dict in books_data:
                book = Book(
                    book_dict["title"],
                    book_dict["author"],
                    book_dict["year"]
                )
                book.is_read=book_dict["is_read"]
                book.rating = book_dict.get("rating", 0)
                self.books.append(book)

            print(f"Loaded {len(self.books)} books from {filename}")

        except json.JSONDecodeError:
            print("Error reading library file. Starting fresh!")

    def search_by_title(self, search_term):
        """Search for books by title"""
        results = []
        for book in self.books:
            if search_term.lower() in book.title.lower():
                results.append(book)

        return results

    def search_by_author(self, search_term):
        """Search books by author"""
        results = []
        for book in self.books:
            if search_term.lower() in book.author.lower():
                results.append(book)

        return results

    def filter_by_status(self, read_status):
        """Filter books by read/unread status
    
        Args:
            read_status : True for read books, False for unread books
        """
        results = []
        for book in self.books:
            if book.is_read == read_status:
                results.append(book)
        
        return results
    
    def display_search_results(self, results, search_type=""):
        """Display a list of books from search reults."""

        if not results:
            print(f"No books found{search_type}.")
            return
        
        print(f"\n---Search Results {search_type}---")

        for index, book in enumerate(results, start=-1):
            print(f"{index}.{book}")
        print(f"\nFound {len(results)} book(s)")

    def rate_book(self, title):
        """Find a book and set its rating."""
        for book in self.books:
            if book.title.lower() == title.lower():
                while True:
                    try:
                        rating = int(input("Rate this book(1-5 stars): "))
                        book.set_rating(rating)
                        break
                    except ValueError:
                        print("Please enter a number between 1 and 5.")
                return
            
            print(f"Book '{title}' not found in your library.")

    def show_statistics(self):
        """Display library statistics."""
        if not self.books:
            print("Your library is empty. Add some books first!")
            return
        
        total_books = len(self.books)
        read_books = sum(1 for book in self.books if book.is_read)
        unread_books = total_books - read_books
        
        # Calculate percentage read
        percent_read = (read_books / total_books * 100) if total_books > 0 else 0
        
        # Calculate average rating (only for rated books)
        rated_books = [book for book in self.books if book.rating > 0]
        if rated_books:
            avg_rating = sum(book.rating for book in rated_books) / len(rated_books)
            avg_rating_str = f"{avg_rating:.1f} ★"
        else:
            avg_rating_str = "No ratings yet"
        
        print("\n" + "="*40)
        print("📊 LIBRARY STATISTICS")
        print("="*40)
        print(f"Total Books:       {total_books}")
        print(f"Read:              {read_books} ({percent_read:.1f}%)")
        print(f"Unread:            {unread_books}")
        print(f"Average Rating:    {avg_rating_str}")
        print(f"Rated Books:       {len(rated_books)}/{total_books}")
        print("="*40)

            
                


# if __name__ == "__main__":
#     print("Testing Library class....\n")

#     #Create a library
#     my_Library = Library()

#     #Test empty Library
#     my_Library.view_books()

#     #Add some books
#     my_Library.add_book("The Hobbit","J.R.R Tolkein", 1937)
#     my_Library.add_book("1984","George Orwell", 1949)
#     my_Library.add_book("Python Crash Course","Eric Matthes",2019)

#     # View All Books
#     my_Library.view_books()

#     # Mark one as read
#     my_Library.mark_book_read("1984")
#     my_Library.view_books()

#     #Delete a book
#     my_Library.delete_book("The Hobbit")
#     my_Library.view_books()

#     #Try to delete a book that doesnot exist
#     my_Library.delete_book("Harry Potter")
    

#     print("\n Library class working")

