class Library:
    bookList = ['Chronicles of Narnia', 
    'Sherlock Holmes', 'Harry Potter', 
    "The Handmaid's Tale", 'To kill a Mocking Bird'
    ]

    def __init__(self, name):
        self.name = name
        self.lendDict = {}

    def display_book(self):
        for i in range(len(self.bookList)):
            print(i+1, self.bookList[i])

    def lend_book(self, book, user):
        

    def add_book(self, book):
        pass

    def return_book(self, user):
        pass


