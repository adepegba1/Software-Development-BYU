"""
Have your program open the file, read through it line by line, 
strip off leading and trailing whitespace and display each book to the screen.
"""
with open("books.txt") as mormon_book:
    for book in mormon_book:
        book = book.strip()
        print(book)