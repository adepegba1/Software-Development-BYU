import csv
"""
A common task for many knowledge workers is to use a number, key,
or ID to look up information about a person. For example, a
knowledge worker may use a phone number or e-mail address as a key
to find (or look up) additional information about a customer.
During this activity, your team will write a Python program that
uses a student's I-Number to look up the student's name.
"""

def main():
    # The column headings and indexes.
    KEY_INDEX  = 0
    NAME_INDEX = 1

    # Read the contents of a CSV file named students.csv
    # into a dictionary named students_dict. Use the I-Number
    # as the key in the dictionary.
    students = read_dictionary("students.csv", KEY_INDEX)

    # Get an I-Number from the user.
    inumber = input("Please enter the student I-Number: ")

    # The I-Numbers are stored in the CSV file as digits only (without
    # any dashes), so we remove all dashes from the user's input.
    inumber = inumber.replace("-","")
    
    # Determine if the user input is formatted correctly.    
    if not inumber.isdigit():
        print(f"Invalid ID Number {inumber}")
    else:
        if len(inumber) < 9:
            print(f"Invalid ID Number {inumber}: too few digits")
        elif len(inumber) > 9:
            print(f"Invalid ID Number {inumber}: too many digits")
        else:
            # The user input is a valid I-Number. Find
            # the I-Number in the list of I-Numbers.
            if inumber in students:
                # Retrieve the student name that corresponds
                # to the I-Number that the user entered.
                student = students[inumber]
                name = student[NAME_INDEX]

                # Print the student name.
                print(f"The student with the I-number {inumber} is {name}")
            else:
                print("No such student")

def read_dictionary(filename, key_column_index):
    """
        Read the contents of a CSV file into a compound
        dictionary and return the dictionary.

        Parameters
            filename: the name of the CSV file to read.
            key_column_index: the index of the column
                to use as the keys in the dictionary.
        Return: a compound dictionary that contains
            the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    s_dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        csv_reader = csv.reader(csv_file, delimiter=",")

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(csv_reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row in csv_reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            key_value = row[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            s_dictionary[key_value] = row

    # Return the dictionary.
    return s_dictionary

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()