
class Library:
    bookList = ['Chronicles of Narnia', 
    'Sherlock Holmes', 'Harry Potter', 
    "The Handmaid's Tale", 'To kill a Mocking Bird'
    ]

    def __init__(self):
        self.lendBook = {}

    def display_book(self, name):
        for i in range(len(self.bookList)):
            print(i+1, self.bookList[i])
        import main
        main.user.continue_game(name)
        

    def lend_book(self, name):
        import main
        for i in range(len(self.bookList)):
            print(i+1, self.bookList[i])
        book_name = input("Enter name of the book that you want to lend? ")
        if book_name in self.lendBook:
            print("The book is already been taken.")
            main.user.continue_game(name)
        else:
            
            self.lendBook[book_name] = name
            print("User Database Updated. You can take the book now!")
            main.user.continue_game(name)

    def add_book(self, book, name):
        self.bookList.append(book)
        print(f"Thanks for adding the book to the Library {self.name}")

    def return_book(self, book, name):
        popped_book = self.lendBook.pop(book)
        self.bookList.append(popped_book)
        print(f"{popped_book} is returned by {self.name}")


