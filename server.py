import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET is used to load family address and socket.stream is use to stream the data
host = socket.gethostname() #to get host name 
port = 4321 #To define port
s.bind((host,port))
s.listen()
print("Waiting for connection...")
while True: #for connecting to server
	cs,addr = s.accept() #to accept the connection from the client as we have only one client hence at print we use addr[0]
	print("Connecting received from",addr[0])
	msg = "Thankyou for connecting"
	cs.send(msg.encode("UTF")) #to encode msg Universal transfer function 
	while True: #to reply to connection
		msg2 = cs.recv(1024)
		print(msg2.decode("UTF-8"))
		msg1 = input()
		cs.send(msg1.encode("UTF-8"))