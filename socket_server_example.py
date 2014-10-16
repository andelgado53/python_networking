import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535

port = 5011

s.bind(('', port))


while True:
	print('Listenting at', s.getsockname())
	
	data, address = s.recvfrom(MAX)
	print('the client', address, 'said', repr(data))
	s.sendto('hello client', address)
	
