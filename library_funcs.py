
from typing import AsyncContextManager


class Library:
    bookList = ['Chronicles of Narnia', 
    'Sherlock Holmes', 'Harry Potter', 
    "The Handmaid's Tale", 'To kill a Mocking Bird'
    ]

    def __init__(self):
        self.lendBook = {}

    def display_book(self):
        for i in range(len(self.bookList)):
            print(i+1, self.bookList[i])
        import main
        main.user.continue_game()
        

    def lend_book(self, name):
        import main
        for i in range(len(self.bookList)):
            print(i+1, self.bookList[i])
        book_name = input("Enter name of the book that you want to lend? ")
        if book_name in self.lendBook:
            print("The book is already been taken.")
            main.user.continue_game()
        else:
            self.lendBook[book_name] = name
            print("User Database Updated. You can take the book now!")
            main.user.continue_game()

    def add_book(self, book):
        pass

    def return_book(self, user):
        pass


