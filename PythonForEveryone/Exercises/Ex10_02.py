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
			if ':' in word:
				time = word.split(":")
				if time[0] not in counts:
					counts[time[0]]=1
				else:
					counts[time[0]]+=1



lst = list()
for time, count in list(counts.items()):
	lst.append((time,count))

lst.sort(reverse=False)

for time,count in lst:
	print(time,count)
