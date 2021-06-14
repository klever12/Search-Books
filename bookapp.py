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

        print("Welcome to my book search app! \n")

        # Starts the application
        while self.app_quit is not True:
            user_choice = input("Would you like to search for a book(b), "
                                "see your reading list(r), or quit app(q)?\n")\
                .strip()

            if user_choice == "B" or user_choice == "b":
                # calls search_books method to search for books
                self.search_books()

            elif user_choice == "R" or user_choice == "r":
                # prints the user's reading list if not empty
                curr_reading_list = self.get_reading_list()

                if bool(curr_reading_list) is False:
                    print("Reading list is currently empty.\n")
                else:
                    print("Here is your current reading list: \n")
                    for x in curr_reading_list:
                        authors = ", ".join(curr_reading_list[x][1])
                        print(str(x) + " Title: " + curr_reading_list[x][0] +
                              ", Author(s): " + authors +
                              ", Publishing Company: " +
                              curr_reading_list[x][2] + "\n")

            elif user_choice == "Q" or user_choice == "q":
                # sets self.app_quit to True to exit while loop and quit app
                self.app_quit = True

            else:
                print("Sorry. That was an invalid option.\n")

        print("Goodbye!")

    def get_reading_list(self):
        """This method returns the reading list"""

        return self.reading_list

    def get_searched_books(self):
        """This method returns the searched books"""

        return self.searched_books

    def search_books(self):
        """This method searches for books using the Google Books API"""
        # TODO
        print("Performed book search!\n")

    def add_to_reading_list(self):
        """This method adds books the user chooses to the reading list"""
        # TODO
        print("Perform add books to reading list!\n")


if __name__ == '__main__':
    my_app = BookApp()
    my_app.start_app()
