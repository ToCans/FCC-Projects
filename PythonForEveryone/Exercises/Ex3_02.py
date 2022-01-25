# Chatper 3
#Exercise 2
hours = input("Please enter the number of hours worked this week: ")
try:
    ihours = int(hours)
    rate = input("Please enter your hourly rate: ")
    irate = int(rate)
    if ihours > 40:
        ihours_extra = int(ihours - 40)
        pay = (float(40 * irate)) + (float(ihours_extra * irate) * 1.5)
    else:
        pay = (float(int(hours) * int(rate)))
    print("Pay for this week: ",pay)
except:
    print("Error, please enter numeric input.")

