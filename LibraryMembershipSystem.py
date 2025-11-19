from datetime import datetime


class LibraryMember:
    def __init__(self, member_id, name, membership_start_date):
        self.__member_id = member_id
        self.__name = name
        self.__books_borrowed = []
        self.__membership_start_date = membership_start_date
        self.__last_accessed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Getters
    def get_member_id(self):
        return self.__member_id

    def get_name(self):
        return self.__name

    def get_books_borrowed(self):
        # return a copy to prevent direct modification
        return self.__books_borrowed.copy()

    def get_membership_start_date(self):
        return self.__membership_start_date

    def get_last_accessed(self):
        return self.__last_accessed

    # Setters
    def set_name(self, new_name):
        self.__name = new_name
        self.update_last_accessed()

    # Methods
    def borrow_book(self, book_title):
        self.__books_borrowed.append(book_title)
        print(f'"{book_title}" has been borrowed by {self.__name}.')
        self.update_last_accessed()

    def return_book(self, book_title):
        if book_title in self.__books_borrowed:
            self.__books_borrowed.remove(book_title)
            print(f'"{book_title}" has been returned by {self.__name}.')
        else:
            print(f'"{book_title}" is not in the list of borrowed books.')
        self.update_last_accessed()

    def list_borrowed_books(self):
        self.update_last_accessed()

        if not self.__books_borrowed:
            print(f"{self.__name} has not borrowed any books.")
        else:
            print(f"Books borrowed by {self.__name}:")
            for book in self.__books_borrowed:
                print(f"- {book}")

    def update_last_accessed(self):
        self.__last_accessed = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Testing/Menu
def main():
    member = LibraryMember(
        member_id=1,
        name="Jack",
        membership_start_date="2025-01-01"
    )

    while True:
        print("\n=== Library Menu ===")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. List Borrowed Books")
        print("4. View Member Info")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            book = input("Enter the book title to borrow: ")
            member.borrow_book(book)

        elif choice == "2":
            book = input("Enter the book title to return: ")
            member.return_book(book)

        elif choice == "3":
            member.list_borrowed_books()

        elif choice == "4":
            print(f"\nMember ID: {member.get_member_id()}")
            print(f"Name: {member.get_name()}")
            print(f"Membership Start Date: {member.get_membership_start_date()}")
            print(f"Last Accessed: {member.get_last_accessed()}")

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()