from booklover import BookLover

booktest = BookLover('Devlin Bridges', 'cbv6gd@virginia.edu', 'Horror')
booktest.add_book('The Shining', 5)
print(booktest.num_books_read())