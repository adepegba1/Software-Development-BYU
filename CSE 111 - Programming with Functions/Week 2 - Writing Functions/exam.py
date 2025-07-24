password = input("Enter the password: ")
i = lower = upper = special = digit = nothing = 0
top_passwords_list = []
dictionary_list = []
index_dictionary = 0
index_word = 0
with open("toppasswords.txt", "r", encoding="utf-8") as top_passwords:
    for top_word in top_passwords:        
        top_passwords_list.append(top_word.strip())
    while index_dictionary < len(top_passwords_list):
        if password == top_passwords_list[index_dictionary]:
            print("Password is a commonly used password and is not secure.")
        index_dictionary += 1

with open("wordlist.txt", "r", encoding="utf-8") as dictionary_words:
    for dict_word in dictionary_words:       
        dictionary_list.append(dict_word.strip())
    while index_word < len(dictionary_list):
        if password.lower() == dictionary_list[index_word].lower():
            print("Password is a dictionary word and is not secure.")
        index_word += 1

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]
while i < len(password):
    if password[i] in LOWER:
        lower = 1
    elif password[i] in UPPER:
        upper = 1
    elif password[i] in DIGITS:
        digit = 1
    elif password[i] in SPECIAL:
        special = 1
    else:
        nothing = 0
    i += 1

print(lower+ upper+ digit+ special)

length_of_password = len(password)
if length_of_password <= 10:
    print("0")
else:
    print("1")
