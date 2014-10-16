import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535

port = 5011



if sys.argv[1:] == ['server']:
	s.bind(('', port))
	#delay = 10
	while True:
		#s.settimeout(delay)
		print('Listenting at', s.getsockname())
		data, address = s.recvfrom(MAX)
		# with open('test_data.txt') as f:
		# 	for line in f:
		# 		s.sendto(line.strip(), address)
		# 	print('transfer completed...')
		# 	print('port closed, goodbye...')
		# 	s.sendto('end', address)
		#break
		print('the client', address, 'said', repr(data))
		s.sendto('hello client', address)

elif sys.argv[1:] == ['client']:
	s.connect(('71.197.182.38', port))
	s.send('hello server. Can we try this?')
	delay = 0.2

	while  True:
		#s.settimeout(delay)
		data, address = s.recvfrom(MAX)
		if data == 'end':
			break
			
		else:
			print('the server', address, 'says', repr(data))
