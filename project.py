class Library:
    def __init__(self):
        self.books = []  # Initialize an empty list of books
        self.noBooks = 0  # Initialize the count of books to zero

    def addBook(self, book):
        self.books.append(book)  # Add the book to the list
        self.noBooks = len(self.books)  # Update the number of books

    def showInfo(self):
        # Display the list of books and the count
        print(f"The library has {self.books} books. The number of books is {self.noBooks}")

    def borrowBook(self, book):
        # If the book is available, remove it and decrease book count
        if book in self.books:
            self.books.remove(book)
            self.noBooks = len(self.books)
            print(f"You have borrowed '{book}'")
        else:
            print(f"The book '{book}' is not in the library.")

    def returnBook(self, book):
        self.books.append(book)  # Add the book back to the list
        self.noBooks = len(self.books)  # Update the number of books
        print(f"You have returned '{book}'")


# Example usage
l1 = Library()
l1.addBook("Harry Potter")
l1.addBook("The Silent Patient")
l1.addBook("The Fault In Our Stars")
l1.addBook("Ikigai")
l1.addBook("The Alchemist")
l1.showInfo()

# Returning a book after getting input from user
book_to_return = input("Enter the book you want to return: ")
l1.returnBook(book_to_return)
l1.showInfo()
