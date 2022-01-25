# Chapter 7
# Exercise 3

counter = 0

file_name = input("Enter the file name: ")
if file_name == "mbox.txt":
    file_open = open("mbox.txt")
    for line in file_open:
        counter = counter + 1
    print("There were", counter, "subject lines in", file_name)
elif file_name == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    print("File cannot be opened:", file_name)