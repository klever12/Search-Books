import json
from urllib.request import urlopen
from urllib.error import URLError
from termcolor import colored


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
                # calls search_books method to search for books
                self.search_books()

            elif user_choice == "R" or user_choice == "r":
                # calls  print_reading_list method
                self.print_reading_list()

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

    def print_reading_list(self):
        """This method prints the user's reading list if it's not empty"""

        curr_reading_list = self.get_reading_list()

        if bool(curr_reading_list) is False:
            print(colored("Reading list is currently empty.\n", 'blue'))
        else:
            print(colored("Here is your current reading list: \n", 'blue'))
            for x in curr_reading_list:
                authors = ", ".join(curr_reading_list[x][1])
                print(colored(str(x) + "- Title: " + curr_reading_list[x][0] +
                              ", Author(s): " + authors +
                              ", Publishing Company: " +
                              curr_reading_list[x][2] + "\n", 'blue'))

    def print_searched_books(self):
        curr_searched_books = self.get_searched_books()

        print(colored("Here are the searched books: \n", 'blue'))
        for x in curr_searched_books:
            authors = ", ".join(curr_searched_books[x][1])
            print(colored(str(x) + "- Title: " + curr_searched_books[x][0] +
                          ", Author(s): " + authors + ", Publishing Company: " +
                          curr_searched_books[x][2] + "\n", 'blue'))

    def search_books(self):
        """This method searches for books using the Google Books API"""

        searching_books = True
        api = "https://www.googleapis.com/books/v1/volumes?q="
        max_results = "&maxResults=5"

        print("\n")

        # start performing book search
        while searching_books:
            user_choice = input(
                colored("Would you like to search by title(t), "
                        "author(a), or publishing company(p)? Or "
                        "would you like to cancel search(c)?\n", 'red')) \
                .strip()

            # search by title
            if user_choice == "T" or user_choice == "t":
                search_term = "intitle:"

                book_to_search = input(colored("Enter title to search for: ",
                                               'red')).strip()
                book_to_search = ' '.join(book_to_search.split())
                book_to_search = book_to_search.replace(" ", "+")

                try:
                    resp = urlopen(api + search_term + book_to_search +
                                   max_results)
                except URLError:
                    print(colored("Sorry. No internet connection detected. "
                                  "Please check network connection and try "
                                  "again.\n", 'red'))
                    break

                book_data = json.load(resp)

                if book_data['totalItems'] == 0:
                    print(
                        colored("Sorry. No books were found with that title. ",
                                'red'))
                else:
                    if book_data['totalItems'] < 5:
                        number_books_found = book_data['totalItems']
                        self.searched_books = {}
                    else:
                        number_books_found = 5

                    for x in range(number_books_found):
                        book_title = book_data["items"][x]["volumeInfo"] \
                            .get('title')
                        book_author = book_data["items"][x]["volumeInfo"] \
                            .get('authors')
                        book_publisher = book_data["items"][x]["volumeInfo"] \
                            .get('publisher')

                        if book_title is None:
                            book_title = "-No Title-"
                        else:
                            book_title = book_data["items"][x]["volumeInfo"][
                                "title"]

                        if book_author is None:
                            book_author = ["-No author-"]
                        else:
                            book_author = book_data["items"][x]["volumeInfo"][
                                "authors"]

                        if book_publisher is None:
                            book_publisher = "-No Publisher-"
                        else:
                            book_publisher = \
                                book_data["items"][x]["volumeInfo"][
                                    'publisher']

                        book_information = [book_title, book_author,
                                            book_publisher]

                        self.searched_books[x + 1] = book_information

                    self.print_searched_books()
                    self.add_to_reading_list()
                    searching_books = False

            # search by author
            elif user_choice == "A" or user_choice == "a":
                search_term = "inauthor:"

                author_to_search = input(colored("Enter author to search for: "
                                                 , 'red')) \
                    .strip()
                author_to_search = ' '.join(author_to_search.split())
                author_to_search = author_to_search.replace(" ", "+")

                try:
                    resp = urlopen(api + search_term + author_to_search +
                                   max_results)
                except URLError:
                    print(colored("Sorry. No internet connection detected. "
                                  "Please check network connection and try "
                                  "again.\n", 'red'))
                    break

                book_data = json.load(resp)

                if book_data['totalItems'] == 0:
                    print(
                        colored("Sorry. No books were found with that title. ",
                                'red'))
                else:
                    if book_data['totalItems'] < 5:
                        number_books_found = book_data['totalItems']
                        self.searched_books = {}
                    else:
                        number_books_found = 5

                    for x in range(number_books_found):
                        book_title = book_data["items"][x]["volumeInfo"] \
                            .get('title')
                        book_author = book_data["items"][x]["volumeInfo"] \
                            .get('authors')
                        book_publisher = book_data["items"][x]["volumeInfo"] \
                            .get('publisher')

                        if book_title is None:
                            book_title = "-No Title-"
                        else:
                            book_title = book_data["items"][x]["volumeInfo"][
                                "title"]

                        if book_author is None:
                            book_author = ["-No author-"]
                        else:
                            book_author = book_data["items"][x]["volumeInfo"][
                                "authors"]

                        if book_publisher is None:
                            book_publisher = "-No Publisher-"
                        else:
                            book_publisher = \
                                book_data["items"][x]["volumeInfo"][
                                    'publisher']

                        book_information = [book_title, book_author,
                                            book_publisher]

                        self.searched_books[x + 1] = book_information

                    self.print_searched_books()
                    self.add_to_reading_list()
                    searching_books = False

            # search by publisher
            elif user_choice == "P" or user_choice == "p":
                search_term = "inpublisher:"

                publisher_to_search = input(
                    colored("Enter publisher to search for: ", 'red')) \
                    .strip()
                publisher_to_search = ' '.join(publisher_to_search.split())
                publisher_to_search = publisher_to_search.replace(" ", "+")

                try:
                    resp = urlopen(api + search_term + publisher_to_search +
                                   max_results)
                except URLError:
                    print(colored("Sorry. No internet connection detected. "
                                  "Please check network connection and try "
                                  "again.\n", 'red'))
                    break

                book_data = json.load(resp)

                if book_data['totalItems'] == 0:
                    print(
                        colored("Sorry. No books were found with that title. ",
                                'red'))
                else:
                    if book_data['totalItems'] < 5:
                        number_books_found = book_data['totalItems']
                        self.searched_books = {}
                    else:
                        number_books_found = 5

                    for x in range(number_books_found):
                        book_title = book_data["items"][x]["volumeInfo"] \
                            .get('title')
                        book_author = book_data["items"][x]["volumeInfo"] \
                            .get('authors')
                        book_publisher = book_data["items"][x]["volumeInfo"] \
                            .get('publisher')

                        if book_title is None:
                            book_title = "-No Title-"
                        else:
                            book_title = book_data["items"][x]["volumeInfo"][
                                "title"]

                        if book_author is None:
                            book_author = ["-No author-"]
                        else:
                            book_author = book_data["items"][x]["volumeInfo"][
                                "authors"]

                        if book_publisher is None:
                            book_publisher = "-No Publisher-"
                        else:
                            book_publisher = \
                                book_data["items"][x]["volumeInfo"][
                                    'publisher']

                        book_information = [book_title, book_author,
                                            book_publisher]

                        self.searched_books[x + 1] = book_information

                    self.print_searched_books()
                    self.add_to_reading_list()
                    searching_books = False

            # cancel book search
            elif user_choice == "C" or user_choice == "c":
                print(colored("Book search canceled.\n", 'red'))
                searching_books = False

            # user input was invalid
            else:
                print(colored("Sorry. That was an invalid option.\n", 'red'))

    def add_to_reading_list(self):
        """This method adds books the user chooses to the reading list"""

        wants_to_add_books = True

        # start by asking user if they'd like to add to reading list
        while wants_to_add_books:
            user_choice = input(
                colored("Would you like to add any of these books to"
                        " your reading list? \n Yes(y) or No(n): ", 'red')) \
                .strip()

            if user_choice == "Y" or user_choice == "y":
                adding_books = True

                # start add to reading list process
                while adding_books:
                    self.print_searched_books()
                    curr_searched_books = self.get_searched_books()
                    curr_reading_list = self.get_reading_list()
                    num_of_searched_books = len(curr_searched_books)

                    if bool(curr_reading_list) is False:
                        num_of_reading_list = 1
                    else:
                        num_of_reading_list = len(curr_reading_list) + 1

                    try:
                        print(
                            colored("Note: Duplicates will be removed", 'red'))
                        books_to_add = list(map(int,
                                                input(colored(
                                                    "Which books would you like"
                                                    " to add to your reading"
                                                    " list? Separated with space"
                                                    " if multiple, Enter "
                                                    "number "
                                                    "corresponding to book(s) in"
                                                    " list to add: ",
                                                    'red')).split()))

                    except ValueError:
                        print(colored(
                            "Sorry. Please enter numbers corresponding to"
                            " books in the list. \n", 'red'))
                        self.print_searched_books()
                        break

                    books_to_add = list(set(books_to_add))

                    for num in books_to_add:
                        if 1 <= num <= num_of_searched_books:
                            pass
                        else:
                            print(colored(
                                "Sorry. Number(s) input is not one of the"
                                " options in list.", 'red'))
                            books_to_add = False
                            break

                    if books_to_add is False:
                        break
                    else:
                        for book in books_to_add:
                            self.reading_list[num_of_reading_list] = \
                                curr_searched_books[book]
                            num_of_reading_list = num_of_reading_list + 1
                        self.print_reading_list()
                        adding_books = False
                        wants_to_add_books = False

            # user does not want to add to reading list
            elif user_choice == "N" or user_choice == "n":
                wants_to_add_books = False

            # user input was invalid
            else:
                print(colored("Sorry. That was an invalid option.\n", 'red'))
                self.print_searched_books()


if __name__ == '__main__':
    my_app = BookApp()
    my_app.start_app()
