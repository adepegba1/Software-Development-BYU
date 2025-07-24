import string

# Define character lists
LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SPECIAL = string.punctuation

def word_in_file(word, filename, case_sensitive=False):
    try:
        with open("toppasswords.txt", 'r') as file:
            words = file.split()
            if not case_sensitive:
                word = word.lower()
                words = [w.lower() for w in words]
            return word in words
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return False

def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    dictionary_filename = "wordlist.txt"
    toppasswords_filename = "toppasswords.txt"

    if word_in_file(password, dictionary_filename):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, toppasswords_filename, case_sensitive=True):
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

def main():
    while True:
        password = input("Enter a password to test (or 'q' to quit): ")
        if password.lower() == 'q':
            break
        strength = password_strength(password)
        print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()