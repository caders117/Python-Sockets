import socket

s = socket.socket()
host = '192.168.2.130'
port = 90

s.connect((host, port))

while True:
    message = raw_input('what u wan sent')
    s.send(message)
    print s.recv(1024)
s.close
