# Chatper 4
#Exercise 6

def computepay(hr,rt):
    #print("In Computepay:",hr,rt)
    if hr > 40:
        hours_extra = hr - 40
        pay = (float(40 * rt)) + (float(int(hours_extra) * rt * 1.5))
    else:
        pay = (float(int(hr) * rt))
    #print("Returning ", pay)
    return pay

hours = input("Please enter the number of hours worked this week: ")
rate = input("Please enter your hourly rate: ")
hours = int(hours)
rate = int(rate)

xp = computepay(hours, rate)
print("Pay for this week:", xp)