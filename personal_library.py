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
    print("5. Update a book")
    print("6. Exit")


def add_book():
    '''
    Adds a book to the library list.
    '''
    # Get all data for library 
    title = input("Enter book title to add: ").strip().title()
    author = input("Enter the author's name: ").strip().title()
    year_published = input("Enter the year the book was published: ").strip()
    

    # create the dictionary for book
    book = {"title": title, "author": author,
             "year_published": year_published}
    if book in library:
        print("The book is already in the library.")
    else:
        # Add book to the library
        library.append(book)
        print(f"Added {title} to the Library.")
    

def remove_book():
    '''
    Removes a book from the library list
    '''
    # Recieve input for book removal
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
        print(f"{i}: {book["title"]} by {book["author"]} published "
              f"{book["year_published"]}")
    print("End of library.")


def search_book():
    '''
    Basic search functionality
    '''
    search = input("Enter a book title to search: ").lower().strip()
    for book in library:
        if search in book["title"].lower():
            print(f"Book found: {book["title"]} by {book["author"]},"
                  f" published in {book["year_published"]}")
    print("End of Results.")

def update_book():
    '''
    Allows you to update information on a book
    '''
    # Request book to update
    update = input("Which book would you like to update: ").lower().strip()
    for book in library:
        if update in book["title"].lower():
            print(f"Updating: {book["title"]}")
            print("Please choose an option to update. \n1. Title\n2. Author"
                "\n3. Publication Year")
            choice = input()
            if choice == "1":
                book["title"] = input("Please enter a new title: ")
            elif choice == "2":
                book["author"] = input("Please enter new author: ")
            elif choice == "3":
                book["year_published"] = input("Please enter"
                " new publication year: ")
            else:
                print("Book not found.")


def main():
    '''
    Main function for choice
    '''
    # Create validation
    valid = False
    
    while not valid:
        show_menu()
        choice = input("Please Choose a Menu Option: ").strip()
        print()
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            list_books()
        elif choice == "4":
            search_book()
        elif choice == "5":
            update_book()
        elif choice == "6":
            print("Goodbye")
            valid = True
        else:
            print("Invalid choice. Try Again.")


if __name__ == "__main__":
    main()