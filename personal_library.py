'''
Personal Library
Author: Luke Wieder
Description: Create a library with the ability to add and remove books,
             as well as list the boks added and search for a book.
'''
# Initialize an empty library
library: list[str] = []


def show_menu():
    '''
    Docstring for show_menu
    '''
    print("\nPersonal Library Menu")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. List all books")
    print("4. Search a book")
    print("5. Exit")


def add_book():
    '''
    Adds a book to the library list.
    '''
    title = input("Enter book title to add: ").strip()
    author = input("Enter the author's name: ").strip()
    year_published = input("Enter the year the book was published: ").strip()
    print(f"Added: {title}")

    # create the dictionary for book
    book = {"title": title, "author": author,
             "year_published": year_published}

    library.append(book)
    print(f"Added {title} to the Library.")
    

def remove_book():
    '''
    Removes a book from the library list
    '''
    removal = input("Enter book title to remove: ").strip()
    for book in library:
        if book["title"].lower() == removal.lower():
            library.remove(book)
            print(f"Removed {removal} from the Library.")
        else:
            print("Book not found.")

   

def list_books():
    '''
    Prints the library
    '''
    print("All books in library:")
    i = 0
    for book in library:
        i+=1
        print(f"{i}: {book["title"]}")
    print("End of library.")


def search_book():
    '''
    Basic search functionality
    '''
    search = input("Enter a book title to search: ").lower().strip()
    for book in library:
        if search in book["title"].lower():
            print(f"Book found: {book["title"]} by {book["author"]},"
                  f"published in {book["year_published"]}")
    print("End of Results.")

def main():
    '''
    Main function for choice
    '''

    
    while True:
        show_menu()
        choice = input("Please Choose a Menu Option: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            list_books()
        elif choice == "4":
            search_book()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try Again.")


if __name__ == "__main__":
    main()