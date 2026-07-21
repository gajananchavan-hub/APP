class book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def details(self):
        return {
            "ID": self.book_id,
            "Title": self.title,
            "Author": self.author,
            "Available": self.available
        }


class patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed = []

    def borrow(self, book):
        if book.available:
            book.available = False
            self.borrowed.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed:
            book.available = True
            self.borrowed.remove(book)
            return True
        return False


class library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, new_book):
        self.books.append(new_book)

    def add_patron(self, new_patron):
        self.patrons.append(new_patron)

    def show_books(self):
        if not self.books:
            print("No books in the library.")
            return

        for b in self.books:
            status = "Available" if b.available else "Borrowed"
            print(f"{b.book_id} | {b.title} | {b.author} | {status}")

    def show_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
            return

        for p in self.patrons:
            borrowed = [b.title for b in p.borrowed]
            print(f"{p.patron_id} | {p.name} | Borrowed: {borrowed}")


lib = library()

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Add Patron")
    print("4. View Patrons")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Book ID: ")
        title = input("Book Title: ")
        author = input("Author: ")
        lib.add_book(book(book_id, title, author))
        print("Book added successfully.")

    elif choice == "2":
        lib.show_books()

    elif choice == "3":
        patron_id = input("Patron ID: ")
        name = input("Patron Name: ")
        lib.add_patron(patron(patron_id, name))
        print("Patron added successfully.")

    elif choice == "4":
        lib.show_patrons()

    elif choice == "5":
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        user = None
        selected_book = None

        for p in lib.patrons:
            if p.patron_id == patron_id:
                user = p
                break

        for b in lib.books:
            if b.book_id == book_id:
                selected_book = b
                break

        if user and selected_book:
            if user.borrow(selected_book):
                print("Book borrowed successfully.")
            else:
                print("Book is already borrowed.")
        else:
            print("Invalid patron or book ID.")

    elif choice == "6":
        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        user = None
        selected_book = None

        for p in lib.patrons:
            if p.patron_id == patron_id:
                user = p
                break

        for b in lib.books:
            if b.book_id == book_id:
                selected_book = b
                break

        if user and selected_book:
            if user.return_book(selected_book):
                print("Book returned successfully.")
            else:
                print("This patron did not borrow that book.")
        else:
            print("Invalid patron or book ID.")

    elif choice == "7":
        print("Thank you for using the Library System.")
        break

    else:
        print("Please enter a valid option.")
