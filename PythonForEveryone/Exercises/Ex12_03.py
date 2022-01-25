import urllib.request
count = 0

fhand = urllib.request.urlopen('http://data.pr4e.org/intro.txt')
for line in fhand:
    count = count+ len(line)
    if count < 3001:
        print(line.decode().strip())

print("\nThe total number of characters: " + str(count))