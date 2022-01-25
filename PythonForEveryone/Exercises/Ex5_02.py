# Exercise 5.9
# Exercise 2

total = 0
count = 0
user_input = None
lowest = None
largest = None

while user_input != "done":
    user_input = input("Please enter a number: ")
    try:
        user_input = int(user_input)
        total = total + user_input
        count = count + 1 
        if lowest is None or user_input < lowest:
            lowest = user_input
        if largest is None or user_input > largest:
            largest = user_input
    except:
        if user_input == "done":
            print(total,count,largest,lowest)
        else:
            print("Invalid input.")