books = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Quit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Title: ")
        author = input("Author:")
        books.append({"title":title, "author": author})

    elif choice == "2":
        for book in books:
            print(f"{book['title']} by {book['author']}")

    elif choice == "3":1
        break
    