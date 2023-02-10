class Book:
    def __init__(self, name, number, publish):
        self.name = name
        self.number = number
        self.publish = publish
    
    def save_book(self, name, number, publish):
        self.name = name
        self.number = number
        self.publish = publish
    
    def remove_all(self):
        self.name = ''
        self.number = ''
        self.publish = ''
    
    def __str__(self):
        return f'name: {self.name}, number:{self.number}, publish:{self.publish}'
    

class BookShelf:
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.cards = {}

    def save_book(self, book, page=0):
        if self.page_number < 500:
            if page == 0:
                self.books[self.page_number] = book
                self.page_number += 1
            else:
                self.books = {page:book}
                self.page_number += 1
        else:
            print('책이 모두 채워졌습니다.')
    def remove_all(self,page_number):
        if page_number in self.books.keys():
            return self.books.pop(page_number)
        else:
            print('해당 책은 존재하지 않습니다.')
    
    def get_number_of_books(self):
        return len(self.books.keys())
    
    def list_books(self, key = None, reverse = False):
        if key == None:
            for page in self. books:
                print(self.books[page])
        else:
            sorted_dict = sorted(self.books.items(), key= eval(f'lambda item:item[1].{key}'), reverse=reverse)
            for page, book in sorted_dict:
                print(book)