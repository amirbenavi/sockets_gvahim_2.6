import socket

def handle_msg_protocol(client_socket):
	_buffer = 2
	msg = client_socket.recv(_buffer).decode()
	# print(f'msg: {msg}')
	server_msg = msg
	
	while msg != 'dd':
		msg = client_socket.recv(_buffer).decode()
		# print(f'msg: {msg}')
		
		if msg == 'dd':
			break
		server_msg += msg

	return server_msg

def main():

	IP = '127.0.0.1'
	PORT = 8282
	connection = True

	client_socket = socket.socket()
	client_socket.connect((IP,PORT))
	
	welcome_msg = client_socket.recv(281).decode()
	print(welcome_msg)

	while connection:

		command = input('enter a command ')
		if command.upper() == 'TIME' or command.upper() == 'NAME' or command.upper() == 'RAND' or command.upper() == 'EXIT':
			client_socket.send(command.encode())
			server_msg = handle_msg_protocol(client_socket)
			if server_msg == 'dd':
				break
			print(server_msg)
			continue
		print('bad command, please enter one of the following commands: TIME, NAME, RAND, EXIT')






if __name__ == '__main__':
	main()

