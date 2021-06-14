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
                                "see your reading list(r), or quit app(q)?\n") \
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
                print("Sorry. That was an invalid option.\n")

        print("Goodbye!")

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
            print("Reading list is currently empty.\n")
        else:
            print("Here is your current reading list: \n")
            for x in curr_reading_list:
                authors = ", ".join(curr_reading_list[x][1])
                print(str(x) + "- Title: " + curr_reading_list[x][0] +
                      ", Author(s): " + authors +
                      ", Publishing Company: " +
                      curr_reading_list[x][2] + "\n")

    def print_searched_books(self):
        curr_searched_books = self.get_searched_books()

        print("Here are the searched books: \n")
        for x in curr_searched_books:
            authors = ", ".join(curr_searched_books[x][1])
            print(str(x) + "- Title: " + curr_searched_books[x][0] +
                  ", Author(s): " + authors + ", Publishing Company: " +
                  curr_searched_books[x][2] + "\n")

    def search_books(self):
        """This method searches for books using the Google Books API"""

        searching_books = True
        api = "https://www.googleapis.com/books/v1/volumes?q="
        max_results = "&maxResults=5"

        print("\n")

        while searching_books:
            user_choice = input("Would you like to search by title(t), "
                                "author(a), or publishing company(p)? Or "
                                "would you like to cancel search(c)?\n") \
                .strip()

            if user_choice == "T" or user_choice == "t":
                search_term = "+intitle"

                book_to_search = input("Enter title to search for: ").strip()
                book_to_search = ' '.join(book_to_search.split())
                book_to_search = book_to_search.replace(" ", "+")

                resp = urlopen(api + book_to_search + search_term +
                               max_results)
                book_data = json.load(resp)

                for x in range(5):
                    book_title = book_data["items"][x]["volumeInfo"]\
                        .get('title')
                    book_author = book_data["items"][x]["volumeInfo"]\
                        .get('authors')
                    book_publisher = book_data["items"][x]["volumeInfo"]\
                        .get('publisher')

                    if book_title is None:
                        book_title = "-No Title-"
                    else:
                        book_title = book_data["items"][x]["volumeInfo"]["title"]

                    if book_author is None:
                        book_author = ["-No author-"]
                    else:
                        book_author = book_data["items"][x]["volumeInfo"]["authors"]

                    if book_publisher is None:
                        book_publisher = "-No Publisher-"
                    else:
                        book_publisher = book_data["items"][x]["volumeInfo"]['publisher']

                    book_information = [book_title, book_author,
                                        book_publisher]

                    self.searched_books[x + 1] = book_information

                self.print_searched_books()
                self.add_to_reading_list()
                searching_books = False

            elif user_choice == "A" or user_choice == "a":
                search_term = "+inauthor"

                author_to_search = input("Enter author to search for: ")\
                    .strip()
                author_to_search = ' '.join(author_to_search.split())
                author_to_search = author_to_search.replace(" ", "+")

                resp = urlopen(api + author_to_search + search_term +
                               max_results)
                book_data = json.load(resp)

                for x in range(5):
                    book_title = book_data["items"][x]["volumeInfo"] \
                        .get('title')
                    book_author = book_data["items"][x]["volumeInfo"] \
                        .get('authors')
                    book_publisher = book_data["items"][x]["volumeInfo"] \
                        .get('publisher')

                    if book_title is None:
                        book_title = "-No Title-"
                    else:
                        book_title = book_data["items"][x]["volumeInfo"]["title"]

                    if book_author is None:
                        book_author = ["-No author-"]
                    else:
                        book_author = book_data["items"][x]["volumeInfo"]["authors"]

                    if book_publisher is None:
                        book_publisher = "-No Publisher-"
                    else:
                        book_publisher = book_data["items"][x]["volumeInfo"]['publisher']

                    book_information = [book_title, book_author,
                                        book_publisher]

                    self.searched_books[x + 1] = book_information

                self.print_searched_books()
                self.add_to_reading_list()
                searching_books = False

            elif user_choice == "P" or user_choice == "p":
                print("Search by publishing company picked!")
            elif user_choice == "C" or user_choice == "c":
                print("Book search canceled.\n")
                searching_books = False
            else:
                print("Sorry. That was an invalid option.\n")

    def add_to_reading_list(self):
        """This method adds books the user chooses to the reading list"""
        # TODO
        print("Perform add books to reading list!\n")


if __name__ == '__main__':
    my_app = BookApp()
    my_app.start_app()
