from termcolor import colored
import json
from urllib.request import urlopen
from urllib.error import URLError
from printlists import print_searched_books


def search_books():
    """This function searches for books using the Google Books API"""

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
                return {}

            book_data = json.load(resp)

            if book_data['totalItems'] == 0:
                print(
                    colored("Sorry. No books were found with that title. ",
                            'red'))
                return {}
            else:
                if book_data['totalItems'] < 5:
                    number_books_found = book_data['totalItems']
                    searched_books = {}
                else:
                    number_books_found = 5
                    searched_books = {}

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

                    searched_books[x + 1] = book_information

                print_searched_books(searched_books)
                return searched_books

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
                return {}

            book_data = json.load(resp)

            if book_data['totalItems'] == 0:
                print(
                    colored("Sorry. No books were found with that title. ",
                            'red'))
                return {}
            else:
                if book_data['totalItems'] < 5:
                    number_books_found = book_data['totalItems']
                    searched_books = {}
                else:
                    number_books_found = 5
                    searched_books = {}

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

                    searched_books[x + 1] = book_information

                print_searched_books(searched_books)
                return searched_books

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
                return {}

            book_data = json.load(resp)

            if book_data['totalItems'] == 0:
                print(
                    colored("Sorry. No books were found with that title. ",
                            'red'))
                return {}
            else:
                if book_data['totalItems'] < 5:
                    number_books_found = book_data['totalItems']
                    searched_books = {}
                else:
                    number_books_found = 5
                    searched_books = {}

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

                    searched_books[x + 1] = book_information

                print_searched_books(searched_books)
                return searched_books

        # cancel book search
        elif user_choice == "C" or user_choice == "c":
            print(colored("Book search canceled.\n", 'red'))
            return {}

        # user input was invalid
        else:
            print(colored("Sorry. That was an invalid option.\n", 'red'))
