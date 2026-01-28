'''
Docstring for personal_library
'''

def show_menu():
    '''
    Docstring for show_menu
    '''
    print("\nPersonal Librar Menu")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. List all books")
    print("4. Search a book")
    print("5. Exit")


def add_book():
    '''
    
    '''
    pass # TODO


def remove_book():
    '''
    
    '''
    pass # TODO


def list_books():
    '''
    
    '''
    pass # TODO


def search_book():
    '''
    
    '''
    pass # TODO



def main():
    '''
    Docstring for main
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