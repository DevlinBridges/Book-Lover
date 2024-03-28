import pandas as pd

class BookLover():
    '''Allows users to track books they've read and their ratings'''

    def __init__(self, name, email, fav_genre,  num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, book_rating):
        if not isinstance(book_rating, int) or book_rating < 0 or book_rating > 5:
            print("Please input an integer rating between 0 and 5.")
        if self.book_list.empty or book_name not in self.book_list['book_name'].values:
                new_book = pd.DataFrame({'book_name': [book_name],
                                         'book_rating': [book_rating]})
                self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
                return
        else:
            print("Book has already been added!")

    def has_read(self, book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False

    def num_books_read(self):
        return self.book_list['book_name'].count()

    def fav_books(self):
        favorites = self.book_list[self.book_list['book_rating'] > 3]
        print(favorites)
        return self.book_list[self.book_list['book_rating'] > 3]