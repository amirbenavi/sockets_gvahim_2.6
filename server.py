import socket

def handle_welcome_res():
#msg has 281 bytes.
	msg = 'Hello, welcome to the server, you can do 4 commands,\nTIME - The server will give you the current time in the server location\nNAME - The server will give you the name of the server\nRAND - The server will send to you a generated number between 1-10\nEXIT - The server will log you out'
	byte_msg = msg.encode()
	return byte_msg

def handle_msg(msg):
	if msg.decode() == 'TIME':
		return 'time'
	elif msg.decode() == 'NAME':
		return 'Amir\'s server'
	elif msg.decode() == 'RAND':
		return '1'
	else:
		return 'dd'

def handle_respond(respond,client_socket):
	
	if respond == 'dd':
		client_socket.send('dd'.encode())
	else:
		for char in respond:
			client_socket.send(char.encode())
		client_socket.send('dd'.encode())

	





def main():
	
	IP = '0.0.0.0'
	PORT = 8282
	connection = True

	server_socket = socket.socket()
	server_socket.bind((IP,PORT))

	server_socket.listen(1)
	print(f'listening on IP: {IP} and PORT: {PORT} ')
	client_socket, client_address = server_socket.accept()
	print(f'client connected to the server on address: {client_address}')
# send client welcome msg	
	client_socket.send(handle_welcome_res())
	
	while connection:
		command = client_socket.recv(4)
		respond = handle_msg(command)
		handle_respond(respond,client_socket)
		if respond == 'dd':
			connection = False


# getting client's command

	client_socket.close()
	server_socket.close()



if __name__ == '__main__':
	main()

