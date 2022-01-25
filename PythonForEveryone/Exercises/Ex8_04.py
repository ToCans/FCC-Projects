# Chapter 8
# Exercise 4

file_open = open("romeo.txt")
new_list = []

for line in file_open:
    word = line.split()
    for i in word:
        if i not in new_list:
            new_list.append(i)
print(new_list)

