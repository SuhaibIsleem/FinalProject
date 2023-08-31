class Book:
    id_counter = 0

    def __init__(self, title, author, level):
        Book.id_counter += 1
        self.book_id = Book.id_counter
        self.title = title
        self.author = author
        self.level = level
        self.is_available = "Available"

class Member:
    id_counter = 0

    def __init__(self, name, email, level):
        Member.id_counter += 1
        self.member_id = Member.id_counter
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []

    # TODO : implement member method
    def borrow_book(self, book):
        if book.is_available == "Available" and member.level == book.level:
            self.borrowed_books.append(book)
            book.is_available = "Not Available"
            print(f"{member.name} has borrowed the book:{book.title}")
        else:
            print("This book is not suitable.")


    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = "Available"
            print(f"{member.name} has returned the book:{book.title}")
        else:
            print("Book return is not possible.")

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # TODO : implement Library methods
    def add_book(self, book):
      return  self.books.append(book)

    def add_member(self, member):
       return self.members.append(member)


    def display_books(self):
        print("Books in the library:")
        print("ID\t|\tTitle\t|\tAuthor\t|\tLevel\t|\t Status")
        for book in self.books:
                print(
                    f"{book.book_id}\t|\t{book.title}\t|\t{book.author}\t|\t{book.level}\t|\t{book.is_available}")
        print("-" * 50)


    def find_book(self, book_id):

           for book in self.books:
               if book.book_id == book_id:
                    return  book

    def display_members(self):
        print("Members in the library:")
        print("ID\t|\tName\t|\tEmail\t|\tLevel\t")
        for member in self.members:
            print(f"{member.member_id}\t|\t{member.name}\t|\t{member.email}\t|\t{member.level}")
        print("-" * 50)

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return  member


    def edit_member(self):
        member = self.find_member(member_id)

        if member is None:
            print("Member not found.")
        else:
            print("---- Edit Member ----")
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            level = input("Enter new level: ")
            level = level.capitalize()
            member.name = name
            member.email = email
            member.level = level
            print("Member information updated successfully.")
        print("-" * 50)

    def delete_member(self, member_id):
        member = self.find_member(member_id)

        if member is None:
            print("Member not found.")
        else:
            self.members.remove(member)
            print("Member deleted successfully.")
        print("-" * 50)


library = Library()

print(' Welcome to the Library System '.center(100,'-'))
while True:
    print("1. Add Member")
    print("2. Edit Member")
    print("3. Show Members")
    print("4. Delete Member")
    print("5. Add Book")
    print("6. Show Books")
    print("7. Borrow Book")
    print("8. Return Book")
    print("9. Exit")
    choice = int(input("Enter your choice: "))
# TODO : implement the menu
    if choice == 1 :
        name = input("* Enter member name: ")
        email = input("* Enter member email: ")
        level = input("* Enter member level (A/B/C): ")
        level = level.capitalize()
        if level == "A" or level == "B" or level  == "C":
            library.add_member(Member(name,email,level))
            print("Member added successfully")
            print("-" * 50)
        else:
            print("Level is not available!")
            new_level = input("* Enter book level (A/B/C): ")
            new_level = new_level.capitalize()
            library.add_member(Member(name, email, new_level))


    elif choice == 2 :
        member_id = int(input("Enter member ID: "))
        print(library.edit_member())
    elif choice == 3:
        print(library.display_members())

    elif choice == 4 :
        member_id = int(input("Enter member ID: "))
        library.delete_member(member_id)

    elif choice == 5 :
        title = input("* Enter book title: ")
        author = input("* Enter book author: ")
        level = input("* Enter book level (A/B/C): ")
        level = level.capitalize()
        if level == "A" or level == "B" or level  == "C":
            library.add_book(Book(title, author, level))
            print("Book added successfully")
            print("-" * 50)
        else:
            print("Level is not available!")
            new_level = input("* Enter book level (A/B/C): ")
            new_level = new_level.capitalize()
            library.add_book(Book(title, author, new_level))
    elif choice == 6 :
        print(library.display_books())

    elif choice == 7 :

        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
        member = library.find_member(member_id)
        book = library.find_book(book_id)
        if book and member :
            member.borrow_book(book)
        else:
            print("not found")

    elif choice == 8 :
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
        # member = library.find_member(member_id)
        book = library.find_book(book_id)
        if member and book :
            member.return_book(book)
    elif choice == 9 :
        print("~ Thanks You ~")
        break
    else :
        print("Invalid Value !")
        print("Please choose again")

