# Chapter 5
# Exercise 1

total = 0
count = 0
user_input = None

while user_input != "done":
    user_input = input("Please enter a number: ")
    try:
        user_input = int(user_input)
        total = total + user_input
        count = count + 1 
        average = total/count 
    except:
        if user_input == "done":
            print(total,count,average)
        else:
            print("Invalid input.")
            