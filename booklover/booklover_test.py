import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def setUp(self):
    # Initializing BookLover object with test data
        self.book_lover = BookLover(name='Devlin Bridges', email='cbv6gd@virginia.edu', fav_genre='Horror',
                                     book_list=pd.DataFrame({'book_name': ['Pet Semetary', 'The Sellout'],
                                                             'book_rating': [5, 4]}))
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        self.book_lover.add_book('New Book', 5)
        
        self.assertIn('New Book', self.book_lover.book_list['book_name'].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        self.book_lover.add_book("The Tommyknockers", 5)
        self.book_lover.add_book("The Tommyknockers", 5)
        
        self.assertEqual(len(self.book_lover.book_list[self.book_lover.book_list['book_name'] == 'The Tommyknockers']), 1)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        result = self.book_lover.has_read("The Sellout")
        
        self.assertTrue(result)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        result = self.book_lover.has_read("Crime and Punishment")
        
        self.assertFalse(result)
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        self.book_lover.add_book("A Confederacy of Dunces", 5)
        self.book_lover.add_book("The Power of the Dog", 5)
        self.book_lover.add_book("IT", 4)
        self.book_lover.add_book("The Memory Police", 4)

        ## set expected result: 2 books initially + 4 added = 6 total books
        exp_result = 6
        self.assertEqual(self.book_lover.num_books_read(), exp_result)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        self.book_lover.add_book("The Martian", 2)
        self.book_lover.add_book("Sirens of Titan", 5)
        self.book_lover.add_book("Harry Potter and the Sorcerer's Stone", 2)
        self.book_lover.add_book("Random Book", 1)
        self.book_lover.add_book("DS5100 Book", 5)

        ## assign favorite books to a variable and check that all instances have rating > 3
        fav_books = self.book_lover.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))

if __name__ == '__main__':
    
    unittest.main(verbosity=3)