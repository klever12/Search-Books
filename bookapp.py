from termcolor import colored
from performbooksearch import search_books
from performaddreadinglist import add_to_reading_list
from printlists import print_reading_list


class BookApp:
    """The BookApp object contains the implementation of the command-line
    application and is used to start the app."""

    def __init__(self):
        self.app_quit = False
        self.reading_list = {}
        self.searched_books = {}

    def start_app(self):
        """This method starts the application"""

        print(colored("Welcome to my book search app! \n", 'red'))

        # Starts the application
        while self.app_quit is not True:
            user_choice = input(
                colored("Would you like to search for a book(b), "
                        "see your reading list(r), or quit app(q)?\n", 'red')) \
                .strip()

            if user_choice == "B" or user_choice == "b":
                # calls handle_book_search method to search for books and
                # handle_add_to_reading_list method to add to local reading
                # list
                self.handle_book_search()
                if self.get_searched_books() != {}:
                    self.handle_add_reading_list()

            elif user_choice == "R" or user_choice == "r":
                # calls print_reading_list function
                print_reading_list(self.get_reading_list())

            elif user_choice == "Q" or user_choice == "q":
                # sets self.app_quit to True to exit while loop and quit app
                self.app_quit = True

            else:
                print(colored("Sorry. That was an invalid option.\n", 'red'))

        print(colored("Goodbye!", 'red'))

    def get_reading_list(self):
        """This method returns the reading list"""

        return self.reading_list

    def get_searched_books(self):
        """This method returns the searched books"""

        return self.searched_books

    def handle_book_search(self):
        """This method calls the book_search function in order to perform a
        book search"""
        self.searched_books = search_books()

    def handle_add_reading_list(self):
        """This method calls the add_to_reading_list function in order to add
        searched books to a local reading list"""
        curr_reading_list = self.get_reading_list()
        curr_searched_books = self.get_searched_books()
        reading_list = add_to_reading_list(curr_searched_books,
                                           curr_reading_list)
        if reading_list != "no":
            self.reading_list = reading_list


if __name__ == '__main__':
    my_app = BookApp()
    my_app.start_app()
