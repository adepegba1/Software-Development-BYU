# import the random method for this program
import random


word = ["Red", "Green", "Yellow", "Black", "Blue", "Purple", "Dark", "Grey"]
def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    # Call the append_random_numbers function to
    # add one random number to the numbers list.
    append_random_number(numbers)
    print(numbers)
    # Call the append_random_numbers function to
    # add three random number to the numbers list.
    append_random_number(numbers, 3)
    print(numbers)

    # Create a list to store random words.
    word_list = []
    print()
    # Call the append_random_words function
    # to add one random word to the list.
    print(word_list)
    append_random_word(word_list)
    # Call the append_random_words function
    # to add three random word to the list.
    print(word_list)
    append_random_word(word_list, 3)
    print(word_list)

def append_random_word(word_list, quantity=1):
    """
    Append quantity randomly chosen words onto the words list.
        Parameters
            words_list: A list of words where this function will
                append random words.
            quantity: The number of random words that this function
                will append onto words_list.
    Return: nothing. It's unnecessary for this function to return
        anything because this function changes the words_list.
    """
    for _ in range(quantity):
        w_list = random.choice(word)
        word_list.append(w_list)


def append_random_number(numbers_list, quantity = 1):     
     """
        Append quantity random numbers onto the numbers list.
        The random numbers are between 0 and 100, inclusive.
        Parameters
            numbers_list: A list of numbers where this function will
                append random numbers.
            quantity: The number of random numbers that this function
                will append onto numbers_list.
        Return: nothing. It's unnecessary for this function to return
            anything because this function changes the numbers_list.
    """
     for _ in range(quantity):
         num = random.uniform(0,100)
         num = round(num)
         numbers_list.append(num)

if __name__ == "__main__":
    main()