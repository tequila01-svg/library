class Library:
    def __init__(self, name, list):
        self.bookList=list
        self.name=name
        self.lendDict={}
    
    
    def displayBooks(self):
        print(f"we have the following books available here: {self.name}")
        for book in self.bookList:
            print(book)