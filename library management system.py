class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}

    def add_book(self, book_title, author):
        if book_title not in self.books:
            self.books[book_title] = author
            print(f"Book '{book_title}' by {author} added successfully.")
        else:
            print("Book already exists in the library.")

    def display_books(self):
        if self.books:
            print("\nAvailable Books:")
            for title, author in self.books.items():
                print(f"{title} by {author}")
        else:
            print("No books available in the library.")

    def lend_book(self, book_title):
        if book_title in self.books:
            print(f"Book '{book_title}' has been borrowed.")
            del self.books[book_title]
        else:
            print("Sorry, the book is not available.")

    def return_book(self, book_title, author):
        self.books[book_title] = author
        print(f"Book '{book_title}' by {author} has been returned.")


def main():
    library_name = input("Enter the name of the library: ")
    library = Library(library_name)

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add a book")
        print("2. Display available books")
        print("3. Lend a book")
        print("4. Return a book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            library.add_book(title, author)
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            title = input("Enter the title of the book you want to lend: ")
            library.lend_book(title)
        elif choice == '4':
            title = input("Enter the title of the book you want to return: ")
            author = input("Enter the author of the book: ")
            library.return_book(title, author)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
