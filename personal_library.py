'''
Personal Library
Author: Luke Wieder
Description: Create a library with the ability to add and remove books,
             as well as list the boks added and search for a book.
'''

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


def add_book(library):
    '''
    Adds a book to the library list.
    '''
    title = input("Enter book title: ").strip()
    library.append(title)

    print(f"Added {title} to the Library.")
    return library


def remove_book(library):
    '''
    Removes a book from the library list
    '''
    title = input("Enter book title: ").strip()
    library.pop(title)

    print(f"Removed {title} from the Library.")
    return library


def list_books(library):
    '''
    Prints the library
    '''
    print(library)


def search_book():
    '''
    
    '''
    pass # TODO


def main():
    '''
    Docstring for main
    '''
    # Initialize an empty library
    library: list[str] = []
    
    while True:
        show_menu()
        choice = input("Please Choose a Menu Option: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            list_books(library)
        elif choice == "4":
            search_book()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try Again.")


if __name__ == "__main__":
    main()