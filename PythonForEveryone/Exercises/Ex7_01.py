# Chapter 7
# Exercise 1

file = open("mbox-short.txt")
for line in file:
    line = line.rstrip()
    line = line.upper()
    print(line)