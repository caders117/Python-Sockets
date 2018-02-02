import socket

s = socket.socket()
host = socket.gethostname();
port = 80
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    message = raw_input('Send what')
    c.sendto(message, addr)
    print c.recv(1024)
c.close()
