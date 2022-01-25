# Chapter 12 
# Exercise 1

import socket

try:
	url = input("Please enter the url:")
	host = url.split('/')[2]
	count = 0


	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect((host, 80))
	cmd = 'GET '+ url +' HTTP/1.0\r\n\r\n'
	cmd = cmd.encode()
	mysock.send(cmd)

	while True:
		data = mysock.recv(512)
		count = count + len(data)
		if len(data) < 1:
	    		break
		if count < 3000:			
			print(data.decode(), end='')
	
	print("\n\nTotal number of characters:",count)
	mysock.close()


except:
	print("Please enter a properly formatted or existant url.")