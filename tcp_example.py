import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8000
MAX = 4000

def recv_all(sock, lenght):
	data = ''
	while len(data) < lenght:
		more = sock.recv(lenght - len(data))
		if not more:
			raise EOFError
		data = data + more 
	return data

if sys.argv[1:] == ['server']:
	
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(('', PORT))
	s.listen(1)

	while True:
		print('port listening at ', s.getsockname())
		sc, sockname = s.accept()
		print('connection accepted with', sockname)
		message =  sc.recv(MAX) #recv_all(sc, 8)
		print('the client says', repr(message))
		sc.sendall('thank you client')
		sc.close()
		print('sock close')

else:

	s.connect(('10.57.40.108', PORT))
	print('conecting with server')
	s.sendall('hi server, let me connect')
	message = s.recv(MAX) # recv_all(s, 8)
	print('the server says', message)
	s.close()




