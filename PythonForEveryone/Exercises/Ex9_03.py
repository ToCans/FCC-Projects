#Chapter 9
#Exercise 3

file = input("Enter file name: ")
try:
	fbox = open(file)
except:
	print("File cannot be opened: ", file)
	exit()

num = dict()
for line in fbox:
	words = line.split()
	for word in words:
		if '@' in word:
			num[word] = num.get(word,0)+1
			print(word.strip('<>;'),num[word])