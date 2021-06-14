import json
from urllib.request import urlopen


class BookApp:
    """The BookApp object contains the implementation of the command-line
    application and is used to start the app."""

    def __init__(self):
        self.app_quit = False
        self.reading_list = {}
        self.searched_books = {}

    def start_app(self):
        """This method starts the application"""
        # TODO
        print("App started!")

    def get_reading_list(self):
        """This method returns the reading list"""

        return self.reading_list

    def get_searched_books(self):
        """This method returns the searched books"""

        return self.searched_books

    def search_books(self):
        """This method searches for books using the Google Books API"""
        # TODO
        print("Performed book search!")

    def add_to_reading_list(self):
        """This method adds books the user chooses to the reading list"""
        # TODO
        print("Added books to reading list!")


if __name__ == '__main__':
    my_app = BookApp()
    my_app.start_app()
