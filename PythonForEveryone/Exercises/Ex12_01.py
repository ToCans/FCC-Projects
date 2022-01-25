# Chapter 12 
# Exercise 1

import socket

try:
	url = input("Please enter the url:")
	host = url.split('/')[2]


	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect((host, 80))
	cmd = 'GET '+ url +' HTTP/1.0\r\n\r\n'
	cmd = cmd.encode()
	mysock.send(cmd)

	while True:
	    data = mysock.recv(512)
	    if len(data) < 1:
	        break
	    print(data.decode(),end='')

	mysock.close()
except:
	print("Please enter a properly formatted or existant url.")