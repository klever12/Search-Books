from termcolor import colored
from printlists import print_searched_books, print_reading_list


def add_to_reading_list(searched_books, reading_list):
    """This function adds books the user chooses to the reading list"""

    wants_to_add_books = True
    curr_searched_books = searched_books
    curr_reading_list = reading_list

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
                print_searched_books(curr_searched_books)
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
                    print_searched_books(searched_books)
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
                        curr_reading_list[num_of_reading_list] = \
                            curr_searched_books[book]
                        num_of_reading_list = num_of_reading_list + 1
                    print_reading_list(curr_reading_list)
                    return curr_reading_list

        # user does not want to add to reading list
        elif user_choice == "N" or user_choice == "n":
            return "No"

        # user input was invalid
        else:
            print(colored("Sorry. That was an invalid option.\n", 'red'))
            print_searched_books(searched_books)
