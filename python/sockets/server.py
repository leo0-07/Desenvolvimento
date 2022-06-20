# Echo server program
#!/usr/bin/env python
# encoding: utf-8
import socket

HOST = '192.168.1.101'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Conectado a:', addr)
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
