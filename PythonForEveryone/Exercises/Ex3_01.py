# Chatper 3
#Exercise 1
hours = input("Please enter the number of hours worked this week: ")
rate = input("Please enter your hourly rate: ")
hours = int(hours)
rate = int(rate)

if hours > 40:
    hours_extra = hours - 40
    pay = (float(40 * rate)) + (float(int(hours_extra) * rate * 1.5))
else:
    pay = (float(int(hours) * rate))
print("Pay for this week: ",pay,"\n")
