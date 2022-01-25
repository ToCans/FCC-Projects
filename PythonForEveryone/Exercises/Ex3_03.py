# Chatper 3
#Exercise 3

grade = input("Enter score: ")
try:
    f_grade = float(grade)
    if f_grade >= 0.9 and f_grade <= 1:
        print("A")
    elif f_grade >= 0.8:
        print("B")
    elif f_grade >= 0.7:
        print("C")
    elif f_grade >= 0.6:
        print("D")
    elif f_grade < 0.6 and f_grade >= 0:
        print("F")
except:
    print("Bad score.")
