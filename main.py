class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    # Add Book
    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book)

        # Save to file
        with open("books.txt", "a") as file:
            file.write(f"{book_id},{title},{author},Available\n")

        print("Book Added Successfully!")

    # Display Books
    def display_books(self):
        try:
            with open("books.txt", "r") as file:
                books = file.readlines()

                if not books:
                    print("No Books Available.")
                    return

                print("\n===== Book List =====")

                for book in books:
                    data = book.strip().split(",")

                    print("----------------------")
                    print("Book ID:", data[0])
                    print("Title:", data[1])
                    print("Author:", data[2])
                    print("Status:", data[3])

        except FileNotFoundError:
            print("Book file not found.")

    # Search Book
    def search_book(self):
        search_id = input("Enter Book ID to Search: ")

        try:
            with open("books.txt", "r") as file:
                books = file.readlines()

                for book in books:
                    data = book.strip().split(",")

                    if data[0] == search_id:
                        print("\nBook Found!")
                        print("Title:", data[1])
                        print("Author:", data[2])
                        print("Status:", data[3])
                        return

                print("Book Not Found.")

        except FileNotFoundError:
            print("Book file not found.")

    # Issue Book
    def issue_book(self):
        issue_id = input("Enter Book ID to Issue: ")

        updated_books = []

        try:
            with open("books.txt", "r") as file:
                books = file.readlines()

                found = False

                for book in books:
                    data = book.strip().split(",")

                    if data[0] == issue_id:
                        found = True

                        if data[3] == "Available":
                            data[3] = "Issued"
                            print("Book Issued Successfully!")
                        else:
                            print("Book Already Issued.")

                    updated_books.append(",".join(data) + "\n")

            with open("books.txt", "w") as file:
                file.writelines(updated_books)

            if not found:
                print("Book Not Found.")

        except FileNotFoundError:
            print("Book file not found.")

    # Return Book
    def return_book(self):
        return_id = input("Enter Book ID to Return: ")

        updated_books = []

        try:
            with open("books.txt", "r") as file:
                books = file.readlines()

                found = False

                for book in books:
                    data = book.strip().split(",")

                    if data[0] == return_id:
                        found = True

                        if data[3] == "Issued":
                            data[3] = "Available"
                            print("Book Returned Successfully!")
                        else:
                            print("Book was not issued.")

                    updated_books.append(",".join(data) + "\n")

            with open("books.txt", "w") as file:
                file.writelines(updated_books)

            if not found:
                print("Book Not Found.")

        except FileNotFoundError:
            print("Book file not found.")


# Main Program
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        library.add_book()

    elif choice == '2':
        library.display_books()

    elif choice == '3':
        library.search_book()

    elif choice == '4':
        library.issue_book()

    elif choice == '5':
        library.return_book()

    elif choice == '6':
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")