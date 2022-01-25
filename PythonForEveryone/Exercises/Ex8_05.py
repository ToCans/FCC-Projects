# Chapter 8
# Exercise 5

file_to_open = input("Please enter a file to open: ")
file_open = open(file_to_open)
count = 0

for line in file_open:
    word = line.split()
    if len(word) == 0:
        continue
    if word[0] != "From":
        continue
    print(word[1])  
    count = count + 1   

print("\nThere were "+str(count)+" number of lines starting with 'From'.")
        
       


