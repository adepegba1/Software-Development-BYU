"""
The password checker should allow users to check passwords until they choose 
to quit. The hope is that by using the password checker tool employees 
will learn how to create better passwords.

Passwords should be checked against both a list of known passwords and a list of 
dictionary of words. María has provided both a dictionary file that contains about
70,000 words and a file that contains the top 1 million passwords used.

The tool will allow a user to enter a password, the tool will calculate the 
strength of the password (from 0 to 5), a message should be shown to inform 
the user the strength of the password.

María would like the strength calculator created as a function so it can be 
used in other future projects.

A password’s strength is calculated based on several factors including, 
is the password a dictionary word, is the password a known password, the length of 
the password and the complexity of the password. Here are the requirements:

    If the password is in the dictionary file. (this should be a case insensitive match)
        Print the message. "'Password is a dictionary word and is not secure."
        Return a strength value of 0.

    If the password is in the toppassword list.(this should be a case sensitive match)
        Print the message "Password is a commonly used password and is not secure."
        Return a strength value of 0

    If the password is shorter than the minimum password length of 10
        Print the message "Password is too short and is not secure."
        Return a strength value of 1

    If the password is longer than 15 characters, the password is strong
        Print the message "Password is long, length trumps complexity this is a good password."
        Return the strength value of 5
    
    For the remainder of the cases the strength will be determined by the complexity 
    of the password. Passwords are more difficult to crack if they contain multiple 
    kinds of characters. 
    For this program there are 4 kinds of characters, upper case letters, lower case 
    letters, numeric digits, and special symbols. The complexity score is a number 
    from 1 to 4 that indicates how many of the different types of characters are 
    used in the password. 
    E.g. if the password only had upper case characters it would have a complexity 
    score of 1, if it had upper and lower case characters, it would have a complexity 
    score of 2, etc.
        The strength score will be calculated as a base score of 1 plus the complexity 
    score.
        Return the strength score.
"""

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]


def main():
     """
        Provides the user input loop. The loop asks the user for a password to test. 
        If that password is anything but "q" or "Q" call the password_strength function and 
        report the results to the user. If the user enters "q" or "Q", quit the program.
     """
     password = input("Enter a password to test (or 'q' to quit): ")
     while password.lower() != 'q':        
        strength = password_strength(password)
        print(f"Password strength: {strength}")
        password = input("Enter a password to test (or 'q' to quit): ")
    

def word_in_file(word, filename, case_sensitive = False):
    """
        This function reads a file (specified by the filename parameter) in which each line of the 
        file contains a single word. If the word passed in the word parameter matches a word in 
        the file the function returns a true otherwise it returns a false. If the parameter 
        case_sensitive is true a case sensitive match is performed. If case_sensitive is false a 
        case insensitive match is performed. The case_sensitive parameter should default to False
    """
    list_word = []
    with open(filename, "r", encoding="utf=8") as files:
        for i in files:
            list_word.append(i.strip())
        if case_sensitive == False:
            word = word.lower()
            list_word = [w.lower() for w in list_word]
            return word in list_word
        else:
            return word in list_word


def word_has_character(word, character_list):
    """
        This function loops through each character in the string passed in the word parameter to 
        see if that character is in the list of characters passed in the character_list parameter. 
        If any of the characters in the word are present in the character list return a true, 
        If none of the characters in the word are in the character list return false
    """
    for char in word:
        if char in character_list:
            return True
    return False
    
    

def word_complexity(word):
    """
        This function creates a numeric complexity value based on the types of characters 
        the word parameter contains. One point of complexity is given for each type of character 
        in the word. The function calls the word_has_character function for each of the 4 kinds 
        of characters (LOWER, UPPER, DIGITS, SPECIAL). If the word has that kind of character a 
        point is added to complexity rating. Since there are 4 kinds of characters the complexity 
        rating will range from 0 to 4. (0 would be returned only if word contained no characters or 
        only contains characters that are not in any of the lists.)
    """

    complexity = 0
    if word_has_character(word,LOWER):
        complexity += 1
    if word_has_character(word,UPPER):
        complexity += 1
    if word_has_character(word,DIGITS):
        complexity += 1
    if word_has_character(word,SPECIAL):
        complexity += 1
    return complexity


def password_strength(password, min_length = 10, strong_length = 16):
    """
        This function checks length requirements, calls word_complexity to calculate the words 
        complexity then determines the password's strength based on the user requirements. It should'
        ' print the messages defined in the requirements and return the password's strength as a 
        number from 0 to 5. The min_length parameter should have a default value of 10. 
        The strong_length parameter should have a default value of 16
    """
    dictionary_filename = "wordlist.txt"
    top_password_filename = "toppasswords.txt"

    if word_in_file(password, dictionary_filename):
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(password, top_password_filename, case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength

    
if __name__ == "__main__":
    main()
