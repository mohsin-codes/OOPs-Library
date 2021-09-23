
class Library:
    bookList = ['Chronicles of Narnia', 
    'Sherlock Holmes', 'Harry Potter', 
    "The Handmaid's Tale", 'To kill a Mocking Bird'
    ]

    def __init__(self):
        pass

    def display_book(self):
        for i in range(len(self.bookList)):
            print(i+1, self.bookList[i])
        import main
        main.user.continue_game()
        

    def lend_book(self, book, user):
        pass

    def add_book(self, book):
        pass

    def return_book(self, user):
        pass


