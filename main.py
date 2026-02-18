from library import Library

def main():
    """
    Main Program Loop
    """
    my_library = Library()

    #Load saved books when program starts
    my_library.load_from_file()

    print("+++Book Library Manager+++")
    print("Welcome to your personal Library!\n")

    while True: # Loop forever until user quits
        print("\n---Menu---")
        print("1. Add a book")
        print("2. View all books")
        print("3. Mark book as read")
        print("4. Delete a book")
        print("5. Quit")
       

        choice = input("\n Choose an option(1-5):")

        if choice == "1":
            print("\n---Add a Book ---")
            title = input("Title: ")
            author = input("Author: ")

            #Get year and handle errors
            while True:
                try:
                    year = int(input("Year Published:"))
                    break # If conversion worked, exit loop
                except ValueError:
                    print("Please enter a valid year(numbers only)")

            my_library.add_book(title, author, year)

        elif choice == "2":
            my_library.view_books()
        
        elif choice == "3":
            print("\n---Mark as Read---")
            title = input("Enter a book title: ")
            my_library.mark_book_read(title)
        
        elif choice == "4":
            print("\n---Delete Book---")
            title = input("Enter book title to delete: ")
            my_library.delete_book(title)
        
        elif choice == "5":
            my_library.save_to_file() # Add this line
            print("\nThanks for using Book Library Manager!")
            break # Exit the Loop
        else:
            print("\n Invalid choice. Please enter 1-5")

    # We will add the menu here in a moment
if __name__=="__main__":
        main()