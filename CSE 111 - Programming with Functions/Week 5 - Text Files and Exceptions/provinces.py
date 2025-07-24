"""
Write a Python program named provinces.py that reads the contents
of provinces.txt into a list and then modifies the list.
"""

def main():
    """
    Read the contents of a text file named
    provinces.txt into a list named provinces_list.
    """

    provinces_list = read_list("provinces.txt")

    # As a debugging aid, print the entire list.
    print(provinces_list)

    # Remove the first element from the list.
    provinces_list.pop(0)

    # Remove the last element from the list.
    provinces_list.pop()
    
     # Replace all occurrrences of "AB" with "Alberta".
    for line in range(len(provinces_list)):
        if provinces_list[line] == "AB":
            provinces_list[line] = "Alberta"

    # Call the list.count method which will count the
    # number of times that Alberta appears in the list.
    count = provinces_list.count("Alberta")

    print()
    print(f"Alberta occurs {count} times in the modified list.")


def read_list(filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """   
    text_list = []

    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
        return text_list

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.    
if __name__ == "__main__":
    main()