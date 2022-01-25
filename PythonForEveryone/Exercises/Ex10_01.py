#Chapter 10
#Exercise 01

#Opening File
file = input("Enter file name: ")
try:
	fbox = open(file)
except:
	print("File cannot be opened: ", file)
	exit()

# Creating Dictionarily and looking for emails
counts = dict()
for line in fbox:
	words = line.split()
	for word in words:
		if words[0] != "From":
			continue
		else:
			if '@' in word:
				if word not in counts:
					counts[word]=1
				else:
					counts[word]+=1



lst = list()
for email, count in list(counts.items()):
	lst.append((email,count))

lst.sort(reverse=True)

for email,count in lst[:1]:
	print(email,count)