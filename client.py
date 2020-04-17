import socket
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4321
cs.connect((host, port))

data = cs.recv(1024) #TO RECEIVE DATA
print(data.decode("UTF-8"))

while True:
	msg1 = input()
	cs.send(msg1.encode("UTF-8"))

	msg2 = cs.recv(1024)
	print(msg2.decode("UTF-8"))