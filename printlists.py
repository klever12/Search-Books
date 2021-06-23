from termcolor import colored


def print_reading_list(reading_list):
    """This function prints the user's reading list if it's not empty"""

    curr_reading_list = reading_list

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


def print_searched_books(searched_books_list):
    """This function prints the user's searched books"""
    curr_searched_books = searched_books_list

    print(colored("Here are the searched books: \n", 'blue'))
    for x in curr_searched_books:
        authors = ", ".join(curr_searched_books[x][1])
        print(colored(str(x) + "- Title: " + curr_searched_books[x][0] +
                      ", Author(s): " + authors + ", Publishing Company: " +
                      curr_searched_books[x][2] + "\n", 'blue'))
