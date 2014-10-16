import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535

port = 5010

s.connect(('Andress-Air', port))
s.send('hello server this is a cient')
data = s.recv(MAX)
print( 'the server says', repr(data))


