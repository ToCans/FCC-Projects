# Chatper 4
# Exercise 7

score = input("Enter score: ")

def computegrade(grade):
    try:
        f_grade = float(grade)
        if f_grade >= 0.9 and f_grade <= 1:
            print("A")
        elif f_grade >= 0.8 and _grade < 0.9:
            print("B")
        elif f_grade >= 0.7 and _grade < 0.8:
            print("C")
        elif f_grade >= 0.6 and _grade < 0.7:
            print("D")
        elif f_grade < 0.6 and f_grade >= 0:
            print("F")
    except:
        print("Bad score.")

computegrade(score)