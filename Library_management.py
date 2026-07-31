  #library management system

library =[]

def add_book():
    title = input("Enter the Book Title: ")
    author = input("Enter Author name: ")
    book = {
        "title": title,
        "author": author,
        "availability": True
    }
    library.append(book)
    print("Book added Successfully!...")

def veiw_book():
    if not library:
        print("No books availabe in the library: ")
        return
    
    print("\n ==== Available Books ====")

    for book in library:
        print(f"Title      : {book['title']}")
        print(f"Author     : {book['author']}")
        if book["availability"]:
            print("Available  : Yes")
        else:
            print("Available  : No")
        print()

def search_book():
    title = input("Enter the Book Title to search: ")

    found = False

    for book in library:
        if book["title"].lower() == title.lower():
            print("\n ==== Book Found ====")
            print(f"Title      : {book['title']}")
            print(f"Author     : {book['author']}")
            if book["availability"]:
                print("Available  : Yes")
            else:
                print("Available  : No")
            found = True   
            break

    if not found:
        print("Book not found.")

def borrow_book():
    title = input("enter book title to borrow: ")

    found = False

    for book in library:
        if book["title"].lower() == title.lower():

            found = True

            if book["availability"]:
                book["availability"] = False
                print(f"You have borrowed '{book['title']}' successfully.")
                break
            else:
                print(f"Sorry, '{book['title']}' is currently not available.")
                break

    if not found:
        print("Book not found.")

def return_book():
    title = input("enter the book title to return: ")

    found = False

    for book in library:
        if book["title"].lower() == title.lower():
            found = True

            if not book["availability"]:
                book["availability"] = True
                print(f"You have returned '{book['title']}' successfully.")
                break
            else:
                print(f"'{book['title']}' was not borrowed.")
                break

    if not found:
        print("Book not found.")

def delete_book():
    title = input("Enter the Book Title to delete: ")

    found = False

    for book in library:
        if book["title"].lower() == title.lower():
            found = True
            library.remove(book)
            print(f"'{book['title']}' has been deleted from the library.")
            break

    if not found:
        print("Book not found.")


while True:
    print("\n ==== My Library ====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()

    elif choice == '2':
        veiw_book()

    elif choice == '3':
        search_book()

    elif choice == '4':
        borrow_book()

    elif choice == '5':
        return_book()

    elif choice == '6':
        delete_book()

    elif choice == '7':
        print("Goodbye Visit again!")
        break
    else:
        print("Feature coming soon!")



