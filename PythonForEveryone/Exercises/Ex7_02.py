# Chapter 7
# Exercise 2
def average_mboxshort():
    file = open("mbox-short.txt")
    line_count = 0
    counter = 0

    for line in file:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence: "):
            line = float(line.lstrip("X-DSPAM-Confidence: "))
            line_count = line_count + line
            counter = counter + 1

    average1 = line_count / counter
    return average1


def average_mboxlong():
    file = open("mbox.txt")
    line_count = 0
    counter = 0

    for line in file:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence: "):
            line = float(line.lstrip("X-DSPAM-Confidence: "))
            line_count = line_count + line
            counter = counter + 1

    average2 = line_count / counter
    return average2


ave_long = average_mboxlong()
ave_short = average_mboxshort()
print("Average spam counter: ", round(ave_long, 5))
print("Average spam counter: ", round(ave_short, 5))