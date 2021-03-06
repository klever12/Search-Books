# Search-Books

This command-line application allows users to search for books using the [Google Books API](https://developers.google.com/books). The user also has the option to add books to a local "Reading List."

Here are the key files in the project: 

- `bookapp.py` - used to implement the command-line application and start the app.
- `performbooksearch.py` - function used in the BookApp class that searches for books using the Google Books API
- `performaddreadinglist.py` - function used in the BookApp class that adds books the user chooses to the reading list
- `printlists.py` - functions used in order to print the searched books and reading list

## Project Setup 

In order to clone and run this repository, you will need to have Git, [Python 3.x](https://www.python.org/download/releases/3.0/), and the [Python termcolor module](https://pypi.org/project/termcolor/). Then in the command line, you can do:  


```bash
# Clone this repository
git clone https://github.com/klever12/Search-Books
# Go into the repository
cd Search-Books
# install the termcolor module using pip
pip install termcolor
# Run the bookapp.py script
python3 bookapp.py
```

Alternatively, one can run the scripts using an IDE through the IDE's *Run* or *Build* command. 
