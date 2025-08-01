import csv
from datetime import datetime, date

def read_dictionary(filename, key_column_index):
    """
        This function reads the product data from the csv file passed to the function in the 
        filename parameter. The dictionary key is contained in the csv data column indicated 
        by the key_column_index parameter, the value of each dictionary item is the list 
        derived from the values in the row of the csv file. Function returns a dictionary 
        of products.
        Parameters
            filename: the name of the CSV file to read.
            key_column_index: the index of the column
                to use as the keys in the dictionary.
        Return: a compound dictionary that contains
            the contents of the CSV file.
    """

    # Create an empty dictionary that will
    # store the data from the CSV file.
    product_dict = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as product_csv:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        csv_reader  = csv.reader(product_csv, delimiter=",")

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
            product_dict[key_value] = row

    # Return the dictionary.
    return product_dict

def main():
    """
    	Reads the receipt.csv file, processes the file and displays the receipt 
        according to the user requirements.
    """

    try:

        # Get the current date and time from your computer’s operating system
        time = datetime.now()

        # Format the datetime object into the desired string format
        # %a: Abbreviated weekday name (e.g., Wed)
        # %b: Abbreviated month name (e.g., Nov)
        # %d: Day of the month as a zero-padded decimal number (e.g., 04)
        # %H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 05)
        # %M: Minute as a zero-padded decimal number (e.g., 10)
        # %S: Second as a zero-padded decimal number (e.g., 30)
        # %Y: Year with century as a decimal number (e.g., 2020)
        formatted_date = time.strftime("%a %b %d %H:%M:%S %Y")
        #

        # New Years Sale begins start date
        end_date = date(2026, 1, 1)

        # Current date 
        start_date = datetime.date(time)

        # differences between the start date and new year date
        diff = end_date - start_date
        

        KEY_INDEX = 0
        PRODUCT_NAME_INDEX = 1
        PRICE_INDEX = 2
        QUANTITY_INDEX = 1
        TAX_RATE = 0.06
        total_quantity = 0
        subtotal = 0

        # Read the contents of a CSV file named products.csv
        # into a dictionary named products_dict.        
        products_dict = read_dictionary("products.csv", KEY_INDEX)

        # Ask the user for the name of the store
        store_name = input("What is the name of the store: ")

        # print the name of the store
        print(store_name)

        # open and read the content of a CSV file name request.csv
        with open("request.csv", "r", newline="") as request_csv:

            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            csv_reader = csv.reader(request_csv, delimiter=",")

            # The first row of the CSV file contains column
            # headings and not data, so this statement skips
            # the first row of the CSV file.
            next(csv_reader)

            # Read the content of a CSV file name request.csv
            # into a list name request_list
            request_list = list(csv_reader)

        # Read the content of the request_list
        for element in request_list:

            # For each element in position 0
            list_key = element[KEY_INDEX]

            # For each element in position 1
            quantity = int(element[QUANTITY_INDEX])

            # If element at position 0 in the list is also in the dictionary
            # if list_key in products_dict:

            # Get the key value from the dictionary
            key_value = products_dict[list_key] 

            # Retrieve the name from the key of the dictionary         
            name = key_value[PRODUCT_NAME_INDEX]

            # Retrieve the price and save it as a float number from the key of the dictionary
            price = float(key_value[PRICE_INDEX])

            # Add the quantity together
            total_quantity += quantity
            
            # Add the subtotal together
            subtotal += (quantity * price)
            # print the result for each order in the request_list
            print(f"{name}: {price} @ {quantity}")

        # Calculate the tax_sales
        Tax_sales = subtotal * TAX_RATE

        # Addition of the tax_sales with the subtotal
        Total = Tax_sales + subtotal
        print(f"Number of items: {total_quantity}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {Tax_sales:.2f}")
        print(f"Total: {Total}")
        print(f"Thank you for shopping at the {store_name}")
        print(formatted_date)
        print(f"New years sales remain {diff}")
    except FileNotFoundError as file_error:
        print(file_error)
    except PermissionError as per_error:
        print(per_error)
    except KeyError as key_error:
        print(f"Unkown product ID in the request.csv file {key_error}")


if __name__ == "__main__":
    main()