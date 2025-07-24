"""

"""
grade = int(input("Enter your grade: "))
if grade >= 70:
    if grade >= 90:
        if grade % 10 < 3:
            print("A-")
        else:
            print("A")
    elif grade >= 80:
        if grade % 10 >= 7:
            print("B+")
        elif grade % 10 < 3:
            print("B-")
        else:
            print("B")
    else:
        if grade % 10 >= 7:
            print("C+")
        elif grade % 10 < 3:
            print("C-")
        else:
            print("C")
    print(f"You pass the course with {grade}%")
elif grade >= 60:
    if grade % 10 >= 7:
        print("D+")
    elif grade % 10 < 3:
        print("D-")
    else:
        print("D")
else:
    print("F")
