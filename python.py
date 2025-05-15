
class person:
    def __init__(self, name, age, gender, person_id):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class member(person):
    def __init__(self, _member_id, _borrowed, name, age, gender):
        super().__init__(name, age, gender, _member_id)
        self._member_id = _member_id
        self._borrowed = []

    def borrow(self, code, library):
        if library.lend_book(code, self):
            print(f"{self.name} successfully borrowed the book.")
        else:
            print(f"{self.name} could not borrow the book.")

    def return_book(self, book, library):
        if book in self._borrowed:
            self._borrowed.remove(book)
            library.books.append(book)
            print(f"{self.name} returned {book}.")
        else:
            print(f"{self.name} did not borrow {book}.")

    def list_borrowed_books(self):
        if self._borrowed:
            return f"{self.name} has borrowed: {', '.join(self._borrowed)}"
        else:
            return f"{self.name} has not borrowed any books."

    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old, and I am a member with ID {self._member_id}."


class librarian(person):
    def __init__(self, _employee_id, name, age, gender):
        super().__init__(name, age, gender, _employee_id)
        self._employee_id = _employee_id

    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old, and I am a librarian with ID {self.person_id}."


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.__catalog = {}
        self.__available = set()

    def add_book(self, code: str, book: Book):
        self.__catalog[code] = book
        self.__available.add(code)

    def lend_book(self, code: str, member: member) -> bool:
        if code in self.__available:
            self.__available.remove(code)
            member._borrowed.append(self.__catalog[code].title)
            print(f"{member.name} borrowed {self.__catalog[code].title}.")
            return True
        else:
            print(f"The book with code {code} is not available.")
            return False

    def receive_book(self, book: Book):
        for code, b in self.__catalog.items():
            if b.title == book.title:
                self.__available.add(code)
                print(f"{book.title} has been returned to the library.")
                return
        print(f"{book.title} is not in the library's catalog.")

    def list_available_books(self):
        if self.__available:
            print("Available books:")
            for code in self.__available:
                book = self.__catalog[code]
                print(f"{code}: {book.title} by {book.author}")
        else:
            print("No books are currently available.")



librarian = librarian('employee_id=130', 'John', age=30, gender='male')
member = member('member_id=130', [], 'Lynn', 25, 'female')
book1 = Book('The Great Gatsby', 'F. Scott Fitzgerald')
book2 = Book('To Kill a Mockingbird', 'Harper Lee')

library = Library()
library.add_book('L002', book1)
library.add_book('C005', book2)


print(librarian.introduce())
print(member.introduce())
member.borrow('L002', library)
print(member.list_borrowed_books())
member.borrow('L002', library)
member.return_book('The Great Gatsby', library)
library.list_available_books()