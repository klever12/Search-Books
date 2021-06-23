import unittest
from performbooksearch import search_books
from performaddreadinglist import add_to_reading_list
from bookapp import BookApp
from printlists import print_searched_books, print_reading_list


class AppTest(unittest.TestCase):

    def test_print_empty_reading_list(self):
        self.assertEqual(print_reading_list({}), None)

    def test_print_reading_list(self):
        self.assertEqual((print_reading_list({1: ["book", ["author"], "publish"]}), "Here is your current reading list: \n" + "1- Title: title, Author(s): author, Publishing Company: publish"))

    def test_print_searched_books(self):
        self.assertEqual(print_searched_books({1: ["book", ["author"], "publish"]}), "Here are the searched books: \n" + "1- Title: title, Author(s): author, Publishing Company: publish")


if __name__ == '__main__':
    unittest.main()
