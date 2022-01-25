# Chapter 6
# Exercise 5

str = "X-DSPAM-Confidence: 0.8475"
start_pos = str.find(":")
num = str[start_pos + 2 :]
num = float(num)
print(num)